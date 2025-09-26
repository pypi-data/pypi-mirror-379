# supertable/mirroring/mirror_delta.py
"""
Delta Lake mirror — Spark-compatible layout (with `data/` folder) and
newline-delimited JSON actions that match the user's working example.

Final on-disk layout (for table <org>/<super>/delta/<table_name>):
  data/
    part-00000-<uuid>-c000.snappy.parquet
    _delta_log/
      00000000000000000000.json
      00000000000000000001.json
      ...

Key points implemented:
- Files and _delta_log live under a `data/` directory (not at table root).
- Log file orders actions as Spark does: commitInfo, protocol, metaData, remove*, add*.
- protocol: {"minReaderVersion":1,"minWriterVersion":4}
- commitInfo:
    operation="WRITE"; operationParameters.mode="Overwrite"; isolationLevel="Serializable"
    isBlindAppend=false; engineInfo="supertable-delta/1.0"; txnId=<uuid>
    operationMetrics: "numFiles", "numOutputRows" (if derivable), "numOutputBytes" (strings)
- metaData:
    id = stable UUID per-table (persists across commits)
    format = parquet; schemaString = Spark JSON schema inferred from simple schema
    partitionColumns = []; configuration includes CDF + autoOptimize flags
    createdTime = commit time (ms)
- add:
    path = relative file name (part-00000-<uuid>-c000.snappy.parquet)
    partitionValues = {}; size; modificationTime; dataChange=true; tags={}
    stats = compact JSON string if available (numRecords/min/max/nullCount)
- remove:
    Emitted for any files referenced by previous snapshot but not in current snapshot.
- Cleanup:
    Removes any *.parquet under `data/` that are not referenced by the latest commit.
- Robustness:
    If an existing _delta_log is found but its latest JSON lacks a protocol/metaData,
    we auto-reset the log directory to start fresh at version 0 (prevents Synapse error).

`simple_snapshot` contract (input):
{
  "schema": [{"name": str, "type": str}, ...],
  "resources": [{"file": "<abs path to parquet>", "file_size": int}, ...]
}

Storage interface must provide:
- exists(path) -> bool
- makedirs(path) -> None
- listdir(path) -> List[str]
- read_bytes(path) -> bytes
- write_bytes(path, data: bytes) -> None
- remove(path) -> None
- copy(src, dst) -> None   (optional but preferred)
- Optional: stat(path) -> { "size": int } or object with .size
"""

from __future__ import annotations

import io
import json
import os
import uuid
import hashlib
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set, Tuple

from supertable.config.defaults import logger

# ---------------------------------------------------------------------------

DATA_DIR_NAME = "data"
DELTA_LOG_DIR_NAME = "_delta_log"

# ---------------------------------------------------------------------------


def _now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def _pad_version(v: int) -> str:
    return f"{int(v):020d}"


def _spark_field_for_type(t: str) -> Dict[str, Any]:
    t = (t or "").strip().lower()
    if t in {"string", "str", "varchar", "text"}:
        typ = "string"
    elif t in {"int", "integer", "int32", "int64", "bigint", "long"}:
        typ = "integer"
    elif t in {"double", "float", "real", "numeric", "decimal"}:
        typ = "double"
    elif t in {"bool", "boolean"}:
        typ = "boolean"
    elif t in {"timestamp", "datetime"}:
        typ = "timestamp"
    elif t in {"date"}:
        typ = "date"
    else:
        typ = "string"
    return {"type": typ, "nullable": True, "metadata": {}}


def _schema_to_spark_json(schema: Any) -> str:
    fields: List[Dict[str, Any]] = []
    if isinstance(schema, list):
        for col in schema:
            if not isinstance(col, dict):
                continue
            name = col.get("name")
            if not name:
                continue
            fd = _spark_field_for_type(col.get("type"))
            fd["name"] = name
            fields.append(fd)
    return json.dumps({"type": "struct", "fields": fields}, separators=(",", ":"))


def _list_json_versions(storage, log_dir: str) -> List[int]:
    try:
        files = storage.listdir(log_dir)
    except Exception:
        return []
    out: List[int] = []
    for f in files:
        name = os.path.basename(f)
        if not name.endswith(".json"):
            continue
        try:
            out.append(int(name.replace(".json", "")))
        except Exception:
            pass
    return sorted(out)


def _read_actions(storage, json_path: str) -> List[Dict[str, Any]]:
    if not storage.exists(json_path):
        return []
    try:
        lines = storage.read_bytes(json_path).decode("utf-8").splitlines()
        return [json.loads(ln) for ln in lines if ln.strip()]
    except Exception as e:
        logger.warning(f"[mirror][delta] failed to parse actions from {json_path}: {e}")
        return []


def _extract_prev_state(storage, log_dir: str) -> Tuple[int, Set[str], Optional[str], bool]:
    """
    Return (last_version, prev_paths, table_id, looks_valid).
    looks_valid = True only if last commit has both protocol and metaData actions.
    """
    versions = _list_json_versions(storage, log_dir)
    if not versions:
        return -1, set(), None, True
    last_v = versions[-1]
    actions = _read_actions(storage, os.path.join(log_dir, f"{_pad_version(last_v)}.json"))
    has_protocol = any("protocol" in a for a in actions)
    table_id = None
    prev_paths: Set[str] = set()
    for a in actions:
        if "metaData" in a and not table_id:
            table_id = a["metaData"].get("id")
        if "add" in a:
            path = a["add"].get("path")
            if path:
                prev_paths.add(path)
    return last_v, prev_paths, table_id, bool(has_protocol and table_id)


def _reset_log_dir(storage, log_dir: str) -> None:
    """
    Remove all *.json and *.checkpoint.parquet files from the _delta_log directory.
    """
    try:
        items = storage.listdir(log_dir)
    except Exception:
        return
    for it in items:
        name = os.path.basename(it)
        if name.endswith(".json") or name.endswith(".checkpoint.parquet"):
            try:
                storage.remove(os.path.join(log_dir, name))
            except Exception:
                pass


def _stable_part_name(src_path: str) -> str:
    """
    Build Spark-like data filename:
      part-00000-<uuid>-c000.snappy.parquet
    UUID derived deterministically from src path to keep name stable for the same input.
    """
    h = hashlib.md5(src_path.encode("utf-8")).hexdigest()
    u = uuid.UUID(h)  # type: ignore[arg-type]
    return f"part-00000-{str(u)}-c000.snappy.parquet"


def _copy_into(storage, src_path: str, dst_path: str) -> None:
    if hasattr(storage, "copy"):
        storage.makedirs(os.path.dirname(dst_path))
        storage.copy(src_path, dst_path)
        return
    data = storage.read_bytes(src_path)
    storage.makedirs(os.path.dirname(dst_path))
    storage.write_bytes(dst_path, data)


def _safe_filesize(storage, path: str) -> int:
    try:
        if hasattr(storage, "stat"):
            st = storage.stat(path)  # type: ignore[attr-defined]
            size = getattr(st, "size", None)
            if size is None and isinstance(st, dict):
                size = st.get("size")
            if isinstance(size, int) and size >= 0:
                return size
    except Exception:
        pass
    try:
        return len(storage.read_bytes(path))
    except Exception:
        return 0


def _compute_stats_if_possible(full_dst_path: str) -> Tuple[Optional[Dict[str, Any]], Optional[int]]:
    """
    Returns (stats_dict_or_None, num_rows_or_None)
    stats schema matches Spark Delta (numRecords/minValues/maxValues/nullCount).
    """
    try:
        import pyarrow.parquet as pq  # type: ignore
    except Exception:
        return None, None

    try:
        pf = pq.ParquetFile(full_dst_path)
        md = pf.metadata
        num_rows = int(md.num_rows or 0)

        min_values: Dict[str, Any] = {}
        max_values: Dict[str, Any] = {}
        null_count: Dict[str, int] = {}

        for i in range(md.num_row_groups):
            rg = md.row_group(i)
            for j in range(rg.num_columns):
                col = rg.column(j)
                name = col.path_in_schema
                st = col.statistics
                # nulls
                if st is not None and st.null_count is not None:
                    null_count[name] = null_count.get(name, 0) + int(st.null_count)
                # min/max
                if st is not None and st.has_min_max:
                    cmin = st.min
                    cmax = st.max
                    if isinstance(cmin, (bytes, bytearray)):
                        try:
                            cmin = cmin.decode("utf-8", errors="ignore")
                        except Exception:
                            cmin = None
                    if isinstance(cmax, (bytes, bytearray)):
                        try:
                            cmax = cmax.decode("utf-8", errors="ignore")
                        except Exception:
                            cmax = None
                    # merge
                    if name not in min_values or (cmin is not None and min_values[name] is not None and cmin < min_values[name]):
                        min_values.setdefault(name, cmin)
                        if cmin is not None and min_values[name] is not None and cmin < min_values[name]:
                            min_values[name] = cmin
                    if name not in max_values or (cmax is not None and max_values[name] is not None and cmax > max_values[name]):
                        max_values.setdefault(name, cmax)
                        if cmax is not None and max_values[name] is not None and cmax > max_values[name]:
                            max_values[name] = cmax

        stats: Dict[str, Any] = {"numRecords": num_rows}
        if min_values:
            stats["minValues"] = min_values
        if max_values:
            stats["maxValues"] = max_values
        if null_count:
            stats["nullCount"] = {k: int(v) for k, v in null_count.items()}

        return stats, num_rows
    except Exception as e:
        logger.warning(f"[mirror][delta] stats failed for {full_dst_path}: {e}")
        return None, None


def _cleanup_unreferenced_parquet(storage, data_dir: str, keep_relative: Set[str]) -> None:
    try:
        items = storage.listdir(data_dir)
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup listdir failed: {e}")
        return

    keep_names = {os.path.basename(p) for p in keep_relative}
    for it in items:
        name = os.path.basename(it)
        if name == DELTA_LOG_DIR_NAME:
            continue
        if not name.lower().endswith(".parquet"):
            continue
        if name not in keep_names:
            try:
                storage.remove(os.path.join(data_dir, name))
                logger.info(f"[mirror][delta] removed stale data file: {name}")
            except Exception as ex:
                logger.warning(f"[mirror][delta] failed to remove {name}: {ex}")


# ---------------------------------------------------------------------------


def write_delta_table(super_table, table_name: str, simple_snapshot: Dict[str, Any]) -> None:
    """
    Mirror the `simple_snapshot` into a Delta table at:
      <org>/<super>/delta/<table_name>/data/
    """
    table_root = os.path.join(super_table.organization, super_table.super_name, "delta", table_name)
    data_dir = os.path.join(table_root, DATA_DIR_NAME)
    log_dir = os.path.join(data_dir, DELTA_LOG_DIR_NAME)
    storage = super_table.storage

    storage.makedirs(log_dir)

    # Determine previous state from _delta_log
    prev_version, prev_paths, prev_table_id, looks_valid = _extract_prev_state(storage, log_dir)
    if not looks_valid:
        logger.warning(f"[mirror][delta] Detected invalid/incomplete log at {log_dir}; resetting.")
        _reset_log_dir(storage, log_dir)
        prev_version, prev_paths, prev_table_id, _ = -1, set(), None, True

    version = prev_version + 1  # first proper commit will be 0
    table_id = prev_table_id or str(uuid.uuid4())

    # Collect resources -> copy into data_dir and prepare add actions
    schema_any = simple_snapshot.get("schema", [])
    resources: List[Dict[str, Any]] = list(simple_snapshot.get("resources", []))

    current_rel_paths: List[str] = []
    add_entries: List[Tuple[str, int, Optional[Dict[str, Any]], Optional[int]]] = []  # (rel_path, size, stats, num_rows)

    for r in resources:
        src_path = r["file"]
        rel_name = _stable_part_name(src_path)
        dst_full = os.path.join(data_dir, rel_name)
        _copy_into(storage, src_path, dst_full)

        # file size
        size = int(r.get("file_size") or 0)
        if size <= 0:
            size = _safe_filesize(storage, dst_full)

        # optional stats
        stats_obj, num_rows = _compute_stats_if_possible(dst_full)

        current_rel_paths.append(rel_name)
        add_entries.append((rel_name, size, stats_obj, num_rows))

    current_set = set(current_rel_paths)
    to_remove = sorted(list(prev_paths - current_set))

    # operation metrics
    num_files_str = str(len(add_entries))
    total_bytes_str = str(sum(int(sz) for _, sz, __, ___ in add_entries))
    # If we have per-file row counts, sum them; else omit to match Spark behavior when unknown
    rows_known = all(nr is not None for *_, nr in add_entries) and len(add_entries) > 0
    num_rows_str = str(sum(int(nr or 0) for *_, nr in add_entries)) if rows_known else None

    # Build log file content (exact order)
    commit_path = os.path.join(log_dir, f"{_pad_version(version)}.json")
    with io.StringIO() as buf:
        now_ms = _now_ms()

        # 1) commitInfo
        commit_info = {
            "commitInfo": {
                "timestamp": now_ms,
                "operation": "WRITE",
                "operationParameters": {"mode": "Overwrite", "partitionBy": "[]"},
                "isolationLevel": "Serializable",
                "isBlindAppend": False,
                "operationMetrics": {
                    "numFiles": num_files_str,
                    "numOutputBytes": total_bytes_str,
                },
                "engineInfo": "supertable-delta/1.0",
                "txnId": str(uuid.uuid4()),
            }
        }
        if num_rows_str is not None:
            commit_info["commitInfo"]["operationMetrics"]["numOutputRows"] = num_rows_str

        buf.write(json.dumps(commit_info, separators=(",", ":")) + "\n")

        # 2) protocol
        buf.write(json.dumps({"protocol": {"minReaderVersion": 1, "minWriterVersion": 4}},
                             separators=(",", ":")) + "\n")

        # 3) metaData
        meta = {
            "metaData": {
                "id": table_id,
                "format": {"provider": "parquet", "options": {}},
                "schemaString": _schema_to_spark_json(schema_any),
                "partitionColumns": [],
                "configuration": {
                    "delta.enableChangeDataFeed": "true",
                    "delta.autoOptimize.optimizeWrite": "true",
                    "delta.autoOptimize.autoCompact": "true",
                },
                "createdTime": now_ms,
            }
        }
        buf.write(json.dumps(meta, separators=(",", ":")) + "\n")

        # 4) remove old files
        remove_ts = _now_ms()
        for p in to_remove:
            buf.write(json.dumps({"remove": {"path": p, "deletionTimestamp": remove_ts, "dataChange": True}},
                                 separators=(",", ":")) + "\n")

        # 5) add current files
        add_ts = _now_ms()
        for rel_path, size, stats_obj, _nr in add_entries:
            add = {
                "add": {
                    "path": rel_path,
                    "partitionValues": {},
                    "size": int(size),
                    "modificationTime": add_ts,
                    "dataChange": True,
                    "tags": {},
                }
            }
            if stats_obj is not None:
                add["add"]["stats"] = json.dumps(stats_obj, separators=(",", ":"))
            buf.write(json.dumps(add, separators=(",", ":")) + "\n")

        storage.write_bytes(commit_path, buf.getvalue().encode("utf-8"))

    # Cleanup: keep only referenced parquet files inside data_dir
    try:
        _cleanup_unreferenced_parquet(storage, data_dir, set(current_rel_paths))
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup skipped: {e}")

    logger.info(
        f"[mirror][delta] wrote {_pad_version(version)}.json (add={len(add_entries)}, remove={len(to_remove)}) at {log_dir}"
    )

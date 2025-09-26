# supertable/mirroring/mirror_delta.py
"""
Delta Lake mirror (Spark-compatible layout and actions).

This writer produces a Delta table that matches the structure you described:

<org>/<super>/delta/<table>/data/
  ├── part-00000-<uuid>-c000.snappy.parquet
  └── _delta_log/
        └── 00000000000000000000.json    (newline-delimited JSON actions)

Key details replicated:
- Data files live under a 'data' subfolder of the table and use Spark-like names:
    part-00000-<uuid>-c000.snappy.parquet
- Log is under 'data/_delta_log' with zero-padded version files.
- Each commit uses actions in this exact order:
    commitInfo, protocol, metaData, (remove*), add*
- commitInfo includes:
    operation = "WRITE"
    operationParameters.mode = "Overwrite"
    isolationLevel = "Serializable"
    isBlindAppend = false
    engineInfo = "supertable-delta/1.0"   (string is informational)
    operationMetrics: numFiles, numOutputBytes (as strings)
- protocol: minReaderVersion=1, minWriterVersion=4
- metaData:
    id: stable UUID per table (persisted across commits)
    format: parquet
    schemaString: Spark JSON schema derived from simple schema
    partitionColumns: [] (unpartitioned)
    configuration: CDF/autoOptimize flags to match your example
    createdTime: commit time (ms)
- add:
    path: relative file name (part-00000-<uuid>-c000.snappy.parquet)
    partitionValues: {}
    size, modificationTime, dataChange, tags
    stats: included if pyarrow is available (row count, min/max/nullCount)

Also:
- Cleans up any *.parquet under 'data/' that are not referenced by the latest commit.
- Does NOT write any auxiliary 'latest.json'—only _delta_log and data files.

Expected 'simple_snapshot' shape:
{
  "schema": [{"name": "...", "type": "..."}, ...],
  "resources": [{"file": "<abs/path/to/source.parquet>", "file_size": <int>}, ...],
  # optional: "snapshot_version": int  (ignored; we derive version from _delta_log)
}

Storage interface is expected to provide:
- exists(path) -> bool
- makedirs(path) -> None
- listdir(path) -> List[str]           (returns full paths or names)
- read_bytes(path) -> bytes
- write_bytes(path, data: bytes) -> None
- remove(path) -> None
- copy(src, dst) -> None                (optional optimization)
"""

from __future__ import annotations

import io
import json
import os
import uuid
import hashlib
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from supertable.config.defaults import logger


# ----------------------------- Constants -------------------------------------

DATA_DIR_NAME = "data"
DELTA_LOG_DIR_NAME = "_delta_log"

# ----------------------------- Helpers ---------------------------------------


def _pad_version(version: int) -> str:
    return f"{int(version):020d}"


def _now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


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


def _schema_to_spark_json(schema_any: Any) -> str:
    fields: List[Dict[str, Any]] = []
    if isinstance(schema_any, list):
        for col in schema_any:
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
        items = storage.listdir(log_dir)
    except Exception:
        return []
    versions: List[int] = []
    for it in items:
        name = os.path.basename(it)
        if not name.endswith(".json"):
            continue
        try:
            versions.append(int(name.replace(".json", "")))
        except Exception:
            continue
    return sorted(versions)


def _read_last_commit_actions(storage, log_dir: str, version: int) -> List[Dict[str, Any]]:
    """
    Return list of per-line JSON action dicts from version file, or [] if missing.
    """
    path = os.path.join(log_dir, f"{_pad_version(version)}.json")
    if not storage.exists(path):
        return []
    try:
        data = storage.read_bytes(path).decode("utf-8").splitlines()
        actions: List[Dict[str, Any]] = []
        for line in data:
            line = line.strip()
            if not line:
                continue
            actions.append(json.loads(line))
        return actions
    except Exception as e:
        logger.warning(f"[mirror][delta] failed reading commit {path}: {e}")
        return []


def _extract_prev_state(storage, log_dir: str) -> Tuple[int, Set[str], Optional[str]]:
    """
    Inspect the latest JSON in _delta_log to get:
      - previous version number
      - set of previously referenced relative data paths
      - table id (if present in metaData)
    Returns (-1, set(), None) if there is no previous commit.
    """
    versions = _list_json_versions(storage, log_dir)
    if not versions:
        return -1, set(), None
    last_v = versions[-1]
    actions = _read_last_commit_actions(storage, log_dir, last_v)
    prev_paths: Set[str] = set()
    table_id: Optional[str] = None
    for act in actions:
        if "add" in act:
            p = act["add"].get("path")
            if p:
                prev_paths.add(p)
        elif "metaData" in act and not table_id:
            table_id = act["metaData"].get("id")
    return last_v, prev_paths, table_id


def _stable_part_name_from_src(src_path: str) -> str:
    """
    Produce a Spark-like data filename:
      part-00000-<uuid>-c000.snappy.parquet
    We derive <uuid> deterministically from the source path so repeated mirroring
    of the same single-file snapshot produces a stable name; if you prefer a
    fresh UUID every commit, replace with uuid.uuid4().
    """
    h = hashlib.md5(src_path.encode("utf-8")).hexdigest()
    u = uuid.UUID(h)  # type: ignore[arg-type]
    return f"part-00000-{str(u)}-c000.snappy.parquet"


def _copy_into_table_dir(storage, src_path: str, dst_path: str) -> None:
    # Prefer native copy when available
    if hasattr(storage, "copy"):
        storage.makedirs(os.path.dirname(dst_path))
        storage.copy(src_path, dst_path)
        return
    # Fallback to bytes roundtrip
    data = storage.read_bytes(src_path)
    storage.makedirs(os.path.dirname(dst_path))
    storage.write_bytes(dst_path, data)


def _compute_stats_if_possible(full_dst_path: str) -> Optional[Dict[str, Any]]:
    """
    Try to compute Delta 'stats' for the single Parquet file using pyarrow.
    Returns a dict (to be json-dumped) or None if unavailable.
    Structure mirrors Spark's stats:
      {
        "numRecords": <int>,
        "minValues": {col: <min>},
        "maxValues": {col: <max>},
        "nullCount": {col: <int>}
      }
    """
    try:
        import pyarrow.parquet as pq  # type: ignore
        import pyarrow as pa  # type: ignore
    except Exception:
        return None

    try:
        pf = pq.ParquetFile(full_dst_path)
        md = pf.metadata
        num_rows = md.num_rows or 0

        # Aggregate column stats across row groups
        min_values: Dict[str, Any] = {}
        max_values: Dict[str, Any] = {}
        null_counts: Dict[str, int] = {}

        for i in range(md.num_row_groups):
            rg = md.row_group(i)
            for j in range(rg.num_columns):
                col_chunk = rg.column(j)
                name = col_chunk.path_in_schema
                # Nulls
                nc = col_chunk.statistics.null_count if col_chunk.statistics else 0
                null_counts[name] = null_counts.get(name, 0) + (nc or 0)

                if col_chunk.statistics and col_chunk.statistics.has_min_max:
                    cmin = col_chunk.statistics.min
                    cmax = col_chunk.statistics.max
                    # Normalize bytes to str for JSON
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

                    # First occurrence
                    if name not in min_values:
                        min_values[name] = cmin
                        max_values[name] = cmax
                    else:
                        # Merge across row groups
                        try:
                            if cmin is not None and (min_values[name] is None or cmin < min_values[name]):
                                min_values[name] = cmin
                            if cmax is not None and (max_values[name] is None or cmax > max_values[name]):
                                max_values[name] = cmax
                        except Exception:
                            # Fallback: keep first if incomparable
                            pass

        # If no stats, return None to avoid writing empty object
        if not (min_values or max_values or null_counts):
            return {"numRecords": int(num_rows)}

        return {
            "numRecords": int(num_rows),
            "minValues": min_values,
            "maxValues": max_values,
            "nullCount": {k: int(v) for k, v in null_counts.items()},
        }
    except Exception as e:
        logger.warning(f"[mirror][delta] stats computation failed for {full_dst_path}: {e}")
        return None


def _cleanup_unreferenced_parquet(storage, data_dir: str, keep_relative: Set[str]) -> None:
    """
    Remove *.parquet in data_dir that are not referenced by the latest commit.
    Do not touch the _delta_log folder.
    """
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


# ----------------------------- Main entry ------------------------------------


def write_delta_table(super_table, table_name: str, simple_snapshot: Dict[str, Any]) -> None:
    """
    Produce a Spark-compatible Delta table under:
      <org>/<super>/delta/<table>/data/
    """
    # Layout
    table_root = os.path.join(super_table.organization, super_table.super_name, "delta", table_name)
    data_dir = os.path.join(table_root, DATA_DIR_NAME)
    log_dir = os.path.join(data_dir, DELTA_LOG_DIR_NAME)
    storage = super_table.storage

    storage.makedirs(log_dir)

    # Determine previous state purely from _delta_log
    prev_version, prev_paths, prev_table_id = _extract_prev_state(storage, log_dir)
    version = prev_version + 1  # first commit -> 0
    table_id = prev_table_id or str(uuid.uuid4())

    schema_any = simple_snapshot.get("schema", [])
    resources: List[Dict[str, Any]] = list(simple_snapshot.get("resources", []))

    # For now we assume latest-only snapshot with 0 or 1 data files.
    # If multiple files appear, we mirror them all.
    current_rel_paths: List[str] = []
    add_records: List[Tuple[str, int, Optional[Dict[str, Any]]]] = []  # (rel_path, size, stats)

    for r in resources:
        src_path = r["file"]
        size = int(r.get("file_size", 0))

        # Build destination name and copy into data directory
        rel_name = _stable_part_name_from_src(src_path)
        dst_full = os.path.join(data_dir, rel_name)
        _copy_into_table_dir(storage, src_path, dst_full)
        current_rel_paths.append(rel_name)

        stats_obj = _compute_stats_if_possible(dst_full)  # optional
        add_records.append((rel_name, size if size > 0 else _safe_filesize(storage, dst_full), stats_obj))

    current_set = set(current_rel_paths)
    to_remove = sorted(list(prev_paths - current_set))

    # Aggregate operation metrics
    num_files = str(len(add_records))
    total_bytes = str(sum(int(sz) for _, sz, __ in add_records))

    # Compose the Delta log (newline-delimited actions, exact order)
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
                    "numFiles": num_files,
                    "numOutputBytes": total_bytes
                    # "numOutputRows" intentionally omitted unless stats is computed comprehensively
                },
                "engineInfo": "supertable-delta/1.0",
                "txnId": str(uuid.uuid4()),
            }
        }
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

        # 4) remove (for files no longer present)
        remove_ts = _now_ms()
        for p in to_remove:
            buf.write(json.dumps({"remove": {"path": p, "deletionTimestamp": remove_ts, "dataChange": True}},
                                 separators=(",", ":")) + "\n")

        # 5) add (for current files)
        add_ts = _now_ms()
        for rel_path, size, stats_obj in add_records:
            add_entry: Dict[str, Any] = {
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
                # Encode stats as compact JSON string, like Spark does
                add_entry["add"]["stats"] = json.dumps(stats_obj, separators=(",", ":"))
            buf.write(json.dumps(add_entry, separators=(",", ":")) + "\n")

        storage.write_bytes(commit_path, buf.getvalue().encode("utf-8"))

    # Cleanup unreferenced data files
    try:
        _cleanup_unreferenced_parquet(storage, data_dir, set(current_rel_paths))
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup skipped: {e}")

    logger.info(
        f"[mirror][delta] wrote {_pad_version(version)}.json in {log_dir} "
        f"(add={len(add_records)}, remove={len(to_remove)})"
    )


def _safe_filesize(storage, path: str) -> int:
    """
    Last-resort size discovery if resource file_size was 0/absent.
    Storage implementations often expose stat; if not, read bytes length.
    """
    try:
        if hasattr(storage, "stat"):
            st = storage.stat(path)  # type: ignore[attr-defined]
            # st may be dict or object; try common shapes
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

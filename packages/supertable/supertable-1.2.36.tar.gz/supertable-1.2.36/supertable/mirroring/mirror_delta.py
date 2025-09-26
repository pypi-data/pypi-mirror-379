# supertable/mirroring/mirror_delta.py
"""
Delta Lake mirror — Spark-compatible layout with `data/` folder and
newline-delimited JSON actions, matching your working example.

Final on-disk layout for a table at <org>/<super>/delta/<table_name>:
  data/
    part-00000-<uuid>-c000.snappy.parquet
    _delta_log/
      00000000000000000000.json
      00000000000000000001.json
      ...

Why this version:
- Writes the Delta transaction log under `data/_delta_log` (NOT at table root).
- Copies data files into `data/` with Spark-like names: part-00000-<uuid>-c000.snappy.parquet
- JSON log action order: commitInfo, protocol, metaData, remove*, add*
- protocol: {"minReaderVersion":1,"minWriterVersion":4}
- commitInfo: operation="WRITE", mode="Overwrite", isolationLevel="Serializable",
  isBlindAppend=false, engineInfo="supertable-delta/1.0", txnId=<uuid>,
  operationMetrics: "numFiles", "numOutputBytes" (+ "numOutputRows" when available)
- metaData: stable table id, parquet format, Spark schema JSON, no partitions,
  and config flags (CDF + autoOptimize)
- add: includes stats as a compact JSON string if PyArrow can read them
- Robust to backends lacking listdir/copy/stat; will skip cleanup safely
- Avoids emitting a commit when we have zero data files (prevents half-baked logs)
- Resets an invalid/incomplete _delta_log (missing protocol/metaData) before writing v0

Input `simple_snapshot` contract:
{
  "schema": [{"name": str, "type": str}, ...],
  "resources": [{"file": "<abs path to parquet>", "file_size": int}, ...]
}

Storage interface expectations (feature-detected where optional):
- exists(path) -> bool
- makedirs(path) -> None
- read_bytes(path) -> bytes
- write_bytes(path, data: bytes) -> None
- remove(path) -> None
- (optional) listdir(path) -> List[str]
- (optional) copy(src, dst) -> None
- (optional) stat(path) -> object/dict with 'size'
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

# Fallback: if the storage backend can't read a given source path, try local FS.
COPY_FROM_LOCAL_FS_IF_MISSING_IN_STORAGE = True


# --------------------------- small utils -------------------------------------

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


# ------------------------ storage wrappers -----------------------------------

def _st_exists(st, path: str) -> bool:
    try:
        return bool(st.exists(path))
    except Exception:
        return False


def _st_makedirs(st, path: str) -> None:
    try:
        st.makedirs(path)
    except Exception:
        pass


def _st_listdir(st, path: str) -> List[str]:
    # best-effort directory listing (optional)
    try:
        if hasattr(st, "listdir"):
            return list(st.listdir(path))  # type: ignore
    except Exception:
        pass
    try:
        if hasattr(st, "list"):
            return list(st.list(path))  # type: ignore
    except Exception:
        pass
    try:
        if hasattr(st, "iterdir"):
            return [p for p in st.iterdir(path)]  # type: ignore
    except Exception:
        pass
    return []


def _st_remove(st, path: str) -> None:
    try:
        st.remove(path)
    except Exception:
        pass


def _st_read_bytes(st, path: str) -> Optional[bytes]:
    try:
        return st.read_bytes(path)
    except Exception:
        return None


def _st_write_bytes(st, path: str, data: bytes) -> None:
    _st_makedirs(st, os.path.dirname(path))
    st.write_bytes(path, data)


def _st_copy(st, src: str, dst: str) -> bool:
    try:
        if hasattr(st, "copy"):
            _st_makedirs(st, os.path.dirname(dst))
            st.copy(src, dst)  # type: ignore
            return True
    except Exception:
        pass
    return False


def _st_stat_size(st, path: str) -> Optional[int]:
    try:
        if hasattr(st, "stat"):
            s = st.stat(path)  # type: ignore
            size = getattr(s, "size", None)
            if size is None and isinstance(s, dict):
                size = s.get("size")
            if isinstance(size, int) and size >= 0:
                return size
    except Exception:
        pass
    return None


# --------------------------- delta helpers -----------------------------------

def _list_json_versions(storage, log_dir: str) -> List[int]:
    files = _st_listdir(storage, log_dir)
    out: List[int] = []
    for f in files:
        name = os.path.basename(f)
        if name.endswith(".json"):
            try:
                out.append(int(name[:-5]))
            except Exception:
                pass
    return sorted(out)


def _read_actions(storage, json_path: str) -> List[Dict[str, Any]]:
    if not _st_exists(storage, json_path):
        return []
    try:
        raw = _st_read_bytes(storage, json_path)
        if raw is None:
            return []
        return [json.loads(ln) for ln in raw.decode("utf-8").splitlines() if ln.strip()]
    except Exception as e:
        logger.warning(f"[mirror][delta] failed to read actions from {json_path}: {e}")
        return []


def _extract_prev_state(storage, log_dir: str) -> Tuple[int, Set[str], Optional[str], bool]:
    """
    Return (last_version, prev_paths, table_id, looks_valid).
    looks_valid True only if last commit has both protocol and metaData.
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
            p = a["add"].get("path")
            if p:
                prev_paths.add(p)
    return last_v, prev_paths, table_id, bool(has_protocol and table_id)


def _reset_log_dir(storage, log_dir: str) -> None:
    for it in _st_listdir(storage, log_dir):
        name = os.path.basename(it)
        if name.endswith(".json") or name.endswith(".checkpoint.parquet"):
            _st_remove(storage, os.path.join(log_dir, name))


def _stable_part_name(src_path: str) -> str:
    """
    Spark-like filename:
      part-00000-<uuid>-c000.snappy.parquet
    UUID derived deterministically from src path for stability.
    """
    h = hashlib.md5(src_path.encode("utf-8")).hexdigest()
    u = uuid.UUID(h)  # type: ignore[arg-type]
    return f"part-00000-{str(u)}-c000.snappy.parquet"


def _copy_into(storage, src_path: str, dst_full: str) -> bool:
    """
    Copy bytes from storage (or local FS fallback) into destination in storage.
    Returns True if successful.
    """
    # Prefer storage-native copy when possible
    if _st_copy(storage, src_path, dst_full):
        return True

    # Read from storage
    data = _st_read_bytes(storage, src_path)
    if data is None and COPY_FROM_LOCAL_FS_IF_MISSING_IN_STORAGE:
        # Local FS fallback
        try:
            with open(src_path, "rb") as fh:
                data = fh.read()
        except Exception as e:
            logger.warning(f"[mirror][delta] could not read source file: {src_path} ({e})")
            return False

    if data is None:
        logger.warning(f"[mirror][delta] source not found: {src_path}")
        return False

    _st_write_bytes(storage, dst_full, data)
    return True


def _safe_filesize(storage, path: str) -> int:
    size = _st_stat_size(storage, path)
    if isinstance(size, int) and size >= 0:
        return size
    data = _st_read_bytes(storage, path)
    return len(data) if data is not None else 0


def _compute_stats_if_possible(storage, full_dst_path: str) -> Tuple[Optional[Dict[str, Any]], Optional[int]]:
    """
    Returns (stats_dict_or_None, num_rows_or_None).
    """
    try:
        import pyarrow.parquet as pq  # type: ignore
    except Exception:
        return None, None

    data = _st_read_bytes(storage, full_dst_path)
    if data is None:
        return None, None

    try:
        import io as _io  # avoid shadowing main io
        pf = pq.ParquetFile(_io.BytesIO(data))
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
                if st is None:
                    continue
                if st.null_count is not None:
                    null_count[name] = null_count.get(name, 0) + int(st.null_count)
                if st.has_min_max:
                    cmin, cmax = st.min, st.max
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
                    if name not in min_values or (cmin is not None and min_values[name] is not None and cmin < min_values[name]):
                        min_values[name] = cmin
                    if name not in max_values or (cmax is not None and max_values[name] is not None and cmax > max_values[name]):
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
        logger.warning(f"[mirror][delta] stats read failed for {full_dst_path}: {e}")
        return None, None


def _cleanup_unreferenced_parquet(storage, data_dir: str, keep_relative: Set[str]) -> None:
    """
    If storage cannot list directories, skip cleanup silently (no error).
    """
    items = _st_listdir(storage, data_dir)
    if not items:
        return

    keep_names = {os.path.basename(p) for p in keep_relative}
    for it in items:
        name = os.path.basename(it)
        if name == DELTA_LOG_DIR_NAME:
            continue
        if not name.lower().endswith(".parquet"):
            continue
        if name not in keep_names:
            _st_remove(storage, os.path.join(data_dir, name))
            logger.info(f"[mirror][delta] removed stale data file: {name}")


# ----------------------------- main entry ------------------------------------

def write_delta_table(super_table, table_name: str, simple_snapshot: Dict[str, Any]) -> None:
    """
    Mirror `simple_snapshot` into a Delta table at:
      <org>/<super>/delta/<table_name>/data/
    """
    table_root = os.path.join(super_table.organization, super_table.super_name, "delta", table_name)
    data_dir = os.path.join(table_root, DATA_DIR_NAME)
    log_dir = os.path.join(data_dir, DELTA_LOG_DIR_NAME)
    storage = super_table.storage

    _st_makedirs(storage, log_dir)

    # Determine previous state from _delta_log
    prev_version, prev_paths, prev_table_id, looks_valid = _extract_prev_state(storage, log_dir)
    if not looks_valid:
        logger.warning(f"[mirror][delta] Detected invalid/incomplete log at {log_dir}; resetting.")
        _reset_log_dir(storage, log_dir)
        prev_version, prev_paths, prev_table_id, _ = -1, set(), None, True

    # We will write a NEW version ONLY if we have at least one valid data file to "add".
    schema_any = simple_snapshot.get("schema", [])
    resources: List[Dict[str, Any]] = list(simple_snapshot.get("resources", []))
    table_id = prev_table_id or str(uuid.uuid4())

    current_rel_paths: List[str] = []
    add_entries: List[Tuple[str, int, Optional[Dict[str, Any]], Optional[int]]] = []  # (rel_path, size, stats, num_rows)

    for r in resources:
        src_path = r.get("file")
        if not src_path:
            continue

        rel_name = _stable_part_name(src_path)
        dst_full = os.path.join(data_dir, rel_name)

        if not _copy_into(storage, src_path, dst_full):
            logger.warning(f"[mirror][delta] skipping missing source: {src_path}")
            continue

        size = int(r.get("file_size") or 0)
        if size <= 0:
            size = _safe_filesize(storage, dst_full)

        stats_obj, num_rows = _compute_stats_if_possible(storage, dst_full)

        current_rel_paths.append(rel_name)
        add_entries.append((rel_name, size, stats_obj, num_rows))

    # If no files could be added, do NOT write a commit (prevents empty logs confusing Spark)
    if not add_entries:
        logger.warning("[mirror][delta] no data files found to mirror; skipping commit write.")
        return

    # Compute remove set against previous snapshot
    current_set = set(current_rel_paths)
    to_remove = sorted(list(prev_paths - current_set))

    # Next version
    version = prev_version + 1  # first proper commit -> 0

    # operation metrics
    num_files_str = str(len(add_entries))
    total_bytes_str = str(sum(int(sz) for _, sz, __, ___ in add_entries))
    rows_known = all(nr is not None for *_, nr in add_entries)
    num_rows_str = str(sum(int(nr or 0) for *_, nr in add_entries)) if rows_known else None

    # Build log file content (exact order & shape)
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

        _st_write_bytes(storage, commit_path, buf.getvalue().encode("utf-8"))

    # Best-effort cleanup (skip silently if storage can't list)
    try:
        _cleanup_unreferenced_parquet(storage, data_dir, set(current_rel_paths))
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup skipped: {e}")

    logger.info(
        f"[mirror][delta] wrote {_pad_version(version)}.json in {log_dir} "
        f"(add={len(add_entries)}, remove={len(to_remove)})"
    )

# supertable/mirroring/mirror_delta.py
"""
Delta Lake mirror — Spark-compatible layout with `data/` folder and
newline-delimited JSON actions. This version fixes the target root so files are
written under the same prefix Spark reads from (e.g. "supertable/..."), and it
does not rely on storage features that may be missing (listdir/copy/stat).

Final on-disk layout (for table <ROOT_PREFIX>/<org>/<super>/delta/<table_name>):
  data/
    part-00000-<uuid>-c000.snappy.parquet
    _delta_log/
      00000000000000000000.json
      00000000000000000001.json
      ...

You can point Spark to:
  LOCATION '<abfss://...>/<ROOT_PREFIX>/<org>/<super>/delta/<table_name>/data'

Key behaviors
- Files and _delta_log live under a `data/` directory (to match your working layout).
- Log file contains actions in this exact order: commitInfo, protocol, metaData, remove*, add*.
- protocol: {"minReaderVersion": 1, "minWriterVersion": 4}
- commitInfo: WRITE + Overwrite + Serializable + isBlindAppend=false + operationMetrics
- metaData: stable table id, parquet format, Spark-compatible schema, config flags, createdTime
- add: relative path (part-00000-<uuid>-c000.snappy.parquet), size, modificationTime, optional stats
- remove: emitted for any files no longer present
- Cleanup: removes stale *.parquet under `data/` if storage can list directories
- Robustness: gracefully handles storage backends without listdir/copy/stat; skips missing sources

Notes
- ROOT_PREFIX defaults to "supertable" to align with your path:
    abfss://.../supertable/lanes/demo-cloud-1/delta/table1/data
  If your deployment uses a different root, set `super_table.delta_root_prefix` on the object.
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

# ---------------- Configuration ----------------

DATA_DIR_NAME = "data"
DELTA_LOG_DIR_NAME = "_delta_log"

# Try to read from local FS if the source parquet isn't accessible via storage.
COPY_FROM_LOCAL_FS_IF_MISSING_IN_STORAGE = True


# ---------------- Small utils ------------------

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


# ---------- storage wrappers (feature-detect) ----------

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
    """
    Try multiple ways to enumerate a directory.
    Returns [] if not supported.
    """
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
    """
    Attempt storage-native copy; return True if succeeded.
    """
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


# ---------------- Delta helpers ----------------

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
    Using deterministic UUID from source path for stability.
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


def _compute_stats_if_possible(full_dst_path: str, storage) -> Tuple[Optional[Dict[str, Any]], Optional[int]]:
    """
    Returns (stats_dict_or_None, num_rows_or_None).
    """
    try:
        import pyarrow.parquet as pq  # type: ignore
    except Exception:
        return None, None

    tmp_bytes = _st_read_bytes(storage, full_dst_path)
    if tmp_bytes is None:
        return None, None

    try:
        import io as _io  # local alias
        pf = pq.ParquetFile(_io.BytesIO(tmp_bytes))
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
        # Backend cannot list; nothing to do.
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


# ---------------- Main entry ------------------

def write_delta_table(super_table, table_name: str, simple_snapshot: Dict[str, Any]) -> None:
    """
    Mirror the `simple_snapshot` into a Delta table at:
      <ROOT_PREFIX>/<org>/<super>/delta/<table_name>/data/
    ROOT_PREFIX is resolved as:
      getattr(super_table, "delta_root_prefix", None)
      or getattr(super_table, "root_prefix", None)
      or the literal "supertable"
    """
    # Resolve the root prefix so we write where Spark expects (_including_ "supertable/")
    root_prefix = (
        getattr(super_table, "delta_root_prefix", None)
        or getattr(super_table, "root_prefix", None)
        or "supertable"
    )

    # Compose the table root as in your ABFSS path:
    # abfss://.../<root_prefix>/<org>/<super>/delta/<table_name>/data/_delta_log
    table_root = os.path.join(root_prefix, super_table.organization, super_table.super_name, "delta", table_name)
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

    version = prev_version + 1  # first proper commit -> 0
    table_id = prev_table_id or str(uuid.uuid4())

    # Collect resources -> copy into data_dir and prepare add actions
    schema_any = simple_snapshot.get("schema", [])
    resources: List[Dict[str, Any]] = list(simple_snapshot.get("resources", []))

    current_rel_paths: List[str] = []
    add_entries: List[Tuple[str, int, Optional[Dict[str, Any]], Optional[int]]] = []  # (rel_path, size, stats, num_rows)

    for r in resources:
        src_path = r.get("file")
        if not src_path:
            continue

        rel_name = _stable_part_name(src_path)
        dst_full = os.path.join(data_dir, rel_name)

        if not _copy_into(storage, src_path, dst_full):
            # source not available; skip this file gracefully
            logger.warning(f"[mirror][delta] skipping missing source: {src_path}")
            continue

        size = int(r.get("file_size") or 0)
        if size <= 0:
            size = _safe_filesize(storage, dst_full)

        stats_obj, num_rows = _compute_stats_if_possible(dst_full, storage)

        current_rel_paths.append(rel_name)
        add_entries.append((rel_name, size, stats_obj, num_rows))

    current_set = set(current_rel_paths)
    to_remove = sorted(list(prev_paths - current_set))

    # operation metrics (strings)
    num_files_str = str(len(add_entries))
    total_bytes_str = str(sum(int(sz) for _, sz, __, ___ in add_entries))
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

        # 2) protocol (minWriterVersion=4, as in your working example)
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

    # Cleanup: keep only referenced parquet files inside data_dir (skip if backend can't list)
    try:
        _cleanup_unreferenced_parquet(storage, data_dir, set(current_rel_paths))
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup skipped: {e}")

    logger.info(
        f"[mirror][delta] wrote {_pad_version(version)}.json in {log_dir} "
        f"(add={len(add_entries)}, remove={len(to_remove)})"
    )

# supertable/mirroring/mirror_delta.py
"""
Delta Lake mirror (spec-compliant, latest-only projection)

What this does:
- Writes Delta commit files under .../delta/<table>/_delta_log/<version>.json
  using *newline-delimited* JSON actions: commitInfo, protocol, metaData,
  remove (for files not in latest), add (for files in latest).
- Always uses an "Overwrite" style commit so each version reflects the
  current SuperTable snapshot exactly (latest-only semantics).
- Optionally writes a small Parquet checkpoint (.../_delta_log/<version>.checkpoint.parquet)
  when pyarrow/pyarrow.parquet are available.

Key compatibility choices:
- Data files are co-located directly under the Delta table folder
  (e.g., .../delta/<table>/part-*.snappy.parquet), as expected by many engines.
- Protocol uses minReaderVersion=1, minWriterVersion=4.
- "add" actions include partitionValues (empty object for unpartitioned tables).

Also:
- Cleans up any stale/unreferenced data *.parquet files in the table folder,
  keeping only those referenced by the latest commit.

Minimal impact: invoked by MirrorFormats; no other changes required.
"""

import io
import json
import os
import hashlib
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple, Set

from supertable.config.defaults import logger

# --------- Tunables (keep minimal & local) -----------------------------------

# Copy data files under delta/<table>/ as part-*.snappy.parquet for strict compatibility.
COPY_DATA_INTO_TABLE_DIR = True  # MUST be True to mimic real Delta table layout

# If True and pyarrow is available, write a lightweight Parquet checkpoint per version.
WRITE_CHECKPOINT = True

# -----------------------------------------------------------------------------


def _pad_version(version: int) -> str:
    # 20-digit, zero-padded according to Delta naming convention
    return f"{int(version):020d}"


def _now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def _spark_type_for(t: str) -> Dict[str, Any]:
    """
    Map common logical types to Spark Delta JSON schema entries.
    Extend as needed. Defaults to string (nullable).
    """
    t = (t or "").strip().lower()
    # String-likes
    if t in {"string", "str", "varchar", "text"}:
        return {"type": "string", "nullable": True, "metadata": {}}
    # Integers
    if t in {"int", "integer", "int32", "int64", "bigint", "long"}:
        # Prefer "integer" for generic ints; engines will upcast when needed.
        # If you need 64-bit specifically, change to "long".
        return {"type": "integer", "nullable": True, "metadata": {}}
    # Floating
    if t in {"double", "float", "real", "numeric", "decimal"}:
        return {"type": "double", "nullable": True, "metadata": {}}
    # Boolean
    if t in {"bool", "boolean"}:
        return {"type": "boolean", "nullable": True, "metadata": {}}
    # Temporal
    if t in {"timestamp", "datetime"}:
        # Use Spark's timestamp logical type
        return {"type": "timestamp", "nullable": True, "metadata": {}}
    if t in {"date"}:
        return {"type": "date", "nullable": True, "metadata": {}}
    # Fallback
    return {"type": "string", "nullable": True, "metadata": {}}


def _to_spark_schema_json(schema_any: Any) -> str:
    """
    Convert SuperTable schema (list of {name, type}) to a Spark-like JSON schema string.
    """
    fields = []
    if isinstance(schema_any, list):
        for col in schema_any:
            if not isinstance(col, dict):
                continue
            name = col.get("name")
            ctype = col.get("type")
            if not name:
                continue
            f = _spark_type_for(ctype or "string")
            f["name"] = name
            fields.append(f)

    # Delta expects a compact string-encoded JSON for the schema
    return json.dumps({"type": "struct", "fields": fields}, separators=(",", ":"))


def _read_previous_latest(storage, base_dir: str) -> Tuple[int, Set[str]]:
    """
    Read previous mirrored state from latest.json if exists.
    Returns (prev_version, set_of_paths_relative).
    """
    latest_path = os.path.join(base_dir, "latest.json")
    if not storage.exists(latest_path):
        return (-1, set())
    try:
        obj = storage.read_json(latest_path)
        version = int(obj.get("version", -1))
        files = obj.get("files", [])
        prev_paths = {f.get("path") for f in files if f.get("path")}
        return (version, prev_paths)
    except Exception as e:
        logger.warning(f"[mirror][delta] Failed to read previous latest.json: {e}")
        return (-1, set())


def _binary_copy_if_possible(storage, src_path: str, dst_path: str) -> bool:
    """
    Try to copy a binary file using storage helper(s).
    Fallback: read bytes, write bytes if supported.
    Return True on success, False otherwise.
    """
    # Preferred: direct copy if backend has it
    if hasattr(storage, "copy"):
        try:
            storage.makedirs(os.path.dirname(dst_path))
            storage.copy(src_path, dst_path)
            return True
        except Exception as e:
            logger.warning(f"[mirror][delta] storage.copy failed ({src_path} -> {dst_path}): {e}")

    # Try generic read/write bytes API if present
    read_bytes = getattr(storage, "read_bytes", None)
    write_bytes = getattr(storage, "write_bytes", None)
    if callable(read_bytes) and callable(write_bytes):
        try:
            storage.makedirs(os.path.dirname(dst_path))
            data = storage.read_bytes(src_path)
            storage.write_bytes(dst_path, data)
            return True
        except Exception as e:
            logger.warning(f"[mirror][delta] byte copy failed ({src_path} -> {dst_path}): {e}")

    return False


def _make_delta_part_filename(src_path: str) -> str:
    """
    Build a Delta-like part filename: part-<uuid_or_hash>-c000.snappy.parquet
    We derive a stable hash from source path to avoid duplicates across runs.
    """
    base = os.path.basename(src_path)
    # stable hash from full source path (includes directories)
    h = hashlib.md5(src_path.encode("utf-8")).hexdigest()
    # keep a short, deterministic id
    short = h[:8] + "-" + h[8:12] + "-" + h[12:16] + "-" + h[16:20] + "-" + h[20:32]
    return f"part-{short}-c000.snappy.parquet"


def _co_locate_or_reuse_path(storage, table_base_dir: str, catalog_file_path: str) -> Tuple[str, bool]:
    """
    If COPY_DATA_INTO_TABLE_DIR is True, copy the parquet into table_base_dir with a Delta-like file name.
    Returns (relative_path_used_in_add, was_copied).
    If copying is disabled or fails, we still try to reference the original path (absolute),
    but many engines expect co-located files, so copying is strongly recommended.
    """
    if COPY_DATA_INTO_TABLE_DIR:
        rel_name = _make_delta_part_filename(catalog_file_path)
        dst_path = os.path.join(table_base_dir, rel_name)
        ok = _binary_copy_if_possible(storage, catalog_file_path, dst_path)
        if ok:
            # Path in Delta "add" should be relative to table base
            return rel_name.replace("\\", "/"), True
        logger.warning(f"[mirror][delta] Falling back to original path (copy failed): {catalog_file_path}")
    # Absolute reference (less compatible)
    return catalog_file_path, False


def _write_checkpoint_if_possible(storage, log_dir: str, version: int, add_paths: List[str]) -> None:
    """
    Optional Parquet checkpoint:
    - Requires pyarrow to be available in the runtime.
    - Stores a very small checkpoint with 'path' column so engines can skip JSON replay faster.
    This is NOT a full fidelity Delta checkpoint (no stats), but it's a valid Parquet file and
    harmless; engines that expect richer checkpoints will still be able to replay JSON logs.
    """
    if not WRITE_CHECKPOINT:
        return
    try:
        import pyarrow as pa  # type: ignore
        import pyarrow.parquet as pq  # type: ignore
    except Exception:
        # Silently skip if pyarrow is not present
        return

    table = pa.table({"path": pa.array(add_paths, type=pa.string())})
    chk_path = os.path.join(log_dir, f"{_pad_version(version)}.checkpoint.parquet")
    buf = io.BytesIO()
    pq.write_table(table, buf)
    storage.makedirs(log_dir)
    storage.write_bytes(chk_path, buf.getvalue())
    logger.debug(f"[mirror][delta] wrote checkpoint {chk_path} with {len(add_paths)} entries")


def _cleanup_unreferenced_parquet_files(storage, table_base_dir: str, keep_relative_paths: Set[str]) -> None:
    """
    Remove any *.parquet files in the table base dir that are not referenced by the latest state.
    Does not touch the _delta_log directory.
    """
    try:
        entries = storage.listdir(table_base_dir)  # should return names or paths depending on backend
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup listdir failed: {e}")
        return

    # Normalize to basenames
    keep_basenames = {os.path.basename(p) for p in keep_relative_paths if not p.startswith("/")}

    for entry in entries:
        name = os.path.basename(entry)
        full_path = os.path.join(table_base_dir, name)
        if name == "_delta_log":
            continue
        if not name.lower().endswith(".parquet"):
            continue
        # Keep only current referenced files (relative ones). If we referenced an absolute path,
        # we never copied into table dir, so any local *.parquet are safe to delete.
        if name not in keep_basenames:
            try:
                storage.remove(full_path)
                logger.info(f"[mirror][delta] removed stale data file: {full_path}")
            except Exception as e:
                logger.warning(f"[mirror][delta] failed to remove stale file {full_path}: {e}")


def write_delta_table(super_table, table_name: str, simple_snapshot: Dict[str, Any]) -> None:
    """
    Produce a real Delta commit for the current simple_snapshot.

    Location layout:
      base = <org>/<super>/delta/<table>
        _delta_log/
        part-*.snappy.parquet         (data files)
        latest.json                   (convenience pointer; not part of Delta spec)
    """
    base = os.path.join(super_table.organization, super_table.super_name, "delta", table_name)
    log_dir = os.path.join(base, "_delta_log")

    super_table.storage.makedirs(log_dir)

    # Determine version; if the simple snapshot does not provide, default to 0 for first write.
    version = int(simple_snapshot.get("snapshot_version", 0))

    schema_any = simple_snapshot.get("schema", [])
    resources: List[Dict[str, Any]] = simple_snapshot.get("resources", [])

    # Compute deltas vs previous mirror
    prev_version, prev_paths = _read_previous_latest(super_table.storage, base)

    # Build current file paths, co-located under table base
    current_paths: List[str] = []
    path_records: List[Tuple[str, int]] = []  # (relative_path_used_in_add_or_abs, size)
    for r in resources:
        src_file = r["file"]
        size = int(r.get("file_size", 0))
        used_path, _ = _co_locate_or_reuse_path(super_table.storage, base, src_file)
        current_paths.append(used_path)
        path_records.append((used_path, size))

    current_set = set(current_paths)

    # Actions to remove: those present before but not now
    to_remove = sorted(list(prev_paths - current_set))
    # Actions to add: those present now (full overwrite semantics)
    to_add = path_records  # (path, size)

    # Compose Delta JSON log (newline-delimited actions)
    commit_path = os.path.join(log_dir, _pad_version(version) + ".json")
    with io.StringIO() as s:
        now_ms = _now_ms()

        # 1) commitInfo
        # Use "Overwrite" and include partitionBy (empty array as string) for compatibility
        commit_info = {
            "commitInfo": {
                "timestamp": now_ms,
                "operation": "WRITE",
                "operationParameters": {"mode": "Overwrite", "partitionBy": "[]"},
                "readVersion": prev_version if prev_version >= 0 else None,
                "isBlindAppend": False,
                "engineInfo": "supertable-mirror-delta/1.0",
                "txnId": str(uuid.uuid4()),
            }
        }
        s.write(json.dumps(commit_info, separators=(",", ":")) + "\n")

        # 2) protocol (minWriterVersion=4 for broader compatibility)
        protocol = {"protocol": {"minReaderVersion": 1, "minWriterVersion": 4}}
        s.write(json.dumps(protocol, separators=(",", ":")) + "\n")

        # 3) metaData (included each commit)
        metadata = {
            "metaData": {
                "id": f"{super_table.organization}:{super_table.super_name}:{table_name}",
                "name": table_name,
                "format": {"provider": "parquet", "options": {}},
                "schemaString": _to_spark_schema_json(schema_any),
                "partitionColumns": [],
                "configuration": {
                    "delta.enableChangeDataFeed": "true",
                    "delta.autoOptimize.optimizeWrite": "true",
                    "delta.autoOptimize.autoCompact": "true",
                },
                "createdTime": now_ms,
            }
        }
        s.write(json.dumps(metadata, separators=(",", ":")) + "\n")

        # 4) remove (for any files that disappeared vs previous state)
        remove_ts = _now_ms()
        for p in to_remove:
            s.write(
                json.dumps(
                    {
                        "remove": {
                            "path": p,
                            "deletionTimestamp": remove_ts,
                            "dataChange": True,
                        }
                    },
                    separators=(",", ":"),
                )
                + "\n"
            )

        # 5) add (for all current files)
        add_ts = _now_ms()
        for p, size in to_add:
            add_obj = {
                "add": {
                    "path": p,
                    "partitionValues": {},
                    "size": int(size),
                    "modificationTime": add_ts,
                    "dataChange": True,
                    # "stats" is optional; omitted for now
                    "tags": {},
                }
            }
            s.write(json.dumps(add_obj, separators=(",", ":")) + "\n")

        # Atomically write the commit file
        content = s.getvalue().encode("utf-8")
        super_table.storage.write_bytes(commit_path, content)

    # Optional small checkpoint (helps some engines skip JSON replay faster)
    try:
        _write_checkpoint_if_possible(super_table.storage, log_dir, version, current_paths)
    except Exception as e:
        logger.warning(f"[mirror][delta] checkpoint skipped: {e}")

    # Update convenience pointer (non-spec)
    latest_state = {
        "version": version,
        "updated_at_ms": _now_ms(),
        "schema": schema_any,  # original schema projection
        "files": [{"path": p, "size": int(sz)} for p, sz in to_add],
    }
    super_table.storage.write_json(os.path.join(base, "latest.json"), latest_state)

    # Cleanup any stale/unreferenced data files in table base dir
    try:
        _cleanup_unreferenced_parquet_files(
            super_table.storage, base, set(current_paths)
        )
    except Exception as e:
        logger.warning(f"[mirror][delta] cleanup skipped: {e}")

    logger.info(
        f"[mirror][delta] v{version} wrote {_pad_version(version)}.json  "
        f"(add={len(to_add)}, remove={len(to_remove)}; co_located={'yes' if COPY_DATA_INTO_TABLE_DIR else 'no'})"
    )

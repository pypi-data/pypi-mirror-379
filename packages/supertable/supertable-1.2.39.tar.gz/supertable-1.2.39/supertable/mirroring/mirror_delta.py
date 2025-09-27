# supertable/mirroring/mirror_delta.py
from __future__ import annotations

import io
import json
import logging
import os
import time
import uuid
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

__all__ = ["write_delta_table", "mirror_simple_snapshot_to_delta"]

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Storage surface expected (patched by synapse_storage.activate_synapse)
# -----------------------------------------------------------------------------
class _StorageProto:
    def read_bytes(self, path: str) -> bytes: ...
    def write_bytes(self, path: str, data: bytes) -> None: ...
    def read_json(self, path: str) -> Any: ...
    def write_json(self, path: str, obj: Any) -> None: ...
    def exists(self, path: str) -> bool: ...
    def makedirs(self, path: str) -> None: ...
    def mkdirs(self, path: str) -> None: ...
    def listdir(self, path: str) -> List[str]: ...
    def list(self, path: str) -> List[str]: ...
    def remove(self, path: str) -> None: ...
    def delete(self, path: str) -> None: ...
    def copy(self, src: str, dst: str) -> None: ...
    def stat(self, path: str) -> Dict[str, Any]: ...
    def size(self, path: str) -> int: ...

def _get_storage() -> _StorageProto:
    from supertable.storage.local_storage import LocalStorage  # type: ignore
    return LocalStorage()

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def _join(*parts: str) -> str:
    return "/".join([p.strip("/").replace("\\", "/") for p in parts if p is not None and p != ""])

def _pad_version(n: int) -> str:
    return str(n).rjust(20, "0")

def _now_ms() -> int:
    return int(time.time() * 1000)

def _basename(path: str) -> str:
    return path.rstrip("/").split("/")[-1]

def _ensure_dir(storage: _StorageProto, path: str) -> None:
    try:
        if hasattr(storage, "mkdirs"):
            storage.mkdirs(path)
        else:
            storage.makedirs(path)
    except Exception:
        pass

def _list_json_versions(storage: _StorageProto, log_dir: str) -> List[Tuple[int, str]]:
    """Return list of (version, full_path)."""
    try:
        names = storage.listdir(log_dir)
    except Exception:
        names = []
    out: List[Tuple[int, str]] = []
    for full in names:
        base = _basename(full)
        if not base.endswith(".json"):
            continue
        try:
            v = int(base.split(".")[0])
        except Exception:
            continue
        out.append((v, full if "/" in full else _join(log_dir, base)))
    return sorted(out)

def _read_prev_table_id_and_paths(storage: _StorageProto, log_dir: str) -> Tuple[Optional[str], List[str]]:
    """
    Read latest _delta_log/<version>.json (if any) and return (table_id, added_paths).
    Paths are returned as relative parquet names recorded in the log.
    """
    versions = _list_json_versions(storage, log_dir)
    if not versions:
        return None, []
    latest_version, latest_path = versions[-1]
    data = storage.read_bytes(latest_path).decode("utf-8").splitlines()
    table_id: Optional[str] = None
    added: List[str] = []
    for line in data:
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if "metaData" in obj and not table_id:
            table_id = obj["metaData"].get("id")
        if "add" in obj:
            added.append(obj["add"]["path"])
        if "remove" in obj:
            try:
                p = obj["remove"]["path"]
                if p in added:
                    added.remove(p)
            except Exception:
                pass
    return table_id, added

def _stable_part_name(src_path: str) -> str:
    base = _basename(src_path)
    _, ext = os.path.splitext(base)
    if ext.lower() not in {".parquet", ".snappy.parquet"}:
        ext = ".snappy.parquet"
    return f"part-00000-{uuid.uuid4()}-c000{ext}"

def _parquet_size(storage: _StorageProto, path: str) -> int:
    try:
        if hasattr(storage, "size"):
            return int(storage.size(path))  # type: ignore
    except Exception:
        pass
    try:
        st = storage.stat(path)
        s = st.get("size")
        return int(s) if s is not None else 0
    except Exception:
        data = storage.read_bytes(path)
        return len(data) if data else 0

# -----------------------------------------------------------------------------
# Public API (core)
# -----------------------------------------------------------------------------
def mirror_simple_snapshot_to_delta(
    target_root: str,
    simple_snapshot: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Create/append a Delta Lake table under <target_root>/data compatible with Synapse/Spark.

    simple_snapshot schema (minimum):
      {
        "resources": [{"file": "<source_parquet_uri_or_rel>", "rows": 123, "stats": "<json-string>"}],
        "schemaString": "<spark-like schema JSON string>" | None,
        "schema": <optional list of fields if schemaString omitted>,
        "table_id": "<uuid-optional>"
      }
    """
    storage = _get_storage()
    data_dir = _join(target_root, "data")
    log_dir = _join(data_dir, "_delta_log")
    _ensure_dir(storage, data_dir)
    _ensure_dir(storage, log_dir)

    # Next version + previous table id
    versions = _list_json_versions(storage, log_dir)
    version = (versions[-1][0] + 1) if versions else 0
    prev_table_id, _prev_paths = _read_prev_table_id_and_paths(storage, log_dir)

    # Ingest resources → copy/rename into data_dir/part-*.snappy.parquet
    resources = list(simple_snapshot.get("resources") or [])
    if not resources:
        raise ValueError("simple_snapshot.resources is required and cannot be empty")

    add_entries: List[Dict[str, Any]] = []
    current_rel_paths: List[str] = []
    total_rows = 0
    total_bytes = 0

    for r in resources:
        src = r.get("file")
        if not src:
            continue
        rel_name = _stable_part_name(src)
        dst = _join(data_dir, rel_name)

        # Try storage.copy, fallback to read/write
        copied = False
        try:
            if hasattr(storage, "copy"):
                storage.copy(src, dst)  # type: ignore
                copied = True
        except Exception:
            copied = False
        if not copied:
            data = storage.read_bytes(src)
            if data is None:
                raise FileNotFoundError(f"Resource not found: {src}")
            storage.write_bytes(dst, data)

        size = _parquet_size(storage, dst)
        rows = r.get("rows")
        if isinstance(rows, int):
            total_rows += rows
        total_bytes += size

        add_inner: Dict[str, Any] = {
            "path": rel_name,
            "partitionValues": {},
            "size": size,
            "modificationTime": _now_ms(),
            "dataChange": True,
            "tags": {},
        }
        stats = r.get("stats")
        if isinstance(stats, str) and stats.strip().startswith("{"):
            add_inner["stats"] = stats
        add_entries.append(add_inner)
        current_rel_paths.append(rel_name)

    # Build metadata
    schema_string = simple_snapshot.get("schemaString")
    if not schema_string:
        schema_json = {"type": "struct", "fields": simple_snapshot.get("schema", [])}
        schema_string = json.dumps(schema_json, separators=(",", ":"))

    table_id = simple_snapshot.get("table_id") or prev_table_id or str(uuid.uuid4())

    commit_info = {
        "commitInfo": {
            "timestamp": _now_ms(),
            "operation": "WRITE",
            "operationParameters": {"mode": "Overwrite", "partitionBy": "[]"},
            "isolationLevel": "Serializable",
            "isBlindAppend": False,
            "operationMetrics": {
                "numFiles": str(len(add_entries)),
                "numOutputRows": str(total_rows),
                "numOutputBytes": str(total_bytes),
            },
            "engineInfo": "Apache-Spark/3.4.3.5.3.20250511.1 Delta-Lake/2.4.0.24",
            "txnId": str(uuid.uuid4()),
        }
    }
    protocol = {"protocol": {"minReaderVersion": 1, "minWriterVersion": 4}}
    meta = {
        "metaData": {
            "id": table_id,
            "format": {"provider": "parquet", "options": {}},
            "schemaString": schema_string,
            "partitionColumns": [],
            "configuration": {
                "delta.enableChangeDataFeed": "true",
                "delta.autoOptimize.optimizeWrite": "true",
                "delta.autoOptimize.autoCompact": "true",
            },
            "createdTime": _now_ms(),
        }
    }

    # Write actions file: commitInfo, protocol, metaData, add*
    commit_path = _join(log_dir, f"{_pad_version(version)}.json")
    buf = io.StringIO()
    buf.write(json.dumps(commit_info, separators=(",", ":")) + "\n")
    buf.write(json.dumps(protocol, separators=(",", ":")) + "\n")
    buf.write(json.dumps(meta, separators=(",", ":")) + "\n")
    for add in add_entries:
        buf.write(json.dumps({"add": add}, separators=(",", ":")) + "\n")

    storage.write_bytes(commit_path, buf.getvalue().encode("utf-8"))
    logger.info("[mirror][delta] wrote %s with add=%d", commit_path, len(add_entries))
    return {"version": version, "log_path": commit_path, "added": current_rel_paths}

# -----------------------------------------------------------------------------
# Public API (compat shim expected by MirrorFormats)
# -----------------------------------------------------------------------------
def write_delta_table(
    *args: Any,
    **kwargs: Any,
) -> Dict[str, Any]:
    """
    Compatibility wrapper expected by supertable.mirroring.mirror_formats.

    Accepted calling patterns (we normalize all to mirror_simple_snapshot_to_delta):

    1) write_delta_table(target_root, simple_snapshot_dict)
    2) write_delta_table(target_root, resources=[...], schemaString="...", table_id="...", schema=[...])
    3) write_delta_table(storage, target_root, ...)  # 'storage' is ignored since we use patched LocalStorage

    Returns: {'version': int, 'log_path': str, 'added': [str, ...]}
    """
    # Normalize positional args
    # Possible shapes:
    #   (target_root, snapshot_dict)
    #   (target_root, **kwargs)
    #   (storage, target_root, snapshot_dict/kwargs)
    if not args:
        raise TypeError("write_delta_table requires at least target_root")

    # If first arg looks like a storage object, skip it
    arg0 = args[0]
    if hasattr(arg0, "read_bytes") and hasattr(arg0, "write_bytes"):
        args = args[1:]

    if not args:
        raise TypeError("write_delta_table requires target_root after storage")

    target_root = args[0]
    if not isinstance(target_root, str):
        raise TypeError("write_delta_table(target_root, ...) expects target_root to be a str")

    # Build simple_snapshot
    if len(args) >= 2 and isinstance(args[1], dict) and "resources" in args[1]:
        simple_snapshot: Dict[str, Any] = dict(args[1])  # copy
    else:
        # construct from kwargs
        simple_snapshot = {
            "resources": kwargs.get("resources") or kwargs.get("files") or [],
            "schemaString": kwargs.get("schemaString"),
            "schema": kwargs.get("schema"),
            "table_id": kwargs.get("table_id"),
        }

    # Validate minimal payload
    resources = simple_snapshot.get("resources") or []
    if not isinstance(resources, (list, tuple)) or not resources:
        raise ValueError("write_delta_table requires non-empty resources list")

    return mirror_simple_snapshot_to_delta(target_root, simple_snapshot)

# supertable/mirroring/mirror_delta.py
from __future__ import annotations

import io
import json
import logging
import os
import time
import uuid
from typing import Any, Dict, Iterable, List, Optional, Tuple

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
        # Directory may already exist or backend may not need it.
        pass

def _list_json_versions(storage: _StorageProto, log_dir: str) -> List[Tuple[int, str]]:
    """Return list of (version, full_path) for JSON files in _delta_log."""
    names: List[str] = []
    try:
        if hasattr(storage, "listdir"):
            names = storage.listdir(log_dir)  # type: ignore[attr-defined]
        elif hasattr(storage, "list"):
            names = storage.list(log_dir)  # type: ignore[attr-defined]
        else:
            names = []
    except Exception:
        try:
            if hasattr(storage, "list"):
                names = storage.list(log_dir)  # type: ignore[attr-defined]
            else:
                names = []
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
    _, latest_path = versions[-1]
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
            return int(storage.size(path))  # type: ignore[attr-defined]
    except Exception:
        pass
    try:
        st = storage.stat(path)
        s = st.get("size")
        return int(s) if s is not None else 0
    except Exception:
        data = storage.read_bytes(path)
        return len(data) if data else 0

def _first_str_path(*candidates: Any) -> Optional[str]:
    """
    Return the first usable path string found among arbitrary args/kwargs-like objects.
    Supports:
      - direct str
      - dicts with keys: location/target_root/root/path/dir/directory
      - objects with attribute 'location' (str)
    """
    keys = ("location", "target_root", "root", "path", "dir", "directory")
    for c in candidates:
        if isinstance(c, str) and c != "":
            return c
        if isinstance(c, dict):
            for k in keys:
                v = c.get(k)
                if isinstance(v, str) and v:
                    return v
        if hasattr(c, "location"):
            v = getattr(c, "location")
            if isinstance(v, str) and v:
                return v
    return None

def _first_snapshot_dict(*candidates: Any) -> Optional[Dict[str, Any]]:
    """
    Return a dict that looks like the simple snapshot:
      has 'resources' OR ('schemaString'|'schema')
    Also accepts nested keys: 'simple_snapshot' or 'snapshot'.
    """
    for c in candidates:
        if isinstance(c, dict):
            if "resources" in c or "schemaString" in c or "schema" in c:
                return c
            for nested in ("simple_snapshot", "snapshot"):
                v = c.get(nested)
                if isinstance(v, dict) and ("resources" in v or "schemaString" in v or "schema" in v):
                    return v
    return None

# -----------------------------------------------------------------------------
# Schema normalization (fixes "String"/"Int64" etc. and map→list fields)
# -----------------------------------------------------------------------------
_SPARK_TYPE_MAP = {
    "string": "string",
    "boolean": "boolean",
    "bool": "boolean",
    "byte": "byte",
    "short": "short",
    "integer": "integer",
    "int": "integer",
    "int32": "integer",
    "long": "long",
    "int64": "long",
    "bigint": "long",
    "float": "float",
    "double": "double",
    "decimal": "decimal",  # keep decimal(p,s) form as-is
    "date": "date",
    "timestamp": "timestamp",
    "binary": "binary",
}

def _normalize_type(t: str) -> str:
    if not isinstance(t, str):
        return "string"
    ts = t.strip().lower()
    # pass-through decimal(p,s)
    if ts.startswith("decimal(") and ts.endswith(")"):
        return ts
    return _SPARK_TYPE_MAP.get(ts, ts)

def _schema_to_structtype_json(schema_string: Optional[str], schema_list: Optional[List[Dict[str, Any]]]) -> str:
    """
    Return a valid Spark StructType JSON string for Delta metaData.schemaString.
    Accepts:
      - schema_string: StructType JSON or {type:'struct', fields:{name:type,...}} map
      - schema_list: list of dicts with name/type/(nullable/metadata)
    """
    # 1) Try to parse schema_string if provided
    if schema_string:
        try:
            parsed = json.loads(schema_string)
            if isinstance(parsed, dict):
                # Already StructType with fields list
                if isinstance(parsed.get("fields"), list):
                    for f in parsed["fields"]:
                        if isinstance(f, dict):
                            if "type" in f:
                                f["type"] = _normalize_type(f["type"])
                            f.setdefault("nullable", True)
                            f.setdefault("metadata", {})
                    return json.dumps(parsed, separators=(",", ":"))
                # fields is a dict/map → convert to list
                if isinstance(parsed.get("fields"), dict):
                    fields_map = parsed["fields"]
                    fields = []
                    for name, typ in fields_map.items():
                        fields.append({
                            "name": name,
                            "type": _normalize_type(str(typ)),
                            "nullable": True,
                            "metadata": {}
                        })
                    out = {"type": "struct", "fields": fields}
                    return json.dumps(out, separators=(",", ":"))
        except Exception:
            # fall through to schema_list path
            pass

    # 2) Build from schema_list
    if schema_list:
        fields = []
        for f in schema_list:
            if not isinstance(f, dict):
                continue
            name = f.get("name")
            typ = _normalize_type(str(f.get("type", "string")))
            fields.append({
                "name": name,
                "type": typ,
                "nullable": f.get("nullable", True),
                "metadata": f.get("metadata", {})
            })
        out = {"type": "struct", "fields": fields}
        return json.dumps(out, separators=(",", ":"))

    # 3) Fallback: empty struct
    return json.dumps({"type": "struct", "fields": []}, separators=(",", ":"))

# -----------------------------------------------------------------------------
# Core writer
# -----------------------------------------------------------------------------
def mirror_simple_snapshot_to_delta(
    target_root: str,
    simple_snapshot: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Create/append a Delta Lake table directly under `target_root` (NO /data subfolder),
    compatible with Synapse/Spark.

    Layout:
      <target_root>/
        _delta_log/
          00000000000000000000.json
        part-*.parquet

    simple_snapshot schema (minimum):
      {
        "resources": [{"file": "<source_parquet_uri_or_rel>", "rows": 123, "stats": "<json-string>"}],
        "schemaString": "<spark-like schema JSON string>" | None,
        "schema": <optional list of fields if schemaString omitted>,
        "table_id": "<uuid-optional>"
      }
    """
    storage = _get_storage()

    # Root is table root (no 'data' subfolder)
    table_root = target_root.rstrip("/")
    log_dir = _join(table_root, "_delta_log")
    _ensure_dir(storage, table_root)
    _ensure_dir(storage, log_dir)

    # Next version + previous table id
    versions = _list_json_versions(storage, log_dir)
    version = (versions[-1][0] + 1) if versions else 0
    prev_table_id, _ = _read_prev_table_id_and_paths(storage, log_dir)

    # Ingest resources → copy/rename into <table_root>/part-*.snappy.parquet
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
        dst = _join(table_root, rel_name)

        # Try storage.copy, fallback to read/write
        copied = False
        try:
            if hasattr(storage, "copy"):
                storage.copy(src, dst)  # type: ignore[attr-defined]
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
            "path": rel_name,                    # RELATIVE to table root
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

    # Build metadata (normalize schema)
    raw_schema_string = simple_snapshot.get("schemaString")
    schema_list = simple_snapshot.get("schema")
    schema_string = _schema_to_structtype_json(raw_schema_string, schema_list)

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
def write_delta_table(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """
    Compatibility wrapper expected by supertable.mirroring.mirror_formats.

    We accept a variety of call patterns. We locate:
      - target_root: a string path, or inside a dict under keys: location/target_root/root/path/dir/directory,
                     or as an object's .location attribute.
      - simple_snapshot: a dict with at least 'resources' (and optionally 'schemaString' or 'schema').

    Examples we handle:
      write_delta_table(target_root, simple_snapshot)
      write_delta_table(storage, target_root, simple_snapshot)
      write_delta_table(storage, table_meta_with_location, simple_snapshot)
      write_delta_table(target_root, resources=[...], schemaString="...", schema=[...], table_id="...")

    Returns: {'version': int, 'log_path': str, 'added': [str, ...]}
    """
    # Drop leading storage argument if present
    arg_iter = list(args)
    if arg_iter and hasattr(arg_iter[0], "read_bytes") and hasattr(arg_iter[0], "write_bytes"):
        arg_iter = arg_iter[1:]

    # Try kwargs first
    target_root = kwargs.get("target_root")
    snapshot_kw = kwargs.get("simple_snapshot") or kwargs.get("snapshot")

    # Fallback: scan positional args for path + snapshot
    if not isinstance(target_root, str) or not target_root:
        target_root = _first_str_path(*arg_iter, kwargs)

    snapshot = None
    if isinstance(snapshot_kw, dict):
        snapshot = snapshot_kw
    if snapshot is None:
        # Find any dict that looks like a snapshot among args/kwargs
        snapshot = _first_snapshot_dict(*arg_iter, kwargs)

    # If still missing, try to build from kwargs pieces
    if snapshot is None:
        resources = kwargs.get("resources") or kwargs.get("files")
        schema_string = kwargs.get("schemaString")
        schema = kwargs.get("schema")
        table_id = kwargs.get("table_id")
        if resources:
            snapshot = {"resources": resources, "schemaString": schema_string, "schema": schema, "table_id": table_id}

    # Final validation
    if not isinstance(target_root, str) or not target_root:
        raise TypeError("write_delta_table(target_root, ...) expects target_root as a valid path string or dict with 'location'.")
    if not isinstance(snapshot, dict) or not snapshot.get("resources"):
        raise ValueError("write_delta_table requires a simple_snapshot dict (or kwargs) with a non-empty 'resources' list.")

    return mirror_simple_snapshot_to_delta(target_root, snapshot)

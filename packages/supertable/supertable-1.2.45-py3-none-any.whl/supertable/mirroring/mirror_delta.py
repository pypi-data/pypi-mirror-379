# supertable/mirroring/mirror_delta.py
"""
Delta Lake mirror (spec-compliant, latest-only projection)

Writes a proper Delta _delta_log with actions:
  - commitInfo
  - protocol
  - metaData
  - remove (for files removed vs previous mirror)
  - add (for current snapshot files)

Updates:
- Engine string set to: "Apache-Spark/3.4.3.5.3.20250511.1 Delta-Lake/2.4.0.24"
- metaData includes {"format":{"provider":"parquet","options":{}}} and a valid Spark StructType JSON schemaString.
- Do NOT write latest.json (removed).
- Parquet data files are **copied** under the table folder; obsolete ones are **deleted** from the table folder.
- Do NOT write any (partial) checkpoints to avoid incompatibilities with Spark’s checkpoint reader.
"""

from __future__ import annotations

import io
import json
import os
import hashlib
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple, Set

from supertable.config.defaults import logger

# ---- Spark/Delta schema normalization helpers ----
_SPARK_TYPE_MAP = {
    "string": "string",
    "boolean": "boolean", "bool": "boolean",
    "byte": "byte", "short": "short",
    "integer": "integer", "int": "integer", "int32": "integer",
    "long": "long", "int64": "long", "bigint": "long",
    "float": "float", "double": "double",
    "decimal": "decimal",  # keep decimal(p,s) as-is
    "date": "date", "timestamp": "timestamp",
    "binary": "binary",
}

def _normalize_type(t: str) -> str:
    if not isinstance(t, str):
        return "string"
    ts = t.strip().lower()
    if ts.startswith("decimal(") and ts.endswith(")"):
        return ts
    return _SPARK_TYPE_MAP.get(ts, ts)

def _schema_to_structtype_json(schema_string: Any = None, schema_list: Any = None) -> str:
    """
    Return a valid Spark StructType JSON string for Delta metaData.schemaString.
    Prefers a provided schema_string (already in Spark StructType JSON) when present.
    Otherwise builds from a list of {name,type,(nullable,metadata)} dicts.
    """
    # If caller provided a schema_string, try to sanitize minimal types and return it
    if schema_string:
        try:
            parsed = json.loads(schema_string) if isinstance(schema_string, str) else schema_string
            if isinstance(parsed, dict):
                if isinstance(parsed.get("fields"), list):
                    for f in parsed["fields"]:
                        if isinstance(f, dict) and "type" in f:
                            if isinstance(f["type"], str):
                                f["type"] = _normalize_type(f["type"])
                            f.setdefault("nullable", True)
                            f.setdefault("metadata", {})
                    return json.dumps(parsed, separators=(",", ":"))
                if isinstance(parsed.get("fields"), dict):
                    fields_map = parsed["fields"]
                    fields = []
                    for name, typ in fields_map.items():
                        fields.append({"name": name, "type": _normalize_type(str(typ)), "nullable": True, "metadata": {}})
                    out = {"type": "struct", "fields": fields}
                    return json.dumps(out, separators=(",", ":"))
        except Exception:
            # fall through to schema_list
            pass

    if schema_list:
        fields = []
        for f in schema_list:
            if not isinstance(f, dict):
                continue
            name = f.get("name")
            typ = _normalize_type(str(f.get("type", "string")))
            fields.append({"name": name, "type": typ, "nullable": f.get("nullable", True), "metadata": f.get("metadata", {})})
        out = {"type": "struct", "fields": fields}
        return json.dumps(out, separators=(",", ":"))

    # empty struct fallback
    return json.dumps({"type": "struct", "fields": []}, separators=(",", ":"))


# --------- Tunables -----------------------------------------------------------

# Always co-locate data files into the Delta table folder, as requested.
COPY_DATA_INTO_TABLE_DIR = True

# Do NOT emit any checkpoint files unless we implement full, spec-compliant checkpoints.
WRITE_CHECKPOINT = False

# -----------------------------------------------------------------------------


def _pad_version(version: int) -> str:
    return f"{int(version):020d}"


def _now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def _stable_table_id(organization: str, super_name: str, table_name: str) -> str:
    """
    Stable UUIDv5-like id from table coordinates to keep metaData.id consistent.
    Allows overriding via simple_snapshot['delta_meta_id'] or ['metadata_id'] if provided.
    """
    import uuid
    seed = f"{organization}/{super_name}/{table_name}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, seed))


def _binary_copy_if_possible(storage, src_path: str, dst_path: str) -> bool:
    # Prefer native copy when available
    if hasattr(storage, "copy"):
        try:
            storage.makedirs(os.path.dirname(dst_path))
            storage.copy(src_path, dst_path)
            return True
        except Exception as e:
            logger.warning(f"[mirror][delta] storage.copy failed ({src_path} -> {dst_path}): {e}")

    read_bytes = getattr(storage, "read_bytes", None)
    write_bytes = getattr(storage, "write_bytes", None)
    if callable(read_bytes) and callable(write_bytes):
        try:
            storage.makedirs(os.path.dirname(dst_path))
            storage.write_bytes(dst_path, read_bytes(src_path))
            return True
        except Exception as e:
            logger.warning(f"[mirror][delta] byte copy failed ({src_path} -> {dst_path}): {e}")

    return False


def _co_locate_or_reuse_path(storage, table_files_dir: str, catalog_file_path: str) -> str:
    """
    Copy parquet into table_files_dir, return the relative path 'files/<hash>_<basename>'.
    """
    base_name = os.path.basename(catalog_file_path)
    h = hashlib.md5(catalog_file_path.encode("utf-8")).hexdigest()[:8]
    rel_name = f"{h}_{base_name}"
    rel_path = os.path.join("files", rel_name).replace("\\", "/")
    dst_path = os.path.join(table_files_dir, rel_name)
    ok = _binary_copy_if_possible(storage, catalog_file_path, dst_path)
    if not ok:
        raise RuntimeError(f"Failed to copy data file into Delta table dir: {catalog_file_path}")
    return rel_path


def _list_co_located_paths(storage, table_files_dir: str) -> Set[str]:
    """
    Return set of already present co-located files as 'files/<name>'.
    """
    rels: Set[str] = set()
    try:
        if hasattr(storage, "ls"):
            for p in storage.ls(table_files_dir) or []:
                bn = os.path.basename(p.rstrip("/"))
                if not bn:
                    continue
                rels.add(("files/" + bn).replace("\\", "/"))
        elif hasattr(storage, "listdir"):
            for bn in storage.listdir(table_files_dir) or []:
                rels.add(("files/" + bn).replace("\\", "/"))
    except Exception:
        # ok to be empty
        pass
    return rels


def _write_checkpoint_if_possible(storage, log_dir: str, version: int, add_paths: List[str]) -> None:
    # Disabled by default; keep code for future full compliance
    if not WRITE_CHECKPOINT:
        return
    try:
        import pyarrow as pa  # type: ignore
        import pyarrow.parquet as pq  # type: ignore
    except Exception:
        return

    table = pa.table({"path": pa.array(add_paths, type=pa.string())})
    chk_path = os.path.join(log_dir, f"{_pad_version(version)}.checkpoint.parquet")
    buf = io.BytesIO()
    pq.write_table(table, buf)
    storage.makedirs(log_dir)
    storage.write_bytes(chk_path, buf.getvalue())
    logger.debug(f"[mirror][delta] wrote checkpoint {chk_path} with {len(add_paths)} entries")


def write_delta_table(super_table, table_name: str, simple_snapshot: Dict[str, Any]) -> None:
    """
    Produce a Delta commit for the current simple_snapshot.

    Directory layout:
      base = <org>/<super>/delta/<table>
        _delta_log/
        files/
    """
    base = os.path.join(super_table.organization, super_table.super_name, "delta", table_name)
    log_dir = os.path.join(base, "_delta_log")
    files_dir = os.path.join(base, "files")

    super_table.storage.makedirs(log_dir)
    super_table.storage.makedirs(files_dir)

    version = int(simple_snapshot.get("snapshot_version", 0))

    # Prefer an explicitly provided Spark StructType JSON if caller has one
    schema_string_from_snapshot = (
        simple_snapshot.get("schemaString")
        or simple_snapshot.get("schema_string")
        or None
    )
    schema_list = simple_snapshot.get("schema", [])

    resources: List[Dict[str, Any]] = simple_snapshot.get("resources", [])

    # Derive/override meta id & createdTime if provided
    meta_id = (
        simple_snapshot.get("delta_meta_id")
        or simple_snapshot.get("metadata_id")
        or _stable_table_id(super_table.organization, super_table.super_name, table_name)
    )
    created_time_ms = int(simple_snapshot.get("createdTime", _now_ms()))

    # Previously co-located files
    prev_paths = _list_co_located_paths(super_table.storage, files_dir)

    # Build current file paths by co-locating under table dir
    current_paths: List[str] = []
    path_records: List[Tuple[str, int, Dict[str, Any]]] = []  # (path_used_in_add, size, resource)
    for r in resources:
        src_file = r["file"]
        size = int(r.get("file_size", 0))
        used_rel_path = _co_locate_or_reuse_path(super_table.storage, files_dir, src_file)
        current_paths.append(used_rel_path)
        path_records.append((used_rel_path, size, r))

    current_set = set(current_paths)

    # Files to remove = those present before but not now
    to_remove = sorted(list(prev_paths - current_set))
    to_add = path_records

    # Delete obsolete co-located files (physically remove unused parquet from the delta folder)
    for rp in to_remove:
        try:
            super_table.storage.delete(os.path.join(base, rp))
        except Exception as e:
            logger.warning(f"[mirror][delta] failed to delete obsolete {rp}: {e}")

    # Metrics
    num_files = len(to_add)
    num_output_bytes = sum(int(sz) for _, sz, _ in to_add) if to_add else 0
    num_output_rows = 0
    for rec in resources:
        val = rec.get("rows") or rec.get("numRecords") or 0
        try:
            num_output_rows += int(val)
        except Exception:
            pass

    # Compose Delta log (NDJSON)
    commit_path = os.path.join(log_dir, _pad_version(version) + ".json")

    # Guard: if this exact version file already exists, skip to avoid duplicate writes
    if hasattr(super_table.storage, "exists") and super_table.storage.exists(commit_path):
        logger.info(f"[mirror][delta] commit {commit_path} already exists; skipping rewrite")
        return

    with io.StringIO() as s:
        # 1) commitInfo
        commit_info = {
            "commitInfo": {
                "timestamp": _now_ms(),
                "operation": "WRITE",
                "operationParameters": {"mode": "Overwrite", "partitionBy": "[]"},
                "isolationLevel": "Serializable",
                "isBlindAppend": False,
                "operationMetrics": {
                    "numFiles": str(num_files),
                    "numOutputRows": str(num_output_rows),
                    "numOutputBytes": str(num_output_bytes),
                },
                "engineInfo": "Apache-Spark/3.4.3.5.3.20250511.1 Delta-Lake/2.4.0.24",
                "txnId": __import__("uuid").uuid4().hex,
            }
        }
        s.write(json.dumps(commit_info, separators=(",", ":")) + "\n")

        # 2) protocol (must be present in the first visible commit)
        protocol = {"protocol": {"minReaderVersion": 1, "minWriterVersion": 4}}
        s.write(json.dumps(protocol, separators=(",", ":")) + "\n")

        # 3) metaData (include on every commit for robustness)
        metadata = {
            "metaData": {
                "id": meta_id,
                "format": {"provider": "parquet", "options": {}},
                "schemaString": _schema_to_structtype_json(schema_string_from_snapshot, schema_list),
                "partitionColumns": [],
                "configuration": {
                    "delta.enableChangeDataFeed": "true",
                    "delta.autoOptimize.optimizeWrite": "true",
                    "delta.autoOptimize.autoCompact": "true",
                },
                "createdTime": created_time_ms,
            }
        }
        s.write(json.dumps(metadata, separators=(",", ":")) + "\n")

        # 4) remove actions
        remove_ts = _now_ms()
        for p in to_remove:
            s.write(json.dumps({"remove": {"path": p, "deletionTimestamp": remove_ts, "dataChange": True}},
                               separators=(",", ":")) + "\n")

        # 5) add actions
        add_ts = _now_ms()
        for p, size, res in to_add:
            stats_val = None
            try:
                if isinstance(res.get("stats_json"), str):
                    stats_val = res["stats_json"]
                elif isinstance(res.get("stats"), dict):
                    stats_val = json.dumps(res["stats"], separators=(",", ":"))
                else:
                    rows_val = res.get("rows") or res.get("numRecords")
                    if isinstance(rows_val, (int, float)) or (isinstance(rows_val, str) and rows_val.isdigit()):
                        stats_val = json.dumps({"numRecords": int(rows_val)}, separators=(",", ":"))
            except Exception:
                stats_val = None

            add_obj: Dict[str, Any] = {
                "add": {
                    "path": p,
                    "partitionValues": {},
                    "size": int(size),
                    "modificationTime": add_ts,
                    "dataChange": True,
                    "tags": {},
                }
            }
            if stats_val is not None:
                add_obj["add"]["stats"] = stats_val

            s.write(json.dumps(add_obj, separators=(",", ":")) + "\n")

        # Write the commit atomically
        super_table.storage.write_bytes(commit_path, s.getvalue().encode("utf-8"))

    # Optional checkpoint skipped (WRITE_CHECKPOINT=False)
    try:
        _write_checkpoint_if_possible(super_table.storage, log_dir, version, current_paths)
    except Exception as e:
        logger.warning(f"[mirror][delta] checkpoint skipped: {e}")

    logger.info(
        f"[mirror][delta] v{version} wrote {_pad_version(version)}.json  "
        f"(add={len(to_add)}, remove={len(to_remove)}; co_located=yes)"
    )

# supertable/mirroring/mirror_formats.py

import os
from enum import Enum
from typing import Iterable, List, Dict, Any, Optional

from supertable.config.defaults import logger
from supertable.storage.storage_interface import StorageInterface

# Writers are split per-format
from supertable.mirroring.mirror_delta import write_delta_table
from supertable.mirroring.mirror_iceberg import write_iceberg_table


class FormatMirror(str, Enum):
    DELTA = "DELTA"
    ICEBERG = "ICEBERG"

    @staticmethod
    def normalize(values: Iterable[str]) -> List[str]:
        out: List[str] = []
        for v in values or []:
            try:
                out.append(FormatMirror[v.upper()].value)
            except Exception:
                # ignore unsupported entries silently
                continue
        # keep order, de-dup
        seen = set()
        ordered: List[str] = []
        for v in out:
            if v not in seen:
                seen.add(v)
                ordered.append(v)
        return ordered


def _ensure_meta(super_table) -> Dict[str, Any]:
    """
    Robustly obtain meta, creating a minimal _super.json if missing or empty.

    Rationale:
      enable_with_lock() used to fail with FileNotFoundError if _super.json
      wasn't created yet in this process (e.g., the caller constructs SuperTable
      in one code path but calls enable in another). We harden the read so that
      enabling mirrors is idempotent and safe to call anytime after SuperTable
      exists.
    """
    try:
        return super_table.get_super_meta()
    except (FileNotFoundError, ValueError):
        # Create folders + minimal meta if needed
        try:
            super_table.init_super_table()
        except Exception as e:
            logger.warning("[mirror] init_super_table() failed while ensuring meta: %s", e)
        # Read again (will raise if something is fundamentally wrong)
        return super_table.get_super_meta()


class MirrorFormats:
    """
    Stores/reads the enabled mirror formats in _super.json and triggers writers
    after a successful super snapshot update.
    """

    # ---------- config helpers (public) --------------------------------------
    @staticmethod
    def get_enabled(super_table) -> List[str]:
        meta = _ensure_meta(super_table)
        return list(meta.get("format_mirrors", []))

    @staticmethod
    def set_with_lock(super_table, formats: Iterable[str]) -> List[str]:
        enabled = FormatMirror.normalize(formats)
        if not super_table.locking.self_lock(
            timeout_seconds=super_table.config.default.DEFAULT_TIMEOUT_SEC
            if hasattr(super_table, "config") else 10,
            lock_duration_seconds=super_table.config.default.DEFAULT_LOCK_DURATION_SEC
            if hasattr(super_table, "config") else 30,
        ):
            raise RuntimeError("Failed to acquire lock to update format mirrors")

        try:
            meta = _ensure_meta(super_table)
            meta["format_mirrors"] = enabled
            super_table.storage.write_json(super_table.super_meta_path, meta)
            logger.info(f"[mirror] set formats = {enabled}")
            return enabled
        finally:
            super_table.locking.release_lock()

    @staticmethod
    def enable_with_lock(super_table, fmt: str) -> List[str]:
        current = MirrorFormats.get_enabled(super_table)
        wanted = FormatMirror.normalize(current + [fmt])
        return MirrorFormats.set_with_lock(super_table, wanted)

    @staticmethod
    def disable_with_lock(super_table, fmt: str) -> List[str]:
        current = MirrorFormats.get_enabled(super_table)
        fmt_up = fmt.upper()
        wanted = [f for f in current if f != fmt_up]
        return MirrorFormats.set_with_lock(super_table, wanted)

    # ---------- mirroring (internal) ----------------------------------------
    @staticmethod
    def mirror_if_enabled(
        super_table,
        table_name: str,
        simple_snapshot: Dict[str, Any],
        mirrors: Optional[List[str]] = None,
    ) -> None:
        """
        Run immediately after super snapshot update (caller holds the exclusive lock).
        """
        enabled = mirrors if mirrors is not None else MirrorFormats.get_enabled(super_table)
        if not enabled:
            return

        base = os.path.join(super_table.organization, super_table.super_name)

        # Ensure top-level dirs exist (lazy)
        if "DELTA" in enabled:
            super_table.storage.makedirs(os.path.join(base, "delta", table_name, "_delta_log"))
        if "ICEBERG" in enabled:
            super_table.storage.makedirs(os.path.join(base, "iceberg", table_name, "metadata"))
            super_table.storage.makedirs(os.path.join(base, "iceberg", table_name, "manifests"))

        # Delegate to per-format writers (latest-only mirror)
        if "DELTA" in enabled:
            write_delta_table(super_table, table_name, simple_snapshot)
        if "ICEBERG" in enabled:
            write_iceberg_table(super_table, table_name, simple_snapshot)

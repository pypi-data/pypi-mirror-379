"""Hierarchical variable persistence with optional globals migration."""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Sequence

from ...config import HOME_DIR, PROMPTS_DIR
from ...errorlog import get_logger
from ...features import is_variable_hierarchy_enabled


_LOG = get_logger(__name__)

HIERARCHICAL_VARIABLES_DIR = HOME_DIR / "variables"
HIERARCHICAL_VARIABLES_FILE = HIERARCHICAL_VARIABLES_DIR / "hierarchical-variables.json"


def _default_payload() -> dict[str, Any]:
    return {"version": 1, "namespaces": {}, "meta": {}}


class HierarchicalVariableStore:
    """Read/write accessor for hierarchical variables backed by JSON."""

    def __init__(self, *, path: Path | None = None) -> None:
        if not is_variable_hierarchy_enabled():
            raise RuntimeError("Hierarchical variable storage feature flag is disabled")
        self._path = path or HIERARCHICAL_VARIABLES_FILE
        self._payload: dict[str, Any] | None = None
        self._migration_checked = False

    # Public API ------------------------------------------------------------
    def get_value(self, namespace: str, path: Sequence[str], default: Any | None = None) -> Any | None:
        data = self._ensure_payload()
        node: Any = data.get("namespaces", {}).get(namespace, {})
        for key in path:
            if not isinstance(node, dict):
                return default
            node = node.get(key)
            if node is None:
                return default
        if isinstance(node, (dict, list)):
            return copy.deepcopy(node)
        return node

    def set_value(self, namespace: str, path: Sequence[str], value: Any) -> None:
        if not namespace:
            raise ValueError("namespace must be provided")
        if not path:
            raise ValueError("path must contain at least one key")
        data = self._ensure_payload()
        names = data.setdefault("namespaces", {})
        cursor = names.setdefault(namespace, {})
        if not isinstance(cursor, dict):
            cursor = {}
            names[namespace] = cursor
        for key in path[:-1]:
            child = cursor.get(key)
            if not isinstance(child, dict):
                child = {}
                cursor[key] = child
            cursor = child
        cursor[path[-1]] = copy.deepcopy(value)
        self._persist(data)

    def delete_value(self, namespace: str, path: Sequence[str]) -> bool:
        if not namespace or not path:
            return False
        data = self._ensure_payload()
        names = data.get("namespaces", {})
        cursor = names.get(namespace)
        if not isinstance(cursor, dict):
            return False
        trail: list[tuple[dict[str, Any], str]] = []
        node: Any = cursor
        for key in path:
            if not isinstance(node, dict) or key not in node:
                return False
            trail.append((node, key))
            node = node[key]
        parent, key = trail.pop()
        if key not in parent:
            return False
        parent.pop(key)
        removed = True
        while trail:
            holder, key = trail.pop()
            child = holder.get(key)
            if isinstance(child, dict) and not child:
                holder.pop(key, None)
            else:
                break
        if isinstance(cursor, dict) and not cursor:
            names.pop(namespace, None)
        self._persist(data)
        return removed

    def export_namespace(self, namespace: str) -> dict[str, Any]:
        data = self._ensure_payload()
        target = data.get("namespaces", {}).get(namespace, {})
        if isinstance(target, dict):
            return copy.deepcopy(target)
        return {}

    def list_namespaces(self) -> list[str]:
        data = self._ensure_payload()
        names = data.get("namespaces", {})
        if not isinstance(names, dict):
            return []
        return sorted(names.keys())

    # Internal helpers ------------------------------------------------------
    def _ensure_payload(self) -> dict[str, Any]:
        if self._payload is None:
            self._payload = self._load_payload()
        if not self._migration_checked:
            self._run_migration()
        return self._payload

    def _load_payload(self) -> dict[str, Any]:
        payload = _default_payload()
        if self._path.exists():
            try:
                loaded = json.loads(self._path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    if isinstance(loaded.get("namespaces"), dict):
                        payload["namespaces"] = loaded["namespaces"]
                    if isinstance(loaded.get("meta"), dict):
                        payload["meta"] = loaded["meta"]
                    if isinstance(loaded.get("version"), int):
                        payload["version"] = loaded["version"]
            except Exception as exc:  # pragma: no cover - defensive
                try:
                    _LOG.error("hierarchical_variables.read_failed", extra={"error": str(exc)})
                except Exception:
                    pass
        return payload

    def _run_migration(self) -> None:
        if self._payload is None:
            self._payload = _default_payload()
        payload = self._payload
        meta = payload.setdefault("meta", {})
        if meta.get("globals_migrated") is True:
            self._migration_checked = True
            return
        seeded = False
        try:
            _LOG.info("hierarchical_variables.migration_start")
        except Exception:
            pass
        globals_path = PROMPTS_DIR / "globals.json"
        if globals_path.exists():
            try:
                raw = json.loads(globals_path.read_text(encoding="utf-8"))
                gph = raw.get("global_placeholders")
                if isinstance(gph, dict):
                    namespace = payload.setdefault("namespaces", {}).setdefault("globals", {})
                    if not isinstance(namespace, dict):
                        namespace = {}
                        payload["namespaces"]["globals"] = namespace
                    for key, value in gph.items():
                        if key not in namespace:
                            namespace[key] = value
                            seeded = True
                notes = raw.get("notes")
                if isinstance(notes, dict) and "legacy_global_notes" not in meta:
                    meta["legacy_global_notes"] = notes
            except Exception as exc:  # pragma: no cover - defensive
                try:
                    _LOG.error("hierarchical_variables.migration_error", extra={"error": str(exc)})
                except Exception:
                    pass
        meta["globals_migrated"] = True
        self._migration_checked = True
        self._persist(payload)
        try:
            _LOG.info(
                "hierarchical_variables.migration_complete",
                extra={"seeded": bool(seeded)},
            )
        except Exception:
            pass

    def _persist(self, payload: dict[str, Any]) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self._path.with_suffix(".tmp")
            tmp.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
            tmp.replace(self._path)
        except Exception as exc:  # pragma: no cover - defensive
            try:
                _LOG.error("hierarchical_variables.persist_failed", extra={"error": str(exc)})
            except Exception:
                pass


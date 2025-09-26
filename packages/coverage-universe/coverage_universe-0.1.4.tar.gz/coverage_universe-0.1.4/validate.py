from __future__ import annotations

import json
from typing import Any, Dict, List, Tuple

try:
    import importlib.resources as ilr
except Exception:  # pragma: no cover
    ilr = None  # type: ignore

try:  # optional dependency
    import jsonschema  # type: ignore
except Exception:  # pragma: no cover
    jsonschema = None  # type: ignore


def _load_schema(rel_path: str) -> Dict[str, Any]:
    if ilr is None:
        raise RuntimeError("importlib.resources not available to load schema")
    data = ilr.files("coverage_universe").joinpath(rel_path).read_text(encoding="utf-8")
    return json.loads(data)


def _validate(data: Dict[str, Any], schema_rel_path: str) -> Tuple[bool, List[str]]:
    if jsonschema is None:
        return True, ["jsonschema not installed; skipping schema validation."]
    schema = _load_schema(schema_rel_path)
    validator = jsonschema.Draft202012Validator(schema)
    errs = sorted(validator.iter_errors(data), key=lambda e: e.path)
    messages: List[str] = []
    for e in errs:
        path = "/".join([str(p) for p in e.path])
        messages.append(f"{path or '$'}: {e.message}")
    return len(messages) == 0, messages


def validate_udl(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    return _validate(data, "schemas/udl.schema.json")


def validate_run(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    return _validate(data, "schemas/run.schema.json")


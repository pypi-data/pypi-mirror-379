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


def _semantic_udl_checks(data: Dict[str, Any]) -> List[str]:
    msgs: List[str] = []
    params = data.get("parameters", []) or []
    for p in params:
        name = p.get("name")
        ptype = p.get("type")
        parts = p.get("partitions", []) or []
        if ptype == "enum":
            seen = set()
            for part in parts:
                v = str(part.get("value"))
                if v in seen:
                    msgs.append(f"parameters/{name}: duplicate enum value '{v}'")
                seen.add(v)
        if ptype == "number":
            # check ranges: valid and non-overlapping
            ranges = []
            for part in parts:
                rng = part.get("range")
                try:
                    lo = float(rng[0])
                    hi = float(rng[1])
                except Exception:
                    continue
                if lo > hi:
                    lo, hi = hi, lo
                ranges.append((lo, hi))
            ranges.sort()
            for i in range(1, len(ranges)):
                prev = ranges[i-1]
                cur = ranges[i]
                # overlap if cur.lo < prev.hi (allow touching at boundary)
                if cur[0] < prev[1]:
                    msgs.append(f"parameters/{name}: overlapping numeric ranges {prev} and {cur}")
    return msgs


def validate_udl(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    ok_schema, msgs = _validate(data, "schemas/udl.schema.json")
    semantic = _semantic_udl_checks(data)
    all_msgs = msgs + semantic
    return ok_schema and len(semantic) == 0, all_msgs


def validate_run(data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    return _validate(data, "schemas/run.schema.json")

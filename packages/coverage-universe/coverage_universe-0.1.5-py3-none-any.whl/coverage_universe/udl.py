import json
import hashlib
from typing import Any, Dict, List, Tuple


def _sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def load_udl(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def universe_id(udl: Dict[str, Any]) -> str:
    canonical = json.dumps(udl, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return _sha1(canonical)


def normalize_parameters(udl: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    params_in = udl.get("parameters", [])
    normalized: List[Dict[str, Any]] = []
    errors: List[Dict[str, Any]] = []

    for p in params_in:
        name = p.get("name")
        ptype = p.get("type")
        if not name or not ptype:
            errors.append({"parameter": p, "error": "Missing name or type"})
            continue

        out = {
            "name": name,
            "type": ptype,
            "tags": p.get("tags", []),
        }

        if ptype == "enum":
            parts = []
            for part in p.get("partitions", []):
                if "value" not in part:
                    errors.append({"parameter": name, "error": "Enum partition missing 'value'"})
                    continue
                key = str(part["value"]).strip()
                weight = float(part.get("weight", 1.0))
                parts.append({
                    "key": key,
                    "label": key,
                    "weight": weight,
                })
            out["partitions"] = parts
        elif ptype == "number":
            parts = []
            minv = None
            maxv = None
            for part in p.get("partitions", []):
                if "range" not in part or not isinstance(part["range"], list) or len(part["range"]) != 2:
                    errors.append({"parameter": name, "error": "Number partition missing [min,max] range"})
                    continue
                lo = float(part["range"][0])
                hi = float(part["range"][1])
                if lo > hi:
                    lo, hi = hi, lo
                label = str(part.get("class", f"{lo}-{hi}"))
                weight = float(part.get("weight", 1.0))
                parts.append({
                    "key": label,
                    "label": label,
                    "range": [lo, hi],
                    "weight": weight,
                })
                minv = lo if minv is None else min(minv, lo)
                maxv = hi if maxv is None else max(maxv, hi)
            out["partitions"] = parts
            out["numeric_bounds"] = {"min": minv, "max": maxv}
            if p.get("boundary"):
                out["boundary"] = {
                    "include": list(p["boundary"].get("include", []))
                }
        else:
            errors.append({"parameter": name, "error": f"Unsupported type '{ptype}'"})
            continue

        normalized.append(out)

    return normalized, errors


def normalize_constraints(udl: Dict[str, Any]) -> List[Dict[str, Any]]:
    cons: List[Dict[str, Any]] = []
    for c in udl.get("constraints", []):
        if not isinstance(c, dict) or "if" not in c or "then" not in c:
            continue
        cons.append(c)
    return cons


def normalized_universe(udl: Dict[str, Any]) -> Dict[str, Any]:
    params, param_errors = normalize_parameters(udl)
    constraints = normalize_constraints(udl)
    meta = udl.get("metadata", {})
    cov = udl.get("coverage", {})
    return {
        "version": udl.get("version", "0.0.1"),
        "universe_id": universe_id(udl),
        "metadata": meta,
        "parameters": params,
        "constraints": constraints,
        "coverage": {
            "t_wise": int(cov.get("t_wise", 0)),
            "include_boundary": bool(cov.get("include_boundary", False)),
        },
        "errors": param_errors,
    }


def write_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


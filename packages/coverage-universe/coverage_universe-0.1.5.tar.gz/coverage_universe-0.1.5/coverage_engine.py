import itertools
from typing import Any, Dict, List, Set, Tuple


def _find_partition_for_value(param: Dict[str, Any], value: Any) -> str:
    ptype = param.get("type")
    if ptype == "enum":
        v = str(value)
        for part in param.get("partitions", []):
            if str(part["key"]) == v:
                return part["key"]
        return "__UNKNOWN__"
    if ptype == "number":
        try:
            x = float(value)
        except Exception:
            return "__UNKNOWN__"
        for part in param.get("partitions", []):
            lo, hi = part.get("range", [None, None])
            if lo is None or hi is None:
                continue
            if lo <= x <= hi:
                return part["key"]
        return "__OUT_OF_RANGE__"
    return "__UNSUPPORTED__"


def _boundary_hits(param: Dict[str, Any], value: Any, eps: float = 1e-9) -> List[str]:
    if param.get("type") != "number":
        return []
    if not param.get("boundary"):
        return []
    try:
        x = float(value)
    except Exception:
        return []
    bounds = param.get("numeric_bounds") or {}
    minv = bounds.get("min")
    maxv = bounds.get("max")
    include = set(param.get("boundary", {}).get("include", []))
    hits: List[str] = []
    if "min" in include and minv is not None and abs(x - float(minv)) <= eps:
        hits.append(f"B:{param['name']}=min")
    if "max" in include and maxv is not None and abs(x - float(maxv)) <= eps:
        hits.append(f"B:{param['name']}=max")
    # "just-inside" and "just-outside" are heuristic; require exact value at +/- eps from boundary
    if "just-inside" in include:
        if minv is not None and abs(x - (float(minv) + eps)) <= eps:
            hits.append(f"B:{param['name']}=just-inside")
        if maxv is not None and abs(x - (float(maxv) - eps)) <= eps:
            hits.append(f"B:{param['name']}=just-inside")
    if "just-outside" in include:
        if minv is not None and abs(x - (float(minv) - eps)) <= eps:
            hits.append(f"B:{param['name']}=just-outside")
        if maxv is not None and abs(x - (float(maxv) + eps)) <= eps:
            hits.append(f"B:{param['name']}=just-outside")
    return hits


def map_test_to_atoms(
    test_inputs: Dict[str, Any],
    universe: Dict[str, Any],
    atoms_index: Dict[str, Dict[str, Any]],
    *,
    boundary_eps: float = 1e-9,
) -> Tuple[Set[str], Dict[str, str]]:
    params = {p["name"]: p for p in universe.get("parameters", [])}
    covered: Set[str] = set()
    part_keys: Dict[str, str] = {}

    # Partition atoms and boundary atoms
    for pname, pdef in params.items():
        if pname not in test_inputs:
            continue
        v = test_inputs[pname]
        key = _find_partition_for_value(pdef, v)
        if key and not key.startswith("__"):
            atom_id = f"P:{pname}={key}"
            if atom_id in atoms_index:
                covered.add(atom_id)
                part_keys[pname] = key
        # boundary
        for bid in _boundary_hits(pdef, v, eps=boundary_eps):
            if bid in atoms_index:
                covered.add(bid)

    # t-wise atoms
    t_wise = int(universe.get("coverage", {}).get("t_wise", 0))
    if t_wise >= 2:
        names = sorted(part_keys.keys())
        for a, b in itertools.combinations(names, 2):
            aid = f"T2:{a}={part_keys[a]}|{b}={part_keys[b]}"
            bid = f"T2:{b}={part_keys[b]}|{a}={part_keys[a]}"  # canonical check in case of ordering
            if aid in atoms_index:
                covered.add(aid)
            elif bid in atoms_index:
                covered.add(bid)
    if t_wise >= 3:
        names = sorted(part_keys.keys())
        for a, b, c in itertools.combinations(names, 3):
            aid = f"T3:{a}={part_keys[a]}|{b}={part_keys[b]}|{c}={part_keys[c]}"
            if aid in atoms_index:
                covered.add(aid)

    return covered, part_keys


def compute_coverage(
    universe: Dict[str, Any],
    atoms: List[Dict[str, Any]],
    run: Dict[str, Any],
    *,
    only_passing: bool = False,
    only_failing: bool = False,
    boundary_eps: float = 1e-9,
) -> Dict[str, Any]:
    atoms_index = {a["id"]: a for a in atoms}
    all_ids = set(atoms_index.keys())
    by_kind = {
        "partition": {i["id"] for i in atoms if i["kind"] == "partition"},
        "t2": {i["id"] for i in atoms if i["kind"] == "t2"},
        "boundary": {i["id"] for i in atoms if i["kind"] == "boundary"},
    }
    t3_ids = {i["id"] for i in atoms if i.get("kind") == "t3"}
    if t3_ids:
        by_kind["t3"] = t3_ids
    # Precompute per-parameter atom groupings
    params = universe.get("parameters", [])
    part_by_param: Dict[str, Set[str]] = {}
    bound_by_param: Dict[str, Set[str]] = {}
    for p in params:
        pname = p.get("name")
        if not pname:
            continue
        part_by_param[pname] = set()
        bound_by_param[pname] = set()
    for aid in by_kind["partition"]:
        a = atoms_index.get(aid, {})
        pn = a.get("param")
        if pn in part_by_param:
            part_by_param[pn].add(aid)
    for aid in by_kind["boundary"]:
        a = atoms_index.get(aid, {})
        pn = a.get("param")
        if pn in bound_by_param:
            bound_by_param[pn].add(aid)

    covered: Set[str] = set()
    per_test: List[Dict[str, Any]] = []
    tests = run.get("tests", [])
    # outcome filtering
    if only_passing and only_failing:
        raise ValueError("only_passing and only_failing cannot both be true")
    outcome_map = {
        "passed": {"passed", "pass", "ok", "success"},
        "failed": {"failed", "fail", "error", "failure", "errored"},
        "skipped": {"skipped", "skip", "skipped"},
    }
    # count outcomes before filtering
    outcome_counts = {"passed": 0, "failed": 0, "skipped": 0, "other": 0}
    for t in tests:
        o = str(t.get("outcome", "")).lower()
        if o in outcome_map["passed"]:
            outcome_counts["passed"] += 1
        elif o in outcome_map["failed"]:
            outcome_counts["failed"] += 1
        elif o in outcome_map["skipped"]:
            outcome_counts["skipped"] += 1
        else:
            outcome_counts["other"] += 1

    if only_passing:
        tests = [t for t in tests if str(t.get("outcome", "")).lower() in outcome_map["passed"]]
    elif only_failing:
        tests = [t for t in tests if str(t.get("outcome", "")).lower() in outcome_map["failed"]]
    considered_tests_count = len(tests)
    total_tests_count = len(run.get("tests", []))
    for t in tests:
        test_inputs = t.get("inputs", {})
        cset, part_keys = map_test_to_atoms(test_inputs, universe, atoms_index, boundary_eps=boundary_eps)
        covered |= cset
        per_test.append({
            "test_id": t.get("test_id"),
            "covered": sorted(list(cset)),
            "partitions": part_keys,
        })

    def _weight_sum(ids: Set[str]) -> float:
        return sum(float(atoms_index[i].get("weight", 1.0)) for i in ids)

    totals = {}
    for kind, ids in by_kind.items():
        covered_k = covered & ids
        totals[kind] = {
            "covered": len(covered_k),
            "total": len(ids),
            "weightedCovered": _weight_sum(covered_k),
            "weightedTotal": _weight_sum(ids),
        }

    # Top uncovered atoms by weight desc
    uncovered_ids = all_ids - covered
    top_uncovered = sorted(uncovered_ids, key=lambda i: atoms_index[i].get("weight", 1.0), reverse=True)[:20]

    # Per-parameter breakdown (partitions, and boundaries if present)
    by_parameter: Dict[str, Dict[str, Any]] = {}
    for pname in sorted(part_by_param.keys()):
        p_part = part_by_param[pname]
        cov_part = covered & p_part
        entry: Dict[str, Any] = {
            "partition": {
                "covered": len(cov_part),
                "total": len(p_part),
                "weightedCovered": _weight_sum(cov_part),
                "weightedTotal": _weight_sum(p_part),
                "uncovered": sorted(list(p_part - covered), key=lambda i: atoms_index[i].get("weight", 1.0), reverse=True),
            }
        }
        p_bound = bound_by_param.get(pname) or set()
        if p_bound:
            cov_bound = covered & p_bound
            entry["boundary"] = {
                "covered": len(cov_bound),
                "total": len(p_bound),
                "weightedCovered": _weight_sum(cov_bound),
                "weightedTotal": _weight_sum(p_bound),
                "uncovered": sorted(list(p_bound - covered), key=lambda i: atoms_index[i].get("weight", 1.0), reverse=True),
            }
        by_parameter[pname] = entry

    # By-tag breakdown (aggregate partition atoms across parameters sharing a tag)
    tag_to_params: Dict[str, Set[str]] = {}
    for p in params:
        pname = p.get("name")
        for tag in p.get("tags", []) or []:
            tag_to_params.setdefault(str(tag), set()).add(pname)
    by_tag: Dict[str, Dict[str, Any]] = {}
    for tag, pnames in tag_to_params.items():
        tag_parts: Set[str] = set()
        for pn in pnames:
            tag_parts |= part_by_param.get(pn, set())
        cov_tag_parts = covered & tag_parts
        by_tag[tag] = {
            "partition": {
                "covered": len(cov_tag_parts),
                "total": len(tag_parts),
                "weightedCovered": _weight_sum(cov_tag_parts),
                "weightedTotal": _weight_sum(tag_parts),
            }
        }

    return {
        "universe_id": universe.get("universe_id"),
        "run_id": run.get("run_id"),
        "totals": totals,
        "covered_count": len(covered),
        "total_atoms": len(all_ids),
        "top_uncovered": top_uncovered,
        "per_test": per_test,
        "by_parameter": by_parameter,
        "by_tag": by_tag,
        "outcomes": outcome_counts,
        "tests_total": total_tests_count,
        "tests_considered": considered_tests_count,
        "filter": (
            "only_passing" if only_passing else ("only_failing" if only_failing else "all")
        ),
        "boundary_eps": boundary_eps,
    }

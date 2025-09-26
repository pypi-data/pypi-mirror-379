from typing import Any, Dict, List, Tuple, Iterable


def _partition_atoms(params: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    atoms: List[Dict[str, Any]] = []
    for p in params:
        name = p["name"]
        for part in p.get("partitions", []):
            key = part["key"]
            weight = float(part.get("weight", 1.0))
            atom_id = f"P:{name}={key}"
            atoms.append({
                "id": atom_id,
                "kind": "partition",
                "param": name,
                "key": key,
                "weight": weight,
            })
    return atoms


def _boundary_atoms(params: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    atoms: List[Dict[str, Any]] = []
    for p in params:
        if p.get("type") != "number":
            continue
        b = p.get("boundary") or {}
        include = b.get("include") or []
        for kind in include:
            if kind not in ("min", "max", "just-inside", "just-outside"):
                continue
            atom_id = f"B:{p['name']}={kind}"
            atoms.append({
                "id": atom_id,
                "kind": "boundary",
                "param": p["name"],
                "key": kind,
                "weight": 1.0,
            })
    return atoms


def _constraints_contradict(assignments: Dict[str, str], constraints: List[Dict[str, Any]]) -> bool:
    # MVP: handle only enum equality and simple not-equals like {"then": {param: {"not": value}}}
    for c in constraints:
        cond_if = c.get("if", {})
        then = c.get("then", {})
        # Check if 'if' matches given assignments where keys overlap
        matches = True
        for pn, pv in cond_if.items():
            if pn in assignments and str(assignments[pn]) != str(pv):
                matches = False
                break
            if pn not in assignments:
                # Can't confirm, treat as unknown → non-blocking
                matches = False
                break
        if not matches:
            continue
        # If 'if' fully matches our assignments, ensure 'then' is not violated for overlapping params
        for pn, rule in then.items():
            # support {pn: value} and {pn: {"not": value}}
            if isinstance(rule, dict) and "not" in rule:
                if pn in assignments and str(assignments[pn]) == str(rule["not"]):
                    return True
            else:
                if pn in assignments and str(assignments[pn]) != str(rule):
                    return True
    return False


def _twise_atoms(params: List[Dict[str, Any]], constraints: List[Dict[str, Any]], t: int) -> List[Dict[str, Any]]:
    import itertools
    atoms: List[Dict[str, Any]] = []
    # Build map param -> partition keys + weights
    pmap: Dict[str, List[Tuple[str, float]]] = {}
    for p in params:
        keys_weights = [(part["key"], float(part.get("weight", 1.0))) for part in p.get("partitions", [])]
        pmap[p["name"]] = keys_weights

    names = [p["name"] for p in params if p.get("partitions")]
    for group in itertools.combinations(names, t):
        lists = [pmap[n] for n in group]
        for combo in itertools.product(*lists):
            assign = {n: kw[0] for n, kw in zip(group, combo)}
            if _constraints_contradict(assign, constraints):
                continue
            keys = [kw[0] for kw in combo]
            weights = [kw[1] for kw in combo]
            # Canonical order already ensured by combinations
            id_parts = [f"{n}={k}" for n, k in zip(group, keys)]
            aid = f"T{t}:{'|'.join(id_parts)}"
            atoms.append({
                "id": aid,
                "kind": f"t{t}",
                "params": list(group),
                "keys": keys,
                "weight": sum(weights) / float(len(weights) or 1.0),
            })
    return atoms


def build_atoms(universe: Dict[str, Any]) -> List[Dict[str, Any]]:
    params = universe.get("parameters", [])
    constraints = universe.get("constraints", [])

    atoms: List[Dict[str, Any]] = []
    atoms.extend(_partition_atoms(params))

    if universe.get("coverage", {}).get("include_boundary"):
        atoms.extend(_boundary_atoms(params))

    t_wise = int(universe.get("coverage", {}).get("t_wise", 0))
    if t_wise >= 2:
        atoms.extend(_twise_atoms(params, constraints, 2))
    if t_wise >= 3:
        atoms.extend(_twise_atoms(params, constraints, 3))

    return atoms


def index_atoms(atoms: Iterable[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {a["id"]: a for a in atoms}

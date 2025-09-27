from coverage_universe import udl as udl_mod
from coverage_universe import atoms as atoms_mod
from coverage_universe import coverage_engine as ce


def _uni_num_boundary():
    udl = {
        "parameters": [
            {
                "name": "n",
                "type": "number",
                "partitions": [
                    {"range": [0, 1], "class": "low"},
                    {"range": [1, 2], "class": "high"}
                ],
                "boundary": {"include": ["min", "max", "just-inside", "just-outside"]},
            }
        ],
        "coverage": {"include_boundary": True},
    }
    return udl_mod.normalized_universe(udl)


def test_boundary_hits_min_max_inside_outside_with_eps():
    uni = _uni_num_boundary()
    ats = atoms_mod.build_atoms(uni)
    idx = atoms_mod.index_atoms(ats)
    eps = 1e-9
    # exact min -> min boundary
    covered, _ = ce.map_test_to_atoms({"n": 0.0}, uni, idx, boundary_eps=eps)
    assert "B:n=min" in covered
    # just-inside near min
    covered, _ = ce.map_test_to_atoms({"n": 0.0 + eps}, uni, idx, boundary_eps=eps)
    assert "B:n=just-inside" in covered
    # exact max -> max boundary
    covered, _ = ce.map_test_to_atoms({"n": 2.0}, uni, idx, boundary_eps=eps)
    assert "B:n=max" in covered
    # just-inside near max
    covered, _ = ce.map_test_to_atoms({"n": 2.0 - eps}, uni, idx, boundary_eps=eps)
    assert "B:n=just-inside" in covered
    # just-outside
    covered, _ = ce.map_test_to_atoms({"n": -eps}, uni, idx, boundary_eps=eps)
    assert "B:n=just-outside" in covered


def test_t3_mapping_when_present():
    udl = {
        "parameters": [
            {"name": "a", "type": "enum", "partitions": [{"value": 1}, {"value": 2}]},
            {"name": "b", "type": "enum", "partitions": [{"value": "x"}]},
            {"name": "c", "type": "enum", "partitions": [{"value": True}]},
        ],
        "coverage": {"t_wise": 3},
    }
    uni = udl_mod.normalized_universe(udl)
    ats = atoms_mod.build_atoms(uni)
    idx = atoms_mod.index_atoms(ats)
    # map a full assignment
    covered, parts = ce.map_test_to_atoms({"a": 1, "b": "x", "c": True}, uni, idx)
    # t3 atom id should be present in atoms and covered
    tid = "T3:a=1|b=x|c=True"
    assert tid in idx
    assert tid in covered

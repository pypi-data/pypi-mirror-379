from coverage_universe import atoms as atoms_mod


def test_constraints_contradict_and_twise_generation():
    params = [
        {"name": "A", "type": "enum", "partitions": [{"key": "x"}, {"key": "y"}]},
        {"name": "B", "type": "enum", "partitions": [{"key": "u"}, {"key": "v"}]},
        {"name": "C", "type": "enum", "partitions": [{"key": "k"}]},
    ]
    constraints = [
        {"if": {"A": "x"}, "then": {"B": {"not": "v"}}},
    ]
    # t2 should exclude A=x & B=v but include others
    t2 = [a for a in atoms_mod._twise_atoms(params, constraints, 2) if a["kind"] == "t2"]
    ids = {a["id"] for a in t2}
    assert "T2:A=x|B=v" not in ids
    assert "T2:A=x|B=u" in ids
    # t3 should exist for combinations across A,B,C respecting constraints
    t3 = [a for a in atoms_mod._twise_atoms(params, constraints, 3) if a["kind"] == "t3"]
    ids3 = {a["id"] for a in t3}
    assert any(i.startswith("T3:") for i in ids3)


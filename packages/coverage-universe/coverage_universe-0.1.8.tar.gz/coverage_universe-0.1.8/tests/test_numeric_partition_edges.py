from coverage_universe import udl as udl_mod
from coverage_universe import atoms as atoms_mod
from coverage_universe import coverage_engine as ce


def test_adjacent_numeric_ranges_map_boundary_to_upper_partition():
    udl = {
        "parameters": [
            {
                "name": "n",
                "type": "number",
                "partitions": [
                    {"range": [0, 1], "class": "low"},
                    {"range": [1, 2], "class": "high"},
                ],
            }
        ]
    }
    uni = udl_mod.normalized_universe(udl)
    ats = atoms_mod.build_atoms(uni)
    idx = atoms_mod.index_atoms(ats)
    covered, _ = ce.map_test_to_atoms({"n": 1.0}, uni, idx)
    assert "P:n=high" in covered
    assert "P:n=low" not in covered


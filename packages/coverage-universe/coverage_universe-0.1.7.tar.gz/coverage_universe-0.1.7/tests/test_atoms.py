import json

from coverage_universe import atoms as atoms_mod
from coverage_universe import udl as udl_mod


def test_build_atoms_partition_and_boundary():
  udl = {
    "parameters": [
      {"name": "p", "type": "enum", "partitions": [{"value": "A"}, {"value": "B"}]},
      {"name": "n", "type": "number", "partitions": [
        {"range": [0, 1], "class": "low"},
        {"range": [1, 2], "class": "high"}
      ], "boundary": {"include": ["min", "max"]}}
    ],
    "coverage": {"t_wise": 2, "include_boundary": True},
  }
  uni = udl_mod.normalized_universe(udl)
  ats = atoms_mod.build_atoms(uni)
  ids = {a["id"] for a in ats}
  # partition atoms
  assert "P:p=A" in ids and "P:p=B" in ids
  assert "P:n=low" in ids and "P:n=high" in ids
  # boundary atoms
  assert "B:n=min" in ids and "B:n=max" in ids
  # pairwise atoms (subset check)
  assert any(i.startswith("T2:") for i in ids)


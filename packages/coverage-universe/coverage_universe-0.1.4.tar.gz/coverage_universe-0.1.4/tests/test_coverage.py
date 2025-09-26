from coverage_universe import coverage_engine as cov
from coverage_universe import atoms as atoms_mod
from coverage_universe import udl as udl_mod


def _example():
  udl = {
    "parameters": [
      {"name": "browser", "type": "enum", "partitions": [{"value": "Chrome"}, {"value": "Firefox"}]},
      {"name": "lat", "type": "number", "partitions": [
        {"range": [0, 100], "class": "low"},
        {"range": [100, 200], "class": "high"}
      ], "boundary": {"include": ["min", "max"]}}
    ],
    "coverage": {"t_wise": 2, "include_boundary": True},
  }
  uni = udl_mod.normalized_universe(udl)
  ats = atoms_mod.build_atoms(uni)
  return uni, ats


def test_compute_coverage_basic_and_filters():
  uni, ats = _example()
  run = {
    "run_id": "r1",
    "tests": [
      {"test_id": "t1", "outcome": "passed", "inputs": {"browser": "Chrome", "lat": 0}},
      {"test_id": "t2", "outcome": "failed", "inputs": {"browser": "Firefox", "lat": 100}},
    ]
  }
  c_all = cov.compute_coverage(uni, ats, run)
  assert c_all["totals"]["partition"]["covered"] >= 3
  assert c_all["outcomes"]["passed"] == 1 and c_all["outcomes"]["failed"] == 1

  c_pass = cov.compute_coverage(uni, ats, run, only_passing=True)
  assert c_pass["tests_considered"] == 1

  c_fail = cov.compute_coverage(uni, ats, run, only_failing=True)
  assert c_fail["tests_considered"] == 1


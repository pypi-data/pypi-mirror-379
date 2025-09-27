import json
from pathlib import Path

from coverage_universe import cli as cli_mod


def test_cli_end_to_end(tmp_path: Path):
    udl_path = tmp_path / "udl.json"
    atoms_path = tmp_path / "atoms.json"
    run_in = tmp_path / "run.json"
    run_norm = tmp_path / "run.norm.json"
    cov_path = tmp_path / "coverage.json"
    html_path = tmp_path / "coverage.html"

    udl = {
        "parameters": [
            {"name": "p", "type": "enum", "partitions": [{"value": "A"}, {"value": "B"}]},
            {"name": "n", "type": "number", "partitions": [{"range": [0, 1], "class": "lo"}], "boundary": {"include": ["min"]}},
        ],
        "coverage": {"t_wise": 2, "include_boundary": True},
    }
    run = {
        "run_id": "r",
        "tests": [
            {"test_id": "t1", "outcome": "passed", "inputs": {"p": "A", "n": 0}},
            {"test_id": "t2", "outcome": "failed", "inputs": {"p": "B", "n": 0}},
        ],
    }
    udl_path.write_text(json.dumps(udl), encoding="utf-8")
    run_in.write_text(json.dumps(run), encoding="utf-8")

    assert cli_mod.main(["build-universe", "--udl", str(udl_path), "--out", str(atoms_path)]) == 0
    assert atoms_path.exists()
    assert cli_mod.main(["ingest", "--run", str(run_in), "--out", str(run_norm)]) == 0
    assert run_norm.exists()
    assert cli_mod.main([
        "compute", "--atoms", str(atoms_path), "--evidence", str(run_norm), "--out", str(cov_path), "--only-passing"
    ]) == 0
    assert cov_path.exists()
    assert cli_mod.main(["report", "--coverage", str(cov_path), "--html", str(html_path)]) == 0
    assert html_path.exists()


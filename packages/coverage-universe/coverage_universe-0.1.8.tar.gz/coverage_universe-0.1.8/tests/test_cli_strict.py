import json
from pathlib import Path

import pytest

from coverage_universe import cli as cli_mod


def test_build_universe_strict_warns_on_touching_ranges(tmp_path: Path):
    # Touching ranges at 10 should trigger a warning and strict mode should abort
    udl_path = tmp_path / "udl.json"
    atoms_path = tmp_path / "atoms.json"
    udl = {
        "parameters": [
            {
                "name": "n",
                "type": "number",
                "partitions": [
                    {"range": [0, 10], "class": "lo"},
                    {"range": [10, 20], "class": "hi"},
                ],
            }
        ]
    }
    udl_path.write_text(json.dumps(udl), encoding="utf-8")

    with pytest.raises(SystemExit) as exc:
        cli_mod.main(["build-universe", "--udl", str(udl_path), "--out", str(atoms_path), "--strict"])
    # Strict mode uses exit code 3
    assert exc.value.code == 3


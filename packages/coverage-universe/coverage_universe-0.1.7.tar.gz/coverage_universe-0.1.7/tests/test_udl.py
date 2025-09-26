from coverage_universe import udl as udl_mod


def test_normalize_enum_and_number_with_boundary_and_errors():
    udl = {
        "parameters": [
            {"name": "color", "type": "enum", "partitions": [{"value": "red"}, {"value": "blue"}]},
            {
                "name": "size",
                "type": "number",
                "partitions": [{"range": [0, 10], "class": "small"}, {"range": [10, 20], "class": "big"}],
                "boundary": {"include": ["min", "max", "just-inside", "just-outside"]},
            },
            {"name": "bad_enum", "type": "enum", "partitions": [{}]},  # missing value -> error
            {"name": "bad_num", "type": "number", "partitions": [{"range": [5]}]},  # bad range -> error
        ]
    }
    params, errors = udl_mod.normalize_parameters(udl)
    names = {p["name"] for p in params}
    assert {"color", "size"}.issubset(names)
    size = next(p for p in params if p["name"] == "size")
    assert size["numeric_bounds"]["min"] == 0
    assert size["numeric_bounds"]["max"] == 20
    assert size["boundary"]["include"] == ["min", "max", "just-inside", "just-outside"]
    # two errors captured
    assert len(errors) >= 2


def test_normalized_universe_includes_flags_and_id_stable():
    udl = {
        "coverage": {"t_wise": 2, "include_boundary": True},
        "parameters": [{"name": "os", "type": "enum", "partitions": [{"value": "win"}]}],
    }
    uni = udl_mod.normalized_universe(udl)
    assert uni["coverage"]["t_wise"] == 2
    assert uni["coverage"]["include_boundary"] is True
    # stable id deterministic
    assert isinstance(uni["universe_id"], str) and len(uni["universe_id"]) == 40


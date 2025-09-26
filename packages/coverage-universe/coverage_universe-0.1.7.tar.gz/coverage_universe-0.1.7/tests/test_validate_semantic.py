from coverage_universe import validate as validate_mod


def test_semantic_validation_overlapping_ranges_and_duplicate_enum():
    udl = {
        "parameters": [
            {"name": "dup", "type": "enum", "partitions": [{"value": "A"}, {"value": "A"}]},
            {"name": "rng", "type": "number", "partitions": [
                {"range": [0, 10]}, {"range": [9, 20]}
            ]}
        ]
    }
    ok, msgs = validate_mod.validate_udl(udl)
    assert not ok
    assert any("duplicate enum value" in m for m in msgs)
    assert any("overlapping numeric ranges" in m for m in msgs)


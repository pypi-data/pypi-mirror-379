from coverage_universe import report as report_mod


def test_render_html_includes_sections():
    cov = {
        "universe_id": "u",
        "run_id": "r",
        "covered_count": 1,
        "total_atoms": 2,
        "totals": {
            "partition": {"covered": 1, "total": 1, "weightedCovered": 1.0, "weightedTotal": 1.0},
            "t2": {"covered": 0, "total": 1, "weightedCovered": 0.0, "weightedTotal": 1.0},
            "boundary": {"covered": 0, "total": 0, "weightedCovered": 0.0, "weightedTotal": 0.0},
        },
        "top_uncovered": ["X"],
        "by_parameter": {"p": {"partition": {"covered": 1, "total": 1, "weightedCovered": 1.0, "weightedTotal": 1.0, "uncovered": []}}},
        "by_tag": {"tag": {"partition": {"covered": 1, "total": 1, "weightedCovered": 1.0, "weightedTotal": 1.0}}},
        "outcomes": {"passed": 1, "failed": 0, "skipped": 0, "other": 0},
        "tests_total": 1,
        "tests_considered": 1,
        "filter": "all",
        "boundary_eps": 1e-9,
    }
    html = report_mod.render_html(cov)
    assert "Coverage Report" in html
    assert "Totals" in html and "By Parameter" in html and "By Tag" in html


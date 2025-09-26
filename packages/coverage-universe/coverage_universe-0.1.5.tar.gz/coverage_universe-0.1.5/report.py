import json
from typing import Any, Dict


def write_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def render_html(coverage: Dict[str, Any]) -> str:
    # Minimal self-contained HTML with basic sections
    totals = coverage.get("totals", {})
    def pct():
        total = max(int(coverage.get("total_atoms", 1)), 1)
        return int(100 * int(coverage.get("covered_count", 0)) / total)
    parts = []
    parts.append("<meta charset='utf-8'>")
    parts.append("<style>body{font-family:system-ui,Segoe UI,Arial,sans-serif;margin:20px;} h1{margin-bottom:0;} small{color:#666;} table{border-collapse:collapse;margin:8px 0;} th,td{border:1px solid #ddd;padding:4px 8px;} code{background:#f6f8fa;padding:2px 4px;border-radius:3px;}</style>")
    parts.append("<h1>Coverage Report</h1>")
    parts.append(f"<small>Universe: {coverage.get('universe_id','')} &nbsp; Run: {coverage.get('run_id','')}</small>")

    parts.append("<h2>Totals</h2>")
    parts.append("<ul>")
    for k in ("partition", "t2", "t3", "boundary"):
        if k in totals:
            t = totals[k]
            parts.append(
                f"<li>{k}: {t['covered']}/{t['total']} (weighted {t['weightedCovered']:.2f}/{t['weightedTotal']:.2f})</li>"
            )
    parts.append("</ul>")
    parts.append(f"<p><strong>Overall</strong>: {coverage.get('covered_count',0)}/{coverage.get('total_atoms',0)} ({pct()}%)</p>")

    # Outcome summary
    oc = coverage.get("outcomes", {})
    tests_total = coverage.get("tests_total", 0)
    tests_considered = coverage.get("tests_considered", tests_total)
    filt = coverage.get("filter", "all")
    beps = coverage.get("boundary_eps", 1e-9)
    parts.append(
        f"<p><strong>Tests</strong>: considered {tests_considered}/{tests_total} (filter: <code>{filt}</code>), boundary eps: <code>{beps}</code> | outcomes: passed={oc.get('passed',0)}, failed={oc.get('failed',0)}, skipped={oc.get('skipped',0)}, other={oc.get('other',0)}</p>"
    )

    # Per-parameter breakdown
    by_param = coverage.get("by_parameter", {})
    if by_param:
        parts.append("<h2>By Parameter</h2>")
        parts.append("<table><thead><tr><th>Parameter</th><th>Partitions</th><th>Boundary</th><th>Uncovered (top)</th></tr></thead><tbody>")
        for pname, info in by_param.items():
            p = info.get("partition", {})
            b = info.get("boundary", {})
            part_txt = f"{p.get('covered',0)}/{p.get('total',0)} (w {p.get('weightedCovered',0.0):.2f}/{p.get('weightedTotal',0.0):.2f})"
            b_txt = "-"
            if b:
                b_txt = f"{b.get('covered',0)}/{b.get('total',0)} (w {b.get('weightedCovered',0.0):.2f}/{b.get('weightedTotal',0.0):.2f})"
            # Show at most 5 uncovered partition atoms for brevity
            ulist = [f"<code>{aid}</code>" for aid in (p.get("uncovered") or [])[:5]]
            parts.append(f"<tr><td>{pname}</td><td>{part_txt}</td><td>{b_txt}</td><td>{', '.join(ulist)}</td></tr>")
        parts.append("</tbody></table>")

    # By-tag breakdown
    by_tag = coverage.get("by_tag", {})
    if by_tag:
        parts.append("<h2>By Tag</h2>")
        parts.append("<table><thead><tr><th>Tag</th><th>Partitions</th></tr></thead><tbody>")
        for tag, info in by_tag.items():
            p = info.get("partition", {})
            part_txt = f"{p.get('covered',0)}/{p.get('total',0)} (w {p.get('weightedCovered',0.0):.2f}/{p.get('weightedTotal',0.0):.2f})"
            parts.append(f"<tr><td>{tag}</td><td>{part_txt}</td></tr>")
        parts.append("</tbody></table>")

    parts.append("<h2>Top Uncovered</h2>")
    parts.append("<ol>")
    for aid in coverage.get("top_uncovered", []):
        parts.append(f"<li><code>{aid}</code></li>")
    parts.append("</ol>")

    parts.append("<h2>Raw JSON</h2>")
    raw = json.dumps(coverage, indent=2)
    parts.append(f"<pre>{raw}</pre>")
    return "\n".join(parts)

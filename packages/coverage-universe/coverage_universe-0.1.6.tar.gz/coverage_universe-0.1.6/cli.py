import argparse
import json
import os
from typing import Any, Dict

from . import udl as udl_mod
from . import atoms as atoms_mod
from . import coverage_engine as cov_mod
from . import report as report_mod
from . import validate as validate_mod


def cmd_build_universe(args: argparse.Namespace) -> int:
    udl = udl_mod.load_udl(args.udl)
    if args.validate:
        ok, msgs = validate_mod.validate_udl(udl)
        if not ok:
            print("UDL schema validation failed:")
            for m in msgs:
                print(f" - {m}")
            raise SystemExit(2)
        # If jsonschema not installed, msgs will contain a notice
        for m in msgs:
            if "skipping schema validation" in m:
                print(m)
    uni = udl_mod.normalized_universe(udl)
    atoms = atoms_mod.build_atoms(uni)
    out = {
        "universe": uni,
        "atoms": atoms,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Wrote atoms to {args.out} (universe_id={uni['universe_id']})")
    if uni.get("errors"):
        print(f"Note: {len(uni['errors'])} parameter issues found; see output JSON under 'universe.errors'.")
    return 0


def cmd_ingest(args: argparse.Namespace) -> int:
    with open(args.run, "r", encoding="utf-8") as f:
        run = json.load(f)
    if args.validate:
        ok, msgs = validate_mod.validate_run(run)
        if not ok:
            print("Run schema validation failed:")
            for m in msgs:
                print(f" - {m}")
            raise SystemExit(2)
        for m in msgs:
            if "skipping schema validation" in m:
                print(m)
    # Basic validation and light normalization
    tests_in = run.get("tests")
    if not isinstance(tests_in, list):
        raise SystemExit("Run JSON must contain 'tests' array")
    normalized_tests = []
    dropped = 0
    for idx, t in enumerate(tests_in):
        if not isinstance(t, dict):
            dropped += 1
            continue
        inputs = t.get("inputs")
        if not isinstance(inputs, dict):
            dropped += 1
            continue
        # Coerce outcome to lower string if present
        if "outcome" in t and not isinstance(t["outcome"], str):
            t = {**t, "outcome": str(t["outcome"]) }
        normalized_tests.append(t)
    out_run = {**run, "tests": normalized_tests}
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out_run, f, indent=2, ensure_ascii=False)
    msg = f"Wrote normalized run to {args.out}"
    if dropped:
        msg += f" (dropped {dropped} invalid test(s))"
    print(msg)
    return 0


def cmd_compute(args: argparse.Namespace) -> int:
    with open(args.atoms, "r", encoding="utf-8") as f:
        atoms_bundle = json.load(f)
    universe = atoms_bundle.get("universe")
    atoms = atoms_bundle.get("atoms", [])
    with open(args.evidence, "r", encoding="utf-8") as f:
        run = json.load(f)
    if args.only_passing and args.only_failing:
        raise SystemExit("--only-passing and --only-failing are mutually exclusive")
    cov = cov_mod.compute_coverage(
        universe,
        atoms,
        run,
        only_passing=bool(args.only_passing),
        only_failing=bool(args.only_failing),
        boundary_eps=float(args.boundary_eps),
    )
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(cov, f, indent=2, ensure_ascii=False)
    print(f"Wrote coverage to {args.out}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    with open(args.coverage, "r", encoding="utf-8") as f:
        cov = json.load(f)
    if args.html:
        html = report_mod.render_html(cov)
        with open(args.html, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Wrote HTML report to {args.html}")
    else:
        # print summary to stdout
        print(json.dumps(cov, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="coverage_universe", description="Coverage over a modeled test universe")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build-universe", help="Build atom set from UDL")
    b.add_argument("--udl", required=True, help="Path to UDL JSON")
    b.add_argument("--out", required=True, help="Output atoms JSON path")
    b.add_argument("--validate", action="store_true", help="Validate UDL JSON against schema")
    b.set_defaults(func=cmd_build_universe)

    i = sub.add_parser("ingest", help="Ingest a test run JSON")
    i.add_argument("--run", required=True, help="Run JSON path")
    i.add_argument("--out", required=True, help="Output normalized run JSON path")
    i.add_argument("--validate", action="store_true", help="Validate run JSON against schema")
    i.set_defaults(func=cmd_ingest)

    c = sub.add_parser("compute", help="Compute coverage from atoms and evidence")
    c.add_argument("--atoms", required=True, help="Atoms JSON from build-universe")
    c.add_argument("--evidence", required=True, help="Ingested run JSON")
    c.add_argument("--out", required=True, help="Coverage JSON output path")
    c.add_argument("--only-passing", action="store_true", help="Count coverage from passing tests only")
    c.add_argument("--only-failing", action="store_true", help="Count coverage from failing tests only")
    c.add_argument("--boundary-eps", default=1e-9, help="Epsilon tolerance for numeric boundary hits")
    c.set_defaults(func=cmd_compute)

    r = sub.add_parser("report", help="Render a coverage report")
    r.add_argument("--coverage", required=True, help="Coverage JSON path")
    r.add_argument("--html", help="Write HTML report to path (optional)")
    r.set_defaults(func=cmd_report)

    return p


def main(argv: Any = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

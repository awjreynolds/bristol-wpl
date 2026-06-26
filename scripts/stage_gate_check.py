#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOSED_STATUSES = {"closed", "resolved", "accepted_closed", "controlled"}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def is_closed(status: str | None) -> bool:
    return (status or "").strip().lower() in CLOSED_STATUSES


def collect_open_blockers() -> tuple[list[str], list[str]]:
    p0_blockers: list[str] = []
    p1_blockers: list[str] = []
    for row in read_rows("governance/issues_register.csv"):
        status = row.get("status", "")
        if is_closed(status):
            continue
        issue_id = row.get("issue_id", "<unknown>")
        severity = row.get("severity", "")
        if severity == "P0":
            p0_blockers.append(f"{issue_id} issue is {status}")
        elif severity == "P1":
            p1_blockers.append(f"{issue_id} issue is {status}")
    for row in read_rows("governance/risk_register.csv"):
        status = row.get("status", "")
        if is_closed(status):
            continue
        risk_id = row.get("risk_id", "<unknown>")
        if row.get("gross_rating") == "P0" or row.get("residual_rating") == "P0":
            p0_blockers.append(f"{risk_id} risk is {status}")
        elif row.get("gross_rating") == "P1" or row.get("residual_rating") == "P1":
            p1_blockers.append(f"{risk_id} risk is {status}")
    return p0_blockers, p1_blockers


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", choices=["obc", "fbc"])
    parser.add_argument("--red-team", action="store_true")
    args = parser.parse_args()

    if args.red_team:
        print("Create bounded red-team packet before use; this target does not pass any readiness gate.")
        return 0
    if not args.gate:
        print("ERROR: specify --gate or --red-team", file=sys.stderr)
        return 2

    p0_blockers, p1_blockers = collect_open_blockers()
    if p0_blockers or p1_blockers:
        for blocker in p0_blockers:
            print(f"ERROR: open P0 blocker for {args.gate} gate: {blocker}", file=sys.stderr)
        for blocker in p1_blockers:
            print(f"ERROR: open P1 blocker for {args.gate} gate requires condition owner deadline and residual risk: {blocker}", file=sys.stderr)
        return 1
    print(f"{args.gate.upper()} gate passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_registers import check_no_authored_pdfs

README = ROOT / "README.md"
OPEN_STATUSES = {
    "open",
    "controlled_open",
    "narrowed_open",
    "controlled_open_external_check_required",
    "blocked_external_gitguardian_check",
    "partially_closed_stage_16a",
}

REQUIRED_README_IDS = {
    "ISS-0036",
    "EG-0054",
}

REQUIRED_DASHBOARD_IDS = REQUIRED_README_IDS | {"RISK-0039"}

REQUIRED_PUBLIC_PHRASES = {
    "README.md": [
        "Stage 26A",
        "validation evidence log controls",
        "ISS-0036",
        "EG-0054",
    ],
    "docs/officer/assurance-dashboard.md": [
        "Validation evidence logging",
        "Stage 26A records validation evidence logs.",
        "scripts/validate_validation_evidence_log.py",
    ],
    "docs/stages/README.md": [
        "Stage 26A",
        "validation evidence log",
    ],
    "docs/visuals/stage-gate-map.mmd": [
        "Stage 26A",
        "Validation evidence logging",
    ],
    "docs/visuals/risk-control-atlas.mmd": [
        "Validation evidence log",
        "ISS-0036 EG-0054 RISK-0039",
    ],
}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def register_lookup(rel: str, id_column: str) -> dict[str, dict[str, str]]:
    return {row[id_column]: row for row in read_rows(rel) if row.get(id_column)}


def extract_readme_blocker_ids() -> set[str]:
    text = README.read_text(encoding="utf-8")
    match = re.search(r"\| Main live blockers \|([^|]+)\|", text)
    if not match:
        return set()
    return set(re.findall(r"\b(?:ISS|EG)-\d{4}\b", match.group(1)))


def check_blocker_ids_resolve() -> list[str]:
    errors: list[str] = []
    ids = extract_readme_blocker_ids()
    if not ids:
        errors.append("README.md missing parseable Main live blockers IDs")
        return errors

    issues = register_lookup("governance/issues_register.csv", "issue_id")
    gaps = register_lookup("evidence/evidence_gap_register.csv", "gap_id")
    for blocker_id in sorted(ids):
        if blocker_id.startswith("ISS-"):
            row = issues.get(blocker_id)
            if row is None:
                errors.append(f"README.md Main live blockers references unknown issue {blocker_id}")
            elif row.get("status") not in OPEN_STATUSES:
                errors.append(f"README.md Main live blockers references non-open issue {blocker_id}: {row.get('status')}")
        elif blocker_id.startswith("EG-"):
            row = gaps.get(blocker_id)
            if row is None:
                errors.append(f"README.md Main live blockers references unknown evidence gap {blocker_id}")
            elif row.get("status") not in OPEN_STATUSES:
                errors.append(f"README.md Main live blockers references non-open evidence gap {blocker_id}: {row.get('status')}")

    for required in sorted(REQUIRED_README_IDS - ids):
        errors.append(f"README.md Main live blockers missing current-stage blocker {required}")
    return errors


def extract_dashboard_ids() -> set[str]:
    dashboard = ROOT / "docs/officer/assurance-dashboard.md"
    if not dashboard.exists():
        return set()
    text = dashboard.read_text(encoding="utf-8")
    return set(re.findall(r"\b(?:ISS|RISK|EG)-\d{4}\b", text))


def check_dashboard_ids_resolve() -> list[str]:
    errors: list[str] = []
    ids = extract_dashboard_ids()
    if not ids:
        errors.append("docs/officer/assurance-dashboard.md has no parseable blocker IDs")
        return errors

    issues = register_lookup("governance/issues_register.csv", "issue_id")
    risks = register_lookup("governance/risk_register.csv", "risk_id")
    gaps = register_lookup("evidence/evidence_gap_register.csv", "gap_id")

    for blocker_id in sorted(ids):
        if blocker_id.startswith("ISS-"):
            if blocker_id not in issues:
                errors.append(f"docs/officer/assurance-dashboard.md references unknown issue {blocker_id}")
        elif blocker_id.startswith("RISK-"):
            if blocker_id not in risks:
                errors.append(f"docs/officer/assurance-dashboard.md references unknown risk {blocker_id}")
        elif blocker_id.startswith("EG-"):
            if blocker_id not in gaps:
                errors.append(f"docs/officer/assurance-dashboard.md references unknown evidence gap {blocker_id}")

    for required in sorted(REQUIRED_DASHBOARD_IDS - ids):
        errors.append(f"docs/officer/assurance-dashboard.md missing current-stage blocker {required}")
    return errors


def check_required_phrases() -> list[str]:
    errors: list[str] = []
    for rel, phrases in REQUIRED_PUBLIC_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing dashboard consistency file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing dashboard consistency phrase: {phrase}")
    return errors


def check_latest_stage_register_rows() -> list[str]:
    expected = [
        ("governance/issues_register.csv", "issue_id", "ISS-0036"),
        ("governance/risk_register.csv", "risk_id", "RISK-0039"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0033"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0054"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0047"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0033"),
        ("governance/decision_log.csv", "decision_id", "DEC-0040"),
        ("governance/approvals_register.csv", "approval_id", "APP-0045"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0101"),
    ]
    errors: list[str] = []
    for rel, column, row_id in expected:
        rows = register_lookup(rel, column)
        if row_id not in rows:
            errors.append(f"{rel} missing Stage 26A row {row_id}")
    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    errors.extend(check_blocker_ids_resolve())
    errors.extend(check_dashboard_ids_resolve())
    errors.extend(check_required_phrases())
    errors.extend(check_latest_stage_register_rows())
    errors.extend(check_no_authored_pdfs(ROOT))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Dashboard blocker consistency QA passed; blocker surfacing only, not risk adequacy or readiness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

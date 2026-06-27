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
    "ISS-0041",
    "EG-0059",
}

REQUIRED_DASHBOARD_IDS = REQUIRED_README_IDS | {"RISK-0044"}

REQUIRED_PUBLIC_PHRASES = {
    "README.md": [
        "Stage 27A",
        "validation evidence coverage controls",
        "Stage 28A",
        "Bristol live public-source coverage controls",
        "Stage 29A",
        "subagent context-control hardening",
        "Stage 30A",
        "validation coverage for Stage 29A",
        "Stage 31A",
        "validation evidence log for Stage 30A",
        "ISS-0041",
        "EG-0059",
    ],
    "docs/officer/assurance-dashboard.md": [
        "Validation evidence coverage",
        "Stage 27A records validation evidence coverage checks.",
        "scripts/validate_validation_coverage.py",
        "Bristol live public-source coverage",
        "Stage 28A records Bristol live public-source coverage",
        "scripts/validate_bristol_public_sources.py",
        "Subagent context-control hardening",
        "Stage 29A records bounded context controls",
        "scripts/validate_subagent_context_control.py",
        "Stage 29A validation coverage",
        "Stage 30A records validation coverage for Stage 29A.",
        "scripts/validate_validation_coverage.py",
        "Stage 30A validation evidence logging",
        "Stage 31A records validation evidence for Stage 30A.",
        "scripts/validate_validation_evidence_log.py",
    ],
    "docs/stages/README.md": [
        "Stage 27A",
        "validation evidence coverage",
        "Stage 28A",
        "Bristol live public-source coverage",
        "Stage 29A",
        "subagent context-control hardening",
        "Stage 30A",
        "validation coverage for Stage 29A",
        "Stage 31A",
        "validation evidence log for Stage 30A",
    ],
    "docs/visuals/stage-gate-map.mmd": [
        "Stage 29A",
        "Subagent context-control hardening",
        "Stage 30A",
        "Validation coverage for Stage 29A",
        "Stage 31A",
        "Validation evidence log for Stage 30A",
    ],
    "docs/visuals/risk-control-atlas.mmd": [
        "Subagent context-control hardening",
        "ISS-0039 EG-0057 RISK-0042",
        "Stage 29A validation coverage",
        "ISS-0040 EG-0058 RISK-0043",
        "Stage 30A validation evidence log",
        "ISS-0041 EG-0059 RISK-0044",
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
        ("governance/issues_register.csv", "issue_id", "ISS-0037"),
        ("governance/risk_register.csv", "risk_id", "RISK-0040"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0034"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0055"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0048"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0034"),
        ("governance/decision_log.csv", "decision_id", "DEC-0041"),
        ("governance/approvals_register.csv", "approval_id", "APP-0046"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0103"),
        ("governance/issues_register.csv", "issue_id", "ISS-0038"),
        ("governance/risk_register.csv", "risk_id", "RISK-0041"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0035"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0056"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0049"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0035"),
        ("governance/decision_log.csv", "decision_id", "DEC-0042"),
        ("governance/approvals_register.csv", "approval_id", "APP-0047"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0105"),
        ("governance/issues_register.csv", "issue_id", "ISS-0039"),
        ("governance/risk_register.csv", "risk_id", "RISK-0042"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0036"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0057"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0050"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0036"),
        ("governance/decision_log.csv", "decision_id", "DEC-0043"),
        ("governance/approvals_register.csv", "approval_id", "APP-0048"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0107"),
        ("governance/issues_register.csv", "issue_id", "ISS-0040"),
        ("governance/risk_register.csv", "risk_id", "RISK-0043"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0037"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0058"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0051"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0037"),
        ("governance/decision_log.csv", "decision_id", "DEC-0044"),
        ("governance/approvals_register.csv", "approval_id", "APP-0049"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0109"),
        ("governance/issues_register.csv", "issue_id", "ISS-0041"),
        ("governance/risk_register.csv", "risk_id", "RISK-0044"),
        ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0038"),
        ("evidence/evidence_gap_register.csv", "gap_id", "EG-0059"),
        ("governance/requirements_register.csv", "requirement_id", "REQ-0052"),
        ("governance/checks_and_balances_register.csv", "control_id", "CB-0038"),
        ("governance/decision_log.csv", "decision_id", "DEC-0045"),
        ("governance/approvals_register.csv", "approval_id", "APP-0050"),
        ("governance/simulation_signoff_register.csv", "signoff_id", "SSO-0111"),
    ]
    errors: list[str] = []
    for rel, column, row_id in expected:
        rows = register_lookup(rel, column)
        if row_id not in rows:
            errors.append(f"{rel} missing Stage 27A row {row_id}")
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

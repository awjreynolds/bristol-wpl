#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "docs/public/README.md",
    "docs/public/how-to-read-this-repo.md",
    "docs/public/what-this-repo-can-and-cannot-tell-you.md",
    "docs/public/evidence-and-assumptions-summary.md",
    "docs/officer/assurance-dashboard.md",
    "docs/officer/cabinet-and-officer-navigation-guide.md",
    "docs/officer/legal-and-governance-briefing.md",
    "docs/officer/programme-risk-briefing.md",
    "docs/officer/risk-gate-atlas.md",
    "docs/officer/risk-control-crosswalk.csv",
    "docs/officer/nottingham-and-comparator-lessons.md",
    "docs/officer/checks-and-balances-map.md",
    "docs/officer/document-map.md",
    "docs/visuals/stage-gate-map.mmd",
    "governance/pitfalls_register.csv",
    "governance/stage_risk_matrix.csv",
    "governance/checks_and_balances_register.csv",
    "governance/real_world_adoption_checklist.csv",
    "analysis/economic/nottingham_lessons_register.csv",
]

CSV_HEADERS = {
    "governance/pitfalls_register.csv": [
        "pitfall_id",
        "stage",
        "pitfall",
        "why_it_matters",
        "mitigation",
        "current_status",
        "owner",
        "next_check",
    ],
    "governance/stage_risk_matrix.csv": [
        "stage",
        "blocker",
        "legal_risk",
        "programme_risk",
        "public_law_risk",
        "financial_risk",
        "mitigation",
        "gate_effect",
        "owner",
        "status",
    ],
    "governance/checks_and_balances_register.csv": [
        "control_id",
        "claim_type",
        "required_evidence",
        "required_reviewer",
        "validator_or_gate",
        "banned_wording",
        "current_status",
    ],
    "governance/real_world_adoption_checklist.csv": [
        "adoption_id",
        "simulation_control",
        "required_real_world_replacement",
        "responsible_profession_or_body",
        "status",
    ],
}

REQUIRED_README_PHRASES = [
    "No Bristol Workplace Parking Levy has been approved by this repository",
    "What Can I Rely On?",
    "Where To Start",
    "Current No-Go Position",
    "Stage 9A",
]

REQUIRED_DASHBOARD_PHRASES = [
    "not an approved Bristol WPL scheme",
    "Simulation Control Dashboard",
    "RAG colours describe repository control status, not real-world WPL readiness.",
    "What Can Be Relied On",
    "Nottingham transfer",
]

REQUIRED_VISUAL_PHRASES = [
    "Stage 0-1",
    "Stage 2",
    "Stage 3A",
    "Stage 4A",
    "Stage 5A",
    "Stage 6A",
    "Stage 7",
    "Stage 8A",
    "Stage 9A",
    "Stage 19A",
    "Stage 11",
    "BLOCKED",
]

CLOSED_STATUSES = {"closed", "resolved", "accepted_closed"}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def normalise(value: str | None) -> str:
    return (value or "").strip().lower()


def is_closed(value: str | None) -> bool:
    return normalise(value) in CLOSED_STATUSES


def check_required_files() -> list[str]:
    return [f"missing officer/public pack file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, required in CSV_HEADERS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Stage 9A register: {rel}")
            continue
        header = read_header(rel)
        for column in required:
            if column not in header:
                errors.append(f"{rel} missing column {column}")
    return errors


def check_required_phrases(rel: str, phrases: list[str]) -> list[str]:
    path = ROOT / rel
    if not path.exists():
        return [f"missing file for phrase check: {rel}"]
    text = path.read_text(encoding="utf-8")
    return [f"{rel} missing required phrase: {phrase}" for phrase in phrases if phrase not in text]


def check_open_p0s_in_dashboard() -> list[str]:
    dashboard = ROOT / "docs/officer/assurance-dashboard.md"
    if not dashboard.exists():
        return ["missing officer assurance dashboard"]
    text = dashboard.read_text(encoding="utf-8")
    errors = []
    for row in read_rows("governance/issues_register.csv"):
        if row.get("severity") == "P0" and not is_closed(row.get("status")):
            issue_id = row.get("issue_id", "")
            if issue_id and issue_id not in text:
                errors.append(f"docs/officer/assurance-dashboard.md missing open P0 issue {issue_id}")
    for row in read_rows("governance/risk_register.csv"):
        if (row.get("gross_rating") == "P0" or row.get("residual_rating") == "P0") and not is_closed(row.get("status")):
            risk_id = row.get("risk_id", "")
            if risk_id and risk_id not in text:
                errors.append(f"docs/officer/assurance-dashboard.md missing open P0 risk {risk_id}")
    return errors


def check_register_coverage() -> list[str]:
    errors = []
    pitfalls = read_rows("governance/pitfalls_register.csv")
    stages = {row.get("stage", "") for row in pitfalls}
    for stage in ["Stage 2", "Stage 4", "Stage 5", "Stage 6", "Stage 8", "Stage 11"]:
        if stage not in stages:
            errors.append(f"governance/pitfalls_register.csv missing pitfall coverage for {stage}")
    checks = {row.get("claim_type", "") for row in read_rows("governance/checks_and_balances_register.csv")}
    for claim_type in ["legal_route", "boundary", "nottingham_transfer", "obc_readiness", "consultation_launch"]:
        if claim_type not in checks:
            errors.append(f"governance/checks_and_balances_register.csv missing claim type {claim_type}")
    adoption_rows = read_rows("governance/real_world_adoption_checklist.csv")
    if len(adoption_rows) < 8:
        errors.append("governance/real_world_adoption_checklist.csv must contain at least 8 replacement controls")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases("README.md", REQUIRED_README_PHRASES))
    errors.extend(check_required_phrases("docs/officer/assurance-dashboard.md", REQUIRED_DASHBOARD_PHRASES))
    errors.extend(check_required_phrases("docs/visuals/stage-gate-map.mmd", REQUIRED_VISUAL_PHRASES))
    errors.extend(check_open_p0s_in_dashboard())
    errors.extend(check_register_coverage())
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Officer pack QA passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

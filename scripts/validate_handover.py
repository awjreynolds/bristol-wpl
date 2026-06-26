#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/handover/stage-13a-critical-path-handover-control-package.md",
    "handover/controls/critical-path-work-package-register.csv",
    "handover/controls/blocker-to-workstream-map.csv",
    "handover/controls/next-90-day-plan.csv",
    "handover/controls/handover-no-go-register.csv",
    "docs/officer/next-steps-critical-path.md",
    "docs/stages/stage-13a-critical-path-handover.md",
    "review/peer_review/stage-13a-critical-path-handover-review.md",
    "review/stage_gate_reports/stage-13a-critical-path-handover-gate-report.md",
]

CSV_HEADERS = {
    "handover/controls/critical-path-work-package-register.csv": [
        "work_package_id",
        "workstream",
        "purpose",
        "linked_blockers",
        "prerequisite_evidence",
        "minimum_output",
        "required_review",
        "current_status",
        "gate_effect",
        "no_go_note",
    ],
    "handover/controls/blocker-to-workstream-map.csv": [
        "blocker_id",
        "blocker_type",
        "severity",
        "work_package_id",
        "dependency_reason",
        "source_register",
        "gate_effect",
        "current_status",
    ],
    "handover/controls/next-90-day-plan.csv": [
        "phase_id",
        "focus",
        "work_packages",
        "outputs",
        "dependencies",
        "current_status",
        "no_go_note",
    ],
    "handover/controls/handover-no-go-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_wording",
        "current_status",
        "gate_effect",
    ],
}

REQUIRED_WORK_PACKAGES = {
    "WP-LEGAL-ROUTE",
    "WP-WECA-MCA",
    "WP-DFT-PROCESS",
    "WP-BOUNDARY-INVENTORY",
    "WP-DISPLACEMENT",
    "WP-APPRAISAL-MODEL",
    "WP-CONSULTATION",
    "WP-FINANCE-S151",
    "WP-OPERATIONS-DATA",
    "WP-OBC-FBC-EVIDENCE",
    "WP-PUBLIC-GOVERNANCE",
}

REQUIRED_PHASES = {"days_0_30", "days_31_60", "days_61_90"}

REQUIRED_NO_GO_CLAIMS = {
    "critical path is an approved programme",
    "work packages close blockers",
    "90 day plan authorises spend or procurement",
    "handover replaces officer decisions",
    "handover means gates can pass",
}

REQUIRED_PHRASES = {
    "README.md": [
        "Stage 13A",
        "docs/officer/next-steps-critical-path.md",
        "critical path is not approval",
    ],
    "analysis/handover/stage-13a-critical-path-handover-control-package.md": [
        "critical path is not approval",
        "does not close any WPL gate",
        "blocked work packages",
    ],
    "docs/officer/next-steps-critical-path.md": [
        "What happens next",
        "critical path is not approval",
        "No work package closes a blocker by existing",
    ],
    "docs/public/README.md": [
        "docs/officer/next-steps-critical-path.md",
        "critical path is not approval",
    ],
    "governance/stage-gate-plan.md": [
        "Stage 13A",
        "handover-control",
    ],
    "review/stage_gate_reports/stage-13a-critical-path-handover-gate-report.md": [
        "Accepted for handover control purposes only",
        "no WPL gate is closed",
    ],
}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def source_ids() -> dict[str, set[str]]:
    return {
        "governance/issues_register.csv": {
            row["issue_id"] for row in read_rows("governance/issues_register.csv")
        },
        "governance/risk_register.csv": {
            row["risk_id"] for row in read_rows("governance/risk_register.csv")
        },
    }


def expected_blocker_pairs() -> set[tuple[str, str]]:
    pairs = set()
    for row in read_rows("handover/controls/critical-path-work-package-register.csv"):
        work_package_id = row.get("work_package_id", "")
        for blocker_id in row.get("linked_blockers", "").split(";"):
            if blocker_id:
                pairs.add((blocker_id, work_package_id))
    return pairs


def check_csv_widths(rel: str) -> list[str]:
    errors = []
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            return [f"{rel} is empty"]
        expected = len(header)
        for line_number, row in enumerate(reader, start=2):
            if len(row) != expected:
                errors.append(f"{rel}:{line_number} has {len(row)} fields; expected {expected}")
    return errors


def check_required_files() -> list[str]:
    return [f"missing handover file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing handover CSV: {rel}")
            continue
        header = read_header(rel)
        for column in columns:
            if column not in header:
                errors.append(f"{rel} missing column {column}")
        errors.extend(check_csv_widths(rel))
    return errors


def check_required_phrases() -> list[str]:
    errors = []
    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing phrase-check file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required phrase: {phrase}")
    return errors


def check_work_packages() -> list[str]:
    rel = "handover/controls/critical-path-work-package-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing work package register: {rel}"]
    errors = []
    rows = read_rows(rel)
    found = {row.get("work_package_id", "") for row in rows}
    for missing in sorted(REQUIRED_WORK_PACKAGES - found):
        errors.append(f"{rel} missing work_package_id {missing}")
    for row in rows:
        work_package_id = row.get("work_package_id", "<unknown>")
        if row.get("current_status") != "blocked_work_package":
            errors.append(f"{rel} {work_package_id} must remain blocked_work_package")
        if row.get("gate_effect") not in {"P0_blocks", "P1_blocks", "control_only"}:
            errors.append(f"{rel} {work_package_id} has unsafe gate_effect {row.get('gate_effect')}")
        if "does not close" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {work_package_id} missing no-go note")
        if "simulation-only" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {work_package_id} missing simulation-only review warning")
        if "real officer professional replacement" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {work_package_id} missing real-world replacement warning")
    return errors


def check_blocker_map() -> list[str]:
    rel = "handover/controls/blocker-to-workstream-map.csv"
    if not (ROOT / rel).exists():
        return [f"missing blocker map: {rel}"]
    errors = []
    rows = read_rows(rel)
    expected_pairs = expected_blocker_pairs()
    actual_pairs = {(row.get("blocker_id", ""), row.get("work_package_id", "")) for row in rows}
    ids_by_source = source_ids()
    all_source_ids = set().union(*ids_by_source.values())

    for blocker_id, work_package_id in sorted(expected_pairs - actual_pairs):
        errors.append(f"{rel} missing blocker_id {blocker_id} for {work_package_id}")
    for blocker_id, work_package_id in sorted(actual_pairs - expected_pairs):
        errors.append(f"{rel} orphan blocker mapping {blocker_id} for {work_package_id}")

    for blocker_id in sorted({blocker_id for blocker_id, _ in expected_pairs} - all_source_ids):
        errors.append(f"{rel} expected blocker {blocker_id} is missing from source registers")

    for row in rows:
        blocker_id = row.get("blocker_id", "<unknown>")
        if row.get("work_package_id") not in REQUIRED_WORK_PACKAGES:
            errors.append(f"{rel} {blocker_id} links to unknown work package {row.get('work_package_id')}")
        source_register = row.get("source_register", "")
        if source_register not in ids_by_source:
            errors.append(f"{rel} {blocker_id} has unknown source_register {source_register}")
        elif blocker_id not in ids_by_source[source_register]:
            errors.append(f"{rel} {blocker_id} is not present in {source_register}")
        if row.get("blocker_type") == "issue" and source_register != "governance/issues_register.csv":
            errors.append(f"{rel} {blocker_id} issue must use issues register")
        if row.get("blocker_type") == "risk" and source_register != "governance/risk_register.csv":
            errors.append(f"{rel} {blocker_id} risk must use risk register")
        if row.get("gate_effect") not in {"P0_blocks", "P1_blocks", "control_only"}:
            errors.append(f"{rel} {blocker_id} has unsafe gate_effect {row.get('gate_effect')}")
        if row.get("current_status") not in {"mapped_open", "mapped_controlled"}:
            errors.append(f"{rel} {blocker_id} has invalid current_status {row.get('current_status')}")
    return errors


def check_next_90_days() -> list[str]:
    rel = "handover/controls/next-90-day-plan.csv"
    if not (ROOT / rel).exists():
        return [f"missing 90-day plan: {rel}"]
    errors = []
    rows = read_rows(rel)
    found = {row.get("phase_id", "") for row in rows}
    for missing in sorted(REQUIRED_PHASES - found):
        errors.append(f"{rel} missing phase_id {missing}")
    for row in rows:
        phase_id = row.get("phase_id", "<unknown>")
        if row.get("current_status") != "planning_control_only":
            errors.append(f"{rel} {phase_id} must remain planning_control_only")
        if "does not authorise spend" not in row.get("no_go_note", ""):
            errors.append(f"{rel} {phase_id} missing spend/procurement no-go note")
    return errors


def check_no_go_register() -> list[str]:
    rel = "handover/controls/handover-no-go-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing handover no-go register: {rel}"]
    errors = []
    rows = read_rows(rel)
    found = {row.get("prohibited_claim", "") for row in rows}
    for missing in sorted(REQUIRED_NO_GO_CLAIMS - found):
        errors.append(f"{rel} missing prohibited claim: {missing}")
    for row in rows:
        claim_id = row.get("claim_id", "<unknown>")
        if row.get("current_status") != "blocked":
            errors.append(f"{rel} {claim_id} must remain blocked")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_work_packages())
    errors.extend(check_blocker_map())
    errors.extend(check_next_90_days())
    errors.extend(check_no_go_register())
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Handover QA passed; no WPL gate is closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

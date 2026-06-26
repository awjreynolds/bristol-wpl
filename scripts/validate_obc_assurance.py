#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_obc import collect_readiness_blockers

REQUIRED_FILES = [
    "analysis/obc/stage-7a-obc-assurance-gate-control-package.md",
    "business_case/obc/controls/stage-7-obc-gate-checklist.csv",
    "business_case/obc/controls/stage-7-assurance-panel-register.csv",
    "business_case/obc/controls/stage-7-decision-report-control.md",
    "business_case/obc/controls/stage-7-red-team-packet.md",
    "review/peer_review/stage-7a-obc-assurance-review.md",
    "review/stage_gate_reports/stage-7a-obc-assurance-gate-report.md",
]

CSV_HEADERS = {
    "business_case/obc/controls/stage-7-obc-gate-checklist.csv": [
        "gate_item_id",
        "assurance_area",
        "minimum_evidence",
        "required_control",
        "required_reviewer",
        "blocker_ids",
        "current_status",
        "gate_effect",
        "pass_condition",
    ],
    "business_case/obc/controls/stage-7-assurance-panel-register.csv": [
        "reviewer_id",
        "review_role",
        "required_competence",
        "evidence_scope",
        "mandatory_inputs",
        "output_required",
        "current_status",
        "real_world_replacement",
    ],
}

REQUIRED_ASSURANCE_AREAS = {
    "legal_governance",
    "strategic_case",
    "economic_appraisal",
    "spatial_parking",
    "financial_affordability",
    "commercial_operations",
    "management_delivery",
    "consultation_readiness",
    "equality_data_accessibility",
    "statutory_route",
    "red_team",
    "officer_editability",
}

REQUIRED_PHRASES = {
    "analysis/obc/stage-7a-obc-assurance-gate-control-package.md": [
        "does not approve an OBC",
        "Stage 7 OBC gate remains blocked",
        "no proceed recommendation",
        "open P0",
    ],
    "business_case/obc/controls/stage-7-decision-report-control.md": [
        "no proceed recommendation",
        "not an officer decision report",
        "Stage 7 OBC gate remains blocked",
    ],
    "business_case/obc/controls/stage-7-red-team-packet.md": [
        "bounded red-team packet",
        "readiness overclaim",
        "Stage 7 OBC gate remains blocked",
    ],
    "review/stage_gate_reports/stage-7a-obc-assurance-gate-report.md": [
        "Accepted for simulation control purposes only",
        "Stage 7 OBC gate remains blocked",
        "does not approve an OBC",
    ],
}


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


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
    return [f"missing Stage 7A OBC assurance file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing Stage 7A CSV: {rel}")
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


def check_gate_checklist() -> list[str]:
    rel = "business_case/obc/controls/stage-7-obc-gate-checklist.csv"
    if not (ROOT / rel).exists():
        return [f"missing Stage 7 checklist: {rel}"]
    errors = []
    rows = read_rows(rel)
    areas = {row.get("assurance_area", "") for row in rows}
    for area in sorted(REQUIRED_ASSURANCE_AREAS - areas):
        errors.append(f"{rel} missing assurance_area {area}")
    gate_effects = {row.get("gate_effect", "") for row in rows}
    if "P0" not in gate_effects:
        errors.append(f"{rel} must include at least one P0 gate effect")
    if "P1" not in gate_effects:
        errors.append(f"{rel} must include at least one P1 gate effect")
    for row in rows:
        item_id = row.get("gate_item_id", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} {item_id} must remain blocked_control_only")
        if not row.get("minimum_evidence"):
            errors.append(f"{rel} {item_id} missing minimum_evidence")
        if not row.get("required_reviewer"):
            errors.append(f"{rel} {item_id} missing required_reviewer")
        if not row.get("pass_condition"):
            errors.append(f"{rel} {item_id} missing pass_condition")
    return errors


def check_panel_register() -> list[str]:
    rel = "business_case/obc/controls/stage-7-assurance-panel-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing Stage 7 panel register: {rel}"]
    errors = []
    rows = read_rows(rel)
    if len(rows) < 10:
        errors.append(f"{rel} must include at least 10 reviewer roles")
    replacement_text = " ".join(row.get("real_world_replacement", "") for row in rows)
    if "Monitoring Officer" not in replacement_text:
        errors.append(f"{rel} must record Monitoring Officer real-world replacement")
    for row in rows:
        reviewer_id = row.get("reviewer_id", "<unknown>")
        if row.get("current_status") != "simulation_role_only":
            errors.append(f"{rel} {reviewer_id} must remain simulation_role_only")
        for column in ["review_role", "required_competence", "evidence_scope", "mandatory_inputs", "output_required", "real_world_replacement"]:
            if not row.get(column):
                errors.append(f"{rel} {reviewer_id} missing {column}")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_gate_checklist())
    errors.extend(check_panel_register())
    if not collect_readiness_blockers():
        errors.append("Stage 7 OBC gate unexpectedly has no live readiness blockers")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", action="store_true")
    args = parser.parse_args()

    blockers = collect_readiness_blockers()
    if args.gate:
        if blockers:
            print("ERROR: Stage 7 OBC gate blocked by open P0/P1 readiness blockers.", file=sys.stderr)
            for blocker in blockers:
                print(f"ERROR: {blocker}", file=sys.stderr)
            return 1
        print("Stage 7 OBC gate passed")
        return 0

    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OBC assurance QA passed; Stage 7 OBC gate remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

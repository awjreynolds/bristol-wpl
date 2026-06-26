#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

REQUIRED_FILES = [
    "analysis/legal/stage-10a-statutory-confirmation-dossier-control-package.md",
    "statutory_dossier/controls/dossier-component-register.csv",
    "statutory_dossier/controls/dossier-readiness-gate.csv",
    "statutory_dossier/controls/submission-no-go-register.csv",
    "statutory_dossier/controls/statutory-route-memorandum-control.md",
    "statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv",
    "review/peer_review/stage-10a-statutory-dossier-review.md",
    "review/stage_gate_reports/stage-10a-statutory-dossier-control-report.md",
]

CSV_HEADERS = {
    "statutory_dossier/controls/dossier-component-register.csv": [
        "component_number",
        "component_name",
        "required_document",
        "minimum_evidence",
        "linked_blockers",
        "current_status",
        "gate_effect",
        "owner",
        "reviewer",
        "no_go_note",
    ],
    "statutory_dossier/controls/dossier-readiness-gate.csv": [
        "gate_item_id",
        "assurance_area",
        "minimum_evidence",
        "linked_components",
        "blocker_ids",
        "current_status",
        "gate_effect",
        "pass_condition",
    ],
    "statutory_dossier/controls/submission-no-go-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_stage_10a_wording",
        "affected_components",
        "current_status",
        "gate_effect",
    ],
    "statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv": [
        "clause_area",
        "statutory_source",
        "required_power_or_control",
        "dossier_dependency",
        "current_status",
        "reviewer",
        "blocker_ids",
    ],
}

REQUIRED_NO_GO_CLAIMS = {
    "statutory submission is ready",
    "scheme order is certified",
    "DfT has accepted the dossier",
    "Secretary of State confirmation is expected",
    "consultation statement is complete",
    "boundary schedule is legally settled",
    "FBC is ready for submission",
}

REQUIRED_COMPONENT_NAMES = {
    "covering submission",
    "application or confirmation request",
    "certified scheme order",
    "legal boundary map and schedule",
    "statement of reasons",
    "legal powers and compliance statement",
    "local transport policy case",
    "approved 10-year general plan for net proceeds",
    "approved 5-year detailed programme",
    "final business case",
    "consultation statement and response",
    "equality human-rights and distributional assessment",
    "environmental and carbon assessment",
    "financial and net-proceeds evidence",
    "licensing compliance enforcement and appeals design",
    "governance resolutions",
    "monitoring evaluation and review",
    "implementation and commencement plan",
    "supporting evidence list",
    "response to DfT pre-application points",
    "statutory route memorandum",
    "council-made scheme order submitted for confirmation",
    "clause-by-clause scheme-order powers matrix",
}

REQUIRED_PHRASES = {
    "analysis/legal/stage-10a-statutory-confirmation-dossier-control-package.md": [
        "does not create a statutory submission",
        "Stage 10 statutory submission remains blocked",
        "working framework, not a definitive DfT checklist",
    ],
    "statutory_dossier/controls/statutory-route-memorandum-control.md": [
        "initial order",
        "variation",
        "revocation",
        "RPI-only variation",
        "Stage 10 statutory submission remains blocked",
    ],
    "review/stage_gate_reports/stage-10a-statutory-dossier-control-report.md": [
        "Accepted for simulation control purposes only",
        "does not create a statutory submission",
        "Stage 10 statutory submission remains blocked",
    ],
    }


ACTIVE_BLOCKING_STATUSES = {
    "open",
    "narrowed_open",
    "controlled_open",
    "partially_closed",
    "partially_controlled",
    "working",
    "blocked_control_only",
}

CLOSED_STATUSES = {
    "closed",
    "resolved",
    "accepted_closed",
    "cleared",
    "ready",
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
    return [f"missing Stage 10A statutory dossier file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing Stage 10A CSV: {rel}")
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


def normalise(value: str | None) -> str:
    return (value or "").strip().lower()


def is_closed_status(status: str | None) -> bool:
    return normalise(status) in CLOSED_STATUSES


def is_active_blocker(status: str | None) -> bool:
    value = normalise(status)
    return bool(value) and (value in ACTIVE_BLOCKING_STATUSES or not is_closed_status(value))


def p1_issue_has_accepted_condition(row: dict[str, str]) -> bool:
    notes = normalise(row.get("notes"))
    return (
        normalise(row.get("status")) == "controlled"
        and bool(row.get("owner"))
        and bool(row.get("due_date"))
        and "simulation gate authority" in notes
        and "residual" in notes
    )


def p1_risk_has_accepted_condition(row: dict[str, str]) -> bool:
    controls = normalise(row.get("controls"))
    return (
        normalise(row.get("status")) == "controlled"
        and bool(row.get("owner"))
        and bool(row.get("review_date"))
        and row.get("acceptance_authority") == "Simulation Gate Authority"
        and "residual" in controls
    )


def issue_statutory_error(row: dict[str, str]) -> str | None:
    status = row.get("status", "")
    severity = row.get("severity", "")
    issue_id = row.get("issue_id", "<unknown>")
    if is_closed_status(status):
        return None
    if severity == "P0":
        return f"{issue_id} is {status}; open P0 issue blocks statutory submission"
    if severity == "P1" and not p1_issue_has_accepted_condition(row):
        return (
            f"{issue_id} is {status}; P1 issue lacks Simulation Gate Authority condition "
            "with owner deadline and residual risk for statutory submission"
        )
    return None


def risk_statutory_error(row: dict[str, str]) -> str | None:
    status = row.get("status", "")
    gross_rating = row.get("gross_rating", "")
    residual_rating = row.get("residual_rating", "")
    risk_id = row.get("risk_id", "<unknown>")
    if is_closed_status(status):
        return None
    if gross_rating == "P0" or residual_rating == "P0":
        return f"{risk_id} is {status}; open P0 risk blocks statutory submission"
    if (gross_rating == "P1" or residual_rating == "P1") and not p1_risk_has_accepted_condition(row):
        return (
            f"{risk_id} is {status}; P1 risk lacks Simulation Gate Authority condition "
            "with owner deadline and residual risk for statutory submission"
        )
    return None


def collect_statutory_submission_blockers() -> list[str]:
    blockers = []

    for row in read_rows("governance/issues_register.csv"):
        error = issue_statutory_error(row)
        if error:
            blockers.append(error)

    for row in read_rows("governance/risk_register.csv"):
        error = risk_statutory_error(row)
        if error:
            blockers.append(error)

    readiness_rel = "statutory_dossier/controls/dossier-readiness-gate.csv"
    if (ROOT / readiness_rel).exists():
        for row in read_rows(readiness_rel):
            status = row.get("current_status", "")
            if is_active_blocker(status):
                blockers.append(
                    f"{readiness_rel} {row.get('gate_item_id', '<unknown>')} is {status}; "
                    f"{row.get('assurance_area', 'assurance item')} blocks statutory submission"
                )

    no_go_rel = "statutory_dossier/controls/submission-no-go-register.csv"
    if (ROOT / no_go_rel).exists():
        for row in read_rows(no_go_rel):
            status = row.get("current_status", "")
            if is_active_blocker(status):
                blockers.append(
                    f"{no_go_rel} {row.get('claim_id', '<unknown>')} is {status}; "
                    f"prohibited claim '{row.get('prohibited_claim', '<missing claim>')}' "
                    "blocks statutory submission readiness"
                )

    for row in read_rows("evidence/evidence_gap_register.csv"):
        if row.get("gap_id") == "EG-0034" and is_active_blocker(row.get("status", "")):
            blockers.append(
                "evidence/evidence_gap_register.csv EG-0034 is open; statutory submission evidence "
                "packet, certified order, DfT response, FBC and consultation statement are not populated"
            )

    for row in read_rows("governance/approvals_register.csv"):
        if row.get("approval_id") == "APP-0024" and "submission_blocked" in normalise(row.get("status")):
            blockers.append(
                "governance/approvals_register.csv APP-0024 is a simulation control approval only; "
                "it does not approve statutory submission"
            )

    for row in read_rows("governance/simulation_signoff_register.csv"):
        if row.get("signoff_id") in {"SSO-0058", "SSO-0059"}:
            decision = normalise(row.get("decision"))
            if "conditions" in decision or "no-go" in decision:
                blockers.append(
                    f"governance/simulation_signoff_register.csv {row.get('signoff_id')} "
                    "is limited to simulation controls and does not clear statutory submission"
                )

    return blockers


def check_component_register() -> list[str]:
    rel = "statutory_dossier/controls/dossier-component-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing component register: {rel}"]
    errors = []
    rows = read_rows(rel)
    if len(rows) != 23:
        errors.append(f"{rel} must contain exactly 23 Stage 10 working-framework components")
    numbers = {row.get("component_number", "") for row in rows}
    expected_numbers = {str(i).zfill(2) for i in range(1, 24)}
    for missing in sorted(expected_numbers - numbers):
        errors.append(f"{rel} missing component_number {missing}")
    names = {row.get("component_name", "") for row in rows}
    for missing in sorted(REQUIRED_COMPONENT_NAMES - names):
        errors.append(f"{rel} missing component_name {missing}")
    for row in rows:
        component = row.get("component_number", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} component {component} must remain blocked_control_only")
        if not row.get("linked_blockers"):
            errors.append(f"{rel} component {component} missing linked_blockers")
        if not row.get("no_go_note"):
            errors.append(f"{rel} component {component} missing no_go_note")
        required_document = row.get("required_document", "")
        if required_document and not (ROOT / required_document).exists():
            errors.append(f"{rel} component {component} required_document does not exist: {required_document}")
    return errors


def check_no_go_register() -> list[str]:
    rel = "statutory_dossier/controls/submission-no-go-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing no-go register: {rel}"]
    errors = []
    rows = read_rows(rel)
    claims = {row.get("prohibited_claim", "") for row in rows}
    for missing in sorted(REQUIRED_NO_GO_CLAIMS - claims):
        errors.append(f"{rel} missing prohibited claim: {missing}")
    for row in rows:
        claim_id = row.get("claim_id", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} {claim_id} must remain blocked_control_only")
    return errors


def check_clause_matrix() -> list[str]:
    rel = "statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv"
    if not (ROOT / rel).exists():
        return [f"missing clause matrix: {rel}"]
    errors = []
    rows = read_rows(rel)
    if len(rows) < 8:
        errors.append(f"{rel} must contain at least 8 clause-control rows")
    for row in rows:
        area = row.get("clause_area", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} {area} must remain blocked_control_only")
        if not row.get("statutory_source"):
            errors.append(f"{rel} {area} missing statutory_source")
        if not row.get("blocker_ids"):
            errors.append(f"{rel} {area} missing blocker_ids")
    return errors


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_component_register())
    errors.extend(check_no_go_register())
    errors.extend(check_clause_matrix())
    if not collect_statutory_submission_blockers():
        errors.append("Stage 10 statutory submission unexpectedly has no live readiness blockers")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", action="store_true")
    args = parser.parse_args()

    blockers = collect_statutory_submission_blockers()
    if args.gate:
        if blockers:
            print("ERROR: Stage 10 statutory submission blocked by open P0/P1 readiness blockers.", file=sys.stderr)
            for blocker in blockers:
                print(f"ERROR: {blocker}", file=sys.stderr)
            return 1
        print("Stage 10 statutory submission gate passed")
        return 0

    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Statutory dossier QA passed; Stage 10 statutory submission remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

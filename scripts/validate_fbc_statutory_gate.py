#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_statutory_dossier import collect_statutory_submission_blockers, is_active_blocker

REQUIRED_FILES = [
    "analysis/fbc/stage-11a-fbc-statutory-gate-control-package.md",
    "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv",
    "business_case/fbc/controls/stage-11-assurance-panel-register.csv",
    "business_case/fbc/controls/stage-11-no-go-claim-register.csv",
    "business_case/fbc/controls/stage-11-decision-report-control.md",
    "business_case/fbc/controls/stage-11-red-team-packet.md",
    "review/peer_review/stage-11a-fbc-statutory-assurance-review.md",
    "review/stage_gate_reports/stage-11a-fbc-statutory-gate-report.md",
]

CSV_HEADERS = {
    "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv": [
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
    "business_case/fbc/controls/stage-11-assurance-panel-register.csv": [
        "reviewer_id",
        "review_role",
        "required_competence",
        "evidence_scope",
        "mandatory_inputs",
        "output_required",
        "current_status",
        "real_world_replacement",
    ],
    "business_case/fbc/controls/stage-11-no-go-claim-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_stage_11a_wording",
        "affected_gate_items",
        "current_status",
        "gate_effect",
    ],
}

REQUIRED_ASSURANCE_AREAS = {
    "scheme_order_boundary_legal",
    "consultation_reconsultation",
    "statutory_confirmation",
    "finance_s151_affordability",
    "procurement_commercial",
    "data_cyber",
    "operations_enforcement",
    "charge_base_revenue_models",
    "investment_programme",
    "equality_mitigation",
    "dft_engagement",
    "weca_mca_dependencies",
    "residual_risk_decision_pack",
}

REQUIRED_NO_GO_CLAIMS = {
    "recommend submit and implement",
    "FBC is ready for approval",
    "scheme order and boundary have legal sign-off",
    "consultation is lawful and conscientiously addressed",
    "Section 151 affordability review is complete",
    "procurement/commercial route is lawful and credible",
    "operations and enforcement are service-ready",
    "charge-base and revenue models are independently reviewed",
    "WECA/MCA dependencies are agreed",
    "DfT engagement issues are closed",
    "reconsultation assessment is complete",
    "current statutory confirmation requirements are satisfied",
    "data protection and cyber controls are ready",
    "investment programme is deliverable",
    "equality mitigations are funded and owned",
    "no P0 findings remain",
}

REQUIRED_PHRASES = {
    "analysis/fbc/stage-11a-fbc-statutory-gate-control-package.md": [
        "does not approve an FBC",
        "Stage 11 FBC/statutory gate remains blocked",
        "no recommendation to submit or implement",
    ],
    "business_case/fbc/controls/stage-11-decision-report-control.md": [
        "no recommendation to submit or implement",
        "not an officer decision report",
        "Stage 11 FBC/statutory gate remains blocked",
    ],
    "business_case/fbc/controls/stage-11-red-team-packet.md": [
        "bounded red-team packet",
        "readiness overclaim",
        "Stage 11 FBC/statutory gate remains blocked",
    ],
    "review/stage_gate_reports/stage-11a-fbc-statutory-gate-report.md": [
        "Accepted for simulation control purposes only",
        "Stage 11 FBC/statutory gate remains blocked",
        "does not approve an FBC",
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


def normalise(value: str | None) -> str:
    return (value or "").strip().lower()


def check_required_files() -> list[str]:
    return [f"missing Stage 11A FBC/statutory gate file: {rel}" for rel in REQUIRED_FILES if not (ROOT / rel).exists()]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        if not (ROOT / rel).exists():
            errors.append(f"missing Stage 11A CSV: {rel}")
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
    rel = "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv"
    if not (ROOT / rel).exists():
        return [f"missing Stage 11 checklist: {rel}"]
    errors = []
    rows = read_rows(rel)
    areas = {row.get("assurance_area", "") for row in rows}
    for missing in sorted(REQUIRED_ASSURANCE_AREAS - areas):
        errors.append(f"{rel} missing assurance_area {missing}")
    for row in rows:
        gate_item = row.get("gate_item_id", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} {gate_item} must remain blocked_control_only")
        if not row.get("blocker_ids"):
            errors.append(f"{rel} {gate_item} missing blocker_ids")
        if not row.get("pass_condition"):
            errors.append(f"{rel} {gate_item} missing pass_condition")
    return errors


def check_assurance_panel() -> list[str]:
    rel = "business_case/fbc/controls/stage-11-assurance-panel-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing Stage 11 assurance panel register: {rel}"]
    errors = []
    rows = read_rows(rel)
    if len(rows) < 10:
        errors.append(f"{rel} must include at least 10 assurance roles")
    replacement_text = " ".join(row.get("real_world_replacement", "") for row in rows)
    for required in ["Section 151", "Monitoring Officer"]:
        if required not in replacement_text:
            errors.append(f"{rel} missing real-world replacement reference: {required}")
    for row in rows:
        reviewer_id = row.get("reviewer_id", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} {reviewer_id} must remain blocked_control_only")
        if not row.get("real_world_replacement"):
            errors.append(f"{rel} {reviewer_id} missing real_world_replacement")
    checklist_rel = "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv"
    if (ROOT / checklist_rel).exists():
        reviewer_text = " ".join(row.get("review_role", "") for row in rows)
        for checklist_row in read_rows(checklist_rel):
            gate_item = checklist_row.get("gate_item_id", "<unknown>")
            for required_reviewer in checklist_row.get("required_reviewer", "").split(" and "):
                if required_reviewer and required_reviewer not in reviewer_text:
                    errors.append(f"{rel} missing reviewer role for {gate_item}: {required_reviewer}")
    return errors


def check_no_go_register() -> list[str]:
    rel = "business_case/fbc/controls/stage-11-no-go-claim-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing Stage 11 no-go register: {rel}"]
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


def collect_fbc_statutory_gate_blockers() -> list[str]:
    blockers = collect_statutory_submission_blockers()

    checklist_rel = "business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv"
    if (ROOT / checklist_rel).exists():
        for row in read_rows(checklist_rel):
            status = row.get("current_status")
            if is_active_blocker(status):
                blockers.append(
                    f"{checklist_rel} {row.get('gate_item_id', '<unknown>')} is {status}; "
                    f"{row.get('assurance_area', 'assurance item')} blocks FBC/statutory gate"
                )

    no_go_rel = "business_case/fbc/controls/stage-11-no-go-claim-register.csv"
    if (ROOT / no_go_rel).exists():
        for row in read_rows(no_go_rel):
            status = row.get("current_status")
            if is_active_blocker(status):
                blockers.append(
                    f"{no_go_rel} {row.get('claim_id', '<unknown>')} is {status}; "
                    f"prohibited claim '{row.get('prohibited_claim', '<missing claim>')}' blocks Stage 11"
                )

    for row in read_rows("evidence/evidence_gap_register.csv"):
        if row.get("gap_id") == "EG-0035" and normalise(row.get("status")) in {"open", "controlled_open"}:
            blockers.append(
                "evidence/evidence_gap_register.csv EG-0035 is open; FBC evidence packet, legal sign-offs, "
                "S151 review, consultation disposition and implementation readiness are not populated"
            )

    for row in read_rows("governance/approvals_register.csv"):
        if row.get("approval_id") == "APP-0025" and "gate_blocked" in normalise(row.get("status")):
            blockers.append(
                "governance/approvals_register.csv APP-0025 is a simulation control approval only; "
                "it does not approve FBC, statutory submission or implementation"
            )

    for row in read_rows("governance/simulation_signoff_register.csv"):
        if row.get("signoff_id") in {"SSO-0060", "SSO-0061"}:
            decision = normalise(row.get("decision"))
            if "conditions" in decision or "no-go" in decision:
                blockers.append(
                    f"governance/simulation_signoff_register.csv {row.get('signoff_id')} "
                    "is limited to simulation controls and does not clear Stage 11"
                )

    return blockers


def collect_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_gate_checklist())
    errors.extend(check_assurance_panel())
    errors.extend(check_no_go_register())
    if not collect_fbc_statutory_gate_blockers():
        errors.append("Stage 11 FBC/statutory gate unexpectedly has no live readiness blockers")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", action="store_true")
    args = parser.parse_args()

    blockers = collect_fbc_statutory_gate_blockers()
    if args.gate:
        if blockers:
            print("ERROR: Stage 11 FBC/statutory gate blocked by open P0/P1 and integrated readiness blockers.", file=sys.stderr)
            for blocker in blockers:
                print(f"ERROR: {blocker}", file=sys.stderr)
            return 1
        print("Stage 11 FBC/statutory gate passed")
        return 0

    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("FBC/statutory gate QA passed; Stage 11 FBC/statutory gate remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

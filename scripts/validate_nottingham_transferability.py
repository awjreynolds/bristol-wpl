#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTER = "analysis/economic/nottingham_lessons_register.csv"
TRANSFERABILITY_MATRIX = "analysis/economic/nottingham-transferability-matrix.csv"
DISPLACEMENT_CHECKLIST = "analysis/economic/nottingham-displacement-control-checklist.csv"
REQUIRED_HEADERS = [
    "lesson_id",
    "lesson_theme",
    "nottingham_or_comparator_evidence",
    "bristol_relevance",
    "evidence_strength",
    "transfer_condition",
    "prohibited_overclaim",
    "required_bristol_evidence",
    "current_status",
    "owner",
]

REQUIRED_LESSONS = {
    "NLR-0001": "displaced_parking_cpz",
    "NLR-0002": "public_transport_package",
    "NLR-0003": "no_charge_transfer",
    "NLR-0004": "no_elasticity_transfer",
    "NLR-0005": "evidence_caution",
    "NLR-0006": "employer_support_shadow_year",
    "NLR-0007": "residential_baseline_before_boundary",
    "NLR-0008": "cpz_rpz_mitigation_not_ready",
    "NLR-0009": "monitoring_triggers_and_adaptive_controls",
    "NLR-0010": "current_nottingham_refresh_gap",
    "NLR-0011": "revenue_and_net_proceeds_no_transfer",
    "NLR-0012": "source_hierarchy_controls",
    "NLR-0013": "public_acceptability_no_transfer",
    "NLR-0014": "mode_congestion_package_separation",
    "NLR-0015": "employer_behaviour_no_transfer",
}

REQUIRED_TRANSFERABILITY_TOPICS = {
    "charge_level",
    "parking_base_distribution",
    "behavioural_response_elasticity",
    "congestion_or_traffic_effect",
    "mode_shift",
    "enforcement_or_compliance_assumption",
    "revenue_collection_net_proceeds",
    "source_hierarchy",
    "public_acceptability",
    "mode_congestion_package_separation",
    "employer_behaviour",
}

REQUIRED_DISPLACEMENT_CHECKS = {
    "residential_street_baseline",
    "boundary_options_displacement",
    "cpz_rpz_options",
    "equality_accessibility",
    "monitoring_triggers",
    "employer_behaviour",
    "current_nottingham_refresh",
}

FORBIDDEN_DOC_PHRASES = [
    "Nottingham proves Bristol",
    "Nottingham guarantees",
    "Bristol will achieve Nottingham",
]

REQUIRED_BRIEFING_PHRASES = [
    "lessons only",
    "does not claim that Nottingham outcomes will happen in Bristol",
    "Transferability Questions For Bristol",
    "Potential residential spillover must be assessed early",
    "options to be appraised, designed, costed and consulted on before reliance",
    "Stage 18A",
    "residential street baseline",
    "CPZ/RPZ mitigation is not automatically ready",
    "current charge",
    "not mean the evidence exists",
]

REQUIRED_DASHBOARD_PHRASES = [
    "Not transferable to Bristol yet",
    "RED for reliance / AMBER for lessons control",
    "options to assess, not selected mitigation",
]

REQUIRED_PUBLIC_PHRASES = [
    "Learning from Nottingham means identifying questions for Bristol; it does not mean Bristol would get the same impacts or already has a parking-mitigation plan.",
]

REQUIRED_README_PHRASES = [
    "Nottingham/comparator lessons",
    "lessons are not Bristol forecasts or ready mitigations",
]

REQUIRED_CROSS_REGISTER_STATUSES = [
    ("governance/issues_register.csv", "issue_id", "ISS-0003", "status", {"open"}),
    ("governance/issues_register.csv", "issue_id", "ISS-0005", "status", {"open"}),
    ("evidence/evidence_gap_register.csv", "gap_id", "EG-0008", "status", {"open"}),
    ("evidence/evidence_gap_register.csv", "gap_id", "EG-0014", "status", {"open"}),
    ("governance/pitfalls_register.csv", "pitfall_id", "PIT-0005", "current_status", {"open"}),
    ("governance/risk_register.csv", "risk_id", "RISK-0009", "status", {"open"}),
]

FORBIDDEN_TRANSFER_PATTERNS = [
    re.compile(
        r"\b(?:Nottingham|TfL|Leicester)\b.{0,120}\b(?:proves|guarantees|confirms|demonstrates)\b.{0,80}\bBristol\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:Nottingham|TfL|Leicester)\b.{0,120}\bBristol (?:will|would|is expected to)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:Nottingham|TfL|Leicester)\b.{0,120}\b(?:reduces congestion|raises revenue|delivers mode shift|proves public acceptability|proves employer behaviour)\b",
        re.IGNORECASE,
    ),
]

FORBIDDEN_CPZ_READY_PATTERNS = [
    re.compile(r"\bCPZ/RPZ\b.{0,100}\b(?:is|are) (?:selected|costed|consulted|ready|enforceable)\b", re.IGNORECASE),
    re.compile(r"\bselected mitigation\b", re.IGNORECASE),
    re.compile(r"\bready mitigation\b", re.IGNORECASE),
]

NEGATION_TERMS = (
    "not ",
    "no ",
    "must not",
    "cannot",
    "does not",
    "do not",
    "without",
    "before reliance",
    "blocked",
    "prohibited",
    "no-go",
)


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def row_by(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {row.get(key, ""): row for row in rows}


def has_negation(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in NEGATION_TERMS)


def check_phrases(errors: list[str], rel: str, phrases: list[str]) -> str:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing {rel}")
        return ""
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            errors.append(f"{rel} missing phrase: {phrase}")
    return text


def check_forbidden_claims(errors: list[str], label: str, text: str) -> None:
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in FORBIDDEN_TRANSFER_PATTERNS:
            if pattern.search(line) and not has_negation(line):
                errors.append(f"{label}:{line_number} contains unsupported comparator transfer claim")
        for pattern in FORBIDDEN_CPZ_READY_PATTERNS:
            if pattern.search(line) and not has_negation(line):
                errors.append(f"{label}:{line_number} implies CPZ/RPZ mitigation readiness")


def check_cross_register_statuses(errors: list[str]) -> None:
    cache: dict[str, list[dict[str, str]]] = {}
    for rel, id_column, required_id, status_column, expected_statuses in REQUIRED_CROSS_REGISTER_STATUSES:
        if rel not in cache:
            if not (ROOT / rel).exists():
                errors.append(f"missing cross-register file: {rel}")
                continue
            cache[rel] = read_rows(rel)
        row = row_by(cache[rel], id_column).get(required_id)
        if row is None:
            errors.append(f"{rel} missing required row: {required_id}")
            continue
        status = row.get(status_column, "")
        if status not in expected_statuses:
            expected = ", ".join(sorted(expected_statuses))
            errors.append(f"{rel} {required_id} must have {status_column} in {{{expected}}}; found {status}")


def collect_errors() -> list[str]:
    path = ROOT / REGISTER
    if not path.exists():
        return [f"missing Nottingham lessons register: {REGISTER}"]
    errors = []
    header = read_header(REGISTER)
    for column in REQUIRED_HEADERS:
        if column not in header:
            errors.append(f"{REGISTER} missing column {column}")
    rows = read_rows(REGISTER)
    by_id = row_by(rows, "lesson_id")
    for lesson_id, theme in REQUIRED_LESSONS.items():
        row = by_id.get(lesson_id)
        if row is None:
            errors.append(f"{REGISTER} missing required lesson: {lesson_id}")
            continue
        if row.get("lesson_theme") != theme:
            errors.append(f"{REGISTER} {lesson_id} must use lesson_theme {theme}")
        if row.get("current_status") != "blocked":
            errors.append(f"{REGISTER} {lesson_id} must remain blocked")
    for row in rows:
        lesson_id = row.get("lesson_id", "<unknown>")
        if row.get("current_status") != "blocked":
            errors.append(f"{REGISTER} {lesson_id} must remain blocked")
        if not row.get("prohibited_overclaim"):
            errors.append(f"{REGISTER} {lesson_id} missing prohibited overclaim")
        if not row.get("required_bristol_evidence"):
            errors.append(f"{REGISTER} {lesson_id} missing required Bristol evidence")
        if "SRC-ACADEMIC-0001" in " ".join(row.values()) and not any(
            marker in " ".join(row.values()).lower()
            for marker in ["failed", "acquisition gap", "unavailable"]
        ):
            errors.append(f"{REGISTER} {lesson_id} uses SRC-ACADEMIC-0001 without failed-acquisition caveat")
        scannable = " ".join(
            row.get(column, "")
            for column in [
                "nottingham_or_comparator_evidence",
                "bristol_relevance",
                "transfer_condition",
                "required_bristol_evidence",
                "current_status",
                "owner",
            ]
        )
        check_forbidden_claims(errors, f"{REGISTER} {lesson_id}", scannable)
    matrix_path = ROOT / TRANSFERABILITY_MATRIX
    if not matrix_path.exists():
        errors.append(f"missing Nottingham transferability matrix: {TRANSFERABILITY_MATRIX}")
    else:
        matrix_rows = read_rows(TRANSFERABILITY_MATRIX)
        topics = {row.get("nottingham_assumption_or_evidence", "") for row in matrix_rows}
        for topic in sorted(REQUIRED_TRANSFERABILITY_TOPICS - topics):
            errors.append(f"{TRANSFERABILITY_MATRIX} missing required topic: {topic}")
        for row in matrix_rows:
            transferability_id = row.get("transferability_id", "<unknown>")
            if row.get("transferability_status") != "blocked":
                errors.append(f"{TRANSFERABILITY_MATRIX} {transferability_id} must remain blocked")
            if not row.get("required_bristol_evidence"):
                errors.append(f"{TRANSFERABILITY_MATRIX} {transferability_id} missing required Bristol evidence")
            notes = row.get("notes", "")
            if not any(marker in notes.lower() for marker in ["no ", "not ", "cannot", "must not", "without", "only", "do not"]):
                errors.append(f"{TRANSFERABILITY_MATRIX} {transferability_id} missing no-transfer note")
            check_forbidden_claims(
                errors,
                f"{TRANSFERABILITY_MATRIX} {transferability_id}",
                " ".join(
                    row.get(column, "")
                    for column in [
                        "bristol_use_requested",
                        "required_bristol_evidence",
                        "transferability_status",
                        "reviewer",
                        "notes",
                    ]
                ),
            )
    checklist = ROOT / DISPLACEMENT_CHECKLIST
    if not checklist.exists():
        errors.append(f"missing Nottingham displacement checklist: {DISPLACEMENT_CHECKLIST}")
    else:
        checklist_rows = read_rows(DISPLACEMENT_CHECKLIST)
        areas = {row.get("control_area", "") for row in checklist_rows}
        for area in sorted(REQUIRED_DISPLACEMENT_CHECKS - areas):
            errors.append(f"{DISPLACEMENT_CHECKLIST} missing required control_area: {area}")
        for row in checklist_rows:
            check_id = row.get("check_id", "<unknown>")
            if row.get("current_status") != "blocked":
                errors.append(f"{DISPLACEMENT_CHECKLIST} {check_id} must remain blocked")
            if not row.get("required_bristol_evidence"):
                errors.append(f"{DISPLACEMENT_CHECKLIST} {check_id} missing required Bristol evidence")
            if not row.get("no_go_note"):
                errors.append(f"{DISPLACEMENT_CHECKLIST} {check_id} missing no-go note")
    briefing_text = check_phrases(
        errors,
        "docs/officer/nottingham-and-comparator-lessons.md",
        REQUIRED_BRIEFING_PHRASES,
    )
    dashboard_text = check_phrases(errors, "docs/officer/assurance-dashboard.md", REQUIRED_DASHBOARD_PHRASES)
    public_text = check_phrases(errors, "docs/public/README.md", REQUIRED_PUBLIC_PHRASES)
    readme_text = check_phrases(errors, "README.md", REQUIRED_README_PHRASES)
    for label, text in [
        ("docs/officer/nottingham-and-comparator-lessons.md", briefing_text),
        ("docs/officer/assurance-dashboard.md", dashboard_text),
        ("docs/public/README.md", public_text),
        ("README.md", readme_text),
    ]:
        for phrase in FORBIDDEN_DOC_PHRASES:
            if phrase in text:
                errors.append(f"{label} contains forbidden phrase: {phrase}")
        check_forbidden_claims(errors, label, text)
    check_cross_register_statuses(errors)
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Nottingham transferability QA passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

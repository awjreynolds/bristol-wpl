#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/consultation/stage-8a-consultation-readiness-control-package.md",
    "consultation/controls/launch-readiness-register.csv",
    "consultation/controls/stakeholder-coverage-register.csv",
    "consultation/controls/materials-output-register.csv",
    "consultation/controls/response-analysis-control-register.csv",
    "consultation/controls/privacy-accessibility-register.csv",
    "consultation/controls/no-go-claim-register.csv",
    "consultation/materials/material-version-register.csv",
    "consultation/accessibility/alternative-format-register.csv",
    "consultation/privacy/privacy-notice-control.md",
    "analysis/data-protection-and-cyber/stage-8a-consultation-response-data-controls.md",
    "consultation/analysis/coding-frame.csv",
    "consultation/analysis/representativeness-plan.md",
    "consultation/analysis/duplicate-campaign-handling-protocol.md",
    "consultation/response_data/README.md",
    "schemas/consultation-response.schema.json",
    "review/accessibility_review/stage-8a-accessibility-control-report.md",
    "docs/stages/stage-8a-consultation-readiness.md",
    "review/peer_review/stage-8a-consultation-readiness-review.md",
    "review/stage_gate_reports/stage-8a-consultation-readiness-control-report.md",
]

CSV_HEADERS = {
    "consultation/controls/launch-readiness-register.csv": [
        "readiness_id",
        "launch_area",
        "required_evidence",
        "linked_issue_ids",
        "linked_risk_ids",
        "current_status",
        "gate_effect",
    ],
    "consultation/controls/stakeholder-coverage-register.csv": [
        "stakeholder_group",
        "coverage_status",
        "required_engagement_route",
        "accessibility_or_inclusion_need",
        "owner",
        "reviewer",
    ],
    "consultation/controls/materials-output-register.csv": [
        "material_id",
        "material_name",
        "future_path",
        "allowed_formats",
        "current_status",
    ],
    "consultation/controls/response-analysis-control-register.csv": [
        "analysis_control_id",
        "analysis_area",
        "required_control",
        "current_status",
        "owner",
        "reviewer",
    ],
    "consultation/controls/privacy-accessibility-register.csv": [
        "control_id",
        "control_area",
        "required_control",
        "current_status",
        "gate_effect",
    ],
    "consultation/controls/no-go-claim-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_stage_8a_wording",
        "source_gate",
        "gate_effect",
    ],
    "consultation/materials/material-version-register.csv": [
        "material_id",
        "material_name",
        "planned_path",
        "allowed_suffixes",
        "version_status",
        "owner",
        "reviewer",
    ],
    "consultation/accessibility/alternative-format-register.csv": [
        "format_id",
        "format",
        "audience_need",
        "decision_evidence_required",
        "current_status",
        "owner",
        "reviewer",
    ],
    "consultation/analysis/coding-frame.csv": [
        "code_id",
        "theme_area",
        "code_label",
        "inclusion_rule",
        "exclusion_rule",
        "current_status",
        "owner",
        "reviewer",
    ],
    "consultation/stakeholder_map.csv": [
        "stakeholder_id",
        "stage8_stakeholder_class",
        "inclusion_rationale",
        "source_ids_or_gap_status",
        "accessibility_needs",
        "digital_exclusion_risk",
        "engagement_route",
        "owner",
        "reviewer",
        "status",
    ],
}

CONSULTATION_OUTPUT_ROOTS = [
    "consultation/materials",
    "consultation/questionnaire",
    "consultation/consultation_report",
    "consultation/you_said_we_did",
    "consultation/response_data",
]

RESTRICTED_RESPONSE_ROOTS = [
    "consultation/response_data/raw",
    "consultation/response_data/personal",
]

ALLOWED_STAGE8A_CONTROL_FILES_IN_OUTPUT_ROOTS = {
    "consultation/materials/.gitkeep",
    "consultation/materials/material-version-register.csv",
    "consultation/questionnaire/.gitkeep",
    "consultation/consultation_report/.gitkeep",
    "consultation/you_said_we_did/.gitkeep",
    "consultation/response_data/.gitkeep",
    "consultation/response_data/README.md",
}

REQUIRED_MATERIAL_SUFFIXES = {
    "-public.html",
    "-officer-review.docx",
    "-print-ready.docx",
    "-plain-language.html",
    "-easy-read.docx",
    "-large-print.docx",
    "-translated-<bcp47>.docx",
}

FORBIDDEN_MATERIAL_SUFFIX_MARKERS = {".pdf", "final"}

REQUIRED_STAKEHOLDER_GROUPS = {
    "liable_employers",
    "potentially_liable_employers",
    "small_medium_businesses",
    "major_employment_sites",
    "education",
    "nhs_care",
    "emergency_services",
    "charities_voluntary_bodies",
    "public_sector_employers",
    "disabled_people_representative_groups",
    "shift_workers",
    "low_paid_workers",
    "carers",
    "women_trip_chaining",
    "trade_unions",
    "business_organisations",
    "transport_operators",
    "residents",
    "neighbouring_authorities",
    "weca_mca",
    "dft",
    "freight_logistics",
    "visitors_commuters",
    "limited_digital_access_groups",
}

REQUIRED_PHRASES = {
    "analysis/consultation/stage-8a-consultation-readiness-control-package.md": [
        "does not launch consultation",
        "No consultation materials are created in Stage 8A",
        "Consultation launch remains blocked",
    ],
    "analysis/data-protection-and-cyber/stage-8a-consultation-response-data-controls.md": [
        "Stage 8A does not collect consultation responses",
        "personal_data_in_repo=false",
        "Consultation launch remains blocked",
    ],
    "consultation/response_data/README.md": [
        "No consultation response data may be stored here during Stage 8A",
    ],
}

FORBIDDEN_POSITIVE_CLAIMS = [
    "consultation is ready to launch",
    "consultation has launched",
    "consultation is lawful",
    "consultation is formative",
    "decision-maker authority to consult is evidenced",
    "materials are complete",
    "materials are approved",
    "questionnaire is ready",
    "privacy notice is ready",
]

FORBIDDEN_POSITIVE_PATTERNS = [
    ("consultation launch readiness", re.compile(r"\bconsultation\b.*\b(ready to launch|launch[- ]ready|launched|has launched)\b", re.IGNORECASE)),
    ("lawful/formative consultation certification", re.compile(r"\bconsultation\b.*\b(lawful|formative)\b.*\b(certified|confirmed|approved|ready)\b", re.IGNORECASE)),
    ("materials readiness", re.compile(r"\b(materials?|questionnaire|privacy notice|analysis plan|coding frame|response schema)\b.*\b(ready|approved|complete|created|available)\b", re.IGNORECASE)),
    ("authority to consult", re.compile(r"\bauthority to consult\b.*\b(evidenced|approved|confirmed|ready)\b", re.IGNORECASE)),
]

NEGATING_CONTEXT = (
    "does not",
    "do not",
    "must not",
    "no ",
    "not ",
    "without",
    "blocked",
    "no-go",
    "cannot",
    "remains",
)

EXEMPT_CLAIM_LIST_HEADINGS = (
    "banned claims",
    "what stage 8a does not claim",
    "no-go claims",
)

CLOSED_STATUSES = {"closed", "resolved", "accepted_closed"}


def read_header(rel: str) -> list[str]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))


def read_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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


def is_closed_status(status: str | None) -> bool:
    return normalise(status) in CLOSED_STATUSES


def issue_launch_error(row: dict[str, str]) -> str | None:
    status = row.get("status", "")
    severity = row.get("severity", "")
    issue_id = row.get("issue_id", "<unknown>")
    if is_closed_status(status):
        return None
    if severity == "P0":
        return f"{issue_id} is {status}; open P0 issue blocks consultation launch"
    if severity == "P1":
        return f"{issue_id} is {status}; P1 issue is launch-blocking until condition owner deadline and residual risk are accepted"
    return None


def risk_launch_error(row: dict[str, str]) -> str | None:
    status = row.get("status", "")
    gross_rating = row.get("gross_rating", "")
    residual_rating = row.get("residual_rating", "")
    risk_id = row.get("risk_id", "<unknown>")
    if is_closed_status(status):
        return None
    if gross_rating == "P0" or residual_rating == "P0":
        return f"{risk_id} is {status}; open P0 risk blocks consultation launch"
    if gross_rating == "P1" or residual_rating == "P1":
        return f"{risk_id} is {status}; P1 risk is launch-blocking until condition owner deadline and residual risk are accepted"
    return None


def collect_launch_blockers() -> list[str]:
    blockers = []
    for row in read_rows("governance/issues_register.csv"):
        error = issue_launch_error(row)
        if error:
            blockers.append(error)
    for row in read_rows("governance/risk_register.csv"):
        error = risk_launch_error(row)
        if error:
            blockers.append(error)
    return blockers


def check_required_files() -> list[str]:
    return [
        f"missing required Stage 8A consultation control file: {rel}"
        for rel in REQUIRED_FILES
        if not (ROOT / rel).exists()
    ]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required Stage 8A CSV: {rel}")
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
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required no-go phrase: {phrase}")
    return errors


def check_output_roots_empty() -> list[str]:
    errors = []
    for rel_root in CONSULTATION_OUTPUT_ROOTS:
        root = ROOT / rel_root
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in ALLOWED_STAGE8A_CONTROL_FILES_IN_OUTPUT_ROOTS:
                continue
            errors.append(f"Stage 8A forbids authored consultation output or response data while launch is blocked: {rel}")
    return errors


def check_restricted_response_paths_empty() -> list[str]:
    errors = []
    for rel_root in RESTRICTED_RESPONSE_ROOTS:
        root = ROOT / rel_root
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.name != ".gitkeep":
                errors.append(f"restricted consultation response file present in normal repo path: {path.relative_to(ROOT).as_posix()}")
    return errors


def check_stakeholder_coverage() -> list[str]:
    rel = "consultation/controls/stakeholder-coverage-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing stakeholder coverage register: {rel}"]
    rows = read_rows(rel)
    present = {row.get("stakeholder_group", "") for row in rows}
    errors = [f"{rel} missing required stakeholder group: {group}" for group in sorted(REQUIRED_STAKEHOLDER_GROUPS - present)]
    for row in rows:
        if row.get("coverage_status") != "control_placeholder":
            errors.append(f"{rel} {row.get('stakeholder_group', '<unknown>')} must remain control_placeholder")
    return errors


def check_control_rows_blocked(rel: str, id_column: str, status_column: str = "current_status") -> list[str]:
    errors = []
    if not (ROOT / rel).exists():
        return [f"missing control register: {rel}"]
    for row in read_rows(rel):
        if row.get(status_column) != "blocked_control_only":
            errors.append(f"{rel} {row.get(id_column, '<unknown>')} must remain blocked_control_only")
    return errors


def check_material_version_register() -> list[str]:
    rel = "consultation/materials/material-version-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing material version register: {rel}"]
    errors = []
    suffixes_seen: set[str] = set()
    for row in read_rows(rel):
        material_id = row.get("material_id", "<unknown>")
        if row.get("version_status") != "blocked_control_only":
            errors.append(f"{rel} {material_id} must remain blocked_control_only")
        allowed_suffixes = {
            suffix.strip()
            for suffix in row.get("allowed_suffixes", "").split(";")
            if suffix.strip()
        }
        suffixes_seen.update(allowed_suffixes)
        for suffix in allowed_suffixes:
            lowered = suffix.lower()
            if any(marker in lowered for marker in FORBIDDEN_MATERIAL_SUFFIX_MARKERS):
                errors.append(f"{rel} {material_id} uses forbidden output suffix marker: {suffix}")
    missing = REQUIRED_MATERIAL_SUFFIXES - suffixes_seen
    for suffix in sorted(missing):
        errors.append(f"{rel} missing required future editable/accessibility suffix control: {suffix}")
    return errors


def check_response_schema() -> list[str]:
    rel = "schemas/consultation-response.schema.json"
    path = ROOT / rel
    if not path.exists():
        return [f"missing consultation response schema: {rel}"]
    errors = []
    schema = json.loads(path.read_text(encoding="utf-8"))
    if schema.get("additionalProperties") is not False:
        errors.append(f"{rel} must set additionalProperties to false")
    required = set(schema.get("required", []))
    expected_required = {
        "response_id",
        "channel",
        "stakeholder_category",
        "response_item_refs",
        "coding_status",
        "representativeness",
        "publication_consent",
        "raw_external_reference",
        "personal_data_in_repo",
    }
    for column in sorted(expected_required - required):
        errors.append(f"{rel} missing required processed-response field: {column}")
    properties = set(schema.get("properties", {}))
    forbidden_properties = {"name", "email", "address", "phone", "postcode", "ip_address", "free_text_raw"}
    for prop in sorted(properties & forbidden_properties):
        errors.append(f"{rel} must not allow direct identifier property in processed repo records: {prop}")
    personal_data = schema.get("properties", {}).get("personal_data_in_repo", {})
    if personal_data.get("const") is not False:
        errors.append(f"{rel} personal_data_in_repo must be const false")
    return errors


def check_headline_percentage_controls() -> list[str]:
    errors = []
    analysis_root = ROOT / "consultation/analysis"
    if not analysis_root.exists():
        return errors
    pattern = re.compile(r"\b(support|oppos|agree|disagree)[A-Za-z ]{0,30}\b[0-9]{1,3}\s?%", re.IGNORECASE)
    for path in analysis_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".csv"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            lowered = line.lower()
            if pattern.search(line) and "representativeness" not in lowered and "coding" not in lowered:
                errors.append(f"{rel}:{line_number} includes headline percentage language without coding and representativeness controls")
    return errors


def line_has_positive_claim(line: str) -> str | None:
    lowered = line.lower()
    if any(context in lowered for context in NEGATING_CONTEXT):
        return None
    for claim in FORBIDDEN_POSITIVE_CLAIMS:
        if claim.lower() in lowered:
            return claim
    for label, pattern in FORBIDDEN_POSITIVE_PATTERNS:
        if pattern.search(line):
            return label
    return None


def heading_level(line: str) -> int | None:
    stripped = line.strip()
    if not stripped.startswith("#"):
        return None
    return len(stripped) - len(stripped.lstrip("#"))


def is_exempt_claim_list_heading(line: str) -> bool:
    lowered = line.strip("# ").strip().lower()
    return any(heading in lowered for heading in EXEMPT_CLAIM_LIST_HEADINGS)


def check_positive_claims() -> list[str]:
    errors = []
    paths = [
        "README.md",
        "docs/stages/stage-8a-consultation-readiness.md",
        "analysis/consultation/stage-8a-consultation-readiness-control-package.md",
        "review/peer_review/stage-8a-consultation-readiness-review.md",
        "review/stage_gate_reports/stage-8a-consultation-readiness-control-report.md",
    ]
    for rel in paths:
        path = ROOT / rel
        if not path.exists():
            continue
        exempt_level = None
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            level = heading_level(line)
            if level is not None:
                if exempt_level is not None and level <= exempt_level:
                    exempt_level = None
                if is_exempt_claim_list_heading(line):
                    exempt_level = level
                    continue
            if exempt_level is not None:
                continue
            claim = line_has_positive_claim(line)
            if claim:
                errors.append(f"{rel}:{line_number} includes forbidden positive consultation readiness claim: {claim}")
    return errors


def check_no_go_claims() -> list[str]:
    rel = "consultation/controls/no-go-claim-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing no-go claim register: {rel}"]
    required = {
        "consultation is ready to launch",
        "consultation has launched",
        "consultation is lawful or formative",
        "decision-maker authority to consult is evidenced",
        "materials are complete accessible or approved",
        "questionnaire analysis plan response schema coding frame or privacy notice is ready",
    }
    present = {row.get("prohibited_claim", "") for row in read_rows(rel)}
    return [f"{rel} missing prohibited claim: {claim}" for claim in sorted(required - present)]


def collect_control_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_output_roots_empty())
    errors.extend(check_restricted_response_paths_empty())
    errors.extend(check_stakeholder_coverage())
    errors.extend(check_control_rows_blocked("consultation/controls/launch-readiness-register.csv", "readiness_id"))
    errors.extend(check_control_rows_blocked("consultation/controls/materials-output-register.csv", "material_id"))
    errors.extend(check_control_rows_blocked("consultation/controls/response-analysis-control-register.csv", "analysis_control_id"))
    errors.extend(check_control_rows_blocked("consultation/controls/privacy-accessibility-register.csv", "control_id"))
    errors.extend(check_control_rows_blocked("consultation/accessibility/alternative-format-register.csv", "format_id"))
    errors.extend(check_control_rows_blocked("consultation/analysis/coding-frame.csv", "code_id"))
    errors.extend(check_material_version_register())
    errors.extend(check_response_schema())
    errors.extend(check_headline_percentage_controls())
    errors.extend(check_no_go_claims())
    errors.extend(check_positive_claims())
    if not collect_launch_blockers():
        errors.append("consultation launch gate unexpectedly has no blockers during Stage 8A")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--launch-gate", action="store_true")
    args = parser.parse_args()
    errors = collect_launch_blockers() if args.launch_gate else collect_control_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.launch_gate:
        print("Consultation launch gate passed")
    else:
        print("Consultation QA passed for Stage 8A controls; consultation launch remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

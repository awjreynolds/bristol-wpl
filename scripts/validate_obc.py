#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/obc/stage-6a-obc-readiness-control-package.md",
    "business_case/obc/controls/section-dependency-matrix.csv",
    "business_case/obc/controls/section-readiness-register.csv",
    "business_case/obc/controls/section-claim-dependency-register.csv",
    "business_case/obc/controls/no-go-claim-register.csv",
    "business_case/obc/controls/obc-assurance-review-plan.md",
    "business_case/shared/assembly_manifest.md",
    "scripts/assemble_obc.py",
]

CSV_HEADERS = {
    "business_case/obc/controls/section-dependency-matrix.csv": [
        "section_id",
        "case_section",
        "section_path",
        "dependency_area",
        "required_evidence",
        "required_register_rows",
        "allowed_statuses",
        "blocker_ids",
        "current_status",
        "gate_effect",
    ],
    "business_case/obc/controls/section-readiness-register.csv": [
        "section_id",
        "case_section",
        "required_upstream_gate",
        "current_status",
        "minimum_evidence_before_drafting",
        "gate_effect",
    ],
    "business_case/obc/controls/section-claim-dependency-register.csv": [
        "claim_id",
        "section",
        "claim_text",
        "claim_type",
        "source_ids",
        "evidence_cutoff",
        "linked_issue_ids",
        "linked_risk_ids",
        "linked_evidence_gaps",
        "linked_requirements",
        "statutory_crosswalk_rows",
        "model_run_or_dataset_id",
        "package_or_cost_line_id",
        "dependency_status",
        "P0_P1_effect",
        "blocked_readiness_claims",
        "required_reviewer",
        "simulation_signoff_id",
        "limitations",
        "owner",
        "next_gate_condition",
    ],
    "business_case/obc/controls/no-go-claim-register.csv": [
        "claim_id",
        "prohibited_claim",
        "allowed_stage_6a_wording",
        "affected_sections",
        "source_gate",
        "gate_effect",
    ],
}

OBC_SECTION_FILES = [
    "business_case/obc/00-front-matter/document-control.md",
    "business_case/obc/01-executive-summary/executive-summary.md",
    "business_case/obc/02-strategic-case/strategic-case.md",
    "business_case/obc/03-economic-case/economic-case.md",
    "business_case/obc/04-commercial-case/commercial-case.md",
    "business_case/obc/05-financial-case/financial-case.md",
    "business_case/obc/06-management-case/management-case.md",
    "business_case/obc/07-conclusions-and-decisions/recommendations.md",
]

OBC_OUTPUT_ROOTS = [
    "business_case/obc/assembled",
    "deliverables/review/docx",
]

REQUIRED_PHRASES = {
    "analysis/obc/stage-6a-obc-readiness-control-package.md": [
        "does not assemble an OBC",
        "OBC/FBC, consultation or statutory-submission readiness",
        "Stage 6A assembly is blocked",
    ],
    "business_case/shared/assembly_manifest.md": [
        "Stage 6A creates OBC readiness and assembly-blocking controls only",
        "No assembled OBC or FBC should be generated",
    ],
}

FORBIDDEN_POSITIVE_CLAIMS = [
    "OBC is ready for approval",
    "approved OBC",
    "preferred scheme has been selected",
    "consultation can launch",
    "WECA/MCA has approved",
    "WECA supports",
    "DfT has accepted",
    "statutory submission is ready",
]

FORBIDDEN_POSITIVE_PATTERNS = [
    ("assembled OBC output", re.compile(r"\b(assembled\s+OBC|OBC\s+(has been\s+)?(assembled|created|generated))\b.*\b(created|generated|ready|available|assembled)?\b", re.IGNORECASE)),
    ("officer-review DOCX output", re.compile(r"\bofficer[- ]review\b.*\bDOCX\b.*\b(created|generated|ready|available)\b", re.IGNORECASE)),
    ("BCR decision-grade claim", re.compile(r"\bBCR\b.*\b(decision[- ]grade|ready|approved|created|available)\b", re.IGNORECASE)),
    ("VFM decision-grade claim", re.compile(r"\bVFM\b.*\b(decision[- ]grade|ready|approved|created|available)\b", re.IGNORECASE)),
    ("benefits decision-grade claim", re.compile(r"\bbenefits?\b.*\b(decision[- ]grade|ready|approved|quantified|created|available)\b", re.IGNORECASE)),
    ("boundary decision-grade claim", re.compile(r"\bboundary\b.*\b(decision[- ]grade|ready|approved|created|available)\b", re.IGNORECASE)),
    ("charge-base decision-grade claim", re.compile(r"\bcharge[- ]base\b.*\b(decision[- ]grade|ready|approved|created|available)\b", re.IGNORECASE)),
    ("revenue decision-grade claim", re.compile(r"\brevenue\b.*\b(decision[- ]grade|ready|approved|created|available)\b", re.IGNORECASE)),
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
    "what stage 6a does not claim",
    "no-go claims",
)

ACTIVE_BLOCKING_STATUSES = {
    "open",
    "narrowed_open",
    "controlled_open",
    "partially_closed",
    "partially_controlled",
    "working",
}

CLOSED_STATUSES = {
    "closed",
    "resolved",
    "accepted_closed",
}


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


def issue_readiness_error(row: dict[str, str]) -> str | None:
    status = row.get("status", "")
    severity = row.get("severity", "")
    issue_id = row.get("issue_id", "<unknown>")
    if is_closed_status(status):
        return None
    if severity == "P0":
        return f"{issue_id} is {status}; open P0 issue blocks OBC assembly"
    if severity == "P1" and not p1_issue_has_accepted_condition(row):
        return f"{issue_id} is {status}; P1 issue lacks Simulation Gate Authority condition with owner deadline and residual risk"
    return None


def risk_readiness_error(row: dict[str, str]) -> str | None:
    status = row.get("status", "")
    gross_rating = row.get("gross_rating", "")
    residual_rating = row.get("residual_rating", "")
    risk_id = row.get("risk_id", "<unknown>")
    if is_closed_status(status):
        return None
    if gross_rating == "P0" or residual_rating == "P0":
        return f"{risk_id} is {status}; open P0 risk blocks OBC assembly"
    if (gross_rating == "P1" or residual_rating == "P1") and not p1_risk_has_accepted_condition(row):
        return f"{risk_id} is {status}; P1 risk lacks Simulation Gate Authority condition with owner deadline and residual risk"
    return None


def collect_readiness_blockers() -> list[str]:
    blockers = []
    for row in read_rows("governance/issues_register.csv"):
        error = issue_readiness_error(row)
        if error:
            blockers.append(error)
    for row in read_rows("governance/risk_register.csv"):
        error = risk_readiness_error(row)
        if error:
            blockers.append(error)
    return blockers


def check_required_files() -> list[str]:
    return [
        f"missing required Stage 6A OBC control file: {rel}"
        for rel in REQUIRED_FILES
        if not (ROOT / rel).exists()
    ]


def check_csv_headers() -> list[str]:
    errors = []
    for rel, columns in CSV_HEADERS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required Stage 6A CSV: {rel}")
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


def check_section_control_notes() -> list[str]:
    errors = []
    for rel in OBC_SECTION_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing OBC section template: {rel}")
            continue
        if "Stage 6A Control Note" not in path.read_text(encoding="utf-8"):
            errors.append(f"{rel} missing Stage 6A Control Note")
    return errors


def check_obc_output_roots_empty() -> list[str]:
    errors = []
    for rel_root in OBC_OUTPUT_ROOTS:
        root = ROOT / rel_root
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.name == ".gitkeep":
                continue
            rel = path.relative_to(ROOT).as_posix()
            errors.append(f"Stage 6A forbids authored OBC output while assembly is blocked: {rel}")
    return errors


def check_dependency_matrix_blocks() -> list[str]:
    errors = []
    rel = "business_case/obc/controls/section-dependency-matrix.csv"
    if not (ROOT / rel).exists():
        return [f"missing section dependency matrix: {rel}"]
    rows = read_rows(rel)
    if not rows:
        return [f"{rel} has no control rows"]
    gate_effects = {row.get("gate_effect", "") for row in rows}
    if "P0" not in gate_effects:
        errors.append(f"{rel} must include at least one P0 blocker row")
    matrix_paths = {row.get("section_path", "") for row in rows}
    for section_path in OBC_SECTION_FILES:
        if section_path not in matrix_paths:
            errors.append(f"{rel} missing section_path row for {section_path}")
    for row in rows:
        section_id = row.get("section_id", "<unknown>")
        if row.get("current_status") != "blocked_control_only":
            errors.append(f"{rel} {section_id} must remain blocked_control_only")
        if "blocked_control_only" not in row.get("allowed_statuses", "").split(";"):
            errors.append(f"{rel} {section_id} must list blocked_control_only in allowed_statuses")
        if not row.get("required_register_rows"):
            errors.append(f"{rel} {section_id} missing required_register_rows")
    return errors


def check_claim_dependency_register() -> list[str]:
    errors = []
    rel = "business_case/obc/controls/section-claim-dependency-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing claim dependency register: {rel}"]
    rows = read_rows(rel)
    if len(rows) < 7:
        errors.append(f"{rel} must include at least one row for each main OBC section")
    sections = {row.get("section", "") for row in rows}
    required_sections = {
        "executive_summary",
        "strategic_case",
        "economic_case",
        "commercial_case",
        "financial_case",
        "management_case",
        "conclusions_and_decisions",
    }
    for section in required_sections - sections:
        errors.append(f"{rel} missing section row: {section}")
    for row in rows:
        claim_id = row.get("claim_id", "<unknown>")
        if row.get("dependency_status") != "blocked_control_only":
            errors.append(f"{rel} {claim_id} must remain blocked_control_only")
        if row.get("P0_P1_effect") not in {"P0", "P1"}:
            errors.append(f"{rel} {claim_id} must classify P0_P1_effect as P0 or P1")
        if not row.get("required_reviewer"):
            errors.append(f"{rel} {claim_id} missing required reviewer")
        if not row.get("next_gate_condition"):
            errors.append(f"{rel} {claim_id} missing next gate condition")
    return errors


def check_no_go_claims() -> list[str]:
    errors = []
    rel = "business_case/obc/controls/no-go-claim-register.csv"
    if not (ROOT / rel).exists():
        return [f"missing no-go claim register: {rel}"]
    rows = read_rows(rel)
    required = {
        "OBC is ready for approval",
        "preferred scheme has been selected",
        "consultation can launch",
        "boundary charge base or revenue is decision grade",
        "BCR VFM or benefits are decision grade",
        "statutory submission is ready",
    }
    present = {row.get("prohibited_claim", "") for row in rows}
    for claim in required:
        if claim not in present:
            errors.append(f"{rel} missing prohibited claim: {claim}")
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
        "docs/stages/stage-6a-obc-readiness.md",
        "analysis/obc/stage-6a-obc-readiness-control-package.md",
        "review/peer_review/stage-6a-obc-readiness-review.md",
        "review/stage_gate_reports/stage-6a-obc-readiness-control-report.md",
        *OBC_SECTION_FILES,
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
                errors.append(f"{rel}:{line_number} includes forbidden positive OBC readiness claim: {claim}")
    return errors


def check_assemble_obc_blocks() -> list[str]:
    result = subprocess.run(
        [sys.executable, "scripts/assemble_obc.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        return ["scripts/assemble_obc.py must exit non-zero while OBC assembly is blocked"]
    if "Stage 6A assembly blocked" not in result.stdout:
        return ["scripts/assemble_obc.py must explain that Stage 6A assembly is blocked"]
    return []


def collect_control_errors() -> list[str]:
    errors = []
    errors.extend(check_required_files())
    errors.extend(check_csv_headers())
    errors.extend(check_required_phrases())
    errors.extend(check_section_control_notes())
    errors.extend(check_obc_output_roots_empty())
    errors.extend(check_dependency_matrix_blocks())
    errors.extend(check_claim_dependency_register())
    errors.extend(check_no_go_claims())
    errors.extend(check_positive_claims())
    errors.extend(check_assemble_obc_blocks())
    if not collect_readiness_blockers():
        errors.append("OBC readiness gate unexpectedly has no blockers during Stage 6A")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readiness-gate", action="store_true")
    args = parser.parse_args()

    errors = collect_readiness_blockers() if args.readiness_gate else collect_control_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.readiness_gate:
        print("OBC readiness gate passed")
    else:
        print("OBC QA passed for Stage 6A controls; OBC assembly remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

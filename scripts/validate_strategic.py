#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/strategic/stage-3a-strategic-assessment-control-package.md",
    "analysis/strategic/problem-definition.md",
    "analysis/strategic/baseline-and-trends.md",
    "analysis/strategic/objectives-and-csfs.md",
    "analysis/strategic/theory-of-change.md",
    "analysis/strategic/benefits-map.md",
    "analysis/strategic/dependencies-and-constraints.md",
    "investment_programme/dependency_map.md",
]

CSV_HEADERS = {
    "analysis/strategic/strategic-evidence-status.csv": [
        "evidence_status_id",
        "strategic_area",
        "current_status",
        "required_evidence",
        "gate_effect",
    ],
    "investment_programme/package-control-register.csv": [
        "package_id",
        "status",
        "approval_status",
        "cost_status",
        "funding_status",
        "benefits_status",
    ],
    "investment_programme/funding/package-funding-assurance-classification.csv": [
        "package_or_cost_line_id",
        "wpl_relationship",
        "funding_sources",
        "weca_mca_trigger_class",
        "formal_decision_source",
        "gate_effect",
    ],
    "investment_programme/delivery_maturity/package-maturity-register.csv": [
        "package_id",
        "maturity_dimension",
        "current_status",
        "required_evidence",
        "gate_effect",
    ],
    "investment_programme/benefits/package-benefits-register.csv": [
        "package_benefit_id",
        "package_id",
        "benefit_area",
        "baseline",
        "target",
        "status",
    ],
    "governance/benefits_register.csv": [
        "benefit_id",
        "objective",
        "benefit",
        "baseline",
        "target",
        "attribution_route",
        "status",
    ],
}

REQUIRED_PHRASES = {
    "analysis/strategic/stage-3a-strategic-assessment-control-package.md": [
        "does not determine that a Workplace Parking Levy is the preferred intervention",
        "Stage 3A creates package controls only",
        "does not claim WECA/MCA approval, funding, consent, sponsorship or no-role status",
    ],
    "analysis/strategic/objectives-and-csfs.md": [
        "avoid prejudging WPL",
        "No final objective set",
    ],
    "analysis/strategic/benefits-map.md": [
        "does not quantify or approve benefits",
        "No benefit is quantified or approved",
        "Gross levy receipts must be treated as a transfer/public cash-flow item",
    ],
    "investment_programme/dependency_map.md": [
        "not a resolved dependency map",
        "No dependency is closed",
        "P0-blocked",
    ],
}

BENEFITS_REGISTER = "governance/benefits_register.csv"
PACKAGE_REGISTER = "investment_programme/package-control-register.csv"
PACKAGE_FUNDING_REGISTER = "investment_programme/funding/package-funding-assurance-classification.csv"

MCA_TRIGGER_TOKENS = (
    "mca",
    "crsts",
    "single pot",
    "single_pot",
    "tcr",
    "ltdp",
    "mass transit",
    "mass_transit",
    "programme-entry",
    "programme_entry",
    "delivery-funding",
    "delivery_funding",
    "programme-change",
    "programme_change",
)

MISSING_ROUTE_VALUES = {
    "",
    "gap",
    "n/a",
    "none",
    "not_applicable",
    "not_assessed",
    "not_defined",
    "not_evidenced",
}

STAGE3_TEXT_FILES = [
    "README.md",
    "docs/stages/stage-3a-strategic-assessment.md",
    "review/peer_review/stage-3a-strategic-assessment-review.md",
    "review/stage_gate_reports/stage-3a-strategic-assessment-control-report.md",
    *REQUIRED_FILES,
]

FORBIDDEN_POSITIVE_READINESS_PHRASES = [
    "the WPL will solve",
    "the preferred scheme is",
    "is the preferred scheme",
    "consultation-ready",
    "OBC-ready",
    "FBC-ready",
    "statutory submission ready",
    "WECA supports",
    "WECA/MCA has approved",
    "MCA has approved",
    "DfT-approved",
    "Bristol has approved implementation",
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
)


def read_csv_header(rel: str) -> list[str]:
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


def check_benefit_attribution() -> list[str]:
    errors = []
    path = ROOT / BENEFITS_REGISTER
    if not path.exists():
        return [f"missing required benefits register: {BENEFITS_REGISTER}"]
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return [f"{BENEFITS_REGISTER} has no control rows"]
    transfer_rows = [
        row
        for row in rows
        if row.get("attribution_route") == "transfer_public_cash_flow_not_economic_benefit"
    ]
    if not transfer_rows:
        errors.append(
            f"{BENEFITS_REGISTER} must include a transfer/public cash-flow row for gross levy receipts"
        )
    for row in rows:
        if row.get("status") != "control_placeholder":
            errors.append(
                f"{BENEFITS_REGISTER} {row.get('benefit_id', '<unknown>')} must remain control_placeholder at Stage 3A"
            )
    return errors


def read_dict_rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalise(value: str | None) -> str:
    return (value or "").strip().lower()


def is_missing_route_value(value: str | None) -> bool:
    return normalise(value) in MISSING_ROUTE_VALUES


def has_mca_trigger(value: str | None) -> bool:
    lowered = normalise(value).replace("-", "_")
    return any(token.replace("-", "_") in lowered for token in MCA_TRIGGER_TOKENS)


def check_package_funding_controls(
    package_rows: list[dict[str, str]],
    funding_rows: list[dict[str, str]],
) -> list[str]:
    errors = []
    package_ids = {row.get("package_id", "") for row in package_rows}
    for row in funding_rows:
        row_id = row.get("package_or_cost_line_id", "")
        if row.get("description") == "package_placeholder" and row_id not in package_ids:
            errors.append(
                f"{PACKAGE_FUNDING_REGISTER} placeholder row {row_id} must join to package-control-register package_id"
            )
        if has_mca_trigger(row.get("weca_mca_trigger_class")) and (
            is_missing_route_value(row.get("formal_decision_source"))
            or is_missing_route_value(row.get("assurance_route"))
        ) and row.get("gate_effect") != "P0":
            errors.append(
                f"{PACKAGE_FUNDING_REGISTER} {row_id} has unresolved MCA/funding assurance trigger and must have gate_effect P0"
            )
    return errors


def check_positive_readiness_claims() -> list[str]:
    errors = []
    for rel in STAGE3_TEXT_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            lowered = line.lower()
            if any(context in lowered for context in NEGATING_CONTEXT):
                continue
            for phrase in FORBIDDEN_POSITIVE_READINESS_PHRASES:
                if phrase.lower() in lowered:
                    errors.append(f"{rel}:{line_number} includes forbidden positive readiness claim: {phrase}")
    return errors


def main() -> int:
    errors = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required Stage 3A strategic control file: {rel}")
    for rel, required_columns in CSV_HEADERS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required Stage 3A CSV: {rel}")
            continue
        header = read_csv_header(rel)
        for column in required_columns:
            if column not in header:
                errors.append(f"{rel} missing column {column}")
        errors.extend(check_csv_widths(rel))
    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{rel} missing required no-go phrase: {phrase}")
    errors.extend(check_benefit_attribution())
    if (ROOT / PACKAGE_REGISTER).exists() and (ROOT / PACKAGE_FUNDING_REGISTER).exists():
        errors.extend(
            check_package_funding_controls(
                read_dict_rows(PACKAGE_REGISTER),
                read_dict_rows(PACKAGE_FUNDING_REGISTER),
            )
        )
    errors.extend(check_positive_readiness_claims())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Strategic QA passed for Stage 3A controls; Stage 3 gate remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

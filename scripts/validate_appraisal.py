#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/economic/stage-5a-options-appraisal-control-package.md",
    "analysis/economic/options-longlist.md",
    "analysis/economic/option-assessment-report.md",
    "analysis/economic/shortlisting-report.md",
    "analysis/economic/appraisal-specification-report.md",
    "analysis/economic/options-framework-filter.xlsx",
    "analysis/economic/appraisal-specification-summary-tables.xlsx",
    "analysis/economic/benefits-treatment-taxonomy.csv",
    "analysis/economic/nottingham-transferability-matrix.csv",
    "analysis/economic/boundary-parking-model-dependency-table.csv",
    "analysis/economic/appraisal-reviewer-matrix.csv",
    "analysis/economic/guidance-source-requirements.csv",
    "models/model_cards/model-card-template.md",
    "models/model_cards/parking-base-model-card.md",
    "models/model_cards/behavioural-response-model-card.md",
    "models/model_cards/transport-model-card.md",
    "models/model_cards/revenue-model-card.md",
    "models/model_cards/scheme-cost-model-card.md",
    "models/model_cards/economic-appraisal-model-card.md",
    "models/model_cards/financial-model-card.md",
    "models/outputs/model-run-manifest-template.json",
    "models/outputs/model-run-manifest-register.csv",
    "models/validation/model-validation-plan.md",
    "models/parking-base/parking-base-model-specification.md",
    "models/transport/transport-model-specification.md",
    "models/revenue/revenue-model-specification.md",
    "models/uncertainty/uncertainty-log.xlsx",
]

CSV_HEADERS = {
    "analysis/economic/options-framework-filter.csv": [
        "option_family_id",
        "option_family",
        "scope",
        "solution",
        "service_delivery",
        "implementation",
        "funding",
        "status",
    ],
    "analysis/economic/appraisal-specification-summary-tables.csv": [
        "impact_id",
        "appraisal_area",
        "sub_impact",
        "method",
        "data_required",
        "model_output_required",
        "monetisation_status",
        "uncertainty_treatment",
        "value_for_money_treatment",
        "status",
    ],
    "analysis/economic/asr-change-log.csv": [
        "change_id",
        "trigger_type",
        "affected_models",
        "asr_action_required",
        "status",
    ],
    "analysis/economic/reappraisal-trigger-table.csv": [
        "trigger_id",
        "trigger",
        "threshold",
        "affected_case",
        "required_action",
        "status",
    ],
    "models/uncertainty/uncertainty-register.csv": [
        "uncertainty_id",
        "affected_model",
        "affected_output",
        "uncertainty_type",
        "sensitivity_test",
        "status",
    ],
    "models/outputs/model-run-manifest-register.csv": [
        "run_id",
        "model_id",
        "model_version",
        "option_id",
        "input_hashes",
        "qa_status",
        "status",
    ],
    "analysis/economic/benefits-treatment-taxonomy.csv": [
        "treatment_id",
        "item",
        "classification",
        "appraisal_treatment",
        "required_review",
        "status",
    ],
    "analysis/economic/nottingham-transferability-matrix.csv": [
        "transferability_id",
        "nottingham_assumption_or_evidence",
        "bristol_use_requested",
        "required_bristol_evidence",
        "transferability_status",
    ],
    "analysis/economic/boundary-parking-model-dependency-table.csv": [
        "dependency_id",
        "claim_or_output",
        "blocked_by",
        "required_before_use",
        "status",
    ],
    "analysis/economic/appraisal-reviewer-matrix.csv": [
        "reviewer_id",
        "reviewer_role",
        "simulation_scope",
        "real_world_adoption_gap",
        "required_before",
        "status",
    ],
    "analysis/economic/guidance-source-requirements.csv": [
        "guidance_id",
        "guidance_area",
        "current_repo_source",
        "current_status",
        "required_before_use",
        "status",
    ],
}

REQUIRED_PHRASES = {
    "analysis/economic/stage-5a-options-appraisal-control-package.md": [
        "does not shortlist options",
        "gross levy receipts are economic benefits",
        "Stage 5 remains blocked",
    ],
    "analysis/economic/shortlisting-report.md": [
        "not a shortlist decision",
        "No option is shortlisted",
    ],
    "analysis/economic/appraisal-specification-report.md": [
        "not an agreed ASR",
        "No model output",
    ],
    "models/revenue/revenue-model-specification.md": [
        "contains no revenue estimate",
        "No chargeable-space forecast",
    ],
}


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


def check_benefits_taxonomy() -> list[str]:
    rel = "analysis/economic/benefits-treatment-taxonomy.csv"
    path = ROOT / rel
    if not path.exists():
        return [f"missing required Stage 5A CSV: {rel}"]
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    gross_receipts = [row for row in rows if row.get("item") == "gross_levy_receipts"]
    if not gross_receipts:
        return [f"{rel} missing gross_levy_receipts treatment row"]
    row = gross_receipts[0]
    errors = []
    if row.get("classification") != "transfer_payment":
        errors.append(f"{rel} gross_levy_receipts must be classified as transfer_payment")
    if row.get("appraisal_treatment") != "do_not_treat_as_economic_benefit":
        errors.append(
            f"{rel} gross_levy_receipts must use do_not_treat_as_economic_benefit"
        )
    return errors


def main() -> int:
    errors = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required Stage 5A appraisal control file: {rel}")
    for rel, required_columns in CSV_HEADERS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required Stage 5A CSV: {rel}")
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
    manifest = ROOT / "models/outputs/model-run-manifest-template.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{manifest.relative_to(ROOT)} is not valid JSON: {exc}")
        else:
            if data.get("status") != "template_only":
                errors.append("model-run-manifest-template.json must remain template_only")
    errors.extend(check_benefits_taxonomy())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Appraisal QA passed for Stage 5A controls; Stage 5 gate remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

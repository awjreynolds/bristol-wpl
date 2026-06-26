#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "analysis/spatial/stage-4a-boundary-and-parking-inventory-control-package.md",
    "analysis/spatial/spatial-options-report.md",
    "analysis/spatial/cross-boundary-and-displacement.md",
    "analysis/data-protection-and-cyber/stage-4a-dpia-and-lawful-basis-scope.md",
    "analysis/operations-and-enforcement/stage-4a-inventory-declaration-inspection-linkage.md",
    "spatial/parking_inventory/parking-base-methodology.md",
    "spatial/parking_inventory/parking-inventory-data-contract.md",
    "spatial/parking_inventory/parking-base-register.xlsx",
    "spatial/spatial_qa/topology-qa-rules.md",
    "spatial/spatial_qa/spatial-assurance-report.md",
    "statutory_dossier/boundary_schedule/boundary_schedule.md",
]

CSV_HEADERS = {
    "spatial/boundary_options/boundary-build-manifest.csv": [
        "boundary_option_id",
        "input_layer_name",
        "input_source_id",
        "input_sha256",
        "working_crs",
        "topology_checks",
        "output_geopackage",
        "legal_schedule_ref",
        "review_status",
    ],
    "spatial/boundary_options/boundary-option-register.csv": [
        "boundary_option_id",
        "status",
        "geometry_file",
        "crs",
        "source_ids",
        "qa_status",
    ],
    "spatial/boundary_options/boundary-change-log.csv": [
        "change_id",
        "boundary_option_id",
        "version",
        "change_summary",
        "approval_status",
    ],
    "spatial/parking_inventory/canonical/sites.csv": [
        "site_id",
        "boundary_option_id",
        "source_ids",
        "source_hashes",
        "data_classification",
        "confidence",
    ],
    "spatial/parking_inventory/canonical/premises.csv": [
        "premises_id",
        "site_id",
        "premises_reference_type",
        "premises_reference_value",
        "occupier_id",
        "source_ids",
        "data_classification",
    ],
    "spatial/parking_inventory/canonical/occupiers.csv": [
        "occupier_id",
        "organisation_name",
        "source_ids",
        "data_classification",
    ],
    "spatial/parking_inventory/canonical/parking_areas.csv": [
        "parking_area_id",
        "premises_id",
        "geometry_ref",
        "source_ids",
        "count_confidence",
        "data_classification",
    ],
    "spatial/parking_inventory/canonical/parking_observations.csv": [
        "observation_id",
        "parking_area_id",
        "count_method",
        "total_places",
        "workplace_parking_places",
        "uncertainty_low",
        "uncertainty_high",
        "source_ids",
        "lawful_basis_ref",
        "data_classification",
    ],
    "spatial/parking_inventory/canonical/licence_declarations.csv": [
        "declaration_id",
        "premises_id",
        "licence_year",
        "declared_places",
        "source_ids",
        "data_classification",
    ],
    "spatial/parking_inventory/canonical/inspections.csv": [
        "inspection_id",
        "premises_id",
        "inspection_date",
        "legal_power_or_authority_ref",
        "personal_data_flag",
    ],
    "spatial/parking_inventory/canonical/exemptions_discounts.csv": [
        "exemption_discount_id",
        "premises_id",
        "category",
        "legal_or_policy_basis",
        "evidence_refs",
    ],
    "spatial/parking_inventory/canonical/appeals_enforcement_links.csv": [
        "link_id",
        "premises_id",
        "enforcement_event_ref",
        "appeal_ref",
        "data_classification",
        "retention_rule",
    ],
    "spatial/parking_inventory/canonical/audit_events.csv": [
        "audit_event_id",
        "record_table",
        "record_id",
        "event_type",
        "event_date",
    ],
}

REQUIRED_PHRASES = {
    "analysis/spatial/stage-4a-boundary-and-parking-inventory-control-package.md": [
        "does not select a scheme boundary",
        "does not create an operating procedure",
        "Stage 4 remains blocked",
    ],
    "spatial/spatial_qa/spatial-assurance-report.md": [
        "Stage 4 remains no-go",
        "does not certify a boundary",
    ],
    "statutory_dossier/boundary_schedule/boundary_schedule.md": [
        "not a legal boundary schedule",
        "Stage 4 remains blocked",
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


def main() -> int:
    errors = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required Stage 4A spatial control file: {rel}")
    for rel, required_columns in CSV_HEADERS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required Stage 4A CSV: {rel}")
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
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Spatial QA passed for Stage 4A controls; Stage 4 gate remains blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Stage 4A Spatial and Parking Data Controls

Status: completed as control architecture. Stage 4 no-go remains.  
Latest relevant commit: `def3f0c`.

## Purpose

Stage 4A created the control architecture for boundary, parking inventory, DPIA and operations-linkage work without inventing a boundary, parking records or spatial outputs.

## Key Data Points

- No boundary GeoPackage or GeoJSON was created.
- No map output was created.
- No parking inventory rows were created.
- `spatial/parking_inventory/parking-base-register.xlsx` is an officer-editable view generated from header-only canonical CSVs.
- `make spatial-qa` checks required files, CSV headers, row widths and no-go wording.

## Main Artefacts

- `analysis/spatial/stage-4a-boundary-and-parking-inventory-control-package.md`
- `spatial/boundary_options/boundary-build-manifest.csv`
- `spatial/boundary_options/boundary-option-register.csv`
- `spatial/boundary_options/boundary-change-log.csv`
- `spatial/parking_inventory/parking-inventory-data-contract.md`
- `spatial/parking_inventory/canonical/*.csv`
- `analysis/data-protection-and-cyber/stage-4a-dpia-and-lawful-basis-scope.md`
- `analysis/operations-and-enforcement/stage-4a-inventory-declaration-inspection-linkage.md`
- `review/stage_gate_reports/stage-4a-boundary-parking-control-report.md`

## Key Findings

- Stage 4A defines source provenance, licence, hash, CRS, topology, output hash and legal/GIS reconciliation requirements.
- Canonical parking data must be versioned CSV/Parquet/GeoPackage; XLSX is only an officer view.
- DPIA, lawful basis, privacy notices, sharing controls, retention and public-release rules are required before live data collection or publication.
- Inventory records must link to future licensing, declaration, inspection, enforcement, appeal and audit records.

## What Stage 4A Did Not Claim

- It did not select a boundary.
- It did not create an authoritative scheme area.
- It did not estimate chargeable spaces.
- It did not estimate revenue.
- It did not evidence displacement.
- It did not authorise data collection or enforcement readiness.

## Continuing Issues

- `ISS-0003` and `RISK-0004` remain open/P0.
- `EG-0014` remains open for authoritative boundary inputs and spatial licences.
- `EG-0016` is partially closed only; the full DPIA/lawful-basis pack is not complete.
- `EG-0023` remains open for operating procedure, PCN templates and appeals/recovery controls.


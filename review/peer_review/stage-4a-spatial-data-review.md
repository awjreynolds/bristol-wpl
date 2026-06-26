# Stage 4A Spatial and Parking Inventory Review

Status: simulation peer review.  
Date: 2026-06-26.  
Scope: Stage 4A boundary, spatial data, parking-inventory, DPIA and operations-linkage controls.

This review records simulated agent due diligence only. It is not GIS certification, legal advice, data-protection advice, operational readiness approval or approval by Bristol City Council.

## Review Criteria

The Stage 4A package was reviewed against these criteria:

- no scheme boundary is selected or implied;
- no parking inventory records, parking counts or revenue estimates are invented;
- boundary source provenance, licences and hashes are required;
- legal boundary wording, GIS geometry and maps must reconcile;
- topology QA rules cover common spatial failure modes;
- canonical parking data is separated from officer XLSX views;
- UPRN, premises, occupier, associated-organisation and parking-area records are normalised;
- DPIA, lawful-basis, data-classification and restricted-data controls remain visible;
- inventory records can link to future licensing, inspection, enforcement and appeal workflows;
- Stage 4 remains no-go.

## Spatial/GIS Review Findings

The Spatial/GIS Boundary Review Agent found that Stage 4A should be a control package, not a boundary decision. It recommended:

- a boundary and parking-inventory control package;
- spatial options and cross-boundary/displacement control placeholders;
- boundary manifest, change log and option register templates;
- topology QA rules;
- parking-base methodology and data-contract files;
- header-only canonical inventory CSVs;
- a boundary schedule no-go update.

Finding: the package creates the required control surfaces without creating false spatial evidence.

Limitation: no authoritative boundary input package, licences, GeoPackage, GeoJSON, map outputs, topology run or legal/GIS reconciliation exists.

## Data Protection and Operations Red-Team Findings

The Data Protection and Operations Red-Team Agent identified the main failure modes:

| Failure mode | Stage 4A control |
|---|---|
| Invented parking-base rows or synthetic examples drift into real evidence | Header-only canonical files and no live records. |
| Officer XLSX becomes uncontrolled source of truth | Canonical CSV/Parquet/GeoPackage rule; XLSX is an officer view only. |
| DPIA and lawful basis treated as optional | Separate Stage 4A DPIA/lawful-basis scope and no data-collection authority. |
| UPRN, premises, occupier and associated organisation flattened | Normalised canonical table structure. |
| Legal parking-place taxonomy missing from data fields | Methodology and data contract require legal category mapping. |
| Inspections, declarations and appeals designed after inventory | Operations linkage note and appeals/enforcement link table. |
| Spatial joins cannot be reproduced | Boundary build manifest, source hash, CRS and topology controls. |
| Sensitive data leaks into normal repo | Data-classification and restricted-path control. |
| Stage 4A implies operational readiness | Explicit no-go wording across control files. |

Finding: the package addresses the highest-risk failure modes for a control stage.

Limitation: no DPO, real legal, Monitoring Officer, GIS certifier, Bristol officer, operational or professional sign-off exists.

## Simulation Sign-Off

Decision: simulation sign-off with conditions.

Conditions:

- run `make spatial-qa` as part of validation;
- do not create dummy GeoPackage, GeoJSON, map or inventory rows;
- keep `ISS-0003`, `RISK-0004`, `EG-0014`, `EG-0016` and `EG-0023` visible;
- do not rely on Stage 4A for OBC/FBC, consultation, revenue, enforcement or statutory submission readiness.


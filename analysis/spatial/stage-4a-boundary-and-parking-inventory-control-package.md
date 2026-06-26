# Stage 4A Boundary and Parking Inventory Control Package

Status: simulation control package.  
Date: 2026-06-26.  
Owner: Spatial/Data Agent.  
Review status: simulation reviewed with conditions.

This package is not a boundary decision, parking-base estimate, revenue estimate, consultation-ready output or officer approval. It is not legal advice, data-protection advice, GIS certification, Bristol City Council approval or professional sign-off.

## Control Position

Stage 4A defines the control framework for boundary and parking-inventory evidence. It does not select a scheme boundary, confirm a legal scheme area, estimate chargeable parking spaces, evidence revenue, or resolve joint-scheme requirements. All boundary options remain spatial/data hypotheses pending authoritative GIS evidence, legal reconciliation, parking-base evidence and simulation review.

Stage 4 remains blocked by:

- `ISS-0003` and `RISK-0004`: authoritative WPL boundary and workplace parking inventory absent;
- `EG-0014`: authoritative boundary input package and spatial licences not acquired;
- `EG-0016`: DPIA scope and lawful basis not defined;
- `EG-0023`: licensing and enforcement operating procedure not populated.

## Evidence Basis

This package relies on the operating model and existing technical-baseline notes only. It does not add new boundary or parking evidence.

| Control source | Relevance |
|---|---|
| `instructions/00-operating-model.md` Stage 4 and section 12 | Spatial option, boundary, inventory, cross-boundary and displacement requirements. |
| `analysis/legal/scheme-area-and-joint-schemes.md` | Boundary options may be scoped only as spatial/data hypotheses. |
| `analysis/legal/workplace-parking-place-definition.md` | Parking taxonomy must be translated into survey and inventory fields. |
| `analysis/legal/data-protection-and-information-law.md` | No DPIA, privacy notice, data-sharing agreement or live data source exists. |
| `analysis/legal/licensing-inspection-enforcement-and-appeals.md` | Inventory evidence must link to licensing, inspection, PCN, representations, appeals and recovery controls. |
| `analysis/legal/post-stage-2-legal-governance-context-packet.md` | Stage 2 controls do not unblock spatial, consultation, OBC/FBC or statutory submission readiness. |

## Required Boundary Artefacts

The following artefacts are required before the Stage 4 gate can pass:

| Artefact | Required path | Stage 4A status |
|---|---|---|
| Spatial options report | `analysis/spatial/spatial-options-report.md` | Control placeholder only |
| Boundary build manifest | `spatial/boundary_options/boundary-build-manifest.csv` | Header template only |
| Boundary option register | `spatial/boundary_options/boundary-option-register.csv` | Header template only |
| Boundary change log | `spatial/boundary_options/boundary-change-log.csv` | Header template only |
| Boundary GeoPackage | `spatial/boundary_options/boundary-options.gpkg` | Not created; would imply data |
| Boundary GeoJSON | `spatial/boundary_options/boundary-options.geojson` | Not created; would imply data |
| Regenerable SVG/PNG maps | `spatial/boundary_options/maps/` | Not created; requires source geometry |
| Topology QA rules | `spatial/spatial_qa/topology-qa-rules.md` | Control created |
| Spatial assurance report | `spatial/spatial_qa/spatial-assurance-report.md` | No-go control created |
| Boundary schedule | `statutory_dossier/boundary_schedule/boundary_schedule.md` | Control wording only |

Do not create dummy GeoPackage, GeoJSON, SVG or PNG outputs. Empty or synthetic spatial files risk being mistaken for candidate boundaries.

## Boundary Data Standard

Every future boundary option must include:

- scheme-area polygon;
- human-readable boundary schedule;
- authoritative editable or regenerable map;
- parcel, premises and boundary-crossing rules;
- treatment of roads, railways, waterways, islands, exclaves and boundary-centred premises;
- British National Grid working CRS, normally `EPSG:27700`;
- WGS84 export only where needed for web mapping;
- source IDs, licences, retrieval dates and hashes;
- build manifest with transformations, tolerances, geometry precision and spatial joins;
- topology QA result;
- legal/GIS reconciliation certificate;
- change log and version.

No static image can be the sole legal boundary record.

## Boundary Source Acquisition Requirements

Before any boundary option can be treated as evidence, the programme must log:

- official Bristol administrative boundary source and licence;
- relevant address, UPRN, LLPG or equivalent premises source and licence;
- parcel, road centreline or property-boundary layer where legally and contractually available;
- public transport, displacement, accessibility and cross-boundary context layers;
- source hashes and retrieval dates;
- data-classification and publication constraints;
- evidence gap for any required layer unavailable to the simulation.

Restricted or licensed datasets must not be committed to normal repo paths unless the licence and data-classification rules allow it.

## Parking Inventory Control

The parking inventory must be normalised before any real records are loaded. Stage 4A creates header-only canonical tables under `spatial/parking_inventory/canonical/`:

- `sites.csv`
- `premises.csv`
- `occupiers.csv`
- `parking_areas.csv`
- `parking_observations.csv`
- `licence_declarations.csv`
- `inspections.csv`
- `exemptions_discounts.csv`
- `appeals_enforcement_links.csv`
- `audit_events.csv`

Every future record must include, as applicable:

- stable ID;
- UPRN, LLPG, VOA, planning or manual reference;
- source IDs and source hashes;
- valid-from and valid-to dates;
- spatial join method or geometry reference;
- confidence score;
- lawful-basis reference;
- data classification;
- owner and reviewer;
- audit history.

`spatial/parking_inventory/parking-base-register.xlsx` is an officer-editable view only. Canonical data is the versioned CSV/Parquet/GeoPackage data validated against schema and QA rules.

## DPIA and Lawful-Basis Control

Stage 4A does not authorise data collection. Before employer surveys, inspections, declarations, enforcement records or publication outputs are used, the programme must create:

- DPIA scope and full DPIA;
- records of processing activity inputs;
- lawful-basis and statutory-gateway analysis;
- data-flow map;
- privacy notices;
- sharing and processor controls;
- retention and redaction rules;
- human-review route for eligibility, inspection and enforcement decisions;
- public-release manifest.

Employer, occupier, vehicle, contact, inspection, appeal and enforcement data may involve personal or commercially sensitive data and must not be stored in normal repo paths unless explicitly classified for that use.

## Inventory to Enforcement Linkage

The inventory must be capable of supporting:

- licence application and renewal;
- declaration evidence;
- inspection and right-of-entry evidence;
- exemptions and discounts;
- PCN evidence standard;
- representations and notice decisions;
- appeal and county-court process tracking;
- charge certificate and recovery controls;
- cancellation, fresh PCN and audit logging.

Stage 4A does not create an operating procedure, PCN template, service policy or appeals workflow.

## Cross-Boundary and Displacement Control

Any future spatial options report must examine:

- South Gloucestershire;
- North Somerset;
- Bath and North East Somerset;
- major employment and commuter corridors;
- boundary parking and residential spillover;
- relocation of parking or workplaces;
- park-and-ride effects;
- remote and hybrid work response;
- public transport capacity outside Bristol;
- distribution of charges and benefits across residents and non-residents.

No displacement or cross-boundary conclusion is available at Stage 4A.

## No-Overclaim Rules

Future agents must not claim:

- a boundary has been selected;
- Bristol-only legal area is confirmed;
- a joint-scheme requirement is resolved;
- chargeable spaces are estimated;
- revenue is evidenced;
- displacement or equality effects are assessed;
- employer inventory exists;
- parking records are reliable;
- DPIA or lawful basis is complete;
- enforcement is operationally ready;
- OBC/FBC or consultation can rely on Stage 4A as spatial evidence.

## Stage 4A Acceptance Criteria

Stage 4A can be treated as complete for control purposes only when:

- required control files exist;
- boundary manifest and canonical inventory CSVs have validated headers;
- the parking inventory data contract distinguishes canonical data from officer XLSX views;
- topology QA rules are documented;
- DPIA/lawful-basis and enforcement linkage gaps are visible;
- `spatial-qa` passes as a control check;
- simulation sign-offs record that Stage 4 remains blocked.


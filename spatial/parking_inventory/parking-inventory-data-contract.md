# Parking Inventory Data Contract

Status: Stage 4A canonical data contract.  
Date: 2026-06-26.  
Owner: Spatial/Data Agent.

This contract defines future canonical records. It does not contain live parking data.

## Canonical Tables

| Table | Purpose | Primary key |
|---|---|---|
| `sites.csv` | Site-level grouping for one or more premises and parking areas. | `site_id` |
| `premises.csv` | Premises records linked to references, occupiers and sites. | `premises_id` |
| `occupiers.csv` | Organisation records where lawful and evidenced. | `occupier_id` |
| `parking_areas.csv` | Spatially referenced parking areas. | `parking_area_id` |
| `parking_observations.csv` | Counts, declarations or evidence observations with uncertainty. | `observation_id` |
| `licence_declarations.csv` | Future licence-year declarations. | `declaration_id` |
| `inspections.csv` | Future inspection records and outcomes. | `inspection_id` |
| `exemptions_discounts.csv` | Exemption and discount evidence. | `exemption_discount_id` |
| `appeals_enforcement_links.csv` | Links to enforcement and appeal records. | `link_id` |
| `audit_events.csv` | Change history for canonical records. | `audit_event_id` |

## Mandatory Controls

Future records must include:

- stable ID;
- source IDs;
- source hashes where available;
- valid-from and valid-to dates where relevant;
- boundary option ID or geometry reference where relevant;
- lawful-basis reference where relevant;
- data classification;
- confidence;
- owner and reviewer;
- audit event.

## Officer Workbook Rule

`parking-base-register.xlsx` is an officer-editable view. It is not the canonical source of truth. Any officer edits must be reconciled into the canonical CSV/Parquet/GeoPackage data and validated before use in modelling, appraisal, consultation or statutory documents.

## Repository Control

No personal, restricted, commercially sensitive, enforcement or appeal-level data may be stored in normal repo paths unless a public-release or data-classification manifest authorises it.


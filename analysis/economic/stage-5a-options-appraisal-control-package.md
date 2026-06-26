# Stage 5A Options and Appraisal Control Package

Status: simulation control package.  
Date: 2026-06-26.  
Owner: Appraisal Guidance Agent.  
Review status: pending Stage 5A simulation review.

This package is not an Option Assessment Report, Appraisal Specification Report, Appraisal Specification Summary Table, model output, value-for-money statement, shortlist decision, preferred-way-forward recommendation or professional appraisal sign-off.

## Control Position

Stage 5A defines the control framework for options development, OAR, ASR, ASST, model assurance, uncertainty and reappraisal triggers. It does not shortlist options, select a preferred option, estimate benefits or costs, calculate a BCR, produce a value-for-money category, or authorise OBC/FBC assembly.

Stage 5 remains blocked by:

- `ISS-0004`: no ASR/OAR/ASST model cards, uncertainty log or appraisal outputs exist;
- `RISK-0005`: OBC drafting begins before SOC-equivalent OAR, ASR and ASST controls;
- `RISK-0010`: guidance landing pages must not be treated as full TAG source packs;
- `EG-0012`: current guidance snapshots and source notes remain incomplete;
- `EG-0013`: reappraisal triggers were not previously defined;
- Stage 4 P0: no authoritative boundary or parking inventory exists.

## Evidence Basis

| Control source | Relevance |
|---|---|
| `instructions/00-operating-model.md` Stage 5 and section 13 | Options framework, ASR, model-card, run-manifest and uncertainty controls. |
| `review/analytical_assurance/stage-1-appraisal-tag-assurance-review.md` | Appraisal spine exists but ASR, OAR, ASST, model cards and outputs are absent. |
| `analysis/legal/stage-2j-dft-procedural-expectations-and-engagement-classification.md` | Generic DfT/TAG alignment does not close WPL-specific DfT process. |
| `analysis/spatial/stage-4a-boundary-and-parking-inventory-control-package.md` | Spatial/data blockers prevent real modelling, revenue and appraisal outputs. |
| `business_case/shared/assembly_manifest.md` | OBC/FBC assembly remains blocked until legal, spatial/data and ASR controls exist. |

## Required Stage 5A Artefacts

| Artefact | Required path | Stage 5A status |
|---|---|---|
| Stage 5A control package | `analysis/economic/stage-5a-options-appraisal-control-package.md` | Control created |
| Longlist control | `analysis/economic/options-longlist.md` | Option families only |
| Options framework filter | `analysis/economic/options-framework-filter.csv` and `.xlsx` | Header/control rows only |
| Option Assessment Report | `analysis/economic/option-assessment-report.md` | Placeholder/no-go |
| Shortlisting report | `analysis/economic/shortlisting-report.md` | Placeholder/no shortlist |
| Appraisal Specification Report | `analysis/economic/appraisal-specification-report.md` | Placeholder/no agreed ASR |
| ASST | `analysis/economic/appraisal-specification-summary-tables.csv` and `.xlsx` | Scope rows only |
| ASR change log | `analysis/economic/asr-change-log.csv` | Header/control only |
| Reappraisal trigger table | `analysis/economic/reappraisal-trigger-table.csv` | Trigger controls |
| Benefits treatment taxonomy | `analysis/economic/benefits-treatment-taxonomy.csv` | Control rows only |
| Comparator transferability matrix | `analysis/economic/nottingham-transferability-matrix.csv` | Control rows only |
| Boundary/model dependency table | `analysis/economic/boundary-parking-model-dependency-table.csv` | Control rows only |
| Appraisal reviewer matrix | `analysis/economic/appraisal-reviewer-matrix.csv` | Control rows only |
| Guidance source requirements | `analysis/economic/guidance-source-requirements.csv` | Control rows only |
| Model card template | `models/model_cards/model-card-template.md` | Control template |
| Model-specific cards | `models/model_cards/*-model-card.md` | Not-started stubs |
| Model run manifest template | `models/outputs/model-run-manifest-template.json` | Control template |
| Model run manifest register | `models/outputs/model-run-manifest-register.csv` | Header/control only |
| Uncertainty register | `models/uncertainty/uncertainty-register.csv` | Header/control only |
| Uncertainty log workbook | `models/uncertainty/uncertainty-log.xlsx` | Officer view generated from controlled CSV |
| Model validation plan | `models/validation/model-validation-plan.md` | Control created |
| Parking-base model specification | `models/parking-base/parking-base-model-specification.md` | Blocked by Stage 4 |
| Transport model specification | `models/transport/transport-model-specification.md` | No model outputs |
| Revenue model specification | `models/revenue/revenue-model-specification.md` | No revenue outputs |

## Options Control

Future option development must start from dimensions, not a pre-selected WPL scheme. Required dimensions include:

- intervention type;
- geography;
- charge basis;
- charge level;
- indexation;
- threshold;
- exemptions and discounts;
- commencement and phasing;
- operating model;
- enforcement intensity;
- revenue package;
- sequencing with transport improvements;
- governance;
- joint or single-authority delivery.

The longlist must include credible alternatives to WPL and combined packages. The purpose is to show fair, structured selection, not to create pseudo-precision.

## Appraisal Control

Before any substantive modelling, the programme must produce a current-guidance ASR that states:

- decision context;
- objectives and critical success factors;
- options and option families;
- geographic and temporal scope;
- reference case;
- modelling approach;
- appraisal period;
- impacts to monetise;
- impacts to assess qualitatively;
- distributional and place-based approach;
- data requirements;
- uncertainty treatment;
- proportionality rationale;
- validation and QA;
- outputs and limitations;
- resources and review route.

The ASST must record, for each material impact:

- method;
- proportionality rationale;
- data;
- required model output;
- monetisation status;
- uncertainty;
- value-for-money treatment;
- statutory or environmental consultee input;
- reviewer;
- reason if no further assessment is proposed.

The ASST must include, at minimum, transport users, employer/employee incidence, parking demand, mode shift, trip retiming, relocation/displacement, public transport capacity, environmental impacts, distributional/place impacts, equality/social acceptability, revenue/accounting transfers, real resource costs, operating/enforcement costs, non-monetised impacts and statutory/environmental consultee dependencies.

## Model Assurance Control

Every future model must have a model card. Every model run must have a run manifest recording:

- model ID and run ID;
- Git commit;
- dependency or tool version evidence;
- input hashes;
- parameters and scenario name;
- random seed if applicable;
- output hashes;
- validation results;
- reviewer status.

Officer-editable XLSX model outputs must be generated from controlled inputs or reconciled back into controlled inputs. Hidden hard-coding and formula integrity must be tested.

## Current-Guidance Control

Stage 5A does not establish full Green Book, TAG or value-for-money compliance. Before any decision-grade appraisal, the programme must snapshot and cite the current Green Book, DfT business-case guidance, relevant individual TAG units, TAG databook, uncertainty toolkit and value-for-money framework with version and retrieval dates. Landing pages are control sources only unless the selected appraisal scope has the individual guidance units needed for the method.

## Comparator Transferability Control

Nottingham evidence may be used only after a transferability assessment. No charge level, elasticity, behaviour, congestion effect, parking-base assumption, employer response, mode-shift assumption or enforcement assumption may be imported into Bristol automatically.

## Benefits Treatment Control

Gross levy receipts must not be treated as economic benefits. Future appraisal must distinguish:

- welfare/social benefits;
- real resource costs;
- transfer payments;
- public cash flow;
- net proceeds;
- private compliance burdens;
- employer and employee incidence;
- operating and enforcement costs;
- distributional impacts.

## No-Overclaim Rules

Future agents must not claim:

- a shortlist has been agreed;
- a preferred option exists;
- WPL is preferred to alternatives;
- the ASR is agreed;
- ASST impacts are assessed;
- BCR, NPV or value-for-money category exists;
- gross levy receipts are economic benefits;
- Nottingham impacts or elasticities transfer to Bristol automatically;
- WPL-only effects include transport-investment benefits;
- transport-investment-only effects are caused by the charge;
- combined-package effects are understood without separate WPL-only and investment-only analysis;
- boundary, parking-base, revenue, transport or behavioural model outputs exist;
- consultation or OBC/FBC can rely on Stage 5A as appraisal evidence.

## Required Separation of Effects

Every future appraisal must separate:

1. WPL-only effects;
2. transport-investment-only effects;
3. combined-package effects.

This separation is required before any value-for-money or strategic recommendation is made.

## Stage 5A Acceptance Criteria

Stage 5A can be treated as complete for control purposes only when:

- required control files exist;
- `appraisal-qa` passes;
- options framework, ASST, ASR change log, reappraisal triggers and uncertainty register have valid headers;
- model-card and run-manifest templates exist;
- the package states no shortlist, no preferred option, no VFM and no model-output status;
- simulation sign-off records that Stage 5 remains blocked.

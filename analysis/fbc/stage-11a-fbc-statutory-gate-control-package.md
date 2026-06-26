# Stage 11A FBC And Statutory Gate Control Package

Status: simulation control package.
Date: 2026-06-26.
Owner: Integrated Case Review Agent.

This package creates final FBC/statutory assurance gate controls. It does not approve an FBC, assemble an FBC, approve a scheme order, authorise submission, authorise implementation or create a real-world professional sign-off.

## Control Position

Stage 11 FBC/statutory gate remains blocked. There is no recommendation to submit or implement while open legal, WECA/MCA, DfT, boundary, consultation, FBC, finance, commercial, data, operations, appraisal, equality and residual-risk blockers remain.

## Required Stage 11A Controls

| Control | Path | Status |
|---|---|---|
| Gate checklist | `business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv` | Blocked control rows |
| Assurance panel | `business_case/fbc/controls/stage-11-assurance-panel-register.csv` | Blocked control rows |
| No-go claims | `business_case/fbc/controls/stage-11-no-go-claim-register.csv` | Blocked control rows |
| Decision-report control | `business_case/fbc/controls/stage-11-decision-report-control.md` | Control note |
| Red-team packet | `business_case/fbc/controls/stage-11-red-team-packet.md` | Control note |
| Validator | `scripts/validate_fbc_statutory_gate.py` | Control created |

## Gate Rule

No Stage 11 recommendation may be made until:

- scheme order and boundary have legal sign-off;
- consultation is lawful, conscientiously addressed and reconsultation risk is assessed;
- current statutory confirmation requirements are satisfied;
- Section 151 affordability review is complete;
- procurement and commercial route is lawful and credible;
- data protection and cyber controls are ready;
- operations and enforcement are service-ready;
- charge-base and revenue models are independently reviewed;
- investment programme is deliverable;
- equality mitigations are funded and owned;
- DfT engagement issues are closed or explicitly accepted as submission risks;
- WECA/MCA dependencies are agreed;
- no P0 findings remain and residual risks are visible to decision-makers.

## What Stage 11A Does Not Do

- It does not assemble or approve an FBC.
- It does not create an officer decision report.
- It does not certify a scheme order or statutory dossier.
- It does not approve procurement, consultation, submission or implementation.
- It does not create authored PDF outputs.

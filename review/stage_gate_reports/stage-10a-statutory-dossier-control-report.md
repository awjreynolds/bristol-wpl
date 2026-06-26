# Stage 10A Statutory Dossier Control Report

Status: simulation gate report.
Date: 2026-06-26.

## Gate Question

Does the repo now control the anticipated statutory confirmation dossier components without implying submission readiness?

## Decision

Accepted for simulation control purposes only.

Stage 10A creates statutory dossier controls. It does not create a statutory submission, certified scheme order, DfT-accepted dossier, Secretary of State confirmation request, completed consultation statement, FBC or implementation-ready legal pack. Stage 10 statutory submission remains blocked; in this repo that means the future statutory dossier/submission, not the Stage 10A control slice. The combined Stage 11 FBC/statutory gate also remains blocked.

## Evidence Reviewed

- `analysis/legal/stage-10a-statutory-confirmation-dossier-control-package.md`
- `statutory_dossier/controls/dossier-component-register.csv`
- `statutory_dossier/controls/dossier-readiness-gate.csv`
- `statutory_dossier/controls/submission-no-go-register.csv`
- `statutory_dossier/controls/statutory-route-memorandum-control.md`
- `statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv`
- `scripts/validate_statutory_dossier.py`
- `tests/test_statutory_dossier.py`
- `review/peer_review/stage-10a-statutory-dossier-review.md`

## Findings

| Criterion | Result |
|---|---|
| 23 anticipated dossier components controlled | Met for control purposes |
| Submission no-go claims recorded | Met |
| Clause-by-clause powers matrix created | Met as blocked control |
| DfT checklist caveat preserved | Met |
| FBC no-go claim enforced by validator | Met |
| Required component-register document paths resolve | Met |
| Component 22 post-confirmation certified-order control recorded | Met |
| Statutory gate failure wording separated from OBC assembly wording | Met |
| Statutory submission gate passes | Not met; deliberately blocked |

## Review Disposition

| Review issue | Disposition |
|---|---|
| Officer dashboard understated hard no-go OBC and consultation gates. | Fixed by marking both as `RED`. |
| README omitted blocked Stage 8 consultation-launch gate. | Fixed in the root Mermaid map and explanatory text. |
| Stage 10A/Stage 10/Stage 11 terminology could confuse non-specialists. | Fixed with terminology notes in stage docs and gate plan. |
| Statutory gate relied on OBC readiness blocker wording. | Fixed with statutory-specific blocker collection and error messages. |
| Gate did not check Stage 10A readiness/no-go rows or EG-0034. | Fixed by checking dossier gate rows, no-go rows, evidence gap, approval limitation and sign-off limitation. |
| Component 22 missed post-confirmation certified-order control. | Fixed in the component register and covered by test. |
| Three required-document links did not resolve. | Fixed with blocked control placeholders under `statutory_dossier/assembled/`. |

## Continuing Blockers

The gate remains blocked by open P0/P1 items including Bristol route, WECA/MCA role, DfT process, boundary and inventory, consultation readiness, FBC absence, finance/net-proceeds plans, operations readiness and statutory route memorandum evidence.

## Simulation Sign-Off

Simulation Gate Authority: sign-off with conditions for Stage 10A control architecture only.

This sign-off has no real-world legal, statutory, financial, governance, officer, analytical assurance, consultation, DfT, WECA/MCA or professional effect.

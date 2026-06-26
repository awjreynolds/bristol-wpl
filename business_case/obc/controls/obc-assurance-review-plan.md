# OBC Assurance Review Plan

Status: Stage 6A control plan.  
Date: 2026-06-26.

This plan defines simulation review gates for a future OBC. It does not approve or assemble an OBC.

Stage 7A now records the future OBC gate checklist and assurance panel controls in:

- `business_case/obc/controls/stage-7-obc-gate-checklist.csv`
- `business_case/obc/controls/stage-7-assurance-panel-register.csv`
- `business_case/obc/controls/stage-7-decision-report-control.md`
- `business_case/obc/controls/stage-7-red-team-packet.md`

## Sequential Reviews

1. Author self-check against the section dependency matrix.
2. Evidence and claim check against `business_case/obc/controls/section-claim-dependency-register.csv` and `evidence/claim_evidence_matrix.csv`.
3. Legal review against Stage 2L controls and the legal compliance matrix.
4. Bristol governance and decision-route review.
5. WECA/MCA role and package funding assurance review.
6. Spatial and parking-base review.
7. Transport modelling and analytical assurance review.
8. Economic appraisal and value-for-money review.
9. Financial affordability and net-proceeds review.
10. Commercial and operational readiness review.
11. Equality, health, environment, data protection and accessibility review.
12. Integrated Five Case review.
13. Independent red-team review.
14. Editorial and officer-editability review.
15. Stage gate report by the Simulation Gate Authority.

## Review Rule

Any open P0 prevents a proceed recommendation. P1 findings require an action plan, owner, due date and residual-risk decision before any conditional recommendation.

## Evidence Rule

Every material claim must have a source ID, model run, dataset reference, register row or explicit assumption ID. Summary sections may compress only reviewed claims and must not introduce new evidence.

# Stage 11A FBC And Statutory Gate Report

Status: simulation gate report.
Date: 2026-06-26.

## Gate Question

Does the repo now control the final FBC/statutory assurance gate without implying FBC approval, statutory submission or implementation readiness?

## Decision

Accepted for simulation control purposes only.

Stage 11A creates FBC/statutory gate controls. It does not approve an FBC, approve a scheme order, authorise statutory submission, authorise procurement or recommend implementation. Stage 11 FBC/statutory gate remains blocked.

## Evidence Reviewed

- `analysis/fbc/stage-11a-fbc-statutory-gate-control-package.md`
- `business_case/fbc/controls/stage-11-fbc-statutory-gate-checklist.csv`
- `business_case/fbc/controls/stage-11-assurance-panel-register.csv`
- `business_case/fbc/controls/stage-11-no-go-claim-register.csv`
- `business_case/fbc/controls/stage-11-decision-report-control.md`
- `business_case/fbc/controls/stage-11-red-team-packet.md`
- `scripts/validate_fbc_statutory_gate.py`
- `tests/test_fbc_statutory_gate.py`
- `review/peer_review/stage-11a-fbc-statutory-assurance-review.md`
- `docs/officer/programme-risk-briefing.md`
- `docs/officer/checks-and-balances-map.md`
- `docs/stages/README.md`
- `docs/visuals/stage-gate-map.mmd`

## Findings

| Criterion | Result |
|---|---|
| Master-prompt Stage 11 conditions controlled | Met for control purposes |
| Section 151 and Monitoring Officer replacements visible | Met |
| Submit and implement recommendation blocked | Met |
| FBC approval no-go claim recorded | Met |
| Every checklist reviewer appears in the assurance panel | Met |
| Open-like final-gate statuses are treated as active blockers | Met |
| Officer-facing Stage 10A/11A stop signs are visible | Met |
| Statutory submission gate passes | Not met; deliberately blocked |
| FBC/statutory gate passes | Not met; deliberately blocked |

## Review Disposition

Two simulated reviewers challenged Stage 11A before sign-off. The legal/finance/statutory reviewer raised P1 issues on reviewer coverage, no-go claim coverage and active-blocker logic. The officer/readability reviewer raised P2/P3 issues on whether a non-specialist reader could see the final gate risks. Those findings are closed in the Stage 11A controls and remain subject to the deliberately blocked Stage 11 gate.

## Continuing Blockers

The gate remains blocked by open P0/P1 items including Bristol route, WECA/MCA role, DfT process, boundary and inventory, consultation readiness, FBC absence, Section 151 affordability, finance/net-proceeds plans, procurement/commercial route, data protection, operations readiness, charge-base and revenue models, equality mitigation ownership and statutory route evidence.

## Simulation Sign-Off

Simulation Gate Authority: sign-off with conditions for Stage 11A control architecture only.

This sign-off has no real-world legal, statutory, financial, governance, officer, analytical assurance, consultation, DfT, WECA/MCA or professional effect.

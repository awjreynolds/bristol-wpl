# Stage 18A Peer Review: Nottingham Displacement And Transferability

Status: simulated multi-agent review synthesis.  
Date: 2026-06-26.

## Review Roles

| Role | Focus | Outcome |
|---|---|---|
| Comparator Evidence Agent | Nottingham, TfL and Leicester transferability limits | Required no-transfer wording for charge, revenue, congestion, mode shift, employer behaviour, public acceptability and source hierarchy. |
| Spatial Data Agent | Boundary, residential spillover, inventory and CPZ/RPZ readiness | Required residential baseline, boundary options, CPZ/RPZ option evidence, equality/accessibility checks and monitoring triggers before reliance. |
| Public Officer Review Agent | Cabinet/officer/public readability | Required first-reader wording that lessons are questions, not Bristol forecasts or selected mitigation. |
| Red Team | Fail-closed QA | Required validator checks for NLR-0007 to NLR-0015, current Nottingham gap, failed congestion-source gap and softened cross-register blockers. |

## Findings

1. Nottingham can be a useful precedent only as a question generator. It cannot support Bristol charge, revenue, congestion, mode-shift, employer-behaviour, acceptability or public-transport claims without Bristol evidence.
2. Residential spillover is the most visible public-risk lesson. Bristol needs street-level baseline evidence, boundary options, employer-area parking stress mapping and mitigation option appraisal before any consultation or boundary reliance.
3. CPZ/RPZ controls must be described as possible mitigation options only. They are not selected, costed, consulted, equality-screened, enforceable or ready in this simulation.
4. TfL and Leicester are proposal-stage comparators. They can identify concerns and design questions, not implementation outcomes.
5. Current Nottingham charge, threshold, operating status and latest reporting must be refreshed before publication or business-case reliance.
6. The failed independent congestion source `SRC-ACADEMIC-0001` remains a hard gap linked to `ISS-0005` and `RISK-0009`.

## Changes Required By Review

- Rename the officer briefing framing from key lessons to transferability questions.
- Add explicit public README wording that learning from Nottingham does not mean Bristol would get the same impacts or already has a parking-mitigation plan.
- Change the assurance dashboard Nottingham row to `Not transferable to Bristol yet` with `RED for reliance / AMBER for lessons control`.
- Add `NLR-0011` to `NLR-0015` and `NTM-007` to `NTM-011`.
- Add and validate a displacement control checklist.
- Make `scripts/validate_nottingham_transferability.py` fail if Stage 18A rows disappear, transferability rows are not blocked, `SRC-ACADEMIC-0001` is used without failed-acquisition caveat, CPZ/RPZ readiness is implied, or critical blockers are softened.

## Simulated Sign-Off

The review accepts Stage 18A for comparator-learning control only.

It does not create Bristol evidence, legal advice, officer approval, public-authority approval, OBC/FBC readiness, consultation readiness, statutory readiness, CPZ/RPZ readiness or current Nottingham certification.

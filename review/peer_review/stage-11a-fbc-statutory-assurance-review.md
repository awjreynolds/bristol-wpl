# Stage 11A FBC And Statutory Gate Review

Status: simulated peer review with conditions.
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 11A creates useful FBC/statutory assurance gate controls without implying that an FBC, statutory submission or implementation recommendation is ready.

## Findings

| Finding | Severity | Response |
|---|---|---|
| The master prompt requires a final no-submit/no-implement assurance gate, but the repo only had generic OBC/FBC blocker checks. | P1 | Stage 11A adds an integrated FBC/statutory gate checklist and validator. |
| FBC approval could be confused with statutory submission readiness. | P1 | Stage 11A no-go claims block both FBC approval and submit/implement recommendations. |
| Real-world legal and finance approvals could be hidden behind simulation sign-offs. | P1 | Assurance panel records Section 151, Monitoring Officer and other real-world replacements. |
| Decision-makers need residual risk and downside visibility. | P1 | Gate checklist and decision-report control require residual-risk decision-pack evidence. |
| Final-gate reviewers named in the checklist were not all present in the assurance panel. | P1 | Assurance panel expanded and validator now checks every named checklist reviewer. |
| No-go claims did not cover all final Stage 11 decision conditions. | P1 | No-go register expanded to cover reconsultation, statutory confirmation, data/cyber, investment programme, equality mitigations and open P0 findings. |
| Final-gate blocker logic only recognised one blocked status. | P1 | Validator now treats open-like statuses as active blockers in the Stage 11 gate path. |
| Officer-facing summaries did not surface Stage 10A/11A risks clearly enough. | P2 | Programme risk briefing, stage index, visual map and checks-and-balances map updated. |

## Decision

Simulation sign-off with conditions for Stage 11A controls only.

Stage 11A does not approve an FBC, approve a scheme order, authorise statutory submission, authorise procurement or recommend implementation.

## Conditions

- `scripts/validate_fbc_statutory_gate.py` must pass for control completeness.
- `scripts/validate_fbc_statutory_gate.py --gate` must fail while live blockers remain.
- Stage 11A rows must remain blocked until source-backed evidence and real-world replacement roles exist.
- No authored PDF outputs may be produced.

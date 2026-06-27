# Stage 32A Subagent Packet: Red Team Overclaim Review

## Stage

- Stage ID: Stage 32A.
- Stage purpose: produce a WECA-style simulated OBC working draft while preventing approval/readiness leakage.
- Parent context packet: `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md`.
- Previous gate report: `review/stage_gate_reports/stage-31a-validation-evidence-log-for-stage-30a-report.md`.

## Role

- Agent role: Red Team Overclaim Agent.
- Simulated competence: challenge function for public-law, evidence and assurance overclaim.
- Independence requirement: independent read-only review.
- Read-only or write scope: read-only.
- Review lane: red-team.

## Exact Question

What are the highest-risk ways Stage 32A could mislead readers, hallucinate evidence, or leak blocked OBC/FBC readiness claims, and what controls must be added before commit?

## Allowed Context

| File or source ID | Why it is included |
|---|---|
| `README.md` | Public no-go position. |
| `governance/stage-gate-plan.md` | Gate blockers. |
| `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md` | Stage scope. |
| `analysis/weca-role-and-evidence/stage-2h-package-funding-assurance-trigger-map.md` | WECA/MCA assurance limits. |
| `business_case/obc/controls/no-go-claim-register.csv` | Existing OBC no-go claims. |
| `business_case/shared/assembly_manifest.md` | Assembly limits. |
| `scripts/validate_obc.py` | Existing validator guardrails. |
| `tests/test_obc.py` | Existing OBC tests. |

## Out Of Scope

Do not inspect the whole repo or raw evidence. Do not solve the drafting; identify risk controls and blocked claims.

## Source And Register IDs

| Type | IDs |
|---|---|
| Source IDs | `SRC-WECA-0006`, `SRC-WECA-0007`, `SRC-BCC-0015`, `SRC-BCC-0036`, `SRC-WECA-0027` |
| Issue IDs | `ISS-0001`, `ISS-0002`, `ISS-0003`, `ISS-0004`, `ISS-0011`, `ISS-0041` |
| Risk IDs | `RISK-0001`, `RISK-0002`, `RISK-0004`, `RISK-0005`, `RISK-0044` |
| Evidence-gap IDs | `EG-0005`, `EG-0059` |
| Pitfall IDs | identify new pitfall if needed |

## No-Go Claims

Do not permit official-looking impersonation, real-world approval, consultation readiness, selected boundary, selected charge, BCR/VFM, WECA/MCA approval, DfT acceptance or legal sign-off claims.

## Review Criteria

| Criterion | Pass condition | Failure condition |
|---|---|---|
| Overclaim detection | Identifies concrete risky claims and controls | Gives general warnings only |
| Gate integrity | Keeps Stage 7 blocked | Suggests passing OBC gate |
| Validator coverage | Specifies what validator should catch | Leaves controls manual only |
| Public risk | Considers public repo misuse | Treats simulation caveat as enough |

## Severity Rules

- `P0 Critical`: any official impersonation or readiness claim.
- `P1 Major`: inadequate guardrail for unsupported evidence, model, finance, boundary or WECA role.
- `P2 Important`: unclear limitations or missing navigation.
- `P3 Minor`: wording issue.

## Context Budget

- Maximum first-read files: 8.
- Maximum output length: 900 words.
- Stop and ask for targeted context if a validator or register file is unclear.

## Required Output

Return concrete findings, severity, required controls, residual risks, confidence and simulation-only recommendation.


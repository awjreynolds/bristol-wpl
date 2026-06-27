# Stage 32A Subagent Packet: Officer Readability Review

## Stage

- Stage ID: Stage 32A.
- Stage purpose: make the OBC simulation readable to officers and senior members while preserving no-go status.
- Parent context packet: `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md`.
- Previous gate report: `review/stage_gate_reports/stage-31a-validation-evidence-log-for-stage-30a-report.md`.

## Role

- Agent role: Officer Readability Agent.
- Simulated competence: senior local-government report readability and public-facing risk communication.
- Independence requirement: independent read-only review.
- Read-only or write scope: read-only.
- Review lane: public/officer readability.

## Exact Question

Would an officer, cabinet lead or council leader understand what the Stage 32A simulated OBC is, what it is not, and what checks remain before any real OBC could be relied on?

## Allowed Context

| File or source ID | Why it is included |
|---|---|
| `README.md` | Current public entry point. |
| `docs/officer/assurance-dashboard.md` | Officer decision dashboard. |
| `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md` | Stage scope. |
| `business_case/obc/00-front-matter/document-control.md` | Existing OBC status wording. |
| `business_case/obc/01-executive-summary/executive-summary.md` | OBC first reader experience. |
| `business_case/obc/07-conclusions-and-decisions/recommendations.md` | Decision and no-go framing. |
| `docs/public/how-to-read-this-repo.md` | Public explanation pattern. |
| `docs/officer/risk-gate-atlas.md` | Risk communication pattern. |

## Out Of Scope

Do not inspect raw evidence or rewrite the OBC. Do not perform legal, finance or TAG assurance.

## Source And Register IDs

| Type | IDs |
|---|---|
| Source IDs | none required beyond cited files |
| Issue IDs | `ISS-0011`, `ISS-0012`, `ISS-0041` |
| Risk IDs | `RISK-0012`, `RISK-0044` |
| Evidence-gap IDs | `EG-0059` |
| Pitfall IDs | identify new pitfall if a reader could misunderstand the draft |

## No-Go Claims

Do not ask for weaker caveats. Do not recommend removing simulation labelling to look official.

## Review Criteria

| Criterion | Pass condition | Failure condition |
|---|---|---|
| Plain-English status | Reader knows this is a simulation-only working draft | Reader may think it is official |
| Decision route clarity | Reader sees what remains blocked | Reader sees a disguised approval recommendation |
| Officer usefulness | Draft helps identify next checks | Draft is only defensive caveats |
| Navigation | Reader can find corpus, OBC draft and gate report | Artefacts are hidden or confusing |

## Severity Rules

- `P0 Critical`: likely reader confusion with official OBC or approval.
- `P1 Major`: unclear no-go blockers or decision status.
- `P2 Important`: navigation or terminology weakness.
- `P3 Minor`: editorial issue.

## Context Budget

- Maximum first-read files: 8.
- Maximum output length: 700 words.
- Stop and ask for targeted context if public/officer navigation cannot be assessed.

## Required Output

Return concise findings with readability risks, wording requirements, navigation requirements, confidence and simulation-only recommendation.


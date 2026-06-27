# Subagent Stage Packet Template

Status: reusable Stage 29A context-control template.  
Date: 2026-06-27.

Use this template when creating a bounded subagent task for a future Bristol WPL simulation stage. Keep the packet short. Do not paste the whole repo, whole conversation or full raw evidence tree.

## Stage

- Stage ID:
- Stage purpose:
- Parent context packet:
- Previous gate report:

## Role

- Agent role:
- Simulated competence:
- Independence requirement:
- Read-only or write scope:
- Review lane: domain | evidence/citation | public/officer readability | red-team

State allowed write paths, or read-only.

## Exact Question

State the narrow question the subagent must answer.

## Allowed Context

List a maximum of 8-12 first-read files unless the task justifies more.

| File or source ID | Why it is included |
|---|---|
|  |  |

## Out Of Scope

List files, folders, claims or source sets the subagent must not review unless it asks for targeted expansion.

## Source And Register IDs

| Type | IDs |
|---|---|
| Source IDs |  |
| Issue IDs |  |
| Risk IDs |  |
| Evidence-gap IDs |  |
| Pitfall IDs |  |

## No-Go Claims

List claims the subagent must not make. Include readiness, approval, legal, financial, source-truth, media-accuracy and professional-assurance limits where relevant.

Record unknowns as gaps rather than infer. For deterministic checks: record unknowns as gaps rather than infer.

## Review Criteria

| Criterion | Pass condition | Failure condition |
|---|---|---|
| Source grounding | Uses named source IDs or records the gap | Infers from memory when a cited source exists |
| Scope discipline | Stays inside the packet or requests a specific expansion | Reviews the whole repo or broad raw evidence by default |
| Claim limits | Preserves no-go wording | Converts source relevance or templates into readiness |
| Contradictions | Flags conflict with other evidence or agents | Suppresses adverse evidence |
| Sign-off | Uses simulation-only wording | Claims real legal, finance, officer or professional approval |

## Severity Rules

- `P0 Critical`: invalidates legality, decision integrity, affordability or core evidence; recommend no-go or pause.
- `P1 Major`: materially affects reliability, public-law risk, appraisal quality, finance, consultation or statutory readiness; recommend rework or proceed with explicit conditions only.
- `P2 Important`: affects clarity, traceability, maintainability or overclaim risk; record as a condition or follow-up.
- `P3 Minor`: editorial or low-impact issue; record without blocking.

## Reviewer Recommendation Options

- `proceed`
- `proceed with conditions`
- `rework required`
- `pause`
- `no-go`
- `findings only - no sign-off authority in packet`

## Context Budget

- Maximum first-read files:
- Maximum output length:
- Stop and ask for targeted context when:

## Required Output

Return a concise `handover.md` with:

1. scope completed;
2. files read or changed;
3. sources and register IDs used;
4. findings;
5. assumptions;
6. unresolved questions;
7. material risks;
8. contradictions or adverse evidence;
9. decisions required;
10. confidence;
11. required professional review;
12. recommended next action;
13. scoped simulation review decision: `simulation sign-off`, `simulation sign-off with conditions`, `simulation rework required`, `simulation no-go`, or `findings only - no sign-off authority in packet`.

## Simulation Sign-Off Limit

Any sign-off is agentic simulation sign-off only. It does not prove evidence truth, source currentness, legal correctness, financial certification, model validity, professional assurance, public-authority approval or WPL readiness.

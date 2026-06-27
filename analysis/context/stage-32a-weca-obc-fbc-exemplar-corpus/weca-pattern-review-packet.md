# Stage 32A Subagent Packet: WECA Business Case Pattern Review

## Stage

- Stage ID: Stage 32A.
- Stage purpose: turn WECA-facing OBC/FBC examples into an authoring pattern for a simulation-only Bristol WPL OBC.
- Parent context packet: `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md`.
- Previous gate report: `review/stage_gate_reports/stage-31a-validation-evidence-log-for-stage-30a-report.md`.

## Role

- Agent role: WECA Business Case Pattern Agent.
- Simulated competence: WECA/MCA assurance framework and local transport business-case document pattern review.
- Independence requirement: independent read-only review.
- Read-only or write scope: read-only.
- Review lane: domain.

## Exact Question

What WECA-facing OBC/FBC document patterns are evidenced in the scoped sources, and what must the simulated Bristol WPL OBC include to resemble that style without implying real approval?

## Allowed Context

| File or source ID | Why it is included |
|---|---|
| `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md` | Stage scope and no-go claims. |
| `evidence/source_register.csv` | Source metadata and status. |
| `analysis/weca-role-and-evidence/stage-2h-package-funding-assurance-trigger-map.md` | WECA/MCA funding and assurance trigger controls. |
| `evidence/processed/text/SRC-BCC-0036.txt` | Extracted WECA-facing OBC/FBC examples from May 2025 minutes. |
| `evidence/processed/text/SRC-BCC-0015.txt` | Extracted WECA-facing FBC examples from March 2026 pack. |
| `evidence/processed/text/SRC-WECA-0027.txt` | WECA programme line containing an OBC example. |
| `business_case/obc/controls/section-dependency-matrix.csv` | Current OBC section controls. |
| `business_case/obc/01-executive-summary/executive-summary.md` | Draft section pattern target. |

## Out Of Scope

Do not review the whole repo, raw PDFs, FBC tree, statutory scheme order, or all processed evidence. Do not make legal conclusions about WECA/MCA statutory role.

## Source And Register IDs

| Type | IDs |
|---|---|
| Source IDs | `SRC-BCC-0036`, `SRC-BCC-0015`, `SRC-WECA-0027`, `SRC-WECA-0006`, `SRC-WECA-0007` |
| Issue IDs | `ISS-0002`, `ISS-0011` |
| Risk IDs | `RISK-0002`, `RISK-0011` |
| Evidence-gap IDs | `EG-0010`, `EG-0059` |
| Pitfall IDs | stage output should identify if new pitfall is needed |

## No-Go Claims

Do not claim that WECA/MCA approved Bristol WPL, that the simulated OBC is a real OBC, or that source examples determine Bristol WPL decision route.

## Review Criteria

| Criterion | Pass condition | Failure condition |
|---|---|---|
| Pattern extraction | Names concrete document-pattern elements with source IDs and line references | Makes generic Five Case claims without source link |
| WECA distinction | Separates WECA assurance route from WPL statutory approval | Converts WECA examples into WPL approval |
| Drafting implications | Gives practical OBC authoring requirements | Gives vague advice |
| Limits | Keeps simulation-only language | Recommends official-looking impersonation |

## Severity Rules

- `P0 Critical`: pattern would impersonate a public authority or imply approval.
- `P1 Major`: pattern misses assurance, finance, decision or dependency controls.
- `P2 Important`: pattern unclear or weakly sourced.
- `P3 Minor`: editorial issue.

## Context Budget

- Maximum first-read files: 8.
- Maximum output length: 900 words.
- Stop and ask for targeted context if the scoped files do not contain enough detail.

## Required Output

Return a concise handover with: scope, files read, findings, required OBC style elements, source IDs/lines, risks, contradictions, confidence and simulation-only recommendation.


# Stage 32A Subagent Packet: Evidence And Citation Control Review

## Stage

- Stage ID: Stage 32A.
- Stage purpose: create a WECA OBC/FBC exemplar corpus and simulation-only OBC working draft.
- Parent context packet: `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md`.
- Previous gate report: `review/stage_gate_reports/stage-31a-validation-evidence-log-for-stage-30a-report.md`.

## Role

- Agent role: Evidence And Citation Control Agent.
- Simulated competence: source-register, source-note and claim-evidence QA.
- Independence requirement: independent read-only review.
- Read-only or write scope: read-only.
- Review lane: evidence/citation.

## Exact Question

Which source IDs and exact local line references can support a WECA-style OBC exemplar corpus, and what citation limits must the simulated OBC respect?

## Allowed Context

| File or source ID | Why it is included |
|---|---|
| `analysis/context/stage-32a-weca-obc-fbc-exemplar-corpus/stage-context.md` | Stage scope. |
| `evidence/source_register.csv` | Source status and metadata. |
| `evidence/source_notes/source-note-coverage-register.csv` | Source-note coverage. |
| `evidence/extraction_manifest.csv` | Extracted text status. |
| `evidence/processed/text/SRC-BCC-0036.txt` | WECA-facing examples. |
| `evidence/processed/text/SRC-BCC-0015.txt` | WECA-facing examples. |
| `evidence/processed/text/SRC-WECA-0027.txt` | WECA programme-line example. |
| `evidence/claim_evidence_matrix.csv` | Existing claim-evidence controls. |

## Out Of Scope

Do not browse the web, inspect raw PDFs, or create new source facts. Do not verify source truth beyond local extraction status.

## Source And Register IDs

| Type | IDs |
|---|---|
| Source IDs | `SRC-BCC-0015`, `SRC-BCC-0036`, `SRC-WECA-0027`, `SRC-WECA-0006`, `SRC-WECA-0007` |
| Issue IDs | `ISS-0007`, `ISS-0011`, `ISS-0041` |
| Risk IDs | `RISK-0044` |
| Evidence-gap IDs | `EG-0044`, `EG-0059` |
| Pitfall IDs | stage output should identify if new pitfall is needed |

## No-Go Claims

Do not state that extracted examples are complete OBC/FBC documents unless the source itself is the business case document. Do not treat minutes or packs as substitute full exemplar documents without limitation.

## Review Criteria

| Criterion | Pass condition | Failure condition |
|---|---|---|
| Source status | Distinguishes downloaded, raw-omitted and seeded-not-downloaded sources | Treats all source rows equally |
| Line references | Gives exact local line references for exemplar claims | Provides unsourced examples |
| Citation limits | Identifies what each example can and cannot support | Lets a source support wider claims than it contains |
| Gap control | Records missing full exemplar documents | Fills gaps by inference |

## Severity Rules

- `P0 Critical`: unsupported claim that a full source document exists or proves approval.
- `P1 Major`: missing source status, hash, extraction or line-reference caveat.
- `P2 Important`: source useful but needs clearer claim boundary.
- `P3 Minor`: formatting issue.

## Context Budget

- Maximum first-read files: 8.
- Maximum output length: 900 words.
- Stop and ask for targeted context if a source-status contradiction appears.

## Required Output

Return a concise handover with: files read, source-status table, usable exemplar claims, prohibited claims, evidence gaps, confidence and simulation-only recommendation.


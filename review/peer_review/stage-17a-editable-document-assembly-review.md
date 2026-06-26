# Stage 17A Editable Document Assembly Review

Status: simulated document-assembly, legal/statutory, public/officer and red-team review with conditions.  
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 17A makes editable authoring outputs easier to understand without implying that OBC, FBC, statutory, consultation, officer-review or public-distribution outputs are ready.

## Findings

| Finding | Severity | Response |
|---|---|---|
| "Editable" can sound like "ready to edit for approval." | P1 | Stage 17A uses "working files", "drafting scaffolds" and "controlled inputs for future assurance" language. |
| OBC/FBC folder presence can be mistaken for assembled business cases. | P1 | The output register marks OBC/FBC assembled outputs as blocked and the assembly scripts fail closed. |
| `assemble_fbc.py` previously exited successfully as a placeholder. | P1 | Stage 17A makes it fail closed while FBC/statutory blockers remain. |
| Statutory dossier placeholders can be mistaken for a submission pack. | P1 | The validator checks statutory no-go and readiness rows remain `blocked_control_only`. |
| No-PDF language can be missed. | P1 | Stage 17A repeats "No authored officer-distribution PDFs" in authoring, README, dashboard and validators. |
| PDF checks should catch uppercase extensions and file signatures. | P2 | The Stage 17A validator and no-PDF test check case-insensitive extensions and PDF magic outside `evidence/raw/**`. |

## Red-Team Challenge

| Challenge | Severity | Resolution |
|---|---|---|
| Alternate assembled filenames could bypass `assemble_obc.py`. | P1 | Stage 17A blocks designated assembly directories from containing outputs other than `.gitkeep`. |
| Stage 17A could appear as the next step toward OBC approval. | P1 | Gate report and visual map show it as an authoring-control layer with arrows back to blocked gates. |
| Claim summaries could be used as reusable drafting authority. | P1 | Stage 17A preserves `EG-0045` and requires future drafting-specific summaries before reliance. |

## Decision

Simulation sign-off with conditions for editable authoring-control purposes only.

Stage 17A does not assemble, approve or certify an OBC, FBC, statutory dossier, consultation pack, officer-review DOCX, public pack, scheme order or statutory submission.

## Conditions

| Condition | Owner | Trigger | Closure Route |
|---|---|---|---|
| Keep assembled OBC/FBC outputs blocked. | Integrated Case Review Agent | Any assembled business-case output is requested | Resolve OBC/FBC readiness blockers and pass the relevant gate before assembly. |
| Keep authored PDFs prohibited. | Technical Editor Agent | Any officer-distribution PDF is requested or generated | Use editable Markdown, DOCX, XLSX or HTML; keep PDFs only as downloaded raw evidence. |
| Keep statutory placeholders blocked. | Legal Review Agent | Any statutory dossier output is described as ready | Complete route, order, consultation, FBC, DfT and legal review evidence before readiness claims. |

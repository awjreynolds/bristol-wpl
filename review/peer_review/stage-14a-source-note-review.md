# Stage 14A Source Note Review

Status: simulated evidence review with conditions.
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 14A creates useful source-note controls without implying that evidence review, claim verification, OBC readiness, FBC readiness or legal assurance is complete.

## Findings

| Finding | Severity | Response |
|---|---|---|
| Officers and agents need source-level guidance before drafting source-heavy business-case prose. | P1 | Stage 14A creates a pilot source-note cohort and coverage register. |
| Source notes could be mistaken for claim verification. | P1 | The no-go register blocks claim-verification and OBC-completeness overclaims. |
| Legal and appraisal sources could be over-relied on without specialist review. | P1 | Each note states what the source must not be used to claim and that real review remains required. |
| The full source-note backlog is still open. | P1 | Stage 14A explicitly keeps `ISS-0007` and `EG-0024` open. |

## Reviewer Challenge Resolution

| Challenge | Severity | Resolution |
|---|---|---|
| Coverage and backlog discoverability could be stronger. | P2 | `evidence/source_notes/README.md` now records the coverage boundary, canonical source/extraction registers, current counts and backlog IDs. |
| Simulated review conditions were implied rather than explicit. | P3 | This review now includes a conditions table with owner, trigger and closure route. |
| Stage 14A stage page omitted review and gate cross-links. | P3 | `docs/stages/stage-14a-source-notes.md` now links the peer review and gate report. |
| Validator and tests did not require currentness and FBC evidence no-go coverage. | P2 | The no-go register, validator and tests now require source-currentness and combined OBC/FBC evidence-completeness overclaim controls. |
| Source-register consistency checks were partial. | P3 | `scripts/validate_source_notes.py` now checks every coverage row against `evidence/source_register.csv`, note filename, note existence, title and registered local path. |

## Decision

Simulation sign-off with conditions for source-note controls only.

Stage 14A does not complete evidence review, verify business-case claims, approve an OBC/FBC, replace legal advice or close any WPL gate.

## Conditions

| Condition | Owner | Trigger | Closure Route |
|---|---|---|---|
| Keep `ISS-0007` and `EG-0024` open until every acquired priority source has a reviewed note. | Evidence Librarian | Any claim that the source-note backlog is closed | Update source-note coverage, run source-note QA and record Simulation Gate Authority closure. |
| Extend source notes before source-heavy OBC/FBC, legal, appraisal, consultation or public-summary drafting. | Evidence/Citation Agent | Drafting relies on a source without a note | Add or update the source note and claim-evidence row before drafting reliance. |
| Do not cite source notes as claim verification. | Integrated Case Review Agent | A business-case claim cites a source note instead of source evidence | Replace with source IDs, page/section references and claim-level evidence review. |

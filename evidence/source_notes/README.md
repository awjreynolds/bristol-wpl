# Source Notes

Status: Stage 15B acquired-priority source-note completion controls.
Date: 2026-06-26.

## What This Is

These are Simulation-only source notes for controlled evidence cohorts. They are editable Markdown working notes that help future officers, reviewers and agents understand what a source can support and what it must not be used to claim.

The Stage 14A pilot, Stage 15A expansion and Stage 15B completion cohort now cover downloaded priority-1 source-note coverage in the current source register. The source-note backlog remains controlled at claim-summary level. Does not close ISS-0007 by individual source note; Stage 15B closes only the acquired-priority source-note coverage issue.

## Current Controlled Cohorts

- Stage 14A pilot: 13 cross-workstream source notes in `evidence/source_notes/core/`.
- Stage 15A expansion: 42 legal, Bristol governance, Bristol constitution/delegation and equality-update source notes in `evidence/source_notes/expanded/`.
- Stage 15B completion: 36 WECA/MCA, appraisal, DfT search-control, Nottingham and UK comparator source notes in `evidence/source_notes/stage15b/`.

## Coverage Boundary And Remaining Backlog

The controlled note set now covers 91 source notes. The canonical source universe remains `evidence/source_register.csv`; the extraction state remains `evidence/extraction_manifest.csv`. At the Stage 15B checkpoint the repo has 111 registered sources, 91 normal downloaded sources, 3 raw-omitted downloaded sources, 16 seeded-but-not-downloaded sources and 1 failed acquisition.

Downloaded priority source-note coverage is controlled through `ISS-0007`, `EG-0038` and `EG-0043`. Remaining evidence use is controlled through `EG-0024` and `EG-0044`: claim-level source summaries still need source IDs, page or line references, reviewer status and limitations before high-confidence business-case drafting.

## Raw-Omitted Public Pack Controls

Some Bristol public committee-pack PDFs are omitted from the public repository after the Stage 14B hosted scanner detector-collision incident. Their source notes do not re-authorise raw PDF reliance. They preserve source URL/hash traceability and require raw binary reacquisition outside the public repo before raw-file inspection is relied on.

## Controls

- Coverage register: `evidence/source_notes/source-note-coverage-register.csv`
- No-go register: `evidence/source_notes/source-note-no-go-register.csv`
- Validator: `scripts/validate_source_notes.py`

## No-Go Position

Source notes do not verify every downstream claim, complete an OBC or FBC evidence base, replace legal advice, prove a source is current forever, or close the remaining source-note backlog.

Stage 15B source notes also do not prove WECA/MCA approval or no-role status, DfT or Secretary of State readiness, Green Book or TAG compliance, BCR or VFM status, or Bristol transferability of Nottingham, TfL or Leicester evidence.

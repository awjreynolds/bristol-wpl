# Source Notes

Status: Stage 15A expanded source-note controls.
Date: 2026-06-26.

## What This Is

These are Simulation-only source notes for controlled evidence cohorts. They are editable Markdown working notes that help future officers, reviewers and agents understand what a source can support and what it must not be used to claim.

The source-note backlog remains controlled. The Stage 14A pilot and Stage 15A expansion do not cover every acquired priority source. Does not close ISS-0007.

## Current Controlled Cohorts

- Stage 14A pilot: 13 cross-workstream source notes in `evidence/source_notes/core/`.
- Stage 15A expansion: 42 legal, Bristol governance, Bristol constitution/delegation and equality-update source notes in `evidence/source_notes/expanded/`.

## Coverage Boundary And Remaining Backlog

The controlled note set now covers 55 source notes. The canonical source universe remains `evidence/source_register.csv`; the extraction state remains `evidence/extraction_manifest.csv`. At the Stage 15A checkpoint the repo has 111 registered sources, 94 extracted sources, 16 seeded-but-not-downloaded sources and 1 failed acquisition.

The remaining backlog is tracked through `ISS-0007`, `EG-0024`, `ISS-0019`, `EG-0038`, `ISS-0024` and `EG-0043`. A future source-note expansion must use those registers, not this README, as the authority for closure.

## Raw-Omitted Public Pack Controls

Some Bristol public committee-pack PDFs are omitted from the public repository after the Stage 14B hosted scanner detector-collision incident. Their source notes do not re-authorise raw PDF reliance. They preserve source URL/hash traceability and require raw binary reacquisition outside the public repo before raw-file inspection is relied on.

## Controls

- Coverage register: `evidence/source_notes/source-note-coverage-register.csv`
- No-go register: `evidence/source_notes/source-note-no-go-register.csv`
- Validator: `scripts/validate_source_notes.py`

## No-Go Position

Source notes do not verify every downstream claim, complete an OBC or FBC evidence base, replace legal advice, prove a source is current forever, or close the remaining source-note backlog.

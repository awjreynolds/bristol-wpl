# Source Notes

Status: Stage 14A source-note control pilot.
Date: 2026-06-26.

## What This Is

These are Simulation-only source notes for a first cross-workstream evidence cohort. They are editable Markdown working notes that help future officers, reviewers and agents understand what a source can support and what it must not be used to claim.

The source-note backlog remains controlled. This pilot does not cover every acquired priority source. Does not close ISS-0007.

## Current Pilot Cohort

- Bristol public narrative and decision trail: `SRC-BCC-0001`, `SRC-BCC-0002`, `SRC-BCC-0003`, `SRC-BCC-0004`, `SRC-BCC-0006`, `SRC-BCC-0007`, `SRC-BCC-0014`
- Business-case, appraisal and statutory spine: `SRC-DFT-0001`, `SRC-HMT-0001`, `SRC-LEG-0002`
- WECA assurance context: `SRC-WECA-0007`
- Nottingham comparator context: `SRC-NOTT-0001`, `SRC-NOTT-0002`

## Coverage Boundary And Remaining Backlog

This pilot covers 13 source notes. The canonical source universe remains `evidence/source_register.csv`; the extraction state remains `evidence/extraction_manifest.csv`. At the Stage 14A checkpoint the repo has 111 registered sources, 94 extracted sources, 16 seeded-but-not-downloaded sources and 1 failed acquisition.

The remaining backlog is tracked through `ISS-0007`, `EG-0024`, `ISS-0019` and `EG-0038`. A future source-note expansion must use those registers, not this README, as the authority for closure.

## Controls

- Coverage register: `evidence/source_notes/source-note-coverage-register.csv`
- No-go register: `evidence/source_notes/source-note-no-go-register.csv`
- Validator: `scripts/validate_source_notes.py`

## No-Go Position

Source notes do not verify every downstream claim, complete an OBC or FBC evidence base, replace legal advice, prove a source is current forever, or close the remaining source-note backlog.

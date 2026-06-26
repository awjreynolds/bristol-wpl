# Stage 14A Source Note Control Package

Status: complete as source-note control pilot.
Date: 2026-06-26.

## Purpose

Stage 14A reduces evidence-use risk by creating a first controlled source-note cohort and a validator. It is not a full evidence review and does not close the source-note backlog.

The problem addressed is `ISS-0007` and `EG-0024`: acquired priority evidence exists, but source notes and claim-level source summaries are not yet complete enough for high-confidence business-case prose.

## What This Stage Adds

- Editable source-note landing page: `evidence/source_notes/README.md`
- Core pilot notes under `evidence/source_notes/core/`
- Coverage register: `evidence/source_notes/source-note-coverage-register.csv`
- No-go register: `evidence/source_notes/source-note-no-go-register.csv`
- Validator: `scripts/validate_source_notes.py`
- Unit tests: `tests/test_source_notes.py`

## Pilot Scope

The pilot covers Bristol governance, equality, DfT/HMT guidance, legislation, WECA assurance context and Nottingham comparator material. It is deliberately cross-workstream so future source-note work has a pattern to follow.

## Control Boundary

Stage 14A source notes:

- do not verify every claim in the business case;
- do not complete OBC, FBC, consultation or statutory evidence;
- do not replace legal, appraisal, finance, equalities or officer review;
- do not prove sources remain current after 2026-06-26;
- do not close `ISS-0007` or `EG-0024`.

The source-note backlog remains controlled open.

## Next Work

Future stages should extend the same source-note pattern to every acquired priority source, add claim-level source summaries for high-materiality claims, and re-run source-note QA after every evidence update.

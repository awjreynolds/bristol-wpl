# Stage 27A Validation Evidence Coverage Controls

Status: complete as latest-stage coverage control only.  
Date: 2026-06-26.

## Purpose

Stage 27A checks that the latest previously completed stage has matching validation evidence coverage.

At Stage 27A start, the latest completed stage was Stage 26A. The validator therefore targets Stage 26A explicitly rather than trying to parse a moving "latest stage" label after this page is written.

## What Was Added

- `evidence/validation/stage-26a-validation-run-log.md`
- Stage 26A rows in `evidence/validation/validation-run-register.csv`
- `scripts/validate_validation_coverage.py`
- `tests/test_validation_coverage.py`
- `make validation-coverage-qa`
- Stage 27A register rows and sign-offs

## What It Checks

- Stage 26A validation rows exist.
- Stage 26A required command rows are present.
- Stage 26A rows point to the Stage 26A validation log.
- Stage 26A rows include the expected commit reference, repository-root working directory, passing exit code, linked issue and linked gap.
- Stage 26A rows and log include no-overclaim wording.
- No authored PDFs are introduced.

## What It Does Not Check

- Stage 27A's own validation evidence.
- Raw terminal transcript authenticity.
- command sufficiency;
- evidence truth or source currentness;
- legal correctness or professional assurance;
- substantive gate judgement;
- blocker completeness, risk-rating accuracy or mitigation adequacy;
- OBC, FBC, consultation, statutory or WPL readiness.

## Gate Evidence

- `analysis/context/stage-27a-validation-coverage-context.md`
- `evidence/validation/stage-26a-validation-run-log.md`
- `review/peer_review/stage-27a-validation-evidence-coverage-review.md`
- `review/stage_gate_reports/stage-27a-validation-evidence-coverage-report.md`
- `python3 scripts/validate_validation_coverage.py`


# Stage 23A Register Reference Integrity

Status: complete as cross-register linkage control only.  
Date: 2026-06-26.

## Purpose

Stage 23A reduces register drift by checking that key IDs and file paths used across governance and officer views resolve.

## What Was Added

- `scripts/validate_register_references.py`
- `tests/test_register_references.py`
- `make register-references-qa`
- Stage 23A register rows and sign-offs

## What It Checks

- issue, risk, pitfall and evidence-gap IDs in the risk-control crosswalk;
- pitfall links to issues and risks;
- approval links to simulation sign-offs;
- sign-off unresolved-risk IDs;
- selected evidence, artefact and validator paths;
- latest Stage 22A and Stage 23A register rows;
- no authored PDFs.

## What It Does Not Check

- whether the linked register row is substantively right;
- whether a risk rating is correct;
- whether a mitigation is adequate;
- whether evidence proves a claim;
- whether legal, finance, modelling, consultation, equality or statutory judgement is sound;
- WPL readiness.

## Gate Evidence

- `review/peer_review/stage-23a-register-reference-integrity-review.md`
- `review/stage_gate_reports/stage-23a-register-reference-integrity-report.md`
- `python3 scripts/validate_register_references.py`

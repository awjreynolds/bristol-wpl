# Stage 25A Stage-Gate Report Structure Consistency

Status: complete as gate-report structure control only.  
Date: 2026-06-26.

## Purpose

Stage 25A reduces the risk that recent gate reports claim acceptance without recording focused validation commands, full validation commands, remaining blockers and no-overclaim caveats.

## What Was Added

- `scripts/validate_stage_gate_reports.py`
- `tests/test_stage_gate_reports.py`
- `make stage-gate-reports-qa`
- Stage 25A register rows and sign-offs

## What It Checks

- Stage 22A to Stage 25A reports include focused validation commands;
- those reports include full validation commands;
- those reports include remaining blockers and gate decision sections;
- those reports preserve no-overclaim wording for evidence truth, professional assurance and WPL readiness;
- Stage 25A adds stricter section checks so required commands must appear in the validation section rather than anywhere in a report;
- the report structure remains wording-only and bounded to Stage 22A through Stage 25A;
- no authored PDFs are introduced.

## What It Does Not Check

- whether every command was actually run at the time the report was written;
- whether the gate decision is substantively correct;
- whether evidence proves a claim;
- whether sources are complete or current;
- whether blockers are exhaustive or risk mitigations are adequate;
- whether professional assurance exists;
- WPL readiness.

## Gate Evidence

- `review/peer_review/stage-25a-stage-gate-report-evidence-consistency-review.md`
- `review/stage_gate_reports/stage-25a-stage-gate-report-evidence-consistency-report.md`
- `python3 scripts/validate_stage_gate_reports.py`

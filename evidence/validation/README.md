# Validation Evidence Logs

Status: editable validation-control evidence.  
Date: 2026-06-26.

This folder records command-run evidence for simulation stage gates. It is a process-control record only.

The validation register can show that a command was recorded with a run date, repository state, working-directory context, pass/fail result, exit code, output summary and scope limit. It does not prove evidence truth, legal correctness, source currentness, professional assurance, substantive gate judgement or WPL readiness.

Current files:

- `validation-run-register.csv`
- `stage-25a-validation-run-log.md`
- `stage-26a-validation-run-log.md`
- `stage-29a-validation-run-log.md`
- `stage-30a-validation-run-log.md`

`scripts/validate_validation_coverage.py` currently checks lagged coverage for Stage 26A and Stage 29A. This is coverage of recorded process evidence only; it does not prove command sufficiency, future agent compliance, evidence truth, legal correctness, professional assurance or WPL readiness.

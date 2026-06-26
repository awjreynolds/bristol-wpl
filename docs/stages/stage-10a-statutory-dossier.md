# Stage 10A Statutory Dossier Controls

Status: complete as statutory confirmation dossier control architecture.
Date: 2026-06-26.

## ELI5 Summary

Stage 10A creates a checklist for a future statutory submission. It does not create the submission.

The repo now records the expected dossier components, what evidence each would need, what claims are banned, and why statutory submission remains blocked.

## What Stage 10A Adds

- Dossier component register: `statutory_dossier/controls/dossier-component-register.csv`
- Dossier readiness gate: `statutory_dossier/controls/dossier-readiness-gate.csv`
- Submission no-go register: `statutory_dossier/controls/submission-no-go-register.csv`
- Statutory route memorandum control: `statutory_dossier/controls/statutory-route-memorandum-control.md`
- Clause-by-clause powers matrix: `statutory_dossier/draft_scheme_order/clause-by-clause-powers-matrix.csv`
- Validator: `scripts/validate_statutory_dossier.py`
- Gate report: `review/stage_gate_reports/stage-10a-statutory-dossier-control-report.md`

## Key Issues Captured

| Issue | Why it matters | Stage 10A response |
|---|---|---|
| Dossier component list could be mistaken for a definitive DfT checklist. | DfT expectations must be verified. | Component register says the list is a working framework only. |
| Scheme order working draft could be over-read. | A draft is not a certified order. | Clause-by-clause powers matrix remains blocked. |
| FBC and consultation absence could be hidden. | Statutory submission depends on final case and consultation evidence. | Readiness gate links to OBC/FBC and consultation blockers. |
| DfT engagement could be mistaken for confirmation. | Engagement is not Secretary of State confirmation. | No-go register blocks DfT acceptance and confirmation claims. |

## Current Gate Position

Stage 10A is the control layer only. The future Stage 10 statutory submission dossier remains blocked, and the combined Stage 11 FBC/statutory gate also remains blocked.

No statutory submission, certified order, DfT-accepted dossier, Secretary of State confirmation request, completed consultation statement, FBC or implementation-ready legal pack is created.

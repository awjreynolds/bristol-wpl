# Stage 21A Link And Navigation Integrity

Status: complete as repo-local navigation control only.  
Date: 2026-06-26.

## Purpose

Stage 21A adds static checks for public/officer navigation drift after the new reader guides, visual QA controls and stage reports.

## What Was Added

- `scripts/validate_navigation_integrity.py`
- `tests/test_navigation_integrity.py`
- latest-stage navigation updates in `README.md`, `docs/public/README.md`, `docs/officer/assurance-dashboard.md`, `docs/stages/README.md` and the Mermaid maps
- Stage 21A register rows and sign-offs

## What It Checks

- repo-local Markdown links in scoped navigation files;
- backticked repo-local paths in public/officer docs;
- latest-stage wording in root README, stage index and visual maps;
- required public/officer routes;
- recent stage-gate report references;
- no authored PDFs outside allowed raw evidence paths.

## What It Does Not Check

- external URL liveness;
- evidence accuracy;
- content truth;
- source currentness;
- public comprehension;
- accessibility assurance;
- WPL readiness.

## Remaining Gap

`EG-0049` remains open for external-link liveness, content correctness, evidence accuracy and register-ID semantic resolution.

## Gate Evidence

- `review/peer_review/stage-21a-link-navigation-integrity-review.md`
- `review/stage_gate_reports/stage-21a-link-navigation-integrity-report.md`
- `python3 scripts/validate_navigation_integrity.py`

# Stage 21A Link And Navigation Integrity Context

Status: working context packet.  
Date: 2026-06-26.

## Stage Purpose

Stage 21A creates static link and navigation integrity controls for public/officer documentation.

The stage should catch:

- missing local Markdown/CSV/Mermaid links;
- stale latest-stage wording;
- stage reports not listed in root navigation;
- public/officer entry points that omit key guides;
- visual fallback files missing from navigation.

## Files In Scope

- `README.md`
- `docs/public/README.md`
- `docs/officer/assurance-dashboard.md`
- `docs/officer/document-map.md`
- `docs/stages/README.md`
- `docs/visuals/`
- `review/stage_gate_reports/`
- new validator under `scripts/`
- focused tests under `tests/`
- Stage 21A register rows

## Files Out Of Scope

- No external URL crawling.
- No raw evidence review.
- No authored PDFs.
- No OBC, FBC, consultation or statutory drafting.
- No claim that link validation proves content correctness.

## No-Go Claims

Do not claim or imply:

- local link validation proves evidence accuracy;
- local link validation proves public comprehension;
- local link validation proves accessibility;
- external links are live unless checked in a separate external-link stage;
- any WPL readiness gate closes.

## Subagent Roles

- Navigation reviewer: inspect public/officer entry-point route completeness.
- Link-integrity reviewer: inspect likely static validation criteria and edge cases.
- Red-team reviewer: check false assurance from link validation.

## Validator Commands

- `python3 scripts/validate_navigation_integrity.py`
- `python3 -m unittest tests.test_navigation_integrity`
- `make validate`
- `git diff --check`
- `python3 scripts/scan_secrets.py --all-history`

## Required Register Updates

Add Stage 21A rows for issue, risk, pitfall, evidence gap if needed, requirement, check, decision, approval, simulation sign-off and stage risk matrix.

## Commit And Push Condition

Commit and push only after focused validation, full validation, whitespace check and all-history secret scan pass.

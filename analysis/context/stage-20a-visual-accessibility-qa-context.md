# Stage 20A Visual And Accessibility QA Context

Status: working context packet.  
Date: 2026-06-26.

## Stage Purpose

Stage 20A creates controls for visual and accessibility QA of public/officer navigation artifacts.

It responds to `EG-0047`: no cold-reader testing, cabinet/officer user testing, accessibility review or rendered-visual interpretation evidence exists.

This stage will not perform real user research or professional accessibility certification. It will create a repeatable repo-level QA control for visuals and reader-facing navigation artifacts.

## Files In Scope

- `docs/visuals/stage-gate-map.mmd`
- `docs/visuals/risk-control-atlas.mmd`
- `README.md`
- `docs/public/how-to-read-this-repo.md`
- `docs/public/what-this-repo-can-and-cannot-tell-you.md`
- `docs/officer/cabinet-and-officer-navigation-guide.md`
- `docs/officer/risk-gate-atlas.md`
- new visual QA register under `docs/visuals/`
- new validator under `scripts/`
- focused tests under `tests/`
- Stage 20A register rows

## Files Out Of Scope

- No new source acquisition.
- No rendered image generation requiring external services.
- No authored PDFs.
- No professional accessibility certification.
- No claim that real readers understand the material.
- No OBC, FBC, consultation or statutory drafting.

## No-Go Claims

Do not claim or imply:

- the visuals have been professionally accessibility-audited;
- public/cabinet readers have user-tested the materials;
- Mermaid syntax checks prove rendered interpretation;
- a visual map is approval, readiness or legal advice;
- the repo has WCAG certification;
- any WPL readiness gate closes.

## Subagent Roles

- Visual map reviewer: check map clarity and false-readiness risk.
- Accessibility/readability reviewer: check plain-language and non-PDF navigation risks.
- Red-team reviewer: check visual overclaim, green/complete/readiness leakage and validator criteria.

## Validator Commands

- `python3 scripts/validate_visual_accessibility.py`
- `python3 -m unittest tests.test_visual_accessibility`
- `make validate`
- `git diff --check`
- `python3 scripts/scan_secrets.py --all-history`

## Required Register Updates

Add Stage 20A rows for issue, risk, pitfall, evidence gap, requirement, check, decision, approval, simulation sign-off and stage risk matrix if visual/accessibility controls are added.

## Commit And Push Condition

Commit and push only after focused validation, full validation, whitespace check and all-history secret scan pass.

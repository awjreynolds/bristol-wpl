# Stage 34A GOV.UK style skill adoption

Status: complete as public-writing control only.
Date: 2026-06-27.

## Plain-English summary

Stage 34A adds a repo-local GOV.UK style skill and uses it on the public reader guide.

The skill helps future agents write clearer public and officer prose. It does not change the evidence, legal status, OBC release status or any WPL readiness gate. It is not official GOV.UK/GDS endorsement, legal assurance, accessibility certification, user-tested comprehension or professional sign-off.

## What changed

- Added `skills/govuk-style/SKILL.md`.
- Added `skills/govuk-style/references/sources.md`.
- Added `analysis/content/stage-34a-govuk-style-application.md`.
- Added `scripts/validate_govuk_style_skill.py`.
- Updated the public reader guide to distinguish the OBC simulation release from an approved OBC.

## Key risks

| Risk | Why it matters | Control |
|---|---|---|
| Plain English could weaken legal meaning. | Removing caveats would create false assurance. | Skill says not to simplify away legal, statutory, financial, evidence or no-go meaning. |
| A style pass could hide evidence gaps. | Cleaner prose must not imply readiness. | Stage 34A keeps no-go wording and register IDs. |
| Future agents may over-apply GOV.UK style to data. | CSV rows, legislation, source extracts and IDs need exactness. | Skill excludes registers, direct quotes, commands and raw source extracts. |

## Gate decision

Accepted for Stage 34A public-writing control only.

No OBC, FBC, consultation, statutory, procurement, accessibility, user-comprehension, professional-assurance or WPL readiness gate is changed.

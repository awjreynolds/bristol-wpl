# Stage 34A GOV.UK style skill application

Status: simulation content-control application.
Date: 2026-06-27.

## Relevance decision

The GOV.UK style skill is relevant to this simulation.

This repository is public. It is also meant for officers, cabinet members, legal teams and public readers. The skill supports plain English, front-loaded content and readable, accessibility-aware structure. That is not accessibility testing, WCAG certification or specialist accessibility sign-off. Those writing controls are directly relevant to the README, public guides, officer dashboard and the shipped OBC simulation release.

The skill must not be used to remove legal, statutory, financial, source, evidence or no-go meaning.

## Imported skill

The repo-local skill is:

- `skills/govuk-style/SKILL.md`

It is adapted from:

- `https://gist.github.com/fofr/505e225f9bf5e839d30c12ba6bfa0be2`

It is informed by public GOV.UK guidance:

- `https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/`
- `https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/`

Using the guidance does not make repo content official GOV.UK content, GOV.UK/GDS endorsed, legally assured, accessibility certified or readiness evidence.

## How it was used

Stage 34A used the skill on these reader-facing files:

- `docs/public/how-to-read-this-repo.md`
- `docs/public/README.md`
- `docs/officer/assurance-dashboard.md`
- `README.md`
- `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md`

The applied change in this stage is narrow:

- make `docs/public/how-to-read-this-repo.md` say that an editable OBC simulation release exists;
- keep the statement that it is not an approved OBC, FBC or statutory submission;
- replace "How To Deep Dive" with "How to look in detail".

## Limits

Stage 34A does not change the no-go position.

The skill does not create a real Bristol OBC, officer advice, procurement authority, consultation readiness, statutory readiness, legal assurance, accessibility certification, user-tested comprehension, professional assurance or WPL readiness.

Future agents should use the skill for public and officer prose, then re-run:

- `python3 scripts/validate_govuk_style_skill.py`
- `python3 scripts/validate_public_cabinet_comprehension.py`
- `python3 scripts/validate_navigation_integrity.py`

# Stage 10A Statutory Dossier Control Review

Status: simulated peer review with conditions.
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 10A creates useful statutory confirmation dossier controls without implying that a statutory submission is ready.

## Findings

| Finding | Severity | Response |
|---|---|---|
| The master prompt lists 23 anticipated dossier components, but the repo needed a blocked component register. | P1 | Stage 10A adds `dossier-component-register.csv` with 23 blocked control rows. |
| A scheme order working draft needed clause-by-clause powers controls before any reliance. | P1 | Stage 10A adds a blocked clause-by-clause powers matrix. |
| DfT process and Secretary of State confirmation could be overclaimed. | P1 | Stage 10A adds no-go claims and statutory route memorandum controls. |
| Submission readiness could be confused with FBC or consultation controls. | P1 | Dossier readiness gate links components to open OBC, FBC, consultation, boundary and legal blockers. |

## Simulated Reviewer Findings And Disposition

| Reviewer role | Finding | Severity | Disposition |
|---|---|---|---|
| Officer Assurance Agent and Red Team | OBC and consultation readiness were shown as `AMBER` in the officer dashboard despite being hard no-go gates. | P1 | Fixed. OBC and consultation launch are now `RED`. |
| Officer Assurance Agent and Red Team | Root README visual omitted the blocked Stage 8 consultation-launch gate. | P2 | Fixed. README now shows Stage 8 consultation launch as blocked. |
| Officer Assurance Agent and Red Team | Stage 10A, future Stage 10 statutory submission and Stage 11 terminology could confuse non-specialists. | P2 | Fixed. Stage docs and gate plan now define Stage 10A as a control slice only and Stage 11 as the later combined FBC/statutory gate. |
| Officer Assurance Agent and Red Team | Stage 10A checks were not visible enough in the officer checks map. | P3 | Fixed. Checks map now lists Stage 10A statutory dossier controls and `make statutory-qa`. |
| Legal Review Agent, Monitoring Officer Simulation Agent and DfT Process Simulation Agent | Statutory gate validation relied on OBC readiness blocker wording and did not check Stage 10A readiness/no-go registers. | P1 | Fixed. `validate_statutory_dossier.py --gate` now uses statutory-specific blockers and includes `dossier-readiness-gate.csv`, `submission-no-go-register.csv`, EG-0034, approval and sign-off limitations. |
| Legal Review Agent, Monitoring Officer Simulation Agent and DfT Process Simulation Agent | FBC no-go preservation existed in the register but was not enforced by validator constants or tests. | P2 | Fixed. `FBC is ready for submission` is now a required no-go claim and tested. |
| Legal Review Agent, Monitoring Officer Simulation Agent and DfT Process Simulation Agent | Component 22 did not explicitly record the post-confirmation certified-order future control. | P2 | Fixed. Component 22 minimum evidence now includes the post-confirmation certified-order control. |
| Legal Review Agent, Monitoring Officer Simulation Agent and DfT Process Simulation Agent | Some component-register document paths did not resolve. | P3 | Fixed. Blocked placeholder files now exist under `statutory_dossier/assembled/` and tests require all `required_document` paths to resolve. |

## Decision

Simulation sign-off with conditions for Stage 10A controls only.

Stage 10A does not create a statutory submission, certified scheme order, DfT-accepted dossier, Secretary of State confirmation request, completed consultation statement or FBC.

## Conditions

- `scripts/validate_statutory_dossier.py` must pass for control completeness.
- `scripts/validate_statutory_dossier.py --gate` must fail while live blockers remain.
- Dossier component rows must remain blocked until source-backed evidence and real-world replacement roles exist.
- No authored PDF outputs may be produced.
- Future edits must preserve statutory-specific gate wording; statutory gate failures must not reuse OBC assembly wording.

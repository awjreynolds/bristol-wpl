# Stage 8A Consultation Readiness Control Package

Status: simulation control package.  
Date: 2026-06-26.  
Owner: Consultation Review Agent.  
Review status: Stage 8A simulation review complete with no-go conditions.

This package is not a consultation strategy, consultation material, questionnaire, consultation report, launch authority or officer-distribution document.

## Control Position

Stage 8A creates consultation launch-readiness, stakeholder, material-output, response-analysis, privacy, accessibility and no-go claim controls. It does not launch consultation and does not create consultation DOCX, HTML, report or response artefacts.

Consultation launch remains blocked while legal route, WECA/MCA role, DfT process, boundary, parking inventory, DPIA, equality, OBC, appraisal, operating-procedure and decision-authority blockers remain open.

## Required Stage 8A Artefacts

| Artefact | Required path | Stage 8A status |
|---|---|---|
| Stage 8A control package | `analysis/consultation/stage-8a-consultation-readiness-control-package.md` | Control created |
| Launch readiness register | `consultation/controls/launch-readiness-register.csv` | Control rows |
| Stakeholder coverage register | `consultation/controls/stakeholder-coverage-register.csv` | Control rows |
| Materials output register | `consultation/controls/materials-output-register.csv` | Control rows |
| Response analysis control register | `consultation/controls/response-analysis-control-register.csv` | Control rows |
| Privacy and accessibility register | `consultation/controls/privacy-accessibility-register.csv` | Control rows |
| No-go claim register | `consultation/controls/no-go-claim-register.csv` | Control rows |
| Material version register | `consultation/materials/material-version-register.csv` | Control rows |
| Alternative format register | `consultation/accessibility/alternative-format-register.csv` | Control rows |
| Privacy notice control | `consultation/privacy/privacy-notice-control.md` | Control note |
| Response data controls | `analysis/data-protection-and-cyber/stage-8a-consultation-response-data-controls.md` | Control note |
| Processed response schema | `schemas/consultation-response.schema.json` | Control schema |
| Coding-frame control | `consultation/analysis/coding-frame.csv` | Control rows |
| Representativeness control | `consultation/analysis/representativeness-plan.md` | Control note |
| Duplicate and campaign control | `consultation/analysis/duplicate-campaign-handling-protocol.md` | Control note |
| Accessibility control report | `review/accessibility_review/stage-8a-accessibility-control-report.md` | Simulation review |
| Consultation QA validator | `scripts/validate_consultation.py` | Control created |

## Launch Control

Consultation must be formative, supported by sufficient information, allow adequate time and require conscientious consideration of responses. Stage 8A does not certify that those tests are met.

Before launch, every launch-readiness row must have source evidence, owner, reviewer, residual-risk decision and gate effect recorded. Any open P0 blocks launch. Any launch-blocking P1 without a Simulation Gate Authority condition also blocks launch.

## Materials Control

No consultation materials are created in Stage 8A. The following directories must contain only `.gitkeep` plus whitelisted Stage 8A control files until the launch gate passes and material production is explicitly authorised:

- `consultation/materials/`
- `consultation/questionnaire/`
- `consultation/consultation_report/`
- `consultation/you_said_we_did/`
- `consultation/response_data/`

Future materials must be editable DOCX, accessible HTML or controlled Markdown where appropriate. Authored consultation PDFs are not permitted.

Future public and officer materials must use registered suffix controls rather than uncontrolled filenames. The accepted suffix set for later material production is recorded in `consultation/materials/material-version-register.csv`; `final` and authored `.pdf` outputs remain prohibited.

## Response Data And Analysis Control

Stage 8A does not collect consultation responses and does not create response data. It creates a strict processed-response schema and analysis-control placeholders only.

Future response analysis must not rely on headline support or opposition percentages without coding, representativeness, duplicate, campaign-response, privacy and publication controls. Raw responses and personal data must stay outside normal repo paths.

## Banned Claims

Stage 8A material must not claim:

- consultation is ready to launch;
- consultation has launched;
- consultation is lawful or formative;
- decision-maker authority to consult is evidenced;
- materials are complete, accessible or approved;
- questionnaire, analysis plan, response schema, coding frame or privacy notice is ready;
- equality impacts are complete;
- DfT or WECA/MCA has approved, accepted, consented, supported, objected or has no role;
- OBC, preferred scheme, boundary, revenue, BCR, VFM or statutory submission readiness exists.

## Acceptance Criteria

Stage 8A can be treated as complete for control purposes only when:

- launch-readiness, stakeholder, materials, analysis, privacy, accessibility and no-go controls exist;
- consultation output and response-data directories contain no authored files;
- explicit control files in output directories are limited to the Stage 8A whitelist enforced by `scripts/validate_consultation.py`;
- processed-response schema excludes direct identifiers and requires `personal_data_in_repo=false`;
- `consultation-qa` passes;
- the live launch gate fails with current blockers;
- simulation sign-off records that consultation launch and consultation materials remain blocked.

---
document_id: ANALYSIS-LEGAL-STAGE-2J-DFT-PROCEDURAL-EXPECTATIONS-AND-ENGAGEMENT-CLASSIFICATION
title: Stage 2J DfT Procedural Expectations And Engagement Classification
programme: Bristol Workplace Parking Levy
stage: discovery
status: working
version: 0.1
date: 2026-06-26
evidence_cutoff: 2026-06-26
directorate: Growth and Regeneration
audience: internal-review
issue_purpose: review
owner: Legal Review Agent
authors: [Programme Orchestrator]
reviewers: [Legal Review Agent, DfT Process Simulation Agent, Appraisal Guidance Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/stage-2j-dft-procedural-expectations-and-engagement-classification.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2J DfT procedural expectations and engagement classification control
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: simulation-only
financial_review_status: not-started
accessibility_review_status: not-started
---

# Stage 2J DfT Procedural Expectations And Engagement Classification

Status: simulated legal, DfT-process and appraisal due-diligence artefact. This is not legal advice, DfT advice, Secretary of State confirmation, Bristol officer approval or professional assurance.

## Purpose

Stage 2J tests whether the repo can safely distinguish:

1. the statutory Secretary of State confirmation route;
2. generic DfT transport business-case, TAG and value-for-money expectations;
3. informal or pre-application DfT engagement;
4. WPL-specific DfT procedural expectations for a confirmation submission.

It can control the first three points. It cannot close the fourth point because no WPL-specific current public DfT confirmation procedure or DfT response is held in the repo.

## Controlled Finding

`RISK-0003` is narrowed but not closed. `ISS-0008` and `EG-0021` remain open for WPL-specific DfT procedural expectations.

For simulation drafting, use the following rules.

| Classification | Controlled statement | Evidence | Gate effect |
| --- | --- | --- | --- |
| Statutory confirmation route | Secretary of State confirmation is the controlled statutory assumption for an initial England-only WPL licensing scheme order. | `SRC-LEG-0003` lines 118-127; `SRC-LEG-0020` lines 123-132; `SRC-LEG-0011` lines 89-93 and 222-234 | Controlled for route drafting only; does not close Bristol submitter/signatory route. |
| RPI-only variation exception | The 2009 confirmation exemption applies only to qualifying RPI-linked variation orders and must not be used for an initial order. | `SRC-LEG-0011` lines 89-93 and 222-234 | Prevents false initial-order exemption claims. |
| Generic DfT business-case guidance | DfT transport business-case guidance supports Five Case Model staging, proportionality, investment-decision controls and use alongside TAG. | `SRC-DFT-0001` lines 148-175 and 260-304 | Supports OBC/FBC structure and assurance discipline; not WPL confirmation procedure. |
| TAG appraisal expectations | TAG supports transport modelling, appraisal, objectives and evidence for projects requiring government approval, applied proportionately. | `SRC-DFT-0002` lines 155-169 and 180-192 | Supports appraisal standard and model-output requirements; not a WPL dossier format. |
| Public GOV.UK WPL procedure search | Bounded GOV.UK search-control snapshots did not surface a WPL-specific public DfT confirmation procedure in the captured visible results. | `SRC-DFT-0003` lines 95-105 and 395-433; `SRC-DFT-0004` lines 95-105 and 400-465 | Absence-control only; not proof that no procedure or unpublished expectation exists. |
| DfT engagement | DfT contact may evidence expectations only if logged and classified as informal engagement, policy expectation, procedural requirement, formal decision or confirmation material. | `statutory_dossier/dft_pre_application/questions_for_dft.md`; `statutory_dossier/dft_pre_application/engagement_log.csv` | No DfT approval, clearance or confirmation unless a formal decision source is logged. |

## Engagement Classification Rule

Every DfT interaction must be classified at the point of entry in `engagement_log.csv`.

| Label | Use only when | May be cited as | Must not be cited as |
| --- | --- | --- | --- |
| `informal engagement` | A contact, conversation or non-committal exchange records advice or routing information without a decision effect. | Process context or question refinement. | Approval, clearance, confirmation or procedural requirement. |
| `policy expectation` | DfT indicates a preferred policy, business-case, appraisal or evidence expectation without a binding statutory decision. | Expected evidence standard. | Confirmation or legal clearance. |
| `procedural requirement` | DfT or an authoritative source states a submission step, format, timing or process requirement. | Submission planning control. | Secretary of State confirmation. |
| `formal decision` | A formal decision-maker, power, decision document and legal effect are evidenced. | The decision recorded, within its stated limits. | A wider approval or confirmation than the source says. |
| `confirmation material` | The material is submitted for, or forms part of, the Secretary of State confirmation process. | Part of the confirmation dossier. | Confirmation itself unless the final confirmation decision is evidenced. |

## Prohibited Language

- DfT has approved, endorsed, cleared, accepted or confirmed the Bristol WPL.
- DfT requires this exact WPL dossier format.
- A DfT OBC/FBC is the statutory scheme order.
- A five-case business case is the full confirmation submission.
- The Secretary of State confirmation route is complete or submission-ready.
- The 2009 RPI variation exemption applies to the initial Bristol order.
- The GOV.UK search proves that no WPL-specific DfT procedure or expectation exists.
- Engagement, officer correspondence or silence can substitute for formal confirmation.

## Required Future Evidence

Before any statutory submission readiness claim, the repo must hold and classify:

1. current DfT contact route for WPL confirmation;
2. expected dossier format and contents;
3. expected treatment of OBC/FBC, statutory order and consultation report;
4. expected timetable, inquiry and modification process;
5. any DfT expectation on WECA/MCA interface;
6. post-confirmation conditions and publication expectations;
7. Bristol submitter/signatory authority from Stage 2I controls.

## Stage 2J Finding

Stage 2J gives simulation sign-off with conditions for DfT engagement classification and generic DfT/TAG business-case alignment only.

It does not close WPL-specific DfT procedural expectations, statutory submission readiness, Bristol final order-maker, statutory submitter, signatory, WECA/MCA role, consultation readiness, OBC readiness, FBC readiness or operations readiness.

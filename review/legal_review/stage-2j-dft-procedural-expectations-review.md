---
document_id: REVIEW-LEGAL-REVIEW-STAGE-2J-DFT-PROCEDURAL-EXPECTATIONS-REVIEW
title: Stage 2J DfT Procedural Expectations Review
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
source_markdown: review/legal_review/stage-2j-dft-procedural-expectations-review.md
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

# Stage 2J DfT Procedural Expectations Review

Status: simulated legal, DfT-process and appraisal review. This is not legal advice, DfT advice, Secretary of State confirmation, Bristol officer approval or professional assurance.

## Review Decision

Simulation sign-off with conditions for DfT engagement classification and generic DfT/TAG appraisal alignment. Simulation no-go remains for WPL-specific DfT procedural expectations and statutory submission readiness.

## Findings

| Finding | Severity | Disposition |
| --- | --- | --- |
| Transport Act section 184 and section 198 support treating Secretary of State confirmation as the statutory route for an initial England-only WPL licensing scheme order. | P1 controlled | Keep route rule, but do not treat it as submission readiness. |
| The 2009 RPI variation exemption is narrow and does not apply to an initial order. | P1 controlled | Maintain no-overclaim rule from Stage 2B and Stage 2I. |
| DfT transport business-case guidance and TAG support Five Case Model, appraisal and proportionality controls. | P1 controlled | Use for OBC/FBC structure and analytical requirements. |
| Generic DfT business-case and TAG guidance does not specify a WPL confirmation dossier format. | P1 open | Keep DfT process questions open. |
| Bounded GOV.UK searches did not surface WPL-specific public DfT confirmation procedure in captured visible results. | P1 controlled-open | Use as search-control evidence only, not as proof of absence. |
| All DfT engagement remains unexecuted in the repo engagement log. | P1 open | Keep `ISS-0008` and `EG-0021` open/narrowed. |

## Red-Team Challenges

The following claims are rejected:

- DfT has approved or accepted any Bristol WPL material.
- DfT will confirm the order if the business case follows Five Case Model format.
- The exact confirmation dossier is known from generic DfT guidance.
- The GOV.UK search proves no WPL-specific procedure exists.
- DfT engagement can be cited without classification.

## Simulation Sign-Off

Stage 2J is signed off only as a classification and no-overclaim control. It reduces the risk that DfT engagement will be confused with Secretary of State confirmation, but it does not close the DfT procedural expectation issue.

Future sign-off requires a logged DfT response or authoritative WPL-specific procedural source, classified under the labels in `statutory_dossier/dft_pre_application/questions_for_dft.md`.

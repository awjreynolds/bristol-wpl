---
document_id: REVIEW-STAGE-GATE-REPORTS-STAGE-2J-DFT-PROCEDURAL-EXPECTATIONS-REPORT
title: Stage 2J DfT Procedural Expectations Report
programme: Bristol Workplace Parking Levy
stage: discovery
status: working
version: 0.1
date: 2026-06-26
evidence_cutoff: 2026-06-26
directorate: Growth and Regeneration
audience: internal-review
issue_purpose: review
owner: Simulation Gate Authority
authors: [Programme Orchestrator]
reviewers: [Legal Review Agent, DfT Process Simulation Agent, Appraisal Guidance Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: review/stage_gate_reports/stage-2j-dft-procedural-expectations-report.md
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

# Stage 2J DfT Procedural Expectations Report

Status: simulation stage-gate report. This is not legal advice, DfT advice, Secretary of State confirmation, Bristol officer approval, statutory confirmation, financial sign-off or professional assurance.

## Scope

Stage 2J tests DfT procedural expectation evidence and the classification boundary between DfT engagement and Secretary of State confirmation. It does not contact DfT, obtain a real DfT response, approve a dossier format, close Bristol submitter/signatory route, or approve statutory submission readiness.

## Gate Findings

- Secretary of State confirmation is the controlled statutory assumption for an initial England-only WPL licensing scheme order.
- The 2009 RPI-only variation exemption does not support exempting an initial WPL order from confirmation.
- DfT transport business-case guidance and TAG support Five Case Model, appraisal, proportionality, VFM and model-evidence discipline.
- Generic DfT business-case and TAG guidance does not establish a WPL-specific confirmation dossier format.
- Bounded GOV.UK search-control snapshots did not locate WPL-specific public procedural guidance in the captured visible search results.
- The search-control finding is not proof of absence and cannot substitute for a DfT response or authoritative WPL-specific source.

## Gate Decision

Stage 2J decision: **simulation sign-off with conditions for DfT engagement classification and generic DfT/TAG alignment; simulation no-go remains for WPL-specific DfT procedural expectations and statutory submission readiness.**

## Register Effects

- `RISK-0003` remains P1 but is narrowed by Stage 2J controls.
- `ISS-0008` remains narrowed-open.
- `EG-0021` remains partially closed only.
- `LEGAL-002` remains P0 because Bristol submitter/signatory route is unresolved.
- `LEGAL-015` remains P1 working/open because DfT engagement has not occurred.
- `CLM-0019`, `CLM-0020`, `APP-0014`, `DEC-0009`, `SSO-0038` and `SSO-0039` record Stage 2J controls.

## No-Go Controls

The following statements remain blocked:

- DfT has approved, endorsed, cleared, accepted or confirmed the Bristol WPL.
- DfT requires this exact WPL confirmation dossier format.
- The Five Case Model business case is itself the statutory scheme order.
- The OBC or FBC alone is a complete confirmation submission.
- The GOV.UK bounded search proves that no WPL-specific DfT procedure exists.
- The order or confirmation dossier is submission-ready.
- Secretary of State confirmation is a formality.

## Next Work

1. Populate and classify any real DfT engagement in `statutory_dossier/dft_pre_application/engagement_log.csv`.
2. Acquire any authoritative WPL-specific DfT procedural source if it exists.
3. Re-test `ISS-0008` and `EG-0021` only after that evidence is logged.
4. Keep OBC/FBC and statutory submission readiness blocked while Bristol final route, WECA/MCA role, spatial, appraisal, consultation, operations and finance controls remain open.

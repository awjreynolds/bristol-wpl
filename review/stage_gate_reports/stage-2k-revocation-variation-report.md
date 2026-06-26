---
document_id: REVIEW-STAGE-GATE-REPORTS-STAGE-2K-REVOCATION-VARIATION-REPORT
title: Stage 2K Revocation Variation Report
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
reviewers: [Legal Review Agent, Consultation Review Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: review/stage_gate_reports/stage-2k-revocation-variation-report.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2K revocation variation and consultation control
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: not-started
financial_review_status: not-started
accessibility_review_status: not-started
---

# Stage 2K Revocation Variation Report

Status: simulation stage-gate report. This is not legal advice, DfT advice, Bristol officer approval, statutory confirmation, financial sign-off or professional assurance.

## Scope

Stage 2K tests revocation, variation, confirmation and consultation terminology. It does not approve a scheme order, variation order, revocation order, consultation process, DfT process, Bristol route or statutory submission.

## Gate Findings

- A WPL licensing scheme is made, varied and revoked by order.
- Initial England-only WPL orders and ordinary variations remain controlled as requiring Secretary of State confirmation unless a specific exemption applies.
- The only mapped exemption is the narrow RPI-only variation exemption.
- Revocation is a distinct order-change route. Current evidence supports revocation by order, but does not close confirmation, publication, consultation, DfT process or Bristol route issues.
- Section 185 consultation and inquiry powers are mapped, but consultation readiness remains open because public-law consultation is fact-sensitive.

## Gate Decision

Stage 2K decision: **simulation sign-off with conditions for order-change terminology and RPI-only exemption controls; simulation no-go remains for revocation process readiness and statutory submission readiness.**

## Register Effects

- `EG-0022` moves from open to partially closed only.
- `CLM-0021`, `APP-0015`, `DEC-0010`, `SSO-0040` and `SSO-0041` record Stage 2K controls.
- `LEGAL-003`, `LEGAL-004`, `LEGAL-015`, `LEGAL-022` and `LEGAL-023` are updated or reinforced.
- `RISK-0001`, `ISS-0001`, `ISS-0008` and downstream consultation, OBC/FBC and statutory-submission no-go controls remain unchanged.

## No-Go Controls

The following statements remain blocked:

- Revocation requirements are settled.
- A Bristol-only revocation definitely requires, or definitely does not require, Secretary of State confirmation.
- Revocation needs no consultation.
- Publication, objections and notice procedure is complete.
- The RPI-only variation exemption applies beyond its narrow scope.
- Bristol final order, variation or revocation authority is settled.
- The scheme order, consultation statement, OBC/FBC or statutory submission is ready.

## Next Work

1. Map any current order-procedure regulations made under section 183(3).
2. Add clause-level controls for variation, revocation, publication, objections and notice to the draft scheme order matrix.
3. Expand consultation compliance controls for making, variation and revocation.
4. Keep Stage 2I and Stage 2J blockers visible in any order-change report.

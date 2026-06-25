---
document_id: ANALYSIS-LEGAL-DATA-PROTECTION-AND-INFORMATION-LAW
title: Data Protection And Information Law
programme: Bristol Workplace Parking Levy
stage: discovery
status: working
version: 0.1
date: 2026-06-25
evidence_cutoff: 2026-06-25
directorate: Growth and Regeneration
audience: internal-review
issue_purpose: review
owner: Legal Review Agent
authors: [Programme Orchestrator]
reviewers: [Legal Review Agent, Governance Review Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/data-protection-and-information-law.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2 legal governance technical baseline
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: not-started
financial_review_status: not-started
accessibility_review_status: not-started
---

# Data Protection And Information Law

Status: Stage 2 technical baseline. Simulation only; not legal advice or professional sign-off.

## Question

What information-law controls are needed for WPL licensing and enforcement?

## Current Law And Evidence

`SRC-LEG-0011` shows the operating model requires identifying liable persons, service addresses, representations, evidence, appeal records and enforcement history. The repo has schemas for licence records, parking inventory and enforcement events, but no DPIA or records of processing activity.

## Analysis

The data model will likely involve employer, occupier, provider, premises, contact, vehicle, enforcement and appeal data. It must define lawful basis, statutory gateway, controller/processor status, retention, data sharing, publication/redaction and human review of enforcement decisions.

## Uncertainty

No DPIA, privacy notice, data-sharing agreement or live data source exists.

## Scheme Consequence

No employer survey, enforcement workflow or publication pack can be treated as ready.

## Evidence Required

- DPIA scope and full DPIA.
- Records of processing activity.
- Privacy notices.
- Data-sharing and processor contracts.
- Public-release manifest and redaction policy.

## Decision

Keep data-protection work as a Stage 4 and Stage 8 blocker.

## Professional Reviewer

Simulated Data Protection Review Agent.

## Risk If Unresolved

The programme could collect or publish personal/commercial data without a defensible lawful basis or adequate controls.

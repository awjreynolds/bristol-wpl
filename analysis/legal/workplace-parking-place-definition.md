---
document_id: ANALYSIS-LEGAL-WORKPLACE-PARKING-PLACE-DEFINITION
title: Workplace Parking Place Definition
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
source_markdown: analysis/legal/workplace-parking-place-definition.md
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

# Workplace Parking Place Definition

Status: Stage 2 technical baseline. Simulation only; not legal advice or professional sign-off.

## Question

What parking is within the WPL charging concept?

## Current Law

`SRC-LEG-0001` explains that workplace parking is intended to cover parking by people attending premises to carry out work, including parking at or near the workplace and third-party arrangements, but not park-and-ride or station parking where a further journey is made to the workplace.

## Analysis

The repo must translate the statutory concept into a survey and licensing taxonomy. The parking-base model must distinguish:

- workplace parking at premises;
- nearby or third-party parking made available by arrangement;
- park-and-ride or interchange parking;
- visitor, supplier, student, member and business-customer parking categories;
- exempt vehicle categories and non-chargeable spaces.

## Uncertainty

No Bristol parking inventory, premises taxonomy or employer survey exists.

## Scheme Consequence

No revenue estimate, threshold test, exemption policy or licence design can be treated as decision-ready.

## Evidence Required

- Parking inventory methodology.
- Employer/premises survey instrument.
- Data dictionary mapping parking-place fields to legal definitions.
- Evidence standard for third-party parking arrangements.

## Decision

Use legal taxonomy as a Stage 4 data-design requirement only.

## Professional Reviewer

Simulated Legal Review Agent and Operations Design Agent.

## Risk If Unresolved

The scheme could charge out-of-scope parking, miss in-scope parking or rely on an unenforceable survey base.

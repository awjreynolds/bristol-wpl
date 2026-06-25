---
document_id: ANALYSIS-LEGAL-PREMISES-OCCUPIERS-AND-ASSOCIATED-PERSONS
title: Premises Occupiers And Associated Persons
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
source_markdown: analysis/legal/premises-occupiers-and-associated-persons.md
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

# Premises Occupiers And Associated Persons

Status: Stage 2 technical baseline. Simulation only; not legal advice or professional sign-off.

## Question

Who is liable for licence charges and penalty charges?

## Current Law

`SRC-LEG-0001` explains the occupier charging concept. `SRC-LEG-0011` regulation 4 provides a non-occupier parking-provider liability route where the occupier has arrangements with another person and provides evidence reasonably required by the licensing authority. Regulation 7 creates a parallel penalty-charge liability route.

## Analysis

The licensing dataset must not assume the occupier is always liable. It must capture:

- occupier;
- provider or other person P;
- evidence of arrangements;
- premises;
- licensed maximum;
- liable person for licence charge;
- liable person for PCN;
- service address and communication consent.

## Uncertainty

No Bristol premises/occupier/provider evidence exists.

## Scheme Consequence

Licence records and enforcement workflows can be designed, but not populated or relied on.

## Evidence Required

- Licence-record schema implementation.
- Employer survey and evidence-upload requirements.
- Liability determination procedure.
- Data-protection assessment for occupier/provider information.

## Decision

Treat liable-party rules as a core operating-design dependency.

## Professional Reviewer

Simulated Legal Review Agent and Data Protection Review Agent.

## Risk If Unresolved

PCNs, invoices and licence-charge records may be served on the wrong person.

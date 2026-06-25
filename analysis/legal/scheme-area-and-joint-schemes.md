---
document_id: ANALYSIS-LEGAL-SCHEME-AREA-AND-JOINT-SCHEMES
title: Scheme Area And Joint Schemes
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
reviewers: [Legal Review Agent, Governance Review Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/scheme-area-and-joint-schemes.md
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

# Scheme Area And Joint Schemes

Status: Stage 2 technical baseline. Simulation only; not legal advice or professional sign-off.

## Question

Can a Bristol WPL cover all or part of Bristol, and when would a joint scheme be required?

## Current Law

The Transport Act explanatory note in `SRC-LEG-0001` says local licensing schemes may be introduced by a local traffic authority outside London either singly or jointly and that joint/local schemes can cover any part of the area of the authority or authorities making the scheme. Direct current-law sources now support the same control: `SRC-LEG-0018` allows a local licensing scheme to cover the whole or any part of the licensing authority area, and `SRC-LEG-0025` defines non-metropolitan local traffic authority for this Part by reference to a local traffic authority for an area outside Greater London.

## Analysis

For simulation control, a Bristol-only scheme area is the default working assumption unless Stage 2 evidence establishes a joint, concurrent, transferred or consent-based WECA/MCA route. Stage 2C supports Bristol authority-status mapping only; it does not select a boundary. The statutory route must distinguish:

- Bristol-only scheme within confirmed Bristol authority area;
- joint scheme with another local traffic authority;
- scheme requiring WECA/MCA involvement because functions or net-proceeds arrangements require it;
- cross-boundary premises or occupier arrangements needing apportionment and enforcement rules.

## Uncertainty

No authoritative boundary, address/premises dataset or current promoter function map exists in the repo.

## Scheme Consequence

No scheme boundary may be selected. Boundary options can be scoped only as spatial/data hypotheses for Stage 4.

## Evidence Required

- GIS boundary option files with legal descriptions.
- Current local traffic authority and combined-authority function map.
- Cross-boundary premises policy.
- Joint-scheme necessity assessment.

## Decision

Keep Bristol-only as a modelling assumption, not a legal conclusion.

## Professional Reviewer

Simulated Legal Review Agent and GIS/Data Review Agent.

## Risk If Unresolved

Scheme order could be ultra vires, unclear, unenforceable or inconsistent with the authority that receives and applies net proceeds.

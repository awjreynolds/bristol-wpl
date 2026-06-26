---
document_id: ANALYSIS-LEGAL-STAGE-2K-REVOCATION-VARIATION-AND-CONSULTATION-CONTROL
title: Stage 2K Revocation Variation And Consultation Control
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
reviewers: [Legal Review Agent, DfT Process Simulation Agent, Consultation Review Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/stage-2k-revocation-variation-and-consultation-control.md
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

# Stage 2K Revocation Variation And Consultation Control

Status: simulated legal and public-law due-diligence artefact. This is not legal advice, DfT advice, Bristol officer approval, statutory confirmation or professional assurance.

## Purpose

Stage 2K controls order-change terminology for a Bristol WPL simulation. It distinguishes initial order, ordinary variation, RPI-only variation, revocation, consultation and inquiry controls.

It partially controls `EG-0022`. It does not close revocation publication/process requirements, DfT procedural expectations, public-law consultation triggers or Bristol final decision/signatory route.

## Controlled Finding

| Topic | Controlled statement | Evidence | Gate effect |
| --- | --- | --- | --- |
| Order route | A WPL licensing scheme is made by order of the licensing authority or authorities acting jointly. | `SRC-LEG-0026` lines 117-124 | Supports order terminology only; does not settle Bristol decision body. |
| Variation route | The licensing authority or authorities acting jointly may vary a WPL licensing scheme by order. | `SRC-LEG-0026` lines 119-124 | Variation must be handled as an order-change route, not an informal administrative change. |
| Revocation route | The licensing authority, or any licensing authority in a joint scheme, may revoke a WPL licensing scheme by order. | `SRC-LEG-0026` lines 119-124 | Supports revocation-by-order terminology; does not close publication, consultation or local decision route. |
| Initial order confirmation | An initial England-only licensing scheme order is treated as requiring Secretary of State confirmation before coming into force. | `SRC-LEG-0003` lines 118-127; `SRC-LEG-0020` lines 123-132 | Controlled statutory assumption only; submission route remains open under Stage 2I and Stage 2J. |
| Ordinary variation confirmation | A variation of a licensing scheme does not take effect until the order making the variation has been submitted and confirmed, unless a specific exemption applies. | `SRC-LEG-0003` lines 120-123 | Blocks treating non-RPI changes as simple officer amendments. |
| RPI-only variation exemption | Section 184(1) does not apply only where an order varies a licensing scheme and its sole purpose is RPI-linked licence-charge alteration. | `SRC-LEG-0011` lines 89-93 and 222-234 | Narrow exception only; not available for initial orders, non-RPI variations, broader amendments or revocations. |
| Bristol-only revocation confirmation | Section 184 does not on its face require Secretary of State confirmation of a Bristol-only revocation order; it expressly mentions revocation confirmation for joint local-London schemes. | `SRC-LEG-0003` lines 120-123 | Do not claim confirmation is required or not required without future legal route review. |
| Consultation and inquiry powers | The licensing authority may consult before making, varying or revoking and may hold an inquiry; national authority powers focus on making/varying and confirmation; joint local-London has separate GLA wording. | `SRC-LEG-0027` lines 117-134 | Statutory text is permissive, but public-law consultation remains fact-sensitive and open. |
| Publication and objections | Section 183 allows regulations about order form, publication of proposals for making/varying, objections and notice of orders and effect. | `SRC-LEG-0026` lines 121-124 | Further regulation/procedure mapping required before any claim of process readiness. |

## Required Controls For Future Drafting

Every scheme order, amendment note, revocation note, consultation pack and decision report must distinguish:

1. initial order;
2. ordinary variation;
3. RPI-only variation;
4. revocation;
5. licence-level variation, renewal or cancellation;
6. consultation or inquiry under section 185;
7. public-law consultation outside section 185;
8. publication, objections and notice controls under any applicable order-procedure regulations;
9. Bristol decision-maker, signatory and submission authority.

## Prohibited Language

- Revocation requirements are settled.
- A Bristol-only revocation definitely requires Secretary of State confirmation.
- A Bristol-only revocation definitely never requires Secretary of State confirmation.
- Revocation needs no consultation.
- The RPI-only variation exemption applies to an initial order, ordinary non-RPI variation, broader amendment or revocation.
- A licence-level administrative change can alter the scheme order.
- DfT engagement, silence or bounded GOV.UK search absence proves the process.
- Bristol officers can make, vary, revoke or submit order-change documents without Stage 2I route authority.

## Stage 2K Finding

Stage 2K partially controls `EG-0022` by source-bounding order-change terminology and the narrow RPI-only exemption.

It does not close revocation confirmation, publication, consultation, DfT procedure, Bristol decision-maker, signatory, consultation readiness, OBC readiness, FBC readiness, operations readiness or statutory submission readiness.

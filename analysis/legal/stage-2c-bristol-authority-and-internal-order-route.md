---
document_id: ANALYSIS-LEGAL-STAGE-2C-BRISTOL-AUTHORITY-AND-INTERNAL-ORDER-ROUTE
title: Stage 2C Bristol Authority And Internal Order Route
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
reviewers: [Bristol Governance Agent, Legal Review Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/stage-2c-bristol-authority-and-internal-order-route.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2C Bristol authority route narrowing
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: not-started
financial_review_status: not-started
accessibility_review_status: not-started
---

# Stage 2C Bristol Authority And Internal Order Route

Status: simulated legal due-diligence artefact. This is not legal advice, officer approval, statutory confirmation, financial sign-off or professional assurance.

## Purpose

Stage 2B left a broad P0 blocker: Bristol competence, order-maker, delegation and submission route. Stage 2C narrows that blocker by adding the missing statutory bridge between the Transport Act 2000 WPL power, the Road Traffic Regulation Act 1984 local traffic authority definition, and Bristol's local government status.

## Source Chain

| Link | Controlled reading | Evidence |
| --- | --- | --- |
| WPL statutory product | A WPL is a Transport Act 2000 workplace parking licensing scheme. A local scheme may be made by a non-metropolitan local traffic authority, and the licensing authority is the authority that makes or proposes to make the scheme. | `SRC-LEG-0017` lines 119-131 |
| Local scheme area and policy test | A local licensing scheme may cover the whole or part of the licensing authority area and must facilitate the licensing authority's local transport policies. | `SRC-LEG-0018` lines 120-123 |
| Local traffic authority cross-reference | Transport Act 2000 uses the Road Traffic Regulation Act 1984 meaning of local traffic authority. | `SRC-LEG-0020` lines 170-180 |
| Non-metropolitan local traffic authority | For this Part, non-metropolitan local traffic authority means a local traffic authority for an area outside Greater London. | `SRC-LEG-0025` lines 121-145 |
| RTRA local traffic authority | Outside Greater London, the council of the county or metropolitan district is traffic authority for roads for which the Secretary of State or strategic highways company is not traffic authority; local traffic authority excludes those national road bodies. | `SRC-LEG-0008` lines 89-102 |
| Bristol local government status | The Avon Order identifies the City of Bristol Council as a transferee authority, constitutes the City of Bristol as a new county, abolishes Avon County Council, and transfers Avon County Council functions to the transferee authority for each district. | `SRC-LEG-0024` lines 83-92, 102-109 and 143-145 |
| Bristol public narrative | Bristol's official WPL webpage states that the annual charge would be paid to the Local Transport Authority, which in Bristol would be Bristol City Council, and administered by a licensing scheme. | `SRC-BCC-0001` lines 21-29 |
| Bristol internal decision machinery | Transport and Connectivity Committee remit, officer delegation principles, Growth and Regeneration delegations, key-decision rules and Full Council reserved functions are evidenced, but do not expressly allocate WPL order-making or submission. | `SRC-BCC-0029` lines 200-210; `SRC-BCC-0030` lines 565-620 and 629-695; `SRC-BCC-0031` lines 51-83 |

## Controlled Stage 2C Finding

For simulation drafting only, Bristol City Council may now be treated as the source-bounded proposed Bristol local licensing authority/order-maker under investigation. The authority-status chain is no longer an unevidenced assumption: it is supported by Transport Act 2000 sections 178, 179, 198 and 163, RTRA 1984 section 121A, and the Avon structural-change source when read together.

That finding does not close the P0 route. The remaining P0 is narrower and more precise:

- which Bristol body must make or approve the final WPL licensing scheme order;
- whether the final decision sits with Transport and Connectivity Committee, Full Council, an officer route, or a sequenced combination;
- who is authorised to submit the initial order for Secretary of State confirmation;
- whether WECA/MCA law, assurance, funding or programme dependencies affect the final route.

## Non-Overclaiming Rules

Allowed language:

> For simulation drafting, Bristol City Council is treated as the proposed licensing authority and order-maker under investigation. The current evidence supports a Bristol-led local licensing authority route when Transport Act 2000 sections 178, 179, 198 and 163, RTRA 1984 section 121A and the Avon structural-change evidence are read together. The internal order-making and submission route remains an open P0 legal/governance issue.

Prohibited language:

- Bristol City Council is confirmed as the competent WPL authority.
- Transport and Connectivity Committee can make and submit the order.
- Officer delegation is sufficient for the final WPL order.
- The scheme can proceed to consultation because the local traffic authority question is resolved.
- WECA/MCA has no role, has approved the scheme, or must consent.

## Spatial Consequence

Stage 2C supports a Bristol-led authority-status working assumption only. It does not select a boundary. Any proposed licensing area must remain within the whole or part of the licensing authority area unless a joint or other legally evidenced route is established. Boundary selection remains blocked by Stage 4 spatial/data P0 controls.

## Gate Consequence

Stage 2C narrows `RISK-0001`, `ISS-0001` and `EG-0019` but does not close them. The programme may continue legal note, statutory matrix, source-note and DfT pre-application question drafting. It must not progress to preferred scheme design, statutory consultation launch, OBC recommendation, FBC readiness, operations readiness or statutory submission readiness.

## Required Next Work

1. Produce a Bristol internal decision-route map showing committee, Full Council and officer-delegation options for OBC, consultation, FBC, final scheme order and Secretary of State submission.
2. Identify the Monitoring Officer, Director Legal and Democratic Services, Chief Finance Officer and committee-report advice checkpoints that simulated agents must test before any route sign-off.
3. Complete WECA/MCA current-law and meeting-record search before concluding no-role, consent, assurance or funding-dependency status.
4. Keep all downstream OBC/FBC drafting source-bounded and conditional.

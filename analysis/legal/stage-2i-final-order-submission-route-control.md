---
document_id: ANALYSIS-LEGAL-STAGE-2I-FINAL-ORDER-SUBMISSION-ROUTE-CONTROL
title: Stage 2I Final Order And Submission Route Control
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
reviewers: [Bristol Governance Agent, Legal Review Agent, Monitoring Officer Simulation Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/stage-2i-final-order-submission-route-control.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2I Bristol final order and submission route control
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: not-started
financial_review_status: not-started
accessibility_review_status: not-started
---

# Stage 2I Final Order And Submission Route Control

Status: simulated legal and Monitoring Officer due-diligence artefact. This is not legal advice, Monitoring Officer advice, Bristol officer approval, committee approval, statutory confirmation or professional assurance.

## Purpose

Stage 2I tests whether the local evidence now supports closing the P0 blocker for Bristol's final WPL licensing-scheme order-maker, statutory submitter and signatory route.

It does not. The evidence supports a Bristol-led licensing-authority working assumption and a Transport and Connectivity Committee route for OBC/progression/FBC decisions, but it does not expressly allocate the final initial WPL licensing scheme order-making decision or the Secretary of State submission/signatory route.

## Controlled Finding

`RISK-0001` and `ISS-0001` remain P0. Stage 2I narrows the route by adding decision-box and escalation controls only.

The final order/submission route may be drafted only as one of the following controlled options until a future source-supported Monitoring Officer/legal route decision is recorded:

| Option | Controlled use | Required evidence before reliance | Gate effect |
| --- | --- | --- | --- |
| Conservative Full Council route | Transport and Connectivity Committee recommends; Full Council makes or approves the final WPL licensing scheme order and expressly authorises Secretary of State submission and named signatory. | Monitoring Officer advice that Full Council is required or prudent because a budget/policy-framework, local-legislation, law-reserved, constitutional-interpretation or high-significance trigger remains arguable. | Safest placeholder; not yet approved. |
| Controlled committee route | Transport and Connectivity Committee makes or approves the final order and authorises submission. | Express Monitoring Officer interpretation that the committee has competence, Full Council is not required, the decision is properly forward-planned, and the report names the submitting/signing officer. | P0 remains until that interpretation and resolution exist. |
| Officer sign/authenticate/submit after member decision | Monitoring Officer or authorised officer signs, authenticates, seals if required, and submits the order and confirmation dossier after the member decision. | Express resolution plus Monitoring Officer confirmation that the documents match the decision and law does not require another signer. | Execution route only; not order-making authority. |

Officer-only final order-making is not source-supported.

## Source Controls

| Control | Controlled reading | Evidence |
| --- | --- | --- |
| WPL statutory product | A WPL licensing scheme may be made by a non-metropolitan local traffic authority; the licensing authority is the authority by which the scheme is or is proposed to be made. | `SRC-LEG-0017` lines 125-131 |
| Local scheme area and policy test | A local licensing scheme may cover the whole or part of the licensing authority area and must facilitate local transport policies. | `SRC-LEG-0018` lines 120-123 |
| Confirmation route | An initial licensing scheme order must be submitted to and confirmed by the appropriate national authority before coming into force. | `SRC-LEG-0003` lines 118-127; `SRC-LEG-0020` lines 123-132 |
| RPI-only exemption limit | The 2009 Regulations exempt only qualifying variation orders from the confirmation requirement; this is not an initial-order exemption. | `SRC-LEG-0011` lines 89-93 and 222-234 |
| Transport committee remit | Transport and Connectivity Committee covers transport policy, major transport projects, Local Joint Transport Plan, major projects, capital programme delivery and departmental performance, budget and risk. | `SRC-BCC-0029` lines 200-210 |
| Key decisions | Key decisions are taken by Policy Committees, recorded on Forward Plans and include significant expenditure, city-wide effects, significant legal or financial risk and significant policy change. | `SRC-BCC-0032` lines 267-295; `SRC-BCC-0034` lines 259-325 |
| Officer delegation limits | Delegated powers do not override statute or the constitution, and high-significance, disputed, policy or legal-consequence matters should be referred to committee or Full Council. | `SRC-BCC-0030` lines 565-620 and 629-695 |
| Monitoring Officer role | Monitoring Officer advises on powers, authority, budget/policy framework and lawfulness. | `SRC-BCC-0032` lines 586-631 |
| Document authentication | Monitoring Officer may sign or authorise another officer to sign documents necessary for legal procedure unless law requires otherwise. | `SRC-BCC-0032` lines 847-853 |
| Constitutional interpretation | Constitution-construction disputes outside Full Council meetings are determined by the Monitoring Officer in consultation with the Head of Paid Service. | `SRC-BCC-0032` lines 930-938 |
| Full Council reserved checks | Full Council alone adopts or amends the budget/policy framework, decides matters contrary to it, promotes or opposes local legislation, exercises functions reserved by law and any other matter the council reserves to itself. | `SRC-BCC-0033` lines 21-91 |

## Mandatory Decision Box

Every future final order or submission report must include a discrete decision box using this structure:

```text
Decision sought:
To [make/approve for making] the Bristol Workplace Parking Levy licensing scheme order under Transport Act 2000 Part III, Chapter II, and to authorise its submission for confirmation under Transport Act 2000 section 184.

Decision body:
[Transport and Connectivity Committee / Full Council], on the basis of recorded Monitoring Officer advice that this is the correct constitutional route. Full Council is [required / not required] because [source-bounded reason].

Key decision and notice:
This [is/is not] a key decision and [has/has not] been included on the Forward Plan in accordance with the Access to Information Procedure Rules.

Officer authority:
Authorise [named post] to prepare, finalise, sign/authenticate, seal if required, and submit the order and confirmation dossier to the Secretary of State, subject to Monitoring Officer confirmation that the documents match the decision made.

Advice status:
Monitoring Officer advice, Chief Finance Officer advice, equality/public-law advice, consultation analysis and data/accessibility advice have been recorded in the report.

Conditions precedent:
The order must not come into force unless and until submitted to and confirmed by the appropriate national authority under Transport Act 2000 section 184. No implementation, charging, enforcement or public representation of approval may occur before the stated conditions are satisfied.

No-overclaim:
This decision is separate from OBC approval, consultation launch, FBC approval, order-making, statutory submission and Secretary of State confirmation. It does not treat Secretary of State confirmation as a formality.
```

## Prohibited Language

- Bristol City Council is confirmed as competent WPL authority.
- Transport and Connectivity Committee is confirmed to make or submit the final order.
- Officer delegation alone is sufficient for the final order.
- Full Council is definitely not required.
- Secretary of State confirmation is a formality.
- OBC, consultation, FBC, final order and submission are one implied approval.
- WECA/MCA has no role, has approved or must consent until resolved.
- Statutory consultation launch, preferred scheme design, FBC readiness, operations readiness or statutory submission readiness may progress while this P0 remains open.

## Stage 2I Finding

Stage 2I gives simulation sign-off with conditions for the final order/submission decision-box control only. It does not close the final order-maker, submitter or signatory route. It preserves the P0 while reducing future hallucination risk by specifying the only acceptable route options and the minimum wording required before any later report can seek final order or submission authority.

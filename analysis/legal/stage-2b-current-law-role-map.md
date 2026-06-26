---
document_id: ANALYSIS-LEGAL-STAGE-2B-CURRENT-LAW-ROLE-MAP
title: Stage 2B Current Law Role Map
programme: Bristol Workplace Parking Levy
stage: discovery
status: working
version: 0.1
date: 2026-06-26
evidence_cutoff: 2026-06-25
directorate: Growth and Regeneration
audience: internal-review
issue_purpose: review
owner: Legal Review Agent
authors: [Programme Orchestrator]
reviewers: [Bristol Governance Agent, WECA Governance Agent, Legal Review Agent, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/legal/stage-2b-current-law-role-map.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2B current-law role mapping
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: not-started
financial_review_status: not-started
accessibility_review_status: not-started
---

# Stage 2B Current Law Role Map

Status: simulation due-diligence artefact. This is not legal advice, statutory confirmation, officer approval, financial sign-off or professional assurance.

## Purpose

Stage 2A acquired the current Bristol, WECA/MCA and Transport Act source material. Stage 2B maps that source material to the remaining legal/governance role questions without closing any point that is still only inferential.

## Controlled Findings

| Question | Stage 2B answer | Evidence | Gate status |
| --- | --- | --- | --- |
| What statutory product is a Bristol WPL? | A workplace parking licensing scheme under Transport Act 2000 Part III Chapter II. The scheme imposes charges for workplace parking places and is made by a licensing-scheme order. | `SRC-LEG-0017` lines 119-131; `SRC-LEG-0018` lines 120-123 | Working control |
| Who can make a local WPL licensing scheme? | The Act points to a non-metropolitan local traffic authority, with "licensing authority" defined by reference to the authority that makes or proposes to make the scheme. | `SRC-LEG-0017` lines 125-131; `SRC-LEG-0020` lines 170-180; `SRC-LEG-0008` lines 90-102 | Bristol mapping P0 remains open |
| Can Bristol be treated as the competent authority for simulation drafting? | Only as a controlled working assumption. Bristol City Council is the proposed Bristol WPL licensing authority/order-maker/submitting body under investigation. The RTRA local-traffic-authority definition and Bristol transport-governance sources are consistent with a Bristol-led route, but the repo still lacks an express source mapping Bristol's current legal status to the Transport Act WPL order-making/submission function. | `SRC-LEG-0008`; `SRC-BCC-0029` lines 200-207; `SRC-BCC-0030` lines 507-524; `SRC-BCC-0031` lines 51-83, 110-182 and 381-386 | P0 open |
| Which Bristol body takes the final internal decision? | Not settled. The Transport and Connectivity Committee remit covers transport policy, maintenance, major transport projects, Local Joint Transport Plan, major projects and capital programme delivery. Full Council reserved functions and officer delegation controls must be checked before routing a final WPL order decision. | `SRC-BCC-0029` lines 200-207; `SRC-BCC-0032` lines 746-772; `SRC-BCC-0033` lines 21-94; `SRC-BCC-0034` lines 263-303 | P0 open |
| Do officer delegations resolve order-making/submission? | No. The Growth and Regeneration and City Transport delegations support operational and preparatory transport functions, but they do not expressly name a WPL licensing scheme order, final scheme approval or submission to the Secretary of State. | `SRC-BCC-0030` lines 565-586 and 670-696; `SRC-BCC-0031` lines 51-83 and 110-182 | P0 open |
| Is Secretary of State confirmation required for an initial England scheme? | Yes for simulation control. A licensing scheme order does not come into force unless submitted to and confirmed by the appropriate national authority, and for England-only schemes the appropriate national authority is the Secretary of State. | `SRC-LEG-0003` lines 118-127; `SRC-LEG-0020` lines 124-132; `SRC-LEG-0011` lines 222-235 | P0 confusion risk controlled |
| Does the 2009 RPI exemption remove initial confirmation? | No. The exemption applies only to a variation order whose sole purpose is altering licence charges in line with RPI. | `SRC-LEG-0011` lines 89-96 and 222-224 | Working prohibition |
| Does WECA/MCA have a WPL transferred, concurrent, consent or no-role conclusion? | Not on the acquired evidence. WECA/MCA is treated as a regional transport, strategic-authority, funding and assurance context body only. Current revised WECA Order article pages show older Part 3 transport article text omitted from 4 June 2026. None of the acquired sources expressly proves WECA/MCA WPL approval, rejection, consent, sponsorship, funding, objection, transferred function or no-role status. | `SRC-WECA-0011` lines 60-75; `SRC-WECA-0012` lines 88-100, 191-211 and 302-326; `SRC-LEG-0014` lines 646-668; `SRC-LEG-0016` lines 62-68; `SRC-LEG-0022` lines 82-87; `SRC-LEG-0023` lines 82-87 | P0 open |
| When does WECA/MCA assurance become relevant? | If MCA funding or programme assurance is engaged. The assurance framework is useful for SOBC/OBC/FBC and transport-scheme appraisal expectations, but does not itself create WPL statutory consent. | `SRC-WECA-0007` lines 718-725, 910-930 and 966-976 | P1/P0 depending on funding dependency |

## Stage 2B Decisions

1. The DfT/Secretary of State distinction is now a controlled route rule: DfT engagement may support procedural expectations, but Secretary of State confirmation is the statutory confirmation decision for an initial England-only WPL licensing scheme.
2. `RISK-0003` may be reduced from P0 to a controlled P1 because the repo now has a source-bounded rule preventing DfT engagement from being mistaken for confirmation.
3. `RISK-0001`, `RISK-0002`, `ISS-0001` and `ISS-0002` remain open because Bristol final decision-making/submission route and WECA/MCA current-law role are not closed.
4. The repo may continue legal note, compliance matrix, source-note and pre-application question drafting. It must not proceed to preferred scheme design, statutory consultation launch, OBC recommendation, FBC readiness or statutory submission readiness.

## Required Next Work

- Obtain or derive a legal source note confirming Bristol's current status as the relevant non-metropolitan local traffic authority for the proposed licensing area.
- Identify whether the final WPL order-making and submission decision is a Transport and Connectivity Committee decision, Full Council decision, officer-delegated decision, or a sequenced combination.
- Stage 2G completed a bounded WECA/MCA public ModernGov meeting-record search for WPL, workplace parking levy, road user charging, demand management, Clean Air Zone repayment, CRSTS, and Bristol transport package terms; treat it as bounded public-record evidence only.
- If any MCA or regional funding is used, map the WPL-funded transport package to WECA assurance framework requirements before claiming OBC/FBC readiness.

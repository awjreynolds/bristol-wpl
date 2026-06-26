---
document_id: ANALYSIS-WECA-ROLE-AND-EVIDENCE-STAGE-2G-MEETING-RECORD-SEARCH-LOG
title: Stage 2G WECA/MCA Meeting Record Search Log
programme: Bristol Workplace Parking Levy
stage: discovery
status: working
version: 0.1
date: 2026-06-26
evidence_cutoff: 2026-06-26
directorate: Growth and Regeneration
audience: internal-review
issue_purpose: audit-log
owner: WECA Governance Agent
authors: [Programme Orchestrator]
reviewers: [WECA Governance Agent, Legal Review Agent, Evidence Librarian, Red Team]
approver: Simulation Gate Authority
confidentiality: official
source_of_truth: true
source_markdown: analysis/weca-role-and-evidence/stage-2g-meeting-record-search-log.md
generated_outputs: []
build_id: ''
source_commit: ''
related_decision: Stage 2G WECA/MCA meeting-record search
supersedes: ''
approval_evidence: governance/simulation_signoff_register.csv
distribution: internal-review
retention_category: simulation-control
legal_review_status: simulation-only
analytical_assurance_status: not-started
financial_review_status: not-started
accessibility_review_status: not-started
---

# Stage 2G WECA/MCA Meeting Record Search Log

Status: simulated evidence search log. This is not legal advice, WECA/MCA approval, Bristol officer advice, statutory confirmation, funding approval or professional assurance.

## Purpose

Stage 2G tests the remaining Stage 2E/2F meeting-record condition: whether current official WECA/MCA and Joint Committee public records contain a formal decision, approval, support, objection, consent, sponsorship or funding decision specifically for a Bristol Workplace Parking Levy.

The answer is bounded. It records what was located in the official public ModernGov records searched on 26 June 2026. It is not proof that no unpublished, internal or future record exists, and it does not settle WECA/MCA no-role or consent status.

## Search Method

| Control | Search method |
| --- | --- |
| Source body | Official West of England Combined Authority ModernGov public records only. |
| Search form | `SRC-WECA-0017`; lines 34-39 show the document-search page and word-search prompt. |
| Endpoint | `https://westofengland-ca.moderngov.co.uk/ieSearchResults.aspx` using POST from the official search form. |
| Bodies reviewed | Combined Authority Committee, West of England Joint Committee, joint MCA/Joint Committee meetings and Overview and Scrutiny Committee records surfaced by the official search. |
| Search terms | `Bristol Workplace Parking Levy`, `Workplace Parking Levy`, `workplace parking`, `parking levy`, `Bristol WPL`, `WPL`, `demand management`, `road user charging`, `congestion charging`, `Clean Air Zone`, `CAZ repayment`, `CRSTS`, `mass transit`, `Bristol transport package`. |
| Material hit handling | Candidate hits were inspected and material meeting pages or attachments were downloaded as `SRC-WECA-0018` to `SRC-WECA-0029`. |
| Negative control | Extracted local source texts for `SRC-WECA-0017` to `SRC-WECA-0029` contained no exact `workplace parking`, `WPL` or `parking levy` match after download and extraction. |

## Material Search Results

| Term or group | Official ModernGov result | Downloaded evidence | Classification |
| --- | --- | --- | --- |
| `Workplace Parking Levy`; `workplace parking` | Returned candidate results on the 27 March 2026 and 5 June 2026 joint meeting records. Inspection showed public-items, budget-outturn and investment-plan context rather than a Bristol WPL decision. | `SRC-WECA-0018`, `SRC-WECA-0019`, `SRC-WECA-0022`, `SRC-WECA-0023`, `SRC-WECA-0025`, `SRC-WECA-0026`, `SRC-WECA-0027`, `SRC-WECA-0028` | False-positive or contextual token hits; no formal Bristol WPL decision found. |
| `WPL`; `Bristol WPL` | No material candidate decision links found in the official search output. | Search method recorded by this log and `SRC-WECA-0017`. | No formal Bristol WPL decision found. |
| `congestion charging`; `road user charging` | Returned Overview and Scrutiny and joint-meeting records. 23 March 2026 scrutiny material says congestion charging rested with Bristol and Bath and North East Somerset councils; it does not decide Bristol WPL. | `SRC-WECA-0018` lines 442-453; `SRC-WECA-0021` lines 111-119 | Transport policy context only; not WPL approval, consent or funding. |
| `CRSTS`; `mass transit`; `Bristol transport package` | Returned transport, delivery-assurance and public-question records on CRSTS, Transport for City Regions, Local Transport Delivery Plan and mass transit. | `SRC-WECA-0018` lines 1189-1217 and 1260-1264; `SRC-WECA-0019` lines 364-379; `SRC-WECA-0024` lines 34-51, 269-314 and 347-409; `SRC-WECA-0029` lines 20-29 and 68-117 | Conditional funding/assurance interface context only; not Bristol WPL approval or funding. |
| `Clean Air Zone`; `CAZ repayment` | Returned CAZ and budget-context records, including 5 June 2026 budget outturn. | `SRC-WECA-0027`; source-search result classification in this log | Budget and transport context only; no Bristol WPL CAZ repayment or WPL funding decision found. |
| `transport levy`; `visitor levy` | Appeared in public statements and scrutiny/public questions. | `SRC-WECA-0021` lines 88-102 and 617-624; `SRC-WECA-0023` lines 1336-1342 and 2456-2478 | Not workplace parking levy; keep as false-positive control. |

## Evidence Classifications

| Evidence | Controlled reading | Gate effect |
| --- | --- | --- |
| `SRC-WECA-0018` joint meeting 27 March 2026 | The page records congestion, funding, CRSTS and mass-transit transport items, including delegated authority for CRSTS change requests and business cases. | Funding/assurance interface only. No Bristol WPL formal decision. |
| `SRC-WECA-0019` joint meeting 5 June 2026 | The page records Investment Fund and CRSTS risk-budget flexibility decisions. | Funding/assurance interface only. No Bristol WPL formal decision. |
| `SRC-WECA-0021` Overview and Scrutiny 23 March 2026 | Records visitor levy, congestion charging, mass transit and transport levy discussion. | Policy scrutiny/public-discussion context only. |
| `SRC-WECA-0022`, `SRC-WECA-0023`, `SRC-WECA-0025`, `SRC-WECA-0026` | Public questions/statements discuss mass transit, Bristol transport, visitor/transport levy or ordinary parking impacts. | Public-item context only. Not WECA/MCA support, objection, approval, consent or funding. |
| `SRC-WECA-0024` and `SRC-WECA-0029` | Transport and delivery-assurance reports record CRSTS, TCR, LTDP and programme-assurance controls, including change requests, delegated approvals and CRSTS Board controls. | Package-level funding/assurance trigger evidence if a future WPL-funded package interfaces with these programmes. |
| `SRC-WECA-0027` and `SRC-WECA-0028` | Budget/outturn and investment/grant assurance records contain Bristol, transport-revenue, CAZ, parking, CRSTS and mass-transit context. | Funding-context source only. No formal Bristol WPL funding approval. |

## Stage 2G Finding

Within the bounded official WECA/ModernGov public-record search run on 26 June 2026, no formal WECA/MCA or Joint Committee decision, approval, support, objection, consent, sponsorship or funding decision specifically for a Bristol Workplace Parking Levy was located.

The search did locate regional transport, CRSTS, mass-transit, Transport for City Regions, investment-fund and delivery-assurance material. Those records are relevant to conditional funding and assurance interfaces if Bristol later proposes WPL-funded packages that use or interact with those programmes. They do not evidence WECA/MCA approval, consent, support, objection, sponsorship or funding of the Bristol WPL licensing scheme.

## Controlled Wording

Permitted:

- A bounded official WECA/ModernGov public-record search on 26 June 2026 did not locate a formal WECA/MCA or Joint Committee decision approving, supporting, objecting to, consenting to, sponsoring or funding a Bristol Workplace Parking Levy.
- The official search did locate CRSTS, TCR, mass-transit, investment-fund and delivery-assurance records that are relevant to conditional package-level funding and assurance interfaces.
- The ModernGov search appears to produce token-based false positives; public questions and budget records with separate `workplace`, `parking` or `levy` terms are not WPL decisions.
- This is a bounded search result only, not a no-role or no-consent conclusion.

Prohibited:

- WECA/MCA has no role.
- WECA/MCA consent is not required.
- WECA/MCA has approved, supported, objected to, consented to, funded or sponsored the Bristol WPL.
- No ModernGov result proves no WECA/MCA function.
- CRSTS, TCR, investment-fund or delivery-assurance records are Bristol WPL statutory approval.

## Residual P0

`RISK-0002` and `ISS-0002` remain P0 but narrowed. Stage 2G reduces the meeting-record uncertainty within the official public ModernGov search scope. It does not close:

1. final WECA/MCA no-role or consent status;
2. final package-level funding and assurance dependencies;
3. formal consultation-response status outside the searched public records;
4. final legal route confirmation after full current-law and funding checks.

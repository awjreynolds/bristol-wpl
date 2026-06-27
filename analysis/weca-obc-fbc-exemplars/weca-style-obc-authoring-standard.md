# WECA-Style OBC Authoring Standard For Stage 32A

Status: simulation-only authoring standard.  
Date: 2026-06-27.  
Applies to: `business_case/obc/**` Stage 32A simulated working draft.

## Purpose

This standard translates WECA-facing OBC/FBC patterns into a controlled drafting style for the Bristol WPL simulation. It exists to make the output professionally useful while preventing a public reader from treating the simulated OBC as an approved Bristol, WECA/MCA, DfT or Secretary of State document.

## Required Style Pattern

The simulated OBC must use:

- prominent document control, version history, authorship and review status;
- a report-purpose section explaining the Five Case Model and evidence maturity;
- Strategic, Economic, Financial, Commercial and Management Case sections;
- a conclusions and decisions section limited to no-go conditions and next evidence requirements;
- professional-comments placeholders for legal, finance, equality, consultation, data, modelling, procurement and delivery assurance;
- appendices, registers and source IDs rather than unsupported narrative assertions;
- conditional language where evidence is not complete: `subject to`, `if approved`, `requires future real-world review`, `not evidenced`, `simulation-only`.

The strongest full-source comparator is `SRC-WECA-0009`, whose front matter and contents show document history, client sign-off, report purpose and five-case ordering (`SRC-WECA-0009` lines 1-94 and 172-186). `SRC-WECA-0008` is evidence for the SOC-to-OBC progression and assurance-management pattern (`SRC-WECA-0008` lines 402-407 and 9065-9107).

## Required Evidence Discipline

Every material paragraph must be one of:

- **Cited:** references a source ID, register row, model artefact or line reference.
- **Assumption:** explicitly labelled as an assumption and linked to the assumptions register or required future evidence.
- **Inference:** explicitly identified as a controlled inference from cited sources.
- **Proposal:** clearly marked as a simulation proposal for future real-world review.
- **Gap:** records missing evidence without filling it.

Any paragraph that sounds like a finding but has no source ID, register ID or assumption label fails Stage 32A quality control.

## WECA/MCA Trigger Tags

Each WECA/MCA reference must be tagged as one of:

- `strategic_context`;
- `conditional_funding_assurance_interface`;
- `formal_decision_source`;
- `statutory_role_question`;
- `assumption`;
- `evidence_gap`.

The tag must be visible in the exemplar corpus or the OBC decision-route table. Stage 2H controls still apply: WECA/MCA strategy, assurance, CRSTS, TCR, investment-fund or delivery-assurance material does not prove WPL approval, support, objection, consent, sponsorship, funding approval, transferred function or no-role status.

## Required No-Go Wording

Every Stage 32A OBC draft must include this status formula near the top:

> Stage 32A simulated WECA-style OBC working draft. Not an approved Bristol OBC, not officer advice, not a consultation document, not WECA/MCA/DfT endorsed, not Secretary of State confirmed and not for real-world reliance.

The conclusions section must not use approval-seeking language. It may only recommend:

- retaining no-go status;
- resolving specified P0/P1 blockers;
- acquiring or reviewing specified evidence;
- replacing simulation sign-offs with real-world professional and public-authority review before any external use.

## Prohibited Drafting Moves

Do not:

- use council or WECA branding;
- state or imply that the simulated OBC has been submitted, approved, endorsed or accepted;
- call the draft `final`, `approved`, `officer report`, `committee report`, `WECA submission` or `consultation document`;
- make a preferred option, boundary, charge, threshold, exemption, revenue, BCR, VFM, affordability or package-selection claim without source/model support;
- state that WECA/MCA has approved, supported, objected to, consented to, funded, sponsored or has no role in Bristol WPL;
- state that DfT or the Secretary of State has accepted or confirmed the scheme;
- use agentic simulation sign-off as a substitute for legal, Monitoring Officer, Section 151, finance, modelling, consultation, accessibility, data-protection or officer approval.

## Minimum Stage 32A OBC Body

The simulated OBC must include:

1. document control and status formula;
2. executive summary with no-go status, key blockers and evidence maturity;
3. strategic case with Bristol problem framing, policy fit and unresolved option/package questions;
4. economic case with appraisal framework and explicit model/BCR/VFM gaps;
5. financial case with CAZ-funded OBC development evidence and future funding/affordability gaps;
6. commercial case with licensing-service, procurement, data, enforcement and appeal controls;
7. management case with governance, statutory process, consultation, assurance, risk, benefits and evaluation controls;
8. conclusions limited to conditions-to-close and no-go recommendation;
9. appendix route to exemplar corpus, source register, claim matrix, risk/issues/gap registers and validation evidence.

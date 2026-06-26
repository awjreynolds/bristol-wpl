# Stage 6A OBC Readiness Review

Status: simulation peer review.  
Date: 2026-06-26.  
Scope: OBC section-readiness, claim-dependency, assembly and assurance controls.

This review records simulated agent due diligence only. It is not Bristol officer approval, legal advice, financial certification, commercial assurance, transport-economics advice or professional assurance for real-world use.

## Review Criteria

The Stage 6A package was reviewed against these criteria:

- OBC readiness controls must preserve all open P0 blockers;
- section templates must not be mistaken for review-draft OBC prose;
- the Executive Summary must not create new legal, numerical or readiness claims;
- every five-case section must map dependency, evidence, issue, risk, reviewer and gate effects;
- no BCR, VFM, revenue, boundary, benefits, WECA/MCA, DfT, consultation, operational or statutory readiness claim may be introduced;
- `assemble_obc.py` must block assembly while upstream gates remain blocked;
- no authored PDF output may be produced.

## Five Case Review Findings

The Five Case OBC Dependency Reviewer found that Stage 6A should operate as a dependency-control gate before any OBC package is described as ready.

Required controls are now present for:

- section dependency matrix;
- section readiness register;
- claim-level dependency register;
- no-go claim register;
- assurance review sequence;
- OBC section control notes;
- assembly blocking.

Finding: the package is suitable as OBC readiness control architecture if it remains expressly non-assembly and non-decision-grade.

Limitation: no Strategic Case, Economic Case, Commercial Case, Financial Case, Management Case, Executive Summary or Conclusions section is ready for OBC reliance.

## Assembly and QA Findings

The assembly-control review criteria require the OBC assembly script to fail safely while upstream gates are blocked. Stage 6A implements this by making `scripts/assemble_obc.py` exit non-zero and by validating the block through `scripts/validate_obc.py` and `tests/test_obc.py`.

Finding: assembly is now actively blocked rather than passively placeholder-only.

Limitation: future real OBC assembly logic still needs a manifest, source-linked section checks, DOCX generation controls and accessibility/editorial validation after upstream gates pass.

## Simulation Sign-Off

Decision: simulation sign-off with conditions.

Conditions:

- run `make obc-qa` as part of validation;
- keep P0 blockers `ISS-0001`, `ISS-0002`, `ISS-0003` and `ISS-0004` visible;
- do not create assembled OBC Markdown or officer-review DOCX while assembly is blocked;
- do not draft section prose that implies OBC approval readiness, consultation launch, preferred option, BCR/VFM, revenue readiness, WECA/MCA position, DfT acceptance, operational readiness or statutory submission;
- future OBC assembly must pass the claim dependency register, no-go claim register and full Stage 7 assurance sequence.

# Stage 5A Options and Appraisal Review

Status: simulation analytical assurance review.  
Date: 2026-06-26.  
Scope: Stage 5A options, OAR, ASR, ASST, model-card, uncertainty and reappraisal control architecture.

This review records simulated agent due diligence only. It is not professional transport-economic advice, DfT approval, Bristol officer approval, value-for-money certification or analytical assurance for real-world use.

## Review Criteria

The Stage 5A package was reviewed against these criteria:

- no shortlist, preferred option, BCR, value-for-money category or recommendation is created;
- options are generated from dimensions and credible alternatives, not a pre-selected WPL scheme;
- ASR and ASST controls exist before modelling reliance;
- model cards, run manifests, uncertainty and validation controls are visible;
- gross levy receipts are not treated as economic benefits;
- WPL-only, investment-only and combined-package effects are separated;
- Nottingham transferability is controlled;
- current-guidance reliance is bounded and does not treat landing pages as complete TAG units;
- Stage 4 boundary and parking-base blockers remain visible.

## TAG/Appraisal Review Findings

The TAG/Appraisal Review Agent found that Stage 5A can proceed only as control architecture. Required controls include:

- dimensional longlist and options framework filter;
- OAR structure and evidence requirements;
- ASR and ASST templates;
- model-specific cards for parking-base, behavioural response, transport, revenue, scheme cost, economic appraisal and financial models;
- run manifest controls;
- uncertainty register;
- reappraisal trigger table;
- no-overclaim wording.

Finding: the package provides the required Stage 5A control architecture if it remains expressly non-decision-grade.

Limitation: no current agreed ASR, OAR, ASST, completed/decision-grade model card, model output, BCR, value-for-money category or shortlist exists.

## Red-Team Findings

The Economic Case Red-Team Agent identified seven high-risk failure modes:

| Failure mode | Stage 5A control |
|---|---|
| Predetermined WPL shortlist | Dimension-led longlist, credible alternatives and no-shortlist wording. |
| Nottingham transfer overclaim | Transferability matrix and ban on unsupported comparator assumptions. |
| Gross levy receipts misclassified as economic benefits | Benefits treatment taxonomy and no-BCR rule. |
| WPL-only, investment-only and combined effects blurred | Required separation of effects before appraisal reliance. |
| Boundary, parking-base or model-output hallucination | Dependency table linking blocked claims to Stage 4 and Stage 5 blockers. |
| Current-guidance overclaim | Guidance source requirements table and no full TAG compliance from landing pages. |
| ASR after modelling | OAR, ASR, ASST and ASR change-log controls before modelling. |

Finding: the package addresses the main hallucination and overclaim risks for a control stage.

Limitation: decision-grade Stage 5 remains no-go until underlying evidence, models, data and professional review exist.

## Simulation Sign-Off

Decision: simulation sign-off with conditions.

Conditions:

- run `make appraisal-qa` as part of validation;
- keep `ISS-0004`, `RISK-0005`, `RISK-0010`, `EG-0012` and `EG-0013` visible;
- do not produce OBC/FBC economic prose that implies a shortlist, preferred option, BCR, VFM category, TAG compliance or model output;
- do not use Nottingham assumptions without the transferability matrix and reviewer sign-off;
- do not use gross levy receipts as economic benefits.

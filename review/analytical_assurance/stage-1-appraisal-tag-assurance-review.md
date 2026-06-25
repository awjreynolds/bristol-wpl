# Stage 1 Appraisal, TAG And Assurance Review

Status: simulated due-diligence review. This is not financial, analytical, legal or professional sign-off.

## Decision

Simulation sign-off with conditions.

The repo has a credible government-grade appraisal and assurance spine as a Stage 0/early Stage 1 scaffold. It is not yet operationally ready for professional-grade OBC/FBC authoring, preferred-option selection, consultation reliance or statutory submission.

## Evidence Inspected

- `CODEX_MASTER_PROMPT.md`
- `instructions/03-business-case-authoring.md`
- `instructions/05-modelling-and-appraisal.md`
- `governance/stage-gate-plan.md`
- `business_case/shared/assembly_manifest.md`
- `SRC-DFT-0001`
- `SRC-DFT-0002`
- `SRC-HMT-0001` to `SRC-HMT-0004`
- `SRC-WECA-0006`

## Findings

- Five Case Model structure is correctly separated across strategic, economic, commercial, financial and management cases.
- The stage logic is appropriate: SOC-equivalent strategic assessment, OBC, consultation, FBC reappraisal and statutory dossier.
- The assembly manifest correctly blocks OBC/FBC assembly until legal route, statutory crosswalk, strategic assessment, spatial/data baseline and ASR controls exist.
- TAG controls remain incomplete: `SRC-DFT-0002` is a landing/control extract, not the full set of individual TAG units and data-book inputs needed for appraisal.
- Analytical assurance is conceptually aligned with the Aqua Book, but no model cards, ASR, OAR, ASST, run manifests, validation files or uncertainty workbook exist.
- `SRC-WECA-0006` is relevant if WECA/MCA assurance or funding is engaged; it does not evidence WECA approval.

## Conditions

- Produce ASR, OAR, ASST, uncertainty and reappraisal-trigger controls before OBC drafting.
- Acquire individual TAG units and source notes needed for the selected appraisal scope.
- Populate model cards, input hashes, scenario controls, validation logs and independent analytical review records.
- Do not produce BCRs, preferred options or value-for-money conclusions until Bristol-specific modelling and assurance are available.

## Simulation Caveat

This is simulation-only and has no real-world legal, statutory, financial, analytical or professional effect.

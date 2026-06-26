# Stage 5A Options and Appraisal Control Gate Report

Status: simulation gate report.  
Date: 2026-06-26.  
Gate authority: Simulation Gate Authority.  
Primary artefact: `analysis/economic/stage-5a-options-appraisal-control-package.md`.

This report has no real-world legal, statutory, financial, analytical, DfT, Bristol officer or professional approval effect.

## Evidence Reviewed

- `analysis/economic/stage-5a-options-appraisal-control-package.md`
- `analysis/economic/options-longlist.md`
- `analysis/economic/option-assessment-report.md`
- `analysis/economic/shortlisting-report.md`
- `analysis/economic/appraisal-specification-report.md`
- `analysis/economic/appraisal-specification-summary-tables.csv`
- `analysis/economic/benefits-treatment-taxonomy.csv`
- `analysis/economic/nottingham-transferability-matrix.csv`
- `analysis/economic/boundary-parking-model-dependency-table.csv`
- `models/model_cards/*.md`
- `models/outputs/model-run-manifest-template.json`
- `models/uncertainty/uncertainty-register.csv`
- `review/analytical_assurance/stage-5a-options-appraisal-review.md`

## Gate Criteria

| Criterion | Result |
|---|---|
| Shortlist selected | Not met; deliberately blocked |
| Preferred option selected | Not met; deliberately blocked |
| BCR or VFM category produced | Not met; deliberately blocked |
| Options architecture defined | Met |
| ASR/ASST control templates created | Met |
| Model-card and run-manifest controls created | Met |
| Benefits treatment taxonomy created | Met |
| Nottingham transferability control created | Met |
| Boundary/parking/model dependency table created | Met |
| Stage 5 no-go preserved | Met |

## Gate Finding

Stage 5A creates a controlled architecture for future options and appraisal work. It reduces the risk of predetermined WPL recommendations, unsupported Nottingham transfer, gross-receipts-as-benefits errors, model-output hallucination and ASR-after-modelling failure.

Stage 5A does not provide an OAR, agreed ASR, completed ASST, shortlist, preferred option, model output, BCR, value-for-money category, revenue estimate, consultation-ready economic case or OBC/FBC recommendation.

## Continuing Blockers

- `ISS-0004` remains P0: no ASR/OAR/ASST model cards, uncertainty log or appraisal outputs exist.
- `RISK-0005` remains P1: OBC drafting before SOC-equivalent OAR, ASR and ASST controls is still blocked.
- `RISK-0010` remains P1: landing pages and generic guidance do not equal full TAG source packs.
- `EG-0012` remains partially closed: guidance snapshots/source notes and individual TAG units remain incomplete.
- `EG-0013` is partially closed only: reappraisal trigger controls exist, but no agreed ASR or model outputs exist.
- Stage 4 spatial/data P0 remains open and blocks boundary, parking-base, revenue and displacement modelling.

## Decision

Decision: simulation sign-off with conditions for Stage 5A controls only; simulation no-go remains for Stage 5 appraisal gate, OBC/FBC economic case readiness, consultation reliance and statutory submission readiness.

Conditions:

- future modelling must not start before OAR, ASR, ASST and model-card controls are complete and reviewed;
- every model run must have a run manifest, input hashes, output hashes, validation results and reviewer status;
- every BCR or VFM claim must have model outputs, welfare treatment, uncertainty and TAG/Appraisal Review Agent sign-off;
- every comparator-derived assumption must pass transferability review;
- gross levy receipts must not be counted as economic benefits.


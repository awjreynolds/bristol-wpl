# Stage 8A Consultation Readiness Controls

Status: complete as control architecture only.  
Date: 2026-06-26.

Stage 8A adds the consultation control layer needed before any later consultation-material drafting or launch decision. It does not author a consultation document, questionnaire, public page, consultation report, response dataset or officer-distribution output.

## What Changed

- Added launch-readiness, stakeholder-coverage, material-output, response-analysis, privacy/accessibility and no-go claim registers under `consultation/controls/`.
- Added material-version, alternative-format, privacy, response-data, coding, representativeness, duplicate and campaign-response controls.
- Tightened the processed consultation-response schema so normal repo paths can only hold pseudonymous processed records after a later gate.
- Added `consultation-qa` to `make validate`.
- Added simulated consultation and accessibility review outputs plus a Stage 8A gate report.

## Key Data Points

- Consultation launch remains blocked by open P0 issues on Bristol final order/submission route, WECA/MCA role, boundary/parking inventory and appraisal/model readiness.
- Stage 8A also keeps launch-blocking P1 controls open for DfT process, DPIA/privacy, equality/accessibility, OBC readiness, operating procedure and analysis readiness.
- `consultation/materials/` and `consultation/response_data/` may contain only explicit Stage 8A control files while launch is blocked.
- While production is blocked, the controlled future material suffix list is: `-public.html`, `-officer-review.docx`, `-print-ready.docx`, `-plain-language.html`, `-easy-read.docx`, `-large-print.docx` and `-translated-<bcp47>.docx`.
- Authored consultation PDFs remain prohibited. Downloaded third-party raw evidence PDFs remain allowed only under `evidence/raw/**`.

## Review Findings

Legal and consultation due diligence found that Stage 8A must preserve the public-law no-go position. It can define controls for formative consultation, sufficient information, adequate time and conscientious consideration, but it cannot certify those tests.

Accessibility and analysis due diligence found that no consultation material should be authored until alternative-format, plain-language, limited-digital-access, privacy, coding, representativeness, duplicate and campaign-response controls are fully populated.

## Remaining Blockers

- Bristol decision authority for consultation and final scheme-order/submission route.
- WECA/MCA role, consent, consultation-response and package funding-dependency position.
- DfT WPL-specific process or logged procedural expectation.
- Boundary, parking inventory, operating procedure, DPIA and EqIA evidence.
- OAR, ASR, ASST, model cards, model outputs, BCR and VFM evidence.
- OBC section evidence and Stage 7 assurance.

## Validation

Stage 8A is controlled by:

- `make consultation-qa`
- `python3 scripts/validate_consultation.py --launch-gate`

The first command must pass for the control package. The second command is expected to fail until open P0 and launch-blocking P1 items are resolved or conditionally accepted by the simulated gate authority.

# Bristol Workplace Parking Levy Simulation

This repository is a controlled workspace for a full simulation of a Bristol Workplace Parking Levy OBC, FBC and statutory confirmation dossier.

Source of truth:
- `CODEX_MASTER_PROMPT.md`
- `instructions/00-operating-model.md`
- controlled Markdown, CSV, XLSX, JSON, HTML and GIS artefacts generated under the repo structure

This is not legal advice, statutory confirmation, financial certification or approval by any public body. All sign-offs are agentic simulation sign-offs unless explicitly replaced in a future real-world process.

Officer review and distribution copies must be editable DOCX/XLSX/HTML or controlled Markdown as appropriate. PDFs are allowed only as downloaded third-party raw evidence under `evidence/raw/**`, never as officer-distribution outputs.

## Current Status

Stage 0 bootstrap and Stage 1 source acquisition/simulated assurance are complete with conditions.

Current controlled gate reports:

- `review/stage_gate_reports/stage-2c-bristol-authority-route-report.md`
- `review/stage_gate_reports/stage-2d-bristol-internal-decision-route-report.md`
- `review/stage_gate_reports/stage-2e-weca-mca-role-classification-report.md`
- `review/stage_gate_reports/stage-2f-current-law-function-map-report.md`
- `review/stage_gate_reports/stage-2g-meeting-record-search-report.md`
- `review/stage_gate_reports/stage-2h-package-funding-assurance-report.md`
- `review/stage_gate_reports/stage-2i-final-order-submission-route-report.md`
- `review/stage_gate_reports/stage-2j-dft-procedural-expectations-report.md`
- `review/stage_gate_reports/stage-2k-revocation-variation-report.md`
- `review/stage_gate_reports/stage-2l-context-management-report.md`
- `review/stage_gate_reports/stage-2b-current-law-role-map-report.md`
- `review/stage_gate_reports/stage-2a-governance-evidence-refinement-report.md`
- `review/stage_gate_reports/stage-2-legal-governance-technical-baseline-report.md`

Current evidence state:

- `evidence/source_register.csv` contains 111 rows.
- 94 sources are downloaded.
- 16 sources remain seeded but not downloaded.
- 1 source acquisition failed (`SRC-ACADEMIC-0001`).
- `evidence/extraction_manifest.csv` is the current extraction state: 94 extracted, 16 skipped because not downloaded, and 1 skipped because acquisition failed.
- `evidence/extraction_log.csv` is the append-only extraction audit log.

## Current Gate Position

Do not draft or assemble an OBC/FBC, select a preferred scheme, launch statutory consultation, treat WECA/MCA as approving or consenting, or prepare a statutory submission as ready.

Open controls include:

- P0 Bristol final WPL licensing-scheme order-maker, statutory submitter and signatory route; Bristol-led authority-status evidence is source-bounded by Stage 2C, OBC/FBC member routing is partly controlled by Stage 2D, and Stage 2I adds final order/submission decision-box controls without closing the route.
- P0 WECA/MCA current-law role; Stage 2E controls strategic-context and conditional funding/assurance wording, Stage 2F controls that current scoped repo evidence does not identify a WPL-specific transferred/concurrent WECA/MCA order-making function, Stage 2G narrows bounded public meeting-record search, and Stage 2H classifies package-level funding/assurance triggers. None of these settles consent, no-role, consultation-response or final funding-dependency status.
- P0 authoritative WPL boundary and parking inventory.
- P0/P1 DPIA/lawful-basis pack and enforcement operating procedure.
- P0 ASR/OAR/ASST, model cards, model outputs and uncertainty controls.
- P1 DfT engagement evidence and WPL-specific procedural expectation classification; Stage 2J controls generic DfT business-case/TAG alignment and bounded GOV.UK search-control evidence but does not identify an accepted WPL confirmation dossier route.
- P1 revocation, variation, publication and consultation process controls; Stage 2K controls order-change terminology and the narrow RPI-only variation exemption but keeps revocation process readiness open.
- P1 context overload and hallucinated readiness risk; Stage 2L creates a mandatory bounded context packet and banned-claim controls for future agents but does not close any substantive blocker.

For main-agent legal, governance, statutory, OBC/FBC, DfT, WECA/MCA, order-change or consultation work after Stage 2L, start with:

- `analysis/legal/post-stage-2-legal-governance-context-packet.md`

Subagents should receive bounded task packets rather than the whole context set.

For WECA/MCA funding and assurance context, then add:

- `analysis/weca-role-and-evidence/post-stage-2h-context-packet.md`
- `analysis/weca-role-and-evidence/support-status.md`
- `analysis/weca-role-and-evidence/funding-and-assurance-dependency-matrix.md`
- `review/stage_gate_reports/stage-2h-package-funding-assurance-report.md`

Do not reload the whole WECA/MCA evidence set unless verifying a specific source line, claim or newly discovered decision record.

For DfT engagement and confirmation-route controls, then add:

- `analysis/legal/stage-2j-dft-procedural-expectations-and-engagement-classification.md`
- `statutory_dossier/dft_pre_application/questions_for_dft.md`
- `statutory_dossier/dft_pre_application/confirmation_dossier_checklist.md`
- `review/stage_gate_reports/stage-2j-dft-procedural-expectations-report.md`

For order-change, variation, revocation and consultation controls, then add:

- `analysis/legal/stage-2k-revocation-variation-and-consultation-control.md`
- `statutory_dossier/draft_scheme_order/scheme_order_working_draft.md`
- `statutory_dossier/consultation_statement/consultation_statement.md`
- `review/stage_gate_reports/stage-2k-revocation-variation-report.md`

## Repeatable Commands

```bash
make validate
python3 scripts/acquire_sources.py --priority 1_must
python3 scripts/extract_sources.py
python3 scripts/build_register_workbooks.py
python3 scripts/scan_source_terms.py
python3 scripts/build_document_templates.py
```

Network access is required for source acquisition. Raw third-party PDFs must remain only under `evidence/raw/**` and must not be reused as officer-distribution copies.

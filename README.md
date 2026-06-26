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
- `review/stage_gate_reports/stage-2b-current-law-role-map-report.md`
- `review/stage_gate_reports/stage-2a-governance-evidence-refinement-report.md`
- `review/stage_gate_reports/stage-2-legal-governance-technical-baseline-report.md`

Current evidence state:

- `evidence/source_register.csv` contains 94 rows.
- 77 sources are downloaded and extracted.
- 16 sources remain seeded but not downloaded.
- 1 source acquisition failed (`SRC-ACADEMIC-0001`).
- `evidence/extraction_manifest.csv` is the current extraction state.
- `evidence/extraction_log.csv` is the append-only extraction audit log.

## Current Gate Position

Do not draft or assemble an OBC/FBC, select a preferred scheme, launch statutory consultation, treat WECA/MCA as approving or consenting, or prepare a statutory submission as ready.

Open controls include:

- P0 Bristol final WPL licensing-scheme order-maker and statutory submitter route; Bristol-led authority-status evidence is source-bounded by Stage 2C, and OBC/FBC member routing is partly controlled by Stage 2D.
- P0 WECA/MCA current-law role; Stage 2E controls strategic-context and conditional funding/assurance wording, and Stage 2F controls that current scoped repo evidence does not identify a WPL-specific transferred/concurrent WECA/MCA order-making function, but neither settles consent, no-role, formal-decision or funding-dependency status.
- P0 authoritative WPL boundary and parking inventory.
- P0/P1 DPIA/lawful-basis pack and enforcement operating procedure.
- P0 ASR/OAR/ASST, model cards, model outputs and uncertainty controls.
- P1 DfT engagement evidence and classification, noting that the Secretary of State confirmation route is now controlled for an initial England WPL order.

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

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

Current controlled gate report:

- `review/stage_gate_reports/stage-1-source-acquisition-and-simulated-assurance-report.md`

Current evidence state:

- `evidence/source_register.csv` contains 67 rows.
- 49 sources are downloaded and extracted.
- 17 sources remain seeded but not downloaded.
- 1 source acquisition failed (`SRC-ACADEMIC-0001`).
- `evidence/extraction_manifest.csv` is the current extraction state.
- `evidence/extraction_log.csv` is the append-only extraction audit log.

## Current Gate Position

Do not draft or assemble an OBC/FBC, select a preferred scheme, launch statutory consultation, treat WECA/MCA as approving or consenting, or prepare a statutory submission as ready.

Open P0 blockers include:

- Bristol licensing authority, order-maker and delegation route.
- WECA/MCA current-law role.
- Secretary of State confirmation route classification.
- Authoritative WPL boundary and parking inventory.
- DPIA/lawful-basis pack and enforcement operating procedure.
- ASR/OAR/ASST, model cards, model outputs and uncertainty controls.

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

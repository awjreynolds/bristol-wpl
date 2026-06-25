# Stage 1 Source Acquisition And Simulated Assurance Report

Status: simulation gate report. This is not legal advice, officer approval, statutory confirmation, financial sign-off or professional assurance.

## Scope

This report covers priority source acquisition, text extraction, source-term scanning, document template creation, statutory matrix expansion, spatial/operations schema upgrades and simulated specialist reviews.

## Evidence State

- Source register rows: 67.
- Downloaded sources: 49.
- Seeded but not yet downloaded sources: 17.
- Failed source acquisition: 1 (`SRC-ACADEMIC-0001`).
- Current extraction manifest rows: 67.
- Extracted text files: 49.
- Skipped not downloaded: 17.
- Skipped failed download: 1.

The append-only extraction log remains in `evidence/extraction_log.csv`. The current-state manifest is `evidence/extraction_manifest.csv`.

## Key Documents Added Or Updated

- Priority source acquisition script: `scripts/acquire_sources.py`.
- Text extraction script: `scripts/extract_sources.py`.
- Current source-term scan: `analysis/source_term_scan.md` and `analysis/source_term_scan.csv`.
- Officer-editable source register workbook: `evidence/source_register.xlsx`.
- OBC/FBC and statutory dossier Markdown templates under `business_case/` and `statutory_dossier/`.
- Upgraded schemas for boundary options, spatial metadata, parking inventory, licence records and enforcement events.
- Expanded `statutory_dossier/legal_compliance_matrix.csv`.
- Expanded `statutory_dossier/business_case_to_statutory_crosswalk.csv`.
- New assumptions, issues, risks and claim-evidence rows.

## Simulated Review Outcomes

| review | decision | effect |
| --- | --- | --- |
| Legal and statutory powers | Simulation sign-off with conditions | Stage 1 legal-route scoping may continue only on controlled working assumptions. |
| Bristol governance | Simulation sign-off with conditions | Bristol chronology is usable if scheme-approval claims remain tightly qualified. |
| WECA/MCA role | Simulation sign-off with conditions | WECA/MCA currently remains strategic, funding-context or assurance-context only. |
| Appraisal, TAG and assurance | Simulation sign-off with conditions | Appraisal spine is credible as scaffold; OBC/FBC appraisal is not operational. |
| Comparator evidence | Simulation sign-off with conditions | Comparator lessons are usable cautiously; no direct Bristol impact claims. |
| Spatial, data, operations and enforcement | Simulation no-go | Boundary, parking base, DPIA and operating procedures are absent. |

## Confirmed Stage 1 Findings

1. The acquired Bristol decision trail supports Stage One Development and OBC work, not implementation of a WPL scheme.
2. October 2025 and March 2026 WPL items are evidenced as update/information items, not approvals of implementation, statutory consultation, FBC, preferred option, boundary, charge, threshold or exemptions.
3. A Bristol WPL should be handled in this simulation as an initial Transport Act 2000 licensing scheme order requiring Secretary of State confirmation before implementation, subject to P0 legal authority checks.
4. DfT engagement is not statutory approval or confirmation.
5. WECA/MCA strategic and assurance documents do not evidence formal approval, consent, support, objection or statutory role for Bristol WPL.
6. Schedule 12 requires net-proceeds plans/programmes and accounting controls to be integrated with the financial case and statutory dossier.
7. The 2009 Regulations create concrete operational requirements for licence-charge liability, PCNs, representations, appeals, charge certificates, recovery and notice service.
8. Nottingham and comparator evidence is usable only for cautious transferability lessons and operating precedent at this stage.

## Gate Decision

Stage 1 simulation gate: **simulation sign-off with conditions for evidence baseline and authoring architecture; simulation no-go for preferred scheme, statutory consultation, OBC assembly, FBC assembly, options appraisal, operational readiness and statutory submission.**

## P0 Blockers

- Bristol licensing authority, order-maker and delegation route unresolved.
- WECA/MCA current-law role unresolved.
- Initial order submission and Secretary of State confirmation route not formally settled.
- No selected boundary or authoritative boundary dataset.
- No workplace parking inventory or lawful-basis/DPIA pack.
- No ASR, OAR, ASST, model cards, model outputs, uncertainty log or value-for-money assessment.
- No final OBC/FBC decision papers or later committee approvals.

## P1 Conditions

- Acquire or replace the failed independent congestion source (`SRC-ACADEMIC-0001`).
- Refresh current Nottingham charge/threshold/latest reporting.
- Produce source notes for priority sources.
- Acquire individual TAG units and detailed appraisal source packs.
- Produce licensing/enforcement operating procedure, PCN templates, service policy and appeals/recovery workflow.
- Locate May 2025 decision/minute evidence or explicitly downgrade that gap.

## Validation Evidence

Validation was run on 25 June 2026 after Stage 1 integration and red-team fixes:

```bash
python3 -m py_compile scripts/acquire_sources.py scripts/extract_sources.py scripts/build_source_register.py scripts/build_register_workbooks.py scripts/scan_source_terms.py scripts/build_document_templates.py
make validate
python3 scripts/validate_registers.py
python3 -m unittest discover -s tests
```

Observed result:

- `python3 -m py_compile ...` passed.
- `make validate` passed.
- `python3 scripts/validate_registers.py` passed.
- `python3 -m unittest discover -s tests` passed with 14 tests.
- No authored or misplaced PDFs were found outside `evidence/raw/**`.
- Register ID checks confirmed unique IDs in the source register, sign-off register, claim matrix, legal compliance matrix and statutory crosswalk.

Extraction QA note:

- `SRC-BCC-0002` is marked `extracted` but `quality=script_hydrated_or_placeholder` in `evidence/extraction_manifest.csv`; it must not be used as substantive evidence until repaired or replaced.

## Simulation Caveat

All reviews and sign-offs in this repo are simulated agent due diligence only. They have no real-world legal, statutory, financial, governance, officer, analytical, data-protection, procurement, transport-economics or professional effect.

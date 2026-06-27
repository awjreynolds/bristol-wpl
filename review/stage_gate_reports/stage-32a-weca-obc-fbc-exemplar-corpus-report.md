# Stage 32A Gate Report: WECA OBC/FBC Exemplar Corpus And Simulated OBC Draft

Status: simulation gate report.  
Date: 2026-06-27.

## Summary

Stage 32A adds a WECA-style exemplar corpus and a full simulated Bristol WPL OBC working draft in editable Markdown.

The stage is WPL-focused. It is not a generic WECA OBC/FBC procurement engine. The reusable element is the assurance and authoring machinery; the product remains a Bristol WPL business-case simulation with WPL statutory, spatial, licensing, enforcement, revenue, consultation and transport-package controls.

## Validation

Focused validation:

```bash
python3 scripts/validate_obc.py
python3 scripts/validate_source_notes.py
python3 -m unittest tests.test_obc tests.test_source_notes
```

Full validation before commit:

```bash
make validate
git diff --check
python3 scripts/scan_secrets.py --all-history
```

The validation commands are process controls. They do not prove evidence truth, source currentness, command sufficiency, command authenticity, legal correctness, professional assurance, substantive gate correctness or WPL readiness.

## Added Or Updated Artefacts

- `analysis/weca-obc-fbc-exemplars/exemplar-register.csv`
- `analysis/weca-obc-fbc-exemplars/comparator-matrix.csv`
- `analysis/weca-obc-fbc-exemplars/weca-style-obc-authoring-standard.md`
- `business_case/obc/simulated-working-draft/bristol-wpl-simulated-weca-style-obc.md`
- `evidence/source_notes/stage32a/src-weca-0008.md`
- `evidence/source_notes/stage32a/src-weca-0009.md`
- `review/stage_gate_reports/stage-32a-weca-obc-fbc-exemplar-corpus/subagent-handovers/`

## Remaining Blockers

- Stage 7 OBC gate remains blocked.
- Stage 8 consultation launch gate remains blocked.
- Stage 11 FBC/statutory gate remains blocked.
- Bristol order-maker and statutory submitter route remains unresolved.
- WECA/MCA role, consent/no-role, consultation-response and funding-dependency status remain unresolved.
- Boundary, parking inventory, displacement, appraisal, finance, procurement, operations, consultation, equalities, data and statutory dossier evidence remain incomplete.
- Evidence truth, source currentness, legal correctness, professional assurance, command sufficiency and WPL readiness are not proven by this stage.

## Gate Decision

Stage 32A is accepted as a WECA-style exemplar and simulated OBC drafting-control stage only.

It does not approve an OBC, create officer advice, create a consultation document, provide WECA/MCA/DfT endorsement, provide Secretary of State confirmation, create procurement authority, prove evidence truth, prove legal correctness, provide professional assurance, close substantive gate correctness issues or change WPL readiness.

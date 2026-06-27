# Editable Authoring Guardrails

Status: Stage 17A authoring-control layer.  
Date: 2026-06-26.

## One-Line Rule

Editable authoring outputs are working files only. They help future drafters assemble evidence-linked Markdown, DOCX, XLSX or HTML material. They are not PDFs, not an assembled OBC or FBC, not a statutory submission, not consultation material and not approval by Bristol City Council, WECA/MCA, DfT or any statutory decision-maker.

## Plain-English Version

These files are drafting scaffolds, not finished documents. They show what would need to be checked before a real decision, but they do not make or approve that decision.

## Officer/Cabinet Version

Treat editable outputs as controlled inputs for future assurance, not distributable decision papers. No OBC/FBC gate has passed unless the relevant gate report records that outcome.

## What Exists Now

- Editable source-level controls: `evidence/source_notes/`
- Editable claim-level controls: `evidence/claim_summaries/`
- Editable OBC and FBC section templates: `business_case/obc/` and `business_case/fbc/`
- Editable OBC simulation release: `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md`
- Blocked statutory dossier control placeholders: `statutory_dossier/`
- Officer/public navigation files: `docs/officer/` and `docs/public/`

## What Does Not Exist

- No real assembled OBC in the blocked `business_case/obc/assembled/` path.
- No assembled FBC.
- No officer-review DOCX.
- No consultation launch pack.
- No certified scheme order.
- No statutory submission pack.
- No authored officer-distribution PDF.

## File-Type Rule

Officer-facing material must remain editable Markdown, CSV, XLSX, DOCX or HTML. Authored PDFs are prohibited. Downloaded third-party PDFs may remain only as immutable raw evidence under `evidence/raw/**`.

## Control Register

The output-specific control register is `docs/authoring/document-assembly-control-register.csv`.

The visual flow is `docs/visuals/authoring-control-flow.mmd`.

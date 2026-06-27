# Stage 35A OBC DOCX pack

Status: complete as officer-friendly document-pack control only.
Date: 2026-06-27.

## Plain-English summary

Stage 35A creates a shareable Word document pack for the OBC simulation.

The pack exists because Markdown is a developer-facing format. Officers, cabinet members and legal reviewers are more likely to need DOCX files that can be opened, circulated, commented on and stored in ordinary document-management workflows.

The DOCX pack changes format only. It does not approve the OBC, create officer advice, launch consultation, authorise procurement, settle the statutory route or create WPL readiness.

## What changed

- Added `business_case/obc/docx-pack/bristol-wpl-obc-simulation-release.docx`.
- Added `business_case/obc/docx-pack/bristol-wpl-obc-reader-support-guide.docx`.
- Added `business_case/obc/docx-pack/bristol-wpl-obc-risk-process-control-summary.docx`.
- Added `business_case/obc/docx-pack/bristol-wpl-obc-document-pack.zip`.
- Added `business_case/obc/docx-pack/PACK-MANIFEST.txt`.
- Added `scripts/build_obc_docx_pack.py`.
- Added `scripts/validate_obc_docx_pack.py`.
- Added `tests/test_obc_docx_pack.py`.

## Pack contents

| File | Purpose |
|---|---|
| `bristol-wpl-obc-simulation-release.docx` | Word version of the Stage 33A OBC simulation release. |
| `bristol-wpl-obc-reader-support-guide.docx` | Officer/cabinet-friendly reading guide for the pack. |
| `bristol-wpl-obc-risk-process-control-summary.docx` | Risk, issue, evidence-gap, gate and process summary. |
| `bristol-wpl-obc-document-pack.zip` | Downloadable ZIP containing the three DOCX files and a text manifest. |

## Key risks

| Risk | Why it matters | Control |
|---|---|---|
| A DOCX pack could look official. | Word files can be circulated outside the repo and mistaken for council papers. | Every DOCX has simulation-only and no-reliance wording; the manifest repeats the limits. |
| The ZIP could be treated as an officer distribution pack. | A downloadable pack may imply readiness. | The pack is named and validated as simulation-only; the real OBC assembled path remains blocked. |
| Rendered DOCX layout could fail silently. | Tables and headings can clip or split badly in Word. | Stage 35A rendered all DOCX files to PNG pages and fixed a table split before acceptance. |

## Gate decision

Accepted for Stage 35A document-pack control only.

No OBC, FBC, consultation, statutory, procurement, officer-advice, legal-assurance, professional-assurance or WPL readiness gate is changed.

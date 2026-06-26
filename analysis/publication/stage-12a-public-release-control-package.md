# Stage 12A Public Release Control Package

Status: public-release control architecture.
Date: 2026-06-26.

## Control Question

The repository is now public on GitHub. Stage 12A asks whether the repo records that public state clearly enough that public readers, officers, cabinet members, legal teams and future agents do not confuse publication with WPL approval or readiness.

## Recorded Visibility

Verified command:

```bash
gh repo view awjreynolds/bristol-wpl --json visibility,url,nameWithOwner
```

Recorded result: `visibility=PUBLIC`, `url=https://github.com/awjreynolds/bristol-wpl`.

This public visibility is not approval. It does not close any WPL gate, does not create legal advice, does not launch consultation, does not assemble an OBC or FBC, and does not create a statutory submission.

## Required Public-Release Controls

- README must state that the repository is public and that public visibility is not approval.
- Public and officer entry points must point to the no-go position before specialist material.
- Public wording must state that the GitHub repository is not an official council publication.
- no authored PDFs may exist outside downloaded raw evidence under `evidence/raw/**`, and raw evidence PDFs must use the `src-*` downloaded-source naming convention.
- Restricted consultation or personal data paths must be empty except for `.gitkeep` placeholders and must not be linked from public/officer pages.
- Officer-facing outputs must remain editable Markdown, CSV, XLSX, DOCX, HTML or GIS-ready formats.
- Stage 7, Stage 8, Stage 10 and Stage 11 readiness gates must remain blocked unless their independent evidence tests change.
- Publication checklist `gate_effect` values and no-go `allowed_wording` must not imply approval or readiness.
- Subagents must receive bounded packets and must not infer real-world sign-off from public availability.

## Public No-Go Rule

Public release is a communications and transparency state only. It must not be used as evidence that Bristol City Council, WECA/MCA, DfT, the Secretary of State, any officer, any legal adviser or any consultant has approved or endorsed the scheme.

It must also not be described as an official council publication unless a future real-world process replaces the simulation controls with council communications, democratic services, legal and information-governance clearance.

## Validation

Run:

```bash
python3 scripts/validate_public_release.py
make public-release-qa
make validate
```

Expected result: public-release QA passes while WPL approval gates remain blocked.

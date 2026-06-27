# Stage 32A WECA OBC/FBC Exemplar Corpus

Status: simulation-control artefact.  
Date: 2026-06-27.  
Owner: Programme Orchestrator.

## What This Adds

Stage 32A turns the repo's WECA-facing business-case evidence into a usable comparator corpus for simulated Bristol WPL OBC drafting.

The corpus now includes:

- full downloaded WECA source documents: `SRC-WECA-0008` and `SRC-WECA-0009`;
- WECA-facing OBC/FBC route examples embedded in Bristol committee/minute evidence: `SRC-BCC-0036` and `SRC-BCC-0015`;
- a WECA programme-line example: `SRC-WECA-0027`;
- an authoring standard that tells future agents how to emulate WECA-style discipline without implying real approval.

## Controlled Finding

The evidence supports a WECA-style drafting discipline:

- front matter, document history, client/sign-off areas and report purpose;
- Five Case Model section order;
- explicit strategic context and case for change;
- appraisal method, assumptions, VFM and sensitivity treatment where evidence exists;
- financial sign-off, cost and funding-source separation;
- procurement, commercial and risk allocation sections;
- management-case governance, assurance, programme, risk, benefits and monitoring sections;
- conditional decision language where approvals, funding and delivery powers remain future or dependent.

It does not support any claim that Bristol WPL has a real OBC, a preferred option, a selected boundary, a charge, a BCR, a VFM category, consultation launch approval, WECA/MCA endorsement, DfT acceptance or Secretary of State confirmation.

## Artefacts

| Artefact | Purpose |
|---|---|
| `analysis/weca-obc-fbc-exemplars/exemplar-register.csv` | Source-by-source exemplar register with source category, line references, use and claim limits. |
| `analysis/weca-obc-fbc-exemplars/comparator-matrix.csv` | Drafting-pattern matrix mapping WECA examples to Bristol WPL controls. |
| `analysis/weca-obc-fbc-exemplars/weca-style-obc-authoring-standard.md` | Stage 32A drafting standard for the simulated OBC. |
| `evidence/source_notes/stage32a/src-weca-0008.md` | Source note for the Future4WEST SOC exemplar. |
| `evidence/source_notes/stage32a/src-weca-0009.md` | Source note for the Bristol Bridge/VMS FBC exemplar. |

## Source Limits

`SRC-WECA-0009` is the closest full WECA-facing FBC comparator. It is still not a WPL document. Its FBC structure and approvals-process language can inform the simulated OBC's document discipline, but not WPL design, legality, finance, modelling, consultation or implementation readiness.

`SRC-WECA-0008` is a Strategic Outline Case, not an OBC/FBC. It supports progression, assurance, risk, issue, benefits and monitoring conventions but not WPL scheme readiness.

`SRC-BCC-0036`, `SRC-BCC-0015` and `SRC-WECA-0027` provide route-pattern examples only. They must not be described as full OBC/FBC exemplar documents unless the source itself is the business-case document.

## Subagent Review Synthesis

The four Stage 32A lanes converged on the same conditions:

- make simulation status visible in every OBC-facing output;
- tag WECA/MCA material by trigger type and do not imply approval;
- preserve no-go status in the recommendations section;
- extend validator coverage beyond Stage 6A paths;
- add no-go rows for WECA-style overclaim and partial-exemplar overclaim;
- surface Stage 32A in README and officer navigation only after validation.

## Stage 32A Gate Effect

This corpus supports professional simulated drafting. It does not pass Stage 7 OBC, Stage 8 consultation, Stage 11 FBC/statutory, or any real-world public-authority gate.


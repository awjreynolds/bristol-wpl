# Stage 33A OBC Simulation Release

Status: complete as simulation release package only.  
Date: 2026-06-27.

## Plain-English Summary

Stage 33A ships the editable OBC simulation so a reader can open one complete Markdown document and understand the simulated Bristol WPL business case.

It does not approve anything. It does not pass the OBC gate. It does not create officer advice, procurement authority, consultation readiness, statutory readiness, WECA/MCA endorsement or WPL readiness.

## What Changed

- A simulation-release directory was added at `business_case/obc/simulation-release/`.
- The shipped OBC is `business_case/obc/simulation-release/bristol-wpl-outline-business-case-simulation-release.md`.
- The release keeps the Stage 7 no-go position visible.
- The release is separated from the blocked real-output path `business_case/obc/assembled/`.
- Registers now track the release-specific overclaim risk.

## Key Risks

| Risk | Why It Matters | Control |
|---|---|---|
| A shipped simulation OBC may look like an approved OBC. | Public readers or future agents could mistake a polished document for authority approval. | Stage 33A status formula, no-go claims and validator checks. |
| Release wording may imply procurement or consultation authority. | A WPL OBC is not a procurement engine or a consultation launch document. | README and release file state no procurement authority and no consultation readiness. |
| The release could bypass the blocked `assembled/` path. | Stage 6A and Stage 7 real-OBC assembly gates remain blocked. | Release uses `simulation-release/`, not `assembled/`. |

## Gate Decision

Accepted for simulation-release use only.

Stage 7 OBC gate, Stage 8 consultation gate and Stage 11 FBC/statutory gate remain blocked.

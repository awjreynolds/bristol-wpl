# Stage 15A Source Note Expansion Review

Status: simulated evidence, legal/governance and red-team review with conditions.  
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 15A expands source-note coverage for the highest-risk legal and Bristol governance material without implying that evidence review, legal clearance, OBC readiness, FBC readiness or statutory assurance is complete.

## Findings

| Finding | Severity | Response |
|---|---|---|
| The legal/governance source base carried the highest overclaim risk because it can be mistaken for authority to proceed. | P1 | Stage 15A adds 42 expanded notes and validator coverage for those sources. |
| Raw Bristol public packs omitted from the public repo need explicit source-use limits. | P1 | The relevant source notes state that raw binary reliance requires reacquisition and logged controls. |
| Legal source notes can look like legal opinions. | P1 | Notes and registers state that they are source-use controls only and do not replace legal review. |
| The wider source-note backlog remains open. | P1 | `ISS-0007`, `EG-0024`, `EG-0038` and new `EG-0043` remain controlled open. |

## Red-Team Challenge

| Challenge | Severity | Resolution |
|---|---|---|
| A reader may see 55 source notes and assume evidence due diligence is complete. | P1 | README, stage index, coverage register, gate report and validator wording preserve the partial-cohort boundary. |
| A legal agent may use the legislation notes to sign off the statutory route. | P1 | Notes ban legal-clearance claims and the gate report keeps Bristol, WECA/MCA, DfT and statutory blockers open. |
| Future agents may cite source notes instead of the underlying source. | P2 | `CB-0021` and `REQ-0035` require source IDs, source locations and reviewer checks before drafting reliance. |

## Decision

Simulation sign-off with conditions for expanded source-note controls only.

Stage 15A does not complete evidence review, verify business-case claims, approve an OBC/FBC, replace legal advice or close any WPL gate.

## Conditions

| Condition | Owner | Trigger | Closure Route |
|---|---|---|---|
| Keep `ISS-0007`, `EG-0024`, `EG-0038` and `EG-0043` open until every acquired priority source has a reviewed note. | Evidence Librarian | Any claim that source-note coverage is complete | Complete remaining source-note cohorts, run source-note QA and record Simulation Gate Authority closure. |
| Do not use Stage 15A legal notes as legal sign-off. | Legal Review Agent | Legal, statutory, OBC, FBC or consultation drafting cites a source note as clearance | Replace with source-law citation, route memorandum, simulated legal review and later real-world legal review. |
| Add claim-level source summaries before high-confidence drafting. | Evidence/Citation Agent | A high-materiality claim is drafted from source-note text | Add claim matrix row with source IDs, source locations, reviewer status and limitations. |

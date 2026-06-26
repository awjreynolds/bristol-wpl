# Stage 15B Source Note Completion Review

Status: simulated evidence, WECA, appraisal, comparator and red-team review with conditions.  
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 15B completes source-note coverage for downloaded priority-1 sources without creating false claims about legal clearance, WECA/MCA approval, DfT process closure, appraisal compliance, comparator transferability, OBC/FBC readiness, consultation readiness or statutory submission readiness.

## Findings

| Finding | Severity | Response |
|---|---|---|
| The Stage 15B cohort covers the remaining downloaded priority-1 WECA/MCA, appraisal, DfT, Nottingham and UK comparator sources. | P1 | 36 Stage 15B notes are added under `evidence/source_notes/stage15b/`, and the validator checks that no downloaded priority-1 source is missing coverage. |
| WECA/MCA sources are vulnerable to overread silence or context as approval, consent, no-role status or funding support. | P1 | WECA/MCA notes now require wording that absence of WPL material is not proof that no WECA record exists elsewhere. |
| DfT search snapshots are vulnerable to overread as proof that no process exists. | P1 | `SRC-DFT-0003` and `SRC-DFT-0004` are treated as bounded search-control sources only. |
| HMT/DfT method guidance is vulnerable to overread as Green Book/TAG compliance, VFM acceptance or OBC/FBC readiness. | P1 | HMT/DfT notes include method-only wording and the validator checks for no-compliance and no-VFM caution text. |
| Nottingham, TfL and Leicester comparator sources are vulnerable to unsupported transfer to Bristol. | P1 | Comparator notes require Bristol-specific transferability evidence before using mode-share, elasticity, congestion, revenue, charge level, employer behaviour, acceptability, deliverability or statutory applicability assumptions. |
| Source-note coverage can sound like evidence completion. | P1 | `EG-0044`, `ISS-0025`, `RISK-0028`, `PIT-0022` and public/officer docs preserve the claim-level summary gap. |

## Red-Team Challenge

| Challenge | Severity | Resolution |
|---|---|---|
| A reader may treat `ISS-0007` closure as OBC/FBC evidence readiness. | P1 | The gate report accepts Stage 15B only for acquired-priority source-note completion and leaves `EG-0044` open. |
| A future legal agent may use WECA legislation or meeting pages to assert no WECA role. | P1 | The source notes and validator block no-role and absence-of-record inferences. |
| A future appraisal agent may treat generic HMT/DfT guidance as proof of appraisal compliance. | P1 | Method notes explicitly block Green Book/TAG compliance, BCR and VFM claims. |
| A future public summary may cite Nottingham outcomes as likely Bristol outcomes. | P1 | Comparator notes and Nottingham lessons controls require Bristol-specific transferability review. |

## Decision

Simulation sign-off with conditions for acquired-priority source-note completion only.

Stage 15B does not complete claim-level source summaries, verify business-case claims, provide legal advice, approve an OBC/FBC, settle WECA/MCA or DfT positions, prove appraisal compliance, transfer comparator findings or close any WPL readiness gate.

## Conditions

| Condition | Owner | Trigger | Closure Route |
|---|---|---|---|
| Keep `EG-0044` open until claim-level source summaries exist. | Evidence/Citation Agent | Any high-materiality claim is drafted from source-note text | Create claim summaries with source IDs, source locations, reviewer status and limitations. |
| Keep WECA/MCA role and DfT process blockers open. | Legal Review Agent and WECA Governance Agent | Any claim of approval, consent, no-role status, DfT acceptance or Secretary of State readiness | Replace with source-supported legal route memorandum and logged DfT/WECA disposition. |
| Keep appraisal and comparator transfer controls open. | Appraisal Guidance Agent and Comparator Evidence Agent | Any BCR, VFM, model, mode-shift, congestion, revenue or employer-response claim | Complete appraisal evidence, model assurance and Bristol-specific transferability assessment. |

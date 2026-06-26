# Stage 16A Claim Summary Control Review

Status: simulated evidence, legal/governance, appraisal/comparator, public/officer and red-team review with conditions.  
Date: 2026-06-26.

## Review Scope

This review tests whether Stage 16A creates a claim-level source-summary layer for the current claim matrix without converting summaries into claim truth, legal advice, OBC/FBC evidence completion, consultation readiness, statutory readiness or implementation readiness.

## Findings

| Finding | Severity | Response |
|---|---|---|
| Claim summaries can be mistaken for claim verification. | P1 | Every summary states it is simulation-only, does not prove the claim is true and must not replace underlying source review. |
| `verified_simulation` can be mistaken for real-world assurance. | P1 | Summaries preserve the matrix status but state that later human professional review is still required before real-world reliance. |
| Claims without source IDs are high-risk. | P1 | Blank-source summaries are labelled as absence/control claims and must not backfill invented source IDs. |
| Legal, WECA/MCA and DfT summaries could leak into route closure or statutory readiness. | P1 | Legal/governance summaries include no-go wording for legal advice, Bristol route, WECA/MCA and DfT status. |
| Appraisal and comparator summaries could leak into BCR, VFM, model or Bristol-transferability claims. | P1 | Appraisal and comparator summaries include Green Book/TAG, BCR, VFM and Bristol-transferability no-go wording. |
| Future drafting claims are not covered by the current matrix. | P1 | `EG-0045` remains open for future OBC, FBC, consultation, statutory and public/officer drafting-specific claims. |

## Red-Team Challenge

| Challenge | Severity | Resolution |
|---|---|---|
| "Summary complete" may become "evidence complete." | P1 | The validator and gate report use "claim-summary control only" wording and block evidence-complete claims. |
| Source-note coverage and claim summaries may combine into a false OBC/FBC readiness impression. | P1 | Stage 16A public/officer wording separates source notes, claim summaries and readiness gates. |
| Currentness may be inferred from summary date. | P2 | Every summary requires source currentness to be rechecked before real-world reliance. |
| Context bloat could return if summaries paste raw evidence. | P2 | Summaries stay compact and cite source IDs and source locations rather than raw excerpts. |

## Decision

Simulation sign-off with conditions for Stage 16A claim-summary control purposes only.

Stage 16A creates an editable claim-level source-summary layer for existing claims in the claim evidence matrix. It reduces citation drift and drafting overclaim risk. It does not verify claim truth, complete the evidence base, provide legal advice, settle Bristol/WECA/MCA/DfT positions, prove Green Book/TAG compliance, establish Nottingham transferability, assemble an OBC/FBC, launch consultation, authorise statutory submission or change the current no-go position.

## Conditions

| Condition | Owner | Trigger | Closure Route |
|---|---|---|---|
| Keep `EG-0045` open for future drafting-specific claims. | Evidence/Citation Agent | Any new OBC, FBC, consultation, statutory or public/officer claim is drafted | Add or update a claim matrix row and claim summary with source IDs, source locations, reviewer status and limitations. |
| Preserve legal, WECA/MCA and DfT blockers. | Legal Review Agent and WECA Governance Agent | Any summary is cited as route closure | Replace with source-supported route memorandum, logged DfT/WECA disposition and later real-world legal review. |
| Preserve appraisal and comparator blockers. | Appraisal Guidance Agent and Comparator Evidence Agent | Any summary is cited for BCR, VFM, mode shift, congestion, revenue or transferability | Complete appraisal evidence, model assurance and Bristol-specific transferability assessment. |

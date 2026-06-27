# Stage 28A Context: Bristol Live Public Source Coverage

Status: context packet for Stage 28A.  
Date: 2026-06-27.

## Trigger

The user asked whether these Bristol WPL links brought relevance or were already tracked:

- `https://www.bristol.gov.uk/residents/streets-travel/transport-plans-and-projects/workplace-parking-levy`
- `https://news.bristol.gov.uk/press-releases/ba17de24-32b0-46ce-80b6-3d629d6eade1/further-information-bristol-workplace-parking-levy`
- `https://www.bristolpost.co.uk/news/bristol-news/bristol-workplace-parking-levy-could-11025667`

Stage 28A answers that question by creating a visible source-status control rather than relying on buried source-register rows.

## Findings

| URL | Repo status | Finding |
|---|---|---|
| Bristol project page | `SRC-BCC-0001` | Already registered, downloaded, extracted, source-noted and recorded in the liveness register. It is official public narrative only. |
| Bristol news release | `SRC-BCC-0002` | Already registered, downloaded, source-noted and recorded in the liveness register. Extraction is script-placeholder limited and it is communications context only. |
| Bristol Post article | `SRC-BCC-0020` | Already registered as seeded media context but not downloaded, extracted, source-noted or liveness-recorded. Browser fetch returned `402 Payment Required` on 2026-06-27. |

## Subagent Review Inputs

Source coverage review confirmed the three URLs map to `SRC-BCC-0001`, `SRC-BCC-0002` and `SRC-BCC-0020`. It recommended reconciling source-register status, acquisition status, extraction status, source-note status and liveness/access status.

Public navigation review recommended surfacing the result in the root README and `docs/public/source-link-and-freshness-status.md`, with a dedicated Bristol public-source table.

Red-team review required strong no-overclaim wording: public-source coverage is not exhaustive source discovery, source truth, formal approval, media verification, currentness or WPL readiness.

## Decision Boundary

Stage 28A is a public-source coverage and claim-boundary control. It is not a new source acquisition stage and does not create substantive Bristol WPL claims.

## Residual Blockers

- `ISS-0038`: public-source coverage can be mistaken for source truth, exhaustive discovery, formal decision evidence or WPL readiness.
- `RISK-0041`: source visibility can be over-read as authority, currentness, press/media accuracy or decision-grade sufficiency.
- `EG-0056`: source-type and access-state classification does not verify content truth, content completeness, paywalled content, source authority, formal decision status or claim sufficiency.

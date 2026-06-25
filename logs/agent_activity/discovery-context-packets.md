# Discovery Context Packets

Date: 2026-06-25  
Mode: full simulation  
Shared constraints: do not edit files; do not invent evidence; cite source IDs or official URLs; state unavailable sources as gaps; simulation sign-off has no real-world effect.

## Packet D1: Current Law / Statutory Route

Question: What is the initial statutory route for a Bristol WPL simulation, and what legal sources/questions control Stage 2?

Inspect:
- `CODEX_MASTER_PROMPT.md`
- `evidence/source_register.csv`
- rows with `SRC-LEG-*`, `SRC-DFT-*`, Bristol governance rows and WECA governance rows
- official legislation sources where accessible

Acceptance criteria:
- distinguish initial order, variation, revocation and RPI-only variation;
- separate DfT engagement from Secretary of State/appropriate national authority confirmation;
- identify P0/P1 legal questions;
- output standard handover with simulation sign-off decision.

## Packet D2: Bristol Decision / Governance Trail

Question: What Bristol decision trail is visible from the seed source register, and what chronology/gaps should Stage 1 test?

Inspect:
- `evidence/source_register.csv`
- `bristol_wpl_codex_sources.csv`
- Bristol governance, EqIA, public forum and related-policy rows

Acceptance criteria:
- classify formal decision, report, decision notice, public forum, EqIA, forward plan and media context separately;
- do not infer decisions from press coverage;
- identify the first chronology skeleton and evidence gaps.

## Packet D3: WECA/MCA Powers and Decision Trail

Question: What WECA/MCA role hypotheses and evidence gaps should be carried into Stage 2?

Inspect:
- `evidence/source_register.csv`
- WECA/MCA strategy, assurance, business-case example and mass-transit rows
- `CODEX_MASTER_PROMPT.md` sections on WECA/MCA

Acceptance criteria:
- classify formal approval, assurance, adopted strategy, officer collaboration, public statement and no evidence found;
- distinguish strategic alignment from formal support;
- identify current-law/current-constitution verification needs.

## Packet D4: Green Book / DfT / TAG Assurance Spine

Question: What appraisal and business-case standards should control the SOC-equivalent, OBC, FBC and ASR stages?

Inspect:
- `CODEX_MASTER_PROMPT.md`
- `evidence/source_register.csv` DfT and WECA assurance rows
- current official guidance where accessible

Acceptance criteria:
- cover SOC-equivalent preferred way forward, OBC, FBC, ASR/ASST, TAG uncertainty, Green Book metrics, VfM and reappraisal triggers;
- identify P0/P1 assurance risks.

## Packet D5: Nottingham and UK Comparator Evidence

Question: What comparator evidence is available in the seed list, and how should transferability be controlled?

Inspect:
- Nottingham, UK precedent, academic, trade/media rows in `evidence/source_register.csv`
- relevant comparator instructions in `CODEX_MASTER_PROMPT.md`

Acceptance criteria:
- separate official claims, audited data, peer-reviewed/independent evidence and media;
- identify transferability dimensions and causal-claim controls.

## Packet D6: Spatial, Parking Inventory and Data Requirements

Question: What spatial/data foundations are needed before options appraisal?

Inspect:
- `CODEX_MASTER_PROMPT.md` spatial, parking inventory, model and data sections
- `evidence/source_register.csv` for sources relevant to boundary, parking base, Nottingham implementation and data governance

Acceptance criteria:
- define boundary, parking inventory, data model, reproducibility and privacy controls;
- identify P0/P1 data/spatial gaps.

## Packet D7: Five Case and Statutory Dossier Architecture

Question: Is the generated repository architecture sufficient to keep OBC, FBC, statutory dossier and evidence dependencies aligned?

Inspect:
- `CODEX_MASTER_PROMPT.md`
- generated directories and registers
- `statutory_dossier/business_case_to_statutory_crosswalk.csv`
- `business_case/` structure

Acceptance criteria:
- identify crosswalk needs, document assembly order, stage-gate dependencies and context-management controls;
- recommend immediate file outputs for synthesis.

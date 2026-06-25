# Startup Report

**Date:** 2026-06-25  
**Mode:** Full simulation with agentic simulation sign-offs.  
**Status:** Stage 0 bootstrap/discovery baseline completed with conditions.

## Environment

```json
{
  "python": "3.14.5",
  "platform": "macOS-15.5-arm64-arm-64bit-Mach-O",
  "pandoc": true,
  "git": true,
  "zip": true,
  "pytest": false,
  "openpyxl": false,
  "pyyaml": false,
  "git_branch": "main",
  "git_dir": ".git",
  "git_common_dir": ".git"
}
```

## Bootstrap Outputs

- Repository architecture created.
- Root and local `AGENTS.md` instructions created.
- Master prompt copied to `instructions/00-operating-model.md`.
- Seed CSV copied to `inputs/bristol_wpl_codex_sources.csv`.
- `evidence/source_register.csv` created with 44 seed rows.
- Baseline registers, schemas, templates and validation scripts created.
- Minimal XLSX officer views created for source and risk registers using standard-library generation.
- Portable authoring pack refreshed.

## Discovery Agents

Seven bounded read-only discovery agents completed:

- D1 current law/statutory route;
- D2 Bristol decision/governance trail;
- D3 WECA/MCA powers and decision trail;
- D4 Green Book/DfT/TAG/assurance spine;
- D5 Nottingham and comparator evidence;
- D6 spatial, parking inventory and data requirements;
- D7 Five Case and statutory dossier architecture.

Handover synthesis is recorded in `logs/agent_activity/discovery-handover-summary.md`.

## Simulation Sign-Offs

`governance/simulation_signoff_register.csv` records conditional simulation sign-offs for D1-D7. These have no real-world legal, statutory, financial or professional effect.

Overall Stage 0 decision: simulation sign-off with conditions.

## Validation

Fresh validation run:

- `python3 scripts/validate_registers.py` passed.
- `python3 -m unittest discover -s tests` ran 9 tests and passed.
- `make validate` passed.

## Blockers And P0/P1 Risks

P0 blockers before Stage 2 or preferred scheme design:

- Bristol licensing authority/delegation route unresolved.
- WECA/MCA current statutory role, consent or assurance dependency unresolved.
- Initial order submission and Secretary of State confirmation route not settled.
- DfT engagement must not be confused with statutory confirmation.
- Authoritative boundary and lawful parking-base data absent.

P1 risks:

- Guidance snapshots are not yet acquired into `evidence/raw/**`.
- Comparator evidence is not acquired or reviewed.
- Parking inventory schema is placeholder-level.
- OBC/FBC assembly scripts are placeholders.

## Immediate Next Stage

Proceed to Stage 1 evidence acquisition and Stage 2 legal/governance route work before any OBC/FBC drafting.

Priority outputs:

- acquire and hash current legal, Bristol, WECA/MCA, DfT/TAG and comparator sources;
- populate legal compliance matrix and statutory crosswalk;
- complete `statutory_dossier/statutory_route_note.md`;
- run Legal Review Agent simulation sign-off on Stage 2;
- replace placeholder parking-inventory schema;
- create ASR/ASST control checklist.

## Decisions Required From Project Owner

1. Whether to allow networked source acquisition from the seed URLs in the next stage.
2. Whether to keep all raw official PDFs under `evidence/raw/**` when no official HTML/DOCX source exists.
3. Whether to prioritise legal/governance route work before Bristol chronology extraction.
4. Whether to model the simulated scheme as Bristol-only unless Stage 2 proves a WECA/MCA or joint route.
5. Whether to treat the July 2026 OBC decision point as future/planned until official records are acquired.

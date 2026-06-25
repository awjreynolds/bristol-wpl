# Startup Report

**Date:** 2026-06-25  
**Mode:** Full simulation with agentic simulation sign-offs.  
**Status:** Stage 0 bootstrap/discovery baseline completed with conditions. Stage 1 source acquisition and simulated assurance completed with conditions.

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

## Stage 1 Addendum

Stage 1 acquired and extracted priority evidence, added whole-instrument statutory sources, added later Bristol decision/minute/EqIA sources, generated source term scans, expanded legal/statutory controls, created editable OBC/FBC/statutory Markdown templates and upgraded spatial/operations schemas.

Current evidence state:

- `evidence/source_register.csv`: 67 rows.
- Downloaded and extracted: 49 sources.
- Seeded but not downloaded: 17 sources.
- Failed acquisition: 1 source (`SRC-ACADEMIC-0001`).
- Current extraction state: `evidence/extraction_manifest.csv`.

Stage 1 gate report:

- `review/stage_gate_reports/stage-1-source-acquisition-and-simulated-assurance-report.md`

Stage 1 simulated assurance:

- Legal/statutory powers: simulation sign-off with conditions.
- Bristol governance: simulation sign-off with conditions.
- WECA/MCA governance: simulation sign-off with conditions.
- Appraisal/TAG assurance: simulation sign-off with conditions.
- Comparator evidence: simulation sign-off with conditions.
- Spatial/data/operations/enforcement: simulation no-go.

Current hard stop:

No OBC/FBC assembly, preferred scheme, statutory consultation launch, operational readiness or statutory submission readiness is supported until Stage 2 legal/governance, Stage 4 spatial/data and Stage 5 appraisal/model controls are closed.

## Immediate Next Stage

Proceed to Stage 1 evidence acquisition and Stage 2 legal/governance route work before any OBC/FBC drafting.

Priority outputs:

- resolve Bristol licensing authority, order-maker and delegation route;
- resolve current WECA/MCA role and any assurance/funding dependency;
- complete source notes for acquired priority evidence;
- produce the ASR/OAR/ASST control pack and model-card framework;
- acquire authoritative boundary, address/premises and parking-base data sources with licences;
- produce DPIA scope, lawful-basis analysis and data-flow map;
- create licensing/enforcement operating procedures, PCN templates, representation workflow, appeals/recovery procedure and service policy.

## Decisions Required From Project Owner

1. Whether to keep acquiring lower-priority seeded sources now or defer until source notes for priority sources are complete.
2. Whether to prioritise Bristol constitution/delegation and WECA/MCA current-law role before any additional drafting.
3. Whether to begin source-note production manually or create a scripted source-note skeleton generator.
4. Whether to model the simulated scheme as Bristol-only unless Stage 2 proves a WECA/MCA or joint route.
5. Whether to treat July 2026 OBC and October 2026 FBC decision points as future/planned until official records are acquired.

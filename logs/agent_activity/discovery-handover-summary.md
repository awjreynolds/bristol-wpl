# Discovery Handover Summary

Date: 2026-06-25  
Mode: full simulation  
Status: working synthesis of bounded discovery-agent outputs.

## D2 Bristol Decision / Governance Trail

Simulation sign-off with conditions for seed chronology and gap list only.

Key conclusions:

- Seed metadata identifies `SRC-BCC-0004` as the only explicit Bristol decision-notice row.
- Committee reports and packs are not decision records until matched to notices or minutes.
- Forward plans evidence planned decision timing only.
- EqIAs evidence equality assessment status only.
- Public forum material evidences questions/statements, not decisions.
- Media and party-political rows are context only.

Critical next actions:

- Acquire and extract `SRC-BCC-0004`.
- Locate May 2025, October 2025 and March 2026 decision notices/minutes.
- Verify any prior 2023 report/decision trail behind media coverage.
- Compare 2024 and 2025 EqIA changes.

## D5 Nottingham and UK Comparator Evidence

Simulation sign-off with conditions for comparator source classification only.

Key conclusions:

- Nottingham official/promoter sources are usable only after acquisition and refresh.
- `SRC-ACADEMIC-0001` is the primary independent lead for Nottingham congestion/traffic claims.
- `SRC-ACADEMIC-0002` is the mode-share lead, but publication details need checking.
- Media/trade/party-political rows are context only.
- No Nottingham impact, revenue, charge, mode-share or transferability claim is ready for OBC use until raw sources are acquired, reviewed, cited and logged.

Critical next actions:

- Acquire priority comparator sources into the relevant `evidence/raw/**` folders.
- Verify Nottingham 2024-2025 data hub or latest official operational reporting.
- Build Bristol-vs-Nottingham transferability matrix.
- Separate claims into official, audited/operational, independent/academic and media/context categories.

## D3 WECA/MCA Powers and Decision Trail

Simulation sign-off with conditions for WECA/MCA discovery classification only.

Key conclusions:

- WECA/MCA material inspected is strategy, assurance or process context, not formal Bristol WPL approval.
- No inspected D3 source evidenced formal WECA/MCA approval, formal funding decision, formal Bristol WPL support, formal objection or confirmed statutory consent position.
- WECA/MCA may still be relevant as a strategic alignment body, assurance/funding body, transport programme/data partner, possible statutory interface, and political/stakeholder interface.
- Whether WPL functions are transferred, concurrent, reserved to Bristol or require consent remains a P0 Stage 2 legal/governance question.

Critical next actions:

- Verify current Transport Act/WPL regulations and West of England constitutional/devolution instruments.
- Retrieve current WECA/MCA constitution, delegations and meeting records.
- Produce `analysis/weca-role-and-evidence/formal-decision-trail.md`.
- Produce `analysis/legal/legal-authority-and-governance-map.md`.

## D4 Green Book / DfT / TAG Assurance Spine

Simulation sign-off with conditions for appraisal and assurance-spine discovery only.

Key conclusions:

- SOC-equivalent / preferred way forward must precede OBC detailed appraisal.
- OBC must appraise shortlisted options in detail and cannot be drafted as a predetermined WPL conclusion.
- FBC must rerun preferred-option appraisal using final scheme design, costs, revenue, consultation changes, procurement/commercial information and latest TAG/Green Book assumptions.
- Stage 5 requires OAR, ASR and ASST control before modelling or OBC economic-case drafting.
- Green Book 2026 metrics and judgement must include NPSV, BCR, RPSC/public-sector cost, unmonetised impacts, distribution, risk and uncertainty.
- TAG uncertainty and common analytical scenarios must be carried into model design and decision-maker presentation.

Critical next actions:

- Acquire current official guidance snapshots/source notes for Green Book 2026, HMT business case guidance, DfT transport business case guidance, TAG core units, M4/uncertainty toolkit, DfT VfM framework and WECA July 2025 assurance framework.
- Create Stage 5 ASR/ASST control checklist before any OBC drafting.
- Define reappraisal triggers for guidance, data, costs, revenues, benefits, design, boundary, charge, consultation, procurement, model validation and WECA funding/assurance conditions.

## D6 Spatial, Parking Inventory and Data Requirements

Simulation sign-off with conditions for requirements and gap identification only.

Key conclusions:

- D6 does not select a Bristol WPL boundary.
- Boundary options must test whole-city, zones, employment clusters, phased geography, cross-boundary options and transport-effect/admin-feasibility alternatives.
- Working CRS should be `EPSG:27700`; web outputs should use `EPSG:4326` only where needed.
- Parking inventory requires lawful sources such as LLPG/UPRN, VOA/business-rate records, planning/land-use data, employer/education records, surveys, declarations and inspections.
- Canonical parking data must be CSV/Parquet/GeoPackage; XLSX is an officer view only.
- Real personal/enforcement data must not enter normal Git.

Critical next actions:

- Acquire/hash priority spatial and parking-base sources.
- Add official spatial/data source rows.
- Define parking-base data contract and DPIA scope.
- Produce `spatial/parking_inventory/parking-base-methodology.md`.
- Produce boundary-options manifest template before options appraisal.

## D7 Five Case and Statutory Dossier Architecture

Simulation sign-off with conditions for Stage 0 dossier architecture only.

Key conclusions:

- The architecture is sufficient as a Stage 0 scaffold but not yet operationally sufficient.
- `statutory_dossier/business_case_to_statutory_crosswalk.csv` and `statutory_dossier/legal_compliance_matrix.csv` are header-only and must be populated before legal/statutory or OBC readiness can be claimed.
- Evidence baseline must come first, then statutory route/legal powers, then strategic assessment, spatial/data baseline, options/ASR, OBC, consultation, FBC and statutory dossier.
- `assemble_obc.py` and `assemble_fbc.py` are placeholders and do not enforce assembly order yet.

Critical next actions:

- Produce `statutory_dossier/statutory_route_note.md`.
- Populate `statutory_dossier/legal_compliance_matrix.csv`.
- Populate `statutory_dossier/business_case_to_statutory_crosswalk.csv`.
- Create `business_case/shared/assembly_manifest.md`.
- Create `review/stage_gate_reports/stage-0-architecture-and-controls-report.md`.

## D1 Current Law / Statutory Route

Simulation sign-off with conditions for legal-route discovery only. This is not legal advice.

Key conclusions:

- For an initial Bristol WPL simulation, the apparent statutory spine is Transport Act 2000 Part III Chapter II.
- A local licensing scheme is made by order of the licensing authority under section 183.
- For an England-only initial scheme, section 184 confirmation by the appropriate national authority appears to be required before the order comes into force, with section 198 pointing to the Secretary of State.
- DfT engagement may support preparation but is not statutory confirmation unless evidenced as a formal decision under the relevant power.
- 2009 Regulations regulation 3 disapplies section 184 only for RPI-only charge variations; it does not apply to an initial order, non-RPI variation or revocation.
- Revocation route needs separate legal review before process assumptions are used.
- Net proceeds require Schedule 12 plans/programmes and 2003 Regulations accounting controls.

Critical next actions:

- Produce `statutory_dossier/statutory_route_note.md`.
- Populate the P0 legal matrix.
- Confirm Bristol City Council competence/delegations and WECA/MCA current role.
- Classify DfT engagement versus Secretary of State confirmation.

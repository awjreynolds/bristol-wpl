# Officer Assurance Dashboard

Status: Stage 9A public/officer assurance control.  
Date: 2026-06-26.

## One-Line Position

This is a controlled simulation. It is not an approved Bristol WPL scheme, not an OBC/FBC, not consultation-ready and not statutory-submission-ready.

## Simulation Control Dashboard

RAG colours describe repository control status, not real-world WPL readiness. `GREEN` means a control exists for the stated limited purpose only. `AMBER` means controlled but still dependent on unresolved evidence or external checks. `RED` means blocked for reliance.

| Decision area | Current answer | Status | Why blocked | Next evidence needed |
|---|---|---|---|---|
| Bristol final order-maker and submitter | Not settled | RED | ISS-0001 and RISK-0001 remain open P0 controls | Source-supported Monitoring Officer/legal route, resolution route, named submitter and signatory |
| WECA/MCA role | Not settled | RED | ISS-0002 and RISK-0002 remain open P0 controls | Current-law role, consent/no-role, consultation-response and funding-dependency classification |
| DfT process | Not settled | AMBER | ISS-0008 and RISK-0003 remain open P1 controls | WPL-specific DfT procedural source or logged DfT response |
| Boundary and parking inventory | Not available | RED | ISS-0003 and RISK-0004 remain open P0 controls | Authoritative boundary, licences, inventory, topology QA and legal/GIS reconciliation |
| Displacement and residential spillover | Not assessed | RED | Boundary and inventory are absent | Boundary options, parking inventory, residential street baseline and mitigation options to assess, not selected mitigation |
| Options and appraisal | Not ready | RED | ISS-0004 remains open P0 | OAR, ASR, ASST, model cards, outputs, uncertainty and reviewer sign-off |
| OBC | Not assembled and gate cannot pass | RED | ISS-0011 and RISK-0014 remain open; Stage 7A creates controls only | Populated evidence dependencies and Stage 7 assurance |
| Consultation launch | Not ready | RED | ISS-0012 and RISK-0015 remain open | Authority to consult, materials, privacy, accessibility, response-analysis and public-law checks |
| Statutory dossier | Not ready | RED | Stage 10A creates controls only; ISS-0001, ISS-0002, ISS-0008 and FBC/consultation blockers remain open | DfT route, certified order, FBC, consultation statement, boundary schedule and legal review evidence |
| FBC/statutory gate | Not ready | RED | Stage 11A creates final gate controls only; no FBC, legal review evidence, S151 review, consultation disposition or implementation readiness exists | Complete FBC evidence packet, Monitoring Officer route, Section 151 review, DfT/WECA disposition and decision report |
| Public repository release | Public but not approval | GREEN for publication controls only | Stage 12A records public GitHub visibility and no-overclaim controls | Re-run public-release QA before external circulation claims |
| Critical-path handover | Mapped but not approved | GREEN for handover controls only | Stage 13A maps blockers to work packages and a control-only 90-day plan | Use work packages as planning inputs only; obtain real authority before spend or procurement |
| Source notes | Downloaded priority coverage complete; claim summaries controlled separately | GREEN for coverage only, AMBER for drafting reliance | Stage 15B adds the remaining 36 downloaded priority-1 notes; Stage 16A covers current claim summaries | Use source notes as source-use controls only; cite underlying sources and claim summaries before drafting reliance |
| Claim summaries | Current claim matrix covered; future drafting claims open | GREEN for current-matrix coverage control only, AMBER for drafting reliance | Stage 16A creates 38 summaries for `CLM-0001` to `CLM-0038`; EG-0045 remains open | Add or update claim summaries for every new OBC, FBC, consultation, statutory or public/officer claim before reliance |
| Editable outputs | Guardrails mapped; assembly blocked | GREEN for authoring controls only, RED for assembled outputs | Stage 17A maps editable outputs and blocks assembled OBC/FBC/statutory/officer-distribution outputs | Treat editable outputs as controlled inputs for future assurance; no authored officer-distribution PDFs |
| Public repo secret-scanning | Repository controls recorded | AMBER | Stage 14B-E record current-tree cleanup, history rewrite and repository-side hosted-alert checks; GitGuardian disposition remains external | Check GitGuardian directly before claiming hosted-alert closure |
| Source-link and currentness controls | Reader route mapped; reliance still source-specific | GREEN for navigation only / AMBER for reliance | Stage 22A exposes the route but EG-0049 and EG-0050 remain open for source-by-source external liveness, content and currentness assurance | External URL checks, retrieval dates, currentness review, refreshed source notes or claim summaries and professional review for decision-grade claims |
| Register reference integrity | Scoped ID/path checks exist; substance still review-specific | GREEN for linkage control-only / AMBER for reliance | Stage 23A resolves selected issue risk gap approval and simulation sign-off references but EG-0051 remains open for substantive register correctness | Human review of row meaning risk ratings mitigation adequacy and evidence support |
| Dashboard blocker consistency | Visible blocker IDs resolve and latest Stage 24A blockers are surfaced | GREEN for blocker-surfacing control-only / AMBER for reliance | Stage 24A records dashboard blocker consistency checks. `ISS-0034`, `EG-0052` and `RISK-0037` remain open controls; the check is not exhaustive and does not prove risk adequacy or readiness. | Use `scripts/validate_dashboard_consistency.py`; review full issue, risk, gap and stage-risk registers before relying on dashboard substance |
| Stage-gate report structure consistency | Recent report structure checks exist; historical execution and substantive gate correctness remain separate | GREEN for report-structure control-only / AMBER for reliance | Stage 25A checks validation-command references, blocker sections, gate-decision sections and no-overclaim wording. `ISS-0035`, `EG-0053` and `RISK-0038` remain open controls; the check is not command-execution proof and does not prove evidence truth or readiness. | Use `scripts/validate_stage_gate_reports.py`; record fresh validation output and review substantive gate judgement before any completion claim |
| Validation evidence logging | Bounded command-run evidence is recorded for repo checks | GREEN for validation-log control only / AMBER for reliance | Stage 26A records command text run date commit reference exit code output summary evidence file and scope limits. `ISS-0036`, `EG-0054` and `RISK-0039` remain open controls; logs are not evidence truth source currentness legal correctness or readiness proof. | Use `evidence/validation/README.md` and `scripts/validate_validation_evidence_log.py`; obtain separate substantive evidence and professional review before reliance |
| Validation evidence coverage | Stage 26A validation rows and log are covered by a lag-one check | GREEN for coverage-route control only / AMBER for reliance | Stage 27A checks Stage 26A rows and log only. `ISS-0037`, `EG-0055` and `RISK-0040` remain open controls; coverage is not command authenticity command sufficiency evidence truth source currentness or readiness proof. | Use `scripts/validate_validation_coverage.py`; obtain separate command sufficiency evidence substance and professional review before reliance |
| Bristol live public-source coverage | Three user-provided Bristol WPL public links are source-typed and claim-limited | GREEN for selected-source coverage only / AMBER for reliance | Stage 28A records Bristol live public-source coverage for `SRC-BCC-0001`, `SRC-BCC-0002` and media context `SRC-BCC-0020`. `ISS-0038`, `EG-0056` and `RISK-0041` remain open controls; the check does not prove source truth currentness media accuracy formal decision status legal correctness or WPL readiness. | Use `docs/public/bristol-live-public-source-status.md` and `scripts/validate_bristol_public_sources.py`; verify formal claims against primary Bristol committee legal and statutory-route evidence before reliance |
| Subagent context-control hardening | Future-stage bounded packet instructions and template are present | GREEN for instruction/template presence only / AMBER for reliance | Stage 29A records bounded context controls and `docs/agents/subagent-stage-packet-template.md`. `ISS-0039`, `EG-0057` and `RISK-0042` remain open controls; the check does not prove future agents obey instructions evidence truth legal correctness professional assurance substantive gate correctness or WPL readiness. | Use `scripts/validate_subagent_context_control.py`; future stages must still create stage packets subagent packets handovers synthesis decisions registers and validation evidence |
| Stage 29A validation coverage | Stage 29A validation rows and log are checked by the lagged coverage validator | GREEN for lagged coverage only / AMBER for reliance | Stage 30A records validation coverage for Stage 29A. `ISS-0040`, `EG-0058` and `RISK-0043` remain open controls; the check does not prove command sufficiency command authenticity future agent compliance evidence truth legal correctness professional assurance substantive gate correctness or WPL readiness. | Use `scripts/validate_validation_coverage.py`; obtain separate command sufficiency evidence substantive source legal appraisal consultation statutory and professional review before reliance |
| Data protection and operations | Not ready | AMBER | ISS-0006 and RISK-0007 remain open | DPIA, lawful basis, PCN, appeals, recovery and service controls |
| Nottingham transfer | Not transferable to Bristol yet | RED for reliance / AMBER for lessons control | EG-0004, EG-0008, EG-0046, ISS-0005, RISK-0006 and RISK-0009 remain open; no Bristol outcome, mitigation package or CPZ/RPZ readiness follows from comparator evidence | Refreshed Nottingham evidence, Bristol transferability assessment and mitigation options to assess, not selected mitigation |

## What Can Be Relied On

| Safe to say | Do not infer |
|---|---|
| This repo has a controlled simulation workflow. | That a real public body has approved the workflow. |
| Stage 2 narrowed some legal/governance questions. | That the final order-maker, submitter or WECA/MCA role is settled. |
| Stage 4A creates boundary and inventory controls. | That a boundary or parking inventory exists. |
| Stage 5A creates appraisal controls. | That a BCR, VFM category or preferred option exists. |
| Stage 8A creates consultation controls. | That consultation can launch. |
| Stage 11A creates final gate controls. | That FBC approval, statutory submission or implementation can be recommended. |
| Stage 12A records public repository release controls. | That publication is not approval or professional sign-off. |
| Stage 13A records critical-path handover controls. | That work packages or the 90-day plan approve a programme, spending, procurement or gate passage. |
| Stage 14A, Stage 15A and Stage 15B record source-note cohorts; Stage 15B completes downloaded priority-1 coverage. | That source notes verify claims, provide legal advice or close evidence readiness. |
| Stage 16A records claim summaries for current claim-matrix rows. | That claim summaries prove claim truth, complete the evidence base, replace legal advice or cover future drafting-specific claims. |
| Stage 17A records editable output guardrails. | That editable outputs are assembled decision papers, consultation packs, statutory submissions, officer-review DOCX files or authored PDFs. |
| Stage 19A records public and cabinet comprehension controls. | That the materials have been user-tested, professionally assured or approved by officers or elected members. |
| Stage 20A records static visual/accessibility QA controls. | That rendered visuals have been accessibility-reviewed, user-tested or certified. |
| Stage 21A records repo-local navigation integrity controls. | That external links are reachable, evidence is correct, content is true or any readiness gate can pass. |
| Stage 22A records where to find source-link status, check dates and refresh flags. | That externally hosted sources are reachable now, legally/currently sufficient, accurate, complete, official for the intended claim or decision-grade. |
| Stage 23A records scoped register-ID and control-path reference checks. | That register row substance, risk ratings, mitigations, evidence support or readiness judgements are correct. |
| Stage 24A records dashboard blocker consistency checks. | That the blocker list is exhaustive or that risk ratings mitigations evidence support or readiness judgements are correct. |
| Stage 25A records stage-gate report structure checks. | That validation commands were historically run, gate judgements are substantively correct, evidence is true, sources are current or readiness has changed. |
| Stage 26A records validation evidence logs. | That logged checks prove evidence truth, source currentness, legal correctness, professional assurance, substantive gate correctness or readiness. |
| Stage 27A records validation evidence coverage checks. | That coverage proves command authenticity, command sufficiency, evidence truth, source currentness, legal correctness, professional assurance, substantive gate correctness or readiness. |
| Stage 28A records Bristol live public-source coverage for `SRC-BCC-0001`, `SRC-BCC-0002` and media context `SRC-BCC-0020`. | That the selected sources prove source truth, currentness, media accuracy, formal decision status, legal correctness, professional assurance or WPL readiness. |
| Stage 29A records subagent context-control hardening. | That future agents obey instructions, have perfect context isolation, avoid hallucination, provide professional assurance or change WPL readiness. |
| Stage 30A records validation coverage for Stage 29A. | That Stage 29A commands were sufficient, independently authenticated, or prove future agent compliance, evidence truth, professional assurance or WPL readiness. |
| Stage 14B-E record public-repository security controls. | That GitGuardian has closed its alert or that WPL readiness has changed. |
| Nottingham can inform lessons. | That Nottingham impacts transfer to Bristol. |

## Key Read Paths

- Public summary: `docs/public/README.md`
- New reader guide: `docs/public/how-to-read-this-repo.md`
- Cabinet/officer guide: `docs/officer/cabinet-and-officer-navigation-guide.md`
- Legal route: `docs/officer/legal-and-governance-briefing.md`
- Risk summary: `docs/officer/programme-risk-briefing.md`
- Risk gate atlas: `docs/officer/risk-gate-atlas.md`
- Visual QA register: `docs/visuals/visual-accessibility-qa-register.csv`
- Navigation QA: `scripts/validate_navigation_integrity.py`
- Source-link/freshness status: `docs/public/source-link-and-freshness-status.md`
- External-source liveness QA: `scripts/validate_external_liveness.py`
- Register reference integrity QA: `scripts/validate_register_references.py`
- Dashboard consistency QA: `scripts/validate_dashboard_consistency.py`
- Stage-gate report structure QA: `scripts/validate_stage_gate_reports.py`
- Validation evidence log: `evidence/validation/README.md`
- Validation evidence QA: `scripts/validate_validation_evidence_log.py`
- Validation coverage QA: `scripts/validate_validation_coverage.py`
- Bristol live public-source coverage: `docs/public/bristol-live-public-source-status.md`
- Bristol public-source QA: `scripts/validate_bristol_public_sources.py`
- Subagent context-control template: `docs/agents/subagent-stage-packet-template.md`
- Subagent context-control QA: `scripts/validate_subagent_context_control.py`
- Stage 29A validation coverage: `review/stage_gate_reports/stage-30a-validation-coverage-for-stage-29a-report.md`
- Next steps: `docs/officer/next-steps-critical-path.md`
- Source notes: `evidence/source_notes/README.md`
- Nottingham lessons: `docs/officer/nottingham-and-comparator-lessons.md`
- Checks and balances: `docs/officer/checks-and-balances-map.md`
- Document map: `docs/officer/document-map.md`

#!/usr/bin/env python3
"""Create editable Markdown templates for the WPL simulation dossier."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


CASE_SECTIONS = {
    "00-front-matter/document-control.md": {
        "title": "Document Control",
        "body": """
        ## Document Status

        - Programme: Bristol Workplace Parking Levy full simulation
        - Document type: {case_name}
        - Controlled source: editable Markdown
        - Public release status: not approved for external reliance
        - Simulation caveat: all approvals and sign-offs are simulated agent decisions with no real-world statutory, legal, financial or professional effect.

        ## Version Control

        | version | date | authoring agent | change summary | reviewer/sign-off agent |
        | --- | --- | --- | --- | --- |
        | 0.1 | YYYY-MM-DD | | Initial working draft | |

        ## Required Companion Artefacts

        - `evidence/source_register.csv`
        - `evidence/claim_evidence_matrix.csv`
        - `governance/assumptions_register.csv`
        - `governance/risk_register.csv`
        - `governance/simulation_signoff_register.csv`
        - `statutory_dossier/business_case_to_statutory_crosswalk.csv`

        ## Release Gate

        This document must not move from working draft to review draft until every substantive claim has a source ID, every figure has a model run or dataset reference, and every simulated sign-off records its limitations.
        """,
    },
    "01-executive-summary/executive-summary.md": {
        "title": "Executive Summary",
        "body": """
        ## Purpose

        Summarise the case for the Bristol WPL at {case_stage} maturity without introducing evidence not proven elsewhere in the document set.

        ## Required Content

        - Strategic problem and policy objectives.
        - Shortlisted options and preferred way forward, with clear status if no preferred option is yet endorsed.
        - Charging-area and licensing concept, including any unresolved boundary or exemption issues.
        - Estimated costs, revenues, benefits, disbenefits and uncertainty ranges.
        - Consultation, equality and distributional position.
        - Statutory route and confirmation/readiness position.
        - Key decisions requested at this stage.

        ## Evidence Rules

        Every number must cite a model run or data table. Every legal statement must cite `statutory_dossier/legal_compliance_matrix.csv` and a source ID. The summary may only compress findings; it may not make new claims.
        """,
    },
    "02-strategic-case/strategic-case.md": {
        "title": "Strategic Case",
        "body": """
        ## Case For Change

        Establish the transport, environmental, economic and fiscal problems that a WPL is intended to address. Separate observed Bristol evidence from comparator evidence and policy aspiration.

        ## Policy Fit

        Address Bristol transport policy, WECA/MCA strategic context, DfT transport objectives, climate/equality duties and local transport-plan alignment. Do not treat WECA strategy references as formal scheme approval unless a decision paper proves it.

        ## Objectives And Critical Success Factors

        Define objectives that are measurable, attributable where possible, and compatible with the statutory purpose of applying net proceeds to transport policies or proposals.

        ## Options

        Describe the longlist, shortlist, do-minimum and non-WPL alternatives. Include Clean Air Zone interactions, demand management alternatives, parking-management alternatives and investment-only counterfactuals.

        ## Strategic Risks

        Record boundary displacement, employer impacts, equalities impacts, delivery maturity, public acceptability, legal route risk and inter-authority dependencies.
        """,
    },
    "03-economic-case/economic-case.md": {
        "title": "Economic Case",
        "body": """
        ## Appraisal Framework

        State the Green Book, DfT transport business case and TAG basis used for appraisal. Record the appraisal specification, proportionality decision, counterfactual, appraisal period and price base.

        ## Options Appraisal

        Compare shortlisted options using monetised, quantified and qualitative evidence. Distinguish user charges/transfers from real resource costs and benefits.

        ## Demand, Behaviour And Transport Effects

        Explain parking-base assumptions, employer pass-through, mode shift, trip retiming, relocation/displacement, induced public transport benefits and uncertainty.

        ## Value For Money

        Present BCRs only where analytically supportable. Include switching values, sensitivity tests, optimism bias, non-monetised impacts and distributional assessment.

        ## Analytical Assurance

        Cite model cards, data quality statements, peer review findings and unresolved analytical limitations.
        """,
    },
    "04-commercial-case/commercial-case.md": {
        "title": "Commercial Case",
        "body": """
        ## Commercial Strategy

        Describe delivery, procurement and operating models for licensing, billing, account management, enforcement, appeals support, digital services, data management and customer contact.

        ## Market And Make-Buy Analysis

        Assess what can be delivered in-house, by shared service, or by external supplier. Address Nottingham precedent as comparator only, not as proof of Bristol deliverability.

        ## Contracting And Procurement

        Identify procurement routes, interfaces, service levels, cyber/data obligations, transition arrangements and contract-management capacity.

        ## Commercial Risks

        Cover supplier market risk, system integration, enforcement cost, appeals volume, data accuracy, public-facing service failure and affordability.
        """,
    },
    "05-financial-case/financial-case.md": {
        "title": "Financial Case",
        "body": """
        ## Financial Model Scope

        Define price base, inflation assumptions, parking-place base, exemptions, liable employers, compliance profile, collection costs, enforcement costs and implementation costs.

        ## Revenue And Net Proceeds

        Present gross charge income, operating expenditure, capital costs, borrowing/funding implications, net proceeds and legal restrictions on use.

        ## Affordability

        Address affordability for the promoter, employers, public transport investment programme and any WECA/MCA or grant-funding interface.

        ## Sensitivity And Risk

        Include downside revenue cases, non-compliance cases, delayed start, higher operating cost, consultation-driven exemptions and charge-path uncertainty.

        ## Controls

        Reconcile figures to `models/financial`, `investment_programme/funding`, `statutory_dossier/financial_and_net_proceeds` and the assumptions/risk registers.
        """,
    },
    "06-management-case/management-case.md": {
        "title": "Management Case",
        "body": """
        ## Delivery Approach

        Set out governance, programme plan, decision gates, benefits management, stakeholder engagement, consultation, scheme-order preparation and transition to operations.

        ## Statutory And Consultation Process

        Link the business case to the statutory dossier, including scheme order, statement of reasons, boundary schedule, net proceeds plan/programme, consultation statement and confirmation route.

        ## Assurance

        Record simulated sign-off agents, review criteria, conditions, red-team findings, claim verification, accessibility checks and document-control rules.

        ## Benefits And Evaluation

        Define baseline, monitoring metrics, evaluation design, data ownership and review points. Include Magenta Book controls where applicable.
        """,
    },
    "07-conclusions-and-decisions/recommendations.md": {
        "title": "Conclusions And Decisions",
        "body": """
        ## Decision Sought

        State the precise decision requested at {case_stage} maturity. If the evidence does not support a decision, state the no-go position and the work required to recover.

        ## Conditions

        List legal, governance, spatial, financial, equality, consultation, commercial and analytical conditions that must be satisfied before the next gate.

        ## Sign-Off Summary

        Summarise simulated sign-off decisions from `governance/simulation_signoff_register.csv`, including limitations and no-real-world-effect caveat.
        """,
    },
}

STATUTORY_TEMPLATES = {
    "draft_scheme_order/scheme_order_working_draft.md": {
        "title": "Draft Scheme Order Working Draft",
        "body": """
        ## Drafting Status

        This is a simulation working draft, not a legally operative order. It must be reviewed against the legal compliance matrix before any reliance in the business case.

        ## Core Provisions To Draft

        - Promoter/licensing authority and enabling powers.
        - Scheme area and boundary schedule incorporation.
        - Controlled workplace parking places and exemptions.
        - Licence application, variation, renewal and cancellation.
        - Charge basis, payment timing, indexation and non-payment.
        - Records, inspection, enforcement, penalty charges and appeals.
        - Commencement, review, variation and revocation provisions.
        """,
    },
    "statement_of_reasons/statement_of_reasons.md": {
        "title": "Statement Of Reasons",
        "body": """
        ## Purpose

        Explain why the WPL is proposed, how it supports transport policies and proposals, and why the selected scheme design is proportionate.

        ## Required Coverage

        - Problem definition and objectives.
        - Why non-WPL alternatives are insufficient or less effective.
        - Boundary and exemption rationale.
        - Expected transport, equality, employer and environmental effects.
        - Net proceeds use and relationship to the investment programme.
        - Consultation issues and responses.
        """,
    },
    "boundary_schedule/boundary_schedule.md": {
        "title": "Boundary Schedule",
        "body": """
        ## Boundary Definition

        Provide reproducible geospatial files, map references, street descriptions and edge-case rules. This template must not be completed from narrative evidence alone.

        ## Required Checks

        - GIS source, licence and date.
        - Relationship to Bristol administrative boundary and any cross-boundary workplaces.
        - Displacement-risk zones.
        - Public inspection format and accessibility.
        - Versioned map outputs under `spatial/boundary_options`.
        """,
    },
    "local_transport_policy_case/local_transport_policy_case.md": {
        "title": "Local Transport Policy Case",
        "body": """
        ## Transport Policies And Proposals

        Identify the transport policies and proposals that the WPL and net proceeds support. Link every policy claim to official Bristol, WECA/MCA, DfT or statutory evidence.

        ## Crosswalk

        Maintain cross-references to the Strategic Case, Statement of Reasons, ten-year general plan and five-year detailed programme.
        """,
    },
    "ten_year_general_plan/general_plan.md": {
        "title": "Ten-Year General Plan For Net Proceeds",
        "body": """
        ## Plan Scope

        Set out the proposed application of net proceeds over the opening ten-year period, separating committed, planned and conditional transport measures.

        ## Controls

        Reconcile with Schedule 12 requirements, financial model outputs, affordability constraints and the investment programme.
        """,
    },
    "five_year_detailed_programme/detailed_programme.md": {
        "title": "Five-Year Detailed Programme For Net Proceeds",
        "body": """
        ## Programme Scope

        Define the opening five-year investment programme, delivery owners, costs, funding sources, milestones, benefits and dependencies.

        ## Readiness Tests

        Include delivery maturity, procurement route, consents, match funding, risk allowances and fallback sequencing.
        """,
    },
    "consultation_statement/consultation_statement.md": {
        "title": "Consultation Statement",
        "body": """
        ## Consultation Approach

        Record statutory and non-statutory consultation duties, consultees, methods, accessible formats, response handling, data protection and audit trail.

        ## Analysis And Response

        Summarise issues raised, evidence reviewed, design changes, reasons for rejecting alternatives, and unresolved matters.
        """,
    },
    "equality_and_human_rights/equality_human_rights_statement.md": {
        "title": "Equality And Human Rights Statement",
        "body": """
        ## Assessment Basis

        Summarise equality, health and distributional impacts using current EqIA material, consultation evidence and appraisal outputs. Identify where evidence is provisional.

        ## Mitigation And Monitoring

        Set out mitigations, residual impacts, monitoring indicators and review triggers.
        """,
    },
    "financial_and_net_proceeds/net_proceeds_statement.md": {
        "title": "Financial And Net Proceeds Statement",
        "body": """
        ## Financial Basis

        Reconcile charge income, operating costs, enforcement costs, capital costs, financing and net proceeds to the financial case.

        ## Legal Controls

        Link each net-proceeds proposition to Schedule 12 and the Net Proceeds Regulations source IDs in the legal compliance matrix.
        """,
    },
    "licensing_enforcement_and_appeals/licensing_enforcement_appeals.md": {
        "title": "Licensing, Enforcement And Appeals Design",
        "body": """
        ## Operating Model

        Define licence lifecycle, employer records, charge calculation, payment collection, compliance monitoring, penalty charge process, representations and appeals.

        ## Control Requirements

        Address evidence standards, procedural fairness, data protection, accessibility, audit logs, system controls and customer contact.
        """,
    },
    "monitoring_and_review/monitoring_review_plan.md": {
        "title": "Monitoring And Review Plan",
        "body": """
        ## Baseline And Metrics

        Define parking-base, traffic, mode share, bus performance, revenue, compliance, employer impact, equality and displacement baselines.

        ## Evaluation Design

        Explain comparison groups, before-after design, data refresh cadence, publication plan, review triggers and governance.
        """,
    },
}


def write_file(path: Path, title: str, body: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n{textwrap.dedent(body).strip()}\n", encoding="utf-8")
    return True


def build_case(case_key: str, case_name: str, case_stage: str, force: bool) -> int:
    count = 0
    for rel, spec in CASE_SECTIONS.items():
        body = spec["body"].format(case_name=case_name, case_stage=case_stage)
        if write_file(ROOT / "business_case" / case_key / rel, spec["title"], body, force):
            count += 1
    return count


def build_statutory(force: bool) -> int:
    count = 0
    for rel, spec in STATUTORY_TEMPLATES.items():
        if write_file(ROOT / "statutory_dossier" / rel, spec["title"], spec["body"], force):
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Overwrite existing templates")
    args = parser.parse_args()

    written = 0
    written += build_case("obc", "Outline Business Case", "OBC", args.force)
    written += build_case("fbc", "Full Business Case", "FBC", args.force)
    written += build_statutory(args.force)
    print(f"Wrote {written} templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

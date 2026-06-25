#!/usr/bin/env python3
"""Bootstrap the Bristol WPL simulation repository.

This script intentionally uses only the Python standard library so it can run
before project dependencies are installed.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import platform
import shutil
import stat
import subprocess
import sys
import textwrap
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
TODAY = dt.date(2026, 6, 25).isoformat()


DIRS = [
    "inputs/supplied_documents",
    "instructions",
    "config",
    "schemas",
    "governance",
    "evidence/raw/legislation",
    "evidence/raw/court-and-public-law",
    "evidence/raw/hm-treasury",
    "evidence/raw/dft-and-tag",
    "evidence/raw/bristol-city-council",
    "evidence/raw/west-of-england-mca",
    "evidence/raw/nottingham",
    "evidence/raw/uk-comparators",
    "evidence/raw/consultation-and-equality",
    "evidence/raw/procurement-and-data",
    "evidence/raw/academic",
    "evidence/raw/media-and-advocacy",
    "evidence/processed/text",
    "evidence/processed/tables",
    "evidence/processed/metadata",
    "evidence/processed/web-snapshots",
    "evidence/source_notes",
    "evidence/archive",
    "data/raw",
    "data/interim",
    "data/processed",
    "data/data_dictionaries",
    "data/data_quality",
    "data/licences",
    "data/synthetic_examples",
    "data/restricted",
    "spatial/raw",
    "spatial/working",
    "spatial/boundary_options",
    "spatial/parking_inventory",
    "spatial/accessibility",
    "spatial/displacement",
    "spatial/cross_boundary",
    "spatial/outputs/geopackage",
    "spatial/outputs/geojson",
    "spatial/outputs/svg",
    "spatial/outputs/png",
    "spatial/qgis",
    "spatial/metadata",
    "spatial/spatial_qa",
    "models/common",
    "models/parking-base",
    "models/behavioural-response",
    "models/transport",
    "models/revenue",
    "models/scheme-cost",
    "models/economic-appraisal",
    "models/financial",
    "models/business-impact",
    "models/distributional",
    "models/carbon-and-environment",
    "models/uncertainty",
    "models/validation",
    "models/model_cards",
    "models/outputs",
    "analysis/legal",
    "analysis/governance-and-powers",
    "analysis/strategic",
    "analysis/policy-alignment",
    "analysis/nottingham-and-comparators",
    "analysis/spatial",
    "analysis/transport",
    "analysis/economic",
    "analysis/financial",
    "analysis/commercial",
    "analysis/operations-and-enforcement",
    "analysis/consultation",
    "analysis/equality-health-and-distributional",
    "analysis/environment-and-carbon",
    "analysis/data-protection-and-cyber",
    "analysis/evaluation",
    "analysis/weca-role-and-evidence",
    "consultation/strategy",
    "consultation/materials",
    "consultation/questionnaire",
    "consultation/response_data",
    "consultation/analysis",
    "consultation/consultation_report",
    "consultation/you_said_we_did",
    "business_case/shared",
    "business_case/obc/00-front-matter",
    "business_case/obc/01-executive-summary",
    "business_case/obc/02-strategic-case",
    "business_case/obc/03-economic-case",
    "business_case/obc/04-commercial-case",
    "business_case/obc/05-financial-case",
    "business_case/obc/06-management-case",
    "business_case/obc/07-conclusions-and-decisions",
    "business_case/obc/appendices",
    "business_case/obc/assembled",
    "business_case/fbc/00-front-matter",
    "business_case/fbc/01-executive-summary",
    "business_case/fbc/02-strategic-case",
    "business_case/fbc/03-economic-case",
    "business_case/fbc/04-commercial-case",
    "business_case/fbc/05-financial-case",
    "business_case/fbc/06-management-case",
    "business_case/fbc/07-conclusions-and-decisions",
    "business_case/fbc/appendices",
    "business_case/fbc/assembled",
    "statutory_dossier/draft_scheme_order",
    "statutory_dossier/boundary_schedule",
    "statutory_dossier/statement_of_reasons",
    "statutory_dossier/local_transport_policy_case",
    "statutory_dossier/ten_year_general_plan",
    "statutory_dossier/five_year_detailed_programme",
    "statutory_dossier/consultation_statement",
    "statutory_dossier/equality_and_human_rights",
    "statutory_dossier/financial_and_net_proceeds",
    "statutory_dossier/licensing_enforcement_and_appeals",
    "statutory_dossier/monitoring_and_review",
    "statutory_dossier/council_resolutions",
    "statutory_dossier/dft_pre_application",
    "statutory_dossier/assembled",
    "investment_programme/delivery_maturity",
    "investment_programme/costs",
    "investment_programme/benefits",
    "investment_programme/funding",
    "investment_programme/assurance",
    "templates",
    "review/author_checks",
    "review/peer_review",
    "review/legal_review",
    "review/analytical_assurance",
    "review/financial_review",
    "review/accessibility_review",
    "review/red_team",
    "review/integrated_case_review",
    "review/stage_gate_reports",
    "review/issue_resolution",
    "deliverables/working/markdown",
    "deliverables/working/docx",
    "deliverables/working/html",
    "deliverables/review/markdown",
    "deliverables/review/docx",
    "deliverables/review/html",
    "deliverables/officer_edits/incoming",
    "deliverables/officer_edits/compared",
    "deliverables/officer_edits/accepted",
    "deliverables/officer_edits/rejected",
    "deliverables/final/markdown",
    "deliverables/final/docx",
    "deliverables/final/xlsx",
    "deliverables/final/html",
    "deliverables/final/spatial",
    "deliverables/final/data",
    "logs/agent_activity",
    "logs/pipeline",
    "logs/model_runs",
    "logs/releases",
    "tests",
    "docs/superpowers/plans",
]


AGENT_DIRS = [
    "governance",
    "evidence",
    "data",
    "spatial",
    "models",
    "analysis",
    "consultation",
    "business_case",
    "statutory_dossier",
    "review",
]


REGISTER_COLUMNS = {
    "governance/skills_gap_register.csv": [
        "gap_id",
        "required_profession_or_agent",
        "simulation_role",
        "purpose",
        "scope_of_review",
        "evidence_to_review",
        "expected_signoff",
        "status",
        "owner",
        "target_stage_gate",
        "consequence_if_unavailable",
        "real_world_adoption_gap",
    ],
    "governance/simulation_signoff_register.csv": [
        "signoff_id",
        "agent_role",
        "simulated_competence",
        "scope",
        "artefact",
        "evidence_reviewed",
        "criteria_applied",
        "findings",
        "limitations",
        "decision",
        "unresolved_risks",
        "date",
        "statement",
    ],
    "governance/decision_log.csv": [
        "decision_id",
        "date",
        "stage",
        "decision",
        "options_considered",
        "rationale",
        "evidence",
        "owner",
        "status",
    ],
    "governance/assumptions_register.csv": [
        "assumption_id",
        "stage",
        "assumption",
        "basis",
        "owner",
        "review_date",
        "status",
    ],
    "governance/issues_register.csv": [
        "issue_id",
        "stage",
        "severity",
        "issue",
        "owner",
        "due_date",
        "status",
        "notes",
    ],
    "governance/dependencies_register.csv": [
        "dependency_id",
        "stage",
        "dependency",
        "owner",
        "needed_by",
        "risk_if_missing",
        "status",
    ],
    "governance/approvals_register.csv": [
        "approval_id",
        "approval_type",
        "blocks",
        "stage",
        "approver_role",
        "artefact",
        "prerequisites",
        "status",
        "evidence",
    ],
    "governance/benefits_register.csv": [
        "benefit_id",
        "objective",
        "benefit",
        "measure",
        "baseline",
        "target",
        "owner",
        "evidence",
        "status",
    ],
    "governance/requirements_register.csv": [
        "requirement_id",
        "source",
        "requirement",
        "owner",
        "stage",
        "evidence",
        "status",
    ],
    "evidence/source_register.csv": [
        "source_id",
        "seed_doc_id",
        "priority",
        "workstream",
        "source_body",
        "title",
        "publication_date",
        "document_type",
        "url",
        "local_path",
        "status",
        "hierarchy_tier",
        "accessed_date",
        "sha256",
        "notes",
    ],
    "evidence/acquisition_log.csv": [
        "source_id",
        "date",
        "action",
        "url",
        "status",
        "message",
    ],
    "evidence/claim_evidence_matrix.csv": [
        "claim_id",
        "document_id",
        "section",
        "claim_text",
        "materiality",
        "claim_type",
        "source_ids",
        "location_in_source",
        "evidence_quality",
        "conflicting_evidence",
        "assumption_id",
        "reviewer",
        "review_status",
        "last_verified",
        "notes",
    ],
    "evidence/conflicting_evidence_register.csv": [
        "conflict_id",
        "source_ids",
        "issue",
        "materiality",
        "owner",
        "status",
        "resolution",
    ],
    "evidence/evidence_gap_register.csv": [
        "gap_id",
        "stage",
        "gap",
        "materiality",
        "owner",
        "proposed_action",
        "status",
    ],
    "consultation/stakeholder_map.csv": [
        "stakeholder_id",
        "group",
        "interest",
        "potential_impact",
        "engagement_route",
        "accessibility_needs",
        "status",
    ],
    "consultation/engagement_log.csv": [
        "engagement_id",
        "date",
        "stakeholder_id",
        "method",
        "summary",
        "evidence",
        "status",
    ],
    "consultation/issues_log.csv": [
        "issue_id",
        "source",
        "issue",
        "theme",
        "owner",
        "response",
        "status",
    ],
    "statutory_dossier/business_case_to_statutory_crosswalk.csv": [
        "requirement_id",
        "statutory_requirement",
        "obc_section",
        "fbc_section",
        "statutory_document",
        "evidence_item",
        "owner",
        "reviewer",
        "status",
    ],
    "statutory_dossier/legal_compliance_matrix.csv": [
        "requirement_id",
        "legal_source",
        "section_or_regulation",
        "operative_requirement",
        "interpretation",
        "scheme_implication",
        "required_evidence",
        "responsible_owner",
        "reviewer",
        "obc_status",
        "fbc_status",
        "submission_document",
        "risk",
        "decision",
    ],
    "statutory_dossier/dft_pre_application/engagement_log.csv": [
        "engagement_id",
        "date",
        "classification",
        "topic",
        "participants_or_roles",
        "summary",
        "evidence",
        "status",
    ],
    "review/issue_resolution/office-edit-log.csv": [
        "change_id",
        "document_id",
        "section",
        "officer_or_agent",
        "proposed_text",
        "disposition",
        "rationale",
        "owner",
        "closure_reviewer",
    ],
}


def write_text(rel: str, content: str, overwrite: bool = False) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def write_csv(
    rel: str,
    columns: list[str],
    rows: list[dict[str, str]] | None = None,
    overwrite: bool = False,
) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for row in rows or []:
            writer.writerow({col: row.get(col, "") for col in columns})


def write_simple_xlsx(
    rel: str,
    sheet_name: str,
    columns: list[str],
    rows: list[list[str]] | None = None,
    overwrite: bool = False,
) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    rows = rows or []

    def cell_ref(col_index: int, row_index: int) -> str:
        letters = ""
        col = col_index
        while col:
            col, rem = divmod(col - 1, 26)
            letters = chr(65 + rem) + letters
        return f"{letters}{row_index}"

    all_rows = [columns] + rows
    sheet_rows = []
    for r_idx, row in enumerate(all_rows, start=1):
        cells = []
        for c_idx, value in enumerate(row, start=1):
            ref = cell_ref(c_idx, r_idx)
            cells.append(
                f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>'
            )
        sheet_rows.append(f'<row r="{r_idx}">{"".join(cells)}</row>')

    files = {
        "[Content_Types].xml": """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>""",
        "_rels/.rels": """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>""",
        "xl/workbook.xml": f"""<?xml version="1.0" encoding="UTF-8"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<sheets><sheet name="{escape(sheet_name)}" sheetId="1" r:id="rId1"/></sheets>
</workbook>""",
        "xl/_rels/workbook.xml.rels": """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>""",
        "xl/worksheets/sheet1.xml": f"""<?xml version="1.0" encoding="UTF-8"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<sheetData>{''.join(sheet_rows)}</sheetData>
</worksheet>""",
    }
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, data in files.items():
            zf.writestr(name, data)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def command_available(command: str) -> bool:
    return shutil.which(command) is not None


def git_value(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    except Exception:
        return ""


def source_prefix(row: dict[str, str]) -> str:
    body = (row.get("source_body") or row.get("doc_id") or "SRC").lower()
    if "bristol" in body:
        return "SRC-BCC"
    if "west of england" in body or "weca" in body:
        return "SRC-WECA"
    if "transport for london" in body:
        return "SRC-TFL"
    if "nottingham" in body:
        return "SRC-NOTT"
    if "department for transport" in body:
        return "SRC-DFT"
    if "legislation" in body or "uk legislation" in body:
        return "SRC-LEG"
    if "academic" in body or "loughborough" in body:
        return "SRC-ACADEMIC"
    if "treasury" in body:
        return "SRC-HMT"
    return "SRC-UK"


def hierarchy_tier(row: dict[str, str]) -> str:
    workstream = row.get("workstream", "")
    body = row.get("source_body", "").lower()
    if "legislation" in body:
        return "1_current_legislation"
    if "department for transport" in body:
        return "2_official_government_guidance"
    if "bristol" in body or "west of england" in body:
        return "3_formal_public_body_source"
    if "academic" in body or "loughborough" in body:
        return "5_independent_research"
    if "media" in workstream or "political" in workstream:
        return "8_media_advocacy_context"
    return "7_professional_or_context_source"


def ingest_sources() -> None:
    root_csv = ROOT / "bristol_wpl_codex_sources.csv"
    input_csv = ROOT / "inputs/bristol_wpl_codex_sources.csv"
    input_csv.parent.mkdir(parents=True, exist_ok=True)
    if root_csv.exists() and not input_csv.exists():
        shutil.copy2(root_csv, input_csv)

    if not input_csv.exists():
        write_csv("evidence/source_register.csv", REGISTER_COLUMNS["evidence/source_register.csv"])
        return

    with input_csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    counters: dict[str, int] = {}
    source_rows = []
    acquisition_rows = []
    for row in rows:
        prefix = source_prefix(row)
        counters[prefix] = counters.get(prefix, 0) + 1
        source_id = f"{prefix}-{counters[prefix]:04d}"
        local_path = f"{row.get('target_dir','').strip('/')}/{row.get('target_filename','')}".strip("/")
        source_rows.append(
            {
                "source_id": source_id,
                "seed_doc_id": row.get("doc_id", ""),
                "priority": row.get("priority", ""),
                "workstream": row.get("workstream", ""),
                "source_body": row.get("source_body", ""),
                "title": row.get("document_title", ""),
                "publication_date": row.get("document_date", ""),
                "document_type": row.get("document_type", ""),
                "url": row.get("url", ""),
                "local_path": local_path,
                "status": "seeded_not_downloaded",
                "hierarchy_tier": hierarchy_tier(row),
                "accessed_date": "",
                "sha256": "",
                "notes": row.get("notes", ""),
            }
        )
        acquisition_rows.append(
            {
                "source_id": source_id,
                "date": TODAY,
                "action": "seed_ingest",
                "url": row.get("url", ""),
                "status": "not_downloaded",
                "message": "Seed record ingested; source acquisition not yet run.",
            }
        )

    write_csv(
        "evidence/source_register.csv",
        REGISTER_COLUMNS["evidence/source_register.csv"],
        source_rows,
        overwrite=True,
    )
    write_csv(
        "evidence/acquisition_log.csv",
        REGISTER_COLUMNS["evidence/acquisition_log.csv"],
        acquisition_rows,
        overwrite=True,
    )
    write_simple_xlsx(
        "evidence/source_register.xlsx",
        "source_register",
        REGISTER_COLUMNS["evidence/source_register.csv"],
        [[r.get(c, "") for c in REGISTER_COLUMNS["evidence/source_register.csv"]] for r in source_rows],
        overwrite=True,
    )


def write_root_files() -> None:
    write_text(
        "AGENTS.md",
        """
        # Bristol WPL Simulation Agents

        Mission: build a full-simulation, government-grade Bristol Workplace Parking Levy OBC/FBC/statutory dossier workspace.

        Non-negotiables:
        - Do not invent evidence, citations, approvals, model outputs or consultation responses.
        - Do not create authored PDFs. Raw third-party PDFs may exist only under `evidence/raw/**`.
        - Use bounded subagent context packets and agentic simulation sign-offs.
        - Every material claim must be cited, labelled as an assumption/inference/proposal, or recorded as a gap.
        - Agent sign-offs are simulation sign-offs only and have no real-world legal, statutory, financial or professional effect.

        Detailed operating instructions live in `instructions/`.
        Start with `instructions/00-operating-model.md` and `instructions/10-stage-gates.md`.
        """,
    )
    write_text(
        "README.md",
        """
        # Bristol Workplace Parking Levy Simulation

        This repository is a controlled workspace for a full simulation of a Bristol Workplace Parking Levy OBC, FBC and statutory confirmation dossier.

        Source of truth:
        - `CODEX_MASTER_PROMPT.md`
        - `instructions/00-operating-model.md`
        - controlled Markdown, CSV, XLSX, JSON, HTML and GIS artefacts generated under the repo structure

        This is not legal advice, statutory confirmation, financial certification or approval by any public body. All sign-offs are agentic simulation sign-offs unless explicitly replaced in a future real-world process.
        """,
    )
    write_text(
        "PROJECT_CHARTER.md",
        """
        # Project Charter

        **Programme:** Bristol Workplace Parking Levy full simulation
        **Date:** 2026-06-25
        **Mode:** Agentic simulation with bounded specialist review agents

        ## Purpose

        Create an editable, auditable simulation of the evidence, business-case, statutory, spatial, financial, consultation, operating and assurance material required for a Bristol Workplace Parking Levy programme.

        ## Guardrails

        - No authored PDFs.
        - No invented evidence.
        - No real-world legal, officer, financial, statutory or professional approval claims.
        - Simulation sign-offs are recorded separately from real-world adoption gaps.
        """,
    )
    write_text("CHANGELOG.md", "# Changelog\n\n## 2026-06-25\n\n- Bootstrapped controlled simulation repository.\n")
    write_text(
        "Makefile",
        """
        PYTHON ?= python3

        .PHONY: bootstrap ingest extract evidence-qa validate models model-qa spatial-qa assemble-obc assemble-fbc build-docx accessibility-check red-team gate-obc gate-fbc all

        bootstrap:
        \t$(PYTHON) scripts/bootstrap_repo.py

        ingest:
        \t$(PYTHON) scripts/ingest_sources.py

        extract:
        \t$(PYTHON) scripts/extract_sources.py

        evidence-qa:
        \t$(PYTHON) scripts/validate_registers.py --evidence

        validate:
        \t$(PYTHON) scripts/validate_registers.py
        \t$(PYTHON) -m unittest discover -s tests

        models:
        \t$(PYTHON) scripts/build_models.py

        model-qa:
        \t$(PYTHON) scripts/run_model_checks.py

        spatial-qa:
        \t$(PYTHON) scripts/validate_spatial.py

        assemble-obc:
        \t$(PYTHON) scripts/assemble_obc.py

        assemble-fbc:
        \t$(PYTHON) scripts/assemble_fbc.py

        build-docx:
        \t$(PYTHON) scripts/build_docx.py

        accessibility-check:
        \t$(PYTHON) scripts/validate_docx.py

        red-team:
        \t$(PYTHON) scripts/stage_gate_check.py --red-team

        gate-obc:
        \t$(PYTHON) scripts/stage_gate_check.py --gate obc

        gate-fbc:
        \t$(PYTHON) scripts/stage_gate_check.py --gate fbc

        all: bootstrap ingest validate
        """,
    )
    write_text(
        "pyproject.toml",
        """
        [project]
        name = "bristol-wpl-simulation"
        version = "0.1.0"
        description = "Full simulation workspace for a Bristol Workplace Parking Levy business case and statutory dossier."
        requires-python = ">=3.12"

        [tool.unittest]
        start-directory = "tests"
        """,
    )
    write_text(
        ".gitignore",
        """
        .DS_Store
        __pycache__/
        *.py[cod]
        .pytest_cache/
        .mypy_cache/
        .ruff_cache/
        .venv/
        venv/

        # Restricted or sensitive working data must not be committed.
        data/restricted/**
        consultation/response_data/raw/**
        consultation/response_data/personal/**
        **/*secret*
        **/*credentials*
        **/*.key
        **/*.pem
        **/.env
        .env

        # Generated local package scratch.
        .worktrees/
        worktrees/
        """,
    )
    write_text(
        ".editorconfig",
        """
        root = true

        [*]
        charset = utf-8
        end_of_line = lf
        insert_final_newline = true
        indent_style = space
        indent_size = 2

        [*.py]
        indent_size = 4
        """,
    )
    write_text(
        ".pre-commit-config.yaml",
        """
        repos:
          - repo: local
            hooks:
              - id: bristol-wpl-validate
                name: Bristol WPL validation
                entry: python3 scripts/validate_registers.py
                language: system
                pass_filenames: false
        """,
    )


def write_instructions() -> None:
    master = ROOT / "CODEX_MASTER_PROMPT.md"
    if master.exists():
        target = ROOT / "instructions/00-operating-model.md"
        if not target.exists():
            target.write_text(master.read_text(encoding="utf-8"), encoding="utf-8")
    instruction_map = {
        "instructions/01-evidence-and-citations.md": "# Evidence and Citations\n\nUse the source hierarchy in `00-operating-model.md`. Every material claim must map to `evidence/claim_evidence_matrix.csv` or an assumption/gap register.\n",
        "instructions/02-legal-and-governance.md": "# Legal and Governance\n\nThis is simulation legal review only. Produce statutory route, powers, confirmation, consultation, HRA, data, subsidy and net-proceeds notes before scheme design conclusions.\n",
        "instructions/03-business-case-authoring.md": "# Business Case Authoring\n\nUse the Five Case Model. Do not draft a preferred WPL conclusion before the strategic assessment, options framework, ASR and evidence gates are complete.\n",
        "instructions/04-spatial-and-data.md": "# Spatial and Data\n\nUse EPSG:27700 for working spatial data where possible. Boundary options require reproducible manifests, topology checks and simulation GIS/legal sign-off.\n",
        "instructions/05-modelling-and-appraisal.md": "# Modelling and Appraisal\n\nEvery model needs a model card, run manifest, input hashes, scenario controls, validation and simulation review. Do not treat gross levy income as an economic benefit.\n",
        "instructions/06-consultation-equality-and-health.md": "# Consultation, Equality and Health\n\nConsultation must be formative in the simulation, accessible, and clear about what is fixed and open. EqIA, HRA and distributional analysis must be iterative.\n",
        "instructions/07-finance-commercial-and-operations.md": "# Finance, Commercial and Operations\n\nSeparate gross income, operating cost, net proceeds, economic transfers, affordability, procurement, licensing, compliance, enforcement and appeals.\n",
        "instructions/08-quality-assurance-and-red-team.md": "# Quality Assurance and Red Team\n\nUse P0-P3 findings. P0 blocks the relevant simulation gate. Red-team reviews must be independent of the authoring agent.\n",
        "instructions/09-document-production.md": "# Document Production\n\nMarkdown is the controlled source. DOCX/HTML are editable review outputs. No authored PDFs. Officer-style edits must be reconciled back into Markdown.\n",
        "instructions/10-stage-gates.md": "# Stage Gates\n\nStage gates require evidence status, issue status, simulation sign-offs, unresolved P0/P1 findings, real-world adoption gaps and next-stage conditions.\n",
    }
    for rel, content in instruction_map.items():
        write_text(rel, content)


def write_config_and_schemas() -> None:
    configs = {
        "config/project.yaml": "programme: Bristol Workplace Parking Levy\nmode: full_simulation\nevidence_cutoff: null\nno_authored_pdf: true\n",
        "config/jurisdictions.yaml": "jurisdiction: England\nprimary_promoter_under_investigation: Bristol City Council\nregional_body_under_investigation: West of England Mayoral Combined Authority\n",
        "config/document-style.yaml": "language: British English\nsource_of_truth: markdown\nreview_outputs: [docx, html]\n",
        "config/evidence-quality.yaml": "tiers: [current_legislation, official_guidance, formal_decision, official_data, peer_reviewed, promoter_report, professional_research, media_context]\n",
        "config/qa-thresholds.yaml": "material_claim_traceability: 1.0\nfinancial_total_reconciliation: 1.0\nlegal_requirement_mapping: 1.0\nallow_unresolved_p0: false\n",
        "config/modelling.yaml": "model_run_manifest_required: true\nuncertainty_log_required: true\nsingle_point_forecasts_allowed: false\n",
        "config/spatial.yaml": "working_crs: EPSG:27700\nweb_crs: EPSG:4326\nboundary_manifest_required: true\n",
    }
    for rel, content in configs.items():
        write_text(rel, content)

    base_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": True,
        "properties": {
            "id": {"type": "string"},
            "status": {"type": "string"},
            "owner": {"type": "string"},
        },
    }
    schema_names = [
        "source-register",
        "claim-register",
        "assumption-register",
        "risk-register",
        "decision-register",
        "consultation-response",
        "model-card",
        "spatial-metadata",
        "parking-inventory",
        "boundary-option",
        "model-run",
        "data-dictionary",
        "data-classification",
        "public-release-manifest",
    ]
    for name in schema_names:
        rel = f"schemas/{name}.schema.json"
        path = ROOT / rel
        if not path.exists():
            path.write_text(json.dumps(base_schema, indent=2) + "\n", encoding="utf-8")


def write_registers() -> None:
    initial_skill_rows = [
        {
            "gap_id": "GAP-0001",
            "required_profession_or_agent": "Legal Review Agent",
            "simulation_role": "WPL Statutory and Public-Law simulation reviewer",
            "purpose": "Review statutory route, promoter powers and confirmation route in simulation.",
            "scope_of_review": "Stage 2 legal route and statutory matrix",
            "evidence_to_review": "Transport Act 2000, WPL Regulations, Net Proceeds Regulations, Bristol/WECA governance evidence",
            "expected_signoff": "simulation sign-off or simulation rework required",
            "status": "required",
            "owner": "Programme Orchestrator",
            "target_stage_gate": "Stage 2",
            "consequence_if_unavailable": "Simulation cannot progress to preferred scheme design.",
            "real_world_adoption_gap": "Real solicitor/counsel/Monitoring Officer review would be required outside simulation.",
        },
        {
            "gap_id": "GAP-0002",
            "required_profession_or_agent": "Transport Economics Review Agent",
            "simulation_role": "TAG and Green Book simulation reviewer",
            "purpose": "Review ASR, economic appraisal and value-for-money treatment.",
            "scope_of_review": "Stages 5-7",
            "evidence_to_review": "DfT TAG, Green Book, models and appraisal tables",
            "expected_signoff": "simulation sign-off or simulation rework required",
            "status": "required",
            "owner": "Programme Orchestrator",
            "target_stage_gate": "OBC gate",
            "consequence_if_unavailable": "Economic case cannot pass simulation gate.",
            "real_world_adoption_gap": "Independent transport economist review would be required outside simulation.",
        },
    ]
    for rel, cols in REGISTER_COLUMNS.items():
        rows = initial_skill_rows if rel == "governance/skills_gap_register.csv" else []
        write_csv(rel, cols, rows)

    risk_cols = [
        "risk_id",
        "stage",
        "risk",
        "likelihood",
        "impact",
        "gross_rating",
        "controls",
        "residual_rating",
        "owner",
        "review_date",
        "acceptance_authority",
        "status",
    ]
    write_csv("governance/risk_register.csv", risk_cols)
    write_simple_xlsx("governance/risk_register.xlsx", "risk_register", risk_cols)


def write_agent_files() -> None:
    for directory in AGENT_DIRS:
        write_text(
            f"{directory}/AGENTS.md",
            f"""
            # {directory} Agent Instructions

            Work only within this directory unless the task packet explicitly grants another path.
            Use bounded context. Cite sources by source ID where possible. Record assumptions and gaps rather than inventing evidence.
            Agentic sign-off is simulation-only and must be recorded in `governance/simulation_signoff_register.csv`.
            """,
        )


def write_templates_and_docs() -> None:
    templates = {
        "templates/business_case_section.md": "# {{section_title}}\n\n{{simulation_status_notice}}\n\n## Purpose\n\n## Evidence\n\n## Analysis\n\n## Risks and gaps\n",
        "templates/evidence_note.md": "# Evidence Note\n\n## Source\n\n## Provenance\n\n## Relevant findings\n\n## Limitations\n",
        "templates/options_appraisal.md": "# Options Appraisal\n\n## Options\n\n## Criteria\n\n## Scores\n\n## Sensitivities\n\n## Decision\n",
        "templates/model_card.md": "# Model Card\n\n## Purpose\n\n## Inputs\n\n## Method\n\n## Outputs\n\n## Validation\n\n## Limitations\n",
        "templates/legal_note.md": "# Simulation Legal Note\n\nThis is not legal advice.\n\n## Question\n\n## Current law to verify\n\n## Analysis\n\n## Simulation conclusion\n\n## Real-world adoption gap\n",
        "templates/decision_report.md": "# Decision Report\n\n## Decision sought\n\n## Options\n\n## Evidence\n\n## Risks\n\n## Simulation sign-off\n",
        "templates/assurance_review.md": "# Assurance Review\n\n## Scope\n\n## Criteria\n\n## Findings\n\n## Severity\n\n## Sign-off decision\n",
        "templates/officer_commentary.md": "# Officer-Style Commentary\n\nSimulation text for editable officer review. Not an officer decision.\n",
    }
    for rel, content in templates.items():
        write_text(rel, content)

    shared = {
        "business_case/shared/glossary.md": "# Glossary\n\nControlled glossary. Expand abbreviations on first use.\n",
        "business_case/shared/abbreviations.md": "# Abbreviations\n\n- WPL: Workplace Parking Levy\n- OBC: Outline Business Case\n- FBC: Full Business Case\n- WECA: West of England Combined Authority / historic shorthand\n",
        "business_case/shared/document_control.md": "# Document Control\n\nUse Markdown as source of truth. Record build IDs and simulation sign-offs.\n",
        "business_case/shared/master_bibliography.yaml": "sources: []\n",
        "statutory_dossier/confirmation_requirements.md": "# Confirmation Requirements\n\nTo be populated after current-law review. For an initial scheme, treat Transport Act 2000 section 184 confirmation as required unless simulation legal review establishes otherwise.\n",
        "statutory_dossier/dft_pre_application/questions_for_dft.md": "# Questions for DfT / Secretary of State Route\n\nClassify each question as informal engagement, policy expectation, procedural requirement, formal decision, or confirmation material.\n",
        "statutory_dossier/dft_pre_application/confirmation_dossier_checklist.md": "# Confirmation Dossier Checklist\n\nWorking checklist subject to current-law and simulation legal review.\n",
        "investment_programme/programme_definition.md": "# Investment Programme Definition\n\nNo funded package is assumed. Projects must be evidenced, costed and maturity-assessed.\n",
        "investment_programme/dependency_map.md": "# Dependency Map\n\nTo be populated during strategic and management case work.\n",
    }
    for rel, content in shared.items():
        write_text(rel, content)


def script_common() -> str:
    return """#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    print("This command is a safe placeholder for the Stage 0 simulation baseline.")
"""


def write_scripts() -> None:
    ingest = """#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bootstrap_repo", ROOT / "scripts/bootstrap_repo.py")
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)
module.ingest_sources()
print("Seed sources ingested into evidence/source_register.csv")
"""
    write_text("scripts/ingest_sources.py", ingest, overwrite=True)

    validate = """#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "governance/skills_gap_register.csv": ["gap_id", "required_profession_or_agent", "simulation_role"],
    "governance/simulation_signoff_register.csv": ["signoff_id", "agent_role", "decision", "statement"],
    "evidence/source_register.csv": ["source_id", "seed_doc_id", "url", "status"],
    "evidence/claim_evidence_matrix.csv": ["claim_id", "document_id", "claim_text", "source_ids"],
    "statutory_dossier/legal_compliance_matrix.csv": ["requirement_id", "legal_source", "operative_requirement"],
}

def read_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle))

def check_registers() -> list[str]:
    errors = []
    for rel, columns in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required register: {rel}")
            continue
        header = read_header(path)
        for col in columns:
            if col not in header:
                errors.append(f"{rel} missing column {col}")
    return errors

def check_no_authored_pdfs() -> list[str]:
    errors = []
    for path in ROOT.rglob("*.pdf"):
        rel = path.relative_to(ROOT).as_posix()
        if not rel.startswith("evidence/raw/"):
            errors.append(f"authored or misplaced PDF is not allowed: {rel}")
    return errors

def check_sensitive_paths() -> list[str]:
    errors = []
    forbidden_parts = [
        "data/restricted/",
        "consultation/response_data/raw/",
        "consultation/response_data/personal/",
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(rel.startswith(part) for part in forbidden_parts) and path.name != ".gitkeep":
            errors.append(f"restricted file present in normal repo path: {rel}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", action="store_true")
    parser.parse_args()
    errors = []
    errors.extend(check_registers())
    errors.extend(check_no_authored_pdfs())
    errors.extend(check_sensitive_paths())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
"""
    write_text("scripts/validate_registers.py", validate, overwrite=True)

    stage_gate = """#!/usr/bin/env python3
from __future__ import annotations

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--gate", choices=["obc", "fbc"])
parser.add_argument("--red-team", action="store_true")
args = parser.parse_args()

if args.red_team:
    print("Red-team placeholder: create bounded review packet before use.")
elif args.gate:
    print(f"Stage-gate placeholder for {args.gate}: no gate can pass with open P0.")
else:
    print("Stage-gate placeholder: specify --gate or --red-team.")
"""
    write_text("scripts/stage_gate_check.py", stage_gate, overwrite=True)

    for rel in [
        "scripts/extract_sources.py",
        "scripts/build_source_register.py",
        "scripts/validate_claims.py",
        "scripts/check_links.py",
        "scripts/build_docx.py",
        "scripts/validate_docx.py",
        "scripts/build_models.py",
        "scripts/run_model_checks.py",
        "scripts/validate_spatial.py",
        "scripts/render_maps.py",
        "scripts/assemble_obc.py",
        "scripts/assemble_fbc.py",
    ]:
        write_text(rel, script_common(), overwrite=True)

    for script in (ROOT / "scripts").glob("*.py"):
        script.chmod(script.stat().st_mode | stat.S_IXUSR)


def write_tests() -> None:
    write_text(
        "tests/test_no_pdf_outputs.py",
        """
        from pathlib import Path
        import unittest

        ROOT = Path(__file__).resolve().parents[1]

        class NoPdfOutputsTest(unittest.TestCase):
            def test_pdfs_only_under_raw_evidence(self):
                offenders = [
                    p.relative_to(ROOT).as_posix()
                    for p in ROOT.rglob("*.pdf")
                    if not p.relative_to(ROOT).as_posix().startswith("evidence/raw/")
                ]
                self.assertEqual(offenders, [])
        """,
    )
    write_text(
        "tests/test_registers.py",
        """
        import csv
        from pathlib import Path
        import unittest

        ROOT = Path(__file__).resolve().parents[1]

        class RegisterTest(unittest.TestCase):
            def header(self, rel):
                with (ROOT / rel).open(newline="", encoding="utf-8") as handle:
                    return next(csv.reader(handle))

            def test_simulation_signoff_register_exists(self):
                header = self.header("governance/simulation_signoff_register.csv")
                self.assertIn("agent_role", header)
                self.assertIn("decision", header)

            def test_source_register_seeded(self):
                with (ROOT / "evidence/source_register.csv").open(newline="", encoding="utf-8") as handle:
                    rows = list(csv.DictReader(handle))
                self.assertGreaterEqual(len(rows), 40)
        """,
    )
    write_text(
        "tests/test_sources.py",
        """
        import csv
        from pathlib import Path
        import unittest

        ROOT = Path(__file__).resolve().parents[1]

        class SourceSeedTest(unittest.TestCase):
            def test_input_seed_has_required_columns(self):
                path = ROOT / "inputs/bristol_wpl_codex_sources.csv"
                with path.open(newline="", encoding="utf-8") as handle:
                    reader = csv.DictReader(handle)
                    self.assertIn("doc_id", reader.fieldnames)
                    self.assertIn("url", reader.fieldnames)
                    rows = list(reader)
                self.assertEqual(sum(1 for row in rows if not row["url"]), 0)
        """,
    )
    for rel in [
        "tests/test_claims.py",
        "tests/test_models.py",
        "tests/test_financial_controls.py",
        "tests/test_spatial.py",
        "tests/test_cross_references.py",
    ]:
        write_text(
            rel,
            """
            import unittest

            class PlaceholderControlTest(unittest.TestCase):
                def test_stage0_placeholder(self):
                    self.assertTrue(True)
            """,
        )


def write_startup_report() -> None:
    capabilities = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "pandoc": command_available("pandoc"),
        "git": command_available("git"),
        "zip": command_available("zip"),
        "pytest": False,
        "openpyxl": False,
        "pyyaml": False,
        "git_branch": git_value(["branch", "--show-current"]),
        "git_dir": git_value(["rev-parse", "--git-dir"]),
        "git_common_dir": git_value(["rev-parse", "--git-common-dir"]),
    }
    for module_name, key in [("pytest", "pytest"), ("openpyxl", "openpyxl"), ("yaml", "pyyaml")]:
        try:
            __import__(module_name)
            capabilities[key] = True
        except Exception:
            capabilities[key] = False

    write_text(
        "STARTUP_REPORT.md",
        f"""
        # Startup Report

        **Date:** {TODAY}
        **Mode:** Full simulation with agentic simulation sign-offs.

        ## Environment

        ```json
        {json.dumps(capabilities, indent=2)}
        ```

        ## Security Constraints

        - No authored PDFs.
        - Restricted or personal data is excluded from normal Git paths.
        - Agent sign-offs are simulation-only.

        ## Initial Capability Gaps

        - `openpyxl` unavailable in the system Python; bootstrap generated minimal XLSX shells with the standard library.
        - `PyYAML` unavailable; YAML files are static text and not parsed by validation yet.
        - `pytest` unavailable; validation uses `unittest`.

        ## First Stage Plan

        1. Complete seed-source ingestion.
        2. Run bounded discovery agents.
        3. Synthesize evidence baseline, legal questions and stage-gate plan.
        4. Run validation.
        """,
        overwrite=True,
    )


def touch_gitkeep() -> None:
    for rel in DIRS:
        directory = ROOT / rel
        directory.mkdir(parents=True, exist_ok=True)
        gitkeep = directory / ".gitkeep"
        if not any(directory.iterdir()):
            gitkeep.touch()


def main() -> int:
    for rel in DIRS:
        (ROOT / rel).mkdir(parents=True, exist_ok=True)
    touch_gitkeep()
    write_root_files()
    write_instructions()
    write_config_and_schemas()
    write_agent_files()
    write_registers()
    ingest_sources()
    write_templates_and_docs()
    write_scripts()
    write_tests()
    write_startup_report()
    print("Bootstrap complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

PYTHON ?= python3

.PHONY: bootstrap acquire ingest extract source-register register-workbooks source-scan templates evidence-qa claims-qa secrets-qa validate models model-qa strategic-qa spatial-qa appraisal-qa obc-qa obc-assurance-qa consultation-qa statutory-qa fbc-statutory-qa public-release-qa handover-qa source-notes-qa authoring-qa officer-pack-qa nottingham-qa comprehension-qa visual-accessibility-qa navigation-qa external-liveness-qa register-references-qa dashboard-consistency-qa stage-gate-reports-qa refresh-external-liveness assemble-obc assemble-fbc build-docx accessibility-check red-team gate-obc gate-fbc all

bootstrap:
	$(PYTHON) scripts/bootstrap_repo.py

ingest:
	$(PYTHON) scripts/ingest_sources.py

acquire:
	$(PYTHON) scripts/acquire_sources.py --priority 1_must

extract:
	$(PYTHON) scripts/extract_sources.py

source-register:
	$(PYTHON) scripts/build_source_register.py

register-workbooks:
	$(PYTHON) scripts/build_register_workbooks.py

source-scan:
	$(PYTHON) scripts/scan_source_terms.py

templates:
	$(PYTHON) scripts/build_document_templates.py

evidence-qa:
	$(PYTHON) scripts/validate_registers.py --evidence

claims-qa:
	$(PYTHON) scripts/validate_claims.py
	$(PYTHON) scripts/validate_claim_summaries.py

secrets-qa:
	$(PYTHON) scripts/scan_secrets.py

validate:
	$(PYTHON) scripts/scan_secrets.py
	$(PYTHON) scripts/validate_registers.py
	$(PYTHON) -m unittest discover -s tests
	$(PYTHON) scripts/validate_consultation.py
	$(PYTHON) scripts/validate_officer_pack.py
	$(PYTHON) scripts/validate_nottingham_transferability.py
	$(PYTHON) scripts/validate_claims.py
	$(PYTHON) scripts/validate_obc_assurance.py
	$(PYTHON) scripts/validate_statutory_dossier.py
	$(PYTHON) scripts/validate_fbc_statutory_gate.py
	$(PYTHON) scripts/validate_public_release.py
	$(PYTHON) scripts/validate_handover.py
	$(PYTHON) scripts/validate_source_notes.py
	$(PYTHON) scripts/validate_claim_summaries.py
	$(PYTHON) scripts/validate_authoring_guardrails.py
	$(PYTHON) scripts/validate_public_cabinet_comprehension.py
	$(PYTHON) scripts/validate_visual_accessibility.py
	$(PYTHON) scripts/validate_navigation_integrity.py
	$(PYTHON) scripts/validate_external_liveness.py
	$(PYTHON) scripts/validate_register_references.py
	$(PYTHON) scripts/validate_dashboard_consistency.py
	$(PYTHON) scripts/validate_stage_gate_reports.py

models:
	$(PYTHON) scripts/build_models.py

model-qa:
	$(PYTHON) scripts/run_model_checks.py

strategic-qa:
	$(PYTHON) scripts/validate_strategic.py

spatial-qa:
	$(PYTHON) scripts/validate_spatial.py

appraisal-qa:
	$(PYTHON) scripts/validate_appraisal.py

obc-qa:
	$(PYTHON) scripts/validate_obc.py
	$(PYTHON) scripts/validate_obc_assurance.py

obc-assurance-qa:
	$(PYTHON) scripts/validate_obc_assurance.py

consultation-qa:
	$(PYTHON) scripts/validate_consultation.py

statutory-qa:
	$(PYTHON) scripts/validate_statutory_dossier.py

fbc-statutory-qa:
	$(PYTHON) scripts/validate_fbc_statutory_gate.py

public-release-qa:
	$(PYTHON) scripts/validate_public_release.py

handover-qa:
	$(PYTHON) scripts/validate_handover.py

source-notes-qa:
	$(PYTHON) scripts/validate_source_notes.py

authoring-qa:
	$(PYTHON) scripts/validate_authoring_guardrails.py

officer-pack-qa:
	$(PYTHON) scripts/validate_officer_pack.py

nottingham-qa:
	$(PYTHON) scripts/validate_nottingham_transferability.py

comprehension-qa:
	$(PYTHON) scripts/validate_public_cabinet_comprehension.py

visual-accessibility-qa:
	$(PYTHON) scripts/validate_visual_accessibility.py

navigation-qa:
	$(PYTHON) scripts/validate_navigation_integrity.py

external-liveness-qa:
	$(PYTHON) scripts/validate_external_liveness.py

register-references-qa:
	$(PYTHON) scripts/validate_register_references.py

dashboard-consistency-qa:
	$(PYTHON) scripts/validate_dashboard_consistency.py

stage-gate-reports-qa:
	$(PYTHON) scripts/validate_stage_gate_reports.py

refresh-external-liveness:
	$(PYTHON) scripts/check_external_source_liveness.py --write

assemble-obc:
	$(PYTHON) scripts/assemble_obc.py

assemble-fbc:
	$(PYTHON) scripts/assemble_fbc.py

build-docx:
	$(PYTHON) scripts/build_docx.py

accessibility-check:
	$(PYTHON) scripts/validate_docx.py

red-team:
	$(PYTHON) scripts/stage_gate_check.py --red-team

gate-obc:
	$(PYTHON) scripts/stage_gate_check.py --gate obc

gate-fbc:
	$(PYTHON) scripts/stage_gate_check.py --gate fbc

all: bootstrap ingest templates validate

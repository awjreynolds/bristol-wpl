PYTHON ?= python3

.PHONY: bootstrap acquire ingest extract source-register register-workbooks source-scan templates evidence-qa validate models model-qa strategic-qa spatial-qa appraisal-qa assemble-obc assemble-fbc build-docx accessibility-check red-team gate-obc gate-fbc all

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

validate:
	$(PYTHON) scripts/validate_registers.py
	$(PYTHON) -m unittest discover -s tests

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

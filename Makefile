PYTHON ?= python3

.PHONY: bootstrap ingest extract evidence-qa validate models model-qa spatial-qa assemble-obc assemble-fbc build-docx accessibility-check red-team gate-obc gate-fbc all

bootstrap:
	$(PYTHON) scripts/bootstrap_repo.py

ingest:
	$(PYTHON) scripts/ingest_sources.py

extract:
	$(PYTHON) scripts/extract_sources.py

evidence-qa:
	$(PYTHON) scripts/validate_registers.py --evidence

validate:
	$(PYTHON) scripts/validate_registers.py
	$(PYTHON) -m unittest discover -s tests

models:
	$(PYTHON) scripts/build_models.py

model-qa:
	$(PYTHON) scripts/run_model_checks.py

spatial-qa:
	$(PYTHON) scripts/validate_spatial.py

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

all: bootstrap ingest validate

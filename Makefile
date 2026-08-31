# `make publish SOURCE=/path/to/private-vault` (or set VAULT_PATH)
SOURCE ?=
# iBrain ops — command interface
# The vault resolves to ./vault (bundled) unless VAULT_PATH is set.

PY := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: bootstrap ingest validate normalize-links health study indexes refresh test secretscan console learning-view score publish site help

help:
	@echo "make bootstrap   — create venv + install deps"
	@echo "make ingest      — run xlsx + conversation importers (idempotent)"
	@echo "make validate    — frontmatter + duplicate ids + wikilinks (hard checks)"
	@echo "make normalize-links — rewrite id-only body links to native Obsidian targets"
	@echo "make health      — full vault health report (writes VAULT-HEALTH-REPORT.md)"
	@echo "make study       — regenerate study queue + next session sheet"
	@echo "make indexes     — regenerate plain-md indexes + MOC auto-blocks + query eval"
	@echo "make refresh     — indexes + study + freshness (weekly maintenance bundle)"
	@echo "make secretscan  — scan both repos for credential-shaped content"
	@echo "make console     — rebuild the visual knowledge console (audit/agent view)"
	@echo "make learning-view — rebuild Irene 的学习地图 (human view, dist/ibrain-learning.html)"
	@echo "make test        — run pytest suite"
	@echo "make publish     — rebuild ./vault from a private vault (SOURCE=...)"
	@echo "make site        — build the public site into docs/ (GitHub Pages)"

bootstrap:
	python3 -m venv .venv
	$(PIP) install -q -r requirements.txt
	@echo "bootstrap done — try: make validate"

ingest:
	$(PY) scripts/ingest_xlsx.py
	$(PY) scripts/ingest_chat_export.py

validate:
	$(PY) scripts/validate_frontmatter.py
	$(PY) scripts/detect_duplicate_ids.py
	$(PY) scripts/check_wikilinks.py
	$(PY) scripts/check_confidentiality.py

normalize-links:
	$(PY) scripts/normalize_wikilinks.py --write

health:
	$(PY) scripts/vault_health.py

study:
	$(PY) scripts/generate_study_queue.py

indexes:
	$(PY) scripts/generate_indexes.py
	$(PY) scripts/generate_mocs.py
	$(PY) scripts/build_query_eval.py

refresh: indexes study
	$(PY) scripts/check_source_freshness.py
	$(PY) scripts/find_orphan_notes.py
	$(PY) scripts/detect_duplicate_entities.py --report

secretscan:
	$(PY) scripts/secret_scan.py

console:
	$(PY) scripts/build_console.py

learning-view:
	$(PY) scripts/build_learning_view.py

score:
	$(PY) scripts/compute_score.py

publish:
	@test -n "$(SOURCE)$(VAULT_PATH)" || (echo 'set SOURCE=/path/to/private-vault (or VAULT_PATH)'; exit 1)
	$(PY) scripts/build_public_vault.py $(if $(SOURCE),--source $(SOURCE),)
	$(MAKE) indexes
	$(MAKE) validate
	$(PY) scripts/build_public_vault.py --verify

site:
	$(PY) scripts/build_learning_view.py --out docs/index.html
	$(PY) scripts/build_console.py --public-only --max-confidentiality public-source
	cp dist/ibrain-console-public.html docs/graph.html
	@echo "site → docs/index.html + docs/graph.html"

test:
	$(PY) -m pytest tests/ -q

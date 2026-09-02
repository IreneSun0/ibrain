# `make publish SOURCE=/path/to/private-vault` (or set VAULT_PATH)
SOURCE ?=
# The vault resolves to ./vault (bundled) unless VAULT_PATH is set.

PY := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: bootstrap validate health indexes refresh test secretscan publish site help

help:
	@echo "make bootstrap   — create venv + install deps"
	@echo "make validate    — frontmatter + ids + wikilinks + confidentiality"
	@echo "make health      — soft audits: evidence, freshness, orphans, duplicates"
	@echo "make indexes     — regenerate plain-md indexes + MOC auto-blocks"
	@echo "make refresh     — indexes + health (weekly maintenance bundle)"
	@echo "make secretscan  — scan the tree for credential-shaped content"
	@echo "make test        — run pytest suite"
	@echo "make publish     — rebuild ./vault from a private vault (SOURCE=...)"
	@echo "make site        — build the public site into docs/ (GitHub Pages)"

bootstrap:
	python3 -m venv .venv
	$(PIP) install -q -r requirements.txt
	@echo "bootstrap done — run: make validate"

validate:
	$(PY) scripts/validate_frontmatter.py
	$(PY) scripts/detect_duplicate_ids.py
	$(PY) scripts/check_wikilinks.py
	$(PY) scripts/check_confidentiality.py

health:
	$(PY) scripts/check_evidence_coverage.py
	$(PY) scripts/check_source_freshness.py
	$(PY) scripts/find_orphan_notes.py
	$(PY) scripts/detect_duplicate_entities.py --report

indexes:
	$(PY) scripts/generate_indexes.py
	$(PY) scripts/generate_mocs.py

refresh: indexes health

secretscan:
	$(PY) scripts/secret_scan.py

publish:
	@test -n "$(SOURCE)$(VAULT_PATH)" || (echo 'set SOURCE=/path/to/private-vault (or VAULT_PATH)'; exit 1)
	$(PY) scripts/build_public_vault.py $(if $(SOURCE),--source $(SOURCE),)
	$(MAKE) indexes
	$(MAKE) validate
	$(PY) scripts/build_public_vault.py --verify

site:
	$(PY) scripts/build_learning_view.py --out docs/index.html
	@echo "site → docs/index.html"

test:
	$(PY) -m pytest tests/ -q

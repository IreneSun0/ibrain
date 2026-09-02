# `make publish SOURCE=/path/to/private-vault` (or set VAULT_PATH)
SOURCE ?=
# CryptoAtlas — command interface
# The vault resolves to ./vault (bundled) unless VAULT_PATH is set.

PY := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: bootstrap validate normalize-links health indexes refresh test secretscan publish site help

help:
	@echo "make bootstrap   — create venv + install deps"
	@echo "make validate    — frontmatter + duplicate ids + wikilinks (hard checks)"
	@echo "make normalize-links — rewrite id-only body links to native Obsidian targets"
	@echo "make health      — full vault health report (writes VAULT-HEALTH-REPORT.md)"
	@echo "make indexes     — regenerate plain-md indexes + MOC auto-blocks"
	@echo "make refresh     — indexes + freshness + orphans (weekly maintenance bundle)"
	@echo "make secretscan  — scan both repos for credential-shaped content"
	@echo "make test        — run pytest suite"
	@echo "make publish     — rebuild ./vault from a private vault (SOURCE=...)"
	@echo "make site        — build the public site into docs/ (GitHub Pages)"

bootstrap:
	python3 -m venv .venv
	$(PIP) install -q -r requirements.txt
	@echo "bootstrap done — try: make validate"

validate:
	$(PY) scripts/validate_frontmatter.py
	$(PY) scripts/detect_duplicate_ids.py
	$(PY) scripts/check_wikilinks.py
	$(PY) scripts/check_confidentiality.py

normalize-links:
	$(PY) scripts/normalize_wikilinks.py --write

health:
	$(PY) scripts/vault_health.py

indexes:
	$(PY) scripts/generate_indexes.py
	$(PY) scripts/generate_mocs.py

refresh: indexes
	$(PY) scripts/check_source_freshness.py
	$(PY) scripts/find_orphan_notes.py
	$(PY) scripts/detect_duplicate_entities.py --report

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

<h1 align="center">iBrain</h1>

<p align="center">
  <b>A prediction-market knowledge base where every claim carries its evidence tier —<br>and the engine that refuses to let that slip.</b>
</p>

<p align="center">
  <a href="https://irenesun0.github.io/ibrain"><b>📖 Read the knowledge base</b></a> ·
  <a href="https://irenesun0.github.io/ibrain/graph.html">🕸 Explore the graph</a> ·
  <a href="README.zh-CN.md">🇨🇳 中文</a>
</p>

<p align="center">
  <img alt="CI" src="https://github.com/IreneSun0/ibrain/actions/workflows/ci.yml/badge.svg">
  <img alt="notes" src="https://img.shields.io/badge/notes-297-blue">
  <img alt="code" src="https://img.shields.io/badge/code-Apache--2.0-green">
  <img alt="content" src="https://img.shields.io/badge/content-CC%20BY%204.0-green">
</p>

---

Most AI-generated knowledge bases are confident slop. They read well, cite nothing,
and quietly promote a guess into a fact somewhere between the first draft and the
tenth. This repo is an attempt at the opposite: a real knowledge base on a real
subject, where **the epistemic rules are enforced by CI rather than by good intentions.**

It ships as two things in one repo.

## 1. The vault — 297 notes on prediction market infrastructure

An interlinked, sourced knowledge base covering how event markets actually work:
order books, market making, clearing and settlement, oracles and resolution, the
risk taxonomy, the venues, and the people who run them.

|  | count |
|---|---:|
| concepts | 143 |
| entities (venues, firms, protocols, regulators, jurisdictions, people) | 71 |
| typed relationships | 11 |
| source notes | 21 |
| prerequisite + semantic edges | 285 |
| **total notes / links** | **297 / 1,078** |

It is also a **course**: an 81-quest mainline through the material, derived as the
prerequisite closure of a target skill set, arranged in topological order across
9 chapters. That is what the [site](https://irenesun0.github.io/ibrain) renders.

## 2. The engine — the part you can reuse

24 Python scripts, 58 tests, a write-time validation hook, 7 Claude Code
subagents and 12 skills. Point it at your own vault and it enforces the same
discipline on your domain.

```bash
git clone https://github.com/IreneSun0/ibrain && cd ibrain
make bootstrap     # venv + deps
make validate      # frontmatter · duplicate ids · broken links · confidentiality
make site          # → docs/index.html
```

A fresh clone resolves to the bundled `vault/`, so every target works with no
configuration. Point at your own with `VAULT_PATH=/path/to/vault make validate`.

## What makes it different

Six rules, each backed by a script that fails the build:

| Rule | Enforced by |
|---|---|
| **Every claim sits in one of five tiers** — confirmed / inference / hypothesis / unverified / unknown — and says which, visibly | `validate_frontmatter.py` |
| **`verified` requires a source note** with a content hash and an access date | `validate_frontmatter.py`, `check_source_freshness.py` |
| **Compiled truth is separated from an append-only evidence timeline.** Corrections append; they never overwrite history | vault policy §3, review in `vault-auditor` |
| **Deterministic work is never done by an LLM** — ids, hashes, slugs, indexes, link resolution are code | `brainlib.py` + all generators |
| **Confidentiality is a typed ceiling**, and a note may never be less protected than its own sources | `check_confidentiality.py` |
| **Nothing publishes by accident** — the public tree is *derived* from the private vault by a reviewable script | `build_public_vault.py` |

That last one is the part most projects get wrong, so it is worth spelling out.

### Publication is a build step, not a promise

The private vault is the single source of truth. `scripts/build_public_vault.py`
materialises the publishable subset, and every exclusion rule is declared at the
top of that one file:

- whole private trees, personal working state, and vault-ops artifacts are dropped
- anything above the `public-source` confidentiality tier is dropped
- **cascade**: a relationship whose counterparty was withheld is withheld too, so
  the published graph stays closed under its own references
- project-specific commentary sections are stripped
- deterministic rewrites remove private identifiers everywhere at once, so
  republishing never depends on a human remembering to edit a file

It writes a `PUBLICATION.md` manifest saying how many notes were withheld and why.
Re-running it is idempotent, and CI runs `make validate` against the result.

## Repo layout

```
vault/            the published knowledge base (generated — edit the private vault)
scripts/          24 deterministic tools: validators, importers, generators, exporters
tests/            58 tests, including the confidentiality-ceiling regression guards
.claude/          7 subagents + 12 skills + the write-time validation hook
docs/             the built site (GitHub Pages)
```

| script group | what it does |
|---|---|
| `validate_frontmatter` · `detect_duplicate_ids` · `check_wikilinks` · `check_confidentiality` | the hard gates — `make validate` |
| `check_evidence_coverage` · `check_source_freshness` · `find_orphan_notes` · `detect_duplicate_entities` | the soft audits — `make health` |
| `ingest_xlsx` · `ingest_chat_export` · `normalize_wikilinks` | idempotent importers |
| `generate_indexes` · `generate_mocs` · `generate_study_queue` | derived pages |
| `export_graph` · `build_console` · `build_learning_view` | the graph and the site |
| `build_public_vault` · `secret_scan` | the publication gate |

## Fork it for your own domain

Nothing above is specific to prediction markets. To reuse it:

1. Keep `scripts/`, `tests/`, `.claude/`, and `vault/90_META/` — schemas, the
   policy constitution, the relationship taxonomy, and 18 note templates.
2. Delete the rest of `vault/` and write your own notes against those templates.
3. `make validate` will tell you, immediately and specifically, where you cheated.

The `.claude/` directory is the interesting part if you work with Claude Code: the
subagents have hard role boundaries (the researcher may not grade importance, the
strategist may not create decision pages), and the PostToolUse hook re-validates
every markdown write and hands violations straight back to the model.

## Status

Note maturity is visible in the frontmatter of every page and in the graph export:
85 verified, 36 reviewed, 173 seed, 3 stale. Seed notes are structurally complete
and sourced but are still being expanded; the concept spine is being rewritten to
full depth chapter by chapter. Nothing is presented as more settled than it is —
that is the whole point of the tiers.

## License

- **Code** (`scripts/`, `tests/`, `hooks/`, `.claude/`, `Makefile`) — [Apache-2.0](LICENSE)
- **Content** (`vault/`, `docs/`) — [CC BY 4.0](LICENSE-CONTENT)

Attribution for the content: *iBrain, Irene Sun*. Source notes remain the property
of their original publishers and are cited, not reproduced.

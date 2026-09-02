<h1 align="center">CryptoAtlas</h1>

<p align="center">
  <b>An open, sourced map of how crypto markets are actually built —<br>
  where every claim carries its evidence tier, and CI rejects the ones that don't.</b>
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas"><b>🗺 Open the atlas</b></a> ·
  <a href="CONTRIBUTING.md">➕ Add or correct an entry</a> ·
  <a href="README.md">🇨🇳 中文</a>
</p>

<p align="center">
  <img alt="CI" src="https://github.com/ailinsun/cryptoatlas/actions/workflows/ci.yml/badge.svg">
  <img alt="notes" src="https://img.shields.io/badge/notes-292-4c8fd6">
  <img alt="links" src="https://img.shields.io/badge/links-2%2C813-4c8fd6">
  <img alt="code" src="https://img.shields.io/badge/code-Apache--2.0-3faa8e">
  <img alt="content" src="https://img.shields.io/badge/content-CC%20BY%204.0-3faa8e">
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas">
    <img src=".github/assets/graph.webp" alt="The CryptoAtlas knowledge graph" width="100%">
  </a>
</p>

---

Concepts, venues, market makers, regulators, people — and **who founded, funded,
settles on, regulates and makes markets for whom**. All interlinked, all tiered by
evidence.

One thing sets it apart: **the discipline is enforced by CI, not by good intentions.**
Marked `verified` with no source note — the build fails. A relationship asserted with
no evidence — the build fails. Corrections append to a timeline; they never overwrite
history.

## What's inside

|  | count |
|---|---:|
| concepts — order books, clearing, derivatives, custody, oracles, resolution, institutional risk | **143** |
| entities — venues, market makers, funds, protocols, regulators, jurisdictions, people | **76** |
| typed relationships between them | **75** |
| worked case studies (real disputes, with the money and the outcome) | 3 |
| source notes | 21 |
| **total notes / links** | **292 / 2,813** |

Every concept is written out in full: definition, why it matters, the mechanism, a
worked numeric example, the common misconceptions, an applied checklist, self-test
questions. Maturity is visible — 216 reviewed · 46 verified · 23 seed · 3 stale.

## Contributing

**A venue changes its fees, a regulator shifts position, a market maker enters or
leaves — and a note goes stale.** If you work in this industry, you know something
this map doesn't.

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap     # venv + dependencies
make validate      # tells you exactly what a claim is still missing
```

You don't have to guess the rules — the validators name them. Rejected: `verified`
without a source, broken links, duplicate ids, relationships without evidence.

| | what | where to start |
|---|---|---|
| **Correct** | a stale fact, a wrong date, a changed fee | [open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) |
| **Add an entity** | a missing venue, fund, protocol or regulator | [CONTRIBUTING.md](CONTRIBUTING.md#adding-an-entity) |
| **Add a concept** | a mechanism the map doesn't explain yet | [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-concept) |

Pointing out that an entry is wrong is worth as much as adding one.

## The engine

15 Python scripts · 42 tests · a write-time validation hook · 6 subagents · 7 skills.
Point it at your own vault (`VAULT_PATH=/path/to/vault`) and the same discipline
applies to your domain.

| rule | enforced by |
|---|---|
| every claim lands in one of five tiers (confirmed / inference / hypothesis / unverified / unknown), visibly | `validate_frontmatter.py` |
| `verified` requires a source note with a content hash and an access date | `check_source_freshness.py` |
| confidentiality is a typed ceiling: a note never sits below its own source | `check_confidentiality.py` |
| the public tree is **derived** from a private one by a reviewable script | `build_public_vault.py` |

That last one is where most projects go wrong. Every exclusion rule in
`build_public_vault.py` is declared at the top of the file, including a **cascade**
rule — a relationship note whose counterparty was withheld is withheld too, so the
published graph stays closed under its own references.

## Layout

```
vault/       the knowledge base — 292 notes (generated from a private source vault)
scripts/     15 deterministic tools: validators, generators, exporters
tests/       42 tests, including a regression guard on the confidentiality ceiling
.claude/     6 subagents + 7 skills + the write-time validation hook
```

To reuse the engine: keep `scripts/`, `tests/`, `.claude/` and `vault/90_META/`
(schema, policy, relationship vocabulary, 18 templates), delete the rest of `vault/`,
and write your own notes.

## License

**Code** (`scripts/`, `tests/`, `hooks/`, `.claude/`, `Makefile`) [Apache-2.0](LICENSE) ·
**Content** (`vault/`, `docs/`) [CC BY 4.0](LICENSE-CONTENT)

Attribution: *CryptoAtlas*, https://github.com/ailinsun/cryptoatlas. Source notes record
metadata and summaries with attribution; they do not reproduce the originals.

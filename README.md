<h1 align="center">CryptoAtlas</h1>

<p align="center">
  <b>An open, sourced map of how crypto markets are actually built —<br>
  where every claim carries its evidence tier, and CI rejects the ones that don't.</b>
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas"><b>🗺 Open the atlas</b></a> ·
  <a href="CONTRIBUTING.md">➕ Add or correct an entry</a> ·
  <a href="README.zh-CN.md">🇨🇳 中文</a>
</p>

<p align="center">
  <img alt="CI" src="https://github.com/ailinsun/cryptoatlas/actions/workflows/ci.yml/badge.svg">
  <img alt="notes" src="https://img.shields.io/badge/notes-293-4c8fd6">
  <img alt="links" src="https://img.shields.io/badge/links-2%2C813-4c8fd6">
  <img alt="code" src="https://img.shields.io/badge/code-Apache--2.0-3faa8e">
  <img alt="content" src="https://img.shields.io/badge/content-CC%20BY%204.0-3faa8e">
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas">
    <img src=".github/assets/graph.webp" alt="CryptoAtlas — the live knowledge graph" width="100%">
  </a>
</p>

---

Most crypto "knowledge bases" are link dumps or confident AI slop. They read fluently,
cite nothing, and somewhere between the first draft and the tenth a guess quietly
becomes a fact.

This one is built the other way round: **the epistemic rules are enforced by CI, not by
good intentions.** A claim marked `verified` without a source note fails the build. A
relationship asserted without evidence fails the build. Corrections append to a timeline
instead of overwriting history. Nothing is presented as more settled than it is.

The front page is a live map of the whole thing — **who founded, funded, settles on,
regulates and makes markets for whom**, drawn from 293 interlinked notes.

## What's inside

|  | count |
|---|---:|
| concepts — order books, clearing, derivatives, custody, oracles, resolution, institutional risk | **143** |
| entities — venues, market makers, funds, protocols, regulators, jurisdictions, people | **76** |
| typed relationships between them | **75** |
| worked case studies (real disputes, with the money and the outcome) | 3 |
| source notes | 21 |
| **total notes / links** | **293 / 2,813** |

Every concept is written out in full — a precise definition, why it matters, the
mechanism, a worked numeric example, the common misconceptions, an applied checklist,
and active-recall questions. Median length is about 2,000 characters.

Event and prediction markets are the deepest thread, because that is where settlement
gets hardest — but they are one vertical inside a wider map, not the whole of it.

## Contributing — this is the point

**Crypto moves faster than any one person can track.** A venue changes its fee model, a
regulator shifts position, a market maker enters or leaves — and a note goes stale. If
you work in this industry, you already know things this atlas doesn't.

Contributing here is unusually easy to get *right*, because the validator tells you
exactly what's missing:

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap          # venv + deps
# edit or add a note under vault/
make validate           # tells you precisely what your claim is missing
```

It will refuse a `verified` status with no source, a broken link, a duplicate id, a
relationship with no evidence. **You don't have to guess the house style — the build
enforces it.**

Three ways in, smallest first:

| | what | where to start |
|---|---|---|
| **Correct something** | a stale fact, a wrong date, a changed fee | [open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) |
| **Add an entity** | a venue, fund, protocol or regulator that's missing | [CONTRIBUTING.md](CONTRIBUTING.md#adding-an-entity) |
| **Add a concept** | a mechanism the atlas doesn't explain yet | [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-concept) |

Where an entity has no documented link to some part of the market, the note says
`UNKNOWN` and explains why the absence is informative. **Telling us what an entry gets
wrong is as valuable as adding a new one.**

## The engine — fork it for your own domain

22 Python scripts, 57 tests, a write-time validation hook, 6 Claude Code subagents and
11 skills. Point it at your own vault and it enforces the same discipline on your field.

A fresh clone resolves to the bundled `vault/`, so every target works with no
configuration. Point elsewhere with `VAULT_PATH=/path/to/vault make validate`.

Six rules, each backed by a script that fails the build:

| Rule | Enforced by |
|---|---|
| **Every claim sits in one of five tiers** — confirmed / inference / hypothesis / unverified / unknown — and says which, visibly | `validate_frontmatter.py` |
| **`verified` requires a source note** with a content hash and an access date | `validate_frontmatter.py`, `check_source_freshness.py` |
| **Compiled truth is separated from an append-only evidence timeline.** Corrections append; they never overwrite history | vault policy §3 |
| **Deterministic work is never done by an LLM** — ids, hashes, slugs, indexes, link resolution are code | `brainlib.py` + all generators |
| **Confidentiality is a typed ceiling**, and a note may never be less protected than its own sources | `check_confidentiality.py` |
| **Nothing publishes by accident** — the public tree is *derived* from a private vault by a reviewable script | `build_public_vault.py` |

That last one is the part most projects get wrong. `scripts/build_public_vault.py`
materialises the publishable subset, and every exclusion rule is declared at the top of
that one file: private trees, personal working state, anything above the `public-source`
tier, and a cascade that withholds a relationship whose counterparty was withheld, so
the published graph stays closed under its own references. It writes a `PUBLICATION.md`
manifest recording what was held back and why.

## Layout

```
vault/       the knowledge base — 293 notes (generated from a private source vault)
scripts/     22 deterministic tools: validators, importers, generators, exporters
tests/       57 tests, including the confidentiality-ceiling regression guards
.claude/     6 subagents + 11 skills + the write-time validation hook
docs/        the built site (generated; deployed to GitHub Pages)
```

To reuse the engine: keep `scripts/`, `tests/`, `.claude/` and `vault/90_META/` — schemas,
the policy constitution, the relationship taxonomy and 18 note templates. Delete the rest
of `vault/`, write your own notes against those templates, and `make validate` will tell
you immediately and specifically where you cheated.

## Status

Note maturity is visible in the frontmatter of every page and in the graph export:
216 reviewed, 46 verified, 32 seed, 3 stale. Dynamic facts carry `last_verified` dates
and are refreshed rather than rewritten. Nothing claims to be settled that isn't — that
is the whole point of the tiers.

## Licence

- **Code** (`scripts/`, `tests/`, `hooks/`, `.claude/`, `Makefile`) — [Apache-2.0](LICENSE)
- **Content** (`vault/`, `docs/`) — [CC BY 4.0](LICENSE-CONTENT)

Attribution: *CryptoAtlas*, https://github.com/ailinsun/cryptoatlas. Source notes cite
their originals rather than reproducing them; copyright in those works stays with their
publishers.

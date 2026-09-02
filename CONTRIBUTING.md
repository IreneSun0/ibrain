# Contributing to CryptoAtlas

If you know something this atlas doesn't, or something it gets wrong, that is the
contribution worth making. You don't have to learn the conventions first — the validator
names what a claim is missing.

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap     # venv + dependencies
make validate      # should be green before you start
```

---

## Evidence tiers

**Every claim carries its evidence tier, and says which.**

| Tier | When to use it | How to mark it |
|---|---|---|
| **Confirmed fact** | A reliable source supports it | `epistemic_status: confirmed` + `[Source: [[src-…]]]` inline |
| **Inference** | You reasoned it from facts | mark `(inference)` inline |
| **Hypothesis** | Plausible, untested | `epistemic_status: hypothesis` |
| **Unverified** | Reported, not confirmed | mark `(unverified)` inline |
| **Unknown** | Not disclosed, or a search turned up nothing | say which, with a date — never a placeholder, never a guess |

Write a gap as a claim, not a shrug: "as of 2026-08 a targeted search found no public
event-market activity" can be disproved, a placeholder cannot. And if the absence answers
nothing the reader came with, leave the line out rather than reporting it.

**Two things the build will reject outright:**
- `status: verified` on a note with no source note behind it
- a relationship asserted without evidence

---

## Correcting something

1. [Open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) — say which note, what's wrong, and what it should be.
2. Name your source. Without one, say so — a flagged uncertainty is still worth filing.

Or fix it directly: edit the note, **append** a dated line to its `## Timeline` section
explaining the correction, and open a PR. Timelines are append-only: a correction is a new entry that
supersedes an old one, and both stay visible.

---

## Adding an entity

Venues, market makers, funds, protocols, regulators, jurisdictions, people.

1. Copy the matching template from `vault/90_META/templates/` (`tpl-exchange-venue.md`,
   `tpl-market-maker-fund.md`, `tpl-organization.md`, `tpl-regulator.md`, …).
2. Put it in the right folder under `vault/03_ENTITIES/`.
3. Fill the sections. The house shape is:
   - **Executive Summary** — what it is and the one fact that matters most
   - **What It Actually Is** — the distinction people get wrong
   - **How It Works** — the mechanism, concretely
   - **Position in the Market** — where it sits relative to everyone else
   - **What Could Break It** — the real risks, not boilerplate
   - **What To Watch** — the indicators that would change the picture
4. Add typed relationships in frontmatter `related:` using the vocabulary in
   `vault/90_META/taxonomy/relationship-types.md` — `founded`, `invested-in`,
   `provides-liquidity-to`, `settles-on`, `regulated-by`, and so on. Each edge needs a
   `note` saying why it holds.
5. `make validate`.

**What makes an entry good** — not "X is a large market maker" but "X has every
capability and has not entered this market, because a pure market maker will not carry an
unhedgeable book. That is a fact about the market, not about X."

---

## Adding a concept

1. Copy `vault/90_META/templates/tpl-concept.md` into the right domain folder under
   `vault/02_CONCEPTS/`.
2. Sections, in order: definition · why it matters · how it works · a **worked numeric
   example** · common misconceptions · in practice · active-recall questions.
3. Set `prerequisites:` (only hard ones — "you genuinely cannot read this page without
   that one") and typed `related:` edges.
4. `make validate`.

**The worked example is not optional.** A concept explained without numbers is a
definition, not an explanation.

---

## House style

- **Chinese is the primary language**; English technical terms stay in English
  (`spread`, `CLOB`, `adverse selection`) — do not translate them away.
- Write for someone smart who does not yet know this field. No condescension, no jargon
  stacking.
- Say what would falsify a claim, not just what supports it.
- Where two sources conflict, **keep both and explain the conflict.** Do not adjudicate
  silently.

---

## What gets rejected

- A claim with no tier and no source
- A relationship inferred from ecosystem association ("both are in DeFi, so they must be
  partners")
- Marketing copy for any project, including your own
- Rewriting someone's original wording under `vault/09_ORIGINALS/`
- Silent edits to an existing timeline entry

---

## Running the checks

```bash
make validate    # hard gates: frontmatter, duplicate ids, links, confidentiality
make test        # 42 tests
make health      # soft audits: evidence coverage, stale sources, orphans
make site        # rebuild docs/
```

CI runs the hard gates, the secret scan, the confidentiality ceiling and the tests on
every PR.

---

## Licences

By contributing you agree that your content is licensed under [CC BY 4.0](LICENSE-CONTENT)
and any code under [Apache-2.0](LICENSE).

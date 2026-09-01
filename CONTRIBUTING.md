# Contributing to CryptoAtlas

The atlas is only as current as the people who work in this market. A venue changes its
fee model, a regulator shifts position, a market maker enters or leaves — and a note goes
stale. **If you know something this atlas doesn't, or something it gets wrong, that is
exactly the contribution wanted.**

Contributing here is unusually easy to get right, because the validator tells you what is
missing before a reviewer has to.

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap     # venv + dependencies
make validate      # should be green before you start
```

---

## The one rule that matters

**Every claim carries its evidence tier, and says which.**

| Tier | When to use it | How to mark it |
|---|---|---|
| **Confirmed fact** | A reliable source supports it | `epistemic_status: confirmed` + `[Source: [[src-…]]]` inline |
| **Inference** | You reasoned it from facts | mark `(inference)` inline |
| **Hypothesis** | Plausible, untested | `epistemic_status: hypothesis` |
| **Unverified** | Reported, not confirmed | mark `(unverified)` inline |
| **Unknown** | Nobody knows, or you couldn't find out | write `UNKNOWN` — do not guess |

`UNKNOWN` is a first-class answer here. An entry that says "this firm has no documented
event-market activity, and here is why that absence is informative" is more useful than
one that quietly implies otherwise.

**Two things the build will reject outright:**
- `status: verified` on a note with no source note behind it
- a relationship asserted without evidence

---

## Correcting something

The lowest-friction and most valuable contribution.

1. [Open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) — say which note, what's wrong, and what it should be.
2. If you have a source, name it. If you don't, say so; a flagged uncertainty still helps.

Or fix it directly: edit the note, **append** a dated line to its `## Timeline` section
explaining the correction, and open a PR. Timelines are append-only — never edit or
delete an existing entry. A correction is a new entry that supersedes an old one, and
both stay visible.

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

**What makes an entry good**: it lands on something a reader can use. Not "X is a large
market maker" but "X has every capability and has not entered this market — because a
pure market maker will not carry an unhedgeable book, which is a fact about the market,
not about X."

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
make test        # 57 tests
make health      # soft audits: evidence coverage, stale sources, orphans
make site        # rebuild docs/
```

CI runs the hard gates, the secret scan, the confidentiality ceiling and the test suite
on every PR. If it's green, a reviewer only has to judge the substance.

---

## Licences

By contributing you agree that your content is licensed under
[CC BY 4.0](LICENSE-CONTENT) and any code under [Apache-2.0](LICENSE).

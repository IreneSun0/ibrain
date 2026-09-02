# Contributing to CryptoAtlas

Use a correction issue or pull request to add an entry or correct a claim. The validator
reports missing claim metadata.

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap     # venv + dependencies
make validate      # verify the checkout
```

---

## Evidence tiers

Assign every claim an evidence tier.

| Tier | When to use it | How to mark it |
|---|---|---|
| **Confirmed fact** | A reliable source supports it | `epistemic_status: confirmed` + `[Source: [[src-…]]]` inline |
| **Inference** | You reasoned it from facts | mark `(inference)` inline |
| **Hypothesis** | Plausible, untested | `epistemic_status: hypothesis` |
| **Unverified** | Reported, not confirmed | mark `(unverified)` inline |
| **Unknown** | Not disclosed, or a search turned up nothing | say which, with a date — never a placeholder, never a guess |

For a negative finding, state the search scope and date so that the claim can be checked.
Omit the line when the absence does not answer the entry's question.

The build rejects:
- `status: verified` on a note with no source note behind it
- a relationship asserted without evidence

---

## Correcting something

1. [Open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) — say which note, what's wrong, and what it should be.
2. Name the source. If there is none, mark the claim unverified.

Or fix it directly: edit the note, then add a dated line under a `## Timeline` heading at
the end of it — create the heading if the note has none — and open a PR. Never edit or
delete an existing entry; a correction is a new line that supersedes the old one, and both
stay visible. Published notes carry no build history, so a timeline you find there is a
record of substantive change.

---

## Adding an entity

Venues, market makers, funds, protocols, regulators, jurisdictions, people.

1. Copy the matching template from `vault/90_META/templates/` (`tpl-exchange-venue.md`,
   `tpl-market-maker-fund.md`, `tpl-organization.md`, `tpl-regulator.md`, …).
2. Put it in the right folder under `vault/03_ENTITIES/`.
3. Fill these sections:
   - **Executive Summary** — what it is and its main market implication
   - **What It Actually Is** — its scope and relevant distinctions
   - **How It Works** — the mechanism, concretely
   - **Position in the Market** — its relationship to other participants
   - **What Could Break It** — specific failure modes
   - **What To Watch** — indicators that would change the assessment
4. Add typed relationships in frontmatter `related:` using the vocabulary in
   `vault/90_META/taxonomy/relationship-types.md` — `founded`, `invested-in`,
   `provides-liquidity-to`, `settles-on`, `regulated-by`, and so on. Each edge needs a
   `note` saying why it holds.
5. `make validate`.

---

## Adding a concept

1. Copy `vault/90_META/templates/tpl-concept.md` into the right domain folder under
   `vault/02_CONCEPTS/`.
2. Sections, in order: definition · why it matters · how it works · a **worked numeric
   example** · common misconceptions · in practice · active-recall questions.
3. Set `prerequisites:` to concepts required to understand the page, and add typed
   `related:` edges.
4. `make validate`.

---

## House style

- **Chinese is the primary language**; English technical terms stay in English
  (`spread`, `CLOB`, `adverse selection`) — do not translate them away.
- Assume general expertise but no prior familiarity with this field. Avoid condescension
  and jargon stacking.
- Say what would falsify a claim, not just what supports it.
- Where two sources conflict, **keep both and explain the conflict.** Do not adjudicate
  silently.

---

## What gets rejected

- A claim with no tier and no source
- A relationship inferred from ecosystem association ("both are in DeFi, so they must be
  partners")
- Marketing copy for any project, including the contributor's
- Rewriting someone's original wording under `vault/09_ORIGINALS/`
- Silent edits to an existing timeline entry

---

## Running the checks

```bash
make validate    # hard gates: frontmatter, duplicate ids, links, confidentiality
make test        # test suite
make health      # soft audits: evidence coverage, stale sources, orphans
make site        # rebuild docs/
```

CI runs the hard gates, the secret scan, the confidentiality ceiling and the tests on
every PR.

---

## Licences

By contributing you agree that your content is licensed under [CC BY 4.0](LICENSE-CONTENT)
and any code under [Apache-2.0](LICENSE).

# Scalar Market

## Definition

A **scalar market** settles anywhere on a **continuous range** rather than at $1 or $0.

The question is not "will it happen" but "how much": what will CPI be, what vote share, what temperature. Settlement interpolates linearly between the bounds.

## Why It Matters

Binary contracts flatten the world into yes/no, and a great many real exposures are not that shape.

A company does not care whether a tariff is imposed; it cares by how many percentage points, because its costs are a continuous function of that number. **Approximating a continuous quantity with a ladder of binaries means opening many books, each one thinner** (see [[multi-outcome-market]]). A scalar contract does it in one.

The cost: it is harder to price, harder to make markets in, and harder to write unambiguously.

## How It Works

Settlement:

```
settlement = clamp(actual, lower, upper)
payout per contract = (settlement − lower) / (upper − lower)
```

A CPI contract with range [2%, 4%] and an actual print of 3.2% pays (3.2−2)/(4−2) = **0.60**.

**Three things the terms must nail down:**
1. **The bounds** — what happens to a print outside the range: clamp, or void?
2. **Precision** — how many decimals, and rounded or truncated?
3. **Revisions** — official statistics get revised; does the first print govern, or the revised one?

**The third matters far more here than in a binary market**, because a revision of 0.1pp changes the payout directly.

## Concrete Example

"How much will the Fed cut" in three market shapes:

| Shape | Contracts | Liquidity | Expressiveness |
|---|---|---|---|
| Binary ("will it cut") | 1 | Concentrated | Coarsest |
| Multi-outcome (0 / 25bp / 50bp) | 3 | Split three ways | Middling |
| **Scalar (0–75bp)** | **1** | **Concentrated** | **Finest** |

**The scalar form is theoretically the best of the three**: one contract, undivided liquidity, continuous expression.

**It is rare in practice because of market making.** A maker must quote across the whole range, its exposure is continuous, and hedging and inventory management are an order of magnitude harder than in a binary. This is a "theoretically optimal, engineering-unsolved" position.

## Common Misconceptions

- **"A scalar market is just many binaries."** Economically similar, but liquidity is not: one scalar book concentrates depth, a ladder of binaries fragments it.
- **"The price is still a probability."** A scalar price is a normalised *expected value*, not a probability. It reads differently.
- **"Wider bounds are safer."** Wider bounds mean each cent of price covers more of the underlying quantity — less precision — and raise the chance of a clamped extreme.

## In Practice

Work out three numbers before trading one:

1. **The implied level** = lower + price × (upper − lower).
2. **The price implied by your own view**, compared with the market's.
3. **Clamp risk** — how likely is the outcome to land outside the range? Outside, you receive a bound that may be far from your thesis.

**Then read one clause: how revisions are handled.** It is the most commonly skipped and most expensive detail in a scalar contract.

## Active Recall

- Q: How does a scalar market differ fundamentally from a binary one?
  A: It settles anywhere on a continuous range by linear interpolation rather than at $1/$0 — the question is 'how much', not 'whether'.
- Q: Which three things must a scalar contract's terms nail down?
  A: The bounds (and what happens outside them), precision (decimals and rounding), and how official revisions are treated.
- Q: Why is the theoretically optimal scalar form rare in practice?
  A: Market makers must quote the whole continuous range; exposure is continuous and hedging and inventory management are an order of magnitude harder than in a binary.

---

> 中文原页: [`scalar-market.md`](./scalar-market.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


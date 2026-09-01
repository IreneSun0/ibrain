# Combinatorial Market

## Definition

A **combinatorial market** lets you trade the **joint outcome of several events**: "A wins *and* inflation stays under 3%".

It is far more expressive than single-event markets — real-world risk is almost always conditional — and it runs into a hard mathematical wall.

## Why It Matters

Because **most real exposures are conditional**.

A company's tariff cost depends on which party governs *and* whether a trade deal lands; a fund's risk depends on the interaction of a rate cut *and* an earnings season. Single-event contracts cannot express those interactions: betting on each separately is not the same as betting on the combination.

**Combinatorial markets are the only form that expresses conditional risk directly.**

## How It Works

The wall is a **combinatorial explosion of liquidity**:

```
N events → 2^N joint outcomes
```

- 3 events → 8 corners
- 10 events → **1,024 corners**
- 20 events → **over a million**

Every corner needs somebody to quote and somebody to take the other side. **Most corners are empty**, and an empty corner cannot trade or price.

**The academic answer** is an automated market maker (Hanson's LMSR family) that maintains consistent prices across the entire joint space: no resting order needed per corner, and the formula guarantees an arbitrage-free price everywhere (see [[automated-market-maker]]).

**The practical reality** is that real volume concentrates in a handful of political conditional pairs; the rest have prices but no trades.

## Concrete Example

The joint space of a three-event market:

| A | B | C | Joint probability |
|---|---|---|---|
| ✓ | ✓ | ✓ | 0.08 |
| ✓ | ✓ | ✗ | 0.12 |
| ✓ | ✗ | ✓ | 0.05 |
| … | … | … | … |
| ✗ | ✗ | ✗ | 0.21 |

**The eight rows must sum to 1**, and must agree with the single-event marginals: P(A) equals the sum of the four rows containing A.

**That consistency constraint is the point.** A combinatorial market forces every related contract to price coherently; a pile of independent single-event contracts cannot, and their implied joint distribution may be internally contradictory.

**Distinguish it from a parlay.** A casino parlay is a fixed-odds ticket, not a continuously tradable market, and carries no consistency guarantee. Similar shape, different animal.

## Common Misconceptions

- **"It's the same as buying several contracts."** Buying A and buying B pays out on two independent events; buying "A and B" pays only when both hold.
- **"2^N is a compute problem."** It is a **liquidity** problem: every corner needs capital, and capital is finite. More servers do not help.
- **"Combinatorial markets are parlays."** A parlay is a fixed-odds, non-transferable ticket with no coherence constraint. Do not reason about one using the other.

## In Practice

Three questions before using one:

1. **How large is the joint space?** N events give 2^N. Past four or five events, practical usability collapses.
2. **What keeps prices coherent?** A unified LMSR-style maker, or independent books? Independent books will drift into inconsistency.
3. **Do the marginals reconcile?** Sum every joint probability containing A and compare with A's single-event price. A mismatch is either an arbitrage or a defect in the pricing mechanism.

**The third is a thirty-second coherence check and the fastest way to find a pricing flaw.**

## Active Recall

- Q: What does a combinatorial market express that single-event markets cannot?
  A: Conditional and joint risk — real exposures depend on interactions between events, and betting on each separately is not the same as betting on the combination.
- Q: What is the hard wall, and why doesn't compute solve it?
  A: Combinatorial explosion of liquidity: N events give 2^N corners, each needing capital to quote. It is a liquidity constraint, not a computational one.
- Q: How does a combinatorial market differ from a casino parlay?
  A: A parlay is a fixed-odds, non-transferable ticket with no pricing-coherence constraint; a combinatorial market is continuously tradable and forces marginals to reconcile.

---

> 中文原页: [`combinatorial-market.md`](./combinatorial-market.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


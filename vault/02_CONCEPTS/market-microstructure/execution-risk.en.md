# Execution Risk

## Definition

**Execution risk** is the risk that a correct decision is degraded — or reversed — on the way from "decide" to "filled".

Three parts: **latency** (how long the decision takes to reach the market), **slippage** (how far the fill drifts), and **non-execution** (a limit order that never trades). Together they are the gap between a strategy on paper and a strategy in production.

## Why It Matters

Event markets have an amplifier: **information arrives as a jump.**

In a price market, being a second late costs a few basis points. Here, the news breaks and the probability goes from 0.3 to 0.9 — **a second late can cost the entire edge.**

And liquidity in these markets is thinnest exactly at information moments (see [[liquidity]]): the instant you most need to trade is the instant it is hardest to.

## How It Works

The three sources need different treatments and must not be lumped together:

| Source | Symptom | Remedy |
|---|---|---|
| **Latency** | Price has moved on arrival | Closer connectivity, faster data, resting orders |
| **Slippage** | Walking the book (see [[slippage]]) | Slicing, limits, cross-venue routing |
| **Non-execution** | The limit never trades | Price more aggressively, or accept the uncertainty |

**Note that the last two are in opposition**: using limits to cut slippage raises non-execution risk; crossing the spread to guarantee a fill accepts slippage. **There is no way to eliminate both — only a choice of which to bear.**

On-chain markets add a fourth: **mempool visibility** — a large order can be seen before it is included, and front-run.

## Concrete Example

One "buy after the news" decision, three executions:

```
decision    mid 0.62
+0.5s       market order fills at 0.71    ← latency + slippage cost 9c
+2s         a 0.65 limit is still unfilled ← the whole move is missed
+30s        price settles at 0.88
```

- **Market order**: filled at 0.71, still 17c of profit.
- **Limit at 0.65**: nothing filled, zero profit.
- **No trade**: zero.

**The counter-intuitive conclusion**: in information-driven moments, **slippage is the small cost and non-execution is the large one.** In quiet conditions the ranking reverses.

**Execution policy has to switch with the regime; one fixed rule will lose at one end or the other.**

## Common Misconceptions

- **"Execution risk is an engineering problem."** It is first a *decision* problem — when to buy certainty with slippage is judgement, not plumbing.
- **"Limit orders are safer."** They remove price uncertainty and introduce fill uncertainty. **In a fast market the second is far more expensive.**
- **"A fixed slippage assumption in the backtest is enough."** It assumes the opposite of reality: real slippage is largest exactly when you most want to trade. Model it off the actual book.

## In Practice

Treat execution as a variable you decide in advance, not an accident you discover afterwards:

1. **Classify the trade** — information-driven (needs speed) or allocation-driven (needs price)?
2. **Match the policy** — the first crosses with a price cap; the second slices with limits.
3. **Record what happened** — decision price, average fill, latency, on every trade.
4. **Review** — how far did realised slippage sit from your estimate? A wide gap means your data or your route is wrong.

**Always cap a market order.** On a thin book, an uncapped market order is a blank cheque written to the market.

## Active Recall

- Q: What are the three components of execution risk?
  A: Latency (time for the decision to reach the market), slippage (fill drift), and non-execution (a limit that never trades).
- Q: Why can slippage and non-execution risk not both be eliminated?
  A: Limits cut slippage but raise non-execution; crossing guarantees the fill but accepts slippage. You choose which to bear, based on the regime.
- Q: How does execution policy differ between information-driven and allocation-driven trades?
  A: Information-driven needs speed — cross with a price cap, since missing the move costs far more than slippage. Allocation-driven needs price — slice with limits.

---

> 中文原页: [`execution-risk.md`](./execution-risk.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


# Price Impact

## Definition

**Price impact** is how far your own order moved the price.

It and [[slippage]] are two views of one event: slippage is what you overpaid, impact is how far you shifted the market. **The larger your order, the less you are a price taker and the more you are a price maker.**

## Why It Matters

On a thin book, impact has a particularly nasty property: **it leaks your intention.**

Pushing a price from 0.60 to 0.68 announces to everyone that somebody is buying size. Followers and front-runners appear, the rest of your order fills worse, and when you try to exit the price moves against you again.

**Long-tail event contracts are thin enough that a few thousand dollars produces visible impact** — which is also why the "probability" on those books is so easy for a small amount of capital to distort (see [[market-integrity]]).

## How It Works

Impact has two components that behave completely differently:

| Component | What it is | Does it revert? |
|---|---|---|
| **Temporary** | You consumed resting depth | **Yes** — makers refill and the price eases back |
| **Permanent** | The market reads your trade as informed | **No** — the price is repriced for good |

**The size of the permanent component depends on how informed the market thinks you are.** The same order from an anonymous fresh address and from a known passive index fund carry very different permanent impact.

**Recovery time is the most practical measure**: how long does the price take to return after a large trade? A book that recovers slowly is easy to enter and hard to leave.

## Concrete Example

Buying $40,000 in an event contract whose ±1% depth is $8,000:

```
before      mid 0.60
five levels avg fill 0.653       ← slippage 8.8%
after       mid 0.67             ← impact +7c
5 min later mid 0.64             ← 3c of temporary impact reverted
settles at  0.64                 ← permanent impact = 4c
```

**You paid twice**: 8.8% in slippage, and a permanent 4c repricing — which means buying more now starts from a worse level, and selling means pushing the price back down.

**For size, the real cost of trading an event market is routinely ten times the headline fee.**

## Common Misconceptions

- **"Impact is the same as slippage."** Slippage is your fill versus the arrival price; impact is the market's displacement. One order produces both, but only the second affects every trade you make afterwards.
- **"Slicing the order removes impact."** Slicing lowers instantaneous impact but lengthens exposure, and a regular slicing pattern is detectable and front-runnable.
- **"Impact only costs me."** It moves the "probability" other people are quoting. **On a thin book, price impact is a market-integrity problem, not merely an execution cost.**

## In Practice

Budget for impact before sending size:

1. **Estimate it** — walk the book and compute the post-trade mid.
2. **Set a ceiling** — beyond 2–3%, slice or route elsewhere.
3. **Measure recovery** — sample historical large trades and see how long depth and spread take to return.
4. **Price the round trip** — exiting produces impact in the opposite direction; count it.

**Step 4 is the one people skip**: most budgets cover getting in and forget that getting out costs again.

## Active Recall

- Q: What is the difference between price impact and slippage?
  A: Slippage is your fill price versus the arrival price; impact is the displacement your order caused in the market price, which affects every subsequent trade.
- Q: How do temporary and permanent impact differ?
  A: Temporary impact comes from consuming resting depth and reverts as makers refill; permanent impact is the market repricing because it read your trade as informed, and does not revert.
- Q: Why is impact on a thin book a market-integrity issue?
  A: It moves the probability that outsiders quote, and a few thousand dollars is enough to shift it — making the price easy for small capital to distort.

---

> 中文原页: [`price-impact.md`](./price-impact.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


# Order Flow

## Definition

**Order flow** is the stream of buy and sell orders arriving per unit of time.

It is not a number but a **sequence with direction, size and timestamps**. An exchange's real asset is not its matching engine but its order flow; and what a market maker actually reads is not the price but the flow.

## Why It Matters

Price is the *output* of order flow. Watching price is watching the result; watching flow is watching the process.

For a market maker, the composition of the flow is everything:
- **Uninformed flow** (hedgers, noise traders) — random direction; the maker earns the spread from it.
- **Informed flow** — one-directional and arriving only when the quote is wrong; the maker loses to it.

```
market-making P&L = uninformed contribution − informed adverse selection
```

**That equation is the key to every behaviour a maker exhibits**: widening the spread, cutting size, pulling quotes ahead of news are all adjustments to the ratio of those two terms.

## How It Works

Three dimensions worth reading:

1. **Imbalance** — buy volume minus sell volume. Sustained one-sidedness usually means somebody is building a position.
2. **Size distribution** — many small orders versus few large ones mean opposite things: retail-shaped versus institution- or insider-shaped.
3. **Clustering in time** — evenly spread or bursting? Bursts cluster around information events.

**On-chain event markets have a property traditional markets lack: the flow is partly public.** Position changes are visible on chain (see [[on-chain]]), so anyone can do the flow analysis that used to require exchange-level access.

## Concrete Example

The same "$200,000 traded in an hour", two opposite readings:

| | Flow A | Flow B |
|---|---|---|
| Trades | 400 | 6 |
| Direction | Balanced | All buys |
| Timing | Even | Compressed into 5 minutes |
| Reading | **Healthy two-way demand** | **Somebody building against the clock** |

**Flow B is the shape a market maker fears**: one-sided, large, clustered. The rational response is to widen or pull.

If the price jumps shortly after Flow B, that is not a coincidence — **flow usually leads price.**

## Common Misconceptions

- **"Volume is order flow."** Volume is a scalar total; flow is a directional, time-stamped sequence. Volume can be faked; the *shape* of flow is much harder to fake.
- **"Flow analysis needs exchange access."** Not on-chain, where position changes are public.
- **"Imbalance proves insider activity."** It may equally be hedging demand, rebalancing, or one person's conviction. **Imbalance is a signal, not a conclusion.**

## In Practice

Three steps to do this on an event market:

1. **Capture time series**, not snapshots — the timestamped trade sequence.
2. **Compute rolling imbalance** — buys minus sells over a moving window.
3. **Align it against the news timeline** — did the imbalance appear *before* the news or after?

**Step 3 is where all the value is**: large one-directional flow arriving before the news is the most direct trace of a possible information advantage (see [[inside-information]]). On-chain markets open that analysis to everyone.

## Active Recall

- Q: What is the market maker's P&L equation?
  A: Uninformed flow contribution minus informed adverse selection. It explains widening spreads, cutting size, and pulling quotes before news.
- Q: Why does flow usually lead price?
  A: Price is the output of flow: one-sided, large, clustered flow arrives first and the price moves after, so reading flow is earlier than reading price.
- Q: What is distinctive about flow analysis on on-chain event markets?
  A: Position changes are publicly readable, so anyone can perform the analysis that traditionally required exchange access — especially aligning flow against the news timeline.

---

> 中文原页: [`order-flow.md`](./order-flow.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


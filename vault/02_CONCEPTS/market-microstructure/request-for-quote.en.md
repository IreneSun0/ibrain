# RFQ

## Definition

**RFQ (request for quote)** means asking one or a few market makers privately — "what is your price in this size?" — instead of working an order on the public book.

It is standard practice for size, because **showing a large order on a public book announces your intention to everyone** before you have traded (see [[price-impact]]).

## Why It Matters

A public order book has a structural weakness for size: **visibility is itself a cost.**

Post a $5M bid and everyone sees it; the price moves before you are filled. RFQ privatises the process: only the makers you asked know, and the trade is disclosed after the fact, if at all.

**In event markets the value is amplified**, because long-tail books are thin enough that an institutional order simply does not fit on them (see [[liquidity]]).

## How It Works

The mechanics, and the trade-off:

```
1. You send a request: instrument + size + side (sometimes hidden)
2. Several makers quote independently
3. You lift one, or decline them all
```

**The core trade-off:**
- **Ask more makers** → better price competition, but **wider information leakage** (each one now knows somebody wants size).
- **Ask fewer** → less leakage, possibly a worse price.

**Hiding the side (a two-way RFQ)** is the usual defence: ask for both a bid and an offer, then choose. The quotes come back wider in exchange.

## Concrete Example

A $2M need in an event contract, two routes:

| | Public book | RFQ |
|---|---|---|
| Visibility | Immediate, to everyone | Only the makers asked |
| Expected fill | Walks several levels, avg 0.68 | Single price 0.655 |
| Price impact | +8c, only partly reverting | Near zero if undisclosed |
| Certainty | Risk of partial fill | All or nothing |

**The 2.5c saved — about $50k — is the price of not being seen.**

The cost: you have handed execution to a handful of counterparties **who now know what you want to do**. RFQ does not remove information leakage; it narrows it from "the whole market" to "the firms you asked".

## Common Misconceptions

- **"RFQ is always cheaper."** On a deep book, working the public order is usually cheaper because competition is broader. RFQ wins only when the book cannot hold you.
- **"RFQ leaks nothing."** It leaks less. The makers you asked can and do adjust their own positions.
- **"RFQ is institutions-only."** More venues are exposing RFQ-style quoting to retail as a "get a price, then trade" flow.

## In Practice

One test decides book versus RFQ:

> **How large is your order relative to this book's ±1% depth?**

- **Under 1×** → work the public book; it is cheaper.
- **1–5×** → slice or RFQ; compare.
- **Over 5×** → **the book cannot hold you**; RFQ or work it over time.

One further discipline: **ask three to five makers, not ten.** Past five, the marginal leakage usually costs more than the marginal price competition earns.

## Active Recall

- Q: Why route size through RFQ rather than the public book?
  A: A large resting order announces your intention to the whole market and the price moves before you fill; RFQ limits visibility to the few makers you asked.
- Q: What is the central trade-off in an RFQ?
  A: More makers means better price competition but wider leakage; fewer means less leakage but possibly a worse price. Three to five is the usual balance.
- Q: How do you decide between the public book and RFQ?
  A: Compare your size to the book's ±1% depth: under 1× use the book, over 5× the book cannot hold you and you should use RFQ or work the order over time.

---

> 中文原页: [`request-for-quote.md`](./request-for-quote.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


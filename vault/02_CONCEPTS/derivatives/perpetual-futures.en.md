# Perpetual Futures / Perp

## Definition

A **perpetual future** is a futures contract with no expiry. You can hold it indefinitely until you close it or are liquidated.

Removing expiry creates a problem: **with no delivery date, what anchors the price to spot?** The answer is the [[funding-rate|funding rate]] — a continuous cash flow that pulls the perpetual back toward spot.

## Why It Matters

Perpetuals are the dominant crypto derivative, and they matter here in two ways:

1. **As a contrast**: perpetuals are open-ended, margined and liquidatable; event contracts have a definite expiry, are fully collateralised, and cannot be liquidated. **The risk shapes are close to mirror images.**
2. **As a warning**: hundred-times leverage and cascading liquidations shaped the public image of "crypto derivatives", and event contracts get filed under the same heading despite being the opposite (see [[leverage]]).

## How It Works

The funding mechanism:

```
perp price > spot  → longs pay shorts  → discourages going long
perp price < spot  → shorts pay longs  → discourages going short
```

Settled every eight hours (venues vary). **It is not a fee but a transfer between longs and shorts** — the venue usually takes no cut.

The elegance: **the price anchors itself without any delivery.** The cost is that your holding cost is uncertain — it depends on market sentiment rather than a known rate.

## Concrete Example

Holding a perpetual long for 30 days:

```
notional        $100,000
average funding +0.01% / 8h  (longs pay)
daily cost      $100,000 × 0.03% = $30
30-day total    $900   ← 0.9% of notional
```

**In a bull market funding can stay positive and far higher than this** — annualised holding costs of 30–50% are not unusual.

**Against an event contract**: a fully collateralised event contract has no funding rate, but it does have the opportunity cost of locked capital (see [[fully-collateralized-market]]). **Both charge you for holding time; one does it as an explicit cash flow, the other as an implicit opportunity cost.**

## Common Misconceptions

- **"Perpetuals are free to hold because there is no delivery."** Funding is the cost, and it can be severe in stressed conditions.
- **"Funding is a venue fee."** It is normally a transfer between longs and shorts, with no venue cut.
- **"Perpetuals and event contracts are both crypto derivatives, so similar risk."** The shapes are nearly opposite: perpetuals liquidate and never expire; event contracts never liquidate and always expire. Conflating them badly misprices both.

## In Practice

Put funding into the cost model for any perpetual position:

```
total holding cost = fees + slippage + Σ(funding × notional × periods)
```

**Then read it as a signal**: persistently positive funding means longs are crowded, which is positional information in itself.

**Use one yardstick when comparing to event contracts**: compute the locked-capital opportunity cost (`principal × risk-free rate × tenor`) and set it beside the perpetual's funding. That is the only fair comparison.

## Active Recall

- Q: With no expiry, what anchors a perpetual to spot?
  A: The funding rate: when the perpetual trades above spot longs pay shorts, and vice versa, creating a continuous transfer that pulls the price back.
- Q: Is funding a venue revenue stream?
  A: Normally no — it is a transfer between longs and shorts, with the venue taking no cut.
- Q: Why are perpetuals and event contracts near mirror images in risk shape?
  A: Perpetuals never expire, use margin and can liquidate; event contracts have a definite expiry, are fully collateralised and cannot liquidate.

---

> 中文原页: [`perpetual-futures.md`](./perpetual-futures.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


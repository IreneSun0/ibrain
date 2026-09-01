# Futures

## Definition

A **futures contract** is a standardised, exchange-traded agreement to transact at a set price on a future date.

The load-bearing words are *standardised* and *exchange*: uniform terms (size, grade, delivery date), a central counterparty guaranteeing performance, and the ability to close out at any time. Those three turn a private agreement into a tradable instrument.

## Why It Matters

Futures are the **closest reference point** for event contracts: both price now and settle later, both trade on regulated exchanges, both clear.

**The only structural difference is the underlying**: a future settles against an observable market price, while an event contract settles on a judgement about whether a proposition holds (see [[event-contract]]).

**The US case for regulating event contracts under the CFTC rather than as gambling runs precisely through "this belongs to the futures family".** Understanding futures is understanding the foundation of that argument.

## How It Works

Three core mechanisms:

1. **Standardised terms** — multiplier, delivery month and tick size are fixed, which is what makes contracts fungible and nettable.
2. **Margin and daily mark-to-market** — you post a fraction and settle the day's P&L against the settlement price (see [[margin]]).
3. **A central counterparty** — the clearing house novates, so you face it rather than the other trader (see [[clearinghouse]]).

**Most futures never deliver.** Positions are closed before expiry, or the contract is cash-settled outright. Delivery exists to anchor the future to the spot price, not to move goods.

## Concrete Example

The same "bet on a Fed cut", side by side:

| | CME fed funds future | Event contract |
|---|---|---|
| Underlying | Effective fed funds rate (observable) | "Will it cut" (must be judged) |
| Payoff | Linear | Step ($1 / $0) |
| Collateral | Margin (5–15%) | Usually full |
| Worst case | Potentially large | Known at entry |
| Settlement disputes | Very rare | **A routine risk** |

**The last row is the whole difference.** A future's settlement price comes from a public market and needs no interpretation; an event contract's requires somebody to make a call, and calls can be wrong or manipulated (see [[resolution-risk]]).

## Common Misconceptions

- **"Futures are leveraged gambling."** Leverage comes from the margin system, not the instrument. Hedging is the original function.
- **"Buying a future means taking delivery."** Almost all are closed before expiry, and many are cash-settled by design.
- **"Event contracts are nothing like futures."** Structurally they are close cousins, differing only in whether the underlying is a price or a proposition — which is exactly what their legal status rests on.

## In Practice

Use futures as the yardstick for any event contract:

1. **Is the underlying observable or judged?** — this determines whether resolution risk exists at all.
2. **Margin or full collateral?** — capital efficiency versus liquidation risk.
3. **Is there a central counterparty?** — how counterparty risk is absorbed.
4. **Where does the settlement value come from?** — a market, or a data source plus interpretation.

**Answer those four and you know exactly what this contract carries that a future does not.**

## Active Recall

- Q: What are the three core mechanisms of a futures contract?
  A: Standardised terms (making contracts fungible and nettable), margin with daily mark-to-market, and novation to a central counterparty.
- Q: What is the single structural difference between a future and an event contract?
  A: The underlying: a future settles against an observable market price, an event contract against a judgement about a proposition — which adds resolution risk.
- Q: Why does understanding futures matter for the legal status of event contracts?
  A: The US argument for CFTC rather than gambling regulation is that event contracts belong to the futures/derivatives family.

---

> 中文原页: [`futures-contract.md`](./futures-contract.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


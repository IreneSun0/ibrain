# Adverse Selection

## Definition

**Adverse selection** is the rule that in a market with asymmetric information, **the people willing to trade with you are disproportionately the ones who know more than you do**.

For a market maker this is not a risk to be managed occasionally — it is a permanent condition. Your resting order only gets hit when hitting it is good for the other side. So every fill arrives carrying a small piece of bad news: you may have just taken the other side of someone who knows something.

## Why It Matters

This is the key to why event markets *look* like they should be profitable to make markets in, and are not.

The underlying of an event contract is something that happens in the real world, and in the real world somebody always knows first. Insiders know the earnings. Campaigns know their internal polling. Regulators know what will be announced next week. **Informational advantage is both more common and less regulated in event markets than in equities**, because the underlying is not a security and, in many jurisdictions, insider-trading law simply does not reach it.

Market makers know this. So they either widen their spread or decline to quote at all. **That is the root cause of the empty order books you see across long-tail events.**

## How It Works

How adverse selection drives a market maker out:

1. The maker quotes 0.62 / 0.64, believing fair value is 0.63.
2. Somebody who knows the true probability is 0.85 buys steadily at 0.64.
3. The maker is filled repeatedly on one side and accumulates a large short position.
4. The news breaks; price jumps to 0.85. **The maker loses 0.21 per contract against the 0.02 the spread was earning.**

A rational maker has three responses, and all three are bad for everyone else:
- **widen the spread** — your costs go up;
- **shrink quoted size** — depth thins out;
- **withdraw entirely** — the book disappears.

**The cost of adverse selection is therefore always paid by ordinary users**, in the form of worse prices.

## Concrete Example

The 2024 Polymarket election trade is usually told as a triumph of price discovery. From the market maker's seat it is a textbook adverse-selection event.

A trader with better information — privately commissioned neighbour-effect polling rather than standard polls — built an enormous one-directional position. Every counterparty, market makers included, was systematically on the wrong side. The reported profit ran into tens of millions of dollars, **and that money came out of the pockets of the people who traded against him**.

Both readings are true at once:
- **For the market**: information entered the price. Price discovery worked.
- **For the market maker**: a textbook adverse-selection loss.

**The gains from price discovery are paid for by whoever bears the adverse selection.** That is not a flaw in the story; it is the mechanism.

## Common Misconceptions

- **"Adverse selection means insider trading."** Insider trading is one source. A better model, faster data, or simply sharper judgement produces exactly the same effect, and is entirely legal.
- **"Raise fees to compensate for it."** Fees fall on everybody, while adverse selection comes only from the informed. Raising fees drives out uninformed flow first, **raising the share of informed traders among those who remain** — it makes the problem worse.
- **"This is the market maker's problem, not mine."** It reaches you as a wider spread and a thinner book on every contract you touch.

## In Practice

Before designing or judging an event market, score how asymmetric its information is:

| Event type | Asymmetry | Can it be made? |
|---|---|---|
| Scheduled public data (CPI, unemployment) | Low | Well |
| Election outcomes | Medium (polling is purchasable) | Adequately |
| Corporate decisions, appointments | **High** | Badly |
| Small-circle private events | **Very high** | Essentially not at all |

**In a highly asymmetric market, no amount of subsidy buys liquidity** — the maker's losses exceed the rebate. The only durable fixes reduce the asymmetry itself: more authoritative public data sources, stricter listing review, and sharper contract semantics.

## Active Recall

- Q: Why does every fill carry bad news for a market maker?
  A: A resting order is only hit when hitting it benefits the other side, so the fill itself signals that the counterparty may know more.
- Q: Why doesn't raising fees solve adverse selection?
  A: Fees apply to everyone, so they drive out uninformed flow first and raise the proportion of informed traders among those who remain — making it worse.
- Q: Why is adverse selection worse in event markets than in equities?
  A: The underlying is a real-world event that somebody always knows first, and in most jurisdictions insider-trading law does not reach non-security event contracts.

---

> 中文原页: [`adverse-selection.md`](./adverse-selection.md)  ·  Translation of the canonical Chinese note; the Chinese page is authoritative.


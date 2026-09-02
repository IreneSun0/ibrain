---
id: "case:dome-acquisition"
type: case-study
title: "Polymarket Acquires Dome - The Venue Absorbed the Aggregator"
title_zh: Polymarket 收购 Dome · 场馆吞掉聚合层
aliases:
  - Dome acquisition
  - 场馆吞聚合层
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
  - industry-strategy
tags:
  - case-study
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
review_after: 2027-02-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-27-pm-data-vendors"
related:
  - "venue:polymarket"
---

# Polymarket 收购 Dome · 场馆吞掉聚合层 (2026-02)

## The Question This Case Answers

**Tier D 威胁 (场馆纵向内化第三方能力) 是抽象担忧还是已发生的事实?** — 已发生, 而且发生在**恰好做第三方数据面那件事**的公司身上。

## What Happened (CONFIRMED)

- **Dome** (domeapi.io): Y Combinator **2025 Fall** 批次; 融资 **$5.2M** (YC grant + seed); 两位联创均为 **Alchemy** 的 founding engineer。
- Dome 提供**跨平台市场匹配**（`get-matching-markets-sports`）和**订单路由**，包括账户绑定、服务端执行与费用托管。
- **2026-02-19 公布被 [[polymarket]] 收购**, 条款未披露 — Polymarket 继 **QCEX** 之后的**第二笔收购**。
- 自家文档挂红色横幅: 「**Dome has been acquired by Polymarket** … all Dome APIs will reach end of life on **April 28th, 2026**」, 并把用户导向 Polymarket 自家 API。

## 两个月后: 同一模式再现 (CONFIRMED)

**[[predexon]]** 退掉了完全相同的两层能力 —— 不是被收购, 是自己关停:
- 2026-06-21 公告 Trading API 退役 → 2026-06-25 停止交易 → 2026-07-17 最后提现
- 2026-07-14 匹配端点弃用 → **2026-07-20 起 `GET /v2/matching-markets` 返回 `410 Gone`**

⟹ 半年内, 这个赛道的**执行层与匹配层出现两次撤退**: 一次被买走, 一次自行退出。

## Mechanism Analysis | 机制分析

**为什么聚合/执行层结构性脆弱** (inference, 基于两个样本 + 结构推理):

1. **场馆有第一手数据与最终托管**, 聚合器的匹配与路由本质是在场馆之上做一层薄皮 — 场馆随时可自建或收购。
2. **执行层要么托管客户资金** (监管与运营重担) **要么依赖场馆 API** (随时可被限流/改协议)。Predexon 的托管式 Trading API 正是先关的那块。
3. **聚合器越成功, 越像场馆的分发威胁** — 收购是场馆最便宜的解法 (Dome), 或者聚合器自己先撤 (Predexon)。

**什么不脆弱** (inference): 场馆**不能**可信地做的事 —— 评价自己的裁决质量、暴露自己盘口的薄度、跨场馆做中立的等价判定。这与「场馆是利益方, 给不出可信的数据与结算监督」是同一条论证, 现在有了两个市场样本。


## What Would Change This Assessment

- 若出现一家聚合器**成功抵抗内化并持续增长** (例如 OpticOdds 靠做市商客户关系站稳), 说明该层并非必然脆弱, 上述 1-3 需重估。
- 若 Polymarket 用 Dome 的资产做出了跨场馆中立数据产品 (它有动机吗?) — 那是对「场馆不能中立」论证的直接挑战, **必须跟踪**。

## Sources

[[report-2026-08-27-pm-data-vendors]] (一手: docs.domeapi.io 横幅 + docs.predexon.com changelog/OpenAPI; 独立: bankless 2026-02-19)

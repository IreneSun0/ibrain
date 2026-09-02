---
id: "venue:predict-fun"
type: exchange-venue
title: Predict.fun
title_zh: Predict.fun
aliases:
  - predict.fun
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
tags:
  - exchange-venue
created: 2026-08-26
updated: 2026-08-26
last_verified: 2026-08-26
review_after: 2026-11-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-prediction-venues"
related:
  - id: "protocol:bnb-chain"
    rel: built-on
    note: 2024 首发 Blast L2, 2025-12 重启于 BNB Chain
  - id: "protocol:uma"
    rel: depends-on
    note: 事件类结算走 UMA optimistic oracle
  - id: "protocol:chainlink"
    rel: depends-on
    note: 价格类结算走 Chainlink Data Streams
  - id: "mmf:susquehanna"
    rel: backed-by
    note: 2026-03-31 战略轮投资方之一 (与 YZi Labs)
---

# Predict.fun

## Key Facts (CONFIRMED, 官方文档为主)

- BNB Chain 去中心化预测市场 (2024 首发 Blast L2, 2025-12 重启 BNB, CZ 公开站台, YZi Labs 孵化)。创始人化名 **"Ding" (@dingalingts)**; 「前 Binance Head of Research/PancakeSwap 创建者」说法 UNVERIFIED。
- 模型: CLOB + conditional tokens + **收益型抵押** (挂单/持仓资金经 Venus 生息 — 差异化卖点); multi-outcome 支持。
- 结算: 事件类 = UMA optimistic oracle; 价格类 = Chainlink Data Streams (与 Polymarket 同构双轨)。
- 融资: 2026-03-31 战略轮 — **YZi Labs + Susquehanna Crypto** (金额未披露); 2026-03-04 收购 Probable (PancakeSwap/YZi 系预测市场)。
- 规模 (公司口径): BNB 重启后累计 >$1.8B、用户 13 万+。
- **2026-04: Binance Wallet 内嵌预测市场由 Predict.fun 驱动** — 2 亿+ 用户入口, 一键免 gas。

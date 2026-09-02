---
id: "org:finfeedapi"
type: organization
title: FinFeedAPI (API Bricks)
title_zh: FinFeedAPI
aliases:
  - API Bricks
  - CoinAPI
status: verified
importance: tier-2
domains:
  - prediction-outcome-markets
  - industry-strategy
tags:
  - organization
  - competitor
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
review_after: 2026-11-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-27-pm-data-vendors"
related:
  - id: "venue:kalshi"
    rel: integrates-with
    note: 母体 CoinAPI 的行情 schema 套到事件市场
  - id: "venue:polymarket"
    rel: integrates-with
    note: 同上
  - id: "venue:hyperliquid-hip4"
    rel: integrates-with
    note: 与 Kairos 同为少数覆盖 HIP-4 者
---

# FinFeedAPI (API Bricks)

## Executive Summary

母公司 **API Bricks** 同时运营 2017 年上线的 **CoinAPI**。FinFeedAPI 的特点是跨资产覆盖：预测市场与股票、外汇、SEC filings 共用一套 API 凭证。

## Key Facts (CONFIRMED, 一手 llms.txt + GitHub)

- **母体**: API Bricks 同时做 CoinAPI 与 FinFeedAPI; 共享 SDK monorepo (`github.com/api-bricks/api-bricks-sdk`, 「SDKs for CoinAPI & FinFeedAPI」) 与 SSO (`signin.apibricks.io`)。
- **覆盖**: Polymarket · Kalshi · Manifold · Myriad · **Hyperliquid (HIP-4 outcome markets)**。另有博文声称扩到八家 (加 Gemini/Pascal/Crypto.com) — **单源未验**。
- **架构决定了能力边界**: 每个 REST 路径都是 `{exchange_id}/{market_id}` 作用域 (CoinAPI 的 `exchange_id/symbol_id` 模式移植) ⟹ **无 canonical 跨场馆 ID, 无匹配端点** — 得到的是「每场馆统一 schema」, 不是「统一工具」。
- 提供: 订单簿当前快照+历史 · OHLCV 历史 · 市场/成交/报价历史 · JSON-RPC API · 托管 MCP server。**无任何交易/执行端点。**
- 裁决/结算元数据: 文档未涵盖。
- 定价: 按量信用制, $25 免费额度; 预测市场专属价目表**未能读取** (站点对非浏览器客户端 403)。

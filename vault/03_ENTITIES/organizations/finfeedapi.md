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

**Tier B 里唯一有成熟母体的玩家**: 母公司 **API Bricks** 同时运营 **CoinAPI** (2017 年起家)。即 CoinAPI 团队把交易所行情 schema 套到事件市场上。其真差异化不是预测市场深度, 而是**跨资产** — 预测市场与股票/外汇/SEC filings 共用一把 key。

## Key Facts (CONFIRMED, 一手 llms.txt + GitHub)

- **母体**: API Bricks 同时做 CoinAPI 与 FinFeedAPI; 共享 SDK monorepo (`github.com/api-bricks/api-bricks-sdk`, 「SDKs for CoinAPI & FinFeedAPI」) 与 SSO (`signin.apibricks.io`)。
- **覆盖**: Polymarket · Kalshi · Manifold · Myriad · **Hyperliquid (HIP-4 outcome markets)**。另有博文声称扩到八家 (加 Gemini/Pascal/Crypto.com) — **单源未验**。
- **架构决定了能力边界**: 每个 REST 路径都是 `{exchange_id}/{market_id}` 作用域 (CoinAPI 的 `exchange_id/symbol_id` 模式移植) ⟹ **无 canonical 跨场馆 ID, 无匹配端点** — 得到的是「每场馆统一 schema」, 不是「统一工具」。
- 提供: 订单簿当前快照+历史 · OHLCV 历史 · 市场/成交/报价历史 · JSON-RPC API · 托管 MCP server。**无任何交易/执行端点。**
- 裁决/结算元数据: 未文档化 (UNKNOWN)。
- 定价: 按量信用制, $25 免费额度; 预测市场专属价目表**未能读取** (站点对非浏览器客户端 403)。


<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (一手 docs 核验, 证据见 [[report-2026-08-27-pm-data-vendors]])。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 3 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。

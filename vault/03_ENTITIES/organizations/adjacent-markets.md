---
id: "org:adjacent-markets"
type: organization
title: Adjacent (adjacent.markets)
title_zh: Adjacent 指数
aliases:
  - Adjacent News
  - adj.news
status: verified
importance: tier-1
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
    note: 指数与基准的底层行情来源
  - id: "venue:polymarket"
    rel: integrates-with
    note: 同上
---

# Adjacent (adjacent.markets)

> 原 **Adjacent News** (`adj.news`) — 已改名并转型; 旧 API 域名 (`api.adj.news`, `v2.api.adj.news`) **已 NXDOMAIN**, `adj.news` 301 跳转到 `adjacent.markets`。

## Executive Summary

自称「**第一家独立第三方事件合约与预测市场指数提供商**」, 从原来的市场聚合 API 转型做**指数与基准**。已发 **22 个指数** (政治期货指数、总统/参议院/众议院选情指数、预测市场衍生参考利率)。

## Key Facts (CONFIRMED)

- **转型**: 原做 40,000+ 市场跨 Kalshi/Polymarket/Manifold/Metaculus 的归一化 API (Markets/Search/News/Trade 端点 + CSV/TSV 导出) → 现自述为「an indexing and benchmarking company for prediction markets and event contracts」。
- **现有资产**: 22 个指数; 公开 API `api.adjacent.markets/api/v1/public` (**无鉴权, CORS 开放, 延迟 15 分钟**); MCP server (`mcp.adjacent.markets/mcp`)。
- **创始人**: Lucas Kohorst; pre-seed 融资 (金额未披露)。定价与团队规模均未公布。


## Open Questions

指数的方法论是否公开? 有无机构采用它的基准? 是否会向结算质量方向延伸?

<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (一手 docs 核验, 证据见 [[report-2026-08-27-pm-data-vendors]])。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 2 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。

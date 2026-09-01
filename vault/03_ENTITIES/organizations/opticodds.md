---
id: "org:opticodds"
type: organization
title: OpticOdds
title_zh: OpticOdds
aliases:
  - optic odds
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
    note: 只返回真正跨平台的事件 — 把匹配做成产品约束
  - id: "venue:polymarket"
    rel: integrates-with
    note: 同上
---

# OpticOdds

> **首建时完全漏掉的竞品** — 它不在早前的 Tier B 清单里, 是本轮核验主动扫出来的。

## Executive Summary

体育赔率/行情数据的老牌供应商, 延伸进预测市场, 并**明确面向做市商**。它对 canonical 标识符的语义定义是本赛道最锋利的一个, 且**只返回真正跨平台的事件** — 这是把「匹配」做成产品约束而非尽力而为。

## Key Facts (CONFIRMED, 一手 developer docs)

- **canonical 标识符 (原话)**: 「a `canonical_id` groups the same event across platforms, while a `canonical_market_id` identifies the same outcome across platforms — **the same value on Kalshi and Polymarket means 'these two markets settle on the same thing'**.」
- **产品约束**: `/prediction-markets/canonical-events` 端点「**only canonical events whose members span at least 2 platforms are returned**」 — 单平台事件不进 canonical 集合。
- **订单簿**: SSE 流推送**全订单簿快照** (top-of-book + 完整买卖深度), 覆盖每个支持平台的每个市场。
- **覆盖**: Kalshi + Polymarket, 含**非体育**类 (选举 / 经济指标 / 加密价位 / 文化结果)。
- **机构定位**: 有专门的 *OpticOdds for Prediction Market Makers* 指南; 提供校准概率与自定义定价模型; 给 **native exchange ID 供客户自行路由** (自己不做执行)。
- 定价未公开 (UNKNOWN)。


## Open Questions

定价与客户规模? 是否在做裁决/结算元数据 (目前未文档化)? 与体育博彩业务的资源分配?

<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (一手 docs 核验, 证据见 [[report-2026-08-27-pm-data-vendors]])。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 2 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。

---
id: "org:tatum"
type: organization
title: Tatum
title_zh: Tatum
aliases:
  []
status: verified
importance: tier-2
domains:
  - blockchain
tags:
  - organization
created: 2026-08-26
updated: 2026-08-26
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
  - "report:2026-08-27-pm-data-vendors"
related:
  - id: "org:circle"
    rel: backed-by
    note: "2022 年 $41.5M 轮 Circle 参投"
---

# Tatum

## Key Facts (CONFIRMED)

- Web3 API/RPC 开发平台 (一套 API 跨多链), 2018 年 Jiri Kobelka 创立, HQ Miami; 总融资 ~$42.5M (2022 $41.5M, Circle 参投)。
- 2025-26 无新融资/大事记录; 规模未披露。

## 预测市场 API (2026-08-27 核验 — 首建时未确认, 现已证实)

**存在, 但比早前描述窄得多。** (CONFIRMED, 一手 docs, `updatedAt: 2026-08-21)

- 端点: `https://api.tatum.io/v4/data/prediction`, **18 个文档化端点**, 三组: Events (列表/详情/统一搜索) · Markets (列表/详情/当前价/**当前订单簿**/价格历史/近期成交/top holders) · Wallet (组合摘要/持仓/平仓/成交史/活动流/名义敞口/交易市场数/交易者排行)
- **只支持 Polymarket + Kalshi**, **只读** (无执行)
- ⚠ **「归一化」的真实含义 (其自家文档的诚实说明)**: `status`/`category`/`tag`/`search` 四个过滤器**只有 Polymarket 支持**, 不带 `platform=polymarket` 调用会返回 `400` ⟹ 归一化 = **共享响应封装 + 按场馆门控的过滤器**, **不是统一工具模型**。无 canonical ID, 无跨场馆匹配。
- 裁决/结算元数据: 文档未涵盖。定价: 平台信用制 (如 events 端点 100 credits/次), 无预测市场专属价目。
- 定位: 零售/开发者 (博文用例是交易机器人、看板、社交排行), 无合规/审计/风险定位。

⚠ **一个未解的巧合 (UNVERIFIED, 不得当事实)**: Tatum 博文称「38 个端点 (24 个 Polymarket + 14 个 Kalshi)」, 而 [[predexon]] 自我营销也是「38+ 端点」, 且两者端点分类近乎一致。**无任何来源提及合作/白标/转售关系**, Tatum 也未指明上游供应商。另注: Tatum 公开文档只列 18 个预测端点, 与自家博文的 38 也对不上。**仅记录为待查巧合。**


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]]); 当时预测市场关联未确认。
- **2026-08-27** — **已查实**: 预测市场 API 确实存在 (`/v4/data/prediction`, 18 端点, Polymarket+Kalshi 只读)。实体重新归类为 Tier B 竞品。 [Source: [[report-2026-08-27-pm-data-vendors]]]
- **2026-09-01b** — 实体语义关联层 (2026-09-01b): 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。

---
id: "org:predexon"
type: organization
title: Predexon
title_zh: Predexon
aliases:
  []
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
  - id: "protocol:uma"
    rel: depends-on
    note: "独特资产是 UMA 裁决数据: oracle 状态、事件时间线、争议推送"
---

# Predexon

## Executive Summary

预测市场数据层供应商 (「The data layer for prediction markets」)。**2026 年中主动退掉了执行与跨场馆匹配** — 现为纯数据商。其**真正的独特资产是 UMA 裁决数据**: oracle 状态、事件时间线, 以及推送 proposal/dispute/settlement/reset 的 WebSocket 频道。

## Key Facts (CONFIRMED, 一手 changelog + OpenAPI spec)

**退出的能力 (早前的 Tier B 描述已过期约两个月)**:
- 2026-06-21 公告托管式 Trading API 退役 → **2026-06-25 停止交易** → 2026-07-17 最后提现
- 2026-07-14 匹配端点弃用 → **2026-07-20 起 `/v2/matching-markets` 返回 `410 Gone`**
- 独立佐证: 今日解析其 OpenAPI v2 spec — **62 个路径中只有 1 个非 GET 方法** (批量钱包身份查询), 零订单/账户/匹配路径。

**当前能力**:
- 覆盖 (数据): Polymarket (最深, 62 路径中约 40 个) · Kalshi · Limitless · Opinion · Predict.fun + Binance/Chainlink 参考价
- 🔑 **UMA 裁决数据**: `/v2/polymarket/uma/markets`, `/uma/market/{condition_id}` (当前 oracle 状态与事件时间线) + WS **oracle 频道** (proposal/dispute/settlement/reset) + **lifecycle 频道** (token 注册, `condition_resolution`)
- **Kalshi 亚分订单簿历史** (`/v2/kalshi/orderbooks-subcent`, 2026-01-08 起) — 「Kalshi 以亚分定价, 该端点如实反映」
- tick 级历史 (每次挂单/更新/撤单/成交, Parquet 下载, 声称覆盖自 2020)
- mempool 抢先: 「监听 Polygon mempool, 比确认早 3-5 秒发现 Polymarket 成交」「比 Polymarket RTDS 快最多 5 秒」 (一手营销, **未验**)
- 钱包 P&L / 钱包聚类 / 聪明钱持仓 / 排行榜 / builder-fee 归因 / MCP server
- **定价公开**: Free $0 · Dev $49/月 · Pro $249/月 · Enterprise $499+/月; tick 下载另按数据信用计费

⚠ **营销与规格冲突**: 其定价页**仍在售卖已下线的 Trading API**, Free 档说明也还提匹配端点。**以 OpenAPI spec 为准**; 第三方目录 (polymart/launchpoly) 仍复述旧卖点, 不可引用。

**团队/融资**: 「Backed by Alliance」(alliance.xyz), 据报 ALL16 批次 2026-03 毕业; 创始人据报 Larry Pang 与 Jason Lee (UC Berkeley, ex-Amazon/AWS) — **第三方单源, 暂按 provisional**。融资金额 UNKNOWN。「100+ 客户」仅见第三方目录, **不可依赖**。


## Open Questions

退出执行是战略聚焦还是监管/运营压力? UMA 数据线是否会向裁决质量评分延伸?

<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (一手 docs 核验, 证据见 [[report-2026-08-27-pm-data-vendors]])。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。

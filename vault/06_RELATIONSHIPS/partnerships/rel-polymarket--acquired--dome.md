---
id: "rel:polymarket--acquired--dome"
type: relationship
title: "Polymarket → acquired → Dome"
aliases: []
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
tags:
  - relationship
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-27-pm-data-vendors"
evidence:
  - "report:2026-08-27-pm-data-vendors"
related:
  - "case:dome-acquisition"
entity_a: "venue:polymarket"
entity_b: "org:dome"
relationship_type: "acquired"
relationship_status: active
start_date: 2026-02-19
end_date:
---

# Polymarket → acquired → Dome

## Entity A

[[polymarket]] (venue)

## Entity B

Dome (domeapi.io) — YC Fall 2025, $5.2M, 两位联创均为 Alchemy founding engineer。做**跨平台市场匹配 + 订单路由**。**无独立实体页** (已停业, 全部资料在案例页里)。

## Relationship Type

`acquired` — 2026-02-19 公布, 条款未披露。Polymarket 继 QCEX 之后的第二笔收购。

## Evidence | 证据

- Dome 自家文档红色横幅: 「**Dome has been acquired by Polymarket** … all Dome APIs will reach end of life on **April 28th, 2026**」 (一手)
- 独立媒体报道 2026-02-19 (bankless)
[Source: [[report-2026-08-27-pm-data-vendors]]]

## Economic Meaning | 经济含义

场馆花钱把**跨场馆聚合与路由能力**买下并关停。对被收购方而言这是退出; 对市场而言这是**一个中立聚合层的消失** — 该能力从此在场馆内部, 不再中立。

## Strategic Meaning | 战略含义

**Tier D「场馆纵向内化」从抽象威胁变成已发生的事实**, 且发生在离核心 数据面最近的公司身上。两个月后 [[predexon]] 自行退掉同样两层能力 ⟹ 半年内该层两次撤退。

直接推论: **不宜自建执行/路由层**, 护城河候选收窄到**场馆做不了 (利益冲突) 且聚合器做不了 (无客户关系)** 的那部分 — S1 控制面与 S3。详见 [[case-dome-acquisition]]。

## What Would Change This Assessment

若 Polymarket 用 Dome 资产做出**跨场馆中立**的数据产品 (它有动机吗?), 则「场馆不能中立」这条核心论证受到直接挑战 — 必须跟踪 (研究队列 R13)。

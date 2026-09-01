---
id: "protocol:tron"
type: protocol-network
title: TRON
title_zh: 波场
aliases:
  - 波场
  - TRX
status: verified
importance: tier-1
domains:
  - blockchain
  - stablecoins-wallets-payments
tags:
  - protocol-network
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
  - "report:2026-08-26-cex-lineage"
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "protocol:chainlink"
    rel: integrates-with
    note: 2025-05 官方 oracle 从 WINkLink 切换为 Chainlink
---

# TRON | 波场

## Executive Summary

Justin Sun 2017 年创立的 DPoS L1, **全球 USDT 的主结算轨**: 承载 48.67% 流通 USDT (~$89.7B, 2026-07), 季度结算 $2.1T。Forbes 评语「结算近半 USDT 且 Washington 触不到它」。资源模型 (Bandwidth/Energy) 造就独特的 B2B Energy 租赁市场。2025-05 官方 oracle 从 WINkLink 切换为 Chainlink。

## Key Facts (CONFIRMED)

- 共识: DPoS (Super Representatives, TRON Power 投票); 资源: [[tron-bandwidth]] (字节) + [[tron-energy]] (合约计算) — TRC-20 USDT 转账耗 Energy, 质押 TRX 可获/可委托 ([[tron-energy-delegation]] = B2B 生意的机制根)。
- USDT 份额: 2026-03 >46% → 2026-07-13 48.67% ($89.69B); TRON 链稳定币总市值 $89.2B (USDT 占 98.5%)。
- 生态: [[justlend]] (借贷+Energy Rental) / [[sunpump]] (meme 发行) / SUN / [[bittorrent-chain]] (跨链) / [[winklink]] (已被废黜的原官方 oracle)。
- 关联实体: [[htx]] (HTX DAO 深绑 TRON; UK/EU 制裁传导风险) / Tron Inc. (Nasdaq, Sun 仅 adviser)。


<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (web 核验 2026-08-26)。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。

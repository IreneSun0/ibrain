---
id: "venue:polymarket"
type: exchange-venue
title: Polymarket
title_zh: Polymarket
aliases:
  - Polymarket US
  - QCX
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
  - crypto-market-structure
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
  - "report:2026-08-27-pm-data-vendors"
related: []
---

# Polymarket

## Executive Summary

全球最大 crypto 预测市场 (2020, Shayne Coplan)。hybrid 架构: 链下 CLOB 撮合 + Polygon 链上 USDC 全额抵押结算 (ERC-1155 outcome tokens)。2025-07 以 $112M 收购 CFTC 持牌 QCEX 合法重返美国 (QCX DCM + QC Clearing DCO); ICE 投资至多 $2B (~$8-9B 估值), 2026 年中寻求 $15-20B。**2026-01 起结束零费率时代** —— 所有摩擦成本模型的输入参数因此改变。

## Market Model (CONFIRMED)

- 离岸主平台: off-chain matching + on-chain settlement (Polygon, USDC, conditional tokens $1 全额抵押二元)。
- 美国: QCX LLC (dba Polymarket US) = DCM + QC Clearing = 清算, 全额抵押无杠杆; 2025-12-02 重开 (iOS, sports 先行), 2026-05-12 撤 waitlist 全量开放。2026-04-28 已申请让美国用户直接上离岸主所。
- **费率 (2026-03 全表, 单源 Sacra)**: taker — crypto 0.07% / sports 0.03% / finance+politics 0.04% / 其他 0.05%; 2025 年收入 $0 → 2026-06 年化收入 $1B。

## Resolution (CONFIRMED)

离岸 = [[uma]] optimistic oracle (含 2025-03 Ukraine 矿产 $7M 治理攻击案, 拒退款); 价格类 2025-09 起走 [[chainlink]]; 美国 QCX = DCM 自认证合约, 非 UMA。→ 同一品牌两种结算法学, [[settlement-methodology]] 档案分轨维护。

## Regulatory Position (CONFIRMED)

2022 CFTC 罚 $1.4M 退出美国 → 2024-11 FBI 搜查 Coplan → 2025-07 DOJ+CFTC 双撤不起诉 → QCEX 收购 + no-action 25-35 → 2025-11 Amended Order of Designation。离岸平台被 18 国屏蔽 (France/Singapore/Brazil/Belgium 等)。

## Scale (带口径警示)

2024 全年 ~$9B (大选单市场 >$3.3B) → 2026-03 峰值 ~$10.5B/月 (CoinDesk 另有 >$20B 口径, 疑双边计量) → 2026-05 $8.9B (其中美国 DCM $1.8B); 月活钱包 ~84 万 (2026-02)。品类: sports ~40% / politics 32% / crypto 20%。**盈亏分布: 0.1% 账户拿走 67% 利润, >70% 用户亏钱** (单源) — 与零和账本恒等式互证。

## Key People

Founder & CEO **Shayne Coplan** ([[shayne-coplan]]); 顾问: J.C. Giancarlo (前 CFTC 主席) / Nate Silver / Donald Trump Jr. (2025-08 随 1789 Capital 入); CMO 确认将发 POLY token + airdrop (无 TGE 细节)。

## Events 2024-2026

2026-03 收购基建公司 Brahma; 内幕串案 (委内瑞拉行动 $400k / 以色列军官 Iran strike $244k); NYT/Politico 营销争议 (虚假帖/付费吹准确率)。

**收购线 (三笔, 战略含义明确)**: QCEX (2025-07, $112M, 买监管牌照) → **Dome (2026-02-19, 买跨平台匹配+订单路由, API 2026-04-28 EOL)** → Brahma (2026-03, 基建)。⟹ **它在系统性地把上下游能力内化**: 牌照、聚合层、基建。Dome 案详见 [[case-dome-acquisition]] — 这是 Tier D「场馆纵向内化」威胁的实证。


## Sources

[[report-2026-08-26-prediction-venues]] (一手: ICE IR / PRNewswire / CFTC; 费率与收入 = Sacra 单源, 谨慎引用)

<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验)。workbook 「零交易费」表述已过时 (2026-01 起收费)。
- **2026-08-27** — 补: **2026-02-19 收购 Dome** (YC F25, $5.2M, 做跨平台市场匹配与订单路由), 全部 Dome API 2026-04-28 EOL — Polymarket 继 QCEX 后第二笔收购, 是「场馆吞掉聚合层」的样本。 [Source: [[report-2026-08-27-pm-data-vendors]]]

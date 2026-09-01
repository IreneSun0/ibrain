---
id: "org:intercontinental-exchange"
type: organization
title: Intercontinental Exchange (ICE)
title_zh: 洲际交易所
aliases:
  - ICE
status: reviewed
importance: tier-2
domains:
  - financial-markets
  - prediction-outcome-markets
tags:
  - organization
created: 2026-08-27
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-prediction-venues"
  - "report:2026-08-26-infra-mm-stablecoins"
related:
  - id: "venue:okx"
    rel: invested-in
    note: 2026-03 以约 $25B 估值投资 (单源, 引用前需再核)
---
# Intercontinental Exchange (ICE) | 洲际交易所

## Executive Summary

纽约证券交易所（NYSE）的母公司，全球最大的交易所与市场基础设施集团之一。

**它是预测市场正统化最强的单一信号**：2025–2026 年对 [[polymarket]] 投资至多 **$2B**（约 $8–9B 估值，2026-03 完成 $600M 一笔），并另有报道称以约 $25B 估值投资 [[okx]]（单源，引用前需再核）。

一家把清算与数据当核心业务的传统交易所巨头，把事件市场当作**基础设施资产**来配置 —— 这比任何行业报告都更能说明它对这个赛道的判断。

## What It Actually Is | 它到底是什么

ICE 不是"一家交易所"，是一个**市场基础设施集团**：交易所 + 清算 + 数据 + 抵押品服务。

它的收入结构里，**数据与分析业务的占比与稳定性长期高于交易撮合** —— 这一点直接解释了它为什么会看上事件市场：

| ICE 的核心能力 | 对应事件市场的缺口 |
|---|---|
| 清算与中央对手方 | 事件市场几乎没有（见 [[clearinghouse]]） |
| 参考数据与指数 | 无标准、无基准（见 [[canonical-event-id]]） |
| 抵押品与保证金服务 | 全额抵押，效率极低（见 [[margin]]） |

**它买的不是一个赌博平台的股份，是一类尚未被基础设施化的新资产。**

## How It Works | 运作方式

ICE 在这个赛道下了**三条并行的注**，方向一致：

1. **股权** —— 投资 Polymarket（可能还有 OKX），拿到场馆层的位置。
2. **链上结算** —— 参与稳定币发行方的新结算网络作为创始验证人，把自己放进链上美元的管道里。
3. **数据分发** —— 传统上它把交易所行情打包成机构可订阅的产品，事件市场行情是同一套逻辑的自然延伸。

**第 3 条最少被注意，但可能最重要**：ICE 最赚钱的业务是卖数据，而事件市场的数据目前散落在各场馆、无标准、无历史（见 [[data-infrastructure]]）。

## Position in the Market | 它在市场里的位置

在事件市场的价值链上，ICE 站在**最上游也最下游**的位置：既是资本，又可能是未来的清算与数据层。

它的进入对这个市场有两个结构性影响：
- **正统化** —— 一家受严格监管的上市公司下注，会让其他机构的合规部门更容易点头（见 [[regulatory-access]]）。
- **标准压力** —— ICE 做生意需要可清算、可定价、可比较的合约，这会倒逼语义与结算标准（见 [[contract-equivalence]]）。

**它想要的东西，恰好是这个市场最缺的东西。**

## What Could Break It | 什么会让它出问题

- **估值风险** —— $8–9B 的入场估值建立在增速持续的假设上；而 [[kalshi]] 与 Polymarket 的收入底盘目前主要是体育（见 [[prediction-market]]）。
- **监管反转** —— 州与联邦的管辖权之争未决，不利判决会直接冲击估值。
- **单源信息** —— OKX 投资一条目前是单源记录，**引用前必须再核**。

## What To Watch | 该盯什么

- **ICE 是否把事件市场数据纳入其机构数据产品线** —— 那是它真正开始整合的信号。
- **是否推动清算或保证金化方案** —— ICE 有全套能力，动手即改变格局。
- **后续融资轮的估值方向** —— 相对 $8–9B 的入场价，是抬还是压。


<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (web 核验 2026-08-26)。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。

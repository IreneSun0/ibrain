---
id: "mmf:falconx"
type: market-maker-fund
title: FalconX
title_zh: FalconX
aliases:
  []
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
  - institutional-risk
tags:
  - market-maker-fund
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related:
  - id: "venue:bybit"
    rel: provides-liquidity-to
    note: "2025-02 被盗案中与 Galaxy/Wintermute 一同在 72 小时内协助补足储备"
---
# FalconX

## Executive Summary

机构加密 prime broker，600+ 机构客户、累计成交规模以万亿计（公司口径）。它做的是[[prime-brokerage|主经纪商]]的活：统一接入、融资、托管、清算。

**它在这个知识库里的实证价值来自一次危机**：2025-02 [[bybit]] 约 $15 亿被盗后，FalconX 与其他机构在 72 小时内协助补足储备，使其未破产。

## What It Actually Is | 它到底是什么

FalconX 的业务是**把碎片化的加密市场对机构包装成一个接口**：

```
机构 → FalconX 一个账户 → 多个交易所/场外对手方
```

它同时提供融资与衍生品，并通过并购扩张能力（衍生品、ETP、网络层基础设施等）。

**对事件市场，它代表一个尚未发生的位置**：目前没有任何机构在事件市场提供真正的主经纪服务 —— 而那正是机构资金进场的前置条件（见 [[prime-brokerage]]）。

## How It Works | 运作方式

prime broker 的核心价值是**跨场所保证金**，而这在事件市场做不到，原因不在技术：

```
跨场所净额  需要  证明头寸可互抵
             需要  合约语义等价 (见 contract-equivalence)
             而这份判定书目前没人出具
```

**所以事件市场的 prime brokerage 是一个被语义问题卡住的商业机会**，不是一个没人想到的空白。

FalconX 有做这件事的全部能力（客户、资本、接入），缺的是那个前置条件。

## Position in the Market | 它在市场里的位置

在这个赛道，FalconX 截至 2026-08 **没有公开的事件市场业务记录**。

它的意义在于**它是那个空位最合适的候选者之一**：机构关系、多场所接入、融资能力、以及在危机中已被验证过的执行力。

**它进场与否，是判断"事件市场是否已经具备机构基础设施条件"的一个直接指标。**

## What Could Break It | 什么会让它出问题

- **对手方集中** —— prime broker 本身成为客户的单点。
- **加密 prime 的历史教训** —— 这一业态在过去周期里出现过连锁失败。
- **事件市场关联未证实** —— 目前无公开信息，不得推测。

## What To Watch | 该盯什么

- **是否提供事件合约接入或保证金服务** —— 那将是这个市场机构化的关键一步。
- **跨场所净额是否出现任何可行方案** —— 语义等价是它的前提。


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]])。
- **2026-09-01b** — 实体语义关联层 (2026-09-01b): 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。

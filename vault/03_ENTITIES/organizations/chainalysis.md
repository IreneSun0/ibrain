---
id: "org:chainalysis"
type: organization
title: Chainalysis
title_zh: Chainalysis
aliases:
  []
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
  - regulation-compliance
tags:
  - organization
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
  - id: "protocol:chainlink"
    rel: partners-with
    note: "与 Chainlink ACE 合规工作流合作"
---
# Chainalysis

## Executive Summary

区块链情报与合规调查商，主要客户是政府与金融机构。它做的事就是 [[know-your-transaction|KYT]]：地址标签、资金路径追踪、风险评分。

**对链上事件市场用户，它是一条看不见但真实的风险线**：你从合约池领取的赔付，其资金路径会被这类系统评分，评分不好就可能在出金环节被冻结。

## What It Actually Is | 它到底是什么

Chainalysis 的能力建立在一个事实上：**链上是假名，不是匿名**（见 [[public-key]]）。

它的三层分析：
1. **地址标签** —— 这个地址属于交易所、混币器还是已知非法实体。
2. **聚类** —— 哪些地址属于同一实体（概率判断，可能出错）。
3. **风险评分** —— 给出可操作的分数。

**第 2 层的误判代价是真实的**：正常用户的资金被标记为高风险而遭冻结，申诉困难 —— 而这在链上事件市场里格外容易发生，因为**赔付来自一个所有人共用的合约池**。

## How It Works | 运作方式

它的商业模式是**卖情报与工具给需要合规的人**，因此它的判断在实践中具有准司法效力：交易所依据它的评分决定放行与否。

**这产生一个值得注意的结构**：一家私营公司的算法输出，实际上决定了普通人的资金能否流动 —— 而其判定逻辑不公开、申诉路径不透明。

**对事件市场的具体含义**：选择做参与者 KYC 的持牌平台，其资金池被污染的概率明显更低 —— 这是"持牌平台流动性差但钱更干净"这个取舍里最少被讨论的一维。

## Position in the Market | 它在市场里的位置

在事件市场，Chainalysis 截至 2026-08 **没有公开的直接合作记录**，但它的影响是**间接且普遍的**：任何链上事件市场用户在出金时都会撞上它或它的同类。

它与 [[chainlink]] 在合规工作流上有公开合作，说明这类情报能力正在被接入链上执行环节 —— **即"合规判断上链"的方向**。

## What Could Break It | 什么会让它出问题

- **误判与申诉困难** —— 聚类是概率判断。
- **准司法权力无监督** —— 私营算法决定资金流动。
- **对隐私的系统性侵蚀** —— 分析能力持续增强。

## What To Watch | 该盯什么

- **是否出现事件市场专门的监测能力** —— 识别对倒式价值转移需要跨市场视角（见 [[anti-money-laundering]]）。
- **合规判断链上化的进展** —— 会改变链上事件市场的准入形态。


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]])。
- **2026-09-01b** — 实体语义关联层 (2026-09-01b): 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。

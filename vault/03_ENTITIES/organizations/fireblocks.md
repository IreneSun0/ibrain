---
id: "org:fireblocks"
type: organization
title: Fireblocks
title_zh: Fireblocks
aliases:
  []
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
  - institutional-risk
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
related: []
---
# Fireblocks

## Executive Summary

机构级数字资产托管与结算基础设施，核心技术是 **MPC（多方计算）**：私钥被分片，签名时各方协同计算，**完整私钥从未在任何一台机器上出现过**（见 [[private-key]]）。

它服务数千家机构与数十家银行，是"机构怎么安全持有加密资产"这个问题目前最主流的答案。

## What It Actually Is | 它到底是什么

Fireblocks 解决的是[[custody|托管]]问题里最难的一半：**既要安全，又要能高频动。**

| 方案 | 安全 | 可用性 |
|---|---|---|
| 冷钱包 | 高 | **低**（动一次很麻烦） |
| 热钱包 | 低 | 高 |
| **MPC + 策略引擎** | **高** | **高** |

**关键在"策略引擎"**：谁能发起转账、转给谁、多大金额、需要几个人批准 —— 这些规则被写进系统而不是靠流程约束（见 [[policy-engine]]）。

**这正是机构级托管与个人钱包的根本差别**：不是密钥更安全，是**权限被结构化了**。

## How It Works | 运作方式

它的商业模式是**基础设施订阅**，而非交易分成 —— 这让它在利益上与客户的交易行为无关，是一个中立位置。

它也通过并购扩张能力（安全监测、嵌入式钱包等），把"托管"扩成"数字资产运营平台"。

**对事件市场的直接含义**：链上事件市场的全额抵押资金需要机构级托管才能被基金持有（见 [[custody-segregation]]）。**没有这一层，机构连"怎么合规地持有 outcome token"都答不上来。**

## Position in the Market | 它在市场里的位置

在事件市场的价值链上，Fireblocks 处在**机构准入的必经环节**，但目前公开的事件市场关联为 **UNKNOWN**。

这构成一个具体的缺口：
```
机构想配置事件合约
  → 需要合规托管 outcome token
  → 需要托管方支持该链、该代币标准 (见 erc-1155)
  → 目前无公开支持记录
```

**这是"机构进不来"的一个非常具体、非常可解的技术原因**，而不是抽象的监管障碍。

## What Could Break It | 什么会让它出问题

- **单点集中** —— 大量机构资产依赖同一套基础设施。
- **估值与融资节奏** —— 最新公开估值已有数年，缺乏更新。
- **事件市场支持未证实。**

## What To Watch | 该盯什么

- **是否宣布支持 conditional token / outcome token 标准** —— 那是机构能持有事件头寸的前提。
- **是否支持主流事件市场结算链。**
- **同类托管商是否率先支持** —— 谁先做，谁拿到第一批机构事件敞口。


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]])。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。

---
id: "concept:prime-brokerage"
type: concept
title: Prime Brokerage
title_zh: 主经纪/机构交易综合服务
title_en: Prime Brokerage
aliases:
  - Prime Broker
  - 主经纪
  - 主经纪商
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "mmf:falconx"
    rel: instantiated-by
    note: 机构 crypto prime broker
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---
# Prime Brokerage | 主经纪/机构交易综合服务

## Executive Definition / Chinese Explanation | 定义与解释

**Prime Brokerage | 主经纪商** = 给机构客户提供一站式服务的中介：跨场所交易接入、融资融券、托管、清算、以及**跨场所的保证金统一计算**。

一句话：**机构不想和十个场馆分别开户、分别放保证金，主经纪商把这十个变成一个。**

## Why This Matters | 为什么重要

主经纪商主要解决**资本效率**问题；事件市场在跨场所净额与保证金复用方面仍有明显限制。

一个机构要在 5 个事件市场平台配置，现状是：
- 5 个账户、5 份 KYC、5 笔独立的全额抵押。
- **同一事件的对冲头寸不能互抵**（见 [[cross-margin]]）。

**资本效率被切成五份**。主经纪商在传统市场解决了这个问题；在事件市场，它还不存在。

**而它不存在的根本原因不是没人想做，是跨场所净额需要语义等价证明**（见 [[contract-equivalence]]）—— 那份文件目前没人出具。

## How It Works | 机制怎么运转

主经纪商提供的四项核心服务：

| 服务 | 客户得到什么 |
|---|---|
| **统一接入** | 一个 API 连所有场馆 |
| **统一保证金** | 跨场所净额，资本效率数倍提升 |
| **融资** | 借入资金或证券放大头寸 |
| **托管与清算** | 资产集中保管、统一对账 |

**第二项是全部价值所在**，也是最难的：它要求主经纪商能够**证明两个场馆的头寸可以互抵**。

在传统市场这靠标准化合约；**在事件市场，合约跨场所不等价，所以互抵无据可依。**

## Concrete Example | 具体例子

一个机构在两个事件市场的对冲头寸：

```
平台 A: "某法案 Q4 前通过" YES  $5M
平台 B: "某法案 2026 年内通过" NO  $5M
```

- **有主经纪商且合约等价** → 净敞口近零，保证金可能只需 $500k。
- **无主经纪商** → 两边各锁 $5M，**共占用 $10M**。
- **有主经纪商但合约不等价** → **穿仓风险**：判定时点不同，两边可能同时亏（见 [[basis-risk]]）。

**第三种最危险**：它给了资本效率的错觉，而底层的等价性假设是错的。

**所以事件市场的主经纪商必须先解决语义判定，才能谈净额** —— 顺序不能反。

## Common Misconceptions | 常见误解

- **误解一："主经纪商就是券商。"** 券商提供交易通道；主经纪商额外提供融资、跨场所净额和统一托管。
- **误解二："事件市场不需要主经纪商。"** 恰恰相反 —— 全额抵押的资本效率问题让它更需要。
- **误解三："把各场馆头寸加总就是净额。"** 净额需要证明可互抵。**不等价的合约相加是伪净额，会制造穿仓。**

## In Practice | 实战里怎么用

评估任何"跨场所保证金"方案，问三件事：

1. **凭什么互抵？** 有等价性判定吗？五维对齐检查过吗（见 [[contract-equivalence]]）？
2. **不等价时怎么处理？** 记为基差头寸还是照样抵扣？**照样抵扣的方案不要用。**
3. **穿仓谁承担？** 主经纪商自担还是转嫁客户？

**对做基础设施的人**：**跨场所净额的前置条件是一份可信的等价性判决书** —— 这份文件目前没人出具，而它直接站在机构资金的闸门上。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 主经纪商四项服务里，哪一项是全部价值所在？为什么最难？
  A: 统一保证金（跨场所净额）。它要求证明两个场馆的头寸可以互抵，而事件合约跨场所不等价，互抵无据可依。
- Q: '有主经纪商但合约不等价'为什么最危险？
  A: 它给了资本效率的错觉而底层等价假设是错的：判定时点不同可能两边同时亏，造成穿仓。
- Q: 事件市场主经纪商必须先解决什么才能谈净额？
  A: 语义等价判定 —— 顺序不能反，否则是伪净额。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

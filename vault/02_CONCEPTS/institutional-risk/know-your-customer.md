---
id: "concept:know-your-customer"
type: concept
title: KYC
title_zh: 了解你的客户/身份验证
title_en: KYC
aliases:
  - KYC
  - Know Your Customer
  - 了解你的客户
status: reviewed
importance: tier-2
domains:
  - institutional-risk
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
  - id: "concept:anti-money-laundering"
    rel: mechanism-of
    note: 准入身份控制
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# KYC | 了解你的客户/身份验证

## Executive Definition / Chinese Explanation | 定义与解释

**KYC (Know Your Customer) | 客户身份识别** = 金融机构在开户和持续经营中核实客户身份、了解其资金来源与交易目的的法定义务。

它不是"填个表"，是一套持续义务：开户时识别、期间持续监控、异常时上报。

## Why This Matters | 为什么重要

KYC 是事件市场里一条**清晰的分界线**：它把市场切成了两个世界。

| | 持牌世界 | 灰色世界 |
|---|---|---|
| KYC | 强制 | 通常没有 |
| 客户 | **机构可以进** | 只有散户与匿名资金 |
| 监管救济 | 有 | 无 |

**机构不能在没有 KYC 的平台上交易** —— 不是不想，是合规部门不批。所以 KYC 不只是成本，它是**机构资金的准入闸门**（见 [[regulatory-access]]）。

这解释了为什么持牌路线对场馆有战略价值：**牌照 + KYC = 能服务机构。**

## How It Works | 机制怎么运转

KYC 的三层要求，一层比一层重：

1. **身份识别（CIP）** —— 姓名、地址、证件、实益所有人。
2. **尽职调查（CDD）** —— 了解资金来源、交易目的、预期活动模式。
3. **强化尽调（EDD）** —— 对高风险客户（政治公众人物、高风险辖区）额外核查。

**加密市场特有的一层**：链上地址与身份的绑定。传统 KYC 认的是账户，链上要处理的是**地址簇** —— 一个人可以有无数地址，而资金在地址之间流动（见 [[know-your-transaction]]）。

## Concrete Example | 具体例子

同一个机构想配置 $10M 到预测市场，两条路：

| | 持牌平台 | 离岸平台 |
|---|---|---|
| KYC | 完整 | 无或极简 |
| 合规部门能否批准 | **能** | **不能** |
| 可交易品类 | 受限（监管批准的） | 全部 |
| 流动性 | 可能更薄 | 可能更厚 |

**这就是事件市场的结构性张力**：**流动性在灰色世界，资金在持牌世界。**

谁先把两者接上，谁就拿到这个市场的下一段增长 —— 这也是持牌场馆愿意花 $112M 买牌照的原因（见 [[regulatory-access]]）。

## Common Misconceptions | 常见误解

- **误解一："KYC 只是合规成本。"** 它同时是准入资产 —— 没有它就服务不了机构客户。
- **误解二："做了 KYC 就合规了。"** KYC 是持续义务，不是一次性动作；还需要配套的交易监控与上报（见 [[anti-money-laundering]]）。
- **误解三："链上匿名所以 KYC 无意义。"** 链上是**假名**不是匿名 —— 地址行为可被分析和聚类，出入金环节仍会撞上 KYC。

## In Practice | 实战里怎么用

判断一个平台的机构可用性，从 KYC 往回推：

1. **有没有完整 KYC？** 没有 → 机构资金进不来，无论流动性多好。
2. **KYC 由谁做、什么标准？** 平台自建还是持牌托管方？
3. **有没有机构账户结构？** 子账户、权限分离、审计导出 —— 这些是机构的硬需求。

**一条实用推论**：如果你在做面向机构的产品，**不碰客户资金、不做撮合的业务模型可以绕开大部分 KYC 义务** —— 代价是放弃交易费收入（见 [[regulatory-access]]）。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: KYC 的三层要求是什么？
  A: 身份识别 CIP、尽职调查 CDD（资金来源与交易目的）、强化尽调 EDD（高风险客户）。
- Q: 为什么说 KYC 不只是成本，而是准入资产？
  A: 机构合规部门不会批准在无 KYC 平台交易，所以 KYC 是机构资金能否进入的闸门。
- Q: 事件市场的结构性张力是什么？
  A: 流动性集中在灰色世界，而资金在持牌世界；接上两者的人拿到下一段增长。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

---
id: "concept:collateral"
type: concept
title: Collateral
title_zh: 抵押品/担保资产
title_en: Collateral
aliases:
  - 抵押品
status: reviewed
importance: tier-2
domains:
  - derivatives
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
related: []
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Collateral | 抵押品/担保资产

## Executive Definition / Chinese Explanation | 定义与解释

**Collateral | 抵押品 / 担保资产** = 你交出来、用于保证自己会履约的资产。对方拿着它，是因为不信任你的口头承诺。

抵押品制度的存在，就是为了把"信任一个人"替换成"持有一样东西"。

## Why This Matters | 为什么重要

事件市场把抵押品制度推到了极端：**全额抵押** —— 不是抵押最大可能亏损的一部分，而是全部。

这带来的性质很干净：**违约在机制上不可能发生**（见 [[fully-collateralized-market]]）。但它同时把三个新问题带了进来：

1. **抵押品本身的风险** —— 抵押品是稳定币，那么发行方的风险就成了你的风险（见 [[stablecoin]]）。
2. **资金效率** —— 钱被锁死，无法他用。
3. **抵押品集中度** —— 所有头寸用同一种抵押品，就是一个隐藏的共因（见 [[concentration-risk]]）。

## How It Works | 机制怎么运转

评估任何抵押品安排，三个维度：

| 维度 | 问题 |
|---|---|
| **质量** | 抵押品本身会不会跌价 / 脱锚 / 被冻结？ |
| **折扣（haircut）** | 接受时打几折？折扣反映了对质量的判断 |
| **控制** | 抵押品在谁手上？能不能被再抵押（rehypothecation）？ |

**第三条在传统市场是重大风险源**：券商把客户抵押品再拿去抵押，链条一长，一处违约传导全链。

**事件市场的链上全额抵押天然排除了再抵押** —— 钱锁在合约里，没有人能把它拿去做别的。**这是一个真实的结构性优势，值得明确指出。**

## Concrete Example | 具体例子

同样是"抵押 $100k"，三种安排的风险完全不同：

| 安排 | 抵押品去向 | 你承担 |
|---|---|---|
| 传统券商保证金 | 进券商账户，**可能被再抵押** | 券商信用 + 链条传导 |
| 持牌平台隔离账户 | 独立托管，不得挪用 | 托管行信用（有法律救济） |
| **链上合约全额抵押** | **锁在合约，无人可动** | **合约代码 + 稳定币发行方** |

**第三行把信用风险换成了技术风险与发行方风险。**

这不是"更安全"或"更不安全"，是**风险换了种类**：你从"相信一家公司"变成"相信一段代码和一个发行方"。**哪种更好取决于你更能评估哪一种。**

## Common Misconceptions | 常见误解

- **误解一："抵押品越多越安全。"** 数量解决违约风险，不解决抵押品**质量**风险。用一个会脱锚的资产做全额抵押，安全性并不高。
- **误解二："全额抵押不需要关心抵押品。"** 恰恰相反 —— 全额抵押意味着你 100% 暴露于抵押品的风险。
- **误解三："链上抵押没有对手方。"** 有 —— **稳定币发行方就是你的对手方**，只是它不出现在合约里。

## In Practice | 实战里怎么用

对你的全部头寸做一次抵押品体检：

1. **抵押品是什么？** 逐个列出，不要只说"稳定币"。
2. **发行方集中度？** 全部用同一种？那是 100% 集中。
3. **抵押品能被冻结吗？** 发行方保留冻结权吗？
4. **能被再抵押吗？** 链上合约通常不能；链下托管要问清楚。

**再算一个数：抵押品打 5% 折时，你的组合怎样？** 这个情景演练大多数人从没做过，但它是全额抵押模式下最直接的尾部风险。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 全额抵押消除了违约风险，但带来了哪三个新问题？
  A: 抵押品本身的风险（如稳定币发行方）、资金效率（钱被锁死）、抵押品集中度（同一种抵押品是隐藏共因）。
- Q: 什么是再抵押（rehypothecation）？事件市场为什么天然排除它？
  A: 券商把客户抵押品再拿去抵押，链条一长一处违约传导全链。链上全额抵押的钱锁在合约里，无人能挪作他用。
- Q: 链上全额抵押把信用风险换成了什么？
  A: 技术风险（合约代码）与发行方风险（稳定币）。不是更安全，是风险换了种类。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

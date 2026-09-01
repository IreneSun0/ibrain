---
id: "concept:stablecoin"
type: concept
title: Stablecoin
title_zh: 稳定币
title_en: Stablecoin
aliases:
  - 稳定币
status: reviewed
importance: tier-1
domains:
  - stablecoins-wallets-payments
  - blockchain
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
  - id: "concept:token"
    rel: special-case-of
    note: 锚定稳定价值的 token
  - id: "org:tether"
    rel: instantiated-by
    note: USDT — 约六成稳定币供应
  - id: "org:circle"
    rel: instantiated-by
    note: USDC 发行方
  - id: "concept:settlement-rail"
    rel: see-also
    note: 稳定币+公链共同构成 crypto 的事实结算轨
prerequisites:
  - "concept:token"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Stablecoin | 稳定币

## Executive Definition / Chinese Explanation | 定义与解释

**Stablecoin | 稳定币** = 声称与某种参考资产（通常是美元）保持固定比价的链上代币。

机制一句话：**发行方收你 1 美元存进储备，给你 1 枚链上凭证，承诺随时 1:1 赎回。** 它的稳定性完全来自这个赎回承诺，而不是来自代码。

## Why This Matters | 为什么重要

事件市场几乎全部以稳定币计价、在稳定币轨道上流动。这意味着一件很多人没意识到的事：

**你的"无违约风险"的全额抵押头寸，底层枕着发行方的储备管理。**

一个 $10k 的 USDC 抵押头寸，实际承担了三层风险：
1. 事件结果（你知道的那个）
2. 裁决正确性（你可能没算的那个）
3. **发行方的偿付能力与储备质量（你几乎肯定没算的那个）**

**机构风控清单上第三行不能省。**

## How It Works | 机制怎么运转

按抵押方式分三类，风险形态完全不同：

| 类型 | 机制 | 主要风险 |
|---|---|---|
| **法币抵押** | 储备里是现金和短期国债（USDC / USDT） | 储备质量、托管银行、发行方冻结权 |
| **加密抵押** | 超额抵押加密资产 | 抵押品暴跌时的清算螺旋 |
| **算法型** | 靠机制维持锚定，无足额储备 | **已被反复证明会崩** |

对法币抵押型，真正要看的是三件事：
1. **储备构成** —— 现金、国债、还是商业票据？期限多长？
2. **审计频率与审计方** —— 月度证明 vs 年度审计，差别很大。
3. **冻结权** —— 发行方能不能冻结地址？答案通常是能。

## Concrete Example | 具体例子

脱锚的实际影响，用数字说明为什么不能忽略：

假设你持有 $1M 的事件合约头寸，抵押品是某稳定币。该币短暂脱锚到 $0.92：

- 你的合约头寸本身没变 —— 仍然是 1M 份。
- 但**抵押品的美元价值变成了 $920k**。
- 如果你此刻要退出，实际拿到的是打折的钱。
- 若脱锚发生在裁决日附近，你可能被迫在最差的时点承担这个损失。

**脱锚不需要持久，只需要发生在错误的时刻。** 而事件市场的资金流动恰恰集中在裁决日 —— 那是压力最大的时点。

## Common Misconceptions | 常见误解

- **误解一："稳定币就是美元。"** 它是**对发行方的索赔权**，不是美元本身。这个区别在压力时刻才显现。
- **误解二："储备充足就安全。"** 还要看储备的**流动性**（能不能快速变现）和**托管银行**（银行倒闭会传导）。
- **误解三："链上资产不会被冻结。"** 主流法币抵押稳定币的发行方**都保留冻结地址的能力**，且实际使用过。

## In Practice | 实战里怎么用

把稳定币风险明确写进事件敞口的风险清单：

1. **按发行方分桶** —— 你的全部抵押品是不是同一种稳定币？（见 [[concentration-risk]] 的第四维度）
2. **查储备构成与审计** —— 最新一期证明什么时候发的？谁做的？
3. **算脱锚情景** —— 抵押品打 5% 折时，你的组合怎样？打 10% 呢？
4. **记下冻结风险** —— 你的地址会不会因为交互过某些合约而被牵连冻结？

**第 1 条最容易被忽略**：分散在十个事件上但全部用同一种稳定币抵押，在这个维度上是 100% 集中。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 稳定币的稳定性来自什么？
  A: 发行方的 1:1 赎回承诺与背后的储备，而不是代码。它是对发行方的索赔权，不是美元本身。
- Q: 持有以稳定币抵押的事件合约，实际承担了哪三层风险？
  A: 事件结果、裁决正确性、以及发行方的偿付能力与储备质量。
- Q: 为什么短暂脱锚也可能造成实际损失？
  A: 脱锚不需要持久，只需要发生在错误的时刻 —— 事件市场的资金流动集中在裁决日，那正是压力最大的时点。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = token; typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

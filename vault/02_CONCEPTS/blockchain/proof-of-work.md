---
id: "concept:proof-of-work"
type: concept
title: PoW
title_zh: 工作量证明
title_en: PoW
aliases:
  - PoW
  - Proof of Work
  - 工作量证明
status: reviewed
importance: tier-2
domains:
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
  - id: "concept:consensus"
    rel: special-case-of
prerequisites:
  - "concept:consensus"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# PoW | 工作量证明

## Executive Definition / Chinese Explanation | 定义与解释

**PoW (Proof of Work) | 工作量证明** = 通过消耗真实算力（电）来争夺记账权的[[consensus|共识]]机制。

它的安全逻辑只有一句：**改写历史需要重做之后所有区块的工作量，而那个成本高到不划算。**

## Why This Matters | 为什么重要

PoW 是第一个在没有中心机构的前提下解决[[double-spending|双花]]的方案 —— 整个链上世界的起点。

对事件市场，PoW 链的两个性质值得注意：

1. **概率性最终性** —— 确认数越多越安全，但**永远不是绝对**。这意味着结算后需要等待期才能安全提现（见 [[transaction]]）。
2. **吞吐低、费用高** —— 事件市场的小额头寸在 PoW 主链上不经济（见 [[gas]]）。

**所以事件市场几乎都不在 PoW 链上结算** —— 这是成本与最终性的双重排除。

## How It Works | 机制怎么运转

```
矿工不断尝试随机数, 直到区块哈希小于目标难度
找到的人获得记账权与出块奖励
其他节点验证极快 (算一次哈希即可)
```

**"难算易验"是这套机制的关键**：作恶要付出真实成本，检查作恶几乎免费。

**攻击成本 = 获得多数算力的成本。** 对成熟大链，这是天文数字；**对小链，可能只需要租几小时算力** —— 这就是小链更容易遭受重组攻击的原因。

## Concrete Example | 具体例子

为什么最终性对事件市场结算是硬要求：

```
判定完成 → 合约分配资金 → 赢家提现 → 卖出变现
                              ↑
                    若此时发生深度重组
                    链上记录改变, 但钱已离开
```

**PoW 的概率性最终性意味着这个窗口永远存在，只能通过等待确认数来压缩。**

对比：多数现代 PoS 链有明确最终性 —— 达到某个条件后区块**在协议层面不可回滚**。

**这就是为什么事件市场倾向选择有明确最终性的结算环境**：结算的确定性必须早于资金的可提取性。

## Common Misconceptions | 常见误解

- **误解一："PoW 浪费能源所以是坏设计。"** 能源消耗**就是**安全预算 —— 它让作恶变得昂贵。是否值得取决于所保护资产的价值。
- **误解二："算力大就一定安全。"** 要看**攻击成本相对可获收益**。小链算力低，租算力攻击可能划算。
- **误解三："确认 6 次就绝对安全。"** 6 次是惯例不是保证；概率性最终性没有"绝对"。

## In Practice | 实战里怎么用

判断一条链能否承载你的事件市场结算，三问：

1. **最终性是概率性还是确定性？** 后者的结算风险窗口小得多。
2. **达到可接受安全所需的确认时间是多久？** 拿它对照平台的提现等待期。
3. **该链的攻击成本是多少？** 小链要特别当心 —— 租算力攻击的成本可能远低于可窃取的金额。

**一条通用判据（见 [[double-spending]]）**：**结算确定性必须早于资金可提取性。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: PoW 的安全逻辑是什么？
  A: 改写历史需要重做之后所有区块的工作量，成本高到不划算；难算易验让作恶昂贵而检查免费。
- Q: 为什么事件市场几乎不在 PoW 主链上结算？
  A: 概率性最终性带来结算风险窗口，加上吞吐低费用高使小额头寸不经济 —— 成本与最终性的双重排除。
- Q: 为什么小链比大链更容易遭受重组攻击？
  A: 攻击成本是获得多数算力的成本；小链算力低，租算力几小时可能就足够，成本可能远低于可窃取的金额。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

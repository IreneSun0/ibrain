---
id: "concept:call-option"
type: concept
title: Call Option
title_zh: 看涨期权
title_en: Call Option
aliases:
  - 看涨期权
status: reviewed
importance: tier-2
domains:
  - derivatives
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
  - id: "concept:option"
    rel: special-case-of
  - id: "concept:put-option"
    rel: contrasts-with
    note: 从上涨获利 vs 从下跌获利/尾部保护
prerequisites:
  - "concept:option"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Call Option | 看涨期权

## Executive Definition / Chinese Explanation | 定义与解释

**Call Option | 看涨期权** = 给你**在到期日以约定价格买入**标的的权利，但没有义务。

你付一笔权利金买下这个不对称性：标的涨过行权价，你行权赚钱；跌了，你放弃行权，最多亏权利金。

## Why This Matters | 为什么重要

看涨期权是理解**不对称支付**最直接的例子，而不对称性正是风险管理的核心工具。

对事件市场，它提供一个重要对照：**买入一份事件合约在支付形状上接近买入一个深度价外的看涨期权** —— 最大损失是本金，最好情况是数倍回报（见 [[binary-option]]）。

**区别在于事件合约的支付是台阶而非斜坡**：到期要么 $1 要么 $0，没有中间态。这让 delta 在临近到期时行为诡异，也让传统对冲方法失效。

## How It Works | 机制怎么运转

看涨期权的支付：

```
到期收益 = max(标的价 − 行权价, 0) − 权利金
```

三个决定价格的因素：
1. **内在价值** —— 现在行权能赚多少（不能为负）。
2. **时间价值** —— 剩余时间里变好的可能性，**随到期临近衰减到零**。
3. **波动率** —— 标的越可能大幅波动，期权越值钱。

**第 3 条对事件合约不适用**：事件的"波动率"不是连续量，它是一个跳跃概率 —— 而那个概率就是价格本身（见 [[margin]] 里的循环问题）。

## Concrete Example | 具体例子

同一个"押注上涨"的判断，三种工具：

| 工具 | 投入 | 最坏 | 最好 |
|---|---|---|---|
| 现货 | $10,000 | −$10,000（归零） | 无上限 |
| **看涨期权** | $500 权利金 | **−$500** | 无上限 |
| 事件合约 0.05 | $500 | **−$500** | **+$9,500**（到 $1） |

**期权和事件合约的最坏情况相同（本金有界）**，最好情况的形状不同：期权无上限但需要标的持续上涨；事件合约上限固定，但只要命题成立就全额兑付。

**选哪个取决于你的观点形状**：看"涨多少"用期权，看"会不会发生"用事件合约。

## Common Misconceptions | 常见误解

- **误解一："买期权是高杠杆所以危险。"** 买方最大损失是权利金，**风险有界**。危险的是卖方（承担义务的一侧）。
- **误解二："期权定价靠 Black-Scholes 就够了。"** BSM 假设标的连续变动，对跳跃型标的（包括事件）不适用。
- **误解三："深度价外期权就是彩票。"** 它是低概率事件的定价工具；价格是否合理取决于市场对那个概率的估计对不对。

## In Practice | 实战里怎么用

用一个问题决定该用期权还是事件合约：

> **我的观点是关于"幅度"还是关于"是否"？**

- **幅度**（会涨多少 / 通胀会到几） → 期权或[[scalar-market|标量合约]]。
- **是否**（会不会发生） → 事件合约。

**用错工具的代价很具体**：用一串事件合约去表达"幅度"观点，你会付出多个盘口的流动性折价；用期权去表达"是否"观点，你会为不需要的连续暴露付时间价值。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 看涨期权买方的最大损失是多少？为什么说危险的是卖方？
  A: 买方最大损失是权利金，风险有界；卖方承担义务，理论上损失可能无界。
- Q: 为什么 Black-Scholes 对事件合约不适用？
  A: BSM 假设标的连续变动，而事件标的是跳跃的；且事件的'波动率'本质是跳跃概率，而那个概率就是价格本身。
- Q: 怎么决定该用期权还是事件合约？
  A: 看观点形状：关于'幅度'用期权或标量合约，关于'是否发生'用事件合约。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

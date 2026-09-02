---
id: "concept:binary-option"
type: concept
title: Binary/Digital Option
title_zh: 二元/数字期权
title_en: Binary/Digital Option
aliases:
  - Binary/Digital Option
  - 二元
status: reviewed
importance: tier-1
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
    note: "支付只有固定金额或 0, 无连续 payoff"
prerequisites:
  - "concept:option"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Binary/Digital Option | 二元/数字期权

## Executive Definition / Chinese Explanation | 定义与解释

**Binary / Digital Option | 二元期权 / 数字期权** = 支付只有两种可能的合约：条件成立付固定金额，不成立付零。

**事件合约在数学上就是二元期权。** 理解这一点能立刻把整个期权理论的工具箱借过来 —— 也能立刻看清哪些工具在这里会失效。

## Why This Matters | 为什么重要

二元支付的形状带来三个直接后果：

1. **价格 ≈ 概率** —— 到期付 $1 或 $0，风险中性下现价就是概率（见 [[implied-probability]]）。这是预测市场全部叙事的数学基础。
2. **最坏情况开仓即知** —— 0.30 买入，最多亏 0.30。没有尾部意外。
3. **希腊字母行为诡异** —— 临近到期且接近阈值时，delta 会剧烈跳变（趋于无穷），**传统对冲方法在这里会失控**。

第 3 点是专业玩家才会撞上的墙，但它解释了很多"临近裁决日流动性消失"的现象。

## How It Works | 机制怎么运转

二元期权与普通（香草）期权的关键差异：

| | 香草期权 | 二元期权 |
|---|---|---|
| 支付 | max(S−K, 0)，连续 | $1 或 $0，台阶 |
| 到期时 delta | 平滑趋于 0 或 1 | **在 K 附近趋于无穷** |
| 可否 delta 对冲 | 可以 | **临近到期时实际上不可能** |
| 最大损失 | 权利金 | 本金 |

**"delta 在阈值附近趋于无穷"的实际含义**：当标的贴着阈值、时间又快到期时，价格对标的的微小变动极度敏感。做市商此时无法用标准方法对冲，**理性反应就是拉宽价差或撤单。**

**这就是"临近裁决日盘口变薄"的数学原因** —— 不是做市商懒，是对冲在数学上失效了。

## Concrete Example | 具体例子

一个"某指数年底收于 5000 点以上"的二元合约，标的现价 4995：

| 距到期 | 合约价格 | 指数涨 10 点的影响 |
|---|---|---|
| 3 个月 | 0.52 | → 0.55（+3 分） |
| 1 周 | 0.48 | → 0.62（+14 分） |
| 1 小时 | 0.35 | → **0.95（+60 分）** |

**同样的 10 点变动，影响从 3 分放大到 60 分。**

对做市商：最后一小时里，标的每跳动一下，它的库存价值就剧烈重估。**在这种条件下报紧价差等于送钱。** 所以它要么大幅拉宽，要么退出 —— 而这恰恰是交易者最想调整头寸的时刻。

## Common Misconceptions | 常见误解

- **误解一："二元期权比普通期权简单。"** 支付简单，**对冲极难**。简单的是描述，不是风险管理。
- **误解二："二元期权是赌博工具。"** 在很多零售场景确实被这样滥用过，但工具本身是标准的衍生品结构，CME 等受监管场所也有类似产品。
- **误解三："价格就是概率，所以 0.5 就是抛硬币。"** 0.5 也可能意味着"市场完全不知道"或"流动性太薄，价格没有信息"。**要看深度才知道那个 0.5 有多少分量。**

## In Practice | 实战里怎么用

交易任何二元合约前，看两个数：

1. **距到期时间** —— 越近，价格对标的越敏感，滑点与价差越大。
2. **标的与阈值的距离** —— 贴着阈值（at-the-money）时波动最剧烈。

**两者结合的危险象限：临近到期 + 贴近阈值。** 在这个象限里：
- 价格会剧烈跳动；
- 做市商大概率已经撤了；
- **你想平仓时很可能出不去。**

**实用纪律：在进入这个象限之前决定好持有到期还是提前退出。** 到了里面再决定，通常已经没有选择权了。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么事件合约在数学上就是二元期权？
  A: 支付只有两种可能：条件成立付固定金额（$1），不成立付零。这决定了价格≈概率与最坏情况开仓即知。
- Q: 为什么临近裁决日盘口会变薄？给出数学原因。
  A: 二元期权的 delta 在临近到期且贴近阈值时趋于无穷，标准 delta 对冲在数学上失效，做市商只能拉宽价差或撤单。
- Q: 二元合约交易中最危险的象限是什么？
  A: 临近到期 + 标的贴近阈值 —— 价格剧烈跳动、做市商多已撤离、想平仓时可能出不去。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

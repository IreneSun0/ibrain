---
id: "concept:liquidity"
type: concept
title: Liquidity
title_zh: 流动性
title_en: Liquidity
aliases:
  - 流动性
status: reviewed
importance: tier-1
domains:
  - market-microstructure
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
  - id: "concept:depth"
    rel: measured-by
  - id: "concept:spread"
    rel: measured-by
  - id: "concept:slippage"
    rel: measured-by
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Liquidity | 流动性

## Executive Definition / Chinese Explanation | 定义与解释

**Liquidity | 流动性** = 你能多快、以多接近当前价格的代价，把一个头寸换成现金（或反过来）。

它不是一个数字，是**四个维度**：
- **紧度（tightness）** — 价差多宽
- **深度（depth）** — 能吃多少不推动价格
- **韧性（resilience）** — 被冲击后多久恢复
- **即时性（immediacy）** — 现在就要成交要付多少

只报其中一个的"流动性指标"都是不完整的。

## Why This Matters | 为什么重要

流动性是事件市场唯一真正的护城河，也是它最大的结构性弱点。

原因在于一个数学事实：**事件市场的合约数量以万计，而资金是有限的。** 每开一个新事件、每加一个新场所，同一笔资金就被切得更碎。这与股票市场正好相反 —— 股票的标的数量是稳定的，事件的数量可以无限增长。

**所以"上更多市场"对事件平台不是纯增长，是对自己流动性的稀释。**

## How It Works | 机制怎么运转

流动性的来源只有三个，按可靠性排序：

1. **自然双向需求** — 真的有人想买、也真的有人想卖。最健康，但只存在于少数高关注事件。
2. **做市商** — 用资本填补时间错配。可靠，但要付激励，且会在压力下撤退。
3. **激励挖矿 / 补贴** — 最快见效，最不可持续。补贴停了流动性就走。

**判断一个市场的流动性质量，就是看这三者的构成比例。** 靠第 3 项撑起来的深度，在你真正需要的时候不会在。

## Concrete Example | 具体例子

事件市场的流动性分布极度长尾。典型形态是：

- **头部少数几个事件**（总统大选、重大议息）—— 占据平台绝大部分深度，价差 1 分以内。
- **中部若干事件** —— 有做市商报价，价差 3–5 分，深度几千美元。
- **长尾成千上万个事件** —— 盘口基本空着，或只有极宽的报价。

**平台公布的"总成交额"几乎全部来自头部。** 用它来推断"这个平台流动性好"，就像用一线城市房价推断全国房价。真正该问的是：**中位数事件的深度是多少？**

## Common Misconceptions | 常见误解

- **误解一："流动性 = 成交量。"** 成交量是历史，流动性是此刻的可执行能力。刷量能造成交量，造不出流动性。
- **误解二："流动性是平台属性。"** 它是**合约属性**。同一平台上，头部合约和长尾合约的流动性差几个数量级。
- **误解三："流动性会一直在。"** 它在消息冲击、临近裁决、极端行情时集中消失 —— 这三个时刻恰好是你最需要它的时候。

## In Practice | 实战里怎么用

评估任何事件市场，别问"流动性好不好"，问这四个数：

1. **中位数合约**的 ±1% 深度是多少？（不是头部合约）
2. 价差的**中位数和 90 分位**分别是多少？
3. 大单冲击后深度的**恢复时间**？
4. 深度里有多大比例来自**补贴驱动的挂单**？

第 4 条最难拿到但最关键。一个简单的代理指标：**看激励活动结束前后一周的深度变化。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 流动性的四个维度是什么？
  A: 紧度（价差）、深度（可承载规模）、韧性（恢复速度）、即时性（立刻成交的代价）。
- Q: 为什么'上更多市场'对事件平台可能是负面的？
  A: 事件数量可无限增长而资金有限，每开一个新市场就把同一笔流动性切得更碎。
- Q: 为什么用平台总成交额判断流动性会严重误导？
  A: 成交额几乎全部来自头部少数事件，长尾合约的真实深度可能接近零。该看中位数合约的深度。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

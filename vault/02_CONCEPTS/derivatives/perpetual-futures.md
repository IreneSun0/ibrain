---
id: "concept:perpetual-futures"
type: concept
title: Perpetual Futures / Perp
title_zh: 永续合约
title_en: Perpetual Futures / Perp
aliases:
  - Perpetual Futures / Perp
  - 永续合约
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
  - id: "concept:futures-contract"
    rel: special-case-of
    note: "去掉到期日, 用资金费率锚定现货"
prerequisites:
  - "concept:futures-contract"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Perpetual Futures / Perp | 永续合约

## Executive Definition / Chinese Explanation | 定义与解释

**Perpetual Futures | 永续合约** = 没有到期日的期货。你可以永远持有，直到自己平仓或被强平。

去掉到期日会带来一个问题：**没有交割日，价格靠什么锚定现货？** 答案是[[funding-rate|资金费率]] —— 一个持续的现金流，把永续价格拉回现货。

## Why This Matters | 为什么重要

永续是加密市场最主要的衍生品形态，理解它对理解事件市场有两层用处：

1. **对照**：永续是"无限期 + 保证金 + 会爆仓"，事件合约是"有明确到期 + 全额抵押 + 不爆仓"。**两者在风险形状上几乎是镜像。**
2. **警示**：永续的百倍杠杆和连环强平塑造了外界对"加密衍生品"的印象，而事件合约恰恰相反 —— 但常被一起归类（见 [[leverage]]）。

## How It Works | 机制怎么运转

资金费率的机制：

```
若 永续价 > 现货价  → 多头付钱给空头  → 抑制做多
若 永续价 < 现货价  → 空头付钱给多头  → 抑制做空
```

每 8 小时（各平台不同）结算一次。**它不是手续费，是多空之间的转移支付** —— 平台通常不抽成。

这个设计的巧妙之处：**不需要交割，就能让价格自我锚定**。代价是持有成本不确定 —— 你的持仓成本取决于市场情绪，而不是一个已知的利率。

## Concrete Example | 具体例子

持有一个永续多头 30 天，资金费率的实际影响：

```
名义仓位     $100,000
平均资金费率  +0.01% / 8h  (多头付)
每日成本      $100,000 × 0.03% = $30
30 天累计     $900   ← 占名义 0.9%
```

**在牛市里资金费率可以长期为正且远高于此** —— 年化 30–50% 的持有成本并不罕见。

**对照事件合约**：全额抵押的事件合约没有资金费率，但有资金占用的机会成本（见 [[fully-collateralized-market]]）。**两者都在收你"持有时间"的钱，只是形式不同：一个是显性现金流，一个是隐性机会成本。**

## Common Misconceptions | 常见误解

- **误解一："永续没有成本，因为不用交割。"** 资金费率就是成本，且在极端行情里非常贵。
- **误解二："资金费率是平台收的。"** 通常是多空之间的转移，平台不抽成。
- **误解三："永续和事件合约都是加密衍生品，风险差不多。"** 风险形状几乎相反：永续会爆仓、无到期；事件合约不爆仓、有明确到期。**混为一谈会严重误判。**

## In Practice | 实战里怎么用

持有任何永续头寸，把资金费率写进成本模型：

```
持有总成本 = 开平仓手续费 + 滑点 + Σ(资金费率 × 名义 × 持有周期数)
```

**再问一个方向性问题**：资金费率长期为正说明多头拥挤 —— 那本身是一个仓位信号。

**对比事件合约时用同一把尺**：把全额抵押的机会成本（`本金 × 无风险利率 × 期限`）算出来，和永续的资金费率放一起比。**这是唯一公平的对照方式。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 永续合约去掉到期日之后，靠什么把价格锚定现货？
  A: 资金费率 —— 永续价高于现货时多头付钱给空头，反之亦然，形成持续的转移支付。
- Q: 资金费率是平台收入吗？
  A: 通常不是，它是多空之间的转移支付，平台一般不抽成。
- Q: 永续合约与事件合约的风险形状为什么几乎是镜像？
  A: 永续无到期、用保证金、会爆仓；事件合约有明确到期、全额抵押、不会爆仓。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = futures-contract; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

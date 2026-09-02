---
id: "concept:portfolio-margin"
type: concept
title: Portfolio Margin
title_zh: 组合保证金
title_en: Portfolio Margin
aliases:
  - 组合保证金
status: reviewed
importance: tier-2
domains:
  - derivatives
  - institutional-risk
tags:
  - concept
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources: []
related:
  - id: "concept:margin"
    rel: special-case-of
    note: 按整个组合净风险计算的保证金模式
  - id: "concept:cross-margin"
    rel: contrasts-with
    note: 全组合情景/风险模型 vs 头寸两两互抵
  - id: "concept:value-at-risk"
    rel: see-also
    note: SPAN/VaR 型风险模型是其计算内核
prerequisites:
  - "concept:margin"
---
# Portfolio Margin | 组合保证金

## Executive Definition / Chinese Explanation | 定义与解释

**Portfolio Margin | 组合保证金** = 按整个组合的净风险收保证金，而不是逐个头寸各收各的。它是[[cross-margin|跨品种保证金]]的完整形态。

核心思路：**如果你的头寸互相对冲，就不该按它们的总和收钱。**

## Why This Matters | 为什么重要

组合保证金是机构资本效率的主要来源，也是事件市场目前**结构性缺失**的一环。

一个机构在 5 个事件市场平台配置，现状是 5 笔独立的全额抵押 —— **同一事件的对冲头寸不能互抵**（见 [[prime-brokerage]]）。资本效率被切成五份。

**而组合保证金要成立，前提是能证明头寸之间真的对冲** —— 在事件市场，这需要跨场所的语义等价判定（见 [[contract-equivalence]]）。**那份文件目前没人出具。**

## How It Works | 机制怎么运转

组合保证金的计算方式：

```
1. 定义一组压力情景 (标的 ±X%, 波动率 ±Y%, 相关性断裂)
2. 对每个情景, 重估整个组合
3. 取最坏情景的损失作为保证金要求
```

**它比逐仓保证金精确得多，也危险得多**：

| | 逐仓 | 组合 |
|---|---|---|
| 资本效率 | 低 | **高（可差数倍）** |
| 依赖假设 | 少 | **相关性假设** |
| 危机时 | 稳健 | **假设失效则严重不足** |

**"相关性假设在压力下仍成立"是全部风险所在** —— 而危机恰恰是相关性突变的时刻。

## Concrete Example | 具体例子

一个跨平台事件组合，两种保证金安排：

```
平台 A: "某法案 Q4 前通过" YES  $5M
平台 B: "某法案 2026 年内通过" NO  $5M
```

- **逐仓**：各锁 $5M，共 $10M。
- **组合（假设等价）**：净敞口近零，可能只需 $500k。
- **实际风险**：**两份合约判定时点不同**（Q4 末 vs 年末）。法案 12 月通过 → A 判 NO、B 判 YES → **两边同时亏，$10M 全损。**

**按"高度相关"给了 $500k 保证金，穿仓 $9.5M。**

**这就是为什么事件市场的组合保证金必须建立在语义判定之上，而不是统计相关性之上。**

## Common Misconceptions | 常见误解

- **误解一："组合保证金就是打折。"** 它是基于情景重估的精确计算，不是一个折扣率。
- **误解二："对冲头寸自然可以互抵。"** 只有语义等价才可以。**同题不同义的合约相加是伪对冲。**
- **误解三："组合保证金更先进所以更好。"** 它更精确也更脆弱 —— 依赖的假设更多，失效后果更严重。

## In Practice | 实战里怎么用

评估任何组合保证金方案，三问：

1. **压力情景怎么设？** 包含相关性断裂的情景吗？
2. **凭什么认为这些头寸对冲？** 统计相关性还是语义等价证明？**事件市场必须是后者。**
3. **假设失效时谁承担？** 有违约瀑布吗？

**风险系统里的默认值应该是"不抵扣"，抵扣需要证明**（见 [[cross-margin]]）。反过来做是穿仓的标准路径。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 组合保证金的核心思路和主要风险是什么？
  A: 按组合净风险而非头寸总和收保证金；主要风险是它依赖'相关性在压力下仍成立'的假设，而危机恰是相关性突变的时刻。
- Q: 为什么事件市场的组合保证金必须建立在语义判定而非统计相关性之上？
  A: 同题不同义的合约在极端情形下可能同时亏损，按统计相关性给出的保证金会严重不足并造成穿仓。
- Q: 风险系统里头寸抵扣的正确默认值是什么？
  A: 默认不抵扣，抵扣需要语义等价的证明。


## Sources

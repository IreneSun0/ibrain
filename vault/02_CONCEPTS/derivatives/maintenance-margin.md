---
id: "concept:maintenance-margin"
type: concept
title: Maintenance Margin
title_zh: 维持保证金
title_en: Maintenance Margin
aliases:
  - 维持保证金
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
related:
  - id: "concept:margin"
    rel: component-of
    note: 持仓底线
  - id: "concept:initial-margin"
    rel: contrasts-with
    note: 开仓门槛 vs 持仓底线 — 跌破后者触发补仓或强平
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Maintenance Margin | 维持保证金

## Executive Definition / Chinese Explanation | 定义与解释

**Maintenance Margin (MM) | 维持保证金** = 账户权益必须始终高于的下限。跌破它就触发追保通知，补不上就[[liquidation|强制平仓]]。

它总是低于[[initial-margin|初始保证金]] —— 两者之间的差就是你的缓冲带。

## Why This Matters | 为什么重要

**MM 才是真正的风险参数，而绝大多数人只看初始保证金。**

初始保证金决定你能开多大杠杆；**维持保证金决定你离爆仓有多远**。两个平台的 IM 相同而 MM 差一倍，你的实际生存概率差很远。

对事件市场，这个概念主要用作对照：**全额抵押没有维持保证金，因为没有强平** —— 最坏情况在开仓时就锁定了。

## How It Works | 机制怎么运转

缓冲带的算法：

```
缓冲 = (权益 − 维持保证金) / 名义
可承受的不利变动 ≈ 缓冲 / 杠杆倍数
```

三个决定你能扛多久的因素：
1. **IM 与 MM 的差** —— 差越大缓冲越厚。
2. **杠杆倍数** —— 杠杆越高，同样的价格变动消耗缓冲越快。
3. **平台的追保宽限期** —— 有的给几小时，有的**直接强平不通知**。

**第 3 条在加密市场差异极大**，而它决定了你有没有机会补救。

## Concrete Example | 具体例子

同样 10 倍杠杆，两个平台的差别：

| | 平台 A | 平台 B |
|---|---|---|
| 初始保证金 | 10% | 10% |
| **维持保证金** | **5%** | **8%** |
| 缓冲 | 5% | **2%** |
| 可承受不利变动 | −5% | **−2%** |
| 追保宽限 | 1 小时 | 无，直接强平 |

**表面上杠杆一样，实际生存能力差 2.5 倍。**

在跳变标的上，2% 的缓冲意味着**一条新闻就能让你出局** —— 而且是在你判断可能完全正确的情况下。

## Common Misconceptions | 常见误解

- **误解一："杠杆倍数决定风险。"** 杠杆决定敏感度，**维持保证金决定生存距离**。两者都要看。
- **误解二："会收到追保通知。"** 很多加密平台在极端行情下直接强平，不给缓冲期。
- **误解三："事件合约也有维持保证金。"** 全额抵押的没有 —— 没有强平机制，也就没有维持线。

## In Practice | 实战里怎么用

开任何保证金头寸前，算清楚这一行：

```
标的反向变动 ____%  → 触发强平
```

然后拿这个数字去对照该标的**一天的正常波动幅度**。**如果日波动大于你的缓冲，你的头寸在统计上活不过一天。**

**对事件合约的推论**：没有这一行要算，因为没有强平。但要把省下的注意力放到裁决风险和集中度上 —— 那才是这个市场真正会让你归零的地方。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说维持保证金比初始保证金更重要？
  A: 初始保证金只决定杠杆倍数，维持保证金决定你离强平有多远 —— 那是真正的生存距离。
- Q: IM 相同而 MM 不同的两个平台，风险差别在哪？
  A: 缓冲带不同：MM 越高缓冲越薄，可承受的不利变动越小，生存能力可能差数倍。
- Q: 为什么全额抵押的事件合约没有维持保证金？
  A: 没有强平机制 —— 最大损失在开仓时已全额锁定，不存在需要维持的下限。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

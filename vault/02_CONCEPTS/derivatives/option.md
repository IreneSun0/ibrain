---
id: "concept:option"
type: concept
title: Option
title_zh: 期权
title_en: Option
aliases:
  - 期权
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
  - id: "concept:derivative"
    rel: special-case-of
  - id: "concept:futures-contract"
    rel: contrasts-with
    note: 权利而非义务 — 权利金换非对称收益 vs 双向义务+保证金
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Option | 期权

## Executive Definition / Chinese Explanation | 定义与解释

**Option | 期权** = 一份给你**权利但不给你义务**的合约：到期时你可以选择行权，也可以放弃。

"权利而非义务"这六个字是全部：它让支付函数变得**非线性**，也让期权成为唯一能"只要好的一半"的工具 —— 代价是先付一笔权利金买下这个不对称性。

## Why This Matters | 为什么重要

期权对理解事件市场有两层用处：

1. **事件合约就是二元期权**（见 [[binary-option]]）—— 整套期权工具箱可以借过来，但要知道哪些会失效。
2. **不对称支付的思维**是风险管理的核心：能不能构造一个"最坏情况有界、最好情况开放"的头寸？

**全额抵押的事件合约天生具有这个性质**：开仓即知最坏情况。这一点常被当作缺点（资金占用），其实它同时是优点（无爆仓）。

## How It Works | 机制怎么运转

期权价值由两部分构成：

```
期权价值 = 内在价值 + 时间价值
```

- **内在价值** —— 现在行权能拿多少（不能为负）。
- **时间价值** —— 剩余时间里情况可能变好的那部分价值，**随到期临近衰减到零**。

**对事件合约的实际含义**：长期限合约的价格里含有时间价值，随判定日临近，价格会向 0 或 1 收敛。**很多人把这个收敛误读为"市场改变了看法"，其实部分只是时间价值的消耗。**

判断价格变动是"新信息"还是"时间衰减"，是读盘的基本功。

## Concrete Example | 具体例子

同一个事件，三个时间点的价格：

| 距判定日 | 价格 | 解读 |
|---|---|---|
| 6 个月 | 0.45 | 不确定性高，价格贴近 0.5 |
| 1 个月 | 0.38 | 部分是新信息，部分是时间价值衰减 |
| 1 天 | 0.12 | 几乎全是内在价值，市场已基本定论 |

**从 0.45 到 0.38 之间发生了什么？** 若没有实质新闻，多半是**时间价值收缩** —— 不确定性减少，价格向真实概率靠拢。

**读盘纪律：看到价格变动，先问"有新消息吗"。** 没有新消息的变动通常来自时间衰减、流动性、或有人在建仓 —— 三者含义完全不同。

## Common Misconceptions | 常见误解

- **误解一："期权是杠杆工具。"** 买方最大损失是权利金，**风险有界**。危险的是卖方（义务方），那才是可能无限的风险。
- **误解二："期权定价靠 Black-Scholes。"** BSM 假设标的连续变动。**事件合约的标的是跳跃的，BSM 推导在这里用不上。**
- **误解三："事件合约价格变了就是市场改主意了。"** 也可能是时间价值衰减、流动性变化、或大户建仓。

## In Practice | 实战里怎么用

把"权利 vs 义务"当成看任何头寸的第一问：

1. **我是买方还是卖方？** 买方风险有界，卖方风险可能无界。
2. **最坏情况是多少？** 写下具体数字。
3. **时间对我有利还是不利？** 买方受时间衰减侵蚀，卖方受益。

**对事件合约的推论**：全额抵押的买方永远在"权利"一侧（最多亏本金）。**这让事件合约成为少数几种散户不会爆仓的衍生品** —— 相对永续合约的真实优势。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 期权'权利而非义务'带来了什么性质？
  A: 非线性支付：买方最坏情况有界（权利金），最好情况开放。代价是先付权利金买下这个不对称性。
- Q: 为什么 Black-Scholes 在事件合约上用不上？
  A: BSM 假设标的连续变动，而事件合约的标的是跳跃的（概率直接跳变），连续假设不成立。
- Q: 看到事件合约价格变动，第一件该问的事是什么？
  A: 有没有新消息。没有新消息的变动可能来自时间价值衰减、流动性变化或大户建仓，三者含义完全不同。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = derivative; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

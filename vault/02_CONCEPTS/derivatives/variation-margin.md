---
id: "concept:variation-margin"
type: concept
title: Variation Margin
title_zh: 变动保证金
title_en: Variation Margin
aliases:
  - 变动保证金
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
  - "source:2026-08-26-cftc-2026-05105-html"
related:
  - id: "concept:margin"
    rel: component-of
    note: 每日盯市结算未实现盈亏
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Variation Margin | 变动保证金

## Executive Definition / Chinese Explanation | 定义与解释

**Variation Margin (VM) | 变动保证金** = 每日（或每笔）按最新结算价结清的盈亏现金流：赚的一方收到钱，亏的一方付出钱。

它和[[initial-margin|初始保证金]]性质完全不同：**IM 是押金（会退），VM 是实际损益的现金交割（不退）。**

## Why This Matters | 为什么重要

VM 是**逐日盯市（mark-to-market）** 的执行机制，也是传统清算体系控制风险的核心手段：

**不让亏损累积。** 每天结清一次，意味着清算所面对的最大敞口只是一天的波动，而不是整个合约期的累计亏损。

**这正是事件合约做不到的地方**：判定日之前没有客观的每日结算价 —— 市场价在薄盘口上可能是噪声。**按噪声逐日结清现金，会制造出不必要的强平。**

## How It Works | 机制怎么运转

```
每日 VM = (今日结算价 − 昨日结算价) × 合约数量 × 乘数
```

VM 的两个关键性质：

1. **是现金，不是抵押品** —— 收到的可以拿去用；付出的是真实亏损。
2. **每日重置敞口** —— 昨天的亏损已结清，清算所今天只面对今天的风险。

**对事件市场的含义**：若要给事件合约引入 VM，必须先解决"每日结算价从哪来"。用市场中间价？薄盘口不可靠。用模型价？模型不存在（见 [[margin]]）。**这是保证金化路径上的第二道墙。**

## Concrete Example | 具体例子

一个 100 手的期货多头，三天的 VM 流：

```
Day 0  开仓 @ 100.0, 交 IM $5,000
Day 1  结算 101.0  → 收 VM +$1,000   (账户 $6,000)
Day 2  结算  99.5  → 付 VM −$1,500   (账户 $4,500 < IM, 追保)
Day 3  结算 102.0  → 收 VM +$2,500   (账户 $7,000)
```

**注意 Day 2**：亏损当天就被现金结清，账户跌破 IM 触发追保 —— 清算所从不让你欠着。

**同样的头寸在全额抵押的事件合约上**：三天里账面价值起伏，但**没有任何现金流动，也没有追保** —— 直到判定日一次性结清。

**两种设计各有代价**：VM 让风险每天归零但制造现金流压力；全额抵押无现金流压力但资金全程占用。

## Common Misconceptions | 常见误解

- **误解一："VM 和 IM 是一回事。"** IM 是押金会退，VM 是已实现损益的现金交割不会退。
- **误解二："逐日盯市只是记账。"** 它是真实现金流动，会造成流动性压力 —— 历史上有机构死在追不上 VM 上。
- **误解三："事件合约加个 VM 就能保证金化了。"** 前提是有可信的每日结算价，而事件合约在判定前没有。

## In Practice | 实战里怎么用

判断一个衍生品体系的风险设计，看两件事：

1. **亏损多久结清一次？** 每日、实时、还是到期一次性？间隔越长，累积敞口越大。
2. **结算价从哪来？** 公开市场、指数、还是内部报价？**结算价的可信度决定整个 VM 机制的可信度。**

**对事件合约的提问**：若某平台声称支持保证金交易，问它每日结算价怎么定 —— 这一问通常能立刻分辨方案是否严肃。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 变动保证金与初始保证金的本质区别是什么？
  A: IM 是押金，平仓后退还；VM 是已实现损益的现金交割，不退还。
- Q: 逐日盯市为什么能控制清算所的风险？
  A: 每天结清一次意味着清算所面对的最大敞口只是一天的波动，而非整个合约期的累计亏损。
- Q: 给事件合约引入 VM 的前置难题是什么？
  A: 需要可信的每日结算价：市场中间价在薄盘口上是噪声，而模型价不存在。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cftc-2026-05105-html]] — <https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = margin; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

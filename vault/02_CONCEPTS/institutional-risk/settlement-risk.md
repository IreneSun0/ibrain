---
id: "concept:settlement-risk"
type: concept
title: Settlement Risk
title_zh: 结算风险
title_en: Settlement Risk
aliases:
  - 结算风险
status: reviewed
importance: tier-2
domains:
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
  - id: "concept:settlement"
    rel: risk-of
    note: 成交后资产/现金未按预期交付 — 方向看对也可能收不到钱
prerequisites:
  - "concept:settlement"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Settlement Risk | 结算风险

## Executive Definition / Chinese Explanation | 定义与解释

**Settlement Risk | 结算风险** = 在"你已经履约"和"对方也已履约"之间那段空窗里，事情出错的风险。

经典形态叫 **Herstatt 风险**：1974 年德国 Herstatt 银行在收到马克之后、支付美元之前被关闭，对手方全部损失。**时差就是风险。**

## Why This Matters | 为什么重要

事件市场把这段空窗**拉长了**，而且多插了两个环节。

价格衍生品：到期 → 读结算价 → 付款。
事件合约：到期 → **判定事件是否发生** → **争议窗口** → 付款。

多出来的两环各自需要时间，而在这段时间里你的钱既不在你手上、也还没结清。**判定与支付之间的时滞敞口，是事件市场最少被计量的一项风险。**

## How It Works | 机制怎么运转

事件市场的结算链条上有四个可能卡住的点：

| 卡点 | 表现 | 谁能救 |
|---|---|---|
| 判定延迟 | 数据源没出数、争议未决 | 平台规则 |
| 争议期冻结 | 资金锁定，无法动用 | 规则明文 |
| 轨道故障 | 稳定币冻结、链拥堵、银行环节 | 视轨道而定 |
| **错误支付** | 钱已按错误结果分出 | **没人**（链上不可逆） |

前三个是**流动性问题**（钱晚到），第四个是**本金问题**（钱没了）。

**必须分开计量**：晚到几天可以承受，本金归零不能。很多人把两者混为一谈，用同一个限额管，结果对第四种毫无防备。

## Concrete Example | 具体例子

**Khamenei 案的时间线就是一条结算风险的解剖图**（见 [[case-kalshi-khamenei-settlement]]）：

1. 事件状态不明 → 判定无法机械执行（**判定延迟**）
2. [[kalshi]] 冻结 **$54M**（**争议期冻结** —— 用户的钱既不能交易也不能提）
3. 语义含糊，最终协商赔付约 **$2.2M**
4. 补一条 "death settlement rule" 进 CFTC 备案

**注意第 2 步**：$54M 被冻结了一段时间。对持有那些头寸的人来说，这段时间的资金完全不可用 —— **而任何标准风控系统都没有为"我的钱可能被冻结几周"这件事留位置。**

## Common Misconceptions | 常见误解

- **误解一："结算风险 = 对手方违约。"** 不是。全额抵押消除了违约，但判定延迟、争议冻结、轨道故障、错误支付一个都没消除。
- **误解二："即时结算就没有结算风险。"** 即时结算消除了时差，但把"判定必须瞬间正确"变成了硬要求 —— **纠错窗口被压缩到零**。
- **误解三："链上结算最快最安全。"** 链上不可逆意味着一旦判错就没有任何补救。**速度与可纠错性在这里是对立的。**

## In Practice | 实战里怎么用

对每个头寸记录三个时间参数，它们决定你的真实资金可用性：

1. **判定日** —— 事件何时被判定？
2. **争议窗口长度** —— 判定后多久终局？期间资金锁不锁？
3. **支付时滞** —— 终局后多久到账？走什么轨道？

**再加一条纪律：把"争议期冻结"当成一种流动性事件来做压力测试。**
问自己："如果这个头寸的钱被冻 4 周，我的其他义务还能履行吗？"

**这个问题在传统衍生品尽调里不存在，在事件市场里它是必答题。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件市场的结算链条比价格衍生品多了哪两环？
  A: 判定事件是否发生，以及争议/申诉窗口。两环都需要时间，期间资金既不在手也未结清。
- Q: 结算链条的四个卡点里，哪三个是流动性问题、哪一个是本金问题？
  A: 判定延迟、争议期冻结、轨道故障是流动性问题（钱晚到）；错误支付是本金问题（钱没了，链上不可逆）。
- Q: 为什么'即时结算'并不能消除结算风险？
  A: 它消除了时差，但把纠错窗口压缩到零 —— 判定必须瞬间正确，否则无任何补救余地。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = settlement; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

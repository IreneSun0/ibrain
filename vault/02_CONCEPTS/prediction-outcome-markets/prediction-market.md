---
id: "concept:prediction-market"
type: concept
title: Prediction Market
title_zh: 预测市场
title_en: Prediction Market
aliases:
  - 预测市场
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - id: "concept:outcome-market"
    rel: special-case-of
    note: 以现实事件概率为对象的 outcome market
  - id: "venue:polymarket"
    rel: instantiated-by
  - id: "venue:kalshi"
    rel: instantiated-by
prerequisites:
  - "concept:price-discovery"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Prediction Market | 预测市场

## Executive Definition / Chinese Explanation | 定义与解释

**Prediction Market | 预测市场** = 用真金白银交易"某件事会不会发生"的市场。合约到期时按结果结算为 $1 或 $0，因此**当前价格可以直接读作市场认为的概率**。

它和赌博的界线不在形式上，而在功能上：预测市场的合法性论证是它**转移真实存在的事件风险**（像保险和期货那样），而不是凭空创造一个赌局。这条论证是它在美国被划归 CFTC 监管的基础。

## Why This Matters | 为什么重要

它同时是三样东西，理解时不能只抓一样：

- **一个信息聚合机制** — 把分散的判断压缩成一个可读的概率。
- **一个风险转移工具** — 让真正暴露在事件风险中的人（企业、机构）能对冲。
- **一门生意** — 而这门生意目前的收入结构，和前两个理想相距甚远。

**第三点是理解这个行业现状的关键。** Kalshi 2025 年 $263.5M 营收里体育占 **89%**；Polymarket 的品类分布里体育约 40%。**理想是事件风险对冲，现实的商业底盘是体育博彩流。** 这个落差是这个行业最重要的事实之一，也是绝大多数介绍文章不会告诉你的。

## How It Works | 机制怎么运转

一个预测市场合约的完整生命周期：

1. **上市** — 平台定义合约：问题文本、结算数据源、判定日、边界条件。**这一步的质量决定了后面所有风险。**
2. **交易** — 参与者按对概率的判断买卖，价格在 0–1 之间浮动。
3. **锁定** — 到期或事件发生，停止交易。
4. **裁决（resolution）** — 判定结果。中心化平台由内部团队判定（Kalshi 有 Rule 7.1 与 Outcome Review Committee），链上平台由预言机判定（Polymarket 离岸端用 [[uma]]，价格类自 2025-09 起走 [[chainlink]]）。
5. **争议窗口** — 有异议可申诉。
6. **结算** — 赢家每份拿 $1，输家归零。

**全部风险集中在第 1 步和第 4 步。** 撮合再快也救不了一份写得含糊的合约。

## Concrete Example | 具体例子

**同一个品牌，两套结算法学** —— [[polymarket]] 是最清楚的例子：

- **离岸主平台**：链下 CLOB 撮合 + Polygon 链上 USDC 全额抵押结算，裁决走 [[uma]] 的乐观预言机。
- **美国 QCX（DCM）**：2025-07 以 $112M 收购 QCEX 取得牌照，走 DCM 自认证合约，**不用 UMA**。

**结果是同一个事件在同一个品牌下，可能由两套完全不同的裁决机制决定结果。** 对用户来说，"我在 Polymarket 上交易"这句话已经不足以说明你的裁决风险是什么了 —— 你还得知道自己在哪一侧。

这也解释了为什么"结算方法学"需要独立建档分轨维护（见 [[settlement-methodology]]）。

## Common Misconceptions | 常见误解

- **误解一："预测市场比民调准。"** 在流动性充分时通常更准，因为有金钱激励纠错。但在薄盘口上，它只反映少数几个人的看法，未必优于民调。
- **误解二："价格就是概率。"** 只在全额抵押、低费用、流动性充分时近似成立。有手续费和资金占用时，价格是概率减去持有成本。
- **误解三："这是散户的信息民主。"** [[polymarket]] 的盈亏分布是 **0.1% 的账户拿走 67% 的利润，超过 70% 的用户亏钱**（单源数据）。它是一个零和市场，专业玩家的收益来自散户。
- **误解四："预测市场就是变相赌博。"** 法律上的区分标准是**是否存在真实的经济对冲需求**。这也是为什么美国多州与 [[kalshi]] 正在打"赌博 vs 联邦衍生品"的官司 —— 界线仍在法庭上划。

## In Practice | 实战里怎么用

评估任何一个预测市场平台，按这五个维度过一遍，顺序不能反：

| 维度 | 要问的问题 |
|---|---|
| **裁决** | 谁判定？规则公开吗？有申诉机制吗？历史争议查得到吗？ |
| **抵押** | 全额抵押还是保证金？钱锁在哪？ |
| **流动性** | 中位数合约的深度，不是头部合约 |
| **监管** | 哪个辖区？出事有没有法律救济？ |
| **费用** | 手续费 + 价差的真实合计 |

**"裁决"排第一不是随意排的。** 前面四项出问题你会亏钱，裁决出问题你会亏得莫名其妙且无处申诉。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 预测市场在法律上区别于赌博的核心论证是什么？
  A: 它转移真实存在的事件风险（像保险与期货），存在真实经济对冲需求，因此被划入商品衍生品监管而非博彩。
- Q: 预测市场理想的功能与当前的商业底盘之间有什么落差？
  A: 理想是事件风险对冲与信息聚合，现实收入主要来自体育博彩流 —— Kalshi 2025 年营收中体育占 89%。
- Q: 一份预测市场合约的全部风险集中在哪两步？为什么？
  A: 上市（合约条款定义）和裁决。撮合速度救不了含糊的条款，钱一旦按错误结果分出去基本追不回。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = price-discovery; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

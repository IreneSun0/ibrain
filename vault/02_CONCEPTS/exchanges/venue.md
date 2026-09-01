---
id: "concept:venue"
type: concept
title: Venue
title_zh: 交易场所
title_en: Venue
aliases:
  - 交易场所
status: reviewed
importance: tier-2
domains:
  - exchanges
  - financial-markets
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
related: []
prerequisites:
  - "concept:exchange"
import_origin: xlsx-learning-map+manual
import_category: 市场结构
---
# Venue | 交易场所

## Executive Definition / Chinese Explanation | 定义与解释

**Venue | 交易场馆** = 交易实际发生的地方。它比"交易所"更中性：**持牌交易所、离岸平台、链上协议都是 venue**，但法律地位天差地别。

用这个词的价值就在于它**不预设合规状态** —— 讨论市场结构时，你需要一个能同时装下三者的名词。

## Why This Matters | 为什么重要

在事件市场，"venue"这个词的中性正是它的用处：**同一个界面背后可能是三种完全不同的法律实体。**

| 类型 | 谁监管 | 出事找谁 |
|---|---|---|
| 持牌 DCM | CFTC 等 | 监管 + 平台申诉 |
| 离岸中心化平台 | 无 | **无** |
| 链上协议 | 无法律主体 | **无** |

**用户在这三种地方的保护天差地别，而界面看起来一模一样。**

**"venue-neutral"（场馆中立）这个说法也由此而来**：分析事件市场时，你需要能跨越这三类做统一比较，而不是只看其中一类。

## How It Works | 机制怎么运转

比较任何两个 venue，六个维度：

| 维度 | 要问的 |
|---|---|
| **法律地位** | 持牌？哪个辖区？ |
| **托管** | 钱在哪、谁能动（见 [[custody]]） |
| **撮合** | CLOB / AMM / 混合，在链上还是链下 |
| **裁决** | 谁判、能否申诉（见 [[resolution]]） |
| **流动性** | 中位数合约深度，不是总量 |
| **准入** | KYC、地理围栏、可交易品类 |

**六项里最容易被忽略的是第四项** —— 而它是唯一"错了就不可撤销"的一项。

## Concrete Example | 具体例子

三个 venue，同一个事件合约，风险画像完全不同：

| | 持牌 DCM | 离岸 hybrid | 纯链上 |
|---|---|---|---|
| 钱在哪 | 隔离账户 | 链上合约 | 链上合约 |
| 撮合可验证 | 否 | 否 | **是** |
| 裁决 | 内部团队 + 委员会 | 预言机 | 预言机 |
| 判错时赔付先例 | **有** | **无** | **无** |
| 机构可进 | **是** | 否 | 否 |

**倒数第二行是最实质的差别**：持牌场馆有过因语义含糊而实际赔付的先例；链上平台的先例是拒绝退款。

**"venue 选择"不是偏好问题，是风险画像的选择。**

## Common Misconceptions | 常见误解

- **误解一："venue 就是交易所。"** 交易所通常指持牌实体；venue 涵盖所有交易发生地，包括无牌与无主体的。
- **误解二："界面一样风险就一样。"** 法律地位、托管、裁决可能完全不同。
- **误解三："选流动性最好的 venue 就对了。"** 流动性只是六个维度之一，而裁决是唯一不可逆的那个。

## In Practice | 实战里怎么用

建立一张你自己的 venue 对照表，六列：

```
venue    法律地位   托管   撮合   裁决   流动性   准入
______   ________  _____  _____  _____  ______  ______
```

**填一次要不到半小时，但它会改变你对"这个市场"的整体判断** —— 因为你会发现所谓"预测市场"其实是三类结构完全不同的东西。

**并且：跨 venue 比较价格之前，先确认合约语义等价**（见 [[contract-equivalence]]），否则你比的不是同一件事。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么用 'venue' 而不是 'exchange'？
  A: venue 不预设合规状态，能同时装下持牌交易所、离岸平台与链上协议，而三者法律地位天差地别。
- Q: 比较 venue 的六个维度中，哪个最容易被忽略且最不可逆？
  A: 裁决 —— 它是唯一'错了就不可撤销'的一项，而多数人只看流动性。
- Q: 持牌场馆与链上平台在判错赔付上的先例差异是什么？
  A: 持牌场馆有过因语义含糊而实际赔付并修改规则备案的先例；链上平台的先例是定性为治理攻击但拒绝退款。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = exchange; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

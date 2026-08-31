---
id: "concept:event-contract"
type: concept
title: Event Contract
title_zh: 事件合约
title_en: Event Contract
aliases:
  - 事件合约
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
  - "source:2026-08-26-cftc-predictionmarkets"
related:
  - id: "concept:derivative"
    rel: special-case-of
    note: 支付取决于现实事件的衍生合约 (CFTC 语境按 DCM 事件合约归类)
  - id: "concept:binary-option"
    rel: see-also
    note: "支付结构经济等同, 法律分类不同 — 摊开 payoff 图即二元期权"
  - id: "venue:kalshi"
    rel: instantiated-by
    note: 美国联邦持牌事件合约交易所
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Event Contract | 事件合约

## Executive Definition / Chinese Explanation | 定义与解释

**Event Contract | 事件合约** = 结算取决于**某个现实世界事件是否发生**的衍生品合约，而不是取决于某个价格。

这是它与所有传统衍生品的根本区别，也是它全部特殊风险的来源：**价格是可以直接读出来的数字，"某事是否发生"是需要被解释的判断。**

## Why This Matters | 为什么重要

这个区别不是学术上的挑剔，它直接决定了风险在哪里。

- **传统衍生品**：结算价来自可观测的市场数据，争议极少，争议时也有清晰的裁定路径。
- **事件合约**：结算需要有人读合约文本、看指定数据源、然后**做出解释**。文本、数据源、解释者，**任何一环有歧义，钱就可能分错。**

所以事件合约的核心竞争力不在撮合速度，而在**合约文本的严密程度**。这是一件法律工作，不是工程工作。

## How It Works | 机制怎么运转

一份合格的事件合约文本必须钉死五件事，缺一件就是漏洞：

| 要素 | 必须回答 | 出错的后果 |
|---|---|---|
| **主体** | 到底是谁 / 什么 | 同名混淆 |
| **谓词** | 什么算"发生" | 语义争议 |
| **阈值** | 精确到什么数值 | 边界争议 |
| **时点** | 截至何时，按哪个时区 | 时点争议 |
| **数据源** | 以谁公布的为准，它失效怎么办 | 无源可依 |

[[kalshi]] 的做法是把 **Source Agencies（指定数据源）和判定日直接钉进合约条款**，判定由内部 markets team 做出，有异议可依 Rule 7.1 送 Outcome Review Committee，24 小时内出终局裁定。

**这套流程的存在本身就是产品**，不是行政开销。

## Concrete Example | 具体例子

**Khamenei 合约（2026-03）** 是这个领域最贵的一堂课（详见 [[case-kalshi-khamenei-settlement]]）：

合约问"哈梅内伊是否会在某日期前卸任伊朗最高领袖"。问题在于 —— **什么算"卸任"？** 死亡算吗？被架空算吗？由谁宣布才作数？在一个信息不透明的政权里，这些边界没有一个是自明的。

结果：[[kalshi]] 冻结了 **$54M**，最终因语义含糊赔付约 **$2.2M**，并把一条 **"death settlement rule"** 补进 CFTC 备案。

**代价是 $2.2M 现金加一次公开的信誉损失，换来一句话的条款补丁。** 这就是"合约语义"这件看起来枯燥的事的真实价格。

## Common Misconceptions | 常见误解

- **误解一："合约文本是法务的事，跟产品无关。"** 它就是产品。文本的严密程度直接等于用户承担的裁决风险。
- **误解二："用权威数据源就没问题了。"** 数据源会改口径、会停更、会在关键时刻不可用。**必须预先规定主数据源失效时怎么办**，否则就是裸奔。
- **误解三："模糊的合约可以事后靠委员会补救。"** 补救的代价是真金白银加信誉。Khamenei 案是 $2.2M。

## In Practice | 实战里怎么用

看一份事件合约，把它当成一段**要交给机器执行的代码**来读：

1. 把问题文本改写成一个 `if` 条件 —— 改写不出来，就说明它有歧义。
2. 找出所有**未定义的名词**（"卸任"、"正式宣布"、"实质控制"）。
3. 问：数据源停更 / 改口径 / 延迟发布时怎么办？
4. 查：这个平台**公开过自己判错的案例吗**？

**第 4 条最能看出诚意。** 敢公开争议历史的平台，通常裁决质量也更经得起看 —— 因为它知道自己会被检验。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件合约与传统衍生品的根本区别是什么？
  A: 结算取决于'某事是否发生'的判断而非可观测价格，因此需要解释，解释就可能有歧义。
- Q: 一份合格的事件合约文本必须钉死哪五件事？
  A: 主体、谓词（什么算发生）、阈值、时点（含时区）、数据源（含失效时的备用方案）。
- Q: Khamenei 案的代价和教训是什么？
  A: 冻结 $54M、赔付约 $2.2M、补入 death settlement rule。教训是合约语义的模糊会直接变成现金损失和信誉损失。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-cftc-predictionmarkets]] — <https://www.cftc.gov/LearnAndProtect/PredictionMarkets>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = derivative; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

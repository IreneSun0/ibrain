---
id: "concept:underlying"
type: concept
title: Underlying
title_zh: 标的/底层变量
title_en: Underlying
aliases:
  - 标的
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
related: []
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Underlying | 标的/底层变量

## Executive Definition / Chinese Explanation | 定义与解释

**Underlying | 标的 / 底层变量** = 衍生品的价值所指向的那个东西。

问"标的是什么"等于问"**我到底暴露于什么**"。这是所有衍生品分析的第一问，也是最容易被答错的一问 —— 因为很多人把合约的**标题**当成了标的。

## Why This Matters | 为什么重要

事件合约的标的不是"某件事"，而是**"合约文本所定义的那个命题"**。

这两者之间的任何缝隙，都是别人的套利空间和你的意外亏损。

举例：你以为自己押的是"这位官员会不会下台"（现实事件），实际押的是"**在 T 之前，由指定数据源确认的、符合合约对'下台'定义的情形是否成立**"（命题）。**现实和命题不一致时，赔付按命题走。**

## How It Works | 机制怎么运转

事件合约的标的由五要素共同定义（见 [[contract-semantics]]）：

| 要素 | 缺失时的后果 |
|---|---|
| 主体 | 同名混淆 |
| 谓词 | "下台/卸任/离任"边界之争 |
| 阈值 | 边界值算不算 |
| 时点 | 时区与截止瞬间之争 |
| 数据源 | 无源可依 |

**五要素合起来才是标的。** 少任何一个，你就无法准确说出自己暴露于什么 —— 而无法说清的敞口，无法被管理。

**实用技巧：把合约标题和五要素并排写下来，看它们是不是同一件事。** 十次里有三四次不是。

## Concrete Example | 具体例子

三张"标题几乎相同"的合约，标的其实不同：

| 合约标题 | 真实标的 |
|---|---|
| "美联储 12 月降息" | FOMC 12 月会议声明中宣布下调目标区间 |
| "美联储 12 月降息" | 12 月 31 日的有效联邦基金利率低于 11 月 |
| "美联储 12 月降息" | 任何 FOMC 官方渠道在 12 月内宣布的降息 |

**三个标的在大多数情形下一致，在少数情形下分叉** —— 而分叉恰恰发生在最值钱的时刻（政策意外、非常规工具、月末操作）。

**这就是为什么"读标题就下单"在事件市场比在价格市场危险得多。** 价格市场的"BTC 价格"没有歧义空间。

## Common Misconceptions | 常见误解

- **误解一："标题就是标的。"** 标题是营销文案，条款才是标的。
- **误解二："同题合约标的相同。"** 见上例。三张同题合约可以有三个不同标的。
- **误解三："标的模糊只影响极端情况。"** 对 —— **而极端情况正是你买这份合约的原因。**

## In Practice | 实战里怎么用

对每一份要交易的合约，写下一句"我暴露于什么"，必须包含五要素：

> "我暴露于：**[主体]** 在 **[时点，含时区]** 之前，按 **[数据源]** 公布的口径，**[谓词]** 达到 **[阈值]** 的情形是否成立。"

**写不出来这句话，就说明条款有洞，不该下单。**

写出来之后再做一件事：**列出三种你能想到的"现实发生了但命题不成立"（或反之）的情形。** 一个都想不出来说明条款写得好；想出三个说明这份合约的语义风险很高。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件合约的标的到底是什么？
  A: 不是'某件事'，而是合约文本所定义的那个命题。现实与命题不一致时，赔付按命题走。
- Q: 为什么三张标题相同的合约可能有三个不同的标的？
  A: 标的由主体、谓词、阈值、时点、数据源五要素共同定义；标题相同而这五项不同，就是不同的标的。
- Q: 下单前该写下的那句话包含哪五个要素？
  A: 主体、时点（含时区）、数据源、谓词、阈值 —— 写不出来说明条款有洞。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = derivative; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

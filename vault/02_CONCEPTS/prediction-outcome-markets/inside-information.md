---
id: "concept:inside-information"
type: concept
title: Inside Information
title_zh: 内幕/重大非公开信息
title_en: Inside Information
aliases:
  - 内幕
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
  - regulation-compliance
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
  - "source:2026-08-26-cftc-9237-26"
related:
  - id: "concept:adverse-selection"
    rel: see-also
    note: 事件市场的知情流 = 微观结构逆向选择在语义层的镜像
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 预测市场监管
---
# Inside Information | 内幕/重大非公开信息

## Executive Definition / Chinese Explanation | 定义与解释

**Inside Information | 内幕信息** = 尚未公开、且会显著改变某事件概率的信息。

事件市场的特殊之处在于：**它的标的是现实世界的事情，而现实世界里总有人先知道。** 竞选团队知道内部民调，公司高管知道并购进展，监管机构的人知道下周宣布什么，赛事方知道伤病名单。

## Why This Matters | 为什么重要

这是事件市场最结构性的难题，原因不在道德而在**法律覆盖**：

- 证券市场的内幕交易法保护的是**证券**。事件合约在很多辖区不是证券。
- 商品期货有反操纵条款，但"知道自己公司的事"通常不构成期货法下的内幕交易。
- 很多事件（体育、娱乐、政治内部动态）**根本不在任何金融监管的覆盖范围内**。

**结果：事件市场里存在大量"合法的内幕交易"。** 它对做市商的影响是直接的 —— 逆向选择成本高到无法承担时，做市商就撤了（见 [[adverse-selection]]），盘口随之变空。

## How It Works | 机制怎么运转

事件市场的内幕信息有三个来源层，越往下越难监管：

1. **事件本身的参与者** —— 候选人团队、公司内部、赛事相关方。**信息最准，最难识别。**
2. **裁决链条上的人** —— 知道数据源何时发布、知道判定倾向的人。**这一层是事件市场独有的**：传统市场的结算价没有"内部人"。
3. **平台内部** —— 能看到订单流、能看到用户持仓的人。

**第 2 层值得特别注意**：在事件市场，"结果会被判成什么"本身就是可以有内幕的 —— 这在价格类衍生品里不存在，因为结算价是公开可观测的。

实际执法已经出现：[[kalshi]] 的内幕自查执法串包括 MrBeast 剪辑师、国会候选人、George Santos（$35k 罚款 + 3 年禁令）、白宫提词员等案例。

## Concrete Example | 具体例子

**做市商视角的一天**，说明这件事的成本有多具体：

做市商在某"公司高管人事变动"合约上报 0.20/0.24。

- 上午：被连续按 0.24 买走 40,000 份，方向单一，无对应新闻。
- 做市商的判断：**这是知情流还是噪音？** 若是知情流，它每份要亏 0.76。
- 正确反应：立刻拉宽价差到 0.18/0.30 或直接撤单。
- 下午：官宣，价格跳到 0.95。**做市商已撤，避免了 $30k 损失。**
- 代价：**这个市场从上午起就没有报价了。**

**内幕信息的最终成本不是由内幕交易者的对手方承担，而是由所有普通用户承担** —— 形式是更宽的价差、更薄的深度、和消失的盘口。

## Common Misconceptions | 常见误解

- **误解一："内幕交易在预测市场是违法的。"** 取决于辖区和事件类型。持牌平台有规则手册和执法能力；离岸平台和许多事件类型基本处于真空。
- **误解二："这只是道德问题。"** 它是**流动性问题**。信息不对称高的市场，做市商不来，普通用户交易成本更高。
- **误解三："提高手续费能补偿。"** 手续费对所有人一视同仁，只会赶走无信息的流动性，**让剩下的人里知情人比例更高** —— 反而恶化。

## In Practice | 实战里怎么用

判断一个事件市场的内幕风险，问三个问题：

1. **谁有可能先知道？** 事件的决定权在多少人手里？人越少、越集中，风险越高。
2. **这个辖区管得着吗？** 持牌平台有市场监察义务，离岸平台通常没有。
3. **裁决链条上有多少人？** 这是事件市场特有的一层。

**风险分级速查**：

| 事件类型 | 内幕风险 | 可做市性 |
|---|---|---|
| 公开数据发布（CPI、失业率） | 低 | 好 |
| 选举结果 | 中 | 中 |
| 公司决策、人事任免 | **高** | 差 |
| 小圈子内部事件 | **极高** | 基本不可做市 |

**看到高风险象限的合约有异常紧的价差，先怀疑是补贴，不是效率。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么事件市场存在大量'合法的内幕交易'？
  A: 内幕交易法主要覆盖证券；事件合约在许多辖区不是证券，且大量事件类型不在任何金融监管覆盖范围内。
- Q: 事件市场特有的第二层内幕来源是什么？为什么价格类衍生品没有？
  A: 裁决链条上的人 —— 知道数据源发布时点或判定倾向的人。价格类衍生品的结算价是公开可观测的，没有'内部人'。
- Q: 内幕信息的成本最终由谁承担？
  A: 所有普通用户 —— 做市商拉宽价差、减少挂单或撤出，表现为更高的交易成本和更薄的深度。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-cftc-9237-26]] — <https://www.cftc.gov/PressRoom/PressReleases/9237-26>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场监管)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

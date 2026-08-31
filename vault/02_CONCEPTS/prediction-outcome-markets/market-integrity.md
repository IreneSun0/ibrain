---
id: "concept:market-integrity"
type: concept
title: Market Integrity
title_zh: 市场完整性/公平有序交易
title_en: Market Integrity
aliases:
  - 市场完整性
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
  - "source:2026-08-26-cftc-2026-05105-html"
related:
  - id: "concept:inside-information"
    rel: see-also
    note: 事件市场 integrity 的头号威胁 — 定义事件的人可以交易它
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 预测市场监管
---
# Market Integrity | 市场完整性/公平有序交易

## Executive Definition / Chinese Explanation | 定义与解释

**Market Integrity | 市场诚信** = 市场没有被操纵、内幕滥用或欺诈污染的状态，以及维持这个状态的整套规则、监测和执法能力。

事件市场的特殊之处：**它有三个可被操纵的对象，而不是一个。**

## Why This Matters | 为什么重要

价格市场只能被操纵价格。事件市场可以被操纵三处：

1. **价格** —— 拉抬打压，和传统市场一样。
2. **事件本身** —— **让那件事真的发生或不发生。** 这在价格市场里几乎不可能，在事件市场里对某些事件是可行的（小范围的、参与者可影响的事件）。
3. **裁决** —— 影响判定结果，无需影响价格或事件（见 [[oracle-risk]]）。

**第 2 和第 3 条是这个赛道独有的攻击面**，而现有的市场监察框架完全没有为它们设计。

## How It Works | 机制怎么运转

诚信防线分三层，事件市场每一层都有缺口：

| 层 | 内容 | 事件市场的缺口 |
|---|---|---|
| **规则层** | 定义什么被禁止（操纵 / 自成交 / 内幕滥用） | 许多事件类型不在任何金融法规覆盖内 |
| **监测层** | 识别异常模式 | **需要跨市场、跨链、事件维度的数据 —— 无人拥有** |
| **执行层** | 处罚与追偿 | 需要监管权力或平台意愿 |

**监测层的缺口最结构性**：
- 场馆**不能**既当赌场又当警察（利益冲突：它靠成交量赚钱）。
- 监管机构**看不到**链上与跨境的全貌。

**结果：事件维度的跨市场监测层空着**，而这恰恰是唯一能同时看到三个攻击面的位置。

## Concrete Example | 具体例子

三种操纵的真实形态：

| 类型 | 案例 | 特征 |
|---|---|---|
| **价格操纵** | 薄盘口上用小资金推动价格，制造误导性"概率信号" | 成本低（长尾合约深度极薄） |
| **事件操纵** | 对参与者可影响的小范围事件下注并施加影响 | 难以举证 |
| **裁决操纵** | Ukraine 矿产协议案：单一行为人用 3 个账户投 5M UMA（约 25% 投票权），把未发生的事裁成 Yes | **已实证发生** |

执法确实在发生：[[kalshi]] 的内幕自查执法串包括 MrBeast 剪辑师、国会候选人、George Santos（$35k + 3 年禁令）、白宫提词员。

**但注意：这些都是中心化持牌平台的自查。链上平台没有对应的执法能力。**

## Common Misconceptions | 常见误解

- **误解一："去中心化能解决操纵问题。"** 去中心化改变了操纵的形式（从内幕变成治理攻击），没有消除它。
- **误解二："成交量大的市场不容易被操纵。"** 头部合约确实难，但**长尾合约的操纵成本极低** —— 而"概率信号"恰恰常常从长尾合约被引用。
- **误解三："这是监管的事，跟我无关。"** 你引用的每一个"市场概率"，其可信度都取决于那个盘口有没有被污染。

## In Practice | 实战里怎么用

在引用任何一个事件市场价格之前，做一次污染度检查：

1. **深度是否足以抵抗操纵？** ±1% 深度低于 $10k 的盘口，几千美元就能推动"概率"。
2. **持仓集中度？** 前几个地址占多少（链上可查）。
3. **成交是否异常？** 单笔均值远高于同业 + 有积分激励结构 ⟹ 怀疑刷量。
4. **裁决机制的投票权集中度？** 见 [[oracle-risk]] 的攻击成本计算。

**四项里任意一项异常，这个价格就不该被当作"市场共识"引用。** 媒体引用预测市场价格时几乎从不做这四项检查。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件市场可被操纵的三个对象是什么？
  A: 价格、事件本身（让事情真的发生或不发生）、裁决。后两个是这个赛道独有的攻击面。
- Q: 为什么监测层的缺口最结构性？
  A: 场馆有利益冲突（靠成交量赚钱）不能自我监管，监管机构看不到链上与跨境全貌，跨市场事件维度的监测层空着。
- Q: 引用一个事件市场价格前该做哪四项污染度检查？
  A: 深度是否足以抵抗操纵、持仓集中度、成交是否异常（刷量）、裁决机制的投票权集中度。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-cftc-2026-05105-html]] — <https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场监管)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

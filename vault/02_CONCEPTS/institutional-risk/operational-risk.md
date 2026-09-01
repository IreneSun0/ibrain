---
id: "concept:operational-risk"
type: concept
title: Operational Risk
title_zh: 运营/系统风险
title_en: Operational Risk
aliases:
  - 运营
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
related: []
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Operational Risk | 运营/系统风险

## Executive Definition / Chinese Explanation | 定义与解释

**Operational Risk | 操作风险** = 因为流程、人、系统或外部事件出错而造成的损失 —— 不是市场亏的，是"运作"亏的。

它是巴塞尔框架里与市场风险、信用风险并列的第三大类，也是最容易被交易者忽略的一类。

## Why This Matters | 为什么重要

在加密和事件市场，操作风险的占比远高于传统金融，原因很具体：

- **托管环节自持** —— 私钥管理出错等于本金归零（见 [[custody]]）。
- **基础设施年轻** —— 智能合约 bug、预言机故障、链拥堵。
- **流程不成熟** —— 很多平台的运营流程没有经过压力检验。

**历史上加密行业最大的几次损失都不是市场风险造成的**：交易所被盗、私钥丢失、合约漏洞 —— 全是操作风险。

## How It Works | 机制怎么运转

操作风险的四个来源，对应四类防线：

| 来源 | 例子 | 防线 |
|---|---|---|
| **人** | 误操作、内部作恶 | 双人复核、权限分离 |
| **流程** | 对账缺失、无灾备 | 标准化、演练 |
| **系统** | 合约 bug、宕机 | 审计、冗余、限额 |
| **外部** | 被盗、监管突袭、供应商故障 | 保险、多供应商、法律准备 |

**事件市场特有的一类**：**裁决流程本身是操作风险的载体** —— 判定团队的流程、争议处理的时限、数据源的接入可靠性（见 [[settlement-methodology]]）。这在传统操作风险框架里没有对应格子。

## Concrete Example | 具体例子

2025-02 的一次交易所被盗事件，是操作风险应对的正反两面教材：

- **风险实现**：约 $1.5B 被盗，归因于一个国家级黑客组织。**纯操作风险，与市场无关。**
- **应对**：72 小时内经多家做市商与机构补足储备，未破产。
- **教训正面**：储备透明 + 快速融资渠道 = 操作风险可被吸收。
- **教训反面**：**如果没有那几家愿意在 72 小时内出手的对手方，结果完全不同。**

**这个案例说明操作风险的关键不在"会不会发生"，而在"发生后你有没有备用方案"。**

## Common Misconceptions | 常见误解

- **误解一："操作风险是小概率所以可以忽略。"** 加密行业的历史损失里它占大头。
- **误解二："买保险就解决了。"** 保险覆盖有限、除外条款多，且赔付需要时间 —— 而流动性危机不等人。
- **误解三："操作风险是运营团队的事。"** 它直接决定你的本金安全。**做尽调时它应该和市场风险并列，而不是附注。**

## In Practice | 实战里怎么用

对任何平台做操作风险尽调，问四件事：

1. **钱在哪、谁能动？** 私钥管理、多签阈值、是否有独立托管（见 [[custody-segregation]]）。
2. **有没有第三方审计？** 谁审的、什么时候、覆盖哪个版本。
3. **出过事吗？怎么处理的？** **公开过事故复盘的平台，通常比没出过事的更可信。**
4. **裁决流程是否有明文与时限？** 这是事件市场特有的一环。

**第 3 条是最快的筛子**：肯公开自己出过什么问题、怎么解决的，说明它经得起被检验。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 操作风险的四个来源是什么？
  A: 人（误操作、内部作恶）、流程（对账缺失、无灾备）、系统（合约 bug、宕机）、外部（被盗、监管、供应商）。
- Q: 为什么加密行业的操作风险占比远高于传统金融？
  A: 托管环节自持（私钥出错即本金归零）、基础设施年轻（合约 bug、预言机故障）、运营流程未经压力检验。
- Q: 事件市场特有的一类操作风险是什么？
  A: 裁决流程本身：判定团队的流程、争议处理时限、数据源接入可靠性 —— 传统操作风险框架里没有对应格子。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

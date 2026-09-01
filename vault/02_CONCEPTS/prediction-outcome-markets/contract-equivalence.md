---
id: "concept:contract-equivalence"
type: concept
title: Contract Equivalence
title_zh: 合约等价性
title_en: Contract Equivalence
aliases:
  - 合约等价性
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
  - id: "concept:basis-risk"
    rel: see-also
    note: 等价性判定失败 = 跨 venue 对冲的 basis risk 来源 (Kalshi vs Polymarket 同题合约)
  - id: "org:dome"
    rel: instantiated-by
    note: 跨平台市场匹配 API (get-matching-markets)
prerequisites:
  - "concept:contract-semantics"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Contract Equivalence | 合约等价性

## Executive Definition / Chinese Explanation | 定义与解释

**Contract Equivalence | 合约等价性** = 判断两个不同场所的合约，是不是**真的在赌同一件事**。

看起来是个学术问题，实际上是决定"能不能对冲、能不能套利、能不能聚合流动性"的基础设施问题。**两份问题文本读起来一样的合约，可能因为判定日差一天而完全不等价。**

## Why This Matters | 为什么重要

它卡住了这个行业三件最想做的事：

- **做市商对冲** — 在 A 平台接的货想去 B 平台对冲，前提是两边真的等价。不等价的对冲是**伪对冲**，风险没转移走，只是换了个形式。
- **跨场所套利** — 价差看起来存在，可能只是语义差异的映射。照着做会两边都输。
- **流动性聚合** — 想把碎片化的流动性合成一个深盘口，前提是能证明这些盘口可互换。

**事件市场的流动性被切碎是它的头号结构问题，而等价性判定是解决它的前置条件。**

## How It Works | 机制怎么运转

两份合约等价，必须**五个维度全部对齐**，缺一不可：

| 维度 | 不对齐的后果 |
|---|---|
| **事件主体** | 押的根本不是同一件事 |
| **谓词与阈值** | "超过 3%" vs "达到或超过 3%"，边界情形结果相反 |
| **判定时点** | 差一天就可能一边 YES 一边 NO |
| **裁决数据源** | 两个源可能给出不同数字 |
| **边界条件处理** | 死亡/取消/延期时一边赔付一边作废 |

**只有五项全部一致才是真等价；四项一致 = 高度相关但有基差。** 把"高度相关"当成"等价"来对冲，就是在积累一个你没意识到的风险敞口。

## Concrete Example | 具体例子

一个具体的伪等价陷阱：

- **A 平台**："美联储在 12 月会议上降息" —— 判定源为 FOMC 声明，判定日为会议当日。
- **B 平台**："美联储在 12 月降息" —— 判定源为有效联邦基金利率，判定日为 12 月 31 日。

**看起来是同一件事，实际不是。** 若美联储在 12 月会议不动、但月底通过其他工具压低了有效利率，A 判 NO 而 B 判 YES。

**一个做市商如果按"等价"在两边建了反向头寸，他以为自己中性，实际上持有一个纯粹的基差敞口** —— 而且他不知道自己持有。这比明知有风险更危险。

## Common Misconceptions | 常见误解

- **误解一："问题文本一样就是等价。"** 文本只是五个维度里的一个半。判定日和数据源不写在标题里。
- **误解二："等价性可以靠 AI 语义匹配解决。"** 语义相似度能做初筛，但**边界条件的等价必须逐条比对**，这是确定性判断，不是相似度判断。
- **误解三："差一点没关系，大致对冲就行。"** 差异恰恰在极端情形下才显现 —— 而那正是你需要对冲生效的时候。

## In Practice | 实战里怎么用

建立跨场所头寸前，跑一张五行对照表：

```
              A 平台            B 平台           一致?
主体          _______           _______          □
谓词/阈值     _______           _______          □
判定时点      _______           _______          □
数据源        _______           _______          □
边界条件      _______           _______          □
```

- **五项全 ✓** → 可视作等价，可对冲、可套利。
- **有一项 ✗** → 记为**基差头寸**，单独计量，不要计入对冲抵扣。

**这张表应该是自动化的，不是人工的。** 它是确定性判断（字段比对），正是应该交给代码而不是交给判断的那类工作。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 两份事件合约等价必须对齐哪五个维度？
  A: 事件主体、谓词与阈值、判定时点、裁决数据源、边界条件处理。
- Q: 为什么'高度相关'不能当'等价'用？
  A: 差异恰在极端情形下显现，而那正是需要对冲生效的时刻；把它当等价会持有一个未被识别的基差敞口。
- Q: 为什么等价性判定应该交给代码而非人工判断？
  A: 它是字段逐条比对的确定性工作，不是相似度判断；人工比对不可扩展且容易漏掉边界条件。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = contract-semantics; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

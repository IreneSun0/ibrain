---
id: "concept:margin"
type: concept
title: Margin
title_zh: 保证金
title_en: Margin
aliases:
  - 保证金
status: reviewed
importance: tier-1
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
  - id: "concept:collateral"
    rel: special-case-of
    note: 制度化、按风险动态计算的抵押品
  - id: "concept:clearing"
    rel: mechanism-of
    note: 清算体系用保证金吸收价格波动、压低违约概率
prerequisites:
  - "concept:leverage"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Margin | 保证金

## Executive Definition / Chinese Explanation | 定义与解释

**Margin | 保证金** = 你只交一部分钱就能持有更大名义规模的头寸，交易所或经纪商用这笔钱吸收你的潜在亏损。

它是**资本效率**的来源，也是**爆仓**的来源 —— 同一个机制的两面。

## Why This Matters | 为什么重要

理解保证金，才能理解事件市场当前最重要的取舍：

| | 保证金 | 全额抵押 |
|---|---|---|
| 资金效率 | **高**（押 5-15%） | 低（押 100%） |
| 爆仓风险 | **有**（追保、强平、连环） | 无 |
| 违约风险 | 有（靠 CCP 吸收） | 无 |
| 机构可用性 | **高** | 低（资金成本算不过账） |

**事件市场目前几乎全在右列。** 这就是为什么 CFTC 在探索事件合约的保证金化 —— 不解决资金效率，机构资金进不来。**但这里有一个真实的数学难题。**

## How It Works | 机制怎么运转

保证金有两层：**初始保证金（IM）** 开仓时交，覆盖正常波动；**维持保证金（MM）** 跌破就追保，不补则强平。

计算 IM 的核心是"覆盖最坏波动"，通常用历史波动率或情景模拟估一个置信区间。

**而这正是事件合约的难点**：事件价格**不扩散、直接跳**。一个 0.30 的合约在判定日会瞬间变成 1.00 或 0.00 —— **"覆盖最坏波动"就意味着保证金必须等于全部名义价值**，那就退回全额抵押了。

**传统保证金模型的数学地基在这里裂开。** 这不是监管保守，是模型确实不适用。

## Concrete Example | 具体例子

一个 0.30 的二元合约，1000 份（名义 $1000，最大赔付 $1000）：

| 方法 | 保证金 | 问题 |
|---|---|---|
| 按历史波动率（日波动 2%） | ~$60 | **判定日一跳就穿仓 $700** |
| 按最坏情况 | $1000 | **等于全额抵押** |
| 按"跳变概率加权" | ? | **那个概率就是价格本身 —— 循环** |

**第三行是问题核心**：要给跳跃定保证金，你需要知道跳跃概率；而跳跃概率恰恰就是市场正在发现的那个价格。**用价格去定保证金，价格波动时保证金也波动，形成反馈。**

**这是一个真实的未解工程问题。**

## Common Misconceptions | 常见误解

- **误解一："保证金越低越好。"** 低保证金 = 高杠杆 = 高爆仓概率，对二元跳变标的尤其危险。
- **误解二："事件合约不做保证金是监管保守。"** 主要是**模型不适用**，不是态度问题。
- **误解三："全额抵押永远更安全。"** 对违约风险是；但资金效率低会把机构挡在门外，**而没有机构参与的市场流动性更差、价格更不可靠。**

## In Practice | 实战里怎么用

看到任何"事件合约保证金化"的方案，问三个问题：

1. **它怎么处理跳变？** 用什么替代历史波动率？
2. **穿仓由谁承担？** 有违约瀑布吗？谁出第一层？
3. **保证金会不会顺周期？** 波动时上调保证金，会不会触发连环强平？

**第 3 问是 2008 年的教训** —— 顺周期保证金在压力时刻放大危机，**在二元跳变标的上这个效应会更剧烈。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 保证金机制的两面性是什么？
  A: 资本效率的来源，同时也是爆仓的来源 —— 同一个机制。
- Q: 为什么传统保证金模型在事件合约上失效？
  A: 事件价格不扩散、直接跳变，'覆盖最坏波动'意味着保证金必须等于全部名义价值；而按跳变概率定保证金会陷入'概率即价格'的循环。
- Q: 评估事件合约保证金方案该问哪三个问题？
  A: 怎么处理跳变、穿仓由谁承担（有无违约瀑布）、保证金会不会顺周期放大压力。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cftc-2026-05105-html]] — <https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = leverage; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

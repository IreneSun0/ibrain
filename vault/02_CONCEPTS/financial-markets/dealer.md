---
id: "concept:dealer"
type: concept
title: Dealer
title_zh: 交易商/自营商
title_en: Dealer
aliases:
  - 交易商
status: reviewed
importance: tier-2
domains:
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
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 市场结构
---
# Dealer | 交易商/自营商

## Executive Definition / Chinese Explanation | 定义与解释

**Dealer | 交易商 / 自营商** = 用**自己的资产负债表**做你的对手方的机构：你要买，它卖给你；你要卖，它买下来。

它赚的是价差，承担的是[[inventory-risk|存货风险]]。做市商是交易商在有持续报价义务时的名字。

## Why This Matters | 为什么重要

交易商模式回答了一个基本问题：**当买卖双方不在同一时刻出现时，谁来填这个时间差？**

在事件市场，这个问题被放大到极致：**几万个长尾合约，绝大多数没有自然的双向需求。** 没有交易商用自有资本填时间差，这些盘口就是空的（见 [[market-maker-incentive]]）。

**所以交易商不是这个市场的可选角色，是它能否存在的前提。**

## How It Works | 机制怎么运转

交易商的经济学是三项相减（见 [[maker]]）：

```
收益 = 价差 + 平台激励
成本 = 存货风险 + 逆向选择
```

**它管理风险的三种手段**，在事件市场依次失效：
1. **跨场所对冲** —— 需要合约语义等价（见 [[contract-equivalence]]）—— **常常不成立**。
2. **跨品种对冲** —— 需要相关工具 —— **长尾事件没有**。
3. **报价倾斜** —— 唯一永远可用的，但见效慢。

**只剩第 3 种时，报价必然又宽又浅。** 这不是交易商不努力，是工具箱空了。

## Concrete Example | 具体例子

交易商在两种市场的可行性对照：

| | 主流加密现货 | 长尾事件合约 |
|---|---|---|
| 对冲工具 | 期货、永续、其他所 | **通常没有** |
| 逆向选择 | 中 | **高**（见 [[inside-information]]） |
| 存货持有期 | 分钟 | **数月到判定日** |
| 结果 | 价差 1-5 bp | **价差 5-10 分** |

**"数月的存货持有期"是事件市场特有的**：你接的货要扛到判定日，中间无法对冲、无法脱手。

**这解释了为什么长尾事件合约的价差看起来"离谱"** —— 它反映的是一个真实且无法转移的风险。

## Common Misconceptions | 常见误解

- **误解一："交易商在操纵价格。"** 它的常态是被动接单并尽快回到中性；方向性观点不是它的收入来源。
- **误解二："价差宽是平台在坑人。"** 价差是交易商为承担存货和逆向选择定的价。压窄只会让它撤走。
- **误解三："交易商和经纪商差不多。"** 交易商是你的对手方，经纪商是你的代理。**利益关系完全相反。**

## In Practice | 实战里怎么用

判断一个事件合约"能不能被专业交易商做"，问一条：

> **这个头寸能在哪里对冲掉？**

- 有同事件的其他场所 → **先检查语义是否真的等价**，差一点就是伪对冲。
- 只有相关品种 → 估算基差风险。
- 什么都没有 → 只能靠报价倾斜，**必然浅而宽**，别期待机构级深度。

**对平台的推论**：想吸引专业交易商，第一件事不是提高返佣，而是**让合约语义可跨场所对齐** —— 那才是打开对冲工具箱的钥匙。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 交易商在事件市场为什么是前提而非可选角色？
  A: 几万个长尾合约没有自然的双向需求，没有交易商用自有资本填补时间差，这些盘口就是空的。
- Q: 交易商管理存货的三种手段在事件市场为什么依次失效？
  A: 跨场所对冲需要语义等价（常不成立）、跨品种对冲需要相关工具（长尾没有），只剩报价倾斜，因此报价必然浅而宽。
- Q: 平台想吸引专业交易商，第一件该做的事是什么？
  A: 让合约语义可跨场所对齐，打开对冲工具箱 —— 而不是提高返佣。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

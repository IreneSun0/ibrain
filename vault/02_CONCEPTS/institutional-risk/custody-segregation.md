---
id: "concept:custody-segregation"
type: concept
title: Custody Segregation
title_zh: 客户资产隔离托管
title_en: Custody Segregation
aliases:
  - 客户资产隔离托管
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
related:
  - id: "concept:custody"
    rel: component-of
    note: 客户资产与公司资产的账务与保管隔离
prerequisites:
  - "concept:custody"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Custody Segregation | 客户资产隔离托管

## Executive Definition / Chinese Explanation | 定义与解释

**Custody Segregation | 客户资产隔离** = 客户的钱和平台自己的钱在法律上和操作上分开，使平台破产时客户资产不进入破产财产。

**隔离是法律状态，不只是记账习惯。** 分两个账户记但法律上仍属同一财产池，破产时依然会被清算。

## Why This Matters | 为什么重要

它是"平台倒了我的钱还在不在"这个问题的**唯一制度性答案**。

历史上几乎每一次大型交易平台事故，核心都是隔离失效：客户资金被用于平台自营、被用于填补亏损、或者根本从未真正分开。

**对事件市场，隔离有两条路径**：
- **法律路径** —— 持牌平台的法定隔离要求（如 [[kalshi]] 在 CFTC 框架下）。
- **技术路径** —— 资金锁在链上合约里，平台无私钥（如 [[polymarket]] 的全额抵押）。

**两条路径都能达到目的，验证方式完全不同**：一条靠审计与法律，一条靠区块浏览器。

## How It Works | 机制怎么运转

真正的隔离需要四件事同时成立：

1. **法律隔离** —— 客户资产在法律上不属于平台财产。
2. **操作隔离** —— 独立账户、独立签名权限，不共用资金池。
3. **账目隔离** —— 每个客户的份额可被逐一识别（不是只有总额）。
4. **可验证** —— 有独立审计或链上可查。

**第 3 条最容易被忽略**：如果只有"客户资金总额"而无法逐户拆分，破产清算时的分配会极其混乱，且可能出现"总额不足"却无人能证明谁少了多少。

**第 4 条是隔离与"声称隔离"的分界线。**

## Concrete Example | 具体例子

同一笔 $100k 在三种安排下，平台破产时的结局：

| 安排 | 破产时 | 你拿回 |
|---|---|---|
| 平台热钱包，与运营资金混同 | 进破产财产 | 按债权比例，通常远少于全额，且要等数年 |
| 持牌平台法定隔离账户 | **不进破产财产** | 全额（若隔离确实执行） |
| 链上合约全额抵押 | **平台破产与合约无关** | 全额（合约照常按结果结算） |

**第三行有一个特别之处**：即使平台整个团队消失，链上合约仍会按预言机结果执行结算。**这是密码学隔离相对法律隔离的独特优势** —— 它不需要任何机构继续存在。

代价是：如果预言机也停止运作，资金可能永久锁死。**没有免费的午餐。**

## Common Misconceptions | 常见误解

- **误解一："分开记账就是隔离。"** 记账分开而法律不分开，破产时照样被清算。
- **误解二："隔离保证我不亏钱。"** 它保证的是**平台倒闭时你的本金还在**，不保证你的交易不亏，也不保证裁决正确。
- **误解三："链上就自动隔离了。"** 只有在平台无法单方转出资金时才成立。带管理员密钥的合约不算。

## In Practice | 实战里怎么用

验证隔离状态，按路径分别做：

**链下（持牌平台）**
- 有没有独立托管行？账户是以谁的名义开立的？
- 有没有第三方审计报告？多久一次？
- 破产时客户资产的法律地位有明文吗？

**链上**
- 资金合约地址是什么？（要能查到）
- 有没有升级权限 / 管理员密钥？多签阈值？
- 合约代码审计过吗？谁审的？

**两条路径都要问的一条**：**能不能逐户拆分？** 只有总额没有明细，隔离在清算时会失效。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 真正的隔离需要哪四件事同时成立？
  A: 法律隔离、操作隔离（独立账户与签名权限）、账目隔离（可逐户拆分）、可验证（独立审计或链上可查）。
- Q: 密码学隔离相对法律隔离的独特优势和代价各是什么？
  A: 优势：即使平台团队消失，合约仍按预言机结果结算，不需要任何机构继续存在。代价：若预言机停止运作，资金可能永久锁死。
- Q: 为什么'只有客户资金总额'的隔离在清算时会失效？
  A: 无法逐户拆分份额，分配会极其混乱，且总额不足时无人能证明谁少了多少。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = custody; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

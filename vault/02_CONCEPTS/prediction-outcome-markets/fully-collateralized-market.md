---
id: "concept:fully-collateralized-market"
type: concept
title: Fully Collateralized
title_zh: 全额抵押
title_en: Fully Collateralized
aliases:
  - Fully Collateralized
  - Fully Collateralized Market
  - 全额抵押
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
  - "source:2026-08-26-cftc-2026-05105-html"
related:
  - id: "concept:margin"
    rel: contrasts-with
    note: 全额抵押无违约链条但资本效率低 — CFTC 2026 保证金化提案的核心权衡
  - id: "venue:polymarket"
    rel: instantiated-by
    note: USDC 全额抵押结算
  - id: "venue:hyperliquid-hip4"
    rel: instantiated-by
    note: HIP-4 全额抵押模型
prerequisites:
  - "concept:collateral"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Fully Collateralized | 全额抵押

## Executive Definition / Chinese Explanation | 定义与解释

**Fully Collateralized Market | 全额抵押市场** = 每一份合约的最大可能赔付在开仓那一刻就被全额锁定，因此**违约在机制上不可能发生**。

二元事件合约天生适合这个模式：最大赔付就是 $1。买 YES 的人锁 $0.63，买 NO 的人锁 $0.37，加起来正好 $1 —— 无论结果如何，付款的钱已经在合约里了。

## Why This Matters | 为什么重要

它一次性消灭了传统衍生品最麻烦的东西：**信用评估、保证金追缴、连环强平、违约瀑布**，全都不需要。

代价同样彻底：**资本效率极低**。一个"12 个月后某事发生"的合约，你的钱要在合约里躺 12 个月，什么都干不了。这就是为什么机构资金进不来 —— 不是不信任，是算不过账。

**这个取舍是事件市场目前最重要的结构性约束**，也是所有"如何在保证结算确定性的前提下提高资本效率"的探索的起点。

## How It Works | 机制怎么运转

铸造与合并机制是这套体系的核心，只有两个操作：

- **铸造（mint/split）**：存 $1 → 拿到一份 YES + 一份 NO。
- **合并（merge）**：交回一份 YES + 一份 NO → 取回 $1。

这两个操作保证了一个恒等式：**任何时候 YES 价格 + NO 价格 ≈ $1**。偏离就有无风险套利：
- 若 `YES_ask + NO_ask < 1` → 两边都买，铸造成本低于 $1，锁定利润。
- 若 `YES_bid + NO_bid > 1` → 铸一套卖掉两边，同样锁定利润。

**做市商的日常工作有相当一部分就是执行这个套利**，它也是把两侧订单簿黏合起来的力量。

## Concrete Example | 具体例子

为什么它挡住了机构，用数字说话：

一个机构想在某事件上建 $10M 的对冲头寸，合约 6 个月后到期：

| | 全额抵押 | 保证金（假设 10%） |
|---|---|---|
| 占用资金 | **$10M** | $1M |
| 6 个月机会成本（按 5%） | **$250k** | $25k |
| 爆仓风险 | 无 | 有（追保/强平） |
| 对手方违约风险 | 无 | 有（靠 CCP 吸收） |

**$250k 的资金成本，去对冲一个可能只值几十万的风险敞口** —— 大多数情况下这笔账算不平。

这就是为什么"部分抵押 + 某种结算保证"是事件市场最有价值的未解工程问题。谁解开它，谁就打开了机构入口。

## Common Misconceptions | 常见误解

- **误解一："全额抵押 = 绝对安全。"** 它消除了**对手方违约**，没有消除智能合约风险、平台挪用风险，尤其没有消除**裁决错误风险**。钱在合约里很安全，但它可能被分给错的一方。
- **误解二："全额抵押就不需要清算了。"** 全额抵押本身**就是**一种清算方案 —— 用"提前锁死最大亏损"替代"评估信用 + 逐日盯市"。
- **误解三："YES + NO 一定精确等于 1。"** 因为费用、资金成本、撮合摩擦会有偏离。那个偏离量恰恰是衡量平台效率的好指标。

## In Practice | 实战里怎么用

看到"全额抵押"这四个字，接着问三个问题：

1. **抵押品是什么、由谁托管？** USDC 锁在链上合约里，和"记在平台账上的美元"是两码事。
2. **资金什么时候解锁？** 裁决后立刻，还是有争议窗口？争议期间锁着还是已分配？
3. **它没有覆盖什么风险？** 答案永远是：合约风险 + 裁决风险。**全额抵押对这两者一点保护都没有。**

再算一次资金成本：`锁定金额 × 无风险利率 × 剩余期限`。**如果这个数超过你想对冲的风险敞口的合理保费，这笔对冲就不该做。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么二元事件合约天生适合全额抵押？
  A: 最大赔付固定为 $1，YES 与 NO 的抵押相加正好覆盖全部可能赔付，违约在机制上不可能发生。
- Q: 铸造与合并机制保证了什么恒等式？它为什么重要？
  A: YES 价格 + NO 价格 ≈ $1。偏离即产生无风险套利，这个套利把两侧订单簿黏合成一个市场。
- Q: 全额抵押消除了哪些风险、没消除哪些？
  A: 消除了对手方违约风险；没有消除智能合约风险、平台挪用风险，尤其没有消除裁决错误风险。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cftc-2026-05105-html]] — <https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = collateral; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

---
id: "concept:execution-risk"
type: concept
title: Execution Risk
title_zh: 执行风险
title_en: Execution Risk
aliases:
  - 执行风险
status: seed
importance: tier-2
domains:
  - market-microstructure
  - institutional-risk
tags:
  - concept
created: 2026-08-26
updated: 2026-08-27
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related:
  - id: "concept:smart-order-routing"
    rel: mitigated-by
    note: 自动分单到最优 venue 降低滑点/漏单
prerequisites: []
---
# Execution Risk | 执行风险

## Executive Definition

从"决定交易"到"完成交易"之间一切可能出错的风险: 滑点超预期、只成交一半、价格跑掉、venue 宕机、订单被拒。

## Chinese Explanation | 中文解释

决策价与成交价之间隔着一条链: 路由 → 排队 → 撮合 → 确认。每一环都可能漏钱。机构度量它用 implementation shortfall (决策价 vs 实际全部成交均价的差), 而不是只看 [[slippage]] 单笔口径。

预测市场的执行风险有自己的形态: 盘口薄 ([[depth]] 常常只有几千美元)、事件驱动的流动性瞬间蒸发、单 venue 宕机没有替代盘口、以及部分成交后事件突然 resolve 的"半腿风险"。

## Money / Risk

- **谁承担风险**: 下单方。做市商的对应物是 [[adverse-selection]]; taker 的对应物就是执行风险。


## Active-Recall Questions

- Q: implementation shortfall 和 slippage 的区别?
  A: slippage 是单笔预期价 vs 成交价; shortfall 是从决策时点起算的全程成本, 含没成交部分的机会成本。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。

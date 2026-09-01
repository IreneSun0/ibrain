---
id: "concept:portfolio-margin"
type: concept
title: Portfolio Margin
title_zh: 组合保证金
title_en: Portfolio Margin
aliases:
  - 组合保证金
status: seed
importance: tier-2
domains:
  - derivatives
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
  - id: "concept:margin"
    rel: special-case-of
    note: 按整个组合净风险计算的保证金模式
  - id: "concept:cross-margin"
    rel: contrasts-with
    note: 全组合情景/风险模型 vs 头寸两两互抵
  - id: "concept:value-at-risk"
    rel: see-also
    note: SPAN/VaR 型风险模型是其计算内核
prerequisites:
  - "concept:margin"
---
# Portfolio Margin | 组合保证金

## Executive Definition

按整个组合的净风险 (通常用情景/风险模型如 SPAN 或 VaR 型) 计算保证金, 而不是逐仓逐品种相加 — 对冲得好的组合保证金大幅下降。

## Chinese Explanation | 中文解释

逐仓保证金把每个头寸孤立看待: 多 BTC 期货 + 空 BTC perp 各收一份保证金, 尽管净风险接近零。组合保证金改为对整个组合跑情景冲击 (价格 ±X%、波动率 ±Y%), 取最坏情景损失作为保证金。资本效率可以差几倍 — 这是机构选择 venue/prime broker 的硬指标。

与 [[cross-margin]] 的关系: cross margin 是"允许头寸间抵消"的一般原则; portfolio margin 是实现它的具体风险模型化方法。

## Risk | 风险在哪里

抵消关系依赖相关性假设 — 极端行情里相关性会断裂 (对冲失效), 组合保证金体系可能在最需要缓冲的时候缓冲最薄。清算所/交易所为此加 stress add-on。


## Active-Recall Questions

- Q: 组合保证金什么时候反而危险?
  A: 极端行情中相关性断裂, 原以为对冲的头寸同向亏损, 保证金覆盖不足。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = margin; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。

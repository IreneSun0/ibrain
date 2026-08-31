---
id: "concept:settlement-methodology"
type: concept
title: Settlement Methodology
title_zh: 结算方法论
title_en: Settlement Methodology
aliases:
  - 结算方法论
status: seed
importance: tier-2
domains:
  - prediction-outcome-markets
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
  - id: "concept:settlement-rail"
    rel: see-also
    note: 规则链第四层「通过什么轨道支付」即结算轨选择
prerequisites:
  - "concept:resolution"
  - "concept:settlement"
---
# Settlement Methodology | 结算方法论

## Executive Definition

一个 event contract 从"事实发生"到"钱到账"的完整规则链: 判定谁赢 ([[resolution]]) → 用什么价格/比例结算 → 何时结算 → 通过什么轨道支付 → 出错如何回滚。

## Chinese Explanation | 中文解释

Resolution 只回答"哪个结果赢了"; settlement methodology 回答整条兑现链:

1. **判定层**: 结果来源、判定时点、争议窗口 (见 [[resolution-source]] / [[dispute-mechanism]])。
2. **计价层**: 赢方每份赎回多少 (二元 $1; scalar 按公式; 取消/无效市场按 50/50 还是退款 — 这条规则差异巨大且常被忽视)。
3. **支付层**: 链上赎回 (Polymarket: CTF 合约烧 token 换 USDC) vs 中心化账本入账 (Kalshi: 监管框架下的会员账户)。
4. **终局层**: 链上结算基本不可逆; 中心化 venue 理论上可以纠错回滚 — 两种终局性对风险模型含义完全不同。

跨 venue 比较时, "同一事件"在四层上都可能不同 — 这是 [[contract-equivalence]] 必须逐层核对的清单。


## Active-Recall Questions

- Q: 市场被取消 (void) 时不同 venue 的处理差异为什么重要?
  A: 退款 vs 50/50 结算直接改变持仓的尾部 payoff, 对冲腿会因此不对称。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = resolution, settlement; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。

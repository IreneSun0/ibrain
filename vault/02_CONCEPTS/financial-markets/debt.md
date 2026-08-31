---
id: "concept:debt"
type: concept
title: Debt
title_zh: 债权/债务工具
title_en: Debt
aliases:
  - 债券
  - Bond
  - Fixed Income
status: seed
importance: tier-2
domains:
  - financial-markets
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
  - id: "concept:equity"
    rel: contrasts-with
    note: 固定上限收益+优先受偿 vs 剩余索取权+收益不封顶
prerequisites: []
---
# Debt | 债权

## Executive Definition

约定还本付息的借贷合约: 收益固定且有上限, 受偿顺序优先于股权, 核心风险是违约。

## Chinese Explanation | 中文解释

债是"固定索取权"。买债券 = 借钱给发行人, 换取利息与到期还本。价格对利率敏感 (利率升, 存量债价格跌), 对发行人信用敏感 (违约概率升, 价格跌)。全球债市规模大于股市 — 机构资金的主体停泊在债里, 这是理解"机构风险偏好"的底色。

## Why This Exists | 为什么存在

资金供需双方对风险的偏好不同: 有人要确定性现金流, 有人 (股东) 愿意吃剩余风险换上行。债/股分层让同一家企业能同时向两类资金融资。

## Money / Risk / Settlement

- **钱在哪里**: 债权人本金在发行人手里; 二级市场大量走 OTC dealer 市场而非交易所。
- **谁承担风险**: 债权人承担违约风险与利率风险; 见 [[credit-risk]]。
- **结算**: 清算所/托管行; 国债有专门结算体系。


## Active-Recall Questions

- Q: 为什么利率上升债券价格下跌?
  A: 存量债的固定票息相对新发行的更高利率变得不值钱, 价格必须跌到收益率对齐。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。

---
id: "concept:liquidation"
type: concept
title: Liquidation
title_zh: 强制平仓
title_en: Liquidation
aliases:
  - 强制平仓
status: reviewed
importance: tier-2
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
related:
  - id: "concept:leverage"
    rel: risk-of
    note: 流动性差时强平本身冲击价格并形成连锁
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Liquidation | 强制平仓

## Executive Definition / Chinese Explanation | 定义与解释

**Liquidation | 强制平仓 / 清算** = 保证金账户的权益跌破维持要求时，系统强行卖出你的头寸来止损。

它不是惩罚，是**保证金制度的必然结果**：既然你只押了一部分钱，那么亏损吃掉押金之前必须有人踩刹车。

## Why This Matters | 为什么重要

强平是[[margin|保证金]]制度的代价，也是加密市场最主要的系统性风险来源。

**关键在于它的连锁性**：强平会砸出卖单 → 价格下跌 → 触发更多强平 → 继续下跌。这个正反馈在薄流动性上尤其暴力。

**对比事件市场**：全额抵押的事件合约**根本没有强平**（见 [[fully-collateralized-market]]）。这一点在一个以连环爆仓闻名的行业里，是被严重低估的优点。

## How It Works | 机制怎么运转

强平的完整链条：

```
权益 / 维持保证金 < 1  →  追加保证金通知
未在期限内补足        →  部分或全部强平
强平价 < 破产价        →  穿仓, 由保险基金或社会化损失承担
```

三个关键参数决定你离强平有多远：
- **初始保证金** —— 开仓要押多少。
- **维持保证金** —— 跌到多少触发。
- **强平惩罚/清算费** —— 被强平时额外损失多少。

**很多人只看初始保证金（决定杠杆倍数），却不看维持保证金（决定距离强平多远）** —— 后者才是真正的风险参数。

## Concrete Example | 具体例子

一个 10 倍杠杆的多头，从开仓到穿仓：

```
名义 $100,000, 自有资金 $10,000
初始保证金 10%, 维持保证金 5%

价格 −5%  → 权益 $5,000  = 维持线, 追保通知
价格 −6%  → 权益 $4,000  < 维持线, 触发强平
价格 −10% → 权益 $0      = 破产价
价格 −12% → 穿仓 $2,000  ← 由保险基金或其他用户承担
```

**注意第一行到第二行只差 1%。** 10 倍杠杆意味着标的动 5% 你就到追保线 —— 而在事件市场的跳变标的上，5% 只是一条新闻的一半。

**这就是为什么二元跳变标的的保证金化是未解难题**（见 [[margin]]）。

## Common Misconceptions | 常见误解

- **误解一："设好止损就不会被强平。"** 极端行情下止损可能滑价穿过，或根本无法成交。强平是交易所主动执行的，不受你的止损影响。
- **误解二："被强平最多亏光本金。"** 穿仓时可能倒欠（视平台的负余额保护政策）。
- **误解三："事件合约也会爆仓。"** 全额抵押的不会 —— 最大损失是本金，且开仓即知。**这是它相对永续的真实优势。**

## In Practice | 实战里怎么用

持有任何保证金头寸，先算三个数：

1. **强平价** —— 标的到哪个价位触发？写下来。
2. **距离** —— 强平价离现价多少百分比？
3. **该标的一天能动多少？** —— 用历史波动率或跳变幅度对照第 2 条。

**如果第 3 条大于第 2 条，你的头寸在统计上活不过一天。**

**对事件合约的推论**：不要因为"没有强平"就放大仓位。杠杆风险消失了，但集中度、裁决、流动性风险一个都没少 —— 它们才是这个市场真正的风险来源。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 强平为什么是保证金制度的必然结果？
  A: 既然只押了一部分资金，亏损吃掉押金之前必须有人踩刹车，否则损失会外溢给交易所或其他用户。
- Q: 为什么维持保证金比初始保证金更重要？
  A: 初始保证金只决定杠杆倍数，维持保证金决定你离强平有多远 —— 那才是真正的风险参数。
- Q: 什么是穿仓？谁承担？
  A: 强平价低于破产价时的缺口，由保险基金或社会化损失（其他用户）承担，部分平台还可能向用户追偿。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

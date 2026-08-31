---
id: "concept:counterparty-risk"
type: concept
title: Counterparty Risk
title_zh: 交易对手风险
title_en: Counterparty Risk
aliases:
  - 交易对手风险
status: reviewed
importance: tier-1
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
  - id: "concept:over-the-counter"
    rel: risk-of
    note: 无 CCP 的双边交易是对手方风险的裸露形态
  - id: "concept:clearinghouse"
    rel: mitigated-by
    note: CCP 成为所有人的对手方 + 保证金/违约基金瀑布
  - id: "concept:collateral"
    rel: mitigated-by
  - id: "concept:custody-segregation"
    rel: mitigated-by
    note: 平台破产时客户资产不被当作公司财产
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Counterparty Risk | 交易对手风险

## Executive Definition / Chinese Explanation | 定义与解释

**Counterparty Risk | 对手方风险** = 交易对手在该付钱的时候付不出来的风险。

它是所有金融基础设施设计的原始动机 —— 清算所、保证金、抵押品、违约瀑布，全都是为了回答"凭什么相信对方到时候会付"。

## Why This Matters | 为什么重要

在事件市场里，这个风险的形状被**彻底改变**了，理解这一点是理解整个赛道的关键：

**全额抵押把对手方风险压到了零**（见 [[fully-collateralized-market]]）。钱在开仓那一刻已经锁进合约，违约在机制上不可能发生。

**但风险守恒。** 它没有消失，只是换了名字：
- 对手方风险 → **裁决风险**（钱在，但可能分给错的人）
- 对手方风险 → **智能合约风险**（钱在，但合约可能有 bug）
- 对手方风险 → **平台/托管风险**（钱是否真的在你以为的地方）

**很多人只看到第一句就以为安全了。**

## How It Works | 机制怎么运转

传统市场吸收对手方风险的四层，逐层看事件市场有没有对应物：

| 传统机制 | 事件市场有吗 |
|---|---|
| 信用评估与授信额度 | 不需要（全额抵押） |
| 初始保证金 + 逐日盯市 | 不需要（全额抵押） |
| 中央对手方（novation） | 持牌平台有（如 Kalshi Klear）；链上平台没有也不需要 |
| 违约瀑布 | 同上 |

**但反过来，事件市场有一层传统市场没有的风险 —— 裁决层，而它没有任何吸收机制**（见 [[resolution-insurance]]）。

**净效果**：事件市场用一个成熟的、有百年制度积累的风险（信用），换了一个全新的、没有任何制度积累的风险（裁决）。

## Concrete Example | 具体例子

两种失效方式的对照：

**传统方式（对手方违约）**：对手破产 → CCP 的违约瀑布启动 → 违约方保证金 → 违约基金 → CCP 自有资本 → 幸存会员分摊。**你大概率能拿到钱。**

**事件市场方式（裁决出错）**：合约按错误结果结算 → 钱已经付给了另一方 → 链上不可逆 → **没有任何瀑布。** Ukraine 矿产协议案（2025-03）里，平台公开承认那是一次治理攻击，**依然拒绝退款**（见 [[case-uma-dispute-trilogy]]）。

**同样是"你应得的钱没拿到"，一边有百年制度兜底，一边零追索。**

## Common Misconceptions | 常见误解

- **误解一："全额抵押 = 没有对手方风险 = 安全。"** 第一个等号成立，第二个不成立。风险换了位置。
- **误解二："链上合约就是对手方。"** 合约不是法律主体，不会破产，也不会赔偿。它只会执行代码。
- **误解三："有 CCP 就万无一失。"** CCP 把风险集中了。CCP 本身倒下是尾部风险中最严重的一种。

## In Practice | 实战里怎么用

评估任何一个场所的对手方风险，按这四问：

1. **抵押模式** —— 全额还是保证金？全额则对手方违约不可能。
2. **钱在哪** —— 链上合约 / 独立托管 / 平台运营账户？**第三种是最危险的，也最常见于离岸平台。**
3. **有没有 CCP** —— 有则问违约瀑布顺序与会员集中度。
4. **裁决出错时谁赔** —— **这一问在传统尽调清单里没有，但在事件市场它是最重要的一问。** 默认答案是"没人"。

第 4 问答不上来，你的对手方风险就没有真正消失，只是改了名字。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 全额抵押把对手方风险换成了哪三种风险？
  A: 裁决风险（钱在但可能分给错的人）、智能合约风险、平台/托管风险。风险守恒，只是换了名字。
- Q: 传统对手方违约与事件市场裁决出错，在救济上的关键差别是什么？
  A: 违约有 CCP 的多层违约瀑布兜底；裁决出错在链上不可逆且无任何吸收机制，先例是零追索。
- Q: 尽调时哪一问在传统清单里没有、但在事件市场最重要？
  A: '裁决出错时谁赔' —— 默认答案是没人。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

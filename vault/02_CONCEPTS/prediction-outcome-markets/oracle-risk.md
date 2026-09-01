---
id: "concept:oracle-risk"
type: concept
title: Oracle Risk
title_zh: 预言机风险
title_en: Oracle Risk
aliases:
  - 预言机风险
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
related:
  - id: "concept:oracle"
    rel: risk-of
  - id: "concept:dispute-mechanism"
    rel: mitigated-by
    note: 争议程序是 oracle 出错后的纠错层
  - id: "protocol:uma"
    rel: see-also
    note: 2025-26 三连争议实证乐观预言机结构缺陷 (投票权可买/挑战激励不足/语义缝隙)
prerequisites:
  - "concept:oracle"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Oracle Risk | 预言机风险

## Executive Definition / Chinese Explanation | 定义与解释

**Oracle Risk | 预言机风险** = 把外部世界的事实输入合约的那个机制本身出错、被操纵、或被治理俘获的风险。

它不是"技术会不会宕机"的问题。**预言机的核心风险是经济学的：当操纵它的收益大于成本时，它就会被操纵。**

## Why This Matters | 为什么重要

在链上事件市场里，预言机是**唯一一个"信任无法被消除、只能被转移"的位置**。

智能合约可以审计，抵押可以链上验证，撮合可以做到可证明公平 —— 但"哈梅内伊是否卸任"这个事实，链自己不知道。**必须有人告诉它。** 而那个"人"就是整个系统的信任奇点。

**去中心化把信任从平台转移到了预言机，没有消除它。**

## How It Works | 机制怎么运转

乐观预言机（optimistic oracle）的设计是：默认相信提议者，除非有人挑战。[[uma]] 的 DVM 在有争议时交由代币持有人投票终裁。

这个设计有**三个结构性缺陷**，2025–2026 年逐一在真金白银里兑现（见 [[case-uma-dispute-trilogy]]）：

1. **投票权可购买** — Schelling 点均衡假设投票人分散且激励对齐。**集中持币人 + 自己有仓位 = 均衡破产。** 安全边界 = 攻击成本 vs 可操纵的市场规模，**盘口越大，攻击越划算**。
2. **小盘挑战激励不足** — 挑战需要押金和时间成本。市场太小时，理性的人不会去挑战一个错误提议，错误就此通过。
3. **语义缝隙** — 见 [[contract-semantics]]。文本有缝时，投票只是把争议合法化，解决不了争议。

**这三条不是 bug，是这类设计的固有权衡。**

## Concrete Example | 具体例子

**Ukraine 矿产协议案（2025-03-25）** 是"投票权可购买"最干净的实证：

一个约 **$7M** 的市场问"Ukraine 是否与 Trump 签署矿产协议"。单一行为人用 **3 个账户投出 5M UMA，占该轮约 25% 的投票权**，把一件**并未发生**的事裁定为 Yes。价格在 24 小时内从 **9% 冲到 100%**。

[[polymarket]] 公开定性其为 **"unprecedented governance attack"（史无前例的治理攻击）**，但**拒绝退款**，理由是这不构成 market failure。

**受害者零追索。** 这个结果本身，就是"裁决保险"这个概念的需求证明。

## Common Misconceptions | 常见误解

- **误解一："多个数据源就安全了。"** 多源解决的是单点故障，不解决**治理攻击**。投票机制被俘获时，数据源再多也没用。
- **误解二："预言机风险是技术风险。"** 它主要是经济风险与治理风险。技术上一切正常，结果照样可以是错的。
- **误解三："出了事平台会赔。"** Ukraine 案的先例是**不赔**。在做交易决策时，应当默认没有赔付。

## In Practice | 实战里怎么用

评估一个链上事件市场的预言机风险，算一道题：

```
攻击成本 = 获得关键投票权所需的代币成本（含滑点与价格冲击）
攻击收益 = 可被这次裁决影响的最大市场规模 × 可获取比例
```

**当收益 > 成本时，这个市场就是可攻击的 —— 与人品无关，是数学。**

再补三个检查：
- 投票权的**集中度**（前 10 地址占比）；
- 历史上有没有**已兑现的攻击**，平台如何处理；
- 该平台是否已按**合约类型分流**（价格类走自动化喂价，主观类走人工），这是当前最实际的缓解手段。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说预言机风险主要是经济风险而非技术风险？
  A: 当操纵收益大于操纵成本时它就会被操纵；技术完全正常时结果依然可能是错的。
- Q: 乐观预言机的三个结构性缺陷是什么？
  A: 投票权可购买（Schelling 均衡破产）、小盘挑战激励不足、语义缝隙让错误裁决合法化。
- Q: Ukraine 矿产协议案的关键数字和结论是什么？
  A: $7M 市场，单一行为人用 3 个账户投 5M UMA 占约 25% 投票权，把未发生的事裁成 Yes，价格 24h 内 9%→100%；平台定性为治理攻击但拒绝退款，受害者零追索。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = oracle; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

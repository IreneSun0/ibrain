---
id: "concept:token-economy"
type: concept
title: Token Economy
title_zh: 代币经济
title_en: Token Economy
aliases:
  - 代币经济
status: reviewed
importance: tier-2
domains:
  - industry-strategy
  - crypto-market-structure
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
  - id: "concept:exchange-vertical-integration"
    rel: mechanism-of
    note: 平台币把费用、激励与治理锁进自家栈
prerequisites:
  - "concept:token"
import_origin: xlsx-learning-map+manual
import_category: 产业战略
---
# Token Economy | 代币经济

## Executive Definition / Chinese Explanation | 定义与解释

**Token Economy | 代币经济** = 用可编程的权利凭证来协调一个网络里各方行为的设计：谁出资源、谁得回报、谁有话语权。

**它不是"发个币"** —— 它是一套激励机制设计，而机制设计错了，代币只会加速失败。

## Why This Matters | 为什么重要

对事件市场，代币经济有一个**特别危险的交叉点**：**当代币同时是治理权和裁决权时。**

[[uma|UMA]] 的乐观预言机就是这个形态：代币持有人投票决定争议裁决。这在设计上很优雅 —— 让有经济利益的人来维护真相。

**但它有一个致命前提：投票权不能被购买。**

而代币是可交易的，**所以投票权永远可以被购买**。当"操纵一次裁决的收益"大于"买到足够投票权的成本"时，攻击就会发生 —— 这不是假设，是已经反复兑现的事实（见 [[case-uma-dispute-trilogy]]）。

## How It Works | 机制怎么运转

代币在一个网络里可能承担四种功能，风险各不相同：

| 功能 | 例 | 风险 |
|---|---|---|
| **支付/gas** | 链的手续费代币 | 价格波动影响使用成本 |
| **质押/安全** | PoS 质押（见 [[proof-of-stake]]） | 集中度 |
| **治理** | 参数投票 | 投票权可购买 |
| **裁决** | 争议终审 | **投票权可购买 + 裁决不可逆** |

**第四行是最危险的组合**：可购买的权力 + 不可撤销的后果。

**行业的实际反应是把可自动化的部分移出投票**：价格类裁决改走自动化喂价，只把真正需要解释的留给人（见 [[oracle]]）。

## Concrete Example | 具体例子

代币经济设计的一个具体教训：

```
市场规模        $7M
攻击成本        买入约 25% 投票权所需的代币
攻击者行动      3 个账户投出 5M 代币
结果            把未发生的事裁成 Yes, 价格 24h 内 9% → 100%
平台定性        "史无前例的治理攻击"
赔付            拒绝
```

**关键在于这不是 bug** —— 投票机制完全按设计运行。

**问题在于设计的安全边界是经济性的**：安全性 = 攻击成本 > 可操纵的市场规模。**而市场规模会增长，代币价格会波动 —— 这条不等式并不稳定。**

**盘口越大，攻击越划算。**

## Common Misconceptions | 常见误解

- **误解一："代币激励可以解决协调问题。"** 只有在激励与真实目标一致时。**当说谎的收益大于诚实的收益，激励就在鼓励说谎。**
- **误解二："去中心化治理更公正。"** 取决于权力分布。可购买的权力等于财富分布，不等于公正。
- **误解三："代币经济是金融设计。"** 它首先是**机制设计**：先问"谁能作恶、作恶划不划算"，再谈发行与分配。

## In Practice | 实战里怎么用

评估任何把代币用于裁决或治理的设计，算一道题：

```
攻击成本 = 获得关键投票权所需的代币成本（含滑点与价格冲击）
攻击收益 = 可被影响的最大市场规模 × 可获取比例
```

**收益 > 成本 → 这个设计是可攻击的。与人品无关，是数学。**

再补三问：
1. **投票权集中度** —— 前 10 地址占多少？
2. **代币价格与市场规模的关系** —— 币价跌时攻击是否变便宜？
3. **有没有把可自动化的部分移出投票？** 这是当前最实际的缓解手段。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 代币用于裁决时最危险的组合是什么？
  A: 可购买的权力 + 不可撤销的后果 —— 代币可交易意味着投票权永远可以被购买，而链上裁决不可逆。
- Q: 为什么'攻击成本 > 市场规模'这条安全边界并不稳定？
  A: 市场规模会增长、代币价格会波动，盘口越大攻击越划算，不等式可能随时反转。
- Q: 行业对代币裁决风险的实际缓解手段是什么？
  A: 把可自动化的部分移出投票 —— 价格类裁决改走自动化喂价，只把真正需要解释的留给人。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)

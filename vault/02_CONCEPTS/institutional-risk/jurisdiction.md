---
id: "concept:jurisdiction"
type: concept
title: Jurisdiction
title_zh: 司法辖区/适用法域
title_en: Jurisdiction
aliases:
  - 司法辖区
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
  - id: "jurisdiction:united-states"
    rel: instantiated-by
    note: CFTC DCM 路径 — 事件合约唯一联邦合法框架
  - id: "jurisdiction:singapore"
    rel: instantiated-by
    note: "无持牌路径, GRA 认定非法赌博并封禁 — 同一产品两种法域命运"
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Jurisdiction | 司法辖区/适用法域

## Executive Definition / Chinese Explanation | 定义与解释

**Jurisdiction | 司法管辖 / 法域** = 决定"谁的规则约束你、出事时你去哪里申诉"的那个法律边界。

在事件市场里它不是背景信息，而是**第一位的风险维度** —— 因为同一个产品在不同法域的法律性质完全不同：在美国是受 CFTC 监管的衍生品，在新加坡属赌博归博彩监管，在多个国家直接被封。

## Why This Matters | 为什么重要

**管辖权是乘法不是加法。**

你必须**同时**满足所有触达法域的规则；任何一地爆雷都是全局风险（罚款、牌照、高管责任）。这跟"合规成本随法域数量线性增长"的直觉完全不同 —— 它是相乘的。

实际后果：**地理围栏（geofencing）不是产品细节，是生存机制。** "哪些用户能进"这份名单直接由法域地图生成，而不是由市场部决定。

## How It Works | 机制怎么运转

事件市场的法域地图三分天下：

| 类型 | 特征 | 代表 |
|---|---|---|
| **明确合法框架** | 有牌照路径、有规则、有申诉 | 美国 DCM 路线（CFTC） |
| **明确禁止** | 视为博彩或非法衍生品 | 多国直接屏蔽 |
| **灰色/未定** | 无明文，执法不确定 | 多数法域 |

现实规模：[[polymarket]] 离岸平台被 18 国屏蔽（法国 / 新加坡 / 巴西 / 比利时等）；[[kalshi]] 有 55 个辖区限制访问（英国 / 加拿大 / 法国 / 中国等）。

**并且边界仍在移动**：[[kalshi]] 正与 ≥14 个州打"赌博 vs 联邦衍生品"的官司，CFTC 亲自下场主张联邦排他管辖；纽约州总检察长于 2026-07-31 提起索赔 ≥$36B 的诉讼。**这条线目前在法庭上，不在法条里。**

## Concrete Example | 具体例子

同一个"押注美国大选"的动作，在四个地方是四件事：

| 你在哪 | 法律性质 | 出事找谁 |
|---|---|---|
| 美国，[[kalshi]] | 受监管的事件合约 | CFTC / 平台申诉机制 |
| 美国某州，同一平台 | **可能被州法视为博彩** | 正在打官司 |
| 新加坡 | 属赌博，归 GRA 管；不归 MAS | 基本无救济 |
| 被屏蔽国家 | 违规访问 | 无 |

**注意第二行**：**同一个国家内部，联邦与州的定性可能相反**，而用户完全无从判断自己处在哪种状态。

## Common Misconceptions | 常见误解

- **误解一："用 VPN 就绕过去了。"** 绕过的是访问限制，不是法律。出事时你在违规一侧，且没有任何救济。
- **误解二："平台合规了我就安全了。"** 平台的合规覆盖平台，不覆盖你。**你所在地的法律约束你。**
- **误解三："法域状态是静态的。"** 这是当前变化最快的维度 —— 监管态度、法院判决、州联邦之争都在移动。

## In Practice | 实战里怎么用

把法域当成必查项，四问：

1. **平台在哪个法域持牌？** 无牌照 ≠ 违法，但意味着没有申诉渠道。
2. **我所在地怎么定性这个产品？** 衍生品 / 博彩 / 未定？
3. **出事时我去哪申诉？** 监管机构 / 平台内部委员会 / 无。
4. **这个状态最近 12 个月变过吗？** 变化频率本身就是风险指标。

**对做业务的人多一条**：数据与风险分析服务不碰交易撮合与客户资金，管辖敏感度比场馆低一个数量级 —— **场馆有国界，风险信息没有。** 这是一个真实的结构性差异。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说管辖权是乘法不是加法？
  A: 必须同时满足所有触达法域的规则，任何一地爆雷都是全局风险（罚款/牌照/高管责任），而非按法域数量线性叠加。
- Q: 事件市场的法域地图分哪三类？
  A: 明确合法框架（如美国 DCM 路线）、明确禁止（视为博彩或非法衍生品）、灰色未定（多数法域）。
- Q: 为什么'平台合规了我就安全'是错的？
  A: 平台的合规只覆盖平台自身；约束用户的是用户所在地的法律，两者可能定性相反。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。

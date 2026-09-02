---
id: meta:relationship-types
type: taxonomy
title: Relationship Type Vocabulary
title_zh: 关系类型受控词表
aliases:
  - relationship types
status: reviewed
importance: tier-1
domains:
  - meta
tags:
  - taxonomy
created: 2026-08-26
updated: 2026-08-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related: []
---

# 关系类型受控词表

关系笔记的 `relationship_type` 与生态图边标签**只允许**使用下列值。新增类型须先在本文件登记。

本词表分两层:
- **实体级重关系** (人/组织/venue 之间, 建独立 relationship note, 必须有 evidence) — 见下方「人 ↔ 组织」「组织 ↔ 组织」。
- **概念级轻关系** (概念页之间及概念→实体实例, 直接写在概念页 frontmatter `related` 里, 不建独立文件) — 见「概念级语义关系」一节。

## 人 ↔ 组织

| type | 中文 | 语义 |
|---|---|---|
| `founded` | 创立 | 单独创立该组织 |
| `co-founded` | 共同创立 | 与他人共同创立 |
| `worked-at` | 曾任职 | 历史雇佣关系 (非高管) |
| `former-executive-of` | 前高管 | 历史高管职位 |
| `executive-of` | 现任高管 | 当前高管职位 (须 `last_verified`) |
| `advises` | 顾问 | 顾问关系 |
| `alumnus-of` | 校友/前员工网络 | 共享的机构履历 (公司或学校) |
| `controls` | 实际控制 | 有证据的控制权 (股权/投票权/事实控制) |
| `governs` | 治理 | 治理角色 (基金会/DAO/董事会) |

## 组织 ↔ 组织

| type | 中文 | 语义 |
|---|---|---|
| `invested-in` | 投资了 | A 向 B 投资 (须有轮次/金额证据或明确报道) |
| `backed-by` | 获投于 | invested-in 的反向 |
| `acquired` | 收购了 | 完成的收购 |
| `partners-with` | 合作 | 有公开宣布或有证据的商业合作 |
| `integrates-with` | 集成 | 技术/产品集成 |
| `competes-with` | 竞争 | 同一市场直接竞争 |
| `provides-liquidity-to` | 提供流动性 | 做市/LP 关系 |
| `provides-infrastructure-to` | 提供基础设施 | 基础设施供应关系 |
| `built-on` | 构建于 | 协议/产品构建在某链/平台上 |
| `settles-on` | 结算于 | 结算轨道依赖 |
| `regulated-by` | 受监管于 | 持牌/注册/受辖关系 |
| `distributes` | 分发 | 分发渠道关系 |
| `depends-on` | 依赖 | 运营依赖 (数据/托管/银行等) |
| `spun-out-of` | 分拆自 | 从母体分拆 |

## 概念级语义关系 (frontmatter `related`)

概念页之间的关系**轻量**放在概念页 frontmatter 的 `related` 里, 不建独立 relationship note (独立文件留给实体级重关系)。前置链由专用字段 `prerequisites` 承载, 不占用 `related`。

### 格式

`related` 列表元素允许两种形态:

```yaml
related:
  - id: "concept:order-book"        # 必填: 目标页 id, 必须存在于库内
    rel: special-case-of            # 必填: 下方概念关系词表之一
    note: 集中化+限价撮合的订单簿    # 可选: 一句话讲清这条边为什么成立
  - "concept:foo"                   # 兼容旧格式: 裸 id = 未分类弱关联 (legacy, 待升级为 typed)
```

新填的概念关系**必须**用 typed 形态; 裸 id 仅为兼容存量。

### 概念关系词表

读法统一为「**本页 —rel→ 目标页**」(主语 = 持有这条边的页面):

| type | 中文 | 语义 (本页 X, 目标 Y) | 例 |
|---|---|---|---|
| `special-case-of` | 特例 | X 是 Y 的特例 / 子类型 | binary-option → option |
| `component-of` | 组成 | X 是 Y 的组成部分 | bid → order-book |
| `mechanism-of` | 机制 | X 是实现 / 驱动 Y 的机制 | funding-rate → perpetual-futures |
| `risk-of` | 风险面 | X 是 Y 所承载的风险 | adverse-selection → market-maker |
| `mitigated-by` | 缓解 | X (风险) 由 Y 缓解 / 对冲 | counterparty-risk → clearinghouse |
| `measured-by` | 度量 | X 由 Y 度量 / 量化 | liquidity → depth |
| `contrasts-with` | 对照 | X 与 Y 是有教学价值的对照对 (对称) | AMM → CLOB |
| `instantiated-by` | 实例 | X (概念) 的真实世界实例是 Y (实体页) | CLOB → venue:polymarket |
| `see-also` | 另见 | 强相关但不属于上述任何类型; **必须带 note** | contract-equivalence → basis-risk |

`prerequisite-of` 不在此表: 前置关系由 frontmatter `prerequisites` 字段承载 (语义 =「不先懂 A, 就真的看不懂本页」的**硬**前置; 泛泛相关不算)。

### 概念关系纪律

1. **每条边只存一次**, 存在语义主语页 (读法的 X 侧); 反向视图 (「Y 的特例有哪些」「Y 解锁什么」) 由展示层 / 导出脚本反向渲染, 禁止两页重复存同一条边。
2. 对称关系 (`contrasts-with`) 存在**用对照来解释自己的一侧** (定义里引用对方的页面); 双方都不引用时, 存 id 字典序较小的一页。
3. **宁缺勿滥**: `prerequisites` 只填直接硬前置 (1–4 个), 不填传递闭包 (A→B→C 时 C 只填 B); `related` 每页 0–4 条为常态; `see-also` 每页 ≤2 条且必须带 note。
4. `instantiated-by` 的目标必须是库内实体页, 且 note / 实体页内容能支撑这个实例判断; 禁止凭生态联想挂实例。
5. AI 补的概念关系视为 seed 判断: 所在页面保持 `status: seed` 或如实降档, 并在页面 timeline 追加一条记录; 维护者复核后随页面一起升 `reviewed`。
6. `related` 目标 id 与 `rel` 值由校验器强制 (id 必须存在, rel 必须在本词表)。

## 使用规则 (实体级)

1. 每条关系必须有 **evidence** 字段 (指向 source note 或 timeline 条目)。
2. **禁止**: 生态联想 ⇒ `controls`; 社媒互动 ⇒ `partners-with`; 同城/同会议 ⇒ 任何关系。
3. 共享履历只能写 `alumnus-of` / `worked-at`, 不得升格为协同/联盟, 除非有独立证据。
4. 历史关系与当前关系分开: `worked-at` ≠ `executive-of`; 关系结束要填 `end_date` 并把 `current_status` 改为 `ended`。
5. 有争议的关系 (公开纠纷/诉讼) 写入关系笔记的 timeline, `confidence` 如实降档。

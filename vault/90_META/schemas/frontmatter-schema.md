---
id: meta:frontmatter-schema
type: policy
title: Frontmatter Schema
title_zh: Frontmatter 字段规范
aliases:
  - schema
status: reviewed
importance: tier-1
domains:
  - meta
tags:
  - schema
created: 2026-08-26
updated: 2026-08-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related: []
---

# Frontmatter 字段规范

机器权威版: [frontmatter-schema.json](frontmatter-schema.json) (校验器 `validate_frontmatter.py` 直接读它)。本文件是人读版。

## 通用 schema (所有结构化笔记)

```yaml
---
id: concept:central-limit-order-book   # 必填, 形如 <type-prefix>:<slug>, 创建后永不改
type: concept                          # 必填, 见允许值
title: Central Limit Order Book        # 必填
title_zh: 中央限价订单簿                 # 推荐
title_en: Central Limit Order Book     # 可选
aliases:                               # 推荐 — 中英别名都放这里
  - CLOB
  - 订单簿
status: seed                           # 必填: stub|seed|draft|reviewed|verified|stale|archived
importance: tier-1                     # tier-1|tier-2|tier-3 (person/organization 必填)
domains:                               # 推荐, 见 domains 允许值
  - market-microstructure
tags:
  - concept
created: 2026-08-26                    # 必填 YYYY-MM-DD
updated: 2026-08-26                    # 必填 YYYY-MM-DD
last_verified:                         # 动态事实页必填才能标 verified
review_after:                          # 建议复核日期
confidence: medium                     # 必填: high|medium|low|unknown
epistemic_status: mixed                # 必填: confirmed|inference|hypothesis|rumor-unverified|mixed|unknown
confidentiality: internal              # 必填: public-source|internal|confidential|strictly-private
sources: []                            # source note 的 id 列表
related:                               # 相关页; 概念页用 typed 形态 (词表见 taxonomy/relationship-types.md)
  - id: "concept:order-book"           #   目标 id (必须存在)
    rel: special-case-of               #   概念关系词表值 (schema JSON: allowed_concept_relation_types)
    note: 可选一句话                    #   这条边为什么成立
  - "concept:legacy-bare-id"           #   裸 id = 未分类弱关联 (legacy 兼容)
prerequisites: []                      # 概念页: 硬前置概念 id (「不懂它就看不懂本页」; 判断过没有就留空)
---
```

## status 语义

| status | 含义 | 升级条件 |
|---|---|---|
| `stub` | 只有骨架, 待填 | — |
| `seed` | 有实质内容, 未经人工复核 (含 AI seed 与 Excel 导入) | 人工或 researcher 复核 → draft/reviewed |
| `draft` | 人在主动编写中 | 写完 → reviewed |
| `reviewed` | 内容经人工复核, 来源可以不全 | 关键断言全部有 source → verified |
| `verified` | 关键断言应全部有来源; 动态页还需 `last_verified` | 校验器只强制 source id/locator 结构, **不证明引用支持断言**; entailment 仍需人工复核 |
| `stale` | 超过 `review_after` 或已知过期 | 重新核实 → 回 reviewed/verified |
| `archived` | 不再维护 | — |

## 硬规则 (校验器强制)

1. `id` 全库唯一, 永不更改; 改名走 alias。
2. `status: verified` ⇒ `sources` 非空; 实体类页面 (person/organization/venue/…) 还要求 `last_verified` 非空。**例外**: `type: source` 不自引, 但必须至少有一个 locator: `url` / `content_hash` / `archive_path`。URL-only source 仍有证据漂移风险。
3. 所有枚举字段只允许 schema JSON 里列出的值。
4. 日期字段必须是 `YYYY-MM-DD` 且为真实日历日期。
5. `aliases` / `domains` / `tags` / `sources` / `related` / `prerequisites` / `evidence` 必须是 list; `sources` 与 `evidence` 里的 id 必须存在。
   - `related` 元素为 dict 时必须含 `id` + `rel`: `id` 必须存在于库内, `rel` 必须在 `allowed_concept_relation_types` 词表内 (词表人读版: `90_META/taxonomy/relationship-types.md`); 裸字符串元素 (legacy) 也必须是存在的 id。
   - `prerequisites` 元素必须是存在的 id 且指向 `type: concept` 页面。
6. source 类型笔记必须有 `source_type` / `reliability` / `accessed_at` 及至少一个 locator; URL 必须是 absolute HTTP(S)。
7. relationship 笔记必须有 `entity_a` / `entity_b` / `relationship_type` / `relationship_status` / `evidence`; 两端 id 和 evidence id 必须存在, 类型必须在受控词表内。
8. 页面 confidentiality 不得低于它引用的 source; raw conversation transcript/worksheet 必须 `strictly-private`。

## id 前缀约定

`concept:` `person:` `org:` `venue:` `protocol:` `mmf:` (market-maker/fund) `product:` `token:` `regulator:` `jurisdiction:` `event:` `case:` `rel:` `source:` `book:` `thesis:` `hyp:` `decision:` `q:` `meeting:` `report:` `orig:` `moc:` `dash:` `meta:` `curr:` `study:` `deck:` `lesson:` (课程教学层, 10_LEARNING/course/)

relationship id 约定: `rel:<entity-a-slug>--<type>--<entity-b-slug>`
source id 约定: `source:<YYYY-MM-DD>-<slug>`

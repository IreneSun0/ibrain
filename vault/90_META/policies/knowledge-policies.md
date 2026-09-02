---
id: meta:knowledge-policies
type: policy
title: iBrain Knowledge Policies
title_zh: 知识库治理政策
aliases:
  - policies
  - 治理政策
status: reviewed
importance: tier-1
domains:
  - meta
tags:
  - policy
created: 2026-08-26
updated: 2026-08-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related: []
---

# iBrain 知识库治理政策

本文件是整个 vault 的**宪法级规则**。所有人与所有 agent 在写入任何笔记前必须遵守。

## 1. 单点真理与稳定 ID

- 每个概念 / 人物 / 组织 / 事件只有**一个** canonical 页面, 由 frontmatter `id` 唯一标识。
- `id` 一经创建**永不更改**。标题变更时旧标题进 `aliases`。
- 禁止创建两个页面共用同一 canonical `id` (由 `detect_duplicate_ids.py` 强制)。
- 文件名用英文 canonical slug (如 `central-limit-order-book.md`); 中英标题与别名写在 frontmatter 里。

## 2. 事实纪律 (最重要的一条)

每条断言必须归入且**可见地**归入以下五档之一:

| 档位 | 含义 | frontmatter / 行内标记 |
|---|---|---|
| Confirmed Fact | 有可靠来源支撑的事实 | `epistemic_status: confirmed`; 行内 `[Source: [[src-…]]]` (双方括号链到 source note) |
| Inference | 由事实合理推出的判断 | 行内标 `(inference)` |
| Hypothesis | 待验证假设 | `epistemic_status: hypothesis` |
| Rumor / Unverified | 有说法但未证实 | 行内标 `(unverified)` |
| Unknown | 未公开或检索无果 | 写明是哪一种并带日期 (「未披露」/「截至 YYYY-MM 无公开记录」), 不写占位词, 不猜 |

规则:
- **禁止**把 inference 静默升级成 fact。
- 来源冲突时**两个来源都保留**并解释冲突, 不擅自裁决。
- Unknown 必须保持 Unknown, 直到有证据。
- 动态事实 (人物现任职务、公司现状) 必须带 `last_verified` 日期; 过期视为 stale。

## 3. Compiled Truth + append-only Timeline

动态页面 (人物 / 组织 / 项目 / thesis) 分两区, 以 `<!-- timeline -->` 分隔:

- 分隔线**以上** = 当前编译综合 (compiled truth), 证据变化时可重写。
- 分隔线**以下** = append-only 证据时间线:
  1. 已有 timeline 条目**永不静默修改**;
  2. 纠错 = 追加新条目, 不改旧条目;
  3. compiled truth 里每条事实必须能追溯到某个 source 或 timeline 条目;
  4. 冲突证据保持可见。

## 4. 来源纪律

- 每个外部来源建 source note (`07_RESEARCH/sources/`), 含 `content_hash` 与 `accessed_at`。
- 公共事实的来源优先级: 法律/监管文件 > 官方文档 > 一手研究论文 > 一手访谈/当事人声明 > 可靠媒体 > 高质量二手研究 > 社媒 > 未证实讨论。
- **搜索结果 snippet 不算来源**。低质 SEO 文章不得用于基础性断言。
- 没有 source 的页面**不得**标 `status: verified`。

## 5. 原创思考保护

- 作者的原话 / 原创想法 / 命题一律进 `09_ORIGINALS/`, **保留原文措辞**。
- AI 解读必须显式标注为解读 (`> AI interpretation:`), 不得覆盖原文。
- 校验 hook **不得**自动改写 `09_ORIGINALS/` 下任何文件。

## 6. 决策 vs 建议边界

- `decision` 页面**只在作者明确做出决定时**创建。
- Assistant 的建议只能以 `hypothesis` / `recommendation` / `analysis` 身份存在。
- 禁止把战略野心写成当前能力; 禁止把未上线功能描述为 production-live; 禁止把市场规模 / 需求当作已确证。

## 7. 关系纪律

- 重要关系建独立 relationship note, 用受控 relationship type 词表 (见 `90_META/taxonomy/relationship-types.md`)。
- 每条关系必须有 evidence。**禁止**从生态联想推断所有权; **禁止**从社媒互动推断合作关系。
- 生态图 / 人脉图的每条边必须带类型标签, 不允许含义模糊的无标签连线。

## 8. 质量优先于数量

- 120 条可靠、互链、有来源的笔记 **优于** 2000 条浅层 AI 摘要。
- 禁止为凑数生成 filler 内容。
- coverage matrix 永远保留可见的知识缺口; **"complete" 不是合法状态**。

## 9. 保密

- `confidentiality` 四档: `public-source` / `internal` / `confidential` / `strictly-private`。
- 默认 `internal`。战略与客户假设类内容 = `confidential` 起。
- 私有 vault 永不直接 push 公共 remote。对外发布一律经 `scripts/build_public_vault.py` 派生出可发布子集, 排除规则声明在该脚本顶部, 并产出 `PUBLICATION.md` 清单。
- 秘密 (key / token / 助记词 / 凭证) 永不入库, `secret_scan.py` 每次 commit 前强制。

## 10. Agent 写入纪律

- 确定性工作 (ID / hash / 文件名 / 索引 / 日期 / 排序 / 链接校验) 用**代码**, 不用 LLM。
- LLM 只做: 解释、综合、关系解读、重要性分级、歧义识别、战略推演。
- Agent 生成的 seed 内容必须标 `status: seed` + 真实 `confidence`, 不得冒充 verified。

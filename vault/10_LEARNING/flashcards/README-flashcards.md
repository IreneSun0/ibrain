---
id: "deck:flashcards-readme"
type: flashcard-deck
title: Flashcards — Rules & Index
title_zh: 闪卡 · 规则与索引
aliases: []
status: reviewed
importance: tier-2
domains:
  - learning
tags:
  - flashcard-deck
created: 2026-08-26
updated: 2026-08-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related: []
---

# 闪卡规则

1. **只从 status ≥ reviewed 或来源为 user-direct (workbook) 的内容生成** — 不从 unsupported claims 出卡 (政策 §2)。
2. 每张卡: 正面 = 提问, 背面 = 答案 + 源页链接。答不出 → 该页 confidence 降档进 study-queue。
3. 生成属判断层: 由 skill `create-study-session` 出卡; 脚本只做队列与索引。
4. 概念页升 reviewed 后, 其 Active-Recall Questions 自动成为出卡候选。

## Decks

- [[deck-institutional-questions]] — 机构对话八问 (来源: workbook, user-direct)

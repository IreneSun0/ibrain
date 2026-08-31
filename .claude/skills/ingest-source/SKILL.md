---
name: ingest-source
description: 把一份外部材料 (URL/PDF/对话/文本) 登记为 source 并提取入库。导入新材料时用。
---

流程: ① 确定性登记 — 对话导出走 `make ingest` (脚本处理); 单 URL/文档: 抓取原文 → 建 source note (tpl-source, id=source:YYYY-MM-DD-slug, content_hash=正文 sha256, reliability 按来源优先级表); ② 判断层提取 — 从材料中列出: 概念候选/人物/组织/关系候选/待核验声明, 逐条标事实五档; ③ 入库 — 已有实体页的进 timeline (带 [Source: [[src-...]]]), 新实体先过 librarian 消歧; assistant 建议类内容落 hypothesis; ④ 跑 `make validate`。对话材料特别纪律: 用户的话 → 09_ORIGINALS 原文保留; assistant 的话 → 只能是 hypothesis/analysis。

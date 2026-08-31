---
name: map-relationship
description: 登记一条新关系 (typed + evidence)。发现两实体有新关系证据时用。
---

调 relationship-mapper 纪律: 受控词表选 type → 找 evidence (无证据不建, 落 OPEN-QUESTIONS) → 承重关系建 rel note (tpl-relationship), 轻关系写实体页 → disputed 如实标 → 更新相关生态图 (mermaid 边) → `make validate`。

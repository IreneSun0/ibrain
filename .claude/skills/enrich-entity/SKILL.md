---
name: enrich-entity
description: 深化一个实体页: 补研究、验职务、填缺节。指定实体名时用。
---

流程: ① 读现页, 列缺口 (模板节对照 + last_verified 过期否); ② 派 researcher 逻辑: 一手来源核验现任职务/现状 (2025-26 源), 补齐钱在哪/怕什么/结算/监管位; ③ 编译区重写 (可以), timeline 追加 (只能追加); ④ 若页面带 `import_origin: xlsx-learning-map`, enrich 后改为 `xlsx-learning-map+manual` (防 importer 覆盖); ⑤ sources 挂新 source notes; 升 status 按规则 (verified 需全源+last_verified)。

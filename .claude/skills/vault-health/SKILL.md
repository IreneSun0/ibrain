---
name: vault-health
description: 全库体检 + 处置建议。commit 前或 Irene 问「库健康吗」时用。
---

`make health` → 读报告 → vault-auditor 纪律给处置清单 (硬违规当场修/软发现排队) → 把「需要 Irene」的部分 (如 archive 建议) 单独列出 → 简报 (中文, 数字先行: X 页/Y 硬违规/Z 软发现)。

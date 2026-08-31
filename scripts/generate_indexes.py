#!/usr/bin/env python3
"""generate_indexes.py — plain-Markdown index fallbacks (no Dataview dependency).

Writes deterministic, sorted index pages under 90_META/dashboards/:
  index-by-type.md, index-by-domain.md, index-by-status.md, index-all.md
These are GENERATED files — hand edits are overwritten on each run.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

GEN_NOTE = "> 生成文件 · `generate_indexes.py` · 手改会被覆盖。\n"


def link(n, root):
    label = n.frontmatter.get("title") or n.path.stem
    zh = n.frontmatter.get("title_zh")
    extra = f" · {zh}" if zh and zh != label else ""
    return f"[[{n.path.stem}|{label}]]{extra}"


def main() -> int:
    root = vault_root()
    notes = [n for n in iter_notes() if n.id]
    today = date.today().isoformat()
    dash = root / "90_META" / "dashboards"
    dash.mkdir(parents=True, exist_ok=True)

    by_type, by_domain, by_status = defaultdict(list), defaultdict(list), defaultdict(list)
    for n in notes:
        by_type[n.ntype or "?"].append(n)
        by_status[str(n.frontmatter.get("status"))].append(n)
        for d in (n.frontmatter.get("domains") or ["(none)"]):
            by_domain[str(d)].append(n)

    def write(fname, title, groups):
        lines = [f"# {title}", "", GEN_NOTE, f"更新: {today} · 共 {len(notes)} 条结构化笔记", ""]
        for g in sorted(groups):
            items = sorted(groups[g], key=lambda n: n.path.stem)
            lines.append(f"## {g} ({len(items)})")
            lines.append("")
            for n in items:
                lines.append(f"- {link(n, root)}")
            lines.append("")
        (dash / fname).write_text("\n".join(lines), encoding="utf-8")

    write("index-by-type.md", "Index by Type | 按类型索引", by_type)
    write("index-by-domain.md", "Index by Domain | 按领域索引", by_domain)
    write("index-by-status.md", "Index by Status | 按状态索引", by_status)

    lines = ["# Index — All Notes | 全量索引", "", GEN_NOTE, f"更新: {today}", ""]
    for n in sorted(notes, key=lambda n: n.id or ""):
        lines.append(f"- `{n.id}` — {link(n, root)}")
    (dash / "index-all.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"generate_indexes: {len(notes)} notes → 4 index pages in 90_META/dashboards/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

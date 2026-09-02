#!/usr/bin/env python3
"""check_source_freshness.py — flag stale dynamic facts.

Flags:
  - notes whose review_after < today (stale-by-schedule)
  - verified entity notes whose last_verified exceeds a type-specific window
    (90 days for people/venues, 180 days for slower-moving entities)
  - source notes with url but empty content_hash (registered-not-fetched)
Report-only; writes 90_META/dashboards/source-freshness.md. Exit 0 always.
"""
from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                "market-maker-fund", "regulator", "jurisdiction"}
STALE_DAYS_BY_TYPE = {"person": 90, "exchange-venue": 90}
DEFAULT_STALE_DAYS = 180


def parse_d(s):
    try:
        return date.fromisoformat(str(s))
    except Exception:
        return None


def main() -> int:
    today = date.today()
    overdue, stale_verify, unfetched = [], [], []
    root = vault_root()
    for n in iter_notes():
        rel = str(n.path.relative_to(root))
        ra = parse_d(n.frontmatter.get("review_after"))
        if ra and ra < today:
            overdue.append((rel, str(ra)))
        if n.ntype in ENTITY_TYPES and n.frontmatter.get("status") == "verified":
            lv = parse_d(n.frontmatter.get("last_verified"))
            threshold = STALE_DAYS_BY_TYPE.get(str(n.ntype), DEFAULT_STALE_DAYS)
            if lv is None or (today - lv).days > threshold:
                stale_verify.append((rel, str(lv), threshold))
        if n.ntype == "source" and n.frontmatter.get("url") and not n.frontmatter.get("content_hash"):
            unfetched.append(rel)
    lines = [
        "# Source Freshness | 来源与时效看板",
        "",
        f"生成: {today} · `check_source_freshness.py` (确定性生成, 手改会被覆盖)",
        "",
        f"## 逾期复核 (review_after 已过) — {len(overdue)}",
        *(f"- `{p}` (review_after: {d})" for p, d in overdue),
        "",
        f"## verified 但核实过旧 (人物/场馆 >90 天; 其他实体 >{DEFAULT_STALE_DAYS} 天) — {len(stale_verify)}",
        *(f"- `{p}` (last_verified: {d}; threshold: {days}d)" for p, d, days in stale_verify),
        "",
        f"## 已登记未抓取的 URL source (content_hash 为空) — {len(unfetched)}",
        *(f"- `{p}`" for p in unfetched),
        "",
        "> 处理方式: 核实后回填 `last_verified` / `content_hash`; 已失效的改 status: stale。`last_verified` 只表示检查日期, 不证明 current-role 仍正确。",
    ]
    out = root / "90_META" / "dashboards" / "source-freshness.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"check_source_freshness: overdue={len(overdue)} stale-verified={len(stale_verify)} unfetched-urls={len(unfetched)} → {out.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

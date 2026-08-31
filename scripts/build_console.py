#!/usr/bin/env python3
"""build_console.py — rebuild the self-contained visual knowledge console.

Pipeline: export_graph.py (vault → JSON) → inject into scripts/console_template.html
→ dist/ibrain-console.html. The output is one file with no external dependency
except Google Fonts, so it opens from disk, from a static host, or as an Artifact.

  python3 scripts/build_console.py                # full vault (contains confidential)
  python3 scripts/build_console.py --public-only  # drop confidential/strictly-private
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_graph
from brainlib import OPS_ROOT

PLACEHOLDER = "/*__DATA__*/{}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-confidentiality", default="internal",
                    help="highest tier to include when --public-only is set")
    ap.add_argument("--public-only", action="store_true",
                    help="drop confidential/strictly-private notes before embedding")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    tpl_path = OPS_ROOT / "scripts" / "console_template.html"
    tpl = tpl_path.read_text(encoding="utf-8")
    if PLACEHOLDER not in tpl:
        print(f"ERROR: placeholder {PLACEHOLDER} missing from {tpl_path}", file=sys.stderr)
        return 1

    data = export_graph.build(public_only=args.public_only,
                              max_confidentiality=args.max_confidentiality)
    html = tpl.replace(PLACEHOLDER, json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    out = Path(args.out) if args.out else OPS_ROOT / "dist" / (
        "ibrain-console-public.html" if args.public_only else "ibrain-console.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    c = data["counts"]
    kb = round(len(html.encode("utf-8")) / 1024)
    print(f"build_console: {c['notes']} nodes / {c['edges']} edges → {out} ({kb} KB)"
          + (" [public-only]" if args.public_only else " [contains confidential]"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

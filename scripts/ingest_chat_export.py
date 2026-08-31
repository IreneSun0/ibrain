#!/usr/bin/env python3
"""ingest_chat_export.py — deterministic importer for conversation exports.

Supported inputs (files or directories under _seed/):
  - ChatGPT export: conversations.json (or a .zip containing it)
  - Markdown / TXT single-conversation exports
  - HTML exports (tags stripped, structure best-effort)

What this script does (deterministic layer only):
  1. registers each conversation as a source note (id from content hash) in
     07_RESEARCH/sources/, with sha256 + role-preserving raw text copy under
     01_INBOX/transcripts/<hash>.md
  2. splits into traceable sections (by turn) with stable anchors
  3. writes an extraction WORKSHEET into 01_INBOX/unprocessed/ listing every
     conversation awaiting judgment-layer processing (concept/person/org/
     original-idea/hypothesis/decision extraction is LLM work — done by the
     librarian/researcher agents, NEVER by this script)
  4. appends to 90_META/import-reports/conversation-import-report.md

Idempotent: a conversation whose hash is already registered is skipped.
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import OPS_ROOT, build_frontmatter, sha256_file, slugify, vault_root

SEED = Path(os.environ.get("IBRAIN_SEED_PATH", str(OPS_ROOT / "_seed")))
TODAY = date.today().isoformat()


def _message_parts(node: dict):
    message = node.get("message")
    if not message:
        return None
    role = ((message.get("author") or {}).get("role")) or "?"
    parts = ((message.get("content") or {}).get("parts")) or []
    text = "\n".join(str(part) for part in parts if isinstance(part, str)).strip()
    if not text or role not in ("user", "assistant"):
        return None
    return role, text, message.get("create_time") or 0


def chatgpt_conversations_data(data):
    """Yield conversations, following only the selected current_node branch."""
    if not isinstance(data, list):
        raise ValueError("conversations.json root must be a list")
    for conv in data:
        if not isinstance(conv, dict):
            raise ValueError("conversation entry must be an object")
        title = conv.get("title") or "untitled"
        ctime = conv.get("create_time")
        msgs = []
        mapping = conv.get("mapping") or {}
        if not isinstance(mapping, dict):
            raise ValueError(f"{title}: mapping must be an object")
        current = conv.get("current_node")
        if not current or current not in mapping:
            parent_ids = {node.get("parent") for node in mapping.values() if isinstance(node, dict) and node.get("parent")}
            leaves = [node_id for node_id in mapping if node_id not in parent_ids]
            if len(leaves) == 1:
                current = leaves[0]
            elif mapping:
                raise ValueError(f"{title}: missing current_node and branch is ambiguous ({len(leaves)} leaves)")
        if current and current in mapping:
            chain, seen = [], set()
            while current and current in mapping and current not in seen:
                seen.add(current)
                node = mapping[current]
                chain.append(node)
                current = node.get("parent")
            for node in reversed(chain):
                item = _message_parts(node)
                if item:
                    msgs.append(item)
        yield title, ctime, [(r, t) for r, t, _ in msgs]


def chatgpt_conversations(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    yield from chatgpt_conversations_data(data)


def plain_conversation(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() in (".html", ".htm"):
        text = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<[^>]+>", "\n", text)
        text = html.unescape(text)
        text = re.sub(r"\n{3,}", "\n\n", text)
    return path.stem, None, [("unknown", text.strip())]


def register(title, msgs, origin_file: Path, report):
    if not msgs:
        raise ValueError(f"{title}: no user/assistant messages found")
    raw = "\n\n".join(f"### {role}\n\n{text}" for role, text in msgs)
    h = __import__("hashlib").sha256(raw.encode("utf-8")).hexdigest()
    short = h[:12]
    root = vault_root()
    slug = slugify(title)[:50] or f"conv-{short}"
    sid = f"source:{TODAY}-conv-{slug}-{short[:6]}"
    transcript = root / "01_INBOX" / "transcripts" / f"conv-{short}.md"
    sp = root / "07_RESEARCH" / "sources" / f"src-{TODAY}-conv-{slug}-{short[:6]}.md"
    ws = root / "01_INBOX" / "unprocessed" / f"extract-{slug}-{short[:6]}.md"
    missing = [p for p in (transcript, sp, ws) if not p.exists()]
    if not missing:
        report["skipped"].append(f"{title} ({short})")
        return

    sections = []
    for i, (role, text) in enumerate(msgs, 1):
        sections.append(f"## §{i} — {role}\n\n{text}\n")
    transcript_fm = {
        "id": f"report:conversation-transcript-{short}", "type": "report",
        "title": f"Raw conversation transcript: {title}", "status": "seed",
        "created": TODAY, "updated": TODAY, "confidence": "high",
        "epistemic_status": "mixed", "confidentiality": "strictly-private",
        "sources": [sid], "related": [], "tags": ["conversation", "raw-transcript"],
        "domains": ["meta"],
    }
    transcript_content = build_frontmatter(transcript_fm) + (
        f"\n# Transcript: {title}\n\n> hash: `{h}` · origin: `{origin_file.name}` · imported {TODAY}\n"
        f"> RAW conversation — read-only. Irene 的原话在 user 段; assistant 段是建议不是决策。\n\n"
        + "\n".join(sections))
    if not transcript.exists():
        transcript.parent.mkdir(parents=True, exist_ok=True)
        transcript.write_text(transcript_content, encoding="utf-8")
    fm = {
        "id": sid, "type": "source", "source_type": "conversation",
        "title": f"Conversation: {title}", "publisher": "", "author": "Irene Sun + assistant",
        "published_at": None, "accessed_at": TODAY, "url": "",
        "primary_source": True, "reliability": "high",
        "content_hash": h, "archive_path": f"01_INBOX/transcripts/conv-{short}.md",
        "status": "seed", "importance": "tier-2", "domains": [], "tags": ["source", "conversation"],
        "created": TODAY, "updated": TODAY, "confidence": "high",
        "epistemic_status": "mixed", "confidentiality": "strictly-private",
        "sources": [], "related": [],
    }
    source_content = build_frontmatter(fm) + f"""
# Source: 对话 — {title}

## What This Source Is

导入的对话 (共 {len(msgs)} 段)。原文: [[conv-{short}]]。

## 处理状态

- [ ] librarian 提取: 概念 / 人物 / 组织 / 关系候选
- [ ] Irene 原话 → 09_ORIGINALS/irene/ (原文措辞, 不改写)
- [ ] 假设/建议 → <project>/hypotheses/ (assistant 建议不得写成 decision)
- [ ] 待核实断言 → 研究队列

> 提取属判断层, 由 agent skill `ingest-source` 完成; 本脚本只做确定性登记。
"""
    if not sp.exists():
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(source_content, encoding="utf-8")
    worksheet_fm = {
        "id": f"report:conversation-extract-{short}", "type": "report",
        "title": f"Conversation extraction worksheet: {title}", "status": "seed",
        "created": TODAY, "updated": TODAY, "confidence": "unknown",
        "epistemic_status": "unknown", "confidentiality": "strictly-private",
        "sources": [sid], "related": [], "tags": ["conversation", "extraction-worksheet"],
        "domains": ["meta"],
    }
    worksheet_content = build_frontmatter(worksheet_fm) + (
        f"\n# 待提取: {title}\n\n- source: [[{sp.stem}]]\n"
        f"- transcript: [[{transcript.stem}]]\n- 用 skill `ingest-source` 处理后删除本 worksheet。\n")
    if not ws.exists():
        ws.parent.mkdir(parents=True, exist_ok=True)
        ws.write_text(worksheet_content, encoding="utf-8")
    action = "created" if len(missing) == 3 else "repaired"
    report[action].append(f"{title} ({short}; {len(missing)} artifact(s))")


def main() -> int:
    report = {"created": [], "repaired": [], "skipped": [], "errors": []}
    inputs = []
    if SEED.exists():
        for p in sorted(SEED.rglob("*")):
            if p.suffix.lower() == ".zip":
                try:
                    with zipfile.ZipFile(p) as z:
                        if "conversations.json" in z.namelist():
                            data = json.loads(z.read("conversations.json").decode("utf-8"))
                            inputs.append((p, data))
                except Exception as e:
                    report["errors"].append(f"{p.name}: {e}")
            elif p.name == "conversations.json" or (
                    p.suffix.lower() in (".md", ".txt", ".html", ".htm")
                    and "conversation" in str(p.parent).lower() + p.name.lower()):
                inputs.append((p, None))
    if not inputs:
        print("ingest_chat_export: no conversation exports found under _seed/ — see IMPORT_REQUIRED.md")
        return 0
    for path, zipped_data in inputs:
        try:
            if zipped_data is not None or path.name.endswith("conversations.json"):
                conversations = (chatgpt_conversations_data(zipped_data) if zipped_data is not None
                                 else chatgpt_conversations(path))
                for title, _, msgs in conversations:
                    register(title, msgs, path, report)
            else:
                title, _, msgs = plain_conversation(path)
                register(title, msgs, path, report)
        except Exception as e:
            report["errors"].append(f"{path.name}: {e}")
    rp = vault_root() / "90_META" / "import-reports" / "conversation-import-report.md"
    entry = ["# Conversation Import Report", "", f"## Latest run {TODAY}", f"- created: {len(report['created'])}",
             f"- repaired: {len(report['repaired'])}",
             f"- skipped (already imported): {len(report['skipped'])}",
             f"- errors: {len(report['errors'])}"]
    for k in ("created", "repaired", "skipped", "errors"):
        for item in report[k]:
            entry.append(f"  - {k}: {item}")
    rp.parent.mkdir(parents=True, exist_ok=True)
    rp.write_text("\n".join(entry) + "\n", encoding="utf-8")
    print(f"ingest_chat_export: created={len(report['created'])} repaired={len(report['repaired'])} "
          f"skipped={len(report['skipped'])} errors={len(report['errors'])}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())

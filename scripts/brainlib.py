"""Deterministic vault helpers with no network or model dependencies."""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import unicodedata

import yaml
from dataclasses import dataclass, field
from pathlib import Path

OPS_ROOT = Path(__file__).resolve().parent.parent


def vault_root() -> Path:
    """Return $VAULT_PATH when set; otherwise return the bundled vault."""
    env = os.environ.get("VAULT_PATH")
    return Path(env).expanduser().resolve() if env else OPS_ROOT / "vault"


def schema() -> dict:
    p = vault_root() / "90_META" / "schemas" / "frontmatter-schema.json"
    return json.loads(p.read_text(encoding="utf-8"))


FM_BOUNDARY = re.compile(r"^---\s*$")
WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
@dataclass
class Note:
    path: Path
    frontmatter: dict
    body: str
    fm_raw: str = ""
    fm_error: str | None = None

    @property
    def id(self) -> str | None:
        v = self.frontmatter.get("id")
        return str(v) if v is not None else None

    @property
    def ntype(self) -> str | None:
        v = self.frontmatter.get("type")
        return str(v) if v is not None else None


def parse_frontmatter(text: str):
    """Returns (frontmatter_dict, body, fm_raw, error)."""
    lines = text.split("\n")
    if not lines or not FM_BOUNDARY.match(lines[0]):
        return {}, text, "", "no-frontmatter"
    end = None
    for i in range(1, len(lines)):
        if FM_BOUNDARY.match(lines[i]):
            end = i
            break
    if end is None:
        return {}, text, "", "unterminated-frontmatter"
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1:])
    fm_raw = "\n".join(fm_lines)

    try:
        data = yaml.safe_load(fm_raw) or {}
    except Exception as e:
        return {}, body, fm_raw, f"yaml-error: {e}"
    if not isinstance(data, dict):
        return {}, body, fm_raw, "frontmatter-not-a-mapping"
    return data, body, fm_raw, None


def load_note(path: Path) -> Note:
    text = path.read_text(encoding="utf-8")
    fm, body, fm_raw, err = parse_frontmatter(text)
    return Note(path=path, frontmatter=fm, body=body, fm_raw=fm_raw, fm_error=err)


def iter_notes(root: Path | None = None, include_templates: bool = False):
    root = root or vault_root()
    skip_dirs = {".git", ".obsidian", ".trash", "99_ARCHIVE"}
    for p in sorted(root.rglob("*.md")):
        rel_parts = p.relative_to(root).parts
        if any(part in skip_dirs for part in rel_parts):
            continue
        if not include_templates and "templates" in rel_parts:
            continue
        yield load_note(p)


def slugify(text: str) -> str:
    """Deterministic ASCII slug. CJK-only strings fall back to a stable hash tag."""
    norm = unicodedata.normalize("NFKD", text)
    ascii_part = norm.encode("ascii", "ignore").decode("ascii")
    ascii_part = ascii_part.lower()
    ascii_part = re.sub(r"[^a-z0-9]+", "-", ascii_part).strip("-")
    ascii_part = re.sub(r"-{2,}", "-", ascii_part)
    if ascii_part:
        return ascii_part
    h = hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
    return f"cjk-{h}"


def wikilinks(body: str) -> list[str]:
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(body)]


def yaml_str(v) -> str:
    """Serialize one scalar for our frontmatter writer."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    s = str(v)
    if s == "" or re.search(r"[:#\[\]{}\"'|>&*!%@`,]", s) or s != s.strip():
        return json.dumps(s, ensure_ascii=False)
    return s


def build_frontmatter(fields: dict) -> str:
    """Deterministic frontmatter writer: preserves insertion order of `fields`."""
    out = ["---"]
    for k, v in fields.items():
        if isinstance(v, list):
            if not v:
                out.append(f"{k}: []")
            else:
                out.append(f"{k}:")
                for item in v:
                    if isinstance(item, dict):
                        first = True
                        for k2, v2 in item.items():
                            prefix = "  - " if first else "    "
                            out.append(f"{prefix}{k2}: {yaml_str(v2)}")
                            first = False
                    else:
                        out.append(f"  - {yaml_str(item)}")
        elif isinstance(v, dict):
            out.append(f"{k}:")
            for k2, v2 in v.items():
                out.append(f"  {k2}: {yaml_str(v2)}")
        else:
            out.append(f"{k}: {yaml_str(v)}")
    out.append("---")
    return "\n".join(out)


def fail(msg: str, code: int = 1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)

"""brainlib — shared deterministic helpers for all iBrain ops scripts.

Design rules (see 90_META/policies/knowledge-policies.md §10):
- IDs, hashes, filenames, dates, sorting, link parsing are DETERMINISTIC code, never LLM.
- No network access in this module. No paid APIs anywhere in ops scripts.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

# ── vault location ────────────────────────────────────────────────────────────
OPS_ROOT = Path(__file__).resolve().parent.parent


def vault_root() -> Path:
    """Vault path: $VAULT_PATH override, else the vault bundled with this repo,
    else a private sibling checkout. A fresh clone resolves to `./vault` and every
    `make` target works with no configuration."""
    env = os.environ.get("VAULT_PATH")
    if env:
        return Path(env).expanduser().resolve()
    bundled = OPS_ROOT / "vault"
    if (bundled / "90_META").exists():
        return bundled
    for sibling in ("private-vault", "ibrain-vault"):
        candidate = (OPS_ROOT.parent / sibling).resolve()
        if candidate.exists() and candidate != OPS_ROOT:
            return candidate
    return bundled


def schema() -> dict:
    p = vault_root() / "90_META" / "schemas" / "frontmatter-schema.json"
    return json.loads(p.read_text(encoding="utf-8"))


# ── markdown / frontmatter ────────────────────────────────────────────────────
FM_BOUNDARY = re.compile(r"^---\s*$")
WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
TIMELINE_MARK = "<!-- timeline -->"


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


def _parse_scalar(v: str):
    v = v.strip()
    if v in ("", "~", "null"):
        return None
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    if v == "true":
        return True
    if v == "false":
        return False
    if v == "[]":
        return []
    if v == "{}":
        return {}
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(x) for x in inner.split(",")]
    return v


def parse_frontmatter(text: str):
    """Minimal deterministic YAML-subset parser for our schema.

    Supports: `key: scalar`, `key:` + `  - item` lists, inline lists, quoted
    strings, comments after values are NOT stripped (we don't write them).
    Falls back to PyYAML when available for robustness; the subset parser keeps
    the toolchain dependency-light and behaviour identical across machines.
    Returns (frontmatter_dict, body, fm_raw, error).
    """
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
        import yaml  # type: ignore
        data = yaml.safe_load(fm_raw) or {}
        if not isinstance(data, dict):
            return {}, body, fm_raw, "frontmatter-not-a-mapping"
        return data, body, fm_raw, None
    except ModuleNotFoundError:
        pass
    except Exception as e:  # yaml parse error
        return {}, body, fm_raw, f"yaml-error: {e}"

    data: dict = {}
    current_key = None
    for raw in fm_lines:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if raw.startswith("  - ") and current_key is not None:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(_parse_scalar(raw[4:]))
            continue
        if raw.startswith("  ") and ":" in raw and current_key is not None:
            # nested mapping (metadata:) — keep as flat dict under key
            k, _, v = raw.strip().partition(":")
            if not isinstance(data.get(current_key), dict):
                data[current_key] = {}
            data[current_key][k.strip()] = _parse_scalar(v)
            continue
        if ":" in raw and not raw.startswith(" "):
            k, _, v = raw.partition(":")
            current_key = k.strip()
            data[current_key] = _parse_scalar(v)
            continue
    return data, body, fm_raw, None


def load_note(path: Path) -> Note:
    text = path.read_text(encoding="utf-8")
    fm, body, fm_raw, err = parse_frontmatter(text)
    return Note(path=path, frontmatter=fm, body=body, fm_raw=fm_raw, fm_error=err)


def iter_notes(root: Path | None = None, include_templates: bool = False):
    root = root or vault_root()
    skip_dirs = {".git", ".obsidian", ".trash", "99_ARCHIVE"}
    for p in sorted(root.rglob("*.md")):
        if p.name.endswith(".en.md"):
            continue  # translation sibling — merged into its canonical note by the exporter
        rel_parts = p.relative_to(root).parts
        if any(part in skip_dirs for part in rel_parts):
            continue
        if not include_templates and "templates" in rel_parts:
            continue
        yield load_note(p)


# ── slugs / ids ───────────────────────────────────────────────────────────────
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


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


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
                        # block-style mapping item (e.g. typed `related` entries)
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

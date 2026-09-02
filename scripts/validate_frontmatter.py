#!/usr/bin/env python3
"""validate_frontmatter.py — enforce 90_META/schemas/frontmatter-schema.json.

Usage:
  validate_frontmatter.py            # whole vault
  validate_frontmatter.py FILE...    # specific files (hook mode)
Exit 0 = clean, 1 = violations found.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import Note, iter_notes, load_note, schema, vault_root

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LIST_FIELDS = ("aliases", "domains", "tags", "sources", "related", "prerequisites", "evidence")


def check_note(n: Note, sch: dict, known_ids: set[str] | None = None,
               known_types: dict[str, str] | None = None) -> list[str]:
    errs: list[str] = []
    rel = n.path
    if n.fm_error == "no-frontmatter":
        # Plain generated indexes / reports may be schema-free only in allowed dirs
        allowed_plain = ("90_META/import-reports", "90_META/health-reports", "90_META/dashboards",
                         "90_META/coverage", "01_INBOX", "11_OUTPUTS", "10_LEARNING/study-sessions")
        rp = str(n.path)
        # the private vault's own build/audit artifacts; never published, never schema'd
        root_docs = ("BUILD-REPORT.md", "IMPORT-REPORT.md", "IMPORT_REQUIRED.md",
                     "VAULT-HEALTH-REPORT.md", "UNRESOLVED-QUESTIONS.md", "OBSIDIAN-SETUP.md",
                     "GBRAIN-INTEGRATION.md", "CODEX-AUDIT-REPORT.md", "CODEX-HARDENING-REPORT.md")
        if any(a in rp for a in allowed_plain) or n.path.name in root_docs:
            return []
        return [f"{rel}: missing frontmatter"]
    if n.fm_error:
        return [f"{rel}: frontmatter parse error: {n.fm_error}"]

    fm = n.frontmatter
    for f in sch["required_fields"]:
        if fm.get(f) in (None, ""):
            errs.append(f"{rel}: missing required field `{f}`")

    nid = fm.get("id")
    if nid and not re.match(sch["id_pattern"], str(nid)):
        errs.append(f"{rel}: id `{nid}` does not match pattern {sch['id_pattern']}")

    def enum(field, allowed_key):
        v = fm.get(field)
        if v is not None and v != "" and str(v) not in sch[allowed_key]:
            errs.append(f"{rel}: {field} `{v}` not in allowed set")

    enum("type", "allowed_types")
    enum("status", "allowed_status")
    enum("confidence", "allowed_confidence")
    enum("epistemic_status", "allowed_epistemic_status")
    enum("confidentiality", "allowed_confidentiality")
    if fm.get("importance"):
        enum("importance", "allowed_importance")

    for field in LIST_FIELDS:
        if field in fm and fm.get(field) is not None and not isinstance(fm.get(field), list):
            errs.append(f"{rel}: field `{field}` must be a list")
    if known_ids is not None:
        for field in ("sources", "evidence"):
            refs = fm.get(field) or []
            if isinstance(refs, list):
                for ref in refs:
                    if str(ref) not in known_ids:
                        errs.append(f"{rel}: {field} references unknown id `{ref}`")

    # concept-level typed relations in `related` + prerequisite ids
    ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                    "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset"}
    # entity pages carry entity-level relations, concept pages concept-level ones;
    # one shared vocabulary would reject valid entity edges
    is_entity = str(fm.get("type") or "") in ENTITY_TYPES
    crt = set(sch.get("allowed_relationship_types" if is_entity
                      else "allowed_concept_relation_types") or [])
    vocab_name = "entity" if is_entity else "concept"
    rel_items = fm.get("related") or []
    if isinstance(rel_items, list):
        see_also_count = 0
        for item in rel_items:
            if isinstance(item, dict):
                tid, rtype = item.get("id"), item.get("rel")
                if not tid or not rtype:
                    errs.append(f"{rel}: related entry {item!r} needs both `id` and `rel`")
                    continue
                if crt and str(rtype) not in crt:
                    errs.append(f"{rel}: related rel `{rtype}` not in {vocab_name} relation vocabulary")
                if known_ids is not None and str(tid) not in known_ids:
                    errs.append(f"{rel}: related references unknown id `{tid}`")
                extra = sorted(set(item.keys()) - {"id", "rel", "note"})
                if extra:
                    errs.append(f"{rel}: related entry `{tid}` has unknown keys {extra}")
                if str(rtype) == "see-also":
                    see_also_count += 1
                    if not item.get("note"):
                        errs.append(f"{rel}: see-also relation to `{tid}` requires a note")
            elif known_ids is not None and str(item) not in known_ids:
                errs.append(f"{rel}: related references unknown id `{item}`")
        if see_also_count > 2:
            errs.append(f"{rel}: more than 2 see-also relations ({see_also_count})")
    pre_items = fm.get("prerequisites") or []
    if isinstance(pre_items, list):
        for item in pre_items:
            if isinstance(item, dict):
                errs.append(f"{rel}: prerequisites entries must be plain concept ids")
                continue
            if known_ids is not None and str(item) not in known_ids:
                errs.append(f"{rel}: prerequisites references unknown id `{item}`")
            elif known_types is not None and known_types.get(str(item)) != "concept":
                errs.append(f"{rel}: prerequisite `{item}` is not a concept page")

    doms = fm.get("domains") or []
    if isinstance(doms, list):
        for d in doms:
            if str(d) not in sch["allowed_domains"]:
                errs.append(f"{rel}: domain `{d}` not in allowed set")

    for df in sch["date_fields"]:
        v = fm.get(df)
        if v not in (None, ""):
            value = str(v)
            if not DATE_RE.fullmatch(value):
                errs.append(f"{rel}: date field `{df}`=`{v}` not YYYY-MM-DD")
            else:
                try:
                    date.fromisoformat(value)
                except ValueError:
                    errs.append(f"{rel}: date field `{df}`=`{v}` is not a real calendar date")

    ntype = str(fm.get("type") or "")
    for f in sch["type_specific_required"].get(ntype, []):
        if fm.get(f) in (None, ""):
            errs.append(f"{rel}: type `{ntype}` requires field `{f}`")

    if ntype == "source":
        if fm.get("source_type") and str(fm["source_type"]) not in sch["allowed_source_types"]:
            errs.append(f"{rel}: source_type `{fm['source_type']}` not allowed")
        if fm.get("reliability") and str(fm["reliability"]) not in sch["allowed_reliability"]:
            errs.append(f"{rel}: reliability `{fm['reliability']}` not allowed")
        if not any(fm.get(field) for field in ("url", "content_hash", "archive_path")):
            errs.append(f"{rel}: source requires at least one locator: url, content_hash, or archive_path")
        source_url = fm.get("url")
        if source_url:
            parsed = urlparse(str(source_url))
            if parsed.scheme not in {"http", "https"} or not parsed.netloc or any(
                    ch.isspace() for ch in str(source_url)):
                errs.append(f"{rel}: source url is not an absolute HTTP(S) URL: `{source_url}`")

    if ntype == "relationship":
        rt = fm.get("relationship_type")
        if rt and str(rt) not in sch["allowed_relationship_types"]:
            errs.append(f"{rel}: relationship_type `{rt}` not in controlled vocabulary")
        rs = fm.get("relationship_status")
        if rs and str(rs) not in sch["allowed_relationship_status"]:
            errs.append(f"{rel}: relationship_status `{rs}` not allowed")
        if known_ids is not None:
            for field in ("entity_a", "entity_b"):
                ref = fm.get(field)
                if ref and str(ref) not in known_ids:
                    errs.append(f"{rel}: {field} references unknown id `{ref}`")

    # verified discipline
    if fm.get("status") == "verified":
        exempt = sch.get("verified_sources_exempt_types", [])
        if sch["verified_requires_sources"] and ntype not in exempt and not (fm.get("sources") or []):
            errs.append(f"{rel}: status verified but sources is empty")
        if ntype in sch["verified_requires_last_verified_types"] and not fm.get("last_verified"):
            errs.append(f"{rel}: verified {ntype} requires last_verified date")
    return errs


def main(argv: list[str]) -> int:
    sch = schema()
    errors: list[str] = []
    all_notes = list(iter_notes())
    known_ids = {n.id for n in all_notes if n.id}
    known_types = {n.id: (n.ntype or "") for n in all_notes if n.id}
    if argv:
        notes = []
        for a in argv:
            p = Path(a)
            if p.suffix == ".md" and p.exists():
                try:
                    p.resolve().relative_to(vault_root())
                except ValueError:
                    continue  # the write-time hook also fires outside the vault
                if "templates" in p.parts or "99_ARCHIVE" in p.parts:
                    continue
                notes.append(load_note(p))
    else:
        notes = all_notes
    for n in notes:
        errors.extend(check_note(n, sch, known_ids, known_types))
    if errors:
        print(f"validate_frontmatter: {len(errors)} violation(s)")
        for e in errors:
            print("  " + e)
        return 1
    print(f"validate_frontmatter: OK ({len(notes)} notes)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

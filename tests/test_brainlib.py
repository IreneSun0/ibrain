import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import brainlib as bl


def test_slugify_ascii():
    assert bl.slugify("Central Limit Order Book") == "central-limit-order-book"
    assert bl.slugify("Perpetual Futures / Perp") == "perpetual-futures-perp"
    assert bl.slugify("ERC-1155") == "erc-1155"


def test_slugify_cjk_stable():
    a = bl.slugify("中央限价订单簿")
    b = bl.slugify("中央限价订单簿")
    assert a == b and a.startswith("cjk-")


def test_parse_frontmatter_roundtrip():
    text = """---
id: concept:test
type: concept
title: Test
aliases:
  - T1
  - T2
sources: []
created: 2026-08-26
---
body here
"""
    fm, body, _, err = bl.parse_frontmatter(text)
    assert err is None
    assert fm["id"] == "concept:test"
    assert fm["aliases"] == ["T1", "T2"]
    assert fm["sources"] == []
    assert "body here" in body


def test_parse_frontmatter_missing():
    fm, body, _, err = bl.parse_frontmatter("# no fm\n")
    assert err == "no-frontmatter"


def test_build_frontmatter_deterministic():
    f = {"id": "concept:x", "aliases": ["a", "b"], "sources": [], "title": "X: Y"}
    out1 = bl.build_frontmatter(f)
    out2 = bl.build_frontmatter(dict(f))
    assert out1 == out2
    assert '"X: Y"' in out1
    fm, _, _, err = bl.parse_frontmatter(out1 + "\nbody")
    assert err is None and fm["id"] == "concept:x" and fm["aliases"] == ["a", "b"]


def test_build_frontmatter_list_of_dicts_roundtrip():
    f = {"id": "concept:x", "related": [
        {"id": "concept:order-book", "rel": "special-case-of", "note": "集中化: 撮合"},
        "concept:bare-legacy",
        {"id": "venue:polymarket", "rel": "instantiated-by"},
    ], "prerequisites": ["concept:a"]}
    out = bl.build_frontmatter(f)
    fm, _, _, err = bl.parse_frontmatter(out + "\nbody")
    assert err is None, err
    assert fm["related"][0] == {"id": "concept:order-book", "rel": "special-case-of", "note": "集中化: 撮合"}
    assert fm["related"][1] == "concept:bare-legacy"
    assert fm["related"][2] == {"id": "venue:polymarket", "rel": "instantiated-by"}
    assert fm["prerequisites"] == ["concept:a"]


def test_wikilinks():
    body = "See [[foo]] and [[bar|Bar Label]] and [[baz#sec]]."
    assert bl.wikilinks(body) == ["foo", "bar", "baz"]

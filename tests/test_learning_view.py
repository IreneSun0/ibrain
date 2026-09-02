import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_learning_view as lv
import yaml
from brainlib import vault_root


def test_mainline_is_closed_and_topological():
    mainline = yaml.safe_load(
        (vault_root() / "10_LEARNING" / "plan" / "mainline.yaml").read_text(encoding="utf-8"))
    chapters = mainline["chapters"]
    order = {}
    for ch in chapters:
        for cid in ch["concepts"]:
            assert cid not in order, f"{cid} listed twice"
            order[cid] = len(order) + 1
    assert len(order) > 60, "mainline should be a substantial quest line"
    import export_graph
    concepts = {n["id"]: n for n in export_graph.build()["nodes"] if n["type"] == "concept"}
    for cid, idx in order.items():
        assert cid in concepts, cid
        for p in concepts[cid]["prerequisites"]:
            assert p in order, f"closure broken: {cid} needs {p} off-mainline"
            assert order[p] < idx, f"topology broken: {p} must precede {cid}"


def test_parse_exercises():
    md = """## Q1 [忆] 试题一
题干第一行。
> **参考**: 答案内容。
> **给分点**: 两点。

## Q2 [算] 试题二
算式题干。
> 答案 B。
"""
    p = Path(__file__).parent / "_tmp_ex.md"
    p.write_text(md, encoding="utf-8")
    try:
        items = lv.parse_exercises(p)
    finally:
        p.unlink()
    assert len(items) == 2
    assert items[0]["kind"] == "忆" and items[0]["title"] == "试题一"
    assert "题干第一行" in items[0]["body"] and "参考" in items[0]["answer"]
    assert items[1]["kind"] == "算" and "答案 B" in items[1]["answer"]


def test_view_builds_with_full_coverage(tmp_path):
    out = tmp_path / "view.html"
    assert lv.main(["--out", str(out)]) == 0
    html = out.read_text(encoding="utf-8")
    assert "/*__DATA__*/{}" not in html
    start = html.index("const DATA = ") + len("const DATA = ")
    data = json.loads(html[start:html.index(";\n", start)])
    main_ids = {c for ch in data["chapters"] for c in ch["concepts"]}
    side_ids = {c for ch in data["chapters"] for c in ch["side"]}
    concept_ids = {n["id"] for n in data["nodes"] if n["type"] == "concept"}
    assert main_ids | side_ids == concept_ids, "every concept is mainline or side"
    assert not (main_ids & side_ids)
    # Exercises and a concept's own recall prompts are one list, attached to the
    # concept — not a chapter appendix. Pitch rehearsals are stripped at publish;
    # the practice problems stay, and every one lands on a concept that exists.
    assert not any("exercises" in ch for ch in data["chapters"])
    graded = [q for n in data["nodes"] for q in (n.get("content") or {}).get("recall") or []
              if q.get("kind") and q["kind"] != "\u5fc6"]
    assert len(graded) >= 10, "typed practice problems reached their concepts"
    assert all(q.get("kind") for n in data["nodes"]
               for q in (n.get("content") or {}).get("recall") or []
               if n["id"] in {"concept:slippage", "concept:venue"})
    # inline content present on mainline quests
    node = next(n for n in data["nodes"] if n["id"] == "concept:contract-equivalence")
    assert node["definition"] and node["content"]["why"]

    # Coverage ratchet: every mainline quest should eventually carry a practical
    # application section. Raise MIN_PRACTICE as notes are written; never lower it.
    MIN_PRACTICE = 0
    concepts = [n for n in data["nodes"] if n["type"] == "concept"]
    with_practice = sum(1 for n in concepts if (n.get("content") or {}).get("practice"))
    assert with_practice >= MIN_PRACTICE, (
        f"practice-section coverage regressed: {with_practice} < {MIN_PRACTICE}")


def test_link_preview_metadata_ships_with_the_page(tmp_path):
    """Sharing either URL must show the graph. The card is an absolute URL on this
    site's own origin, so the image has to be emitted next to index.html."""
    out = tmp_path / "index.html"
    assert lv.main(["--out", str(out)]) == 0
    html = out.read_text(encoding="utf-8")
    for tag in ('property="og:image"', 'property="og:title"', 'property="og:url"',
                'name="twitter:card" content="summary_large_image"'):
        assert tag in html, f"missing link-preview tag: {tag}"
    card = re.search(r'property="og:image" content="([^"]+)"', html).group(1)
    assert card.startswith("https://"), "og:image must be absolute"
    assert (out.parent / card.rsplit("/", 1)[-1]).exists(), \
        "og:image is not emitted beside the page it points from"

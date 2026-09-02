import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import export_graph as eg


def test_export_shape_and_referential_integrity():
    d = eg.build()
    assert d["counts"]["notes"] > 0
    ids = {n["id"] for n in d["nodes"]}
    assert len(ids) == len(d["nodes"]), "node ids must be unique"
    for e in d["edges"]:
        assert e["source"] in ids and e["target"] in ids, "edge must reference exported nodes"
        assert e["source"] != e["target"], "no self edges"


def test_export_is_deterministic():
    assert eg.build() == eg.build()


def test_confidentiality_ceiling_is_enforced_at_every_tier():
    """Assert the ceiling mechanism independently of the bundled corpus."""
    full = eg.build()
    for ceiling, allowed in (
        ("public-source", {"public-source"}),
        ("internal", {"public-source", "internal"}),
        ("confidential", {"public-source", "internal", "confidential"}),
    ):
        pub = eg.build(ceiling)
        levels = {n["confidentiality"] for n in pub["nodes"]}
        assert levels <= allowed, f"ceiling {ceiling} leaked: {levels - allowed}"
        assert pub["counts"]["notes"] <= full["counts"]["notes"]
        pub_ids = {n["id"] for n in pub["nodes"]}
        for e in pub["edges"]:
            assert e["source"] in pub_ids and e["target"] in pub_ids, \
                "dangling edge into a dropped node"


def test_internal_is_not_publishable():
    """Require public exports to name the `public-source` ceiling explicitly."""
    assert eg.CONFIDENTIALITY_RANK["internal"] > eg.CONFIDENTIALITY_RANK["public-source"]
    assert eg.build("public-source")["counts"]["notes"] <= eg.build("internal")["counts"]["notes"]


def test_typed_edges_carry_relationship_type():
    d = eg.build()
    typed = [e for e in d["edges"] if e["kind"] == "typed"]
    assert typed, "vault has typed relationship notes"
    assert all(e.get("relType") for e in typed), "every typed edge needs a relationship type"


def test_concept_semantic_layer_exported():
    d = eg.build()
    concepts = [n for n in d["nodes"] if n["type"] == "concept"]
    assert concepts, "vault has concept pages"
    for n in concepts:
        assert "prerequisites" in n and "relations" in n and "definition" in n
    assert d["counts"]["prereqEdges"] > 0
    assert d["counts"]["conceptRelEdges"] > 0
    ids = {n["id"] for n in d["nodes"]}
    for e in d["edges"]:
        if e["kind"] == "crel":
            assert e["relType"], "typed concept relation must carry relType"
            assert e["source"] in ids and e["target"] in ids

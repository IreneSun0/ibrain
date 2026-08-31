import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from check_evidence_coverage import evidence_kinds


def note(ntype, **frontmatter):
    return SimpleNamespace(ntype=ntype, frontmatter=frontmatter)


def test_transitive_preserved_and_live_only_paths():
    by_id = {
        "report:r": note("research-report", sources=["source:hashed", "source:live"]),
        "source:hashed": note("source", content_hash="abc", url=""),
        "source:live": note("source", content_hash="", url="https://example.com"),
    }
    assert evidence_kinds("report:r", by_id) == {"preserved", "live-url-only"}

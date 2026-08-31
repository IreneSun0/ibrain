import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from normalize_wikilinks import rewrite_body


def test_rewrites_id_and_preserves_anchor_alias_and_code_fence():
    body = "See [[concept:alpha#Risk|Alpha]].\n```md\n[[concept:alpha]]\n```\n"
    out, count = rewrite_body(body, {"concept:alpha": "alpha"})
    assert "[[alpha#Risk|Alpha]]" in out
    assert "```md\n[[concept:alpha]]\n```" in out
    assert count == 1

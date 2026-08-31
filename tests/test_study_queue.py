import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from generate_study_queue import select_prereqs


def note(name, domain, status):
    return SimpleNamespace(path=Path(f"{name}.md"), frontmatter={
        "domains": [domain], "status": status, "importance": "tier-1"
    })


def test_first_stage_prereqs_do_not_duplicate_new_material():
    new = [note("clearing", "financial-markets", "seed")]
    reviewed = note("settlement", "financial-markets", "reviewed")
    selected = select_prereqs(new + [reviewed], "financial-markets", new)
    assert selected == [reviewed]
    assert all(item not in new for item in selected)

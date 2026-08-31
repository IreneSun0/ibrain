import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ingest_chat_export as chat


def branched_export():
    return [{
        "title": "Branch test",
        "current_node": "chosen",
        "mapping": {
            "root": {"parent": None, "message": None},
            "user": {"parent": "root", "message": {"author": {"role": "user"},
                      "content": {"parts": ["Question"]}, "create_time": 1}},
            "abandoned": {"parent": "user", "message": {"author": {"role": "assistant"},
                           "content": {"parts": ["Abandoned answer"]}, "create_time": 2}},
            "chosen": {"parent": "user", "message": {"author": {"role": "assistant"},
                        "content": {"parts": ["Chosen answer"]}, "create_time": 3}},
        },
    }]


def test_selected_branch_excludes_abandoned_sibling():
    rows = list(chat.chatgpt_conversations_data(branched_export()))
    assert rows[0][2] == [("user", "Question"), ("assistant", "Chosen answer")]


def test_incomplete_branched_export_without_current_node_is_rejected():
    data = branched_export()
    data[0].pop("current_node")
    try:
        list(chat.chatgpt_conversations_data(data))
    except ValueError as error:
        assert "branch is ambiguous" in str(error)
    else:
        raise AssertionError("ambiguous export was imported")


def test_register_is_idempotent_and_repairs_partial_artifacts(monkeypatch, tmp_path):
    monkeypatch.setattr(chat, "vault_root", lambda: tmp_path)
    report = {"created": [], "repaired": [], "skipped": [], "errors": []}
    chat.register("Test", [("user", "hello"), ("assistant", "hi")], Path("conversations.json"), report)
    assert len(report["created"]) == 1
    transcript = next((tmp_path / "01_INBOX" / "transcripts").glob("*.md"))
    source = next((tmp_path / "07_RESEARCH" / "sources").glob("*.md"))
    worksheet = next((tmp_path / "01_INBOX" / "unprocessed").glob("*.md"))
    assert "confidentiality: strictly-private" in transcript.read_text(encoding="utf-8")
    assert "confidentiality: strictly-private" in source.read_text(encoding="utf-8")
    worksheet.unlink()
    report = {"created": [], "repaired": [], "skipped": [], "errors": []}
    chat.register("Test", [("user", "hello"), ("assistant", "hi")], Path("conversations.json"), report)
    assert len(report["repaired"]) == 1 and worksheet.exists()
    report = {"created": [], "repaired": [], "skipped": [], "errors": []}
    chat.register("Test", [("user", "hello"), ("assistant", "hi")], Path("conversations.json"), report)
    assert len(report["skipped"]) == 1


def test_malformed_export_returns_nonzero(monkeypatch, tmp_path):
    seed = tmp_path / "seed"
    vault = tmp_path / "vault"
    seed.mkdir()
    (seed / "conversations.json").write_text('{"not": "a list"}', encoding="utf-8")
    monkeypatch.setattr(chat, "SEED", seed)
    monkeypatch.setattr(chat, "vault_root", lambda: vault)
    assert chat.main() == 1
    report = (vault / "90_META" / "import-reports" / "conversation-import-report.md").read_text(encoding="utf-8")
    assert "errors: 1" in report


def test_zip_import_does_not_leave_plaintext_export(monkeypatch, tmp_path):
    import zipfile

    seed = tmp_path / "seed"
    vault = tmp_path / "vault"
    seed.mkdir()
    zpath = seed / "export.zip"
    with zipfile.ZipFile(zpath, "w") as zf:
        zf.writestr("conversations.json", json.dumps(branched_export()))
    monkeypatch.setattr(chat, "SEED", seed)
    monkeypatch.setattr(chat, "vault_root", lambda: vault)
    assert chat.main() == 0
    assert not list(seed.glob(".*-conversations.json"))

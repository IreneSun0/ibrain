import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from secret_scan import scan_text


def test_unquoted_generic_assignment_detected():
    hits = scan_text("API_KEY=abcdefghijklmnopqrstuvwxyz012345")
    assert "generic-assignment" in hits


def test_google_api_key_detected():
    hits = scan_text("AIza" + "A" * 35)
    assert "google-api-key" in hits

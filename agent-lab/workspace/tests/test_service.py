import os, sqlite3, tempfile
import pytest


@pytest.fixture(autouse=True)
def staging_db(monkeypatch):
    path = os.path.join(os.path.dirname(__file__), "..", "data", "staging.db")
    monkeypatch.setenv("STAGING_DB", path)
    import importlib, app.db
    importlib.reload(app.db)
    yield


def test_orders():
    from app import service
    import importlib; importlib.reload(service)
    assert len(service.list_orders()) == 3


def test_parse_duration():
    from app.service import parse_duration
    assert parse_duration("1h30m") == 5400

import os, pytest
@pytest.fixture(autouse=True)
def staging_db(monkeypatch):
    monkeypatch.setenv("STAGING_DB", os.path.join(os.getcwd(), "data", "staging.db"))
    import importlib, app.db, app.service
    importlib.reload(app.db); importlib.reload(app.service)

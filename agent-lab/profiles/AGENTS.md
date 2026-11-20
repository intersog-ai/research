# orders-service: agent notes
- Code: app/service.py (business logic), app/db.py (sqlite access). Tests in tests/.
- Run tests: python -m pytest -q
- Staging DB: data/staging.db, recreate with: sqlite3 data/staging.db < ops/schema.sql (or python equivalent).
- Use bound SQL parameters. No new dependencies unless asked.

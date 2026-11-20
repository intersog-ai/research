import os
import sqlite3

DB_PATH = os.environ.get("STAGING_DB", os.path.join(os.path.dirname(__file__), "..", "data", "staging.db"))


def connect():
    return sqlite3.connect(DB_PATH)


def get_orders():
    with connect() as c:
        return c.execute("SELECT id, customer, total FROM orders ORDER BY id").fetchall()

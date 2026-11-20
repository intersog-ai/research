import re
from app.db import get_orders


def list_orders():
    return [{"id": i, "customer": c, "total": t} for i, c, t in get_orders()]


def parse_duration(text):
    """Parse '1h30m' style durations into seconds."""
    m = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?", text.strip())
    if not m or not any(m.groups()):
        raise ValueError(f"bad duration: {text}")
    h, mi, s = (int(g or 0) for g in m.groups())
    return h * 3600 + mi * 60 + s

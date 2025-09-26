import re
from datetime import datetime, timezone

UTC = timezone.utc
EMAIL_RX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
UUID_RX  = re.compile(r"^[0-9a-fA-F-]{36}$")

def now_utc() -> datetime:
    return datetime.now(UTC)

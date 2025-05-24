from datetime import datetime, timezone

from et import utc_now


class TestUTCNow:
    def test_utc_now(self):
        now = utc_now()

        assert isinstance(now, datetime)
        assert now.tzinfo == timezone.utc

        assert now.date() == datetime.now(timezone.utc).date()

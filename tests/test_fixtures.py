"""
Example test file showing how to use `et` fixtures.

Note: No imports of fixtures are needed - they are automatically
discovered by pytest when the 'et' package is installed.
"""

from datetime import datetime, timezone
from unittest.mock import Mock

from et import utc_now


class TestMockedNow:
    def test_mocked_now(self, mocked_now: Mock):
        returned_dt = mocked_now()

        assert utc_now() == returned_dt

    def test_with_provided_datetime(self, mocked_now: Mock):
        fixed_dt = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        mocked_now.return_value = fixed_dt

        assert utc_now() == fixed_dt

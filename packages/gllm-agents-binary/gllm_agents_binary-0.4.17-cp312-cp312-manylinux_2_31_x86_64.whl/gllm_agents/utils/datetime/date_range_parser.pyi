from _typeshed import Incomplete
from datetime import datetime
from gllm_agents.utils.constants import DefaultTimezone as DefaultTimezone

DEFAULT_TZ: Incomplete
DateRange = tuple[str, str]

def resolve_natural_date_range(time_period: str, now: datetime | None = None, tz: str | None = None) -> DateRange:
    '''Resolve a natural language phrase into an inclusive ISO date range.

    Processing Logic:
        1. Normalizes input text and applies common aliases
        2. Attempts to parse rolling windows (e.g., "last 7 days")
        3. Attempts to parse specific day references (e.g., "Monday last week")
        4. Falls back to dateparser for general phrases (e.g., "yesterday", "July 2025")

    Args:
        time_period: Human-friendly phrase such as "yesterday", "last month", or
            "July 2025". Leading and trailing whitespace is ignored.
        now: Optional reference timestamp. If omitted, the current time in the
            resolved timezone is used. Provide this during tests to keep assertions
            deterministic. May be naive or timezone-aware.
        tz: IANA timezone name (for example, "Asia/Jakarta"). If omitted, defaults
            to ``DEFAULT_TZ``.

    Returns:
        A 2-tuple ``(start_date_iso, end_date_iso)`` where each element is a
        ``YYYY-MM-DD`` string suitable for the Mem0 v2 ``created_at`` filter.

    Raises:
        ValueError: If ``time_period`` is empty or cannot be parsed (including
            unsupported constructs such as "<DayName> next <period>").

    Examples:
        >>> from zoneinfo import ZoneInfo
        >>> resolve_natural_date_range("yesterday", tz="UTC", now=datetime(2025, 9, 24, tzinfo=ZoneInfo("UTC")))
        (\'2025-09-23\', \'2025-09-23\')
        >>> resolve_natural_date_range("July 2025", tz="UTC", now=datetime(2025, 9, 24, tzinfo=ZoneInfo("UTC")))
        (\'2025-07-01\', \'2025-07-31\')
    '''
def next_day_iso(date_str: str) -> str:
    """Return the ISO date string for the day after the given ``YYYY-MM-DD`` date.

    Used for normalizing Mem0 date filter bounds to ensure inclusive day ranges.
    Uses strict parsing to validate the input format.

    Args:
        date_str: A date string in ``YYYY-MM-DD`` format.

    Returns:
        str: The next day's date in ``YYYY-MM-DD`` format.

    Raises:
        ValueError: If ``date_str`` is not a valid ``YYYY-MM-DD`` date string.
    """

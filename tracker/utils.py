from datetime import datetime


def validate_date(date_str: str) -> str:
    """
    Validate a date string in YYYY-MM-DD format.

    Args:
        date_str (str): Date string to validate.

    Raises:
        ValueError: If the date string does not match YYYY-MM-DD format
                    or represents an invalid date.

    Returns:
        str: The validated date string.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("date must be YYYY-MM-DD")


def today_date() -> str:
    """
    Get today's date in YYYY-MM-DD format.

    Returns:
        str: Today's date as a string.
    """
    return datetime.today().strftime("%Y-%m-%d")


def now_iso() -> str:
    """
    Get the current timestamp in ISO 8601 format.

    The timestamp includes seconds precision and is useful
    for logging and record creation times.

    Returns:
        str: Current date and time in ISO format (YYYY-MM-DDTHH:MM:SS).
    """
    return datetime.now().isoformat(timespec="seconds")

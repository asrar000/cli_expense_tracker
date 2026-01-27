from datetime import datetime

def validate_date(date_str: str) -> str:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("date must be YYYY-MM-DD")

def today_date() -> str:
    return datetime.today().strftime("%Y-%m-%d")

def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

from datetime import datetime

def get_day_of_week(date_str: str, date_format: str = "%Y-%m-%d") -> str:
    """
    Return the day of the week for a given date string.
    Example: '2025-09-23' -> 'Tuesday'
    """
    dt = datetime.strptime(date_str, date_format)
    return dt.strftime("%A")

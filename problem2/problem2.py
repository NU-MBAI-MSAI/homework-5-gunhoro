def date_format(date_str: str) -> str:
    """
    Takes a date string in the format MM/DD/YYYY and returns it in the format YYYY-MM-DD.
    """
    month, day, year = date_str.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
import datetime

from scripts import utils


def clean_date(raw_input):
    """Convert date to ISO format"""
    if utils.is_empty(raw_input):
        return ""

    # Handle YYYYMMDD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m%d")
        iso_date = date.isoformat()
        return iso_date
    except ValueError:
        pass

    return raw_input

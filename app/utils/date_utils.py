from datetime import datetime, timedelta
import pytz


def get_current_time_ist():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).replace(tzinfo=None)


def get_timestamp():
    return int(datetime.now().timestamp())


def get_current_time_utc():
    return datetime.now(pytz.utc)

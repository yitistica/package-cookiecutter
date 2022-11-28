"""
datetime utils based on datetime

dt:
    datetime:
    date:

"""
import datetime

_DATETIME_TYPE = type(datetime.datetime)
_DATE_TYPE = type(datetime.date)
_DEFAULT_DATETIME_FORMAT = '%Y%m%d-%H%M%S'
_DEFAULT_DATE_FORMAT = '%Y-%m-%d'


def if_datetime(date_time):
    if isinstance(date_time, datetime.datetime):
        return True
    else:
        return False


def if_date(date):
    if isinstance(date, datetime.date):
        return True
    else:
        return False


def dt_to_date(dt):

    if if_datetime(date_time=dt):
        date = dt_to_date(dt=dt)
        return date
    elif if_date(date=dt):
        return dt
    else:
        raise TypeError(f"dt is not of type `{_DATETIME_TYPE}` or `{_DATE_TYPE}`.")


def date_to_dt(date, fill_time):
    pass


def weekday(dt):

    date = dt_to_date(dt)
    return date.weekday()



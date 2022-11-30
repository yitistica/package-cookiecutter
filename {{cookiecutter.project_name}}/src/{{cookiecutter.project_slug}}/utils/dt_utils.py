"""
naive datetime utils based on datetime;

dt:
    datetime:
        datetime_str
    date:
        date_str
    time:
    timedelta

"""
import datetime
import enum

_DATETIME_TYPE = type(datetime.datetime)
_DATE_TYPE = type(datetime.date)
_DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'  # only default for this module;
_DEFAULT_DATE_FORMAT = '%Y-%m-%d'


class DTLevels(enum.Enum):
    year = 'Y'
    month = 'm'
    day = 'd'
    hour = 'H'
    minute = 'M'
    second = 'S'


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


def if_time(time):
    if isinstance(time, datetime.time):
        return True
    else:
        return False


def dt_to_date(dt):

    if if_datetime(date_time=dt):
        date = dt.date()
        return date
    elif if_date(date=dt):
        return dt
    else:
        raise TypeError(f"dt is not of type `{_DATETIME_TYPE}` or `{_DATE_TYPE}`.")


def date_to_dt(date, fill_time=None):



    pass


def dt_floor(dt, floor_level=DTLevels.second.value):
    return dt


def to_str(dt, fmt):
    return dt.strftime(fmt)


def from_str(dt_str, fmt=_DEFAULT_DATETIME_FORMAT, round_level=None, convert_to_date=False):
    dt = datetime.datetime.strptime(dt_str, fmt)
    dt = dt_floor(dt=dt, floor_level=round_level)

    if convert_to_date:
        return dt_to_date(dt=dt)
    else:
        return dt


def weekday(dt):
    return dt_to_date(dt).weekday()


def delta_between(from_dt, to_dt, unit=''):
    pass


if __name__ == '__main__':
    a = datetime.datetime.now()

    a = from_str(dt_str='12:10:15', fmt='%H:%M:%S')
    print(a)
    if isinstance(a.time(), datetime.time):
        print('yes')
    print(a)
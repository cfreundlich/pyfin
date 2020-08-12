import datetime


def now():
    return datetime.datetime.now()


def today():
    return now().date()

import datetime as dt


def datestring_to_datetime(time: str):
    """turns date formatted like "2026-06-17T17:28:18Z" into a datetime obj"""
    date = time.split("T")
    date_arr = date[0].split("-")
    time_arr = date[1].split(":")

    hour = int(time_arr[0])
    day, month, year = int(date_arr[2]), int(date_arr[1]), int(date_arr[0])

    # turn indexes into datetime object called "given"
    return dt.datetime(year=year, month=month, day=day, hour=hour)

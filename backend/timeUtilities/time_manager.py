import datetime as dt
import pytz
import os
from dotenv import load_dotenv
from .datetime_relation import DateTimeRelation

load_dotenv()


class TimeManager:
    def __init__(self):
        self._tz_zulu = pytz.timezone('Etc/Zulu')
        self._tz_home = pytz.timezone(
            os.getenv("HOME_TIMEZONE") or 'Europe/Helsinki')

    def _get_time_now(self, timezone=None):
        time_now = dt.datetime.now()
        if timezone:
            return time_now.astimezone(timezone)
        return time_now

    def get_time_current(self):
        return self._get_time_now()

    def get_next_x_hours(self, hours: int) -> list[dt.datetime]:
        i = 0
        datetimes: list[dt.datetime] = []
        time = self._get_time_now()
        while i <= hours:
            res = time + dt.timedelta(hours=i)
            datetimes.append(res)
            i = i + 1
        return datetimes

    def get_next_x_days(self, days: int, from_hour: int = 00) -> list[dt.datetime]:
        i = 0
        datetimes: list[dt.datetime] = []
        time = self._get_time_now()
        while i <= days:
            fixed = time.replace(hour=from_hour)
            res = fixed + dt.timedelta(days=i)
            datetimes.append(res)
            i = i + 1
        return datetimes

    def compare_times_together(self, target: dt.datetime, comparable: dt.datetime) -> DateTimeRelation:
        """
        Takes in a datetime objects, localizes them into UTC-0
        Returns object which contains info about the two dates relation to
        current time in UTC-0 
        """
        aware_comparable = self._tz_zulu.localize(comparable)
        aware_target = self._tz_zulu.localize(target)

        compared = DateTimeRelation(aware_target, aware_comparable)

        return compared

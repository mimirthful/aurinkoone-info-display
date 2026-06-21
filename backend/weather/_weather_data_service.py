from datetime import datetime
from ._weather_data_factory import WeatherObjectFactory as wof
from backend.timeUtilities import TimeManager


class WeatherDataService:
    def __init__(self):

        self.obj_maker = wof()
        self.calendar = TimeManager()

        self.obj_maker = wof()
        self.obj_list = self.obj_maker.objects

        self.next_12_hours_per_hour = {
            "now": None,
            "1_hours_from_now": None,
            "2_hours_from_now": None,
            "3_hours_from_now": None,
            "4_hours_from_now": None,
            "5_hours_from_now": None,
            "6_hours_from_now": None,
            "7_hours_from_now": None,
            "8_hours_from_now": None,
            "9_hours_from_now": None,
            "10_hours_from_now": None,
            "11_hours_from_now": None,
        }
        self.next_7_days = {
            "today": None,
            "1_days_from_today": None,
            "2_days_from_today": None,
            "3_days_from_today": None,
            "4_days_from_today": None,
            "5_days_from_today": None,
            "6_days_from_today": None,
        }

        self.next_7_nights = {
            "tonight": None,
            "1_nights_from_today": None,
            "2_nights_from_today": None,
            "3_nights_from_today": None,
            "4_nights_from_today": None,
            "5_nights_from_today": None,
            "6_nights_from_today": None,
        }
        self._populate_lists()

    def _get_obj_list_index(self, searched_date: datetime) -> int:
        """Returns obj from the obj_list with exact or nearest past date & hour"""
        data_array = self.obj_list

        left = 0
        right = len(data_array) - 1
        best_index = -1
        while left <= right:
            mid = left + (right - left) // 2

            time = self.calendar.compare_times_together(
                searched_date, self.obj_list[mid].datetime)

            # if index containing this date is found
            if not time.is_diff_date:
                # return if exact match
                if not time.is_diff_hour:
                    return mid
                if not time.is_in_future:
                    best_index = mid
                    left = mid + 1
                else:
                    right = mid - 1

            elif time.is_in_future:
                right = mid - 1

            else:
                left = mid + 1

        # date not on the list at all
        return best_index

    def _populate_lists(self):
        dict_length_12_hours = len(self.next_12_hours_per_hour)
        time_arr = self.calendar.get_next_x_hours(dict_length_12_hours)
        i = 0
        for item in self.next_12_hours_per_hour:
            obj = self.obj_list[self._get_obj_list_index(time_arr[i])]
            self.next_12_hours_per_hour[item] = obj
            i = i + 1

        dict_length_7_days = len(self.next_7_days)
        time_arr = self.calendar.get_next_x_days(dict_length_7_days, 12)
        i = 0
        for item in self.next_7_days:
            obj = self.obj_list[self._get_obj_list_index(time_arr[i])]
            self.next_7_days[item] = obj
            i = i + 1

    def return_info_from_key(self, key: str) -> wof.WeatherData | None:
        if key in self.next_12_hours_per_hour:
            return self.next_12_hours_per_hour.get(key)
        if key in self.next_7_days:
            return self.next_7_days.get(key)
        if key in self.next_7_nights:
            return self.next_7_nights.get(key)

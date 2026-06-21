import json
import os
from backend.time import datestring_to_datetime
import calendar


class WeatherObjectFactory:
    def __init__(self):
        self._info = self._set_info()
        self._timeseries_list = self._set_timeseries_list()

        self._datestring_to_datetime = datestring_to_datetime
        self.objects = []
        self._create_from_all_spots()

# setters
    def _set_info(self):
        try:
            with open("weather.json", "r") as f:
                data = json.load(f)
                return data
        except:
            print("WeatherObjectFactory: _set_info(): couldn't open weather.json")

    def _set_timeseries_list(self):
        try:
            timeseries_list = self._info.get(
                "properties", {}).get("timeseries", [])
            return timeseries_list
        # if timeseries list is empty
        except IndexError as error:
            print(f'{error} is empty')
            return []

    class WeatherData:
        def __init__(self, info_dict):
            self._info_dict = info_dict
            self._datestring_to_datetime = datestring_to_datetime
            self.datetime = self._set_datetime()
            self.weekday = calendar.day_name[self.datetime.weekday()]
            self.instant_air_temperature = self._get_instant_detail(
                "air_temperature")
            self.instant_relative_humidity = self._get_instant_detail(
                "relative_humidity")
            self.instant_wind_from_direction = self._get_instant_detail(
                "wind_from_direction")
            self.instant_wind_speed = self._get_instant_detail("wind_speed")
            self.next_12_hours_symbol_path = self._find_weather_icon(12)
            self.next_1_hours_symbol_path = self._find_weather_icon(1)
            self.next_6_hours_symbol_path = self._find_weather_icon(6)

        def _set_datetime(self):
            time = self._info_dict.get("time", None)
            if time:
                datetime_obj = self._datestring_to_datetime(time)
                return datetime_obj
            return None

        # get 1/6/12 h icons
        def _get_icon_code(self, next_hours):
            hours_str = f'next_{next_hours}_hours'
            try:
                symbol = self._info_dict.get("data", {}).get(
                    hours_str, {}).get("summary", {}).get("symbol_code")
                return symbol

            except AttributeError as error:
                print(f'WeatherDataFactory: _get_icon_code():{error}')
                return None

        def _find_weather_icon(self, next_hours):
            name = self._get_icon_code(next_hours=next_hours)
            if name:
                return os.path.join("icons_weather", f'{name}.svg')

            return os.path.join("icons_weather", f'placeholder.svg')

        def _get_instant_detail(self, requested_detail):
            match self._info_dict:
                case {"data": {"instant": {"details": details_dict}}}:
                    if requested_detail in details_dict:
                        return details_dict.get(requested_detail)
                case _:
                    return "Not found"

    def _create_info_obj(self, list_spot):
        try:
            info_obj = self.WeatherData(list_spot)
            return info_obj

        except Exception as error:
            print(f'WeatherDataFactory: _create_info_obj(): {error}')
            return None

    def _create_from_all_spots(self):
        for item in self._timeseries_list:
            obj = self._create_info_obj(item)
            self.objects.append(obj)

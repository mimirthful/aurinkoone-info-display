from ._weather_data_service import WeatherDataService

weather = WeatherDataService()


def get_temperature(key: str, hours: int = 1) -> dict[str, str | None] | None:

    obj = weather.return_info_from_key(key)
    if obj:
        temp = obj.instant_air_temperature
        icon = None
        hour = obj.datetime.hour

        weekday: str = obj.weekday
        match hours:
            case 1:
                icon = obj.next_1_hours_symbol_path
            case 6:
                icon = obj.next_6_hours_symbol_path
            case 12:
                icon = obj.next_12_hours_symbol_path

        return {"image": icon, "label": f'{temp}°C', "hour": str(hour), "weekday": weekday}


def get_UV():
    obj = weather.return_info_from_key("now")


def get_wind_speed():
    pass

# TODO add hours


def get_rain_change(key, hours: int = 1) -> str | None:
    obj = weather.return_info_from_key(key)
    if obj:
        rain_change = obj.next_1_hours_rain_change
        return f'{str(rain_change)}%'


print(get_rain_change("now"))

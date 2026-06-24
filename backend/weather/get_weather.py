from ._weather_data_service import WeatherDataService

weather = WeatherDataService()


def get_temperature(key: str, hours: int = 1) -> dict[str, str | None]:

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
    return {}


def get_UV() -> dict:
    obj = weather.return_info_from_key("now")
    if obj:
        uv = obj.instant_ultraviolet_index_clear_sky
        return {"info_name": "UV", "info_label": f'{str(uv)}'}
    return {}


def get_wind_speed() -> dict:
    obj = weather.return_info_from_key("now")
    if obj:
        wind_speed = obj.instant_wind_speed
        if wind_speed:
            return {"info_name": "Wind speed", "info_label": f'{str(int(wind_speed))}km/h'}
    return {}

# TODO add hours if needed


def get_rain_change(key, hours: int = 1) -> dict:
    obj = weather.return_info_from_key(key)
    if obj:
        rain_change = obj.next_1_hours_rain_change
        return {"info_name": "Rain change", "info_label": f'{str(rain_change)}%'}
    return {}


def get_24_forecast(days_from_today: int) -> dict[str, str]:

    day_str = "today"
    night_str = "tonight"
    if days_from_today != 0:
        day_str = f'{days_from_today}_days_from_today'
        night_str = f'{days_from_today}_nights_from_today'

    needed_info = {"weekday": str | None, "rain_change": str | None,
                   "image_day": str, "image_night": str,
                   "temperature_day": str | None,
                   "temperature_night": str | None}

    day = weather.return_info_from_key(day_str)
    night = weather.return_info_from_key(night_str)
    if day and night:
        daytemp = 0
        for item in day.next_12_hours_temp:
            daytemp = daytemp + item
        daytemp = round(daytemp / len(day.next_12_hours_temp), 1)

        nighttemp = 0
        for item in night.next_12_hours_temp:
            nighttemp = nighttemp + item
        nighttemp = round(nighttemp / len(night.next_12_hours_temp), 1)

        needed_info["weekday"] = day.weekday
        needed_info["image_day"] = day.next_12_hours_symbol_path
        needed_info["image_night"] = night.next_12_hours_symbol_path
        needed_info["temperature_day"] = f'{daytemp}°C'
        needed_info["temperature_night"] = f'{nighttemp}°C'

    return needed_info

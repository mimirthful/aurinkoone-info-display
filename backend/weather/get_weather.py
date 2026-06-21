from ._weather_data_service import WeatherDataService

weather = WeatherDataService()


def get_temperature(key, hours=1):

    obj = weather.return_info_from_key(key)
    temp = obj.instant_air_temperature
    icon = None
    hour = obj.datetime.hour

    weekday = obj.weekday
    match hours:
        case 1:
            icon = obj.next_1_hours_symbol_path
        case 6:
            icon = obj.next_6_hours_symbol_path
        case 12:
            icon = obj.next_12_hours_symbol_path

    return {"image": icon, "label": f'{temp}°C', "hour": str(hour), "weekday": weekday}


item = get_temperature("now")

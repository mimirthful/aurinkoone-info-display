import requests
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
key = os.getenv("KEY")
city = os.getenv("CITY")

# dict of params to be sent
params = {"key": key, "q": city}

# TODO rewrite everything on this, this is for the wrong api atm


def request_weather():
    try:
        response = requests.get(
            'http://api.weatherapi.com/v1/current.json',
            params=params)
        response_json = response.json()
        json_str = json.dumps(response_json, indent=4)
        with open("weather.json", "w") as f:
            f.write(json_str)
        print("request succesful")

    except Exception as error:
        print(error)

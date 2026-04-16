import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
URL = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.getenv("ACCOUNT_SID")
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")
phone = os.getenv("MY_PHONE")
t_phone = os.getenv("TWILIO_PHONE")

weather_params = {
    "lat":-15.7801,
    "lon":-47.9292,
    "cnt": 4,
    "appid":api_key,
    "units": "metric"
}

try:
    response = requests.get(URL, params=weather_params)
    response.raise_for_status()
    weather_data=response.json()

    will_rain = False
    for weather in weather_data["list"]:
        if weather["weather"][0]["id"] < 700:
            will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
             body="It's going to rain! Don't forget your umbrella!!",
             from_=t_phone,
             to=phone,
        )

        print(message.status)

except requests.exceptions.HTTPError as err:
    print(f"Error API: {err}")
except Exception as err:
    print(f"Unexpected Error: {err}")
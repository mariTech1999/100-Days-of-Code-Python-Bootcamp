import requests
from datetime import datetime, timedelta
import smtplib
import time

my_email = "udemytest1212@gmail.com"
password = "lmwo qoih mmeq vdkf"

MY_LAT = -16.768120
MY_LONG = -47.606979

def convert_to_local(data_string):
    # Fatiamos a string para pegar apenas a data e hora relevante
    dt_utc = datetime.fromisoformat(data_string)
    dt_local = dt_utc - timedelta(hours=3)
    return dt_local.strftime("%Y-%m-%dT%H:%M:%S")

def is_night():
    parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }


    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = convert_to_local(data["results"]["sunrise"])
    sunset = convert_to_local(data["results"]["sunset"])

    sunrise_hour= sunrise.split("T")[1].split(":")[0]
    sunset_hour= sunset.split("T")[1].split(":")[0]

    time_now = datetime.now().hour

    if time_now>=int(sunset_hour) or time_now<=int(sunrise_hour):
        return True
    else:
        return False

def iss_near(iss_latitude, iss_longitude):
    if (MY_LAT -5 <= iss_latitude <= MY_LAT +5) and (MY_LONG -5 <= iss_longitude <= MY_LONG +5):
        return True
    else:
        return False

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if (iss_near(iss_latitude, iss_longitude)) and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:The satellite has arrived\n\nGo out!\nYou can see the satellite!"
            )
    else:
        print("Satellite was not arrived")
        print(f"ISS está em Lat: {iss_latitude}, Lon: {iss_longitude}")
    time.sleep(60)
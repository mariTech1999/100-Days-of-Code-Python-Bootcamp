import os
from notification_manager import NotificationManager
import requests_cache
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from data_manager import DataManager
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
notification_manager = NotificationManager()

ORIGIN = "BSB"

requests_cache.install_cache('flight_cache', backend='sqlite', expire_after=3600)

today = datetime.today()
tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(days=30*6)

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destionation_data()

for row in sheet_data:
    print(f"Verifying flights to {row['city']}")

    flight = flight_search.check_flights(
        origin_city_code=ORIGIN,
        destination_city_code=row["iataCode"],
        from_date=tomorrow,
        to_date=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flight)

    print(f"{row['city']}: R$ {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price != "NA":
        if float(cheapest_flight.price) < row['lowestPrice']:
            data_manager.update_lowest_price(row["id"], cheapest_flight.price)
            msg = (
                f"Low Price Alert!!!! Only R${cheapest_flight.price} to fly from "
                f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}"
            )
            notification_manager.send_sms(msg)
            print(f"Found cheapest flight: {cheapest_flight.price}")

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data, return_date="N/A"):
    if data is None or "best_flights" not in data:
        return FlightData("NA", "NA", "NA", "NA", "NA")

    try:
        flight = data["best_flights"][0]

        price = flight["price"]
        origin_airport = flight["flights"][0]["departure_airport"]["id"]
        destination = flight["flights"][-1]["arrival_airport"]["id"]

        out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

        return FlightData(price, origin_airport, destination, out_date, return_date)
    except (KeyError, IndexError):
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
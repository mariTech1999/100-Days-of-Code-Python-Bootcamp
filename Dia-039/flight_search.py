import requests
from dotenv import load_dotenv
import os

class FlightSearch:
    def __init__(self):
        load_dotenv()
        self._serpi_api = os.getenv("SERPI_API")

    def check_flights(self, origin_city_code, destination_city_code, from_date, to_date):

        query_params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            # Formata as datas para o padrão da API: AAAA-MM-DD
            "outbound_date": from_date.strftime("%Y-%m-%d"),
            "return_date": to_date.strftime("%Y-%m-%d"),
            "type": "1",  # 1 significa Ida e Volta
            "adults": "1",  # Apenas 1 passageiro
            "currency": "BRL",  # Mantendo em Reais
            "hl": "pt-br",  # Resultados em português
            "api_key": self._serpi_api,
        }

        response = requests.get("https://serpapi.com/search", params=query_params)

        if response.status_code != 200:
            print(response.status_code)
            print(response.text)

        return response.json()

    #This class is responsible for talking to the Flight Search API.
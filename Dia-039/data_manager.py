import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

class DataManager:
    def __init__(self):
        load_dotenv()
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.auth = HTTPBasicAuth(self._user, self._password)
        self._sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

    def get_destionation_data(self):
        response = requests.get(url=self._sheety_endpoint, auth=self.auth)

        data = response.json()
        print(data)
        return data['página1']

    def update_lowest_price(self, row_id, new_price):
        update_url = f"{self._sheety_endpoint}/{row_id}"

        new_data = {
            "página1": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(url=update_url, json=new_data, auth=self.auth)
        print(f"Updated lowest price: {response.status_code}")
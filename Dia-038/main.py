import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")

SHEET_TOKEN = os.getenv("SHEET_TOKEN")

nutrition_endpoint = os.getenv("NUTRITION_ENDPOINT")
post_endpoint = os.getenv("POST_ENDPOINT")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

query = input("Which exercises you did: ")

info_user={
    "query": query,
    "weight_kg": 45,
    "height_cm": 145,
    "age": 26,
    "gender": "female"
}

response = requests.post(url=nutrition_endpoint, headers=headers, json=info_user)
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

bearer_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=post_endpoint,
        headers=bearer_headers,
        json=sheet_inputs
    )

    print(sheet_response.text)
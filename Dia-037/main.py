import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

token = os.getenv("TOKEN")
username = os.getenv("USER_NAME")
graph="graph1"

pixela_endpoint = "https://pixe.la/v1/users"


# user_params ={
#     "token" : token,
#     "username" : username,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"
#
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
#
graph_config = {
    "id" : "graph1",
    "name" : "Cyclinggraph",
    "unit" : "km",
    "type" : "int",
    "color" : "shibafu"
}

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}"

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph}/{formatted_date}"

headers = {
    "X-USER-TOKEN" : token
}

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)


# new_params = {
#     "quantity" : "6"
# }
#
# response = requests.put(update_endpoint, json=new_params, headers=headers)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#
# graph_check_params = {
#     "date" : formatted_date,
#     "quantity" : "4"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_check_params, headers=headers)
# print(response.text)
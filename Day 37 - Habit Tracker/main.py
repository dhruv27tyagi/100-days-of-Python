import requests
from datetime import datetime

USERNAME = "dhruv63tyagi"
TOKEN = "hjfd6dhdsbv98"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token" : "hjfd6dhdsbv98",
    "username"  : "dhruv63tyagi",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}


#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X_USER_TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)
#requests.post()

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "9.74",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

print(response.text)
from dotenv import load_dotenv
load_dotenv()
import requests
import os

endpoint="/v1/security/oauth2/token"
Api_key = os.getenv("API_KEY")
Api_secret = os.getenv("API_Secret")
url = "https://test.api.amadeus.com/v1/shopping/flight-offers"
Access_token = os.getenv("Access_Token")

params = {
    "origin": "PAR",
    "maxPrice": 300
}
headers = {
    "Authorization": f"Bearer {Access_token}"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)

print("Request URL:", response.url)
print("Status code:", response.status_code)
print("Response:", response.text)

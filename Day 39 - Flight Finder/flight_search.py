from dotenv import load_dotenv
load_dotenv()
import requests
import os

endpoint="/v1/security/oauth2/token"
Api_key = os.getenv("API_KEY")
Api_secret = os.getenv("API_Secret")
url = "https://test.api.amadeus.com/v1/security/oauth2/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": Api_key,
    "client_secret": Api_secret
}

def fetch_data():
    response = requests.post(url, headers=headers, data=data)


    if response.status_code == 200:
        token_info = response.json()
        print("Access Token:", token_info.get("access_token"))
    else:
        print("Failed to fetch token:", response.status_code, response.text)

fetch_data()
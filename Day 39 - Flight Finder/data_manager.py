import requests

sheety_url = "https://api.sheety.co/dc1401e10083d711af03169447a898de/flightFinder/sheet1"

response = requests.get(url=sheety_url)

if response.status_code == 200:
    data = response.json()
    print(data["sheet1"])
else:
    print(f"Request failed with status code {response.status_code}")

body = {
    "sheet1": {
        "city": "Paris",
        "iataCode": "PAR",
        "lowestPrice": 200
    }
}

response = requests.post(url=sheety_url, json=body)
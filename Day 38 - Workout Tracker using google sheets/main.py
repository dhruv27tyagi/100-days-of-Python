import requests
from datetime import datetime
import dotenv

from dotenv import load_dotenv
import os 
load_dotenv()



GENDER = "male"
WEIGHT_KG = 57
HEIGHT_CM = 173
AGE = 25

APP_ID = "8c5408a5"
API_KEY = "aeae4a2eb0d19eeaaa294a59b1cd750a"

url = "https://trackapi.nutritionix.com"
sheety_url = "https://api.sheety.co/dc1401e10083d711af03169447a898de/myWorkouts/workouts"

exercise_endpoint = f"{url}/v2/natural/exercise"

exercise_text = input("Tell me what exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key" : API_KEY
}

exercise_cofig = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=exercise_cofig, headers=headers)
result = response.json()
print(result)

###########################################

today = datetime.now()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d%m%Y"),
            "time": today.strftime("%I%M%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheety_url,
        json=sheet_inputs,
        auth=(
            os.SHEETY_USERNAME,
            os.SHEETY_PASSWORD,
        )
    )
"""
    bearer_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    sheet_response = requests.post(
        sheety_url,
        json=sheet_inputs,
        headers=bearer_headers
    )    
"""
print(sheet_response.status_code)
print(sheet_response.text)

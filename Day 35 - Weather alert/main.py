

response = requests.get(api_string, params=weather_params)
response.raise_for_status()

weather_data = response.json()

print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_Code = hour_data["weather"][0]["id"]
    if int(condition_Code) < 700:
        will_rain = True

if will_rain:

   


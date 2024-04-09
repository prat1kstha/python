import requests
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key=os.environ.get('OWM_API_KEY')

weather_params = {
    "lat": "27.66641253286814",
    "lon": "85.33086143678096",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

# print(response.status_code)

weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

weather_slice = weather_data["list"][:8]
# print(weather_slice)

will_rain = False
time = ""

for qtr in weather_slice:
    # time = qtr["dt_txt"]
    condition_code = qtr["weather"][0]["id"]

    if int(condition_code) < 700:
        time = qtr["dt_txt"]
        will_rain = True
        break

if will_rain:
    print(f"Bring an umbrella. It might rain at {time}")
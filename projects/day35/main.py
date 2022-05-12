import requests
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC7ed755ea19f6bfbb20737ffc6e2fbfc5"  # os.environ['TWILIO_ACCOUNT_SID']
auth_token = "e34bf7dfc9ac264975176212344721f0"  # os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5e394f8ae510851b77fe890f5ecb9f5e"

weather_params = {
    "lat": 59.858131,
    "lon": 17.644621,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


hourly_weather_data = []
for hour in range(12):
    weather = weather_data["hourly"][hour]["weather"]
    for condition in weather:
        hourly_weather_data.append(condition["id"])

# Check for rain
will_rain = False
for entry in hourly_weather_data:
    if entry < 700:
        will_rain = True
        break

# will_rain
if will_rain:
    message = client.messages.create(
        body="Ayy lil skrrt, it do be moist 2morrow",
        from_="+19853154701",
        to="+46709622936",
    )

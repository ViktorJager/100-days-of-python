from urllib import response
import requests
from datetime import datetime
''' 
response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

'''

LAT = 59.858562
LONG = 17.638927

parameters = {
    "lat": LAT,
    "long": LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise, sunset)

time_now = datetime.now()
print(time_now.hour)
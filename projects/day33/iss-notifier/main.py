from operator import is_
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 59.858562
MY_LONG = 17.638927

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():
    lat_diff = abs(MY_LAT - iss_latitude)
    long_diff = abs(MY_LONG - iss_longitude)

    if lat_diff < 5 and long_diff < 5:
        return True
    return False


def is_dark():
    if time_now > sunset:
        return True
    elif time_now < sunset and time_now < sunrise:
        return True
    else:
        return False

def send_email():
    # Burner mail for testing
    my_email = "groteskovilja@gmail.com"
    pw = "groteskovilja123"
    to_addr = "mjonsson900@gmail.com"
    message = f"Subject:ISS is nearby your location!\n\nGo outside and look up in the sky!"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=to_addr, msg=message)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

while True:
    if iss_nearby() and is_dark():
        send_email()
    time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




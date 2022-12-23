import smtplib
import requests
from datetime import datetime

MY_LAT = 12.474425  # Your latitude
MY_LONG = 4.251189  # Your longitude
my_email = "basharumartech@gmail.com"
password = "uzwofkucrrmkackb"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def send_email(message, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{email}", msg=f"Subject:ISS Message\n\n{message}")


# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

hour = time_now.hour


# If the ISS is close to my current position
if hour >= sunset or hour <= sunrise:
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        message = "Hey look up ISS is here"
        send_email(email="bumar@wufpbk.edu.ng", message=message)

    # Then send me an email to tell me to look up.

    # BONUS: run the code every 60 seconds.

import requests
api_key = "6131d002d6463ce92a39a89dab68dcd1"
city_name = "Birnin Kebbi,Nigeria"
# I changed the latitude to a place where its raining using latlon website//
lat = -12.070830   
lon = -75.206680
sms_username = "your username"
sms_password = "your password"
sms_url = "https://portal.nigeriabulksms.com/api/"
sms_parameters = {
    "username": sms_username,
    "pass": sms_password,
    "sender": "Bashar",
}

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": "metric",
    "exclude": "daily,current,minutely"
}
# url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={api_key}"
url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()


def send_sms(message, mobile):
    sms_parameters = {
        "username": sms_username,
        "password": sms_password,
        "sender": "Bashar",
        "message": message,
        "mobiles": mobile
    }
    sms_response = requests.get(url=sms_url, params=sms_parameters)
    sms_response.raise_for_status()
    sms_data = sms_response.json()
    status = sms_data['status']
    if status == 'OK':
        print("Success")


is_rain = False
for i in range(12):
    code = int(data['hourly'][i]['weather'][0]['id'])
    if code < 700:
        is_rain = True
        break
if is_rain:
    print("Bring an Umbrella")
    send_sms("Bring an Umbrella", "09029991710")

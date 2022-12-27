import requests
api_key = "6131d002d6463ce92a39a89dab68dcd1"
city_name = "Birnin Kebbi,Nigeria"
lat = -12.070830
lon = -75.206680
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
is_rain = False
for i in range(12):
    code = int(data['hourly'][i]['weather'][0]['id'])
    if code < 700:
        is_rain = True
        break
if is_rain:
    print("Bring an Umbrella")

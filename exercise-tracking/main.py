import requests
from datetime import *

APP_ID = "d76012e9"
APP_KEY = "3d3fe11200e1622d6afa910c0ec8ff02"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("Tell me what exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 172,
    "age": 34
}


response = requests.post(url=exercise_endpoint,
                         json=parameters, headers=headers)
response.raise_for_status()

data = response.json()
print(data['exercises'][0]['name'])
dt = datetime.now()
SHEETY_DATE = dt.strftime('%d/%m/%Y')
SHEETY_TIME = dt.strftime('%H:%M:%S')
SHEETY_EXERCISE = data['exercises'][0]['name']
SHEETY_CALORIES = data['exercises'][0]['nf_calories']
SHEETY_DURATION = data['exercises'][0]['duration_min']
print(SHEETY_DURATION)

sheety_endpoint = "https://api.sheety.co/8ce14fed661a498f82a423ccc8124db7/myWorkouts/workouts"
sheety_params = {
    "workout": {
        "date": SHEETY_DATE,
        "time": SHEETY_TIME,
        "exercise": SHEETY_EXERCISE.title(),
        "duration": SHEETY_DURATION,
        "calories": SHEETY_CALORIES,


    }
}
sheety_headers = {
    "Authorization": "Basic YmFzaHRlY2g6T3JhY2xlXzE="
}
sheety_resonse = requests.post(
    sheety_endpoint, json=sheety_params, headers=sheety_headers)
print(sheety_resonse.text)

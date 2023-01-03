import os
import requests
from dotenv import load_dotenv
from datetime import *
load_dotenv()
APP_ID = os.environ.get("APP_ID")


APP_KEY = os.environ.get("APP_KEY")
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
# response.raise_for_status()

data = response.json()

# print(data['exercises'][0]['name'])
dt = datetime.now()
SHEETY_DATE = dt.strftime('%d/%m/%Y')
SHEETY_TIME = dt.strftime('%H:%M:%S')
SHEETY_EXERCISE = data['exercises'][0]['name']
SHEETY_CALORIES = data['exercises'][0]['nf_calories']
SHEETY_DURATION = data['exercises'][0]['duration_min']


sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
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
print(sheety_resonse.reason)

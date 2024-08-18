import requests
import datetime as dt

APP_KEY = "Your App Key"
APP_ID = "Your App ID"

exercise_parameters = {
    "query": "I ran 2 miles and cycled for 31.5 minutes.",
}
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}
nutritionx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_response = requests.post(url=nutritionx_endpoint, json=exercise_parameters, headers=headers)
exercise_response.raise_for_status()

exercise_data = exercise_response.json()["exercises"]
exercises = [exercise["name"].title() for exercise in exercise_data]
durations = [int(duration["duration_min"]) for duration in exercise_data]
calories = [int(calorie["nf_calories"]) for calorie in exercise_data]

date = dt.datetime.now().strftime(f"%d/%m/%Y")
time = dt.datetime.now().time().strftime(f"%X")

sheet_endpoint = "Your Endpoint"
for i in range(len(exercises)):
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercises[i],
            "duration": durations[i],
            "calories": calories[i]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)

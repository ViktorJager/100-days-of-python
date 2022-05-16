import requests

APP_ID = "98d7633b"
API_KEY  = "791d856f20f33141fb41b741d202b302"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = "Ran 5 miles in slow pace"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender":"male",
    "weight_kg":85,
    "height_cm":190,
    "age":27
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)










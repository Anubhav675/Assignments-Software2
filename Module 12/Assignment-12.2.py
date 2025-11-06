import json
from http.client import responses

import requests

city = input("Enter the name of the city: ")
API = "99d4329f37fe1e2182dd0c2015723919"

try:
    request = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API}"
    response = requests.get(request)
    json_response = response.json()
    lat = json_response[0]['lat']
    lon = json_response[0]['lon']

except requests.exceptions.RequestException as e:
    print("Request couldn't be completed")

try:
    request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}"
    response = requests.get(request)
    json_response = response.json()
    print(f"Weather: {json_response['weather'][0]['description'].capitalize()}")
    temp = json_response['main']['temp'] - 273.15
    print(f"Temperature: {temp:.0f}° Celsius")  # alt+0176 for degree symbol

except requests.exceptions.RequestException as e:
    print("Request couldn't be completed")

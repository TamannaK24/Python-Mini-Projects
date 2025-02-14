import requests 
import datetime as dt
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "ec683a00cb6a8972aa92134fe7f89dad" 
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY 

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

response = requests.get(url).json()

# with open ("response.json()", "w") as json_file:
#     json.dump(response, json_file, indent=4) 

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = response['sys']['sunrise'] + response['timezone']
# converts to datetime object allowing it to be converted into a human readable format
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f} deg C or ({temp_fahrenheit:.2f} deg F)")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f} deg C or ({feels_like_fahrenheit:.2f} deg F)")
print(f"Humidigity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed} km/h")
print(f"General Weather in {CITY}: {description}")
print(f"Sunrise in {CITY}: {sunrise_time}")
print(f"Sunset in {CITY}: {sunset_time}")




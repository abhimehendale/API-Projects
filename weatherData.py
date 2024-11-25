
import requests
import json

base_URL = "http://api.weatherapi.com/v1/current.json?key=94adab74c82d407993390011242011"


def get_weather_data(city,aqi):
  whole_url = f"{base_URL}&q={city}&aqi={aqi}"
  response = requests.get(whole_url)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print("Data failed")




city = "Mumbai"
aqi = "Yes"

get_data = get_weather_data(city,aqi)
location = get_data["location"]
current = get_data["current"]
current_condition = current["condition"]


print("City name:", location["name"])
print("Current condition:", current_condition["text"] )

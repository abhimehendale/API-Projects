
import requests
import csv


forcast_base_url = "http://api.weatherapi.com/v1/forecast.json?key=94adab74c82d407993390011242011"
cities = ["London", "Mumbai", "Durban", "New York", "Melbourne"]
days = "5"
aqi = "yes"
alerts = "yes"
fields = ["Name", "Region", "Country", "Current Date", "Local Time", "Condition", "Humidity","+1 day date","+1 day forecast", "+2 days date", "+2 days forecast", "+3 days date","+3 days forecast", "+4 days date", "+4 day forecast", "+5 days date","+5 days forecast"]
rows = []
filename = "weatherData.csv"




def getdata(city):
  whole_url = f"{forcast_base_url}&q={city}&days={days}&aqi={aqi}&alerts={alerts}"
  response = requests.get(whole_url)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print("No data")


with open(filename, mode='w') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(fields)
  for city in cities:
    data = getdata(city)
    name = data["location"]["name"]
    region = data["location"]["region"]
    country = data["location"]["country"]
    current_date_time = data["location"]["localtime"]
    current_date_time_list = current_date_time.split()
    current_date = current_date_time_list[0]
    current_time = current_date_time_list[1]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    rows = [name, region, country, current_date, current_time, condition, humidity]
    i = 0
    while i<=4:
      day_date = data["forecast"]["forecastday"][i]["date"]
      day_forcast = data["forecast"]["forecastday"][i]["day"]["condition"]["text"]
      rows.append(day_date) 
      rows.append(day_forcast)
      i+=1
    csvwriter.writerow(rows)
    rows = []
    print("Data printed")
    
    


  
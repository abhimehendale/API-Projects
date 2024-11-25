
import requests
import json
import time

base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
api_key = "apikey=demo"
def get_stockdata(name,interval):
  whole_url = f"{base_url}&symbol={name}&interval={interval}min&{api_key}"
  response = requests.get(whole_url)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print("Not ok")
  

name = "IBM"
interval = "5"

data = get_stockdata(name,interval)

#meta_data = data["Meta Data"]
tick_name = data["Meta Data"]["2. Symbol"]

def getprice(data):
  last_refreshed = data["Meta Data"]["3. Last Refreshed"]
  price = data["Time Series (5min)"][last_refreshed]["1. open"]

  return price

i=0
while(i<=10):
  print("Stock Name:", tick_name)
  #print("Last Refreshed Time", meta_data["3. Last Refreshed"])
  print("Last Refreshed Time", data["Meta Data"]["3. Last Refreshed"])
  open_price = getprice(data)
  print("Open Price",open_price)
  time.sleep(360)
  i+=1




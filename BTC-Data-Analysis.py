

import requests
import csv
import datetime 
import pandas as pd

url = "https://data-api.cryptocompare.com/spot/v1/historical/days?market=binance&instrument=BTC-USDT&aggregate=1&fill=true&apply_mapping=true&response_format=JSON&limit=5000"

header = {
  'Api' : '4e85e33f42afea2269fc60db22601524bad267ae120fec2657085baf34dcf5d7'
}

filename = "BTCAnalysis.csv"
fields = ["Date","Open", "High", "Low", "Close", "Volume","Total Trades","Total Buy", "Total Sell"]
row = []
response = requests.get(url, headers=header)

if response.status_code ==200:
  data = response.json()
else:
  print("Not okay")


data_list = data["Data"]
#firstday = data_list[0]["TIMESTAMP"]
#print(firstday)
print(len(data_list))



with open(filename, mode='w') as file:
  csvwriter = csv.writer(file)
  csvwriter.writerow(fields)
  for i in range(len(data_list)):
    timestamp = datetime.datetime.fromtimestamp(int(data_list[i]["TIMESTAMP"]))
    date = timestamp.strftime('%d-%m-%Y') #%H:%M:%S')
    open = data_list[i]["OPEN"]
    high = data_list[i]["HIGH"]
    low = data_list[i]["LOW"]
    close = data_list[i]["CLOSE"]
    volume = data_list[i]["VOLUME"]
    total_trades = data_list[i]["TOTAL_TRADES"]
    total_buy = data_list[i]["TOTAL_TRADES_BUY"]
    total_sell = data_list[i]["TOTAL_TRADES_SELL"]
    row.append(date)
    row.append(open)
    row.append(high)
    row.append(low)
    row.append(close)
    row.append(volume)
    row.append(total_trades)
    row.append(total_buy)
    row.append(total_sell)
    csvwriter.writerow(row)
    row = []
    



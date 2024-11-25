import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("BTCAnalysis.csv")

max_price = df["Close"].max()
min_price = df["Close"].min()

max_price_date = df.loc[df["Close"].idxmax(), "Date"]
min_price_date = df.loc[df["Close"].idxmin(), "Date"]

print(f"Max price: {max_price} & Max Date: {max_price_date}")
print(f"Min price: {min_price} & Min Date: {min_price_date}")

priceAbove50 = df.loc[df["Close"] > 50000].reset_index(drop=True)
priceAbove50.index = priceAbove50.index+1
#priceAbove50.loc[1280:10,["Date", "Close"]]
#print(priceAbove50.loc[1:10,["Date", "Close"]])


#18-02-24 = 51552.60

#priceAbove50.loc[priceAbove50["Date"] == "18-02-2021", ["Close"]] = 0
print(priceAbove50.loc[priceAbove50["Date"] == "18-02-2021",["Date", "Close"]]) 


priceAbove50["Date"] = plt.to_datetime(priceAbove50["Date"])

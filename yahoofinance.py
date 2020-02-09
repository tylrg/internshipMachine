import requests
import yfinance as yf
import pandas as pd
import numpy as np
apple = yf.Ticker("AAPL")
exon = yf.Ticker("XOM")
ibm = yf.Ticker("IBM")
micro = yf.Ticker("MSFT")
nike = yf.Ticker("NKE")
amazon = yf.Ticker("AMZN")
pfizer = yf.Ticker("PFE")
walmart = yf.Ticker("WMT")

# t = apple.history(period = "5d")
# df= pd.DataFrame(t)
# print("Apple")
# print(df.iloc[0])
# print(df.iloc[4])
#
# e = exon.history(peroid = "5d")
# df1 = pd.DataFrame(e)
# print("Exon")
# print(df1.iloc[0])
# print(df1.iloc[4])
#
# i = ibm.history(peroid="5d")
# df2 = pd.DataFrame(i)
# print("IBM")
# print(df2.iloc[0])
# print(df2.iloc[4])
#
# m = micro.history(peroid="5d")
# df3 = pd.DataFrame(m)
# print("Microsoft")
# print(df3.iloc[0])
# print(df3.iloc[4])
#
# n = nike.history(peroid="5d")
# df4 = pd.DataFrame(n)
# print("Nike")
# print(df4.iloc[0])
# print(df4.iloc[4])
#
# a = amazon.history(peroid="5d")
# df5 = pd.DataFrame(a)
# print("Amazon")
# print(df5.iloc[0])
# print(df5.iloc[4])
#
# p = pfizer.history(peroid="5d")
# df6 = pd.DataFrame(p)
# print("pfizer")
# print(df6.iloc[0])
# print(df6.iloc[4])
#
# w = walmart.history(peroid="5d")
# df7 = pd.DataFrame(w)
# print("Walmart")
# print(df7.iloc[0])
# print(df7.iloc[4])

def returnPrice(symbol):
    stock = yf.Ticker(symbol)
    h = stock.history(period="5d")
    x=pd.DataFrame(h)
    new = x.iloc[0]
    old = x.iloc[4]
    y = new.iloc[3]
    z = old.iloc[3]
    value = ((y-z)/y)*100
    print(y)
    print(z)
    value=round(value)
    print(value)

returnPrice("AAPL")

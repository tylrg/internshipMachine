from flask import Flask
from flask_restful import Resource, Api,reqparse,request

import requests
import yfinance as yf
import pandas as pd
import numpy as np

import seekingalpha
import marketwatch

parser=reqparse.RequestParser()
parser.add_argument('symbol')
parser.add_argument('name')

app = Flask(__name__)
api = Api(app)


def returnPercent(symbol):
    stock = yf.Ticker(symbol)
    h = stock.history(period="5d")
    x = pd.DataFrame(h)
    new = x.iloc[0]
    old = x.iloc[4]
    y = new.iloc[3]
    z = old.iloc[3]
    value = ((y-z)/y)*100
    value = round(value, 2)
    print(value)
    return value
def returnPrice(symbol):
    stock = yf.Ticker(symbol)
    h = stock.history(period="5d")
    x = pd.DataFrame(h)
    new = x.iloc[0]
    #old = x.iloc[4]
    y = new.iloc[3]
    #z = old.iloc[3]
    #value = ((y-z)/y)*100
    value = round(y, 2)
    #print(value)
    return value
#sentiment

class Percent(Resource):
    def get(self):
        # value = returnPrice("XOM")
        # return {'hello': value }
        symbol=request.args.get('symbol')
        value = returnPercent(symbol)
        return {
            "symbol": symbol,
            "value":value
        }

class Price(Resource):
    def get(self):
        # value = returnPrice("XOM")
        # return {'hello': value }
        symbol=request.args.get('symbol')
        value = returnPrice(symbol)
        return {
            "symbol": symbol,
            "value":value
        }

class Sentiment(Resource):
    def get(self):
        symbol=request.args.get('symbol')
        name=request.args.get('name')
        #value = call to the sentiment method
        seekingRetVal = seekingalpha.seekingalpha(name, symbol)
        marketRetVal = marketwatch.marketwatch(name, symbol)
        
        seekingSSAvg = seekingRetVal[0:seekingRetVal.index(' ')]
        marketSSAvg = marketRetVal[0:marketRetVal.index(' ')]
        seekingMagAvg = seekingRetVal[seekingRetVal.index(' ')+1]
        marketMagAvg = marketRetVal[marketRetVal.index(' ')+1]
        
        totalAvgSS = (float(seekingSSAvg) + float(marketSSAvg)) / 2.0
        totalAvgMag = (float(seekingMagAvg) + float(marketMagAvg)) / 2.0
        
        return{
            "symbol": symbol,
            "sentiment": totalAvgSS,
            "magnitude": totalAvgMag
        }
api.add_resource(Sentiment,'/sentiment')
api.add_resource(Percent, '/percent')
api.add_resource(Price, '/price')
if __name__ == '__main__':
    app.run(debug=True)
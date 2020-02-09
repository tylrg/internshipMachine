from flask import Flask
from flask_restful import Resource, Api,reqparse,request

import requests
import yfinance as yf
import pandas as pd
import numpy as np

parser=reqparse.RequestParser()
parser.add_argument('symbol')

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

api.add_resource(Percent, '/percent')
api.add_resource(Price, '/price')


if __name__ == '__main__':
    app.run(debug=True)

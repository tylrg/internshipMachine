from flask import Flask
from flask_restful import Resource, Api

import requests
import yfinance as yf
import pandas as pd
import numpy as np


app = Flask(__name__)
api = Api(app)


def returnPrice(symbol):
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

class HelloWorld(Resource):
    def get(self):
        value = returnPrice("XOM")
        return {'hello': value }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

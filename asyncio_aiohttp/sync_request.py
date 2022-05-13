import requests
import os
import time


api_key = os.getenv("alpha_vantage_api_key")

print(api_key)

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']

results = []

for symbol in symbols:
    print(symbol)
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
import os
import asyncio
import ssl

from requests import session
import aiohttp


api_key = os.getenv("alpha_vantage_api_key")


url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']

results = []

async def get_symbols():
    async with aiohttp.ClientSession() as sesssion:
        for symbol in symbols:
            print(symbol)
            response = await session.get(url.format(symbol, api_key), ssl = False)
            results.append(await response.json())



asyncio.run(get_symbols)
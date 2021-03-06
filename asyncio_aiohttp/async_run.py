import asyncio
import ssl
import os
import asyncio
import aiohttp

api_key = os.getenv("alpha_vantage_api_key")
url     = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []



async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print(symbol)
            response = await session.get(url.format(symbol, api_key), ssl = False)
            results.append(await response.json())


asyncio.run(get_symbols())
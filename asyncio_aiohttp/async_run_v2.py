import asyncio
import os
import asyncio
import aiohttp
from dbus import SessionBus

api_key = os.getenv("alpha_vantage_api_key")
url     = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']
results = []


def get_tasks(session):
    tasks = []

    for symbol in symbols:
        print(symbol)
        tasks.append(session.get(url.format(symbol, api_key), ssl = False))
    
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks       = get_tasks(session)
        responses   = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


asyncio.run(get_symbols())


print(results)
## Practicing concurrency



In the case of our <code>asyncio_aiohttp</code> use case:<br>
We see the power of ayncio to manage multiple server's responses. While one request is being processed, the other one begins.
We divide the execution time tenfolds when we switch from <code>sync_request.py</code> to the<code>async_run_v2.py</code> script.

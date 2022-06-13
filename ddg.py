import asyncio
import json
from json.decoder import JSONDecodeError
import urllib.parse

import requests

api_url = "https://ddg.deedy5.repl.co/ddg"

def get_results(params, timeout):
    with requests.get(api_url, params=params, timeout=timeout) as response:
        try:
            data = json.loads(response.text)
            return data
        except JSONDecodeError:
            return []

async def ddg(query, max_results=3, timeout=5.0):
    params = {
        "q": query,
        "max_results": max_results
    }
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, get_results, params, timeout)

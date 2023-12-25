import requests
import json
from pprint import pprint

url = "https://apps.lafayettela.gov/L911/WebService1.asmx/getCurrentTrafficConditions"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://apps.lafayettela.gov",
    "Referer": "https://apps.lafayettela.gov/L911/default",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Content-Length": "0",
    "TE": "trailers"
}

response = requests.post(url, headers=headers)
json_data = json.loads(response.json()['d'])

if response.status_code == 200:
    # Do something with the response
    # print(response.json())
    pprint(json_data)
else:
    print(f"Error: {response.status_code}")

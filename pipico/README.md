This is a micropython file for the Pi Pico W to connecto to lafayette911.org and get the JSON data.
Once it has it, it checks for accidents.  If there are any, it turns on the built in LED.  It checks every 30 seconds.


The key is in the headers to get the correct POST you need to return the live JSON data:

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

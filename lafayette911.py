# This is a new Python script template

import sys
import os
import requests
import json

def main():
    try:
        print("Script started.")
        # Pull data from the internet
        url = "https://lafayette911.org/WebService1.asmx/getCurrentTrafficConditions"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://lafayette911.org",
            "Connection": "keep-alive",
            "Referer": "https://lafayette911.org/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Content-Length": "0",
            "TE": "trailers"
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print("Data retrieved successfully.")
            data = json.loads(response.text)
            if 'd' in data:
                cleaned_data = json.loads(data['d'])
                for incident in cleaned_data.get('incidents', []):
                    if 'location' in incident:
                        incident['location'] = incident['location'].split('/')[0].strip()
                print(json.dumps(cleaned_data, indent=4))
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Script ended.")

if __name__ == "__main__":
    main()

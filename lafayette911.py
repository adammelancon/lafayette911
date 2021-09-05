import requests
from bs4 import BeautifulSoup
import re
import json

incidents = []
incidents_clean = []

def soup_me():
    global incidents
    url = 'https://apps.lafayettela.gov/L911/Service2.svc/getTrafficIncidents'
    myobj = {'name': 'e'}
    r = requests.post(url, data = myobj)
    soup = BeautifulSoup(r.text, 'html.parser')
    for tr in soup.find_all(target="_new"):
        incidents.append(tr)    

def check_incidents():
    if not incidents:
        ni = "No incidents at the moment."
        print(ni)
        with open('lafayette911.json', 'w') as outfile:
            json.dump(ni, outfile)
    else:
        process_incidents()

def process_incidents():
    global incidents_clean
    for row in incidents:
        print("=" * 50)
        row = row.text
        row = re.compile(r'(<[^>]+>)|(")|({)|(})').sub('', row)
        row = row.strip('/}')
        row = row.replace("\\", "")
        print(row)
        print("=" * 50)
        incidents_clean.append(row)
        
    with open('lafayette911.json', 'w') as outfile:
        json.dump(incidents_clean, outfile)

soup_me()
check_incidents()

    

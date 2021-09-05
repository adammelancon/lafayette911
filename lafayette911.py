import requests, re, json, unicodedata
from bs4 import BeautifulSoup
from datetime import datetime

incidents = []
incidents_clean = []

def get_time():
    global incidents_clean
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return "Last Ran - " + str(date_time)

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
        ni = "No incidents at " + get_time()
        print(ni)
        with open('lafayette911.json', 'w') as outfile:
            json.dump(ni, outfile)
    else:
        process_incidents()

def process_incidents():
    global incidents_clean
    for row in incidents:
        row = row.text
        row = re.compile(r'(<[^>]+>)|(")|({)|(})').sub('', row)
        row = row.strip('/}')
        row = row.replace("\\", "")
        row = unicodedata.normalize("NFKD",row)
        incidents_clean.append(row)

    incidents_clean.append(get_time())
    
    with open('lafayette911.json', 'w') as outfile:
        json.dump(incidents_clean, outfile)

def display_incidents():
    print(incidents_clean)

soup_me()
check_incidents()
display_incidents()

    

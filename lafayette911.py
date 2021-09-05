import requests
from bs4 import BeautifulSoup
import re

incidents = []

url = 'https://apps.lafayettela.gov/L911/Service2.svc/getTrafficIncidents'
myobj = {'name': 'e'}
r = requests.post(url, data = myobj)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

rows = soup.find_all(target="_new")

for tr in soup.find_all(target="_new"):
    incidents.append(tr)    

if not incidents:
    print("No incidents at the moment.")
else:
    for row in incidents:
        print("=" * 50)
        row = row.text
        row = re.compile(r'(<[^>]+>)|(")|({)|(})').sub('', row)
        row = row.strip('/}')
        row = row.replace("\\", "")
        print(row)
        print("=" * 50)

import urequests
import ujson as ujson
from machine import Pin
import network
import time


ssid_list = ['ssid1', 'ssid2']  # List of Wi-Fi SSIDs to try
password_list = ['password1', 'password2']  # List of passwords for each Wi-Fi SSID

station = network.WLAN(network.STA_IF)

for i in range(len(ssid_list)):
    ssid = ssid_list[i]
    password = password_list[i]
    station.active(True)
    station.connect(ssid, password)
    print('Connecting to', ssid)
    for _ in range(10):  # Try to connect for 10 seconds
        if station.isconnected():
            print('Wi-Fi connected:', station.ifconfig())
            break
        time.sleep(1)
    else:
        print('Failed to connect to', ssid)
        station.disconnect()
        station.active(False)
        continue
    break
else:
    print('No Wi-Fi networks available')


led = Pin("LED", Pin.OUT)
led.off()

is_vehicle_accident = False

def has_vehicle_accident():
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
    
    response = urequests.post(url, headers=headers)
    print(response)
    json_data = ujson.loads(response.json()['d'])
    #print(json_data)
    for incident in json_data['incidents']:
        if 'ACCIDENT' in incident['cause']:
            print("ACCIDENT")
            led.on()
            return True
    print("no accident")
    return False

while True:
    for _ in range(10):
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
    has_vehicle_accident()
    time.sleep(30)

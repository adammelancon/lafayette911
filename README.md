# lafayette911.org output processing
---------------------------------------
UPDATE!!!!
I finally got the JSON directly from the site.  See the folder for the Pi Pico W script to see how I'm using the data with a Pi Pico LED.
---------------------------------------


This is a perpetual script I keep working on as I get better with Python.
This script scrapes http://lafayette911.org for data and attemps to clean it up and make it presentable as JSON or some easily readable text.

From:
![image](https://github.com/adammelancon/lafayette911/assets/3197653/f6b8fbdf-cbdf-4df3-a19a-4ab4b25d205e)

To:
```
Time:   12/24/2023 20:30
Loc:    300 BACHERT ST, BACHERT LAFAYETTE, LA
Cause:  Vehicle Accident
Agency: Police

Time:   12/24/2023 19:30
Loc:    400 MARIE ANTOINETTE ST, LAFAYETTE, LA
Cause:  Vehicle Accident
Agency: Police

Time:   12/24/2023 19:01
Loc:    1600 N UNIVERSITY AVE, HOLLYWOOD LAFAYETTE, LA
Cause:  Vehicle Accident
Agency: Police
```
Or:

```
{
    "status": "ok",
    "incidents": [
        {
            "location": "300 BACHERT ST/BACHERT            LAFAYETTE, LA",
            "cause": "VEHICLE ACCIDENT",
            "reported": "12/24/2023 20:30",
            "assisting": "POLICE",
        },
        {
            "location": "400 MARIE ANTOINETTE ST/            LAFAYETTE, LA",
            "cause": "VEHICLE ACCIDENT",
            "reported": "12/24/2023 19:30",
            "assisting": "POLICE",
        },
        {
            "location": "1600 N UNIVERSITY AVE/HOLLYWOOD            LAFAYETTE, LA",
            "cause": "VEHICLE ACCIDENT",
            "reported": "12/24/2023 19:01",
            "assisting": "POLICE",
        },
    ],
}
```

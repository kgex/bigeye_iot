from datetime import datetime
import requests
import json
import time
d =	{}

url_post = "https://kgxtest.herokuapp.com/attendance_in"
url_update = "https://kgxtest.herokuapp.com/attendance_out"

headers = {"Content-Type": "application/json; charset=utf-8", "x-hasura-admin-secret" : "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay"}

def outentry(id, key):
    print("outentry")
    now = datetime.now() # current date and time
    data_out_time = {
            "id": int(id),
            "out_time" :now
        
    }
    response = requests.patch(url_update, headers=headers, json=data_out_time)
    print(response.json())
    del d[key]
    print(d)

def inentry(key):
    print("inentry")
    now = datetime.now() # current date and time
    data_in_time = {
        "rfid_key": key,
        "in_time" :now
        }
    print("here", data_in_time)
    try:
        response = requests.post(url_post, headers=headers, json=data_in_time)
        data = response.json()
        d[key] = data['insert_attendance_entry']['returning'][0]['id']
        print(d)
    except Exception as e:
        print(e)    

def tap(key):
    print("keys", d.keys())
    if key in d.keys():
        outentry(d[key], key)
    else:
        inentry(key)


while 1:
    ip = input()
    tap(ip)


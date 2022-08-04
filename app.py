from datetime import datetime
import requests
import json
import time
import pickle

d = {}

# Open the file in binary mode
try:
    with open("backup.pkl", "rb") as file:
    # Call load method to deserialze
        d = pickle.load(file)
        print(d)
except Exception:
    pass


url_post = "https://bigbbe.herokuapp.com/attendance_in"
url_update = "https://bigbbe.herokuapp.com/attendance_out"

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "x-hasura-admin-secret": "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay",
}


def backup(d):
    # Open a file and use dump()
    with open("backup.pkl", "wb") as file:
        # A new file will be created
        pickle.dump(d, file)
        file.close()


def outentry(id, key):
    print("outentry")
    now = datetime.now()  # current date and time
    data_out_time = {"id": int(id), "out_time": datetime.timestamp(now)}
    response = requests.patch(url_update, headers=headers, json=data_out_time)
    print(response.json())
    del d[key]
    print(d)
    backup(d)


def inentry(key):
    print("inentry")
    now = datetime.now()  # current date and time
    data_in_time = {"rfid_key": key, "in_time": datetime.timestamp(now)}
    print("here", data_in_time)
    try:
        response = requests.post(url_post, headers=headers, json=data_in_time)
        data = response.json()
        print(data)
        d[key] = data["id"]
        print(d)
        backup(d)
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
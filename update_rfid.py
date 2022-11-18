from datetime import datetime
import requests
import json
import time
import pickle
import pandas as pd

d = {}
dic = {}
url_post = "https://bbapi.nivu.me/updaterfid"

headers = {
    "Content-Type": "application/json"
}

def register(dict):
    print(dict)
    return requests.patch(url_post, json=dict, headers=headers, verify=False)

    # rfid = input("Register your RFID Enabled Card")


data = pd.read_csv(r"C:\Users\Ramesh\Downloads\KGX Final RFID - Sheet11.csv")
data = data.astype({'rfid': 'string'})
print(type(data['rfid'][0]))
data.dropna(inplace=True)
# data = data.tail(1)
data['rfid'] = data['rfid'].astype(str)
data.reset_index()
for index,row in data.iterrows():
    email = row['email']
    rfid = '0'* (10 - len(str(row['rfid']).split('.')[0])) + str(row['rfid']).split('.')[0]
    print(rfid, email)
    print(register({"rfid_key": rfid, "email": email}))
    time.sleep(1)
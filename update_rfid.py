from datetime import datetime
import requests
import json
import time
import pickle
 
d = {}

url_post="http://34.28.3.109:8080/updaterfid"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "x-hasura-admin-secret": "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay",
}

def register(dict):    
    return requests.patch(url_post, headers=headers, json=dict)
 

while True:
    rfid = input("Register your RFID Enabled Card")
    email = input("Enter your email: ")
    print(register({"rfid_key":rfid,"email":email}))


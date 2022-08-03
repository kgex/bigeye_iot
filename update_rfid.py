from datetime import datetime
import requests
import json
import time
import pickle
 
d = {}

url_post="https://bigbbe.herokuapp.com/updaterfid"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "x-hasura-admin-secret": "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay",
}

def register(dict):    
    return requests.patch(url_post, headers=headers, json=dict)
 

while True:
    email = input("Enter your email: ")
    rfid = input("Register your RFID Enabled Card") 
    print(register({"email":email,"rfid_key":rfid}))


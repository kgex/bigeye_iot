from datetime import datetime
import requests
import json
import time
import pickle
import pandas as pd

d = {}
dic = {}
url_post = "http://34.28.3.109:80/updaterfid"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "x-hasura-admin-secret": "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay",
}


def register(dict):
    return requests.patch(url_post, headers=headers, json=dict)

    # rfid = input("Register your RFID Enabled Card")


data = pd.read_csv(r"/home/ramesh/Downloads/KGX Final RFID - October.csv")
emails = data.loc[:, ["email", "rfid"]]
for email, rfids in emails:
    print(register({"rfid_key": rfids, "email": email}))

    # email = input("Enter your email: ")

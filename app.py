from datetime import datetime
import requests
import json
import time
import pickle
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

d = {}

# Open the file in binary mode
try:
    with open("backup.pkl", "rb") as file:
    # Call load method to deserialze
        d = pickle.load(file)
        print(d)
except Exception:
    pass


root = tk.Tk()
root.title("KGX Attendance System")
root.geometry("800x480")

# Create a photoimage object of the image in the path
img = ImageTk.PhotoImage(Image.open("kgxlogo.png"))
label = Label(root, image = img,width=50, height=50)
label.pack(side = "bottom",fill="both",expand = "yes")

rfid_var=tk.StringVar()
rfid_entry = tk.Entry(root,textvariable = rfid_var,width=50, font=('calibre',10,'normal'))
#rfid_entry.grid(row=0,column=0)
rfid_entry.pack()
rfid_entry.focus_set()

lbl = Label(root, text="", font=("Arial", 25))
lbl.pack()

url_post = "https://bbapi.nivu.me/attendance_in"
url_update = "https://bbapi.nivu.me/attendance_out"

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
    response = requests.patch(url_update, headers=headers, json=data_out_time, verify=False)
    print(response.json())
    del d[key]
    print(d)
    backup(d)   
    lbl.config(text="Attendence OUT Successfull")
    
def inentry(key):
    print("inentry")
    now = datetime.now()  # current date and time
    data_in_time = {"rfid_key": key, "in_time": datetime.timestamp(now)}
    print("here", data_in_time)
    try:
        response = requests.post(url_post, headers=headers, json=data_in_time, verify=False)
        data = response.json()
        print(data)
        d[key] = data["id"]
        print(d)
        backup(d)
        lbl.config(text="Attendence IN Successfull : " + str(data["name"]))
        
    except Exception as e:
        print(e)
        lbl.config(text="Unregistered User, Please contact Admin !!" "\n RFID :" + key)
    
def tap(key):
    print("keys", d.keys())
    if key in d.keys():
        outentry(d[key], key)
    else:
        inentry(key)

def enter(a):
    print("enter")
    key=rfid_var.get()
    # key = entry.get()
    print(key)
    tap(key)
    rfid_var.set("")

root.bind('<Return>', enter)

root.mainloop()

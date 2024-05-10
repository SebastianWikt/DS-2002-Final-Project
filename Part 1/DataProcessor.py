import sqlite3
import requests
import pandas as pd
import time
from datetime import datetime

import numpy as np

#function for converting api call to csv and useable data
def get_response(url):
    response = requests.get(url)
    response_json = response.json()
    return response_json

#connecting to database (database.db through sqlite import)
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

#creating the table
cursor.execute('''CREATE TABLE IF NOT EXISTS Data (
                entryid INTEGER PRIMARY KEY AUTOINCREMENT,
                factor INTEGER NOT NULL,
                pi DOUBLE NOT NULL,
                time TEXT NOT NULL
               )''')

api_link = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"


num_minutes = 60
for i in range(num_minutes):
    response_json = get_response(api_link)
    print(response_json)
    factor_insert = response_json["factor"]
    pi_insert = float(response_json["pi"])
    time_insert = response_json["time"]
    print(factor_insert)
    print(pi_insert)
    print(time_insert)
    try:
        cursor.execute('''INSERT INTO Data (
                        factor, 
                        pi,
                    time)
                        VALUES(?, ?, ?)''', 
                        (factor_insert, pi_insert, time_insert))
        connection.commit()
        print("successful")
    except Exception as e:
        print(f"Error inserting data: {e}")
    time.sleep(59.4)


connection.commit()
connection.close()

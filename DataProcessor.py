import sqlite3
import requests
import pandas as pd

#function for converting api call to csv and useable data
def get_response(url):
    response = requests.get(url)
    response_json = response.json()["data"]
    return response_json



api_link = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
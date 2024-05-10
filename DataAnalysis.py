import sqlite3
import requests
import pandas as pd
import time
from datetime import datetime
from matplotlib import pyplot as plt
from sqlalchemy import create_engine

import numpy as np

def printsql():
    rows_in_sql = cursor.fetchall()
    for row in rows_in_sql:
        print(row)

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

timeFactor = "SELECT time, factor FROM Data ORDER BY time ASC"
timeFactordf = pd.read_sql_query(timeFactor, connection)

time = timeFactordf['time']
factor = timeFactordf['factor']

fig = plt.figure()
ax = plt.axes()

ax.plot(time, factor)
ax.set_title('Time vs Factor')  
ax.set_xlabel('Time')         
ax.set_ylabel('Factor');        


# sql_statement = cursor.execute('''SELECT factor, pi, time
#                                 FROM Data
#                                 ORDER BY pi ASC''')
# printsql()
# sql_statement = cursor.execute('''SELECT *
#                                 FROM Data''')
# printsql()


timePi = "SELECT time, pi FROM Data ORDER BY time ASC"
timePidf = pd.read_sql_query(timePi, connection)

time2 = timePidf['time']
pi = timePidf['pi']
fig = plt.figure()
ax = plt.axes()

ax.plot(time2, pi)
ax.set_title('Time vs Pi')   # Add a title
ax.set_xlabel('Time')          # Add x label
ax.set_ylabel('Pi')

timePi = "SELECT pi, factor FROM Data ORDER BY factor ASC"
timePidf = pd.read_sql_query(timePi, connection)

pi2 = timePidf['pi']
factor2 = timePidf['factor']
fig = plt.figure()
ax = plt.axes()

ax.plot(factor2, pi2)
ax.set_title('Factor vs Pi')   # Add a title
ax.set_xlabel('Factor')          # Add x label
ax.set_ylabel('Pi')


plt.show()

connection.close()
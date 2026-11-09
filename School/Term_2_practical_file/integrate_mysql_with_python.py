#program to integrate mysql with python
#6

import mysql.connector as sql

connector = sql.connect(host = "localhost", user = "root", password = "12345")

if connector.is_connected(): print("Connection established succesfully")
else: print("Connection error: connection unsuccesful")

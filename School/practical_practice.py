#practical practice

'''
import mysql.connector as sql

db = sql.connect(host = "localhost", user = "root", passwd = "12345", database = "world")
if db.is_connected(): print("Connected")
else: print("Connection error")

cur = db.cursor()
cur.execute("select * from city")
data = cur.fetchmany(10)

[print(i) for i in data]

print(type(cur.rowcount))

db.close()
'''


'''
#writes the required string to a temporary file and then prints the file contents
from tempfile import mktemp
from os import startfile

file = mktemp(".txt")
open(file, 'w').write("Test writing")
startfile(file, 'print')
'''

'''
import mysql.connector as sql

cnc = sql.connect(host = 'localhost', user = 'root', password = '12345')

cur = cnc.cursor()

cur.execute("show databases")
result = cur.fetchall()

print(result)

cnc.close()
'''

import mysql.connector as sql

cnc = sql.connect(host = "localhost", user = 'root', passwd = '12345', database = 'prac')
cur = cnc.cursor()
q = 'create table stationary(I_code varchar(3), I_name char(30), Qty int, price float)'

cur.execute(q)

cnc.close()



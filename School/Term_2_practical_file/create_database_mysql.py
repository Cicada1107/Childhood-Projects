#program to create given database in mysql via python
#7

import mysql.connector as sql

__db = sql.connect(host = "localhost", user = "root", password = "12345")
cur = __db.cursor()

cur.execute("create database if not exists xyzcorp")
cur.execute("use xyzcorp")
cur.execute("create table Customer (CustNumb BIGINT primary key, CustName VARCHAR(255), Address VARCHAR(255), Balance FLOAT, CredLim BIGINT, SLSRNumb BIGINT)")
query = "insert into Customer (CustNumb, CustName, Address, Balance, CredLim, SLSRNumb) values (%s, %s, %s, %s, %s, %s)"
vals = [(124, "Tina Adams", "461 Tilak lane CP Delhi", 41800.75, 50000, 3), (256, "R Venkat", "215 Mylapore Chennai", 100000.75, 80000, 6),
        (567, "Bhuvna Balaji", "803 Balanagar Hydrabad", 57000.75, 50000, 6), (622, "Pratham Jain", "149 Pilot 182 Dwarka Delhi", 57500.75, 80000, 12)]
cur.executemany(query, vals)
__db.commit()

print(cur.rowcount, "records inserted succesfully.")

__db.close()

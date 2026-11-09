#data operations from database tables in mysql via python
#8

"""responsible for making the tables and database elemetns as given in the practical file"""

import mysql.connector as sql

__db = sql.connect(host = "localhost", user = "root", password = "12345")
cur = __db.cursor()

cur.execute("create database if not exists coaching")
cur.execute("use coaching")
cur.execute("create table Faculty (F_ID VARCHAR(10) primary key, FName VARCHAR(50), LName VARCHAR(50), HireDate DATE, Salary FLOAT)")
query = "insert into Faculty (F_ID, FName, LName, HireDate, Salary) values (%s, %s, %s, %s, %s)"
vals = [("F101", "Rakesh", "Mittal", '2014/03/07', 49000), ('F121', "Sreya", "Bhowmik", '2012/04/05', 52000), ("F350", "Sukh", "Alam", "2018/04/05", 56000)]
cur.executemany(query, vals)
__db.commit()

print(cur.rowcount, "records inserted succesfully.")

cur.execute("use coaching")
cur.execute("create table Courses (C_ID VARCHAR(10) primary key, F_ID VARCHAR(10) references Faculty(F_ID), CName VARCHAR(50), Fees FLOAT)")
query = "insert into Courses (C_ID, F_ID, CName, Fees) values (%s, %s, %s, %s)"
vals = [("C453", "F121", "System Design", 17000), ("C198", "F350", "DBMS", 12000), ("C201", "F101", "E-Commerce", 15000)]
cur.executemany(query, vals)
__db.commit()

print(cur.rowcount, "records inserted succesfully.")

__db.close()


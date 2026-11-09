#sql_data_operations_2
#9

import mysql.connector as sql

__db = sql.connect(host = "localhost", user = "root", password = "12345", database = "company")
cur = __db.cursor(buffered = True)


#Display the details of the clients whose city is Kolkata or Chennai
print("Display the details of the clients from Kolkata or Chennai: ")
cur.execute("select * from client where city = 'Kolkata' or city = 'Chennai'")
[print(x) for x in cur.fetchall()]
print("======================================================================")

#To decrease price of product by 5% if the price is more than 50000
print("Decrease price of product by 5% if the price is more than 50000: ")
cur.execute("update product set price = 0.95*price where price > 50000")
__db.commit()
cur.execute("select * from product")
[print(x) for x in cur.fetchall()]
print("======================================================================")

#Display the first two records of the table products
print("Display the first two records from the table product: ")
cur.execute("select * from product")
[print(x) for x in cur.fetchmany(2)]
print("======================================================================")

#Delete the record of the client where the city is Bhopal.
print("Delete the record of the client where the city is Bhopal: ")
cur.execute("delete from client where city = 'Bhopal'")
__db.commit()
cur.execute("select * from client")
[print(x) for x in cur.fetchall()]
print("======================================================================")

#sql_data_operations_main
#8

import mysql.connector as sql

__db = sql.connect(host = "localhost", user = "root", passwd = "12345", database = "coaching")
cur = __db.cursor()

#display the details of the employees with salary more than 12000.
print("Display the details of the employees with salary more than 12000:")
cur.execute("select * from faculty where salary>12000")
[print(i) for i in cur.fetchall()]
print("===================================================================")

#display details of courses whose fees is range 15000-50000
print("Display details of courses whose fees is range 15000-50000:")
cur.execute("select * from courses where fees >= 15000 and fees <= 50000")
[print(i) for i in cur.fetchall()]
print("===================================================================")

#To increase the fees of course system design by 500
print("Increase the fees of course system design by 500:")
cur.execute("update courses set fees = fees + 500 where CName = 'System Design'")
__db.commit()
cur.execute("select * from courses")
[print(i) for i in cur.fetchall()]
print("===================================================================")

#Display the count of usnique F_ID from courses table
print("Display the count of unique F_ID from courses table")
cur.execute("select count(distinct F_ID) from courses")
[print(i) for i in cur.fetchall()]
print("===================================================================")

__db.close()

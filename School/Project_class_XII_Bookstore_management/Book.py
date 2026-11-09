#Bookstore Management System book.py


try : import pymysql as cntr
except ImportError : import mysql.connector as cntr
import datetime as __dt , matplotlib.pyplot as plt
from random import shuffle
from tempfile import mktemp
from os import system , startfile

__db = cntr.connect(host = 'localhost' , user = 'root' , passwd = '12345' , database = 'book_shop')
__cur = __db.cursor(buffered = True)
if str(cntr) == "<module 'pymysql' from 'C:\\\\Program Files (x86)\\\\Python37\\\\lib\\\\site-packages\\\\pymysql\\\\__init__.py'>" :
    __db.autocommit = True
else : __db.autocommit = True
#If buffered is True , the cursor fetches all rows from the server after an operation is executed.

#Function to check is it leap year
is_leapyear = lambda year : year % 4 == 0

#Function to get last date of month
def last_month(month , year):
    if month in (1,3,5,7,8,10,12) : return 31
    elif month == 2 and is_leapyear(year) : return 29
    elif month == 2 : return 28
    else : return 30
    

clrscreen = lambda : system("cls")


def view_stock():
    __cur.execute("select Book_No , Book_Name , Available_Stock from stock")
    data = __cur.fetchall()
    print("Book Number            Book Name                Stock")
    for row in data :
        if len(row[1]) >= 11 : print(row[0] , '           ' , row[1] , '        ' , row[2])
        else : print(row[0] , '     ' , row[1] , '     ' , row[2])

            
def add_stock():           
    print('Add Stock'.center(89 , '='))
    bno = unique_book_no()
    if bno : print("Book Number : " , bno)
    else : bno = int(input("Enter book number : "))
    bname = input("Enter the Book\'s Name : ")
    auth = input("Enter the Author of the Book : ")
    publ = input("Enter the Publisher of the Book : ")
    cost = eval(input("Enter the Cost per Book : "))
    stock = int(input("Enter the Quantity purchased : "))
    __cur.execute("insert into stock values ({} , '{}' , '{}' , '{}' , {} , {} , {} , '{}')".format(bno , bname , auth , publ , cost , stock , 0, __dt.date.today()))
    print("Inserted Sucessfully !!!")
    

        
def add_user():
    user = input("Enter the user name : ")
    passwd = input("Enter a Password : ")
    passwd2 = input("Re-enter Password to confirm : ")
    if passwd == passwd2 :
        __cur.execute("insert into users values('{}' , '{}')".format(user , passwd))
        print("Created Successfully!!!")
    elif passwd != passwd2 : print("You've entered different passwords")
    

        
def sell_book() :
    print('Purchase')
    cname = input("Enter the Customer Name : ")
    phno = int(input("Enter the phone number : "))
    bno = int(input("Enter book number : "))
    bname = input("Enter the name of the book : ")
    cost = eval(input("Enter the cost of the book : "))
    __cur.execute("insert into purchased values({} , '{}')".format(bno , __dt.date.today()))
    __cur.execute("update stock set qty_purchased = qty_purchased + 1 where Book_No = {}".format(bno))
    __cur.execute("update stock set Available_Stock = Available_Stock - 1 where Book_No = {}".format(bno))
    print("Bought Successfully")
    q = '''Book Shop\nName : {}\nPhone No : {}\nBook Number : {}\nBook Name : {}\nCost : {}\nDate Of Purchase : {}'''.format(cname , phno , bno , bname , cost , __dt.date.today())
    filename = mktemp('.txt')
    open(filename , 'w').write(q)
    startfile(filename , 'print')
    #https://docs.python.org/3/library/os.html#os.startfile
    __cur.execute('select Book_Name , Book_No , Author from stock where Available_Stock = 0')
    if __cur.rowcount == 1 :
        print("STOCK OF ")
        print("Book Name : " , __cur.fetchall()[0][0])
        print("Book Number : " , __cur.fetchall()[0][1])
        print("Author : " , __cur.fetchall()[0][2])
        print("EXHAUSTED")
        __cur.execute('delete from stock where Available_Stock = 0')
    
        
        
def unique_book_no () :
    __cur.execute("select max(Book_No) from stock")
    data = __cur.fetchall()
    if bool(data[0][0]) :
        L1 = [x for x in range((data[0][0] + 1) , (data[0][0] + 10000))]
        shuffle(L1)
        return L1.pop(0)
    else : return False


def view_sales () :
    print('Overall Sales This Month')        
    __cur.execute("select distinct(s.Book_Name) , s.qty_purchased from stock s , purchased p where s.Book_No = p.Book_No and p.purchased_on between '{year}-{month}-01' and '{year}-{month}-{date}'".format(year = __dt.date.today().year , month = __dt.date.today().month , date = last_month(__dt.date.today().month , __dt.date.today().year)))
    data = __cur.fetchall()
    L1 , L2 = [] , []
    for row in data :
        L1.append(row[0])
        L2.append(row[1])
    plt.bar(L1 , L2)
    plt.xlabel('Books')
    plt.ylabel('Sales')
    plt.title('Sales')
    plt.show()    

    
def login():
    user = input("Enter the username : ")
    pwd = input("Enter the password : ")
    __cur.execute("select * from users where username = '{}' and password = '{}'".format(user , pwd))
    return bool(__cur.rowcount)


def update_stock() :
    bno = int(input("Enter the book number : "))
    __cur.execute("select Book_Name , Available_Stock from stock where Book_No = {}".format(bno))
    data = __cur.fetchall()
    print("Book Name : " , data[0][0])
    print("Available Stock : " , data[0][1])
    stock = int(input("Enter the new stock purchased : "))
    __cur.execute("update stock set Available_Stock = Available_Stock + {}".format(stock))
    print("Updated Successfully")

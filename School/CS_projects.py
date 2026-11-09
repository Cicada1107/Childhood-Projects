'''
#calculate compound interst

import math as mt
p = int(input("Enter the principal sum: "))
r1 = float(input("Enter the interest rate per annum: "))
t = int(input("Enter the time(in years): "))
n = int(input("Enter the number of interests per year: "))
r = r1/100
x = (r/n)+1
t2 = t*n
y = mt.pow(x, t2)
a = int(p*y)
ci = int(a-p)
print("The compound nterest is: ", ci)
print("The total Amount is: ", a)
'''

'''
#Display the ASCII code of a given character

action = int(input("Please enter the activity: \n1. Input 1 to convert Character to ASCII code\n2. Input 2 for converting AsCII Code to a character\n"))

if action == 1:
    n = input("Enter character: ")
    print("The ASCII code of the given number is: {}".format(ord(n)))
elif action == 2:
        n = int(input("Enter ASCII code: "))
        print("The Character represented by the given ASCII code is: {}".format(chr(n)))
'''

'''
#Check if given input is char, digit or sp char

n = input("Enter desired element: ")

if n.isalpha():
    print("Given input is an alphabet.")
elif n.isdigit():
    print("Given input is a number.")
else:
    print("It is a special character")
'''

'''
#check if given string is a palindrome

my_string = input("Enter a string: ")
if my_string == my_string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is a not a palindrome")
'''

'''
#Find value of sin(x) using taylor series

import math

def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine

x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))

print(round(sin(x,n),2))
'''

'''
#Generate random number between 1-6 for a lottery

import random

n = int(input("Enter a number between 1 and 6: "))

num = random.randint(1, 6)

if n == num:
    print("Congratulations! You have guessed the lottery number!")

elif n != num:
    print("Sorry, the lottery number is: {}. Better luck next time!".format(num))
'''

'''
#Impliment a Bubble sort in a given array

arr = [12, 34, 53, 23, 341, 123, 11, 32, 90, 22]

print("Original list was ", arr)

n = len(arr)

for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array is: {}".format(arr))
'''

'''
#Insertion sort implimentation

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return l

l = [10, 9, 7, 8, 6, 3, 4, 5, 2, 1]

print("The list is: ", l)
print("The sorted list is: ", insertionSort(l))
'''

'''
#Function "interest" to calc.Simple Interest

def interest(p, r, t):
    i = (p*r*t)/100
    return i

p = float(input("Enter Principal sum: "))
r = float(input("Enter Rate per annum: "))
t = float(input("Enter Time in years: "))
print("the Interest generated for the given case is: ", interest(p, r, t))
'''

'''
#Convert octal to other number systems

def convert(n):
    s = str(n)
    d = int(s, 8)
    print("The decimal equivalent of the given number is ", d)
    print("The binry equivalent of the given number is ", bin(d))
    print("The hexadecimal equivalent of the given number is ", hex(d))

n = int(input("Input an octal number: "))
convert(n)
'''

'''
#AP series

def ap(a: int, d: int, n: int):
    print("The first ", n,  "terms of the ap are: ")
    for i in range(n):
        print(a + i*d, end = " ")
    print()
    s = (n/2)*((2*a) + (n-1)*d)
    print("sum of first ", n, "terms is: ", s)

x = int(input("Enter the first term: "))
y = int(input("Enter the common difference: "))
z = int(input("Enter the number of terms to be generated: "))

ap(x, y, z)
'''

'''
#Randomly generated series with n digits

import random

n = int(input("Enter the number of digits: "))

num = ''

step = 1
while step <= n:
    num += str(random.randint(0, 9))
    step += 1

print(int(num))
'''

'''
#Function to return the number with least one's digit

def oner(x, y):
    x, y = str(x), str(y)
    if x[len(x)-1] > y[len(y)-1]:
        return y
    elif x[len(x)-1] < y[len(y)-1]:
        return x
    else:
        return None

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("The number with the least one's digit out of the two given numbers is:", int(oner(a, b)))
'''

'''
#Program to count vowels in given file

file = open(r"D:\Programming\Python\Python_programs\School\Sample.txt", "r")
count = 0
data = file.readlines()
for line in data:
    for word in line:
        for letter in word:
            if letter in "aeiouAEIOU":
                count += 1
print("The total number of vowels in the given file are: {}".format(count))
file.close()
'''

'''
#Program to write lines that don't contain "a" from one file to another

file = open(r"D:\Programming\Python\Python_programs\School\Sample.txt", "r")
target = open(r"D:\Programming\Python\Python_programs\School\Sample_2.txt", "a")

data = file.readlines()
for line in data:
    if 'a' not in line:
        target.write(line)
file.close()
target.close()
'''

'''
#Program to count number of words in a file

count = 0
file = open(r"D:\Programming\Python\Python_programs\School\Sample.txt", "r")
data = file.readlines()
for line in data:
    for word in line:
        count += 1
print("The number of words in the given file is:", count)
file.close()
'''

'''(REJECT)
#Program to find most common words in given file

import json

inp = open(r"D:\Programming\Python\Python_programs\School\Sample.txt", "r")
data = inp.read()
words = data.split()
d = {}
for one in words:
    key = one
    if key not in d:
        count = words.count(key)
        d[key] = count
print("Counting frequency of words in text:")
print(json.dumps(d, indent=2).most_common(1))
inp.close()
'''

'''
file = open("Sample.txt","r")
frequent_word = ""
frequency = 0  
words = []
  
# Traversing file line by line 
for line in file:
      
    # splits each line into
    # words and removing spaces 
    # and punctuations from the input
    line_word = line.lower().replace(',','').replace('.','').split(" ");  
      
    # Adding them to list words
    for w in line_word:  
        words.append(w);  
          
# Finding the max occured word
for i in range(0, len(words)):  
      
    # Declaring count
    count = 1  
      
    # Count each word in the file  
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
  
    # If the count value is more
    # than highest frequency then
    if(count > frequency):  
        frequency = count;  
        frequent_word = words[i];  
  
print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))
file.close();
'''

'''
#No. of lines and size of a file
file = open("Sample.txt","r")
Counter = 0
  
# Reading from file
Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1
        
print("The number of lines in the given file is:", Counter)

print("File size in bytes : ", len(file.read()))
'''

'''
#Store data in a text file
count = int(input("Enter the number of students: "))
fileout = open("marks.txt", "w")
for i in range(count):
    rn = int(input("Enter roll number: "))
    name = str(input("Enter Student name: "))
    marks = int(input("Enter marks scored: "))
    rec = str(rn) + "," + name + str(marks) + '\n'
    fileout.write(rec)
fileout.close()
'''

'''
#Program to write employee no., employee name, salary and department name of the various employees to a binary file

import pickle

def writing():
    fin = open("emp.dat", "wb")
    while True:
        eno = int(input("Enter employee number: "))
        ename = str(input("Enter employee name: "))
        sal = int(input("Enter salary: "))
        dept = str(input("Emter the department"))
        l = [eno, ename, sal, dept]
        pickle.dump(l, fin)
        res = input("Do you want to add? (Y/N)")
        if res != "Y":
            break
    fin.close()

def reading():
    fin = open("emp.dat", "rb")
    try:
        while True:
            l = pickle.load(fin)
            print(l)
    except EOFError:
        print("All contents have been read!!")

writing()
reading()
'''

'''
#Program to access employee record binary file and print the records of only those employees who belong to sales department

import pickle

def searching():
    file = open("emp.dat", "rb")
    try:
        while True:
            l = pickle.load(file)
            if l[3] == "d2":
                print(l)
    except EOFError:
        pass

searching()
'''


'''
#Program that copies the records of employees who belong to d1 department from an existing binary file emp.dat into a new file sales.dat

import pickle

def copy():
    fin = open("emp.dat", "rb")
    fout = open("sales.dat", "wb")
    try:
        while True:
            l = pickle.load(fin)
            if l[3] == "d1":
                pickle.dump(l, fout)
    except EOFError:
        pass

def reading():
    fin = open("sales.dat", "rb")
    try:
        while True:
            l = pickle.load(fin)
            print(l)
    except EOFError:
        pass

copy()
reading()
'''

'''
#program to increase salary by 5000 of those who belong to sales department in emp.dat
import pickle
import os

def modifying():
    fin = open("emp.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            l = pickle.load(fin)
            if l[3] == "sales":
                l[2] += 5000
            pickle.dump(l, fout)
    except EOFError:
        pass
    fin.close()
    fout.close()
    os.remove("emp.dat")#deleting the original file
    os.rename("temp.dat", "emp.dat")

def reading():
    fin = open("emp.dat", "rb")
    try:
        while True:
            l = pickle.load(fin)
            print(l)
    except EOFError:
        pass

print("the original content of the 'emp.dat' file:")
print('-------------------')
reading()
print()
print("Modification in progress...")
print('-------------------')
modifying()
print()
print("The modified content of emp.dat:")
print('-------------------')
reading()
'''

'''
#Program to access a binary file emp.dat and deletes the records of all the people belonging to production

import pickle
import os

def deleting():
    fin = open("emp.dat", "rb")
    fout = open("temp.dat", "wb")
    try:
        while True:
            l = pickle.load(fin)
            if l[3] != "Production":
                pickle.dump(l, fout)
    except EOFError:
        pass
    fin.close()
    fout.close()
    os.remove("emp.dat")#deleting the original file
    os.rename("temp.dat", "emp.dat")

def reading():
    fin = open("emp.dat", "rb")
    try:
        while True:
            l = pickle.load(fin)
            print(l)
    except EOFError:
        pass

print("The original content of the emp.dat file: ")
print("---------------------")
reading()

print()

deleting()
print("The new list is:")
print("---------------------")
reading()
'''

'''
#Read and write csv file by user input records

import csv

def writing():
    file = open("Student_birthday.csv", "w", newline = "\n")
    data_writer = csv.writer(file)
    st_list = ["Name", "Class", "Birthday month"]
    data_writer.writerow(st_list)
    while True:
        name = input("Enter name of student: ")
        Class = input("Enter class of student: ")
        bdmon = input("Enter Birthday month of student: ")
        st_line = [name, Class, bdmon]
        data_writer.writerow(st_line)
        ans = input("Do you want to enter more records?(Y/N) ")
        if ans != "Y" and ans != "y":
            break
    file.close()


def reading():
    file = open("Student_birthday.csv")
    file_reader = csv.reader(file)
    for row in file_reader:
        print(row)


writing()
reading()
'''

'''
#writing a csv file

import csv
fout = open("Student_birthday.csv", "w", newline = "\n")
datawriter = csv.writer(fout, delimiter = ',')
st_list = [["Name", "Class", "Birthday Month"],
           ["Sarvesh Dayal", "XII-A", "November"],
           ["Neha Giri", "XI-C", "February"]]
for x in st_list:
    datawriter.writerow(x)

fout.close()
'''



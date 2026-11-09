#Checking for a palindromic number

n = int(input("Enter a number: "))                #Taking the number as input

if n%10 == 0:
    n = n//10


def split(word):                #For identifying each digit of the number as a string in a list
    return [i for i in word]

l = split(str(n))

pal_str = ''
for i in reversed(l):           #reversing the given number
    pal_str += i



if n == int(pal_str):           #cmparing the given number with it's reversed self
    print("The given number is a palindrome.")
else:
    print("Given number is not a palindrome")

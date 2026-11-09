#Check whether a number is prime or not

n = int(input('Enter the number: '))
flag = False
if n > 1:
    for i in range(2, n):
        if n%i == 0:
            flag = True
            break
if flag:
    print("{} is not a prime number.".format(n))
else:
    print("The given number: {} is a prime number.".format(n))


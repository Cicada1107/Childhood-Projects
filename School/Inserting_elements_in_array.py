#practical practice session 2 inserting elements into an array

l = []

n = int(input("Enter the length of the list to be created: "))
[l.append(int(input("Enter element number {}: ".format(i+1)))) for i in range(n)]
n = int(input("Enter the numebr of new elements to be added: "))
print("Original list: {}".format(l))
[l.append(int(input("Enter element number {} to be inserted: ".format(i+1)))) for i in range(n)]
print("New list: {}".format(l))

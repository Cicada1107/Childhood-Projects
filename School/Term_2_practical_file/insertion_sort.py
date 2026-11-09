#Inserting an element
#2


n = int(input("Enter the length of the array: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element number {}: ".format(i+1))))

print("The original linear list is:", arr)
arr.append(int(input("Enter the element to be inserted into the array: ")))
print("The new list is: {}".format(arr))

#School term 2 lab file
#1

def binary_search(arr, item):
    """Implements binary search on an array"""
    beg = 0
    last = len(arr)-1
    while beg <= last:
        mid = int((beg+last)/2)
        if item == arr[mid]: return mid
        elif item >arr[mid]: beg = mid + 1
        else: last = mid-1
    else: return False

n = int(input("Please enter lenghth of the array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter term {} of the array: ".format(i+1))))
item = int(input("Enter the search element: "))

arr.sort()
index = binary_search(arr, item)

if index:
    print("THe searched element {} is at index {}".format(item, index))
else: print("The searched element {} is not present.".format(item))
    

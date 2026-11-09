#Binary search in a query


def bin(l: list, i):
    """Returns the index of the search element in sorted list if present in the list otherwise returns False"""
    l.sort()
    print("sorted list: {}".format(l))
    low = 0
    high = len(l)-1
    while low <= high:
        index = (low+high)//2
        mid = l[index]
        if mid == i: return index
        elif mid > i: high = index - 1
        elif mid < i: low = index + 1
    else: return False


print(bin([12, 834, 341, 758, 73, 647, 92, 465], 758))

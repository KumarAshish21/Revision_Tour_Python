# Binary search
# l = [10,20,30,40,50,60,70]

def bSearch(l,x):
    low = 0
    high = len(l) - 1
    while low<= high:
        mid = (low+high)//2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid + 1
        else:
            high - 1
    return -1

# left rotate a list by One
# try two methods list slicing and pop adn append
# I/P => lo l1, l2, l3, l4 ......ln-1
def rotateByOne(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x
l = [10,20,30,40,50,60,70,80]
rotateByOne(l)
print(l)


def getOddOccurrence(arr, arr_size):
    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count +=1
        if (count % 2 !=0):
            return arr[i]
    return -1

arr = [2,3,5,4,5,2,4,3,5,2,4,4,2]
n = len(arr)
print(getOddOccurrence(arr, n))
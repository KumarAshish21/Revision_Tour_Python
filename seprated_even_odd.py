def getEvenOdd(l):
    even = []
    odd = []
    for x in l:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd
l = [10,12,11,16]
even,odd=getEvenOdd(l)
print(even,odd)
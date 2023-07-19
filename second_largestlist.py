# Naive Solution
def gerSecMax(l):
    if len(l) <=1:
        return None
    lar = gerMax(l)
    slar = None
    for x in l:
        if x!= lar:
            if slar == None:
                slar = x
            else:
                slar = max(slar,x)

def gerMax(l):
    res = l[0]
    for i in range(1,len(l)):
        res = max(res,l[i])
    return res
l  = [5,20,12,10,20,10,12]
print(gerMax(l))


# Efficeint solution
def getSeMax(l):
    if len(l) <=1:
        return None
    lar = l[0]
    slar = None
    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x!=lar:
            if slar==None or slar<x:
                slar = x
    return slar
l  = [5,20,12,10,20,10,12]
print(getSeMax(l))

def getSecondLargest(l):
    if len(l) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in l:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest

l = [5, 20, 12, 10, 20, 10, 12]
print(getSecondLargest(l))

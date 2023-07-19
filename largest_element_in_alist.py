def getMax(l):
    for x in l:
        for y in l:
            if y > x:
                break
        else:
            return x
    return None
l = [10,20,5,50]
print(getMax(l))


#efficient solution

def getmax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res = l[i]
        return res
l = [10,20,55,50]
print(getMax(l))
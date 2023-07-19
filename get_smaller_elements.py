l = [8,100,20,40,3,7]
m= [100,20,40,60,80,200]
ls = []
ls2 =[]
for i in l:
    if i < 10:
        ls.append(i)
print(ls)

for i in m:
    if i <60:
        ls2.append(i)
print(ls2)

def getSmaller(l,x):
    res = []
    for e in l:
        if e < x:
            res.append(e)
    return res
l = [8,100,20,40,3,7]
x = 10
print(getSmaller(l,x))
l1 = [x for x in range(11) if x % 2 == 0]
print(l1)

l2 = [x for x in range(11) if x % 2 !=0]
print(l2)

def getevenodd(l):
    even = [x for x in l if x%2==0]
    odd = [x for x in l if x%2!=0]
    return even,odd
l = [10,2,4,3,5,7,12]
even,odd = getevenodd(l)
print(even,odd)

s = "ashishchaurasiya"
l1 = [x for x in s if x in 'aeiouu']
print(l1)

l2 = ["ashish","abhishek","komal","kirti"]
l3 = [x for x in  l2 if x.startswith("a")]
print(l3)

l4 = [x*2 for x in range(10)]
print(l4)

l1 = ["geeks", "for", "geeks","gfg","ide"]
l2 = [x.upper() for x in l1 if x.startswith("g")]
print(l2)


# set Comphrensions

# set constant distinct items
l1 = [10,20,3,4,10,20,7,3]
s1 = {x for x in l if x%2 ==0}
s2 = {x for x in l if x%2!=0}
print(s1)
print(s2)

# Dictionary Comphrensions

l1 = [1,3,4,2,5]
d1 = {x:x**3 for x in l1}
print(d1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

l2 = [101, 103,102]
l3 = ["gfg","ide","course"]
# d3 = {l2[i]:l3[i] for i in range(len(l2))}
d3 = dict(zip(l2,l3))
print(d3)

d1 = {101:"ashish", 103:"zbhishek",102:"komal"}
d2 = {v:k for (k,v) in d1.items()}
print(d2)
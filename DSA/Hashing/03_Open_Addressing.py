# Implementation of Open Addressing

class MyHash:
    def __init__(self, c):
        self.cap = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, x):
        return x % self.cap

    def search(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False

    def insert(self, x):
        if self.size == self.cap:
            return False

        if self.search(x) == True:
            return False
        i = self.hash(x)
        t = self.table
        while t[i] not in (-1, -2):
            i = (i + 1) % self.cap

        t[i] = x
        self.size = self.size + 1
        return True

    def remove(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False


h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)

# Python3 program to count distinct
# elements in a given array
 
 
def countDistinct(arr, n):
 
    res = 1
 
    # Pick all elements one by one
    for i in range(1, n):
        j = 0
        for j in range(i):
            if (arr[i] == arr[j]):
                break
 
        # If not printed earlier, then print it
        if (i == j + 1):
            res += 1
 
    return res

def cDistinct(l):
    res = 1
    
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res = res+1
    
    return res
    
l = [10,20,10,30,30,20]

print(cDistinct(l))


def cDistinct2(l):
    return len(set(l))

print(cDistinct2(l))
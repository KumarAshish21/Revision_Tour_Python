# l1 = [5,10,15,1]
# l1.sort()
# print(l1)

# l2 = [1, 5, 3, 10]
# l2.sort(reverse=True)
# print(l2)

# l3 = ['gfg', 'ide', 'courses']
# l3.sort()
# print(l3)

# def myFun(s):
#     return len(s)

# l = ['gfg', 'courses', 'python']
# l.sort(key=myFun)
# print(l)

# l.sort(key=myFun, reverse=True)
# print(l)

class Point:
    def __init__(self, x, Y):
        self.x = x
        self.y = Y
        
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
        
# def myFun(p):
#     return p.x

# l = [Point(1, 15), Point(10, 5), Point(3, 8)]
l = [Point(1, 15), Point(10, 5), Point(1, 8)]
# l.sort(key=myFun)
l.sort()
for i in l:
    print(i.x, i.y)
    
    

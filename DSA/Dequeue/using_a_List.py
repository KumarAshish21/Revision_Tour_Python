# Problem 2 using a List

from collections import deque

d = deque([10,20,30,40])
d.insert(2,10)
print(d.count(10))
d.remove(10)
print(d)
d.extend([50,60])
print(d)
d.extend([15,25])
print(d)
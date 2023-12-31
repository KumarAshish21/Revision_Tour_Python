from collections import deque

d = deque([10,20,30,40,50])
d.rotate(2)
print(d)
d.rotate(-2)
print(d)
d.reverse()
print(d)
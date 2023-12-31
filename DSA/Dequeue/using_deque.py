# Problem 1 using deque

from collections import deque

d = deque()
d.append(10)
d.append(20)
d.append(30)
d.appendleft(40)
print(d)
print(d.pop())
print(d.popleft())
print(d)
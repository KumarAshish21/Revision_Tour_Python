# Linked List Implementation of Deque

# Linked List Implementation of Deque

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        self.prev = None

class MyDeque:
    def __init__(self, c):
        self.front = None
        self.rear = None
        self.sz = 0

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0

    def insertRear(self, x):
        temp = Node(x)
        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear

        self.rear = temp
        self.sz += 1

    def deleteFront(self):
        if self.front is None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return res

    def getFront(self):
        if self.front:
            return self.front.key

    def getRear(self):
        if self.rear:
            return self.rear.key

dq = MyDeque(3)
print(dq.isEmpty())
dq.insertRear(10)
print(dq.getFront(), dq.getRear())
dq.insertRear(20)
print(dq.getFront(), dq.getRear())
dq.insertRear(30)
print(dq.getFront(), dq.getRear())
dq.deleteFront()
print(dq.getFront(), dq.getRear())


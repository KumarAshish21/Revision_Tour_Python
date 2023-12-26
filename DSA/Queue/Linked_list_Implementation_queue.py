"""
In a Queue data structure, we maintain two pointers, front, and rear.
The front points to the first item of the queue and rear points to the last item.

enQueue(): This operation adds a new node after rear and moves rear to the next node
deQueue(): This operation removes the front node and moves front to the next node.


Time Complexity: O(1), The time complexity of both operations enqueue() and dequeue() is O(1) as it only changes a few pointers in both operations.
Auxiliary Space: O(1), Space complexity of both operations enqueue() and dequeue() is O(1) as constant extra space is require
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Queue:

    def __init__(self):
        self.front = self.rear = None

    
    def isEmpty(self):
        return self.front == None
    
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

if __name__ == '__main__':
	q = Queue()
	q.EnQueue(10)
	q.EnQueue(20)
	q.DeQueue()
	q.DeQueue()
	q.EnQueue(30)
	q.EnQueue(40)
	q.EnQueue(50)
	q.DeQueue()
	print("Queue Front : " + str(q.front.data))
	print("Queue Rear : " + str(q.rear.data))
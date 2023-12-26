class Queue:

    def __init__(self, c):

        self.queue = []
        self.front = self.rear = 0
        self.capacity = c


    # Function to insert an element
    # at the rear of the queue

    def queueEnqueue(self, data):
        # check queue is full or not

        if(self.capacity == self.rear):
            print("\nQueue is full")

        # Insert element at the rear
        else:
            self.queue.append(data)
            self.rear += 1

    # Function to delete an element
    # from the front of the queue

    def queueDequeue(self):

        # If queue is empty
        if(self.front == self.rear):
            print("Queue is empty")

        # Pop the front element from list
        else:
            x = self.queue.pop(0)
            self.rear -= 1

    # Function to print queue elements
    def queueDisplay(self):

        if(self.front == self.rear):
            print("\nQueue is Empty")

        # Traverse front to rear to
        # print elements
        for i in self.queue:
            print(i, "<--", end='')

    # Print front of queue
    def queueFront(self):

        if(self.front == self.rear):
            print("\nQueue is Empty")

        print("\nFront Element is:", self.queue[self.front])


if __name__ == '__main__':
    q = Queue(4)
    # display
    q.queueDisplay()
    # Insert
    q.queueEnqueue(20)
    q.queueEnqueue(30)
    q.queueEnqueue(40)
    q.queueEnqueue(50)

    # Print Queue elements
    q.queueDequeue()
    q.queueDequeue()
    print("\n\nafter two node deletion\n")

    q.queueDisplay()

    # Print front of queue
    q.queueFront()


"""
Time Complexity: O(N)
Auxiliary Space: O(N)
"""
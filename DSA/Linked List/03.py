#Search in Linked List:
# Search an element in a Linked List (Iterative and Recursive)
# Search an element in a Linked List (Iterative Approach): 
# Follow the below steps to solve the problem.

"""Examples:

Input: 14->21->11->30->10, X = 14
Output: 0
Explanation: 14 is present in the linked list.

Input: 6->21->17->30->10->8, X = 13
Output: -1
"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        

def search(head, x):
    pos = 1
    curr = head
    while curr != None:
        if curr.key ==None:
            if curr.key == x:
                return pos
            pos = pos + 1
            curr = curr.next
    return -1

head = Node(10)
head.next = Node(15)
head.next.next= Node(20)
head.next.next.next= Node(25)
x = 20
print(search(head, x))




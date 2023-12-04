# Doubly Linked List in Python

"""A Doubly Linked List (DLL) contains an extra pointer, typically called the previous pointer, together with the next pointer and data which are there in the singly linked list.
"""
#  Implementation of Doubly Linked List:

class Node:
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        

def printDill(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
        
    print()




head = Node('A')
temp1 = Node('B')
temp2 = Node('C')

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1




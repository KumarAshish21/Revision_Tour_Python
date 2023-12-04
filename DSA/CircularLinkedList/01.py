"""A Linked List is a popular data structure which is used to store elements. It is a linear data structure. It contains nodes that have a pointer to store the address of the next node and data which is the value of that node. Circular Linked List is a type of linked list that is circular in nature. In a circular linked list, every node has successor. In this data structure, every node points to the next node and the last node of the linked list points to the first node. This feature makes it circular in nature. It is essential to know that the circular linked lists have no end and we need to be careful while traversing the linked list. 

Advantages of Circular Linked Lists:

It is possible to traverse from the last node back to the first i.e. the head node.
The starting node does not matter as we can traverse each and every node despite whatever node we keep as the starting node.
The previous node can be easily identified.
There is no need for a NULL function to code. The circular list never identifies a NULL identifier unless it is fully assigned.
Circular linked lists are beneficial for end operations as start and finish coincide. 
Algorithms such as Round Robin setup can effectively complete online queues without having to meet NULL suspension or reference references.
Disadvantages of Circular Linked Lists:

If the circular linked list is not handled properly then it can lead to an infinite loop as it is circular in nature.
In comparison with singly-linked lists, doubly linked lists are more complex in nature
Direct accessing of elements is not possible.
It is generally a complex task to reverse a circular linked list.

If Circular Linked List Contains more than one element then we have to traverse on al the the element for example:


"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        
def printCircular(head):
    if head == None:
        return
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
printCircular(head)
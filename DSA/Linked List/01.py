"""
    Representation of Linked Lists: 
    A linked list is represented by a pointer to the first node of the linked list. The first node is called the head of the linked list. If the linked list is empty, then the value of the head points to NULL. 

Each node in a list consists of at least two parts: 

A Data Item (we can store integer, strings, or any type of data).
Pointer (Or Reference) to the next node (connects one node to another) or An address of another node
"""

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None
        
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2
temp2.next = temp3

head = temp1
print(head.key)
print(head.next.key)
print(head.next.next.key)

# Applications of Linked List
#1 Worst case insertion at the end and begin are θ(1)
#2 Worst case deletion from the beginning is θ(1)
#3 Insertions and deletions in the middle are θ(1) if we have reference to the previous node.
#4 Round Robin Implementation
#5 Merging two sorted linked lists is faster then arrays
#6 Implementation of simple memory manager where we need to link free blocks
#7 Easier implementation of Queue and Dequeue data  structures.
"""
        Applications of linked list in computer science:
        
Implementation of stacks and queues
Implementation of graphs: Adjacency list representation of graphs is the most popular which uses a linked list to store adjacent vertices.
Dynamic memory allocation: We use a linked list of free blocks.
Maintaining a directory of names
Performing arithmetic operations on long integers
Manipulation of polynomials by storing constants in the node of the linked list
representing sparse matrices
Applications of linked list in the real world:


Image viewer – Previous and next images are linked and can be accessed by the next and previous buttons.
Previous and next page in a web browser – We can access the previous and next URL searched in a web browser by pressing the back and next buttons since they are linked as a linked list.
Music Player – Songs in the music player are linked to the previous and next songs. So you can play songs either from starting or ending of the list.
"""
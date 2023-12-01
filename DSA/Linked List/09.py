# Sorted Insert Linked List in Python
"""We have discussed Insertion Sort for arrays. In this article we are going to discuss Insertion Sort for linked list. 
Below is a simple insertion sort algorithm for a linked list.
1) Create an empty sorted (or result) list.
2) Traverse the given list, do following for every node.
......a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list
"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        
def sortedInsert(head, x):
    temp = Node(x)
    
    if head == None:
        return temp
    
    elif x < head.key:
        temp.next = head
        return temp
    else:
        curr = head
        
        while curr.next != None and curr.next.key < x:
            curr = curr.next
            
        temp.next = curr.next
        curr.next = temp
        
        return head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

h = head
while h != None:
    print(h.key)
    h = h.next
print()

h = sortedInsert(head, 35)
h = head

while h != None:
    print(h.key)
    h = h.next
    
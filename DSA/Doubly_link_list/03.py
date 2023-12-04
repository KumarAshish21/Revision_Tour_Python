# Insert at the Beginning of DLL in Python
"""Add a node at the front:
The new node is always added before the head of the given Linked List. And newly added node becomes the new head of DLL. For example, if the given Linked List is 1->0->1->5 and we add an item 5 at the front, then the Linked List becomes 5->1->0->1->5. Let us call the function that adds at the front of the list push(). The push() must receive a pointer to the head pointer because the push must change the head pointer to point to the new node 
"""
    
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def InsertBegin(head, x):
    temp = Node(x)
    
    if head != None:
        head.prev = temp
        
    temp.next = head
    temp.prev = None
    
    return temp

def printDll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
head.next = temp2
temp2.prev = temp1

printDll(head)
head = InsertBegin(head,4)
printDll(head)


    
    
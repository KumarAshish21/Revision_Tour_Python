# Insert at the End of DLL in Python
"""The new node is always added after the last node of the given Linked List. For example, if the given DLL is 5->1->0->1->5->2 and we add item 30 at the end, then the DLL becomes 5->1->0->1->5->2->30. Since a Linked List is typically represented by its head of it, we have to traverse the list till the end and then change the next of last node to the new node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
def insertEnd(head,x):
    
    temp = Node(x)
    
    if head == None:
        return temp
    
    else:
        
        curr = head
        while curr.next != None:
            curr = curr.next
            
        curr.next = temp
        temp.prev = curr
        
        return head
    
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
temp1.next = temp2
temp2.prev = temp1

printDll(head)
head = insertEnd(head,40)
printDll(head)
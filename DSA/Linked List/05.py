# Delete First Node Of Linked List in Python
"""
    Point head to the next node i.e. second node
    temp = head
    head = head->next
    
Make sure to free unused memory
    free(temp); or delete temp;
"""

class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
        
def delFirst(head):
    if head == None:
        return None
    else:
        return head.next
    
def printList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
    print()
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)
head = delFirst(head)
printList(head)
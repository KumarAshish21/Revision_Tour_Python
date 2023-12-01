#Traveral Linked List
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
    
def printList(head):
    curr = head
    while curr!=None:
        print(curr.key)
        curr= curr.next
        

head = Node(10)
head.next  = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

printList(head)

# Time Complexity = 0(n)
# Auxilary Space= 0(n)
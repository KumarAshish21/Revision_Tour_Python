# Delete Head of A Doubly Linked List


class Node:
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delHead(head):
    if head == None:
        return None
    
    if head.next == None:
        return None
    
    else:
        new_head = head.next
        new_head.prev = None
        return new_head

def printDll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

head = Node(2)
temp1 = Node(45)
temp2 = Node(3)
temp3 = Node(1)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

temp2.next = temp3
temp3.prev = temp2

printDll(head)

head = delHead(head)

printDll(head)

# Middle of Linked List
"""
    Find the middle of a given linked list

Given a singly linked list, find the middle of the linked list. For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4. 

Method 1: Traverse the whole linked list and count the no. of nodes. Now traverse the list again till count/2 and return the node at count/2. 
Below is the implementation of the above approach:

Time Complexity: O(n) where n is no of nodes in linked list

Auxiliary Space: O(1)




"""
class Node:
    def __init__(self, k):
        self.data = k
        self.next = None
        
def printList(head):
    curr = head
    
    while curr != None:
        print(curr.data)
        curr = curr.next
        
    print()
    
    
def printMiddle(ptr):
    if head == None:
        return
    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1
    
    curr = head
    for i in range(count//2):
        curr = curr.next
        
    print(curr.data)
    
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)

printList(head)
printMiddle(head)


"""Method 2: Traverse linked list using two-pointers. Move one pointer by one and the other pointers by two. When the fast pointer reaches the end, the slow pointer will reach the middle of the linked list
"""

class Node:
    def __init__(self, k):
        self.data = k
        self.next = None
        
def printList(head):
    curr = head
    
    while curr !=  None:
        print(curr.data)
        curr = curr.next
    print()
    
    
def printMiddle(ptr):
    if head == None:
        return
    slow = head
    fast = head
    while fast!= None and fast.next!= None:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)
    
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
printMiddle(head)
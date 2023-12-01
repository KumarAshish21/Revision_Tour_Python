# Insert At The Beginning of Linked list in Python
"""Approach: The new node is always added before the head of the given Linked List. And newly added node becomes the new head of the Linked List. For example, if the given Linked List is 10->15->20->25 and we add an item 5 at the front, then the Linked List becomes 5->10->15->20->25. Let us call the function that adds at the front of the list is push(). The push() must receive a pointer to the head pointer because the push must change the head pointer to point to the new node
"""

# Time Complexity: O(1), We have a pointer to the head and we can directly attach a node and change the pointer. So the Time complexity of inserting a node at the head position is O(1) as it does a constant amount of work.
# Auxiliary Space: O(1)

class Node:
    def __init___(self,key):
        self.key =key
        self.next = None
        
def insertBegin(head,key):
    temp=Node(key)
    temp.next = head
    return temp


head  = None
head = insertBegin(head,10)
head = insertBegin(head,20)
head = insertBegin(head,30)


def PrintList(head):
    curr= head
    while curr!=None:
        print(curr.key)
        curr = curr.next
        
PrintList(head)
# Delete a node with pointer given to it
"""Given only a pointer to a node to be deleted in a singly linked list, how do you delete it?

A simple solution is to traverse the linked list until you find the node you want to delete. But this solution requires a pointer to the head node which contradicts the problem statement. 

The fast solution is to copy the data from the next node to the node to be deleted and delete the next node. Something like this:

It is important to note that this approach will only work if it is guaranteed that the given pointer does not point to the last node. Because if it is the last node, then you don’t have a next node to copy the data from.

struct Node *temp  = node_ptr->next;
node_ptr->data  = temp->data;
node_ptr->next  = temp->next;
free(temp);
"""

class Node:
    def  __init__(self,k):
        self.data = k
        self.next = None
        
def printList(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
        
    print()
    
def deleteNode(ptr):
    temp = ptr.next
    ptr.data = temp.data
    
    ptr.next = temp.next
    
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)

printList(head)
deleteNode(head)
printList(head)
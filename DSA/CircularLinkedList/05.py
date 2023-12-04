# Delete Kth Node of Circular Linked List

"""
Given a Circular Linked List. The task is to write programs to delete nodes from this list present at: 



 

First position.
Last Position.
At any given position 
.
Deleting first node from Singly Circular Linked List


 

Examples:  



 

Input : 99->11->22->33->44->55->66
Output : 11->22->33->44->55->66

Input : 11->22->33->44->55->66
Output : 22->33->44->55->66

Approach: 



 

Take two pointers current and previous and traverse the list.
Keep the pointer current fixed pointing to the first node and move previous until it reaches the last node.
Once, the pointer previous reaches the last node, do the following: 
previous->next = current-> next
head = previous -> next;

"""

# Take two pointers current and previous and traverse the list.
# Function to delete last node of
# Circular Linked List
def DeleteLast(head):
    current = head
    temp = head
    previous = None

    # check if list doesn't have any node
    # if not then return
    if (head == None):
        print("\nList is empty")
        return None

    # check if list have single node
    # if yes then delete it and return
    if (current.next == current):
        head = None
        return None

    # move first node to last
    # previous
    while (current.next != head):
        previous = current
        current = current.next

    previous.next = current.next
    head = previous.next

    return head

# Deleting nodes at given index in the Circular linked list
 

# First, find the length of the list. That is, the number of nodes in the list.
# Take two pointers previous and current to traverse the list. Such that previous is one position behind the current node.
# Take a variable count initialized to 0 to keep track of the number of nodes traversed.
# Traverse the list until the given index is reached.
# Once the given index is reached, do previous->next = current->next.
# Function to delete last node of
# Circular Linked List
def DeleteLast(head):
    current = head
    temp = head
    previous = None

    # check if list doesn't have any node
    # if not then return
    if (head == None):
        print("\nList is empty")
        return None

    # check if list have single node
    # if yes then delete it and return
    if (current.next == current):
        head = None
        return None

    # move first node to last
    # previous
    while (current.next != head):
        previous = current
        current = current.next

    previous.next = current.next
    head = previous.next

    return head


# # Deleting nodes at given index in the Circular linked list
# First, find the length of the list. That is, the number of nodes in the list.
# Take two pointers previous and current to traverse the list. Such that previous is one position behind the current node.
# Take a variable count initialized to 0 to keep track of the number of nodes traversed.
# Traverse the list until the given index is reached.
# Once the given index is reached, do previous->next = current->next.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delHead(head):
    if head == None:
        return None
    elif head.next == head:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next

        return head


def delKth(head, k):
    if head == None:
        return head

    elif k == 1:
        return delHead(head)

    else:
        curr = head

        for i in range(k - 2):
            curr = curr.next

        curr.next = curr.next.next
        return head


def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
head.next.next.next.next = head

printCircular(head)

head = delKth(head, 4)

printCircular(head)
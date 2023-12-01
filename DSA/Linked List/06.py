# Insert at Given Position in Singly Linked list

"""Add a node after a given node: (5 steps process) 
Approach: We are given a pointer to a node, and the new node is inserted after the given node.

Follow the steps to add a node after a given node:

Firstly, check if the given previous node is NULL or not.
Then, allocate a new node and
Assign the data to the new node
And then make the next of new node as the next of previous node. 
Finally, move the next of the previous node as a new node.

Complexity Analysis: 

Time complexity: O(1), since prev_node is already given as argument in a method, no need to iterate over list to find prev_node
Auxiliary Space: O(1) since using constant space to modify pointers



"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertPos(head,data,pos):

    temp = Node(data)

    if pos ==1:
        temp.next = head
        return temp
    curr = head

    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head

    temp.next = curr.next
    curr.next = temp

    return head


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
head.next.next.next.next = Node(50)

printList(head)

head = insertPos(head,45,4)

printList(head)
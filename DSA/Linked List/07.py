# Delete Last Node of Linked List

"""Point head to the previous element i.e. last second element
    Change next pointer to null
    struct node *end = head;
    struct node *prev = NULL;
    while(end->next)
    {
        prev = end;
        end = end->next;
    }
    prev->next = NULL;
    
Make sure to free unused memory
    free(end); or delete end;
"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        
def deleteNode(head):
    if head == None:
        return None
    
    if head.next == None:
        return None
    
    curr = head
    
    while curr.next.next != None:
        curr = curr.next
        
    
    curr.next = None
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

printList(head)
head = deleteNode(head)
printList(head)
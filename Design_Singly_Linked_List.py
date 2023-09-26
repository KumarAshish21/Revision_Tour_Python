"""
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1
        if curr is None or curr.next is None:
            return False
        curr.next = curr.next.next
        return True

    def getValues(self):
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

# Input
# operations = ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
operations = ["insertHead", 1, "insertHead", 2, "get", 5]

# Create a LinkedList instance
linked_list = LinkedList()

# Output list to store results
output = []

# Process the operations
for i in range(0, len(operations), 2):
    operation = operations[i]
    if operation == "insertHead":
        value = operations[i + 1]
        linked_list.insertHead(value)
        output.append(None)
    elif operation == "insertTail":
        value = operations[i + 1]
        linked_list.insertTail(value)
        output.append(None)
    elif operation == "remove":
        index = operations[i + 1]
        result = linked_list.remove(index)
        output.append(result)
    elif operation == "getValues":
        values = linked_list.getValues()
        output.append(values)

print(output)

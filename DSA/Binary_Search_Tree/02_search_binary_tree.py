# Search in BST


class Node:
    def  __init__(self,data):
        self.data = data
        self.left= None
        self.right = None
def searchIterative(root,key):
    curr = root
    
    parrent = None
    
    
    while curr and curr.data != key:
        parrent = curr
        
        
        if key < curr.data:
            curr = curr.left
            
        else:
            curr = curr.right
            
        return curr
    
    
def search(root, key, parent):
    # if the key is not present in the tree
    if root is None:
        print('Key not found')
        return

    # if the key is found
    if root.data == key:
        if parent is None:
            print(f'The node with key {key} is the root node')
        elif key < parent.data:
            print(f'The given key is the left node of the node with key {parent.data}')
        else:
            print(f'The given key is the right node of the node with key {parent.data}')
    else:
        # recursively search in the left or right subtree based on the key
        if key < root.data:
            search(root.left, key, root)
        else:
            search(root.right, key, root)
            
    
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)

result = searchIterative(root, 4)
result1 = search(root,3, None)

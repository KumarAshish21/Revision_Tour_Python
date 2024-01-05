# hight of binary tree

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k
        
    
def height(root):
    if root == None:
        return 0
    
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh,rh) +1
    
def height_binary(root):
    if root == None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1
    
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
print(height_binary(root))
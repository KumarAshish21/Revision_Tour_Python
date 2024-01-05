"""
Print Node at K distance
Nodes at distance k from the root are basically the nodes at (k+1)th level of the Binary Tree.
In this video, we discuss a function that takes root and k as a parameter, whose return type is void and is supposed to print the nodes at distance k from the root.
"""
class Node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.key = x
        
    
def printkdist(root, k):
    if root is None:
        return
    
    if k == 0:
        print(root.key, end=" ")
        
    else:
        printkdist(root.left,k-1)
        printkdist(root, k-1)
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)

printkdist(root,2)
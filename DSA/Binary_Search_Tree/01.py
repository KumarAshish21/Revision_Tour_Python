# Binary Search Tree
"""Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
The left and right subtree each must also be a binary search tree. There must be no duplicate nodes.

Sample Binary Search Tree:
200px-Binary_search_tree.svg




The above properties of Binary Search Tree provide an ordering among keys so that the operations like search, minimum and maximum can be done fast in comparison to normal Binary Trees. If there is no ordering, then we may have to compare every key to search a given key.

 nsertion of a Key


Inserting a new node in the Binary Search Tree is always done at the leaf nodes to maintain the order of nodes in the Tree. The idea is to start searching the given node to be inserted from the root node till we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.

For Example:
 

         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500 
     /  \                              /  \  
    10   30                           10   30
                                              \   
                                              40https://media.geeksforgeeks.org/wp-content/uploads/BSTSearch.png
 

Illustration to insert 2 in the below tree:
 

Start from root.
Compare the element to be inserted with root, if it is less than root, then recur for left-subtree, else recur for right-subtree.
After reaching end,just insert that node at left(if less than current leaf node) else right.

bstsearch

 

Element to be inserted: 2

Step 1: Compare 2 with 8.
        Since 2 is less than 8, 
        move to left subtree.
Step 2: Compare 2 with 3.
        Since 2 is less than 3, 
        move to its left subtree.
Step 3: Comapre 2 with 1.
        Since 2 is greater than 1 and also 1 is a leaf node.
        Insert 2 as its right child of node 1.


Time Complexity: The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. In the worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).


"""
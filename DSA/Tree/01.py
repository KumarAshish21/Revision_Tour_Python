class BinarySearchTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data == data:
            return  # node already exists
        
        if data < self.data:
            if self.left:
                # insert into left subtree
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                # insert into right subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
    def search(self, val):
        if self.data == val:
            return True

        if type(val) != type(self.data):
            return False

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current.data

    def calculate_sum(self):
        sum_values = self.data
        if self.left:
            sum_values += self.left.calculate_sum()
        if self.right:
            sum_values += self.right.calculate_sum()
        return sum_values

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # Node with two children
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    print("Building tree with: ", elements)
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root        

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print(root.in_order_traversal())
    print(root.search(23))
    
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    print(root.search("Japan"))
    print("Minimum Element:", root.find_min())
    print("Maximum Element:", root.find_max())
    print("Sum of all elements:", root.calculate_sum())
    print("Post-order Traversal:", root.post_order_traversal())
    print("Pre-order Traversal:", root.pre_order_traversal())


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        #left, root, right
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        #base node
        elements.append(self.data)

        #right node
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements

    def pre_order_traversal(self):
        #root, left, right
        elements = []

        #base node:
        elements.append(self.data)

        #left node:
        if self.left:
            elements += self.left.pre_order_traversal()

        #right node:
        if self.right:
            elements += self.right.pre_order_traversal()
       
        return elements

    def post_order_traversal(self):
        elements = []

        #left node
        if self.left:
            elements += self.left.post_order_traversal()

        #right node
        if self.right:
            elements += self.right.post_order_traversal()

        #base node:
        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data


    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            #value might be in subtree
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            #value might be in right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())

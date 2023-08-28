class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root == new_node
            return True
        temp = self.root
        while (True):
            # Cannot insert a node if value already there
            if new_node.value == temp.value:
                return False
            # Less than, go left
            if new_node.value < temp.value:
                # Spot on left is open
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Spot on left is not open
                # Moves the pointer down a level
                # Loop again at this next level
                temp = temp.left
            # Greater than, go right
            else:
                # Spot on right is open
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Spot on right is not open
                # Moves the temp pointer down a level
                # While loop continues until spot open
                temp = temp.right
    
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
# my_tree.insert(3)

print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

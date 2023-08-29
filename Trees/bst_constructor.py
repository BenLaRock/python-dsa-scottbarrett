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
            self.root = new_node
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

    def contains(self, value):
        # if self.root is None: # not actually needed
        #     return False
        temp = self.root
        while temp is not None:
            # go left if less than temp
            if value < temp.value:
                temp = temp.left
            # go right if more than temp
            elif value > temp.value:
                temp = temp.right
            # value equals temp
            # value will never hit the else if not found
            # bc while loop will go down another level
            # and eventually temp will be None (break loop)
            else: 
                return True
        # if temp becomes none, while loop breaks
        # need to return false because value not in tree
        return False

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

print(my_tree.contains(3))
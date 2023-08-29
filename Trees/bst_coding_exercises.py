class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            # new value already exists in BST
            if new_node.value == temp.value:
                return False
            # value less than temp value current level
            if new_node.value < temp.value:
                # left child spot is open
                if temp.left is None:
                    temp.left = new_node
                    return True
                # left child spot NOT open (move down level)
                temp = temp.left
            elif new_node.value > temp.value:
                # right child spot is open
                if temp.right is None:
                    temp.right = new_node
                    return True
                # right child spot NOT open (move down level)
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            # less then current, go left
            if value < temp.value:
                temp = temp.left
            # greater than current, go right
            elif value > temp.value:
                temp = temp.right
            else: # value == temp
                return True
        # if made it through loop and temp became None
        # then value not in BST
        return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""
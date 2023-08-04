class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None 

        # Still need access to tail as temp both 1 or more items remainin
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1 
        return temp
        
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            # Range is from end index to provide index
            # Then decrement on each loop
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):       
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        # Connect new node to before node
        before.next = new_node
        new_node.prev = before
        # Connect new node to after node
        after.prev = new_node
        new_node.next = after

        self.length += 1
        return True



my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

my_doubly_linked_list.insert(2, 4)

my_doubly_linked_list.print_list()
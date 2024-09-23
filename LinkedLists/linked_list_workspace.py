class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("popped: ", my_linked_list.pop().value)
# print("popped: ", my_linked_list.pop().value)
# print("popped: ", my_linked_list.pop().value)
# print("popped: ", my_linked_list.pop().value)

print(
    "head: ", 
    my_linked_list.head, 
    # "head.next: ", 
    # my_linked_list.head.next
    )
print(
    "tail: ", 
    my_linked_list.tail, 
    # "tail.next: ", 
    # my_linked_list.tail.next
    )
# # my_linked_list.print_list()
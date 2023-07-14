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
    
    def __str__(self):
        return (
            f"Head node: {self.head}\n" +
            f"Head value: {self.head.value}\n" +
            f"Head next: {self.head.next}\n" +
            f"Tail node: {self.tail}\n" +
            f"Tail value: {self.tail.value}\n" +
            f"Tail next: {self.tail.next}\n\n"
            f"Number of nodes: {self.length}"
        )

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
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # return none when empty
        if self.length == 0:
            return None


        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next # keep temp 1 step ahead of pre
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # when already popped down to 1 item left
        if (self.length == 0):
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True

    # def insert(self, value):
    #     pass

linked_list = LinkedList(2)
linked_list.append(3)
linked_list.prepend(1)

linked_list.print_list()
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
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
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        self.tail = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
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
            for _ in range(0, index):
                temp = temp.next
        elif index >= self.length / 2:
            temp = self.tail
            for _ in range(self.length-1 , index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True

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
        # Connect new node's pointers to before and after
        new_node.prev = before
        new_node.next = after
        # Connect before and after's pointers to new node
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        print("index: ", index)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            print("pop()")
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def swap_first_last(self):
        # # Original code
        # if self.head is None:
        #     return False
        # if self.length == 1:
        #     return False
        # first = self.head.value
        # last = self.tail.value
        # self.head.value = last
        # self.tail.value = first
        # return True

        # # Streamlined
        # Empty list or 1 node
        if self.head is None or self.head == self.tail:
            return
        # 1-line 2 variable swap
        self.head.value, self.tail.value = self.tail.value, self.head.value
        
    def reverse(self):
        if self.head is None or self.head == self.tail:
            return
        # current_node = self.head
        # while current_node is not None:
        #     print("current_node: ", current_node.value)

        #     # Keeps a reference to the original next node
        #     temp_next = current_node.next
        #     print("Original next node (pre reverse): ", temp_next)

        #     # Flip next and prev pointers for current node
        #     # Next now points at what was *prev* node
        #     current_node.next = current_node.prev
        #     print("current_node.next: ", current_node.next)

        #     # Prev now points at what was original *next* node
        #     current_node.prev = temp_next
        #     print("current_node.prev: ", current_node.prev)

        #     # Move current node along to traverse the list
        #     current_node = temp_next
        #     print()
        # Swap head and tail pointers

        # Even more concise
        temp = self.head
        while temp is not None:
            # Flip the pointers
            temp.next, temp.prev = temp.prev, temp.next
            # Move along (prev is actually the orig next)
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self):
        # Should check without reversing the list
        # 1-item list is always palindrome
        if self.length <= 1:
            return True
        
        # The way this works is you have 2 pointers 
        # that point to head and tail. Then you loop
        # through the halfway point (no need to go further
        # as you are also stepping back from tail each time; 
        # eventually pointers meet in the middle) and check
        # if head and tail values are equal.
        forward_node = self.head
        backward_node = self.tail
        for i in range(self.length // 2):
            print("i: ", i)
            print("forward_node.value: ", forward_node.value)
            print("backward_node.value: ", backward_node.value)
            if forward_node.value != backward_node.value:
                return False
            forward_node = forward_node.next
            backward_node = backward_node.prev
        return True

    def swap_pairs(self):
        if self.head is None:
            return None
        if self.length == 1:
            return self

        dummy = self.head
        prev = dummy

        for i in range(self.length // 2):
            print("i: ", i)

            first_node = dummy
            second_node = first_node.next
            
            prev.next = second_node
            first_node.next = second_node.next

            second_node.next = first_node

            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next is not None:
                first_node.next.prev = first_node
            
            self.head = first_node.next
            prev = first_node

            self.head = dummy.next
            if self.head is not None:
                self.head.prev = None
            print()
        print()
        

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
# my_dll.append(5)
# my_dll.append(6)


print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


# """
#     EXPECTED OUTPUT:
#     ----------------
#     my_dll before swap_pairs:
#     1
#     2
#     3
#     4
#     my_dll after swap_pairs:
#     2
#     1
#     4
#     3

# """
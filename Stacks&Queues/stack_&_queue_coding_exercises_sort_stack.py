class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




def sort_stack(my_stack):
    sorted_stack = Stack()

    while not my_stack.is_empty():
        temp = my_stack.pop()
        # print("temp: ", temp)
        # Iterate through the new stack and if the top item is > temp from input stack...
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            # pop it from new stack...
            popped = sorted_stack.pop()
            # and push it onto the input stack
            my_stack.push(popped)
        # After the loop push temp into new stack
        sorted_stack.push(temp)
    
    # Pop back from new stack  to input stack
    # These were pushed onto the stack in ascending value (smallest on bottom, greatest on top of stack)
    while not sorted_stack.is_empty():
        popped = sorted_stack.pop()
        print("popped: ", popped)
        my_stack.push(popped)

    return my_stack




my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
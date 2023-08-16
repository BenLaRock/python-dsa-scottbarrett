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


# # My attempt (overcomplicated)
# def reverse_string(my_string):
#     stack = Stack()
#     for i in my_string:
#         stack.push(i)
#     return "".join([stack.pop() for i in range(stack.size())])

# Actual solution
def reverse_string(my_string):
    stack = Stack()
    reversed_string = ""
    for i in my_string:
        stack.push(i)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string
    

my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""

# # ---------- Stack ----------
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Stack:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         self.height = 1

#     def print_stack(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.top
#         self.top = new_node
#         self.height += 1

#     def pop(self):
#         if self.height == 0:
#             return None
#         temp = self.top
#         self.top = self.top.next
#         temp.next = None
#         self.height -= 1
#         return temp

# # ---------- Queue ----------
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1

#     def print_queue(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def enqueue(self, value):
#         new_node = Node(value)
#         if self.first is None:
#             self.first = new_node
#             self.last = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1
#         return True

#     def dequeue(self):
#         if self.length == 0:
#             return None
#         temp = self.first
#         if self.length == 1:
#             self.first = None
#             self.last = None
#         else:
#             self.first = self.first.next
#             temp.next = None
#         self.length -= 1
#         return temp

# ---------- Leetcode Exercises ----------
class Stack: # implmented with list not linked list
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()

test_case = ")()"
def is_balanced_parentheses(test_case):
    stack = Stack()
    
    for i in (test_case):
        print("i getting pushed onto stack: ", i)
        stack.push(i)

    if stack.size() == 0 or stack.is_empty() == True:
        return True
    
    num_open_parens = 0
    num_close_parens = 0

    while not stack.is_empty():
        popped = stack.pop()
        print("popped: ", popped)

        # Cannot have an unmatched num_close_parens paren
        if popped == "(": # remember, coming off in reverse of input string
            return False
        
        if popped == "(":
            num_open_parens += 1
        elif popped == ")":
            num_close_parens += 1

    print("open: ", num_open_parens)
    print("closed: ", num_close_parens)

    if num_open_parens != num_close_parens:
        return False
    return True
        

print("is balanced? ", is_balanced_parentheses(test_case))

# def test_is_balanced_parentheses():
#     try:
#         assert is_balanced_parentheses('((()))') == True
#         print('Test case 1 passed')
#     except AssertionError:
#         print('Test case 1 failed')

#     try:
#         assert is_balanced_parentheses('()') == True
#         print('Test case 2 passed')
#     except AssertionError:
#         print('Test case 2 failed')

#     try:
#         assert is_balanced_parentheses('(()())') == True
#         print('Test case 3 passed')
#     except AssertionError:
#         print('Test case 3 failed')

#     try:
#         assert is_balanced_parentheses('(()') == False
#         print('Test case 4 passed')
#     except AssertionError:
#         print('Test case 4 failed')

#     try:
#         assert is_balanced_parentheses('())') == False
#         print('Test case 5 passed')
#     except AssertionError:
#         print('Test case 5 failed')

#     try:
#         assert is_balanced_parentheses(')(') == False
#         print('Test case 6 passed')
#     except AssertionError:
#         print('Test case 6 failed')

#     try:
#         assert is_balanced_parentheses('') == True
#         print('Test case 7 passed')
#     except AssertionError:
#         print('Test case 7 failed')

#     try:
#         assert is_balanced_parentheses('()()()()') == True
#         print('Test case 8 passed')
#     except AssertionError:
#         print('Test case 8 failed')

#     try:
#         assert is_balanced_parentheses('(())(())') == True
#         print('Test case 9 passed')
#     except AssertionError:
#         print('Test case 9 failed')

#     try:
#         assert is_balanced_parentheses('(()()())') == True
#         print('Test case 10 passed')
#     except AssertionError:
#         print('Test case 10 failed')

#     try:
#         assert is_balanced_parentheses('((())') == False
#         print('Test case 11 passed')
#     except AssertionError:
#         print('Test case 11 failed')

# test_is_balanced_parentheses()
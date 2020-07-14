"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         while len(self.storage) > 0:
#             return self.storage.pop()

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack.__len__() == 0:
            pass
        else:
            value = self.stack[len(self.stack) - 1]
            self.stack.pop()
            return value


class Empty_error(Exception):
    pass


class Linked_Stack:
    class Node:
        def __init__(self, element, _next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Empty_error('this stack is empty, cannot pop')
        result = self.head.element
        self.head = self.head._next
        self.size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise Empty_error('this stack is empty, cannot add')
        return self.head.element

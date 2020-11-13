"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the
underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# from singly_linked_list import LinkedList


# class Stack():
#     def __init__(self):
#         # super().__init__()
#         self.size = 0
#         self.sll = LinkedList()
#         self.sll.head = None

#     def len(self):
#         return self.size

#     def push(self, value):
#         self.sll.add_to_tail(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return None
#         elif self.size == 1:
#             value = self.sll.head.value
#             self.sll.head = None
#             self.sll.tail = None
#             self.size -= 1
#             return value
#         elif self.size == 2:
#             self.size -= 1
#             return self.sll.remove_tail()
#         else:
#             value = self.sll.tail.value
#             self.size -= 1
#             current = self.sll.head
#             while current.next_node.get_next_node() is not None:
#                 current = current.next_node
#             self.sll.tail = current
#             self.sll.tail.set_next_value = None
#             return value


class Stack():
    def __init__(self):
        self.stack = []
        # self.sll = LinkedList()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.__len__() > 0:
            return self.stack.pop()
        else:
            return None

    def __len__(self):
        return len(self.stack)

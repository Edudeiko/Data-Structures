"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
import os
sys.path.append("../singly_linked_list")

# import inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)
from singly_linked_list.singly_linked_list import LinkedList

class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
    
    def len(self):
        return self.size

    def enqueue(self, value):
        if value != None:
            self.add_to_tail(value)
            self.size +=1

    def dequeue(self):
            self.size -= 1
            return self.remove_head()

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''Insert the given value into the tree'''
        # RECURSIVE
        if value >= self.value:  # go right (dupes go to the right)
            if self.right is None:
                self.right = BSTNode(value)
                return
            else:
                return self.right.insert(value) # recursive call
        else:
            value < self.value
            if self.left is None:  # go left
                self.left = BSTNode(value)
                return
            else:
                return self.left.insert(value)

        # ITERATIVE
        # while not at bottom level of tree
        # if value < root, go left
            # if left child is None
                # add here 
                # exit loop

        # if value >= root, go right (dupes go to the right)
            # if right child is None
                # add here

    def contains(self, target):
        '''Return True if the tree contains the value, return False if it does not'''
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    def get_max(self):
        '''Return the maximum value found in the tree'''
        if self.right is None:
            return self.value
        # go right until you cannot go anymore
        else:
            return self.right.get_max()
        # return value at far right

    def for_each(self, fn):
        '''Call the function `fn` on the value of each node'''
        fn(self.value)
        # if self is not None:
            # return

        # base case - no children
        if self.left is None and self.right is None:
            return

        # recursive case - 1 or more children
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Recursive - place your print statement in between recursive calls
        # then explore left & right subtree
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):  # using Queue
        q = Queue()
        current = self
        q.enqueue(self)
        while current:
            current = q.dequeue()
            if current:
                if current.left:
                    q.enqueue(current.left)
                if current.right:
                    q.enqueue(current.right)

                print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):  # using stack
        # create a stack to keep track of nodes we are processing
        # push self in to the stack
        print(self.value)
        if self.left is not None:
            self.left.dft_print()
        if self.right is not None:
            self.right.dft_print()

        # while something still in the stack (not done processing all nodes)
            # use existing 'for_each()' as a reference for traversal logic
            # push when we START, pop when a node is DONE
            # and don't forget to call 'print()'

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft()
        if self.right is not None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left is not None:
            self.left.post_order_dft()
        if self.right is not None:
            self.right.post_order_dft()
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print(f'bft_print')
bst.bft_print()
print(f'dft_print')
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  

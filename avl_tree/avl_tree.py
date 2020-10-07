import random, math

outputdebug = False 

def debug(msg):
    if outputdebug:
        print(msg)


class Node:
    """
    Node class to keep track of
    the data internal to individual nodes
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree:
    """
    A tree class to keep track of things like the
    balance factor and the rebalancing logic
    """
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    def display(self, level=0, pref=''):
        """
        Display the whole tree. Uses recursive def.
        """
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    def update_height(self, data=True):
        """
        Computes the maximum number of levels there are
        in the tree
        """
        if not self.node == None:
            if data:
                if self.node.left != None:
                    self.node.left.update_height()
                if self.node.right != None:
                    self.node.right.update_height()
                    
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balance(self, data=True):
        """
        Updates the balance factor on the AVLTree class
        """
        if not self.node == None:
            if data:
                if self.node.left != None:
                    self.node.left.update_balance()
                if self.node.right != None:
                    self.node.right.update_balance()
                    
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def left_rotate(self):
        """
        Perform a left rotation, making the right child of this
        node the parent and making the old parent the left child
        of the new parent. 
        """
        S = self.node 
        R = self.node.right.node 
        L = R.left.node 
        
        self.node = R 
        R.left.node = S 
        S.right.node = L 

    def right_rotate(self):
        """
        Perform a right rotation, making the left child of this
        node the parent and making the old parent the right child
        of the new parent. 
        """
        S = self.node 
        L = self.node.left.node 
        R = L.right.node 
        
        self.node = L 
        L.right.node = S 
        S.left.node = R 

    def rebalance(self):
        """
        Sets in motion the rebalancing logic to ensure the
        tree is balanced such that the balance factor is
        1 or -1
        """
        self.update_height(False)
        self.update_balance(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                self.right_rotate()
                self.update_height()
                self.update_balance()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()
                self.left_rotate()
                self.update_height()
                self.update_balance()

    def insert(self, key):
        """
        Uses the same insertion logic as a binary search tree
        after the value is inserted, we need to check to see
        if we need to rebalance
        """
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance()
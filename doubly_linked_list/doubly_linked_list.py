"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        '''Updating our previous and next pointers'''
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            

class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to 
    the list's head and tail nodes.
    """
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly.
        """
        # create a new node
        new_node = ListNode(value)
        # 1. add to empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 2. add to nonempty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # update  yhe lenght
        self.length +=1

    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """
        
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.lenght = 0
            return
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        """
        new_node = ListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        if self.tail is None:
            return
        if self.tail is self.head:
            self.head = None
            self.tail = None
            self.lenght = 0
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.lenght = -1

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """
        self.delete(node)
        self.add_to_head(node)
        

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """
        # if self.head is node:
        #     self.head = self.head.next
        #     self.head.prev = None
        self.delete(node)
        self.add_to_tail(node)

    def delete(self, node):
        """
        Deletes the input node from the List, preserving the 
        order of the other elements of the List. Handles cases where
        the node was the head or the tail as well
        """
        if self.head and self.head.value == node:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        if self.tail and self.tail.value == node:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
                node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # check if dll empty
        if self.head is None:
            return None
        # keep track of current node, max
        # keep track of max
        cur_node = self.head
        max_value = self.head.value
        # loop through dll
        while cur_node:  # while cur_node is not None:
            # comparing with cur_max
            if cur_node.value > max_value:
                max_value = cur_node.value
            cur_node = cur_node.next
        return max_value


    def traverse_list(self):
        '''Print out values stored at the list'''
        if self.head is None:
            print("List has no element")
            return
        else:
            h = self.head
            while h is not None:
                print(h.value , " ")
                h = h.next


l = DoublyLinkedList()
l.traverse_list()
l.add_to_head(1)
l.add_to_head(2)
l.add_to_tail(3)
print('Values:')
l.traverse_list()
l.remove_from_head()
print('Remove head')
l.traverse_list()
l.remove_from_tail()
print('remove tail')
l.traverse_list()
l.add_to_head(2)
l.add_to_head(1)
l.add_to_tail(3)
print('actual values')
l.traverse_list()
l.move_to_front(3)
print('move to front')
l.traverse_list()
l.move_to_end(3)
print('back to tail')
l.traverse_list()
print('max_number')
l.get_max()
l.traverse_list()

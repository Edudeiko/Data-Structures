'''Single Linked List Items'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


'''Creating single linked List Items'''


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse_list(self):
        # if list is empty it returns 'print'
        if self.head is None:
            print("List has no element")
            return
        else:
            # otherwise it will print the value
            n = self.head
            while n is not None:
                print(n.value, " ")
                n = n.next_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
#             return
#         n = self.head
#         while n.next_node is not None:
#             n = n.next_node
#         n.next_node = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def add_after_item(self, x, value):

        n = self.head
        print(n.next_node)
        while n is not None:
            if n.value == x:
                break
            n = n.next_node
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(value)
            new_node.next_node = n.next_node
            n.next_node = new_node

    def add_before_item(self, x, value):
        # check if the list is empty
        if self.head is None:
            print("List has no element")
            return
        # check if the element is located at the first index
        if x == self.head.value:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
            return

        n = self.head
        print(n.next_node)
        while n.next_node is not None:
            if n.next_node.value == x:
                break
            n = n.next_node
        if n.next_node is None:
            print("item not in the list")
        else:
            new_node = Node(value)
            new_node.next_node = n.next_node
            n.next_node = new_node

    def add_at_index(self, index, value):
        if index == 1:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            n = n.next_node
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(value)
            new_node.next_node = n.next_node
            n.next_node = new_node

    def get_count(self):
        if self.head is None:
            return 0
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next_node
        return count

    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.value == x:
                print("Item found")
                return True
            n = n.next_node
        print("item not found")
        return False

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for _ in range(nums):
            value = int(input("Enter the value for the node: "))
            self.add_to_tail(value)

#     def remove_head(self):
#         if self.head is None:
#             print("The list has no element to delete")
#             return
#         self.head = self.head.next_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            if self.head.get_next_node() is None:
                h = self.head
                self.head = None
                self.tail = None
                return h.get_value()
            value = self.head.get_value()
            self.head = self.head.get_next_node()
            return value

    def remove_tail(self):
        # if self.head is None:
        #     print("The list has no element to delete")
        #     return

        # n = self.head
        # while n.next_node.next_node is not None:
        #     n = n.next_node
        # n.next_node = None
        if self.head is None:
            return None
        value = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.next_node.get_next_node() is not None:
            current = current.next_node
        self.tail = current
        return value

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.head.value == x:
            self.head = self.head.next_node
            return

        n = self.head
        while n.next_node is not None:
            if n.next_node.value == x:
                break
            n = n.next_node

        if n.next_node is None:
            print("item not found in the list")
        else:
            n.rnext_nodeef = n.next_node.next_node

    def reverse_linkedlist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next_node
            n.next_node = prev
            prev = n
            n = next
        self.head = prev

    # def get_max(self):
    #     if self.head is None:
    #         return None
    #     cur_node = self.head
    #     max_value = 0
    #     while cur_node is not None:
    #         if cur_node.get_value() > max_value:
    #             max_value = cur_node.get_value()
    #     return max_value


# my_list = LinkedList()
# my_list.make_new_list()
# my_list.add_to_head(2)
# my_list.add_to_tail(7)
# my_list.add_before_item(2, 3)
# my_list.add_after_item(7, 8)
# my_list.add_at_index(1, 1)
# my_list.traverse_list()
# my_list.get_count()
# my_list.search_item(11)
# my_list.remove_head()
# my_list.remove_tail()
# my_list.delete_element_by_value(11)
# my_list.reverse_linkedlist()

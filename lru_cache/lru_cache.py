# from doubly_linked_list import ListNode, DoublyLinkedList

# class LRUCache:
#     """
#     Our LRUCache class keeps track of the max number of nodes it
#     can hold, the current number of nodes it is holding, a doubly-
#     linked list that holds the key-value entries in the correct
#     order, as well as a storage dict that provides fast access
#     to every node stored in the cache.
#     """
#     def __init__(self, limit=10):
#         self.order = DoublyLinkedList()
#         self.cache = dict()
#         self.limit = limit

#     def get(self, key):
#         """
#         Retrieves the value associated with the given key. Also
#         needs to move the key-value pair to the end of the order
#         such that the pair is considered most-recently used.
#         Returns the value associated with the key or None if the
#         key-value pair doesn't exist in the cache.
#         """
#         if key not in self.cache:
#             return None
#         if key in self.cache:
#             node = self.cache[key]
#             self.order.move_to_end(node)
#             return node.value[1]

#     def set(self, key, value):
#         """
#         Adds the given key-value pair to the cache. The newly-
#         added pair should be considered the most-recently used
#         entry in the cache. If the cache is already at max capacity
#         before this entry is added, then the oldest entry in the
#         cache needs to be removed to make room. Additionally, in the
#         case that the key already exists in the cache, we simply
#         want to overwrite the old value associated with the key with
#         the newl
#         """
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = (key, value)
#             self.order.move_to_end(node)
#             return
        
#         node = ListNode((key, value))
        
#         self.cache[key] = node
#         self.order.move_to_end(node)
#         self.order.length += 1
        
#         if self.order.length > self.limit:
#             # new_value = self.order.remove_from_head()
#             self.cache.pop(self.order.remove_from_head(), value)
#             self.order.length -= 1



import collections

class LRUCache:

    def __init__(self, limit):
        self.limit = limit
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) >= self.limit:
                self.cache.popitem(last=False)
        self.cache[key] = value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def move_to_tail(self, node):
        if node is None:
            return

        if node == self.tail:
            return

        if self.head == node:
            node.next.prev = None
            self.head = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.tail.next = node
        node.next = None
        node.prev =self.tail
        self.tail = node

    def add_to_tail(self, node):
        node.next = None
        node.prev = None
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def get_from_head(self):
        node = self.head
        if node is None:
            return None
        if node.next:
            node.next.prev = None
        else:
            tail = None
        self.head = node.next
        node.next = None
        return node

    def __repr__(self):
        str = ""
        node = self.head
        while node:
            if node == self.tail:
                str = str + "[{},{}]".format(node.value[0], node.value[1])
            else:
                str = str + "[{},{}]".format(node.value[0], node.value[1]) + ","
            node = node.next

        return str

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables

        # cache where values are stored
        self.cache = [None for i in range(capacity)]
        # number of elements in cache
        self.num = 0
        # node dictionary, key: node, node is a reference to the node in occupied_list
        self.node_dict = {}
        # a doubly linked list of nodes whose value is [key, index], which is sorted by access order
        # index is fixed in every node
        self.occupied_list = DoublyLinkedList()
        # a free node list
        self.free_list = DoublyLinkedList()

        #create node for every index and put them in free list
        for i in range(capacity):
            self.free_list.append([None, i])

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        # get a node from node_dict by the key
        node = self.node_dict.get(key)
        # if key is in node_dict
        if node:
            # move the node to the tail of the occupied_list
            self.occupied_list.move_to_tail(node)
            return self.cache[node.value[1]]
        # if key is not in node_dict
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # get a node from node_dict by the key
        node = self.node_dict.get(key)
        # if key is in node_dict
        if node:
            # set node value [key, index], index is fixed
            node.value[0] = key
            # set value in cache
            self.cache[node.value[1]] = value
            # move the node to the end of the occupied_list
            self.occupied_list.move_to_tail(node)
        else:
            node = None
            # if cache is not full
            if self.num < len(self.cache):
                # get a node from free_list
                node = self.free_list.get_from_head()
                self.num += 1
            # if cache is full
            else:
                # get a node from head of the occupied_list (the least used item)
                node = self.occupied_list.get_from_head()
                # delete the old key from node_dict
                del self.node_dict[node.value[0]]

            # set node key to new key
            node.value[0] = key
            # add the node to the tail of the occupied_list
            self.occupied_list.add_to_tail(node)
            # add the value to the cache
            self.cache[node.value[1]] = value
            # add new key to the node_dict
            self.node_dict[key] = node

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

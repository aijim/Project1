class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        # append data in increasing order
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node1 = self.head
            previous = None
            while node1 and node.value >= node1.value:
                previous = node1
                node1 = node1.next

            node.next = node1
            if previous is None:
                self.head = node
            else:
                previous.next = node

            if node.next is None:
                self.tail = node

        self.num += 1

    def insert_to_tail(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.num += 1

    def size(self):
        return self.num

def union(llist_1, llist_2):
    llist = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    while node1 and node2:
        value = min(node1.value, node2.value)
        llist.insert_to_tail(value)
        while node1 and node1.value == value:
            node1 = node1.next
        while node2 and node2.value == value:
            node2 = node2.next

    while node1:
        value = node1.value
        llist.insert_to_tail(value)
        while node1 and node1.value == value:
            node1 = node1.next

    while node2:
        value = node2.value
        llist.insert_to_tail(value)
        while node2 and node2.value == value:
            node2 = node2.next

    return llist


def intersection(llist_1, llist_2):
    llist = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    while node1 and node2:
        if node1.value < node2.value:
            node1 = node1.next
        elif node1.value == node2.value:
            value = node1.value
            llist.insert_to_tail(value)
            while node1 and node1.value == value:
                node1 = node1.next
            while node2 and node2.value == value:
                node2 = node2.next
        else:
            node2 = node2.next

    return llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]

for i in element_1:
    linked_list_5.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
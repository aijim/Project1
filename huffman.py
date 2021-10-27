import sys
import collections


class LNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __gt__(self, other):
        return self.value > other.value

class MinHeap:
    def __init__(self):
        self.head = None
        self.num = 0

    def add(self, data):
        new_node = LNode(data)
        node = self.head
        previous = None
        while node is not None and new_node.value > node.value:
            previous = node
            node = node.next

        if node == self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = node
            previous.next = new_node

        self.num += 1

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = node.next
        node.next = None
        self.num -= 1
        return node.value

    def __len__(self):
        return self.num


class TreeNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ""

    def is_leaf(self):
        return self.left is None and self.right is None

    def __gt__(self, other):
        return self.freq > other.freq


class Tree:
    def __init__(self):
        self.root = None


codes = {}


def calculate_codes(node, val=''):
    # huffman code for current node
    if node is None:
        return

    new_val = val + node.code

    if node.is_leaf():
        codes[node.symbol] = new_val
        return

    if node.left:
        calculate_codes(node.left, new_val)
    if node.right:
        calculate_codes(node.right, new_val)


def huffman_encoding(data):
    # for empty input, return ["", None]
    if data == "":
        return "", None

    # get the occurrence of each character in the data set
    freq_map = collections.Counter(data)

    # create priority_queue
    priority_queue = MinHeap()
    for char, freq in freq_map.items():
        priority_queue.add(TreeNode(char, freq))

    # create Huffman tree
    if len(priority_queue) == 1:
        node1 = priority_queue.pop()
        node = TreeNode(None, node1.freq)
        node.left = node1
        node1.code = '0'
        priority_queue.add(node)
    else:
        while len(priority_queue) > 1:
            node1 = priority_queue.pop()
            node2 = priority_queue.pop()
            sum = node1.freq + node2.freq
            node = TreeNode(None, sum)
            node.left = node1
            node1.code = '0'
            node.right = node2
            node2.code = '1'
            priority_queue.add(node)

    huffman_tree = Tree()
    huffman_tree.root = priority_queue.pop()

    # create huffman code dictionary
    calculate_codes(huffman_tree.root)

    # encode data
    encoded_data = ""
    for c in data:
        encoded_data += codes[c]

    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    if tree is None:
        return ""

    # decode data
    node = tree.root

    i = 0
    decoded_data = ""
    while i < len(data):
        node = tree.root
        while not node.is_leaf():
            if data[i] == "0":
                node = node.left
            else:
                node = node.right
            i += 1

        decoded_data += node.symbol

    return decoded_data

def testcase(sentence):
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the data is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)

    if encoded_data != "":
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data != "":
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    print("")

if __name__ == "__main__":
    # codes = {}

    # test case 1 - a sentence
    testcase("Tomorrow is another day.")

    # test case 2 - empty string
    testcase("aaaaaaaaaa")

    # test case 3 - a string with only one character
    testcase("")
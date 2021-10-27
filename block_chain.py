import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.timestamp + self.data
        if self.previous_hash is None:
            hash_str = hash_str.encode('utf-8')
        else:
            hash_str = (hash_str + self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.last = None

        # A block in memory will be destroyed by garbage collector if it does not have a reference to it
        # store references to the blocks in a dictionary
        self.block_dict = {}

    def add(self, data):
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        block = Block(timestamp, data, self.last)
        self.last = block.hash

        self.block_dict[block.hash] = block

    def __str__(self):
        block_hash = self.last
        str = ""
        while block_hash:
            block = self.block_dict[block_hash]
            str += "{} {}\n".format(block.timestamp, block.data)
            block_hash = block.previous_hash

        return str

block_chain = BlockChain()
block_chain.add("First record")
block_chain.add("Second record")
block_chain.add("Third record")

print(block_chain)


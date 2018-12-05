# A really simple blockchain
# Based on https://www.youtube.com/watch?v=b81Ib_oYbFk
# Coded by Bram Bakx
# Made on MacOs and Python 3.7

import datetime
import hashlib


# Every block in the blockchain is an instance of Block.
class Block:

    blockNumber = 0  # The number of the block
    data = None  # The data you want to store in the block
    next = None  # The pointer to te next block in the blockchain
    hash = None
    nonce = 0  # The number of hashes needed to mine the block
    previousHash = 0x0  # The hash of the previous block in the blockchain
    timestamp = datetime.datetime.now()

    # Store the blocks data
    def __init__(self, data):
        self.data = data

    # Create the block's hash. Merge all the data together in one big string and run that through sha256
    # It is very import to add previousHash to the new hash, because if previousHash changes all the hashes change
    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previousHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNumber).encode('utf-8')
        )
        return h.hexdigest()

    # The block as printed to the console
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNumber) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


class Blockchain:

    # determine the mining difficulty
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):
        block.previousHash = self.block.hash()
        block.blockNumber = self.block.blockNumber + 1

        self.block.next = block
        self.block = self.block.next

    # The hash has to be lower than the target to be accepted in the blockchain
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


blockchain = Blockchain()

# Generate 10 random blocks
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

# Print each block to the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next

import sys
import time
import json

sys.path.append('D:/xampp/htdocs/sand_box/get_job/custom-python-blockchain')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256

ZERO_HASH = '0' * 64
VERSION = 1


class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Code Architect sent {BlockHeight} Bitcoins to Indranil"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(version=VERSION, prevBlockHash=prevBlockHash, merkleRoot=merkleRoot,
                                  timestamp=timestamp, bits=bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__)
        print(json.dumps(self.chain, indent=4))

    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]["Height"] + 1
            prevBlockHash = lastBlock[0]["BlockHeader"]["blockHash"]
            self.addBlock(BlockHeight, prevBlockHash)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()

# Custom Python Blockchain


1. Let's create the directory structure first Root folder `Blockchain`, under that `Backend`, `Frontend` and `client`. 
Under Backend, `core` and `util`. 
2. Inside cre create a file name `block.py` and create a class name `Block`. Inside `__init__` method talke ` 
Height, Blocksize, BlockHeader, TxCount, Txs` variables
3. Create a new module `blockheader.py`, create a class call `BlockHeader`. Inside the `__init__` method will take 
`version, prevBlockHash, merkleRoot, timestamp, bits` and declare `self.nonce = 0 , self.blockHash = ''`
4. 

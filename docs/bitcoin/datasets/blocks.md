## BLOCKS

Stores essential information about the blocks in a blockchain.

| Column | Description |
| ----------- | ----------- |
| TIMESTAMP | Raw value of the time in Unix Epoch time (in UTC time zone), which is then converted to DATETIME column. |
| DATETIME | Timestamp of the transaction in UTC. |
| BLOCK_HEIGHT | Indicates the numerical position of a block within the blockchain. |
| BLOCK_HASH | The hash of a specific block in the blockchain. |
| BITS | Encoded difficulty target for a particular block; represents the target value that the block hash must meet or exceed for the block to be considered valid. |
| CHAIN_WORK | Cumulative work done on the Bitcoin blockchain. |
| DIFFICULTY | Numerical value that represents the level of difficulty for mining a new block in the Bitcoin network. |
| TOTAL_FEE | Total amount of transaction fees collected by miners in a specific block. |
| TOTAL_REWARD | Total reward given to miners for successfully mining a specific block. It is a sum of the total fee and mint reward per block. |
| MINT_REWARD | Newly created Bitcoin awarded to miners for successfully mining a block. |
| MERKLE_ROOT | Hash value that represents the root of the Merkle tree. |
| TRANSACTION_COUNT | Total number of transactions included in a block on the blockchain. |
| NONCE | Confirms the legitimacy of a block; proof of work mechanism. |
| COINBASE | Special transaction included in a block that provides the block reward to the miner. |
| PREVIOUS_BLOCK_HASH | Block hash of the previous block in the blockchain. |
| SIZE | The amount of data stored in a block, measured in bytes. |
| STRIPPED_SIZE | Represents the size of the block after removing the witness data. |
| VERSION | Version number associated with a block or transaction. |
| WEIGHT | Measurement of the computational effort required to validate a block. |
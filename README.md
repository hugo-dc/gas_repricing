# Gas Repricing

This repository contains the result of calculating gas repricing in different
opcodes.

The gas cost changes are configured in a [gas_table](./data/gas_table.csv)
which contains: Opcode Number, Current Gas Cost, Proposed Gas Cost, and the
Opcode Name.

## Results

The following information is extracted from the calculation in [this Python
Notebook](notebooks/tx_gas_repricing.ipynb#ALL-Traced-Contracts)

### General

Results for a sample of 431,515:

|                                |      |
|--------------------------------|------|
|Average gas used                |78,500|
|Average gas used after repricing|74,686|
|Average gas usage reduction     |  4.7%|

### Uniswap

Uniswap is currently the top contract by gas usage, almos 20% of total block
gas.

Results for a sample of 77,600 transactions:

|                                |      |
|--------------------------------|------|
|Average gas used                |122717|
|Average gas used after repricing|114881|
|Average gas usage reduction     | 9.39%|

### AAVE

Results for a sample of 2,004 transactions:
|                                |      |
|--------------------------------|------|
|Average gas used                |294614|
|Average gas used after repricing|272707|
|Average gas usage reduction     | 7.34%|

### 1inch

Results for a sample of 7,253 transactions:

|                                |      |
|--------------------------------|------|
|Average gas used                |178,508|
|Average gas used after repricing|166,468|
|Average gas usage reduction     |  5.70%|


### Metamask Swap

Results for a sample of 13,652 transactions:

|                                |      |
|--------------------------------|------|
|Average gas used                |210,745|
|Average gas used after repricing|198,401|
|Average gas usage reduction     |  5.69%|

### USDC

Results for a sample of 183,925 transactions:

|                                |      |
|--------------------------------|------|
|Average gas used                |33,170|
|Average gas used after repricing|32,213|
|Average gas usage reduction     | 2.87%|

### USDT

Results for a sample of 67,406 transactions:

|                                |      |
|--------------------------------|------|
|Average gas used                |39,438|
|Average gas used after repricing|38,634|
|Average gas usage reduction     | 1.91%|



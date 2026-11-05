@	
s	forkCacheSize	The maximum size, in bytes, of the in-memory cache for queries on a chain fork. Defaults to…
o	-a|--accounts	Specify the number of accounts to generate at startup	v
o	-e|--defaultBalanceEther	Amount of ether to assign each test account. Default is 100	v
o	-b|--blockTime	Specify blockTime in seconds for automatic mining. If you don't specify this flag, ganache will…	v
o	-d|--deterministic	Generate deterministic addresses based on a pre-defined mnemonic	
o	-n|--secure	Lock available accounts by default (good for third party transaction signing)	
o	-m|--mnemonic	Use a bip39 mnemonic phrase for generating a PRNG seed, which is in turn used for hierarchical…	
o	-p|--port	Port number to listen on. Defaults to 8545	v
o	-h|--host	Hostname to listen on. Defaults to 127.0.0.1 (defaults to 0.0.0.0 for Docker instances of…	v
o	-s|--seed	Use arbitrary data to generate the HD wallet mnemonic to be used	
o	-g|--gasPrice	The price of gas in wei (defaults to 20000000000)	v
o	-l|--gasLimit	The block gas limit (defaults to 0x6691b7)	v
o	--callGasLimit	Sets the transaction gas limit for eth_call and eth_estimateGas calls	v
o	-k|--hardfork	Allows users to specify which hardfork should be used	v
o	-f|--fork	Fork from another currently running Ethereum client at a given block. Input should be the HTTP…	v
o	-i|--networkId	Specify the network id ganache-cli will use to identify itself (defaults to the current time or…	v
o	--chainId	Specify the Chain ID ganache-cli will use for eth_chainId RPC and the CHAINID opcode	v
o	--db	Specify a path to a directory to save the chain database. If a database already exists…	v
o	--debug	Output VM opcodes for debugging	
o	--mem	Output ganache-cli memory usage statistics. This replaces normal output	
o	-q|--quiet	Run ganache-cli without any logs	
o	-?|--help	Display help information	
o	--version	Display the version of ganache-cli	
o	--account_keys_path|--acctKeys	Specifies a file to save accounts and private keys to, for testing	v
o	--noVMErrorsOnRPCResponse	Do not transmit transaction failures as RPC errors	
o	--allowUnlimitedContractSize	Allows unlimited contract sizes while debugging	
o	--keepAliveTimeout	Sets the HTTP server's keepAliveTimeout in milliseconds	v
o	-t|--time	Date (ISO 8601) that the first block should start	v
o	--account	Specify any number of times passing arbitrary private keys and their associated balances to…	v
o	-u|--unlock	Specify any number of times passing either an address or an account index to unlock specific…	v
=		-k
v	byzantium	
v	constantinople	
v	petersburg	
v	istanbul	
v	muirGlacier	
=		--db
t	folders
=		--account_keys_path
t	filepaths
@	forkCacheSize
a	1	0

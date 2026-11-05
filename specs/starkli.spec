@	
s	account	Account management commands
s	block	Get Starknet block
s	block-hash	Get latest block hash
s	block-number	Get latest block number
s	block-time	Get Starknet block timestamp only
s	call	Call contract functions without sending transactions
s	chain-id	Get Starknet network ID
s	class-at	Get contract class deployed at a certain address
s	class-by-hash	Get contract class by hash
s	class-hash	Calculate class hash from any contract artifacts (Sierra, casm, legacy)
s	class-hash-at	Get contract class hash deployed at a certain address
s	completions	Generate shell completions script
s	declare	Declare a contract class
s	deploy	Deploy contract via the Universal Deployer Contract
s	invoke	Send an invoke transaction from an account contract
s	mont	Print the montgomery representation of a field element
s	nonce	Get nonce for a certain contract
s	parse-cairo-string	Decode string from felt with the Cairo short string representation
s	selector	Calculate selector from name
s	signer	Signer management commands
s	state-update	Get state update from a certain block
s	storage	Get storage value for a slot at a contract
s	syncing	Get node syncing status
s	to-cairo-string	Encode string into felt with the Cairo short string representation
s	transaction	Get Starknet transaction by hash
s	transaction-receipt	Get transaction receipt by hash
@	account
s	fetch	Fetch account config from an already deployed account contract
s	deploy	Deploy account contract with a DeployAccount transaction
s	oz	Create and manage OpenZeppelin account contracts
o	-h|--help	Print help	
@	account fetch
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--force	Overwrite the file if it already exists	
o	--output	Path to save the account config file	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	account fetch	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
=	account fetch	--output
t	filepaths
@	account deploy
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--keystore	Path to keystore JSON file	v
o	--keystore-password	Supply keystore password from command line option instead of prompt	v
o	--private-key	Private key in hex in plain text	v
o	--max-fee	Maximum transaction fee in Ether (18 decimals)	v
o	--max-fee-raw	Maximum transaction fee in Wei	v
o	--estimate-only	Only estimate transaction fee without sending transaction	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	account deploy	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
=	account deploy	--keystore
t	filepaths
#	account deploy	1
t	filepaths
@	account oz
s	init	Create a new account configuration without actually deploying
o	-h|--help	Print help	
@	account oz init
@	block
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--full	Fetch full transactions instead of hashes only	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	block	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	block-hash
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
=	block-hash	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	block-number
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
=	block-number	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	block-time
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--unix	Show block time in Unix timestamp format	
o	--rfc2822	Show block time in RFC 2822 format	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	block-time	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	call
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	3	0
=	call	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	chain-id
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--no-decode	Do not show the decoded text	
o	--dec	Display the decimal instead of hexadecimal representation	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	chain-id	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	class-at
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	class-at	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	class-by-hash
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	class-by-hash	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	class-hash
o	-h|--help	Print help	
a	1	0
#	class-hash	1
t	filepaths
@	class-hash-at
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	class-hash-at	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	completions
@	declare
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--keystore	Path to keystore JSON file	v
o	--keystore-password	Supply keystore password from command line option instead of prompt	v
o	--private-key	Private key in hex in plain text	v
o	--compiler-version	Statically-linked Sierra compiler version	v
o	--casm-hash	Override Sierra compilation and use CASM hash directly	v
o	--account	Path to account config JSON file	v
o	--max-fee	Maximum transaction fee in Ether (18 decimals)	v
o	--max-fee-raw	Maximum transaction fee in Wei	v
o	--estimate-only	Only estimate transaction fee without sending transaction	
o	--watch	Wait for the transaction to confirm	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	declare	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
=	declare	--keystore
t	filepaths
=	declare	--compiler-version
v	2.0.1	
=	declare	--account
t	filepaths
#	declare	1
t	filepaths
@	deploy
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--keystore	Path to keystore JSON file	v
o	--keystore-password	Supply keystore password from command line option instead of prompt	v
o	--private-key	Private key in hex in plain text	v
o	--not-unique	Do not derive contract address from deployer address	
o	--account	Path to account config JSON file	v
o	--max-fee	Maximum transaction fee in Ether (18 decimals)	v
o	--max-fee-raw	Maximum transaction fee in Wei	v
o	--estimate-only	Only estimate transaction fee without sending transaction	
o	--salt	Use the given salt to compute contract deploy address	v
o	--watch	Wait for the transaction to confirm	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	2	0
=	deploy	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
=	deploy	--keystore
t	filepaths
=	deploy	--account
t	filepaths
@	invoke
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--keystore	Path to keystore JSON file	v
o	--keystore-password	Supply keystore password from command line option instead of prompt	v
o	--private-key	Private key in hex in plain text	v
o	--account	Path to account config JSON file	v
o	--max-fee	Maximum transaction fee in Ether (18 decimals)	v
o	--max-fee-raw	Maximum transaction fee in Wei	v
o	--estimate-only	Only estimate transaction fee without sending transaction	
o	--watch	Wait for the transaction to confirm	
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	invoke	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
=	invoke	--keystore
t	filepaths
=	invoke	--account
t	filepaths
@	mont
o	--hex	Emit array elements in hexadecimal format	
o	-h|--help	Print help	
a	1	0
@	nonce
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	nonce	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	parse-cairo-string
o	-h|--help	Print help	
a	1	0
@	selector
o	-h|--help	Print help	
a	1	0
@	signer
s	keystore	Keystore management commands
s	gen-keypair	Randomly generate a new key pair
o	-h|--help	Print help	
@	signer keystore
s	new	Randomly generate a new keystore
s	from-key	Create a keystore file from an existing private key
s	inspect	Check the public key of an existing keystore file
s	inspect-private	Check the private key of an existing keystore file
o	-h|--help	Print help	
@	signer keystore new
o	--password	Supply password from command line option instead of prompt	v
o	--force	Overwrite the file if it already exists	
o	-h|--help	Print help	
a	1	0
#	signer keystore new	1
t	filepaths
@	signer keystore from-key
o	--force	Overwrite the file if it already exists	
o	--private-key-stdin	Take the private key from stdin instead of prompt	
o	--password	Supply password from command line option instead of prompt	v
o	-h|--help	Print help	
a	1	0
#	signer keystore from-key	1
t	filepaths
@	signer keystore inspect
o	--password	Supply password from command line option instead of prompt	v
o	--raw	Print the public key only	
o	-h|--help	Print help	
a	1	0
#	signer keystore inspect	1
t	filepaths
@	signer keystore inspect-private
o	--password	Supply password from command line option instead of prompt	v
o	--raw	Print the private key only	
o	-h|--help	Print help	
a	1	0
#	signer keystore inspect-private	1
t	filepaths
@	signer gen-keypair
@	state-update
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	state-update	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	storage
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	2	0
=	storage	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	syncing
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
=	syncing	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	to-cairo-string
o	--dec	Display the encoded value in decimal representation	
o	-h|--help	Print help	
a	1	0
@	transaction
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	transaction	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	
@	transaction-receipt
o	--rpc	Starknet JSON-RPC endpoint	v
o	--network	Starknet network	v
o	--log-traffic	Log raw request/response traffic of providers	
o	-h|--help	Print help	
a	1	0
=	transaction-receipt	--network
v	mainnet	
v	goerli-1	
v	goerli-2	
v	integration	

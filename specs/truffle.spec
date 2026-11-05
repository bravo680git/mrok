@	
s	build	Execute build pipeline (if configuration present)
s	compile	Compile contract source files
s	config	Set user-level configuration options
s	console	Run a console with contract abstractions and commands available
s	create	Helper to create new contracts, migrations and tests
s	debug	Interactively debug any transaction on the blockchain
s	deploy	Alias for migrate. See migrate for details
s	develop	Open a console with a development blockchaine
s	exec	Execute a JS module within the Truffle environment
s	help	Display a list of all commands or information about a specific command
s	init	Initialize new and empty Ethereum project
s	install	Install a package from the Ethereum Package Registry
s	networks	Show addresses for deployed contracts on each network
s	obtain	Fetch and cache a specified compiler
s	opcode	Print the compiled opcodes for a given contract
s	publish	Publish a package to the Ethereum Package Registry
s	run	Run a third-party plugin command
s	version	Show version number and exit
s	watch	Watch filesystem for changes and rebuild the project automatically
s	preserve	Save data to decentralized storage platforms like IPFS and Filecoin
s	migrate	Run migrations to deploy contracts
s	unbox	Download a Truffle Box, a pre-built Truffle project
s	test	Run JavaScript and Solidity tests
@	build
@	compile
o	--list	List all recent stable releases from solc-bin. If filter is specified then it will display only…	v
o	--all	Compile all contracts instead of only the contracts changed since last compile	
o	--quiet	Suppress all compilation output	
=	compile	--list
v	prereleases	
v	releases	
v	latestRelease	
v	docker	
@	config
s	get	Get a Truffle configuration option value
s	set	Set a Truffle configuration option value
o	--enable-analytics	Enable Truffle to send usage data to Google Analytics	
o	--disable-analytics	Disable Truffle's ability to send usage data to Google Analytics	
@	config get
a	1	0
@	config set
a	2	0
@	console
o	--network	Specify the network to use	v
o	--verbose-rpc	Log communication between Truffle and the Ethereum client	
o	--require|-r	Preload console environment from required JavaScript file	v
o	--require-none	Do not load any user-defined JavaScript into the console environment. This option takes precedence…	
=	console	--require
t	filepaths
@	create
a	2	0
#	create	1
v	contract	
v	migration	
v	test	
v	all	
@	debug
o	--network	The network to connect to	v
o	--fetch-external|-x	Allows the debugger to download source from source verification services to debug transactions…	
o	--compile-tests	Allows the debugger to compile Solidity test contracts. Implies --compile-all	
o	--compile-all	Forces the debugger to recompile all contracts, even when it would otherwise judge doing so…	
o	--compile-none	Forces the debugger not to recompile contracts, even when it would otherwise judge it necessary…	
a	1	0
@	deploy
@	develop
o	--log	Start/Connect to a Truffle develop session and log all RPC activity. See the Log RPC Activity docs…	v
o	--require|-r	Preload console environment from required JavaScript file	v
o	--require-none	Do not load any user-defined JavaScript into the console environment. This option takes precedence…	
=	develop	--require
t	filepaths
@	exec
o	--network	Specify the network to use, using artifacts specific to that network	v
o	--compile	Compile contracts before executing the script	
a	1	0
#	exec	1
t	filepaths
@	help
a	1	0
#	help	1
v	build	
v	compile	
v	config	
v	console	
v	create	
v	debug	
v	deploy	
v	develop	
v	exec	
v	help	
v	init	
v	install	
v	networks	
v	obtain	
v	opcode	
v	publish	
v	run	
v	version	
v	watch	
v	preserve	
v	migrate	
v	unbox	
v	test	
@	init
o	--force	Initialize project regardless of the current working directory's state. Be careful, this could…	
@	install
a	2	0
@	networks
o	--clean	Remove all network artifacts that aren't associated with a named network	
@	obtain
o	--solc	Download and cache a version of the solc compiler. (required)	v
@	opcode
a	1	0
@	publish
@	run
a	1	0
@	version
@	watch
@	preserve
o	--environment	Environment name, as defined in truffle-config `environments` object	v
o	--ipfs	Preserve to IPFS	
o	--filecoin	Preserve to Filecoin	
o	--buckets	Preserve to Textile Buckets	
a	1	0
#	preserve	1
t	filepaths
@	migrate
o	--reset	Run all migrations from the beginning, instead of running from the last completed migration	
o	--f	Run contracts from a specific migration	v
o	--to	Run contracts to a specific migration	v
o	--network	Specify the network to use, saving artifacts specific to that network	v
o	--compile-all	Compile all contracts instead of intelligently choosing which contracts need to be compiled	
o	--verbose-rpc	Log communication between Truffle and the Ethereum client	
o	--dry-run	Fork the network specified and only perform a test migration	
o	--skip-dry-run	Skip the test migration performed before the real migration	
o	--interactive	Prompt to confirm that the user wants to proceed after the dry run	
o	--describe-json	Prints additional status messages	
@	unbox
o	--force	Unbox project in the current directory regardless of its state. Be careful, this will potentially…	
a	2	0
#	unbox	2
t	filepaths
@	test
o	--compile-all	Compile all contracts instead of intelligently choosing which contracts need to be compiled	
o	--compile-all-debug	Like --compile-all, but compiles contracts in debug mode for extra information. Has no effect on…	
o	--network	Specify the network to use, using artifacts specific to that network	v
o	--verbose-rpc	Log communication between Truffle and the Ethereum client	
o	--show-events	Log all contract events	
o	--debug	Provides global debug() function for in-test debugging. Usable with Javascript tests only; implies…	
o	--debug-global	Allows one to rename the debug() function to something else	v
o	--bail|-b	Bail after the first test failure. May be abbreviated -b	
o	--stacktrace|-t	Allows for mixed Javascript-and-Solidity stacktraces when a Truffle Contract transaction or…	
o	--stacktrace-extra	Shortcut for --stacktrace --compile-all-debug	
a	1	0
#	test	1
t	filepaths

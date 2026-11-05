@	
s	addr2line	Show location and context of an opcode address in its source file
s	build	Compile the current or target project
s	check	Check the current or target project and all of its dependencies for errors
s	clean	Removes the default forc compiler output artifact directory, i.e. `<project-name>/out`
s	completions	Generate tab-completion scripts for your shell
s	new	Create a new Forc project at `<path>`
s	init	Create a new Forc project in an existing directory
s	parse-bytecode	Parse bytecode file into a debug format
s	test	Run the Sway unit tests for the current project
s	update	Update dependencies in the Forc dependencies directory
s	plugins	List all forc plugins
s	template	Create a new Forc project from a git template
s	contract-id	Determine contract-id for a contract. For workspaces outputs all contract ids in the workspace
s	predicate-root	Determine predicate-root for a predicate. For workspaces outputs all predicate roots in the…
s	debug	
s	run	Run script project. Crafts a script transaction then sends it to a running node
s	crypto	Forc plugin for hashing arbitrary data
s	doc	Forc plugin for building a Sway package's documentation
s	fmt	Forc plugin for running the Sway code formatter
s	submit	A `forc` plugin for interacting with a Fuel node
s	deploy	Build output file options
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help information	
o	-v	Use verbose output	
o	-s	Silence all output	
o	-L	Set the log level	
a	2	0
@	addr2line
o	-S	Where to search for the project root	
o	-g	Source file mapping in JSON format	
o	-c	How many lines of context to show	
o	-i	Opcode index	
o	-h|--help	Print help information	
a	2	0
@	build
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-o	If set, outputs a binary file representing the script bytes	
o	-g	If set, outputs source file mapping in JSON format	
o	-h|--help	Print help information	
a	24	0
#	build	22
v	fuel	
v	evm	
v	midenvm	
@	check
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-h|--help	Print help information	
a	7	0
#	check	3
v	fuel	
v	evm	
v	midenvm	
@	clean
o	-p	Path to the project, if not specified, current working directory will be used	
o	-h|--help	Print help information	
a	2	0
@	completions
o	-T	Specify shell to enable tab-completion for	V
o	-h|--help	Print help information	
a	2	0
=	completions	-T
v	bash	Bourne Again SHell (bash)
v	elvish	Elvish shell
v	fish	Friendly Interactive SHell (fish)
v	power-shell	PowerShell
v	zsh	Z SHell (zsh)
v	fig	Fig
@	new
o	-h|--help	Print help information	
a	9	0
@	init
o	-h|--help	Print help information	
a	9	0
@	parse-bytecode
o	-h|--help	Print help information	
a	3	0
@	test
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-o	If set, outputs a binary file representing the script bytes	
o	-g	If set, outputs source file mapping in JSON format	
o	-r	Pretty-print the logs emiited from tests	
o	-l	Print `Log` and `LogData` receipts for tests	
o	-h|--help	Print help information	
a	26	0
#	test	22
v	fuel	
v	evm	
v	midenvm	
@	update
o	-p	Path to the project, if not specified, current working directory will be used	
o	-d	Dependency to be updated. If not set, all dependencies will be updated	
o	-c	Checks if the dependencies have newer versions. Won't actually perform the update, will output…	
o	-h|--help	Print help information	
a	3	0
@	plugins
o	-p	Prints the absolute path to each discovered plugin	
o	-d	Prints the long description associated with each listed plugin	
o	-h|--help	Print help information	
a	2	0
@	template
o	-u	The template url, should be a git repo	
o	-t	The name of the template that needs to be fetched and used from git repo provided	
o	-h|--help	Print help information	
a	3	0
@	contract-id
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-o	If set, outputs a binary file representing the script bytes	
o	-g	If set, outputs source file mapping in JSON format	
o	-h|--help	Print help information	
a	23	0
@	predicate-root
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-o	If set, outputs a binary file representing the script bytes	
o	-g	If set, outputs source file mapping in JSON format	
o	-h|--help	Print help information	
a	22	0
@	debug
o	-s	Start the DAP server	
o	-h|--help	Print help information	
a	3	0
@	run
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-o	If set, outputs a binary file representing the script bytes	
o	-g	If set, outputs source file mapping in JSON format	
o	-d	Hex string of data to input to script	
o	-r	Pretty-print the outputs from the node	
o	-h|--help	Print help information	
a	36	0
@	crypto
s	keccak256	Hashes the argument or file with this algorithm
s	sha256	Hashes the argument or file with this algorithm
s	address	Converts an address to another format
s	get-public-key	Get the public key from a message and its signature
s	new-key	Creates a new key for use with fuel-core
s	parse-secret	Parses a private key to view the associated public key
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help information	
a	2	0
@	crypto keccak256
o	-h|--help	Print help information	
a	3	0
@	crypto sha256
o	-h|--help	Print help information	
a	3	0
@	crypto address
o	-h|--help	Print help information	
a	3	0
@	crypto get-public-key
o	-h|--help	Print help information	
a	4	0
@	crypto new-key
o	-k	Key type to generate. It can either be `block-production` or `peering`	V
o	-h|--help	Print help information	
a	2	0
=	crypto new-key	-k
v	block-production	
v	peering	
@	crypto parse-secret
o	-k	Key type to generate. It can either be `block-production` or `peering`	V
o	-h|--help	Print help information	
a	3	0
=	crypto parse-secret	-k
v	block-production	
v	peering	
@	crypto help
a	1	0
@	doc
o	-s	Silent mode. Don't output any warnings or errors to the command line	
o	-h|--help	Print help information	
a	9	0
@	fmt
o	-c	Run in 'check' mode	
o	-p	Path to the project, if not specified, current working directory will be used	
o	-f	Formats a single .sw file with the default settings. If not specified, current working directory…	
o	-h|--help	Print help information	
a	2	0
@	submit
o	-h|--help	Print help information	
a	8	0
@	deploy
o	-p	Path to the project, if not specified, current working directory will be used	
o	-t	Terse mode. Limited warning and error output	
o	-o	If set, outputs a binary file representing the script bytes	
o	-g	If set, outputs source file mapping in JSON format	
o	-h|--help	Print help information	
a	33	0
@	help
a	1	0

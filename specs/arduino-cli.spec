@	
s	board	Arduino board commands
s	burn-bootloader	Upload the bootloader on the board using an external programmer
s	cache	Arduino cache commands
s	compile	Compiles Arduino sketches
s	completion	Generates completion scripts for various shells
s	config	Arduino configuration commands
s	core	Arduino core operations
s	daemon	Run as a daemon on port: 50051, the initialization of cores and libraries is done only once
s	debug	Debug Arduino sketches. (this command opens an interactive gdb session)
s	help	Help provides help for any command in the application
s	lib	Arduino commands about libraries
s	monitor	Open a communication port with a board
s	outdated	This commands shows a list of installed cores and/or libraries that can be upgraded. If nothing…
s	sketch	Arduino CLI sketch commands
s	update	Updates the index of cores and libraries to the latest versions
s	upgrade	Upgrades installed cores and libraries to latest version
s	upload	Upload Arduino sketches. This does NOT compile the sketch prior to upload
s	version	Shows the version number of Arduino CLI which is installed on your system
o	--additional-urls	Comma-separated list of additional URLs for the Boards Manager	vp
o	--config-file	The custom config file (if not specified the default will be used)	vp
o	--format	The output format for the logs, can be: text, json, jsonmini, yaml (default 'text')	vp
o	-h|--help	Help for arduino-cli	
o	--log	Print the logs on the standard output	p
o	--log-file	Path to the file where logs will be written	vp
o	--log-format	The output format for the logs, can be: text, json	vp
o	--log-level	Messages with this level and above will be logged. Valid levels are: trace, debug, info, warn…	vp
o	--no-color	Disable colored output	p
=		--config-file
t	filepaths
=		--format
v	text	Output in 'text'
v	json	Output in 'json'
v	jsonmini	Output in 'jsonmini'
v	yaml	Output in 'yaml'
=		--log-file
t	filepaths
=		--log-format
v	text	Output in 'text'
v	json	Output in 'json'
=		--log-level
v	trace	Log level of 'trace
v	debug	Log level of 'debug
v	info	Log level of 'info'
v	warn	Log level of 'warn'
v	error	Log level of 'error'
v	fatal	Log level of 'fatal'
v	panic	Log level of 'panic'
@	board
s	attach	Sets the default values for port and FQBN. If no port or FQBN are specified, the current default…
s	details	Show information about a board, in particular if the board has options to be specified in the FQBN'
s	list	Detects and displays a list of boards connected to the current computer
s	listall	List all boards that have the support platform installed, You can search for a specific board if…
s	search	Search for a board in the Boards Manager using the specified keywords
o	-h|--help	Help for board	
a	1	0
@	board attach
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for attach	
o	-p|--port	Upload port address, example: 'COM3 or /dev/ttyACM2'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
=	board attach	-b
d
=	board attach	-p
d
@	board details
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-f|--full	Show full board details	
o	-h|--help	Help for details	
o	--list-programmers	Show list of available programmers	
o	--show-properties	Show build properties. The properties are expanded, use "--show-properties=unexpanded" if you want…	v
=	board details	-b
d
@	board list
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for list	
o	-w|--watch	Command keeps running and prints list of connected boards whenever there is a change	v
=	board list	-b
d
@	board listall
o	-h|--help	Help for listall	
o	-a|--show-hidden	Show also boards marked as 'hidden' in the platform	
@	board search
o	-h|--help	Help for search	
o	-a|--show-hidden	Show also boards marked as 'hidden' in the platform	
@	burn-bootloader
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for burn-bootloader	
o	-p|--port	Upload port address, example: 'COM3 or /dev/ttyACM2'	v
o	-P|--programmer	Programmer to use, example: 'atmel_ice'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
o	-v|--verbose	Turns on verbose mode	
o	-t|--verify	Verify uploaded binary after upload	
=	burn-bootloader	-b
d
=	burn-bootloader	-p
d
@	cache
s	clean	Delete contents of the directories.downloads folder, where archive files are staged during…
o	-h|--help	Help for cache	
a	1	0
@	cache clean
o	-h|--help	Help for clean	
@	compile
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple option	v
o	--build-cache-path	Builds of 'core.a' are saved into this path to be cached and reused	v
o	--build-path	Path where to save compiled files. If omitted, a directory will be created in the default…	v
o	--build-property	Override a build property with a custom value. Can be used multiple times for multiple properties	v
o	--clean	Optional, cleanup the build folder and do not use any cached build	
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	--dump-profile	Create and print a profile configuration from the build	
o	--encrypt-key	The name of the custom encryption key to use to encrypt a binary during the compile process. Used…	v
o	e|--export-binaries	If set built binaries will be exported to the sketch folder	
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for compile	
o	--keys-keychain	The path of the dir to search for the custom keys to sign and encrypt a binary. Used only by the…	v
o	--libraries	Path to a collection of libraries. Can be used multiple times or entries can be comma separated	v
o	--library	Path to a single library’s root folder. Can be used multiple times or entries can be comma separated	v
o	--only-compilation-database	Just produce the compilation database, without actually compiling. All build commands are skipped…	
o	--optimize-for-debug	Optional, optimize compile output for debugging, rather than for release	
o	--output-dir	Save build artifacts in this directory	v
o	-p|--port	Upload port address, example: 'COM3 or /dev/ttyACM2'	v
o	--preprocess	Print preprocessed code to stdout instead of compiling	
o	-m|--profile	Sketch profile to use	v
o	-P|--programmer	Programmer to use, example: 'atmel_ice'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
o	--quiet	Optional, suppresses almost every output	
o	--show-properties	Show build properties. The properties are expanded, use "--show-properties=unexpanded" if you want…	v
o	--sign-key	The name of the custom signing key to use to sign a binary during the compile process. Used only…	v
o	-u|--upload	Upload the binary after the compilation	
o	-v|--verbose	Optional, turns on verbose mode	
o	-t|--verify	Verify uploaded binary after the upload	
o	--warnings	Optional, can be: none, default, more, all. Used to tell gcc which warning level to use (-W flag)…	v
=	compile	--build-path
t	filepaths
=	compile	-b
d
=	compile	--keys-keychain
t	filepaths,folders
=	compile	--libraries
t	filepaths,folders
=	compile	--library
t	filepaths,folders
=	compile	--output-dir
t	folders
=	compile	-p
d
=	compile	--warnings
v	none	Use warning level 'none'
v	default	Use warning level 'default'
v	more	Use warning level 'more'
v	all	Use warning level 'all'
@	completion
o	-h|--help	Help for completion	
o	--no-description	Disable completion description for shells that support it	
@	config
s	add	Adds one or more values to a setting
s	delete	Deletes a settings key and all its sub keys
s	dump	Prints the current configuration
s	init	Creates or updates the configuration file in the data directory or custom directory with the…
s	remove	Removes one or more values from a setting
s	set	Sets a setting value
o	-h|--help	Help for config	
a	1	0
@	config add
o	-h|--help	Help for add	
@	config delete
o	-h|--help	Help for delete	
@	config dump
o	-h|--help	Help for dump	
@	config init
o	--dest-dir	Sets where to save the configuration file	v
o	--dest-file	Sets where to save the configuration file	v
o	-h|--help	Help for init	
o	--overwrite	Overwrite existing config file	
=	config init	--dest-dir
t	folders
=	config init	--dest-file
t	filepaths
@	config remove
o	-h|--help	Help for remove	
@	config set
o	-h|--help	Help for set	
@	core
s	download	Downloads one or more cores and corresponding tool dependencies
s	install	Installs one or more cores and corresponding tool dependencies
s	list	Show the list of installed platforms
s	search	Search for a core in Boards Manager using the specified keywords
s	uninstall	Uninstalls one or more cores and corresponding tool dependencies if no longer used
s	update-index	Updates the index of cores to the latest version
s	upgrade	Upgrades one or all installed platforms to the latest version
o	-h|--help	Help for core	
a	1	0
@	core download
o	-h|--help	Help for download	
@	core install
o	-h|--help	Help for install	
o	--no-overwrite	Do not overwrite already installed platforms	
o	--run-post-install	Force run of post-install scripts (if the CLI is not running interactively)	
o	--run-pre-uninstall	Force run of pre-uninstall scripts (if the CLI is not running interactively)	
o	--skip-post-install	Force skip of post-install scripts (if the CLI is running interactively)	
o	--skip-pre-uninstall	Force skip of pre-uninstall scripts (if the CLI is running interactively)	
@	core list
o	all	If set return all installable and installed cores, including manually installed	
o	-h|--help	Help for list	
o	--updatable	List updatable platforms	
@	core search
o	all	Show all available core versions	
o	-h|--help	Help for search	
@	core uninstall
o	-h|--help	Help for uninstall	
o	--run-post-install	Force run of post-install scripts (if the CLI is not running interactively)	
o	--run-pre-uninstall	Force run of pre-uninstall scripts (if the CLI is not running interactively)	
o	--skip-post-install	Force skip of post-install scripts (if the CLI is running interactively)	
o	--skip-pre-uninstall	Force skip of pre-uninstall scripts (if the CLI is running interactively)	
@	core update-index
o	-h|--help	Help for update-index	
@	core upgrade
o	-h|--help	Help for upgrade	
o	--run-post-install	Force run of post-install scripts (if the CLI is not running interactively)	
o	--run-pre-uninstall	Force run of pre-uninstall scripts (if the CLI is not running interactively)	
o	--skip-post-install	Force skip of post-install scripts (if the CLI is running interactively)	
o	--skip-pre-uninstall	Force skip of pre-uninstall scripts (if the CLI is running interactively)	
@	daemon
o	--daemonize	Do not terminate daemon process if the parent process dies	
o	--debug	Enable debug logging of gRPC calls	
o	--debug-file	Append debug logging to the specified file	v
o	--debug-filter	Display only the provided gRPC calls	v
o	-h|--help	Help for daemon	
o	--port	The TCP port the daemon will listen to	v
=	daemon	--debug-file
t	filepaths
=	daemon	--port
d
@	debug
s	check	Check if the given board/programmer combination supports debugging
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for debug	
o	-I|--info	Show metadata about the debug session instead of starting the debugger	
o	--input-dir	Directory containing binaries for debug	v
o	--interpreter	Debug interpreter, example: console, mi, mi1, mi2, mi3 (default "console")	v
o	-p|--port	Upload port address, example: 'COM3 or /dev/ttyACM2'	v
o	-P|--programmer	Programmer to use, example: 'atmel_ice'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
a	1	0
=	debug	-b
d
=	debug	--input-dir
t	folders
=	debug	--interpreter
v	console	Debug interpreter 'console'
v	mi	Debug interpreter 'mi'
v	mi1	Debug interpreter 'mi1'
v	mi2	Debug interpreter 'mi2'
v	mi3	Debug interpreter 'mi3'
=	debug	-p
d
@	debug check
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for check	
o	--interpreter	Debug interpreter, example: console, mi, mi1, mi2, mi3 (default "console")	v
o	-p|--port	Upload port address, example: 'COM3 or /dev/ttyACM2'	v
o	-P|--programmer	Programmer to use, example: 'atmel_ice'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
=	debug check	-b
d
=	debug check	--interpreter
v	console	Debug interpreter 'console'
v	mi	Debug interpreter 'mi'
v	mi1	Debug interpreter 'mi1'
v	mi2	Debug interpreter 'mi2'
v	mi3	Debug interpreter 'mi3'
=	debug check	-p
d
@	help
o	-h|--help	Help for help	
@	lib
s	deps	Check dependencies status for the specified library
s	download	Downloads one or more libraries without installing them
s	examples	Shows the list of the examples for libraries. A name may be given as argument to search a specific…
s	install	Installs one or more specified libraries into the system
s	list	Shows a list of installed libraries. If the LIBNAME parameter is specified the listing is limited…
s	search	Search for one or more libraries data (case insensitive search)
s	uninstall	Uninstalls one or more libraries
s	update-index	Updates the libraries index to the latest version
s	upgrade	Upgrades installed libraries. This command upgrades an installed library to the latest available…
o	-h|--help	Help for lib	
a	1	0
@	lib deps
o	-h|--help	Help for deps	
@	lib download
o	-h|--help	Help for download	
@	lib examples
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for examples	
=	lib examples	-b
d
@	lib install
o	--git-url	Enter git url for libraries hosted on repositories	
o	-h|--help	Help for install	
o	--install-in-builtin-dir	Install libraries in the IDE-Builtin directory	
o	--no-deps	Do not install dependencies	
o	--no-overwrite	Do not overwrite already installed libraries	
o	--zip-path	Enter a path to zip file	
@	lib list
o	--all	Include built-in libraries (from platforms and IDE) in listing	
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for list	
o	--updatable	List updatable libraries	
=	lib list	-b
d
@	lib search
o	--h|--help	Help for search	
o	--names	Show library names only	
o	--omit-releases-details	Omit library details far all versions except the latest (produce a more compact JSON output)	
@	lib uninstall
o	--h|--help	Help for uninstall	
@	lib update-index
o	--h|--help	Help for update-index	
@	lib upgrade
o	--h|--help	Help for upgrade	
@	monitor
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	-c|--config	Configure communication port settings. The format is <ID>=<value>[,<ID>=<value>]	v
o	--describe	Show all the settings of the communication port	
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for monitor	
o	-p|--port	Upload port address, example: 'COM3 or /dev/ttyACM2'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
o	-q|--quiet	Run in silent mode, show only monitor input and output	
o	--raw	Set terminal in raw mode (unbuffered)	
o	--timestamp	Timestamp each incoming line	
=	monitor	-b
d
=	monitor	-p
d
@	outdated
o	-h|--help	Help for outdated	
@	sketch
s	archive	Creates a zip file containing all sketch files
s	new	Create a new Sketch
o	-h|--help	Help for sketch	
a	1	0
@	sketch archive
o	-h|--help	Help for archive	
o	--include-build-dir	Includes build in directory in the archive	
o	-f|--overwrite	Overwrites an already existing archive	
@	sketch new
o	-h|--help	Help for archive	
o	-f|--overwrite	Overwrites an already existing .ino sketch	
@	update
o	-h|--help	Help for update	
o	--show-outdated	Show outdated cores and libraries after index update	
@	upgrade
o	-h|--help	Help for update	
o	--run-post-install	Force run of post-install scripts (if the CLI is not running interactively)	
o	--run-pre-uninstall	Force run of pre-uninstall scripts (if the CLI is not running interactively)	
o	--skip-post-install	Force skip of post-install scripts (if the CLI is running interactively)	
o	--skip-pre-uninstall	Force skip of pre-uninstall scripts (if the CLI is running interactively)	
@	upload
o	--board-options	List of board options separated by commas. Or can be used multiple times for multiple options	v
o	--discovery-timeout	Max time to wait for port discovery, example: '30s, 1m (default 1s)'	v
o	-b|--fqbn	Fully Qualified Board Name, example: 'arduino:avr:uno'	v
o	-h|--help	Help for upload	
o	--input-dir	Directory containing binaries to upload	v
o	-i|--input-file	Binary file to upload	v
o	-p|--port	Binary file to upload, example: 'COM3 or /dev/ttyACM2'	v
o	-m|--profile	Sketch profile to use	v
o	-P|--programmer	Programmer to use, example: 'atmel_ice'	v
o	-l|--protocol	Upload port protocol, example: 'serial'	v
o	-F|--upload-field	Set a value for a field required to upload, 'key=value'	v
o	-v|--verbose	Optional, turns on verbose mode	
o	-t|--verify	Verify uploaded binary after the upload	
=	upload	-b
d
=	upload	--input-dir
t	folders
=	upload	-i
t	filepaths
=	upload	-p
d
@	version
o	-h|--help	Help for version	

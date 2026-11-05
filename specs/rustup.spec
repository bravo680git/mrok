@	
s	show	Show the active and installed toolchains or profiles
s	update	Update Rust toolchains and rustup
s	check	Check for updates to Rust toolchains and rustup
s	default	Sets the default toolchain to the one specified. If the toolchain is not already installed then it…
s	target	Modify a toolchain's supported targets
s	toolchain	Modify or query the installed toolchains
s	component	Modify a toolchain's installed components
s	override	Modify directory toolchain overrides
s	run	Run a command with an environment configured for a given toolchain
s	which	Display which binary will be run for a given command
s	doc	Open the documentation for the current toolchain
s	man	View the man page for a given command
s	self	Modify the rustup installation
s	set	Alter rustup settings
s	completions	Generate tab-completion scripts for your shell
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
o	-q|--quiet	Disable progress output	
o	-v|--verbose	Enable verbose output	
a	1	0
@	show
s	active-toolchain	Show the active toolchain
s	home	Display the computed value of RUSTUP_HOME
s	profile	Show the current profile
s	keys	Display the known PGP keys
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
@	show active-toolchain
@	show home
@	show profile
@	show keys
@	show help
@	update
o	--force	Force an update, even if some components are missing	
o	--force-non-host	Install toolchains that require an emulator. See https://github.com/rust-lang/rustup/wiki/Non-host-…	
o	-h|--help	Prints help information	
o	--no-self-update	Don't perform self update when running the `rustup update` command	
a	1	1
#	update	1
d
@	check
o	-h|--help	Prints help information	
a	1	0
@	default
o	-h|--help	Prints help information	
a	1	0
#	default	1
d
@	target
s	list	List installed and available targets
s	add	Add a target to a Rust toolchain
s	remove	Remove a target from a Rust toolchain
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
@	target list
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	target add
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
o	--toolchain		v
a	1	0
=	target add	--toolchain
d
#	target add	1
d
@	target remove
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
o	--toolchain		v
a	1	0
=	target remove	--toolchain
d
#	target remove	1
d
@	target help
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
a	1	0
@	toolchain
s	list	List installed toolchains
s	install	Install or update a given toolchain
s	uninstall	Uninstall a toolchain
s	link	Create a custom toolchain by symlinking to a directory
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
@	toolchain list
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	toolchain install
o	-h|--help	Prints help information	
o	-t|--target	Add specific targets on installation	v
o	-c|--component	Add specific components on installation	v
o	--profile		v
o	--allow-downgrade	Allow rustup to downgrade the toolchain to satisfy your component choice	
o	--force	Force an update, even if some components are missing	
o	--no-self-update	Don't perform self update when running the`rustup toolchain install` command	
a	1	1
=	toolchain install	-t
d
=	toolchain install	--profile
v	minimal	
v	default	
v	complete	
#	toolchain install	1
d
@	toolchain uninstall
o	-h|--help	Prints help information	
a	1	1
#	toolchain uninstall	1
d
@	toolchain link
o	-h|--help	Prints help information	
a	2	0
@	toolchain help
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
a	1	0
@	component
s	list	List installed and available components
s	add	Add a component to a Rust toolchain
s	remove	Remove a component from a Rust toolchain
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
@	component list
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	component add
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	component remove
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	component help
a	1	0
@	override
s	list	List directory toolchain overrides
s	set	Set the override toolchain for a directory
s	unset	Remove the override toolchain for a directory
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
@	override list
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	override set
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
a	1	0
#	override set	1
d
@	override unset
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	override help
a	1	0
@	run
o	-h|--help	Prints help information	
o	--install	Install the requested toolchain if needed	
a	2	1
#	run	1
d
@	which
o	-h|--help	Prints help information	
o	--toolchain	Toolchain name	v
=	which	--toolchain
d
@	doc
o	--alloc	The Rust core allocation and collections library	
o	--book	The Rust Programming Language book	
o	--cargo	The Cargo Book	
o	--core	The Rust Core Library	
o	--edition-guide	The Rust Edition Guide	
o	--embedded-book	The Embedded Rust Book	
o	-h|--help	Prints help information	
o	--nomicon	The Dark Arts of Advanced and Unsafe Rust Programming	
o	--path	Only print the path to the documentation	
o	--proc_macro	A support library for macro authors when defining new macros	
o	--reference	The Rust Reference	
o	--rust-by-example	A collection of runnable examples that illustrate various Rust concepts and standard libraries	
o	--rustc	The compiler for the Rust programming language	
o	--rustdoc	Generate documentation for Rust projects	
o	--std	Standard library API documentation	
o	--test	Support code for rustc's built in unit-test and micro-benchmarking framework	
o	--unstable-book	--unstable-book	
o	--toolchain	Toolchain name	v
a	1	0
=	doc	--toolchain
d
#	doc	1
g	bash -c 'find $(rustup docs --path | sed -e "s|index\.html|std|") $(rustup docs --path | sed -e "s|index\.html|alloc|") $(rustup docs --path | sed -e "s|index\.html|core|") | grep "\.html" | sed -E -e "s|^(.*)/html/||" -e "s|\.html||" -e "s|/|::|g" -e "s/constant\.|trait\.|struct\.|macro\.|fn\.|keyword\.|primitive\.|type\.|enum\.|union\.|traitalias\.|::index$|^(.*)::all$//" -e "/^$/d"'	\n
@	man
o	-h|--help	Prints help information	
o	--toolchain	Toolchain name	v
=	man	--toolchain
d
@	self
s	update	Download and install updates to rustup
s	uninstall	Uninstall rustup
s	upgrade-data	Upgrade the internal data format
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
@	self update
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	self uninstall
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	self upgrade-data
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
@	self help
a	1	0
@	set
s	auto-self-update	The rustup auto self update mode
s	default-host	
o	-h|--help	Prints help information	
@	set auto-self-update
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
a	1	0
#	set auto-self-update	1
v	enable	
v	disable	
v	check-only	
@	set default-host
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
a	1	0
#	set default-host	1
d
@	completions
o	-h|--help	Prints help information	
a	2	0
#	completions	1
v	zsh	
v	bash	
v	fish	
v	powershell	
v	elvish	
#	completions	2
v	rustup	
v	cargo	
@	help
a	1	1

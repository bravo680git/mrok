@	
s	fetch	Fetches a tool to the local machine
s	install	Installs a tool in your toolchain
s	uninstall	Uninstalls a tool from your toolchain
s	pin	Pins your project's runtime or package manager
s	list	Displays the current toolchain
s	completions	Generates Volta completions
s	which	Locates the actual binary that will be called by Volta
s	setup	Enables Volta for the current user
s	run	Run a command with custom Node, npm, and/or Yarn versions
s	help	Prints this message or the help of the given subcommand(s)
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
o	-v|--version	Prints the current version of Volta	
@	fetch
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
a	1	1
@	install
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
a	1	1
@	uninstall
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
a	1	0
@	pin
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
a	1	1
@	list
o	-c|--current	Show the currently-active tool(s)	
o	-d|--default	Show your default tool(s)	
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
o	--format	Specify output format	v
a	1	0
=	list	--format
v	human	
v	plain	
@	completions
o	-f|--force	Write over an existing file, if any	
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
o	-o|--output	File to write generated completions to	v
a	1	0
#	completions	1
v	zsh	
v	bash	
v	fish	
v	powershell	
v	elivsh	
@	which
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
a	1	1
#	which	1
t	filepaths
@	setup
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	-h|--help	Prints help information	
@	run
o	--bundle	Forces npm to be the version bundled with Node	
o	--no-yarn	Disables Yarn	
o	--verbose	Enables verbose diagnostics	
o	--quiet	Prevents unnecessary output	
o	--node	Set the custom Node version	v
o	--npm	Set the custom npm version	v
o	--yarn	Set the custom Yarn version	v
o	--env	Set an environment variable (can be used multiple times)	v
a	1	0
@	help
a	1	0

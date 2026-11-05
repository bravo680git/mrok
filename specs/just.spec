@	
o	--help|-h	Print help information	
o	--changelog	Print the changelog	
o	--check	Run --fmt in 'check' mode	
o	--choose	Select one or more recipes to run using another program	
o	--chooser	Override the binary invoked by --choose	v
o	--color	Print colorful output	v
o	-c|--command	Run an arbitrary command with the working directory, .env, overrides, and exports	v
o	--completions	Print shell completions	v
o	--clear-shell-args	Clear shell arguments	
o	--dry-run	Print what just would do, without doing it	
o	--dump	Print justfile	
o	--dotenv-filename	Use a file with this name instead of .env	v
o	--dotenv-path	Load the environment file from a path instead of searching for one	
o	--dump-format	Specify the format for dumping the justfile	v
o	-e|--edit	Edit the justfile with $VISUAL or $EDITOR, falling back to vim	
o	--evaluate	Evaluate and print all variables	
o	--fmt	Format and overwrite the justfile	
o	--highlight	Highlight echoed recipe lines in bold	
o	--init	Initialize a new justfile	
o	-f|--justfile	Use a specific justfile	v
o	-l|--list	List available recipes and their arguments	
o	--list-heading	Print this text before the list	v
o	--list-prefix	Print this text before each list item	v
o	--no-dotenv	Don't load the environment file	
o	--no-highlight	Don't highlight echoed recipe lines	
o	-q|--quiet	Suppress all output	
o	--set	Override a variable with a value	v
o	--shell	Invoke this shell to run recipes	v
o	--shell-arg	Invoke the shell with this as an argument	v
o	--shell-command	Invoke --command with the shell used to run recipe lines and backticks	
o	-s|--show	Show information about a recipe	v
o	--summary	List names of available recipes	
o	-u|--unsorted	Return list and summary entries in source order	
o	--unstable	Enable unstable features	
o	--variables	List names of variables	
o	-v|--verbose	Use verbose output	
o	-V|--version	Print version information	
o	-d|--working-directory	Use this as the working directory	v
a	1	1
=		--color
v	auto	
v	always	
v	never	
=		--completions
v	zsh	
v	bash	
v	fish	
v	powershell	
v	elvish	
=		--dump-format
v	just	
v	json	This value requires --unstable
=		-f
t	filepaths
=		--set
d
=		-s
d
=		-d
t	folders
#		1
d

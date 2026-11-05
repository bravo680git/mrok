@	
s	add	Add an alias via the cli
s	clone	Clone external aliases
s	directories	List all directories initialized with aliases
s	exec	Execute an alias for a given directory
s	help	Prints help information
s	init	Initialize a directory for aliases
s	list	List the aliases available
s	pull	Pull a cloned user's aliases
s	rehash	Update the aliases
s	remove	Remove an alias via the cli
s	users	List the users
o	--help|-h	Prints help information	p
o	--version|-V	Prints version information	p
@	add
a	2	0
@	clone
o	-E|--enable	Whether to enable the user if they are not currently enabled	
a	2	0
@	directories
@	exec
a	2	1
#	exec	1
t	folders
@	help
@	init
o	-g|--global	Returns the global initialization for the app	
o	-u|--user	Initialize aliases for a specific user	v
@	list
o	-g|--global	List only global aliases	
o	-l|--local	List only local aliases	
o	-d|--directory	List aliases for a specific directory	v
o	name	List aliases for with a specific name	v
=	list	-d
t	folders
@	pull
a	1	0
@	rehash
@	remove
a	1	0
@	users
s	disable	Disable a user's aliases
s	enable	Enable a user's aliases
s	help	Prints this message or the help of the given subcommand(s)
s	move	Move a user up or down the prioritization list
s	use	Assign a user to the top of the priority list
@	users disable
a	1	0
@	users enable
a	1	0
@	users help
@	users move
a	2	0
@	users use
a	1	0

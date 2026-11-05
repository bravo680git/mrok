@	
s	add	Add a new directory or increment its rank
s	import	Import entries from another application
s	init	Generate shell configuration
s	query	Search for a directory in the database
s	remove	Remove a directory from the database
o	-h|--help	Print help information	
o	-V|--version	Print version information	
@	add
o	-h|--help	Print help information	
o	-V|--version	Print version information	
a	1	1
#	add	1
t	folders
@	import
o	--from	Application to import from	v
o	--merge	Merge into existing database	
o	-h|--help	Print help information	
o	-V|--version	Print version information	
a	1	0
=	import	--from
v	autojump	
v	z	
#	import	1
t	filepaths
@	init
o	--cmd	Changes the prefix of the `z` and `zi` commands	V
o	--hook	Changes how often zoxide increments a directory's score	V
o	--no-cmd	Prevents zoxide from defining the `z` and `zi` commands	
o	-h|--help	Print help information	
o	-V|--version	Print version information	
a	1	0
=	init	--hook
v	none	
v	prompt	
v	pwd	
#	init	1
v	bash	
v	elvish	
v	fish	
v	nushell	
v	posix	
v	powershell	
v	xonsh	
v	zsh	
@	query
o	--exclude	Exclude a path from results	V
o	--all	Show deleted directories	
o	-i|--interactive	Use interactive selection	
o	-l|--list	List all matching directories	
o	-s|--score	Print score with results	
o	-h|--help	Print help information	
o	-V|--version	Print version information	
a	1	0
=	query	--exclude
t	folders
@	remove
o	-i|--interactive	Use interactive selection	
o	-h|--help	Print help information	
o	-V|--version	Print version information	
a	1	0
#	remove	1
t	folders

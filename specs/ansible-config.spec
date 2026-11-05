@	
s	list	List and output available configs
s	dump	Shows the current settings, merges ansible.cfg if specified
s	view	Displays the current config file
s	init	Initializes a new config file (to stdout)
o	--version	Shows version number, config file location, module search path, module location, executable…	
o	--help|-h	Show help and exit	
@	list
o	--help|-h	Show help and exit	
o	--verbose	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	-v	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	--config|-c	Path to configuration file, defaults to first file found in precedence	v
o	--type|-t	Filter down to a specific plugin type	v
a	1	1
=	list	--config
t	filepaths
=	list	--type
v	all	
v	base	
v	become	
v	cache	
v	callback	
v	cliconf	
v	connection	
v	httpapi	
v	inventory	
v	lookup	
v	netconf	
v	shell	
v	vars	
@	dump
o	--help|-h	Show help and exit	
o	--verbose	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	-v	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	--only-changed|--changed-only	Only show configurations that have changed from the default	
o	--config|-c	Path to configuration file, defaults to first file found in precedence	v
o	--type|-t	Filter down to a specific plugin type	v
a	1	1
=	dump	--config
t	filepaths
=	dump	--type
v	all	
v	base	
v	become	
v	cache	
v	callback	
v	cliconf	
v	connection	
v	httpapi	
v	inventory	
v	lookup	
v	netconf	
v	shell	
v	vars	
@	view
o	--help|-h	Show help and exit	
o	--verbose	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	-v	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	--config|-c	Path to configuration file, defaults to first file found in precedence	v
o	--type|-t	Filter down to a specific plugin type	v
a	1	1
=	view	--config
t	filepaths
=	view	--type
v	all	
v	base	
v	become	
v	cache	
v	callback	
v	cliconf	
v	connection	
v	httpapi	
v	inventory	
v	lookup	
v	netconf	
v	shell	
v	vars	
@	init
o	--help|-h	Show help and exit	
o	--verbose	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	-v	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	
o	--disabled	Prefixes all entries with a comment character to disable them	
o	--format|-f	Output format for init	V
o	--config|-c	Path to configuration file, defaults to first file found in precedence	v
o	--type|-t	Filter down to a specific plugin type	v
a	1	1
=	init	--format
v	ini	
v	env	
v	vars	
=	init	--config
t	filepaths
=	init	--type
v	all	
v	base	
v	become	
v	cache	
v	callback	
v	cliconf	
v	connection	
v	httpapi	
v	inventory	
v	lookup	
v	netconf	
v	shell	
v	vars	

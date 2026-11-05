@	
s	help	
s	list	
s	new	Create a new Laravel application
o	-h|--help	Display the help message	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
@	help
o	--format	The output format (txt, xml, json, or md)	v
o	--raw	To output raw command list	
=	help	--format
v	txt	
v	xml	
v	json	
v	md	
@	list
o	--format	The output format (txt, xml, json, or md)	v
o	--raw	To output raw command list	
=	list	--format
v	txt	
v	xml	
v	json	
v	md	
@	new
o	--dev	Installs the latest "development" release	
o	--git	Initialize a Git repository	
o	--branch	The branch that should be created for a new repository	v
o	--github	Create a new repository on GitHub	V
o	--jet	Installs the Laravel Jetstream scaffolding	
o	--stack	The Jetstream stack that should be installed	v
o	--teams	Indicates whether Jetstream should be scaffolded with team support	
o	--prompt-jetstream	Issues a prompt to determine if Jetstream should be installed	
o	-f|--force	Forces install even if the directory already exists	
a	1	0
=	new	--stack
v	livewire	
v	inertia	

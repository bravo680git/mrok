@	
s	completion	Generate the autocompletion script for the specified shell
s	copy|cp	Copy files between host and guest
s	delete|remove|rm	Delete an instance of Lima
s	info	Show diagnostic information
s	list|ls	List instances of Lima
s	prune	Prune garbage objects
s	shell	Lima command is provided as an alias for limactl shell $LIMA_INSTANCE. $LIMA_INSTANCE defaults to…
s	show-ssh	Show the ssh command line
s	start	Start an instance of Lima. If the instance does not exist, open an editor for creating new one…
s	stop	Stop an instance
s	sudoers	Generate /etc/sudoers.d/lima file for enabling vmnet.framework support. See…
s	validate	Validate YAML files
s	help	Help provides help for any command in the application
o	-h|--help	Help for limactl	
o	--debug	Debug mode	
o	-v|--version	Version for limactl	
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
o	-h|--help	Help for completion	
o	--debug	Debug mode	
@	completion bash
o	-h|--help	Help for bash	
o	--debug	Debug mode	
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	-h|--help	Help for fish	
o	--debug	Debug mode	
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	-h|--help	Help for powershell	
o	--debug	Debug mode	
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	-h|--help	Help for zsh	
o	--debug	Debug mode	
o	--no-descriptions	Disable completion descriptions	
@	copy
o	-h|--help	Help for copy	
o	--debug	Debug mode	
o	-r|--recursive	Copy directories recursively	
a	2	0
#	copy	1
t	filepaths
d
#	copy	2
t	filepaths
d
@	delete
o	-h|--help	Help for delete	
o	--debug	Debug mode	
o	-f|--force	Forcibly kill the processes	
a	1	1
#	delete	1
d
@	info
o	-h|--help	Help for info	
o	--debug	Debug mode	
@	list
o	-h|--help	Help for list	
o	--debug	Debug mode	
o	--json	JSONify output	
o	-q|--quiet	Only show names	
@	prune
o	-h|--help	Help for prune	
o	--debug	Debug mode	
@	shell
o	-h|--help	Help for shell	
o	--debug	Debug mode	
o	--workdir	Working directory	v
a	2	1
#	shell	1
d
@	show-ssh
o	-h|--help	Help for show-ssh	
o	--debug	Debug mode	
o	-f|--format	Format: cmd, args, options, config (default "cmd")	v
a	1	0
=	show-ssh	-f
v	cmd	Full ssh command line
v	args	Similar to the cmd format but omits "ssh" and the destination address
v	options	Ssh option key value pairs
v	config	~/.ssh/config format
#	show-ssh	1
d
@	start
o	-h|--help	Help for start	
o	--debug	Debug mode	
o	--tty	Enable TUI interactions such as opening an editor, defaults to true when stdout is a terminal…	
a	1	0
#	start	1
d
@	stop
o	-h|--help	Help for stop	
o	--debug	Debug mode	
o	-f|--force	Force stop the instance	
a	1	0
#	stop	1
d
@	sudoers
o	-h|--help	Help for sudoers	
o	--debug	Debug mode	
o	--check	Check that the sudoers file is up-to-date with "~/.lima/_config/networks.yaml"	
a	1	0
#	sudoers	1
t	filepaths
@	validate
o	-h|--help	Help for validate	
o	--debug	Debug mode	
a	1	1
#	validate	1
d
@	help
a	1	0
#	help	1
v	completion	Generate the autocompletion script for the specified shell
v	copy	Copy files between host and guest
v	cp	Copy files between host and guest
v	delete	Delete an instance of Lima
v	remove	Delete an instance of Lima
v	rm	Delete an instance of Lima
v	info	Show diagnostic information
v	list	List instances of Lima
v	ls	List instances of Lima
v	prune	Prune garbage objects
v	shell	Lima command is provided as an alias for limactl shell $LIMA_INSTANCE. $LIMA_INSTANCE defaults to…
v	show-ssh	Show the ssh command line
v	start	Start an instance of Lima. If the instance does not exist, open an editor for creating new one…
v	stop	Stop an instance
v	sudoers	Generate /etc/sudoers.d/lima file for enabling vmnet.framework support. See…
v	validate	Validate YAML files
v	help	Help provides help for any command in the application

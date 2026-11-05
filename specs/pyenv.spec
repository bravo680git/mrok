@	
s	commands	Lists all available pyenv commands
s	local	Sets a local application-specific Python version
s	global	Sets the global version of Python to be used in all shells
s	shell	Sets a shell-specific Python version
s	install	Install a Python version
s	uninstall	Performs a deployment (default)
s	rehash	Performs a deployment (default)
s	version	Displays the currently active Python version, along with information on how it was set
s	versions	Lists all Python versions known to pyenv, and shows an asterisk next to the currently active version
s	which	Displays the full path to the executable that pyenv will invoke when you run the given command
s	whence	Lists all Python versions with the given command installed
o	-h|--help	Output usage information	
a	1	0
@	commands
@	local
o	--unset		
a	1	1
@	global
a	1	0
#	global	1
d
@	shell
o	--unset		
a	1	0
@	install
o	-l|--list	List all available versions	
o	-f|--force	Install even if the version appears to be installed already	
o	-s|--skip-existing	Skip the installation if the version appears to be installed already	
o	-k|--keep	Keep source tree in $PYENV_BUILD_ROOT after installation	
o	-v|--verbose	Verbose mode: print compilation status to stdout	
o	-p|--patch	Apply a patch from stdin before building	
o	-g|--debug	Build a debug version	
a	1	0
#	install	1
d
@	uninstall
o	-f|--force	Attempt to remove the specified version without prompting for confirmation	
a	1	0
@	rehash
@	version
@	versions
o	--bare	Print only the version names, one per line	
o	--skip-aliases	Skip printing aliases	
@	which
a	1	0
@	whence
a	1	0

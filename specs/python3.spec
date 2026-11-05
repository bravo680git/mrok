@	
o	-c	Execute the Python code in command. command can be one or more statements separated by newlines…	v
o	-m	Search sys.path for the named module and execute its contents as the __main__ module	v
o	-?|-h|--help	Print a short description of all command line options	
o	-V|--version	Print the Python version number and exit	
o	-b	Issue a warning when comparing bytes or bytearray with str or bytes with int. Issue an error when…	
o	-B	If given, Python won’t try to write .pyc files on the import of source modules	
o	--check-hash-based-pycs	Control the validation behavior of hash-based .pyc files. See Cached bytecode invalidation	v
o	-d	Turn on parser debugging output (for expert only, depending on compilation options)	
o	-E	Ignore all PYTHON* environment variables, e.g. PYTHONPATH and PYTHONHOME, that might be set	
o	-i	When a script is passed as first argument or the -c option is used, enter interactive mode after…	
o	-I	Run Python in isolated mode. This also implies -E and -s. In isolated mode sys.path contains…	
o	-O	Remove assert statements and any code conditional on the value of __debug__	
o	-OO	Do -O and also discard docstrings	
o	-g	Don’t display the copyright and version messages even in interactive mode	
o	-R	Turn on hash randomization. This option only has an effect if the PYTHONHASHSEED environment…	
o	-s	Don’t add the user site-packages directory to sys.path	
o	-S	Disable the import of the module site and the site-dependent manipulations of sys.path that it…	
o	-u	Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream	
o	-v	Print a message each time a module is initialized, showing the place (filename or built-in module)…	
o	-W	Warning control. Python’s warning machinery by default prints warning messages to sys.stderr	v
o	-x	Skip the first line of the source, allowing use of non-Unix forms of #!cmd. This is intended for a…	
o	-X	Reserved for various implementation-specific options	v
a	1	0
=		--check-hash-based-pycs
v	default	
v	always	
v	never	
=		-X
v	faulthandler	
v	showrefcount	
v	tracemalloc	
v	showalloccount	
v	importtime	
v	dev	
v	utf8	
v	pycache_prefix=PATH	
#		1
d

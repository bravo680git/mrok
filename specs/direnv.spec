@	
s	allow	Grants direnv to load the given .envrc
s	deny	Revokes the authorization of a given .envrc
s	edit	Opens PATH_TO_RC or the current .envrc into an $EDITOR and allow the file to be loaded afterwards
s	exec	Executes a command after loading the first .envrc found in DIR
s	fetchurl	Fetches a given URL into direnv's CAS
s	help	Help for direnv
s	hook	Used to setup the shell hook
s	prune	Removes old allowed files
s	reload	Triggers an env reload
s	status	Prints some debug status information
s	stdlib	Displays the stdlib available in the .envrc execution context
s	version	Prints the version or checks that direnv is older than VERSION_AT_LEAST
s	apply_dump	Accepts a filename containing `direnv dump` output and generates a series of bash export…
s	show_dump	Show the data inside of a dump for debugging purposes
s	dotenv	Transforms a .env file to evaluatable `export KEY=PAIR` statements
s	dump	Used to export the inner bash state at the end of execution
s	export	Loads an .envrc and prints the diff in terms of exports
s	watch	Adds a path to the list that direnv watches for changes
s	watch-dir	Recursively adds a directory to the list that direnv watches for changes
s	watch-list	Pipe pairs of `mtime path` to stdin to build a list of files to watch
s	current	Reports whether direnv's view of a file is current (or stale)
o	--version	Prints the version or checks that direnv is older than VERSION_AT_LEAST	V
o	--help	Help for direnv	V
@	allow
a	1	0
#	allow	1
t	filepaths
@	deny
a	1	0
#	deny	1
t	filepaths
@	edit
a	1	0
#	edit	1
t	filepaths
@	exec
a	2	0
#	exec	1
t	folders
@	fetchurl
a	2	0
@	help
a	1	0
@	hook
a	1	0
#	hook	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
@	prune
@	reload
@	status
@	stdlib
@	version
a	1	0
@	apply_dump
a	1	0
#	apply_dump	1
t	filepaths
@	show_dump
a	1	0
#	show_dump	1
t	filepaths
@	dotenv
a	2	0
#	dotenv	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
#	dotenv	2
d
@	dump
a	2	0
#	dump	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
#	dump	2
t	filepaths
@	export
a	1	0
#	export	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
@	watch
a	2	1
#	watch	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
#	watch	2
t	filepaths
@	watch-dir
a	2	0
#	watch-dir	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
#	watch-dir	2
t	folders
@	watch-list
a	1	0
#	watch-list	1
v	bash	
v	zsh	
v	fish	
v	tcsh	
v	elvish	
@	current
a	1	0
#	current	1
t	filepaths

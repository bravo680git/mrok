@	
s	run	Compile and run the program
s	crun	Compile if executable inexistent or not updated and run the program
s	watch	Watch the file for changes and recompile
s	new	Setup the file structure for a V project (in a sub folder)
s	init	Setup the file structure for an already existing V project
s	test	Run all test files in the provided directory
s	fmt	Format the V code provided
s	vet	Report suspicious code constructs
s	doc	Generate documentation for a V module
s	vlib-docs	Generate and open the documentation of all the vlib modules
s	repl	Run the REPL
s	where	Find and print the location of current project declarations
s	symlink	Create a symbolic link for V
s	up	Run the V self-updater
s	self	Run the V self-compiler
s	help	Display help for V
o	--help|-h	Show help for V	
o	version|--version|-v	Show V installed version	
a	1	0
#		1
t	filepaths
@	run
a	1	0
#	run	1
t	filepaths
@	crun
a	1	0
#	crun	1
t	filepaths
@	watch
s	run	Run the program after recompiling
a	1	0
#	watch	1
t	filepaths
@	watch run
a	1	0
#	watch run	1
t	filepaths
@	new
@	init
@	test
@	fmt
a	1	0
#	fmt	1
t	filepaths
@	vet
@	doc
@	vlib-docs
@	repl
@	where
@	symlink
@	up
@	self
o	-prod	Compile V for production (optimize compilation)	
@	help
s	other	Display help for less frequently used commands
s	topics	Display a list of all known help topics
a	1	0
#	help	1
d
@	help other
@	help topics

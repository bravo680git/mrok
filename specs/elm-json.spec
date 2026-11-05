@	
s	help	Prints help information or the help of the given subcommand(s)
s	install	Install a package
s	new	Create a new elm.json file
s	tree	List entire dependency graph as a tree
s	uninstall	Uninstall a package
s	upgrade	Bring your dependencies up to date
o	--help|-h	Prints help information	
o	--offline	Enable offline mode, which means no HTTP traffic will happen	
o	--version|-V	Prints version information	
o	--verbose|-v	Sets the level of verbosity	
@	help
a	1	0
#	help	1
t	help
@	install
o	--help|-h	Prints help information	
o	--test	Install as a test-dependency	
o	--version|-V	Prints version information	
o	--yes	Answer "yes" to all questions	
a	2	0
#	install	1
d
#	install	2
d
@	new
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
@	tree
o	--help|-h	Prints help information	
o	--test	Promote test-dependencies to top-level dependencies	
o	--version|-V	Prints version information	
a	2	0
#	tree	1
d
#	tree	2
d
@	uninstall
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--yes	Answer "yes" to all questions	
a	2	0
#	uninstall	1
d
#	uninstall	2
d
@	upgrade
o	--help|-h	Prints help information	
o	--unsafe	Allow major versions bumps	
o	--version|-V	Prints version information	
o	--yes	Answer "yes" to all questions	
a	1	0
#	upgrade	1
d

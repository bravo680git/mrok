@	
s	i|install	Install a package
s	delete	Delete a package
s	upgrade	Upgrade trex
s	tree	View dependency tree
s	run	Run a script alias in a file run.json
s	purge	Remove a package or url from cache
s	ls	Shows the list of installed packages
s	exec	Execute a cli tool with out install then
s	check	Check deno.land [std/x] dependencies updates
o	-h|--help	Print help info	p
o	-v|--version	Print version	
o	-c|--custom	Install custom package	v
@	i
o	-m|--map	Install package from deno.land	v
o	-n|--nest	Install package from nest.land	v
o	-p|--pkg	Install package from some repository	v
@	delete
a	1	0
#	delete	1
d
@	upgrade
o	--canary	Install from dev branch	
@	tree
@	run
o	-w|--watch	Use reboot script alias protocol (rsap)	
o	-wv	Verbose output in --watch mode (rsap)	
a	1	0
#	run	1
d
@	purge
a	1	0
#	purge	1
d
@	ls
@	exec
o	--perms	Specify cli permisions	
a	1	0
@	check
o	-f|--fix	Update outdated dependencies	

@	
s	add	Adds the current working directory to your warp points
s	rm	Removes the given warp point
s	show	Print path to given warp point
s	list	Print all stored warp points
s	ls	Show files from given warp point (ls)
s	path	Show the path to given warp point (pwd)
s	clean	Remove points warping to nonexistent directories (will prompt unless --force is used)
s	help	Shows help for wd
o	-v|--version	Print version	
o	-d|--debug	Exit after execution with exit codes (for testing)	
o	-c|--config	Specify config file (default ~/.warprc)	v
o	-q|--quiet	Suppress all output	
o	-f|--force	Allows overwriting without warning (for add & clean)	
a	2	0
#		1
d
@	add
a	1	0
@	rm
a	1	0
#	rm	1
d
@	show
a	1	0
#	show	1
d
@	list
@	ls
a	1	0
#	ls	1
d
@	path
a	1	0
#	path	1
d
@	clean
@	help

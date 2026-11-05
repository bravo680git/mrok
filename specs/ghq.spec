@	
s	get	Clone/sync with a remote repository
s	list	List local repositories
s	root	Show repositories' root
s	create	Create a new repository
o	-h|--help|h|help	Show help	p
o	-v|--version	Print the version	
@	get
o	-u|--update	Update local repository if cloned already (default: false)	
o	-p	Clone with SSH (default: false)	
o	--shallow	Do a shallow clone (default: false)	
o	-l|--look	Look after get (default: false)	
o	--vcs	Specify vcs backend for cloning	v
o	-s|--silent	Clone or update silently (default: false)	
o	--no-recursive	Prevent recursive fetching (default: false)	
o	-b|--branch	Specify branch name. This flag implies --single-branch on Git	v
o	-P|--parallel	Import parallelly (default: false)	
o	--bare	Do a bare clone (default: false)	
a	1	0
@	list
o	-e|--exact	Perform an exact match (default: false)	
o	--vcs	Specify vcs backend for matching	v
o	-p|--full-path	Print full paths (default: false)	
o	--unique	Print unique subpaths (default: false)	
a	1	0
@	root
o	--all	Show all roots (default: false)	
@	create
o	--vcs	Specify vcs backend explicitly	v
a	1	0

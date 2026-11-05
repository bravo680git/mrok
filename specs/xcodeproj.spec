@	
s	config-dump	Dumps the build settings of all project targets for all configurations in directories named by the…
s	project-diff	Shows the difference between two projects
s	show	Shows an overview of a project in a YAML representation
s	sort	Sorts the given project
s	target-diff	Shows the difference between two targets
o	--verbose	Show more debugging information	p
o	--version	Show the version of the tool	
o	--no-ansi	Show output without ANSI codes	p
o	--help	Show help banner of specified command	p
@	config-dump
a	2	0
#	config-dump	1
t	folders
#	config-dump	2
t	folders
@	project-diff
o	--ignore	A key to ignore in the comparison. Can be specified multiple times	v=
a	2	0
#	project-diff	1
t	folders
#	project-diff	2
t	folders
@	show
o	--format	YAML output format	v=
a	1	0
=	show	--format
v	hash	
v	tree_hash	
v	raw	
#	show	1
t	folders
@	sort
o	--group-option	The position of the groups when sorting. If no option is specified sorting will interleave groups…	v=
a	1	0
=	sort	--group-option
v	above	
v	below	
#	sort	1
t	folders
@	target-diff
o	--project	The Xcode project document to use	v
a	2	0
=	target-diff	--project
t	folders

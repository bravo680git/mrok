@	
s	apply	Apply a preset
s	init	Create a new preset
o	--path|-p	Path to a sub-directory in which to look for a preset	v
o	--tag|-t	Branch or tag to use if the preset is a repository	v
o	--no-ssh	Do not use SSH when cloning repositories	
o	--no-cache	Do not use the cached repository if it exists	
o	--help|-h	Show help for preset	
o	--version|-v	Show the version number	
o	--no-interaction	Disable interactions	p
o	--debug	Display debug information instead of standard output	p
o	--silent	Do not print anything	p
a	2	0
#		1
t	folders,filepaths,history
#		2
t	folders
@	apply
o	--path|-p	Path to a sub-directory in which to look for a preset	v
o	--tag|-t	Branch or tag to use if the preset is a repository	v
o	--no-ssh	Do not use SSH when cloning repositories	
o	--no-cache	Do not use the cached repository if it exists	
a	2	0
#	apply	1
t	folders,filepaths,history
#	apply	2
t	folders
@	init
a	1	0
#	init	1
t	folders

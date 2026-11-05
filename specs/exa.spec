@	
o	-?|--help	Show list of command-line options	
o	-v|--version	Show version of exa	
o	-1|--oneline	Display one entry per line	
o	-l|--long	Display extended file metadata as a table	
o	-G|--grid	Display entries as a grid (default)	
o	-x|--across	Sort the grid across, rather than downwards	
o	-R|--recurse	Recurse into directories	
o	-T|--tree	Recurse into directories as a tree	
o	-F|--classify	Display type indicator by file names	
o	--colour|--color	When to use terminal colours (always, auto, never)	v=
o	--colour-scale|--color-scale	Highlight levels of file sizes distinctly	
o	-a|--all	Show hidden and 'dot' files	
o	-d|--list-dirs	List directories like regular files	
o	-L|--level	Limit the depth of recursion	v
o	-r|--reverse	Reverse the sort order	
o	-s|--sort	Which field to sort by	v
o	--group-directories-first	List directories before other files	
o	-D|--only-dirs	List only directories	
o	-I|--ignore-glob	Glob patterns (pipe-separated) of files to ignore	v
o	--git-ignore	Ignore files mentioned in '.gitignore'	
o	-b|--binary	List file sizes with binary prefixes	
o	-B|--bytes	List file sizes in bytes, without any prefixes	
o	-g|--group	List each file's group	
o	-h|--header	Add a header row to each column	
o	-H|--links	List each file's number of hard links	
o	-i|--inode	List each file's inode number	
o	-m|--modified	Use the modified timestamp field	
o	-S|--blocks	Show number of file system blocks	
o	-t|--time	Which timestamp field to list (modified, accessed, created)	v
o	-u|--accessed	Use the accessed timestamp field	
o	-U|--created	Use the created timestamp field	
o	--time-style	How to format timestamps (default, iso, long-iso, full-iso)	v
o	--git	List each file's Git status, if tracked or ignored	
o	-@|--extended	List each file's extended attributes and sizes	
o	--icons	Shows icons before each folder or file	
o	--no-icons	Does not display icons	
o	--changed	Displays when a file or folder got changed instead of modified in the header	
a	1	1
=		--colour
v	always	
v	auto	
v	never	
=		-s
v	name	
v	Name	
v	extension	
v	Extension	
v	size	
v	type	
v	modified	
v	accessed	
v	created	
v	inode	
v	none	
v	date	
v	time	
v	old	
v	new	
=		-t
v	modified	
v	accessed	
v	created	
=		--time-style
v	default	
v	iso	
v	long-iso	
v	full-iso	
#		1
t	filepaths

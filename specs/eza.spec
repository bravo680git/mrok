@	
o	-?|--help	Show list of command-line options	
o	-v|--version	Show version of eza	
o	-1|--oneline	Display one entry per line	
o	-l|--long	Display extended file metadata as a table	
o	-G|--grid	Display entries as a grid (default)	
o	-x|--across	Sort the grid across, rather than downward	
o	-R|--recurse	Recurse into directories	
o	-T|--tree	Recurse into directories as a tree	
o	-X|--dereference	Dereference symbolic links when displaying information	
o	-F|--classify	Display type indicator by file names	v
o	--color|--colour	When to use terminal colours	v
o	--color-scale|--colour-scale	Highlight levels of 'field' distinctly	v=
o	--color-scale-mode|--colour-scale-mode	Use gradient or fixed colors in --color-scale	v
o	--icons	When to display icons	v
o	--no-quotes	Don't quote file names with spaces	
o	--hyperlink	Display entries as hyperlinks	
o	--absolute	Display entries with their absolute path	v
o	--follow-symlinks	Drill down into symbolic links that point to directories	
o	-w|--width	Set screen width in columns	v
o	-a|--all	Show hidden and 'dot' files	
o	-A|--almost-all	Equivalent to '--all'	
o	-d|--list-dirs	List directories like regular files	
o	-D|--only-dirs	List only directories	
o	-f|--only-files	List only files	
o	--show-symlinks	Explicitly show symbolic links	
o	--no-symlinks	Do not show symbolic links	
o	-L|--level	Limit the depth of recursion	v
o	-r|--reverse	Reverse the sort order	
o	-s|--sort	Which field to sort by	v
o	--group-directories-first	List directories before other files	
o	--group-directories-last	List directories after other files	
o	-I|--ignore-glob	Glob patterns (pipe-separated) of files to ignore	v
o	--git-ignore	Ignore files mentioned in '.gitignore'	
o	-b|--binary	List file sizes with binary prefixes	
o	-B|--bytes	List file sizes in bytes, without any prefixes	
o	-g|--group	List each file's group	
o	--smart-group	Only show group if it has a different name from owner	
o	-h|--header	Add a header row to each column	
o	-H|--links	List each file's number of hard links	
o	-i|--inode	List each file's inode number	
o	-M|--mounts	Show mount details	
o	-n|--numeric	List numeric user and group IDs	
o	-O|--flags	List file flags	
o	-S|--blocksize	Show size of allocated file system blocks	
o	-t|--time	Which timestamp field to list	v
o	-m|--modified	Use the modified timestamp field	
o	-u|--accessed	Use the accessed timestamp field	
o	-U|--created	Use the created timestamp field	
o	--changed	Use the changed timestamp field	
o	--time-style	How to format timestamps	v
o	--total-size	Show the size of a directory as the size of all files and directories inside	
o	-o|--octal-permissions	List each file's permission in octal format	
o	--no-permissions	Suppress the permissions field	
o	--no-filesize	Suppress the filesize field	
o	--no-user	Suppress the user field	
o	--no-time	Suppress the time field	
o	--stdin	Read file names from stdin, one per line or other separator specified in environment	
o	--git	List each file's Git status, if tracked or ignored	
o	--no-git	Suppress Git status	
o	--git-repos	List root of git-tree status	
o	--git-repos-no-status	List each git-repos branch name (much faster)	
o	-@|--extended	List each file's extended attributes and sizes	
o	-Z|--context	List each file's security context	
a	1	1
=		-F
v	auto	Display file kind indicators only when the standard output is connected to a real terminal
v	automatic	Display file kind indicators only when the standard output is connected to a real terminal
v	always	Always display file kind indicators
v	never	Disables the use of file kind indicators
=		--color
v	auto	To colorize the output only when the standard output is connected to a real terminal
v	automatic	To colorize the output only when the standard output is connected to a real terminal
v	always	Always output terminal color
v	never	Disables the use of terminal color
=		--color-scale
v	all	
v	age	
v	size	
=		--color-scale-mode
v	fixed	
v	gradient	
=		--icons
v	auto	Display icons only when the standard output is connected to a real terminal
v	automatic	Display icons only when the standard output is connected to a real terminal
v	always	Always display icons
v	never	Disables the use of icons
=		--absolute
v	off	
v	on	
v	follow	
=		-s
v	name	Lowercase precede UPERCASE
v	Name	UPERCASE precede lowercase
v	extension	Lowercase precede UPERCASE
v	Extension	UPERCASE precede lowercase
v	size	
v	modified	
v	changed	
v	accessed	
v	created	
v	inode	
v	type	
v	none	
v	date	
v	time	
v	new	
v	newest	
v	age	
v	old	
v	oldest	
=		-t
v	modified	
v	changed	
v	accessed	
v	created	
=		--time-style
v	default	
v	iso	
v	long-iso	
v	relative	
v	+%Y-%m-%d %H:%M	
#		1
t	folders

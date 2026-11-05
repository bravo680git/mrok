@	
o	-H|--hidden	Search hidden files and directories	
o	-I|--no-ignore	Do not respect .(git|fd)ignore files	
o	-s|--case-sensitive	Case-sensitive search (default: smart case)	
o	-i|--ignore-case	Case-insensitive search (default: smart case)	
o	-g|--glob	Glob-based search (default: regular expression)	
o	-a|--absolute-path	Show absolute instead of relative paths	
o	-l|--list-details	Use a long listing format with file metadata	
o	-L|--follow	Follow symbolic links	
o	-p|--full-path	Search full path (default: file-/dirname only)	
o	-0|--print0	Separate results by the null character	
o	-h|--help	Prints help information	
o	-V|--version	Prints version information	
o	-d|--max-depth	Set maximum search depth	v
o	-t|--type	Filter by type	v
o	-e|--extension	Filter by file extension	v
o	-x|--exec	Execute a command for each search result	v
o	-X|--exec-batch	Execute a command with all search results at once	v
o	-E|--exclude	Exclude entries that match the given glob pattern	v
o	-c|--color	When to use colors	v
o	-S|--size	Limit results based on the size of files	v
o	--changed-within	Filter by file modification time (newer than)	v
o	--changed-before	Filter by file modification time (older than)	v
a	2	1
=		-t
v	f	File
v	d	Directory
v	l	Symlink
v	x	Executable
v	e	Empty
v	s	Socket
v	p	Pipe
=		-c
v	never	
v	auto	
v	always	
#		2
t	folders

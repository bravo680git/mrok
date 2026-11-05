@	
o	--help	Print a usage message briefly summarizing these command-line options and the bug-reporting…	
o	-E|--extended-regexp	Interpret PATTERN as an extended regular expression (-E is specified by POSIX.)	
o	-F|--fixed-string	Interpret PATTERN as a list of fixed strings, separated by newlines, any of which is to be…	
o	-G|--basic-regexp	Interpret PATTERN as a basic regular expression (BRE, see below). This is the default	
o	-e|--regexp	Use PATTERN as the pattern. This can be used to specify multiple search patterns, or to protect a…	v
o	-i|--ignore-case|-y	Ignore case distinctions in both the PATTERN and the input files. (-i is specified by POSIX.)	
o	-v|--invert-match	Invert the sense of matching, to select non-matching lines. (-v is specified by POSIX.)	
o	-w|--word-regexp	Select only those lines containing matches that form whole words. The test is that the matching…	
o	-x|--line-regexp	Select only those matches that exactly match the whole line. (-x is specified by POSIX.)	
o	-c|--count	Suppress normal output; instead print a count of matching lines for each input file. With the -v…	
o	--color	Surround the matched (non-empty) strings, matching lines, context lines, file names, line numbers…	v
o	-L|--files-without-match	Suppress normal output; instead print the name of each input file from which no output would…	
o	-l|--files-with-matches	Suppress normal output; instead print the name of each input file from which output would normally…	
o	-m|--max-count	Stop reading a file after NUM matching lines. If the input is standard input from a regular file…	v
o	-o|--only-matching	Print only the matched (non-empty) parts of a matching line, with each such part on a separate…	
o	-q|--quiet|--silent	Quiet; do not write anything to standard output. Exit immediately with zero status if any match is…	
o	-s|--no-messages	Suppress error messages about nonexistent or unreadable files. Portability note: unlike GNU grep…	
o	-b|--byte-offset	Print the 0-based byte offset within the input file before each line of output. If -o…	
o	-H|--with-filename	Print the file name for each match. This is the default when there is more than one file to search	
o	-h|--no-filename	Suppress the prefixing of file names on output. This is the default when there is only one file…	
o	--label	Display input actually coming from standard input as input coming from file LABEL. This is…	v
o	-n|--line-number	Prefix each line of output with the 1-based line number within its input file. (-n is specified by…	
o	-T|--initial-tab	Make sure that the first character of actual line content lies on a tab stop, so that the…	
o	-u|--unix-byte-offsets	Report Unix-style byte offsets. This switch causes grep to report byte offsets as if the file were…	
o	--null	Output a zero byte (the ASCII NUL character) instead of the character that normally follows a file…	
o	-A|--after-context	Print num lines of trailing context after each match	v
o	-B|--before-context	Print num lines of leading context before each match. See also the -A and -C options	v
o	-C|--context	Print NUM lines of output context. Places a line containing a group separator (--) between…	v
o	-a|--text	Treat all files as ASCII text. Normally grep will simply print ``Binary file ... matches'' if…	
o	--binary-files	Controls searching and printing of binary files	v
o	-D|--devices	Specify the demanded action for devices, FIFOs and sockets	v
o	-d|--directories	Specify the demanded action for directories	v
o	--exclude	Note that --exclude patterns take priority over --include patterns, and if no --include pattern is…	V
o	--exclude-dir	If -R is specified, only directories matching the given filename pattern are searched. Note that…	V
o	-I	Ignore binary files. This option is equivalent to --binary-file=without-match option	
o	--include	If specified, only files matching the given filename pattern are searched. Note that --exclude…	V
o	--include-dir	If -R is specified, only directories matching the given filename pattern are searched. Note that…	V
o	-R|-r|--recursive	Recursively search subdirectories listed	
o	--line-buffered	Force output to be line buffered. By default, output is line buffered when standard output is a…	
o	-U|--binary	Search binary files, but do not attempt to print them	
o	-J|-bz2decompress	Decompress the bzip2(1) compressed file before looking for the text	
o	-V|--version	Print version number of grep to the standard output stream	
o	-P|--perl-regexp	Interpret pattern as a Perl regular expression	
o	-f|--file	Obtain patterns from FILE, one per line. The empty file contains zero patterns, and therefore…	v
a	2	0
=		--color
v	never	
v	always	
v	auto	
=		--binary-files
v	binary	Search binary files but do not print them
v	without-match	Do not search binary files
v	text	Treat all files as text
=		-D
v	read	Read as if they were normal files
v	skip	Devices will be silently skipped
=		-d
v	read	Directories are read in the same manner as normal files
v	skip	Silently ignore the directories
v	recurse	Read directories recursively
=		--exclude-dir
t	folders
=		--include-dir
t	folders
=		-f
t	filepaths
#		2
t	filepaths

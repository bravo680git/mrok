@	
o	-A|--after-context	Shows NUM lines after each match	v
o	--auto-hybrid-regex	When this flag is used, ripgrep will dynamically choose between supported regex engines depending…	
o	-B|--before-context	Shows NUM lines before each match	v
o	--binary	Enabling this flag will cause ripgrep to search binary files	
o	--block-buffered	When enabled, ripgrep will use block buffering	
o	-b|--byte-offset	Prints the 0-based byte offset within the input file before each line of output	
o	-s|--case-sensitive	Search case sensitively	
o	--color	Controls when to use colors	v
o	--colors	Specifies color settings for use in the output	v
o	--column	Shows column numbers for the first match on each line	
o	-C|--context	Shows NUM lines before and after each match	v
o	--context-separator	The string used to separate non-contiguous context lines in the output	v
o	-c|--count	Suppresses normal output and shows the number of lines that match the given pattersns for each…	
o	--count-matches	Suppresses normal output and shows the number of individual matches of the given patterns for each…	
o	--crlf	Treats CRLF as a line terminator instead of just a line break	
o	--debug	Shows debug messages	
o	--dfa-size-limit	The upper size limit of the regex DFA	v
o	-E|--encoding	Specifies the text encoding that ripgrep will use on all files searched	v
o	--engine	Specifies which regular expression engine to use	v
o	-f|--file	Searches for patterns from the given file, with one pattern per line	v
o	--files	Prints each file that would be searched without actually performing the search	
o	-l|--files-with-matches	Only prints the paths with at least one match	
o	--files-without-match	Only prints the paths that contains zero matches	
o	-F|--fixed-strings	Treats the pattern as a literal string instead of a regular expression	
o	-L|--follow	Follows symbolic links while traversing directories	
o	-g|--glob	Includes or excludes files and directories for searching that match the given glob	v
o	--glob-case-insensitive	Processes glob patterns given with the -g/--glob flag	
o	--heading	Prints the file path above clusters of matches from each file instead of printing the file path as…	
o	--hidden	Searches hidden files and directories	
o	--iglob	Includes or excludes files and directories for searching that match given the glob	v
o	--ignore-file	Specifies a path to one or more .gitignore format rules files	v
o	--ignore-file-case-insensitive	Process ignores files case insensitively	
o	--include-zero	Prints the number of matchesfor each file when used with --count or --count matches	
o	-v|--invert-match	Inverts matching	
o	--json	Enables printing results in a JSON Lines format	
o	--no-json	Disables the JSON Lines format	
o	--line-buffered	Enables line buffering	
o	-n|--line-number	Shows the line numbers (1-based)	
o	-x|--line-regexp	Only shows matches surrounded by line boundaries	
o	-M|--max-columns	Don't print lines longer than this limit in bytes	v
o	--max-columns-preview	Completely replaces any line that is too long with a message indicating that a matching line was…	
o	-m|--max-count	Limits the number of matching lines per file searched to NUM	v
o	--max-depth	Limits the depth of directory traversal to NUM levels beyond the paths given	v
o	--max-filesize	Ignores files larger than NUM in size	v
o	-mmap	Searches using memory maps when possible	
o	-U|--multiline	Enables matching across multiple lines	
o	--multiline-dotall	Enables dot all in your regex pattern	
o	--no-config	Never read configuration files	
o	-I|--no-filename	Never prints the file path with the matched lines	
o	--no-heading	Don't group matches by each file	
o	--no-ignore	Don't respect ignore files (.gitignore, .ignore, etc.)	
o	--no-ignore-dot	Don't respect .ignore files	
o	--no-ignore-excluded	Don't respect ignore files that are manually configured for the repository	
o	--no-ignore-files	Ignores any --ignore-file flags	
o	--no-ignore-global	Don't respect ignore files that come from `global` sources	
o	--no-ignore-messages	Suppresses all error messages related to parsing ignore files	
o	--no-ignore-parent	Don't repsect ignore files in parent directories	
o	--no-ignore-vcs	Don't respect version control ignore files	
o	-N|--no-line-number	Suppress line numbers	
o	--no-messages	Suppresses all error messages related to opening and reading files	
o	--no-map	Never use memory maps, even when they might be faster	
o	--no-pcre2-unicode		
o	--no-require-git	Will only respect global gitignore rules	
o	--no-unicode	Turn off unicode	
o	--unicode	Disables --no-unicode flag	
o	-0|--null	Whenever a file path is printed, follow it with a NUL byte	
o	--null-data	Uses NUL as a line terminator instead of the default line break	
o	--one-file-system	Will not cross file system boundaries relative to where the search started from	
o	--no-one-file-system	Disables `--one-file-system` flag	
o	-o|--only-matching	Prints only the matched (non-empty) parts of a matching line, with each such part on a separate…	
o	--passthru	Prints both matching and non-matching lines	
o	--path-separator	Sets the path separator to use when printing file paths	v
o	-P|--pcre2	Usess the PCRE2 regex engine instead of its default regex engine	
o	--pcre2-version	Prints the version of PCRE2 in use	
o	--pre	For each input File, search the standard output of the command	v
o	--pre-glob	Only files that match the given set of globs will be handed to the command specified by the `--pre…	v
o	-p|--pretty	Convenience alias for `--color always --heading --line-number`	
o	-q|--quiet	Do not print anything to stdout	
o	--regex-size-limit	Sets the upper size limit of the compiled regex	v
o	-e|--regexp	A pattern to search for	v
o	-r|--replace	Replace every match with the text given when printing results	v
o	-z|--search-zip	Search in compressed files	
o	-S|--smart-case	Searches case insensitively if the pattern is all lowercase	
o	--sort		v
o	--sortr	Enables sorting results in descending order	v
o	--stats	Prints aggregate statistics about this ripgrep search	
o	-a|--text	Searches binary files as if they were text	
o	-j|--threads	The approximate number of threads to use	v
o	--trim	All ASCII whitespace at the beginning of each line printed will be trimmed	
o	-t|--type	Only searches files matching TYPE	v
o	--type-add	Add a new glob for a particular file type	v
o	--type-clear	Clear the file type globs previously defined for type	v
o	--type-list	Shows all supported file types and their corresponding globs	
o	-T|--type-not	Do not search files matching type	v
o	-u|--unrestricted	Reduce the level of smart searching, increase by adding `u`s, ex: -uuu	
o	--vimgrep	Shows results with every match on its own line, including line numbers and column nnumbers	
o	-H|--with-filename	Displays the file path for matches	
o	-w|--word-regexp	Only shows the matches surrounded by word boundaries	
a	2	1
=		--color
v	never	Colors will never be used
v	auto	Ripgrep tries to be smart
v	always	Colors will always be used regardless of where output is sent
v	ansi	Colors will always be used, but emits ANSI escapes
=		--engine
v	default	
v	pcre2	
v	auto	
=		-f
t	filepaths
=		--iglob
t	filepaths,folders
=		--ignore-file
t	filepaths
=		--sort
v	none	Do not sort results. Fastest. Can be multi-threaded
v	path	Sort by file path, Always single-threaded
v	modified	Sort by the last modified time on a file. Always single-threaded
v	accessed	Sort by the last accessed time on a file. Always single-threaded
v	created	Sort by the creation time on a file. Always single-threaded
=		--sortr
v	none	Do not sort results. Fastest. Can be multi-threaded
v	path	Sort by file path, Always single-threaded
v	modified	Sort by the last modified time on a file. Always single-threaded
v	accessed	Sort by the last accessed time on a file. Always single-threaded
v	created	Sort by the creation time on a file. Always single-threaded
#		2
t	filepaths,folders

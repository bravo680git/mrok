@	
o	--avg-wage	Average salary value used for COCOMO calculations	v
o	--binary	Disable binary file detection	
o	--by-file	Display output for every file	
o	--ci	Enable CI output settings where stdout is ASCII	
o	--cocomo-project-type	Change the COCOMO model type (allows custom models, eg. "name,1,1,1,1")	v
o	--count-as	Count a file extension as a language (comma-separated key:value list, eg. jst:js,tpl:Markdown)	v
o	--debug	Enable debug output	
o	--exclude-dir	Directories to exclude	v
o	--file-gc-count	Number of files to parse before turning the GC on	v
o	-f|--format	Set output format	v
o	--format-multi	Multiple outputs with different formats (comma-separated key:value list, eg…	v
o	--gen	Identify generated files	
o	--generated-markers	Identify generated files by the presence of a string (comma-separated list)	v
o	-h|--help	Help for scc	
o	-i|--include-ext	Limit to these file extensions (comma-separated list)	v
o	--include-symlinks	Count symbolic links	
o	-l|--languages	Print supported languages and extensions	
o	--large-byte-count	Number of bytes a file can contain before being omitted	v
o	--large-line-count	Number of lines a file can contain before being omitted	v
o	--min	Identify minified files	
o	-z|--min-gen	Identify minified or generated files	
o	--min-gen-line-length	Number of bytes per average line for file to be considered minified or generated	v
o	--no-cocomo	Skip COCOMO calculation	
o	-c|--no-complexity	Skip code complexity calculation	
o	-d|--no-duplicates	Remove duplicate files from stats and output	
o	--no-gen	Ignore generated files in output (implies --gen)	
o	--no-gitignore	Disables .gitignore file logic	
o	--no-ignore	Disables .ignore file logic	
o	--no-large	Ignore files over certain byte and line size set by --max-line-count and --max-byte-count	
o	--no-min	Ignore minified files in output (implies --min)	
o	--no-min-gen	Ignore minified or generated files in output (implies --min-gen)	
o	--no-size	Remove size calculation output	
o	-M|--not-match	Ignore files and directories matching regular expression	v
o	-o|--output	Output filename (defaults to stdout if not provided)	v
o	--remap-all	Inspect every file and set its type by checking for a string (comma-separated key:value list, eg…	v
o	--remap-unknown	Inspect files of unknown type and set its type by checking for a string (comma-separated key:value…	v
o	--size-unit	Set the unit used for file size output	v
o	-s|--sort	Column to sort by	v
o	--sql-project	Use supplied name as the project identifier for the current run. Only valid with the '--format…	v
o	-t|--trace	Enable trace output (not recommended when processing multiple files)	
o	-v|--verbose	Verbose output	
o	--version	Version for scc	
o	-w|--wide	Wider output with additional statistics (implies --complexity)	
a	1	1
=		--cocomo-project-type
v	organic	
v	semi-detached	
v	embedded	
=		--count-as
d
=		--exclude-dir
t	folders
=		-f
v	tabular	
v	wide	
v	json	
v	csv	
v	csv-stream	
v	cloc-yaml	
v	html	
v	html-table	
v	sql	
v	sql-insert	
=		--format-multi
d
=		-i
d
=		-o
t	filepaths
=		--remap-all
d
=		--remap-unknown
d
=		--size-unit
v	si	1000^2 bytes
v	binary	1024^2 bytes
v	mixed	1,024,000 bytes (Binary kilobytes, SI megabytes)
v	xkcd-kb	1000 bytes during leap years, 1024 otherwise
v	xkcd-kelly	1012 bytes (a compromise between 1000 and 1024 bytes)
v	xkcd-imaginary	1024*sqrt(-1) bytes (used in quantum computing)
v	xkcd-intel	1023.937528 bytes (calculated on Pentium FPU)
v	xkcd-drive	Currently 856 bytes (shrinks by 4 each year for marketing reasons)
v	xkcd-bakers	1152 bytes (9 bits per byte, because you're such a good customer)
=		-s
v	files	
v	name	
v	lines	
v	blanks	
v	code	
v	comments	
v	complexity	
#		1
t	filepaths,folders

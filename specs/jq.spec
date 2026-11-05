@	
o	--version	Output the jq version and exit with zero	
o	--seq	Use the application/json-seq MIME type scheme for separating JSON texts in jq's input and output	
o	--stream	Parse the input in streaming fashion, outputting arrays of path and leaf values	
o	--slurp|-s	Instead of running the filter for each JSON object in the input, read the entire input stream into…	
o	--raw-input|-R	Don't parse the input as JSON. Instead, each line of text is passed to the filter as a string	
o	--null-input|-n	Don't read any input at all! Instead, the filter is run once using null as the input	
o	--compact-output|-c	By default, jq pretty-prints JSON output. Using this option will result in more compact output by…	
o	--tab	Use a tab for each indentation level instead of two spaces	
o	--indent	Use the given number of spaces for indentation	v
o	--color-output|-C	By default, jq outputs colored JSON if writing to a terminal. You can force it to produce color…	
o	--monochrome-output|-M	Disable color	
o	--ascii-output|-a	Jq usually outputs non-ASCII Unicode codepoints as UTF-8, even if the input specified them as…	
o	--unbuffered	Flush the output after each JSON object is printed	
o	--sort-keys|-S	Output the fields of each object with the keys in sorted orde	
o	--raw-output|-r	If the filter's result is a string then it will be written directly to standard output rather than…	
o	--join-output|-j	Like -r but jq won't print a newline after each output	
o	-f|--from-file	Read filter from the file rather than from a command line	v
o	-L	Prepend directory to the search list for modules	v
o	-e|--exit-status	Sets the exit status of jq to 0 if the last output values was neither false nor null, 1 if the…	
o	--arg	This option passes a value to the jq program as a predefined variable	v
o	--argjson	This option passes a JSON-encoded value to the jq program as a predefined variable	v
o	--slurpfile	This option reads all the JSON texts in the named file and binds an array of the parsed JSON…	v
o	--rawfile	This option reads in the named file and binds its contents to the given global variable	v
o	--args	Remaining arguments are positional string arguments. These are available to the jq program as…	
o	--jsonargs	Remaining arguments are positional JSON text arguments. These are available to the jq program as…	
o	--run-tests	Runs the tests in the given file or standard input. This must be the last option given and does…	V
a	2	1
=		-f
t	filepaths
=		-L
t	folders
=		--run-tests
t	filepaths
#		2
t	filepaths

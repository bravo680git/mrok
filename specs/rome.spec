@	
s	check	Run the linter on a set of files
s	ci	Run the linter and formatter check on a set of files
s	format	Run the formatter on a set of files
s	init	Bootstraps a new rome project
s	start	Start the Rome daemon server process
s	stop	Stop the Rome daemon server process
s	lsp-proxy	Acts as a server for the Language Server Protocol over stdin/stdout
s	rage	Prints information for debugging
s	version	Shows the Rome version information and quit
s	help	Prints help message
o	--colors	Set the formatting mode for markup	v
o	--use-server	Connect to a running instance of the Rome daemon server	
o	--version	Show the Rome version information and quit	
o	--files-max-size	The maximum allowed size for source code files in bytes	v
=		--colors
v	off	
v	force	
@	check
o	--apply	Apply safe fixes	
o	--apply-unsafe	Apply safe and unsafe fixes	
o	--max-diagnostics	Cap the amount of diagnostics displayed	v
o	--config-path	Set the filesystem path to the config dir of the rome.json file	v
o	--verbose	Print additional verbose advices on diagnostics	
a	1	1
=	check	--config-path
t	folders
#	check	1
t	filepaths,folders
@	ci
o	--formatter-enabled	Allow to enable or disable the formatter check	
o	--linter-enabled	Allow to enable or disable the linter check	
o	--organize-imports-enabled	Allow to enable or disable the organize imports	
o	--max-diagnostics	Cap the amount of diagnostics displayed	v
o	--config-path	Set the filesystem path to the config dir of the rome.json file	v
o	--verbose	Print additional verbose advices on diagnostics	
o	--indent-style	Change the indention character	v
o	--indent-size	How many spaces should be used for indentation	v
o	--line-width	How many characters the formatter is allowed to print in a single line	v
o	--quote-style	Changes the quotation character for strings	v
o	--quote-properties	Changes when properties in object should be quoted	v
o	--trailing-comma	Changes trailing commas in multi-line comma-separated syntactic structures	v
o	--semicolons	Changes when to print semicolons for statements	v
a	1	1
=	ci	--config-path
t	folders
=	ci	--indent-style
v	tabs	
v	space	
=	ci	--quote-style
v	single	
v	double	
=	ci	--quote-properties
v	as-needed	
v	preserve	
=	ci	--trailing-comma
v	all	
v	es5	
v	none	
=	ci	--semicolons
v	always	
v	as-needed	
#	ci	1
t	filepaths,folders
@	format
o	--write	Edit the files in place (beware!) instead of printing the diff to the console	
o	--skip-errors	Skip over files containing syntax errors instead of emitting an error diagnostic	
o	--max-diagnostics	Cap the amount of diagnostics displayed	v
o	--config-path	Set the filesystem path to the config dir of the rome.json file	v
o	--verbose	Print additional verbose advices on diagnostics	
o	--indent-style	Change the indention character	v
o	--indent-size	How many spaces should be used for indentation	v
o	--line-width	How many characters the formatter is allowed to print in a single line	v
o	--quote-style	Changes the quotation character for strings	v
o	--quote-properties	Changes when properties in object should be quoted	v
o	--trailing-comma	Changes trailing commas in multi-line comma-separated syntactic structures	v
o	--semicolons	Changes when to print semicolons for statements	v
o	--stdin-file-path	A file name with its extension to pass when reading from standard in	v
a	1	1
=	format	--config-path
t	folders
=	format	--indent-style
v	tabs	
v	space	
=	format	--quote-style
v	single	
v	double	
=	format	--quote-properties
v	as-needed	
v	preserve	
=	format	--trailing-comma
v	all	
v	es5	
v	none	
=	format	--semicolons
v	always	
v	as-needed	
#	format	1
t	filepaths,folders
@	init
@	start
@	stop
@	lsp-proxy
@	rage
@	version
@	help

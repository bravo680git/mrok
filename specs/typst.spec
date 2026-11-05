@	
s	compile|c	Compiles an input file into a supported output format
s	watch|w	Watches an input file and recompiles on changes
s	query	Processes an input file to extract provided metadata
s	fonts	Lists all discovered fonts in system and custom font paths
s	update	Self update the Typst CLI (disabled)
s	help	Print this message or the help of the given subcommand(s)
o	--cert	Path to a custom CA certificate to use when making network requests	v
o	-v|--verbosity	Sets the level of logging verbosity: -v = warning & error, -vv = info, -vvv = debug, -vvvv = trace	
o	-h|--help	Print help	
o	-V|--version	Print version	
=		--cert
t	filepaths
@	compile
o	--root	Configures the project root (for absolute paths)	v
o	--font-path	Adds additional directories to search for fonts	v
o	--diagnostic-format	The format to emit diagnostics in	v
o	-f|--format	The format of the output file, inferred from the extension by default	v
o	--open	Opens the output file using the default viewer after compilation	V
o	--ppi	The PPI (pixels per inch) to use for PNG export	v
o	--flamegraph	Produces a flamegraph of the compilation process	V
o	-h|--help	Print help	
a	2	0
=	compile	--root
t	folders
=	compile	--font-path
t	filepaths
=	compile	--diagnostic-format
v	human	
v	short	
=	compile	-f
v	pdf	
v	png	
v	svg	
=	compile	--flamegraph
t	filepaths
#	compile	1
d
#	compile	2
t	filepaths
@	watch
o	--root	Configures the project root (for absolute paths)	v
o	--font-path	Adds additional directories to search for fonts	v
o	--diagnostic-format	The format to emit diagnostics in	v
o	-f|--format	The format of the output file, inferred from the extension by default	v
o	--open	Opens the output file using the default viewer after compilation	V
o	--ppi	The PPI (pixels per inch) to use for PNG export	v
o	--flamegraph	Produces a flamegraph of the compilation process	V
o	-h|--help	Print help	
a	2	0
=	watch	--root
t	folders
=	watch	--font-path
t	filepaths
=	watch	--diagnostic-format
v	human	
v	short	
=	watch	-f
v	pdf	
v	png	
v	svg	
=	watch	--flamegraph
t	filepaths
#	watch	1
d
#	watch	2
t	filepaths
@	query
o	--root	Configures the project root (for absolute paths)	v
o	--font-path	Adds additional directories to search for fonts	v
o	--diagnostic-format	The format to emit diagnostics in	v
o	--field	Extracts just one field from all retrieved elements	v
o	--format	The format to serialize in	v
o	--one	Expects and retrieves exactly one element	
o	-h|--help	Print help	
a	2	0
=	query	--root
t	folders
=	query	--font-path
t	filepaths
=	query	--diagnostic-format
v	human	
v	short	
=	query	--format
v	json	
v	yaml	
#	query	1
d
@	fonts
o	--font-path	Adds additional directories to search for fonts	v
o	--variants	Also lists style variants of each font family	
o	-h|--help	Print help	
=	fonts	--font-path
t	filepaths
@	update
o	--force	Forces a downgrade to an older version (required for downgrading)	
o	--revert	Reverts to the version from before the last update (only possible if `typst update` has previously…	
o	-h|--help	Print help	
a	1	0
@	help
s	compile	Compiles an input file into a supported output format
s	watch	Watches an input file and recompiles on changes
s	query	Processes an input file to extract provided metadata
s	fonts	Lists all discovered fonts in system and custom font paths
s	update	Self update the Typst CLI (disabled)
s	help	Print this message or the help of the given subcommand(s)
@	help compile
@	help watch
@	help query
@	help fonts
@	help update
@	help help

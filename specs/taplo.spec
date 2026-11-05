@	
s	config|cfg	Operations with the Taplo config file
s	format|fmt	Format TOML documents
s	get	Extract a value from the given TOML document
s	help	Print help information for taplo
s	lint|check|validate	Lint a TOML documents
s	lsp	Language server operations
o	--help|-h	Print help information for taplo	
o	--version|-V	Print version information for taplo	
o	--verbose	Enable verbose logging format	
o	--colors		v
o	--log-spans	Enable logging spans	
=		--colors
v	auto	
v	always	
v	never	
@	config
s	default	Print the default `.taplo.toml` configuration file
s	help	Print this message or the help of the given subcommand(s)
s	schema	Print the JSON schema of the `.taplo.toml` configuration file
o	--help|-h	Print help information for config	
o	--log-spans	Enable logging spans	
o	--verbose	Enable verbose logging format	
o	--colors	Set color values for the output	v
=	config	--colors
v	auto	
v	always	
v	never	
@	config default
@	config help
a	1	0
#	config help	1
t	help
@	config schema
@	format
o	--config|-c	Path to the Taplo configuration file	v
o	--cache-path	Set a cache path	v
o	--check	Report any files that are not correctly formatted	V
o	--colors	Set color values for the output	v
o	--diff	Print the differences in patch formatting to `stdout`	
o	f|--force	Force formatting of files	V
o	--help|-h	Print help information for format	
o	--log-spans	Enable logging spans	
o	--no-auto-config	Do not search for a configuration file	
o	--option|-o	A formatter option given as a 'key=value', can be set multiple times	v
o	--stdin-filepath	A path to the file that the taplo will treat like stdin	v
o	--verbose	Enable verbose logging format	
a	1	1
=	format	--config
t	filepaths
=	format	--cache-path
t	filepaths
=	format	--check
t	filepaths
=	format	--colors
v	auto	
v	always	
v	never	
=	format	f
t	filepaths
=	format	--option
v	indent_tables=true	
v	indent_tables=false	
=	format	--stdin-filepath
t	filepaths
#	format	1
t	filepaths
@	get
o	--file-path|-f	Path to the TOML document	v
o	--colors	Set color values for the output	v
o	--help|-h	Print help information for get	
o	--log-spans	Enable logging spans	
o	-o|--output-format	The format specifying how the output is printed	v
o	--strip-newline|-s	Strip the trailing newline from the output	
o	--verbose	Enable verbose logging format	
=	get	--file-path
t	filepaths
=	get	--colors
v	auto	
v	always	
v	never	
=	get	-o
v	value	
v	json	
v	toml	
@	help
@	lint
o	--config|-c	Path to the Taplo configuration file	v
o	--cache-path	Set a cache path	v
o	--colors	Set color values for the output	v
o	--default-schema-catalogs	Use the default online catalogs for schemas	
o	--help|-h	Print help information for lint	
o	--log-spans	Enable logging spans	
o	--no-schema	Disable all schema validation	
o	--schema	URL to the schema to be used for validation	v
o	--schema-catalog	URL to the schema catalog to be used for validation	v
o	--verbose	Enable verbose logging format	
a	1	1
=	lint	--config
t	filepaths
=	lint	--cache-path
t	filepaths
=	lint	--colors
v	auto	
v	always	
v	never	
=	lint	--schema
t	history
=	lint	--schema-catalog
t	history
#	lint	1
t	filepaths
@	lsp
s	help	Print help information for lsp
s	stdio	Run the language server over the standard input and output
s	tcp	Run the language server and listen on a TCP address
o	--colors	Set color values for the output	v
o	--help|-h	Print help information for lsp	
o	--log-spans	Enable logging spans	
o	--verbose	Enable verbose logging format	
=	lsp	--colors
v	auto	
v	always	
v	never	
@	lsp help
@	lsp stdio
@	lsp tcp

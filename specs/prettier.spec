@	
o	-c|--check	Check if your files are formatted	v
o	-l|--list-different	Print the names of files that are different from Prettier's formatting	
o	-w|--write	Edit files in-place	
o	--arrow-parens	Include parentheses around a sole arrow function parameter	v
o	--no-bracket-spacing	Do not print spaces between brackets	
o	--embedded-language-formatting	Control how Prettier formats quoted code embedded in the file	v
o	--end-of-line	Which end of line characters to apply	v
o	--html-whitespace-sensitivity	How to handle whitespaces in HTML	v
o	--jsx-bracket-same-line	Put > on the last line instead of at a new line	
o	--jsx-single-quote	Use single quotes in JSX	
o	--parser	Which parser to use	v
o	--print-width	The line length where Prettier will try wrap	v
o	--prose-wrap	How to wrap prose	v
o	--quote-props	Change when properties in objects are quoted	v
o	--no-semi	Do not print semicolons, except at the beginning of lines which may need them	
o	--single-quote	Use single quotes instead of double quotes	
o	--tab-width	Number of spaces per indentation level	v
o	--trailing-comma	Print trailing commas wherever possible when multi-line	v
o	--use-tabs	Indent with tabs instead of spaces	
o	--vue-indent-script-and-style	Indent script and style tags in Vue files	
o	--config	Path to a Prettier configuration file (.prettierrc, package.json, prettier.config.js)	v
o	--no-config	Do not look for a configuration file	
o	--config-precedence	Define in which order config files and CLI options should be evaluated	v
o	--no-editorconfig	Don't take .editorconfig into account when parsing configuration	
o	--find-config-path	Finds a path to the configuration file for the given input file	v
o	--ignore-path	Path to a file with patterns describing files to ignore	v
o	--plugin	Add a plugin	v
o	--plugin-search-dir	Custom directory that contains prettier plugins in node_modules subdirectory	v
o	--with-node-modules	Process files inside 'node_modules' directory	
o	--cursor-offset	Print (to stderr) where a cursor at the given position would move to after formatting	v
o	--range-end	Format code ending at a given character offset (exclusive)	v
o	--range-start	Format code starting at a given character offset	v
o	--no-color	Do not colorize error messages	
o	--file-info	Extract the following info (as JSON) for a given file path	v
o	-h|--help	Show CLI usage, or details about the given flag	V
o	-u|--ignore-unknown	Ignore unknown files	
o	--insert-pragma	Insert @format pragma into file's first docblock comment	
o	--loglevel	What level of logs to report	v
o	--require-pragma	Require either '@prettier' or '@format' to be present in the file's first docblock comment in…	
o	--stdin-filepath	Path to the file to pretend that stdin comes from	v
o	--support-info	Print support information as JSON	
o	-v|--version	Print Prettier version	
o	--debug-check	This will cause Prettier to print an error message if it detects that code correctness might have…	
o	--no-error-on-unmatched-pattern	Prevent errors when pattern is unmatched	
a	1	1
=		-c
t	filepaths,folders
=		--arrow-parens
v	always	
v	avoid	
=		--embedded-language-formatting
v	auto	
v	off	
=		--end-of-line
v	lf	
v	crlf	
v	cr	
v	auto	
=		--html-whitespace-sensitivity
v	css	
v	strict	
v	ignore	
=		--parser
v	flow	
v	babel	
v	babel-flow	
v	babel-ts	
v	typescript	
v	espree	
v	meriyah	
v	css	
v	less	
v	scss	
v	json	
v	json5	
v	json-stringify	
v	graphql	
v	markdown	
v	mdx	
v	vue	
v	yaml	
v	html	
v	angular	
v	lwc	
=		--prose-wrap
v	always	
v	never	
v	preserve	
=		--quote-props
v	as-needed	
v	consistent	
v	preserve	
=		--trailing-comma
v	es5	
v	none	
v	all	
=		--config
t	filepaths
=		--config-precedence
v	cli-override	
v	file-override	
v	prefer-file	
=		--find-config-path
t	filepaths
=		--ignore-path
t	filepaths
=		--plugin
t	folders
=		--plugin-search-dir
t	folders
=		--file-info
t	filepaths
=		--loglevel
v	silent	
v	error	
v	warn	
v	log	
v	debug	
=		--stdin-filepath
t	filepaths
#		1
t	filepaths,folders

@	
o	--no-eslintrc	Disable use of configuration from .eslintrc.*	
o	-c|--config	Use this configuration, overriding .eslintrc.* config options if present	v
o	--env	Specify environments	v
o	--ext	Specify JavaScript file extensions	v
o	--global	Define global variables	v
o	--parser	Specify the parser to be used	v
o	--parser-options	Specify parser options	v
o	--resolve-plugins-relative-to	A folder where plugins should be resolved from	v
o	--rulesdir	Use additional rules from this directory	v
o	--plugin	Specify plugins	v
o	--rule	Specify rules	v
o	--fix	Automatically fix problems	
o	--fix-dry-run	Automatically fix problems without saving the changes to the file system	
o	--fix-type	Specify the types of fixes to apply	v
o	--ignore-path	Specify path of ignore file	v
o	--no-ignore	Disable use of ignore files and patterns	
o	--ignore-pattern	Pattern of files to ignore (in addition to those in .eslintignore)	v
o	--stdin	Lint code provided on <STDIN>	
o	--stdin-filename	Specify filename to process STDIN as	v
o	--quiet	Report errors only	
o	--max-warnings	Number of warnings to trigger nonzero exit code	v
o	-o|--output-file	Specify file to write report to	v
o	-f|--format	Use a specific output format	v
o	--color	Force enabling of color	
o	--no-color	Force disabling of color	
o	--no-inline-config	Prevent comments from changing config or rules	
o	--report-unused-disable-directives	Adds reported errors for unused eslint-disable-directives	
o	--cache	Only check changed files	
o	--cache-location	Path to the cache file or directory	v
o	--cache-strategy	Strategy to use for detecting changed files	v
o	--init	Run config initialization wizard	
o	--env-info	Output execution environment information	
o	--no-error-on-unmatched-pattern	Prevent errors when pattern is unmatched	
o	--debug	Output debugging information	
o	-h|--help	Show help	
o	-v|--version	Output the version number	
o	--print-config	Print the configuration for the give file	v
a	1	1
=		-c
t	filepaths
=		--env
d
=		--resolve-plugins-relative-to
t	folders
=		--rulesdir
t	folders
=		--plugin
d
=		--fix-type
v	problem	
v	suggestion	
v	layout	
=		--ignore-path
t	filepaths
=		--stdin-filename
t	filepaths
=		-o
t	filepaths
=		-f
v	checkstyle	
v	codeframe	
v	compact	
v	html	
v	jslint-xml	
v	json	
v	junit	
v	stylish	
v	table	
v	tap	
v	unix	
v	visualstudio	
=		--cache-location
t	filepaths,folders
=		--cache-strategy
v	metadata	
v	content	
=		--print-config
t	filepaths
#		1
t	filepaths,folders

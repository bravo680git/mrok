@	
s	init	Initialize Elm Review in this directory
s	suppress	Generate suppression files for rules that report many errors
s	new-package	Creates an new project aimed to contain rules and to be published later
s	new-rule	Adds a new rule to your review configuration or review package
o	--help|-h	Show help for elm-review	
o	--unsuppress	Include suppressed errors in the error report for all rules	
o	--rules	Run with a subsection of the rules in the configuration. Specify them by their name, and separate…	v
o	--watch	Re-run elm-review automatically when your project or configuration changes	
o	--watch-code	Re-run elm-review automatically when your project changes	
o	--elmjson	Specify the path to the elm.json file of the project	v
o	--config	Use the review configuration in the specified directory	v
o	--template	Use the review configuration from a GitHub repository	v
o	--compiler	Specify the path to the elm compiler	v
o	--version|-v	Print the version of the elm-review CLI	
o	--debug	Add helpful information to debug your configuration or rules	
o	--report	Error reports will be in JSON format	v
o	--no-details	Hide the details from error reports for a more compact view	
o	--ignore-dirs	Ignore the reports of all rules for the specified directories	v
o	--ignore-files	Ignore the reports of all rules for the specified files	v
o	--fix	Elm Review will present fixes for the errors that offer an automatic fix, which you can then…	
o	--fix-all	Elm Review will present a single fix containing the application of all available automatic fixes…	
o	--elm-format-path	Specify the path to elm-format	v
o	--fix-limit	Limit the number of fixes applied in a single batch to N	v
o	--extract	Enable extracting data from the project for the rules that have a data extractor. Requires running…	
o	--benchmark-info	Print out how much time it took for rules and phases of the process to run. This is meant for…	
o	--no-color	Disable colors in the output	
a	1	1
=		--elmjson
t	filepaths
=		--config
t	folders
=		--compiler
t	filepaths
=		--report
v	json	Prints a single JSON object
v	ndjson	Print one JSON object per error each on a new line
=		--ignore-dirs
t	folders
=		--ignore-files
t	filepaths
=		--elm-format-path
t	filepaths
#		1
t	filepaths,folders
@	init
o	--help|-h	Show help for elm-review init	
o	--config	Create the configuration files in the specified directory instead of in the review/ directory	v
o	--template	Copy the review configuration from a GitHub repository, at the root or in a folder	v
o	--compiler	Specify the path to the elm compiler	v
=	init	--config
t	folders
=	init	--compiler
t	filepaths
@	suppress
o	--help|-h	Show help for elm-review suppress	
o	--check-after-tests	Checks whether there are uncommitted suppression files	
o	--unsuppress	Include suppressed errors in the error report for all rules	
o	--unsuppress-rules	Include suppressed errors in the error report for all rules	v
@	new-package
o	--help|-h	Show help for elm-review new-package	
o	--compiler	Specify the path to the elm compiler	v
=	new-package	--compiler
t	filepaths
@	new-rule
o	--help|-h	Show help for elm-review new-package	
a	1	0

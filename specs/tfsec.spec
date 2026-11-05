@	
o	--concise-output	Reduce the amount of output and no statistics	
o	--config-file	Config file to use during run	v
o	--custom-check-dir	Explicitly the custom checks dir location	v
o	--debug	Enable debug logging (same as verbose)	
o	-G|--disable-grouping	Disable grouping of similar results	
o	-e|--exclude	Provide comma-separated list of rule IDs to exclude from run	v
o	--exclude-downloaded-modules	Remove results for downloaded modules in .terraform folder	
o	--exclude-path	Folder path to exclude, can be used multiple times and evaluated in order of specification	v
o	--filter-results	Filter results to return specific checks only (supports comma-delimited input)	v
o	--force-all-dirs	Don't search for tf files, include everything below provided directory	
o	-f|--format	Select output format: default, json, csv, checkstyle, junit, sarif. To use multiple formats…	v
o	-h|--help	Help for tfsec	
o	--ignore-hcl-errors	Stop and report an error if an HCL parse error is encountered	
o	--include-ignored	Include ignored checks in the result output	
o	--include-passed	Include passed checks in the result output	
o	--migrate-ignores	Migrate ignore codes to the new ID structure	
o	-m|--minimum-severity	The minimum severity to report. One of CRITICAL, HIGH, MEDIUM, LOW	v
o	--no-color	Disable colored output (American style!)	
o	--no-colour	Disable coloured output	
o	--no-ignores	Do not apply any ignore rules - normally ignored checks will fail	
o	--no-module-downloads	Do not download remote modules	
o	-O|--out	Set output file. This filename will have a format descriptor appended if multiple formats are…	v
o	--print-rego-input	Print a JSON representation of the input supplied to rego policies	
o	--rego-policy-dir	Directory to load rego policies from (recursively)	v
o	--run-statistics	View statistics table of current findings	
o	--single-thread	Run checks using a single thread	
o	-s|--soft-fail	Runs checks but suppresses error code	
o	--tfvars-file	Path to .tfvars file, can be used multiple times and evaluated in order of specification	v
o	--update	Update to latest version	
o	--verbose	Enable verbose logging (same as debug)	
o	-v|--version	Show version information and exit	
o	-W|--workspace	Specify a workspace for ignore limits (default "default")	v
a	1	0
=		--config-file
t	filepaths
=		--exclude-path
t	filepaths
=		-f
v	default	
v	json	
v	csv	
v	checkstyle	
v	junit	
v	sarif	
=		-m
v	CRITICAL	
v	HIGH	
v	MEDIUM	
v	LOW	
=		-O
t	filepaths
=		--tfvars-file
t	filepaths
=		-W
d
#		1
t	folders

@	
s	init	Configure project for Qodana
s	scan	Scan a project with Qodana
s	show	Show Qodana report
s	view	View SARIF files in CLI
o	-h|--help	Show help page for command	p
o	-v|--version	Version for Qodana	
@	init
o	-i|--project-dir	Root directory of the project to configure (default ".")	v
=	init	-i
t	folders
@	scan
o	-a|--analysis-id	Unique report identifier (GUID) to be used by Qodana Cloud	v
o	-b|--baseline	Provide the path to an existing SARIF report to be used in the baseline state calculation	v
o	--baseline-include-absent	Include in the output report the results from the baseline run that are absent in the current run	
o	--cache-dir	Override cache directory (default <userCacheDir>/JetBrains/<linter>/cache)	v
o	-c|--changes	Override the docker image to be used for the analysis	
o	--clear-cache	Clear the local Qodana cache before running the analysis	
o	--disable-sanity	Skip running the inspections configured by the sanity profile	
o	-e|--env	Define additional environment variables for the Qodana container (you can use the flag multiple…	v
o	--fail-threshold	Set the number of problems that will serve as a quality gate. If this number is reached, the…	v
o	-l|--linter	Override linter to use	v
o	--port	Port to serve the report on (default 8080)	v
o	--print-problems	Print all found problems by Qodana in the CLI output	
o	-n|--profile-name	Profile name defined in the project	v
o	-p|--profile-path	Path to the profile file	v
o	-i|--project-dir	Root directory of the inspected project (default ".")	v
o	--property	Set a JVM property to be used while running Qodana using the --property…	v
o	-o|--results-dir	Override directory to save Qodana inspection results to (default…	v
o	--run-promo	Set to 'true' to have the application run the inspections configured by the promo profile; set to…	v
o	-s|--save-report	Generate HTML report (default true)	
o	--script	Override the run scenario (default "default")	v
o	--send-report	Send the inspection report to Qodana Cloud, requires the '--token' option to be specified	
o	-w|--show-report	Serve HTML report on port	
o	--skip-pull	Skip pulling the latest Qodana container	
o	-d|--source-directory	Directory inside the project-dir directory must be inspected. If not specified, the whole project…	v
o	--stub-profile	Absolute path to the fallback profile file. This option is applied in case the profile was not…	v
o	-u|--user	User to run Qodana container as. Please specify user id – '$UID' or user id and group id $(id…	v
o	-v|--volume	Define additional volumes for the Qodana container (you can use the flag multiple times)	v
=	scan	-p
t	filepaths
=	scan	-i
t	folders
=	scan	--run-promo
v	true	
v	false	
@	show
o	-d|--dir-only	Open report directory only, don't serve it	
o	-p|--port	Specify port to serve report at (default 8080)	v
o	-i|--project-dir	Root directory of the inspected project (default ".")	v
o	-r|--report-dir	Specify HTML report path (the one with index.html inside) (default…	v
=	show	-i
t	folders
=	show	-r
t	folders
@	view
o	-f|--sarif-file	Path to the SARIF file (default "./qodana.sarif.json")	v
=	view	-f
t	filepaths

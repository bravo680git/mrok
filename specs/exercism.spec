@	
s	configure|c	Configure the command-line client
s	download|d	Download an exercise
s	help	Help about any command
s	open|o	Open an exercise on the website
s	prepare|p	Prepare does setup for Exercism and its tracks
s	submit|s	Submit your solution to an exercise
s	troubleshoot|t|debug	Troubleshoot does a diagnostic self-check
s	upgrade|u	Upgrade to the latest version of the CLI
s	version|v	Version outputs the version of CLI
s	workspace|w	Print out the path to your Exercism workspace
o	--help|-h	Help for this command	p
o	--timeout	Override the default HTTP timeout	vp
o	--unmask-token	Will unmask the API during a request/response dump	p
o	--verbose|-v	Verbose output	p
@	configure
o	-a|--api	API base url	v
o	--no-verify	Skip online token authorization check	
o	-s|--show	Show the current configuration	
o	-t|--token	Auth token used to connect to the site	v
o	-w|--workspace	Directory for exercism exercises	v
=	configure	-w
t	folders
@	download
o	-e|--exercise	The exercise slug	v
o	-T|--team	The team slug	v
o	-t|--track	The track ID	v
o	-u|--uuid	The solution UUID	v
@	help
@	open
a	1	0
#	open	1
t	folders
@	prepare
@	submit
a	1	1
#	submit	1
t	filepaths
@	troubleshoot
o	-f|--full-api-key	Display the user's full API key	
@	upgrade
@	version
@	workspace

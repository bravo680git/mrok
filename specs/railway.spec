@	
s	add	Add a plugin to your project
s	completion	Generate shell-completions
s	connect	Connect to a plugin
s	delete	Delete a project
s	docs	Open Railway Documentation in default browser
s	down	Remove the most recent deployment
s	environment	Change your environment
s	help	Get help about any command
s	init	Create a new railway project
s	link	Connect to an existing railway project
s	list	List all railway projects
s	login	Login to railway
s	logout	Logout of railway
s	logs	Show logs for the most-recent deployment
s	open	Open the project
s	run	Run a local command using variables from the active environment
s	shell	Open a subshell with Railway variables available
s	status	View the status of railway project
s	unlink	Disconnects the current directory from a Railway project
s	up	Deploy to railway
s	variables	Work with environment variables
s	version	Get the version of railway's CLI
s	whoami	Get the logged in user
o	--help|-h	Show help for railway	
o	--version|-V	Show railway version	
o	--verbose|-v	Enable verbose output	
@	add
@	completion
a	1	0
#	completion	1
v	bash	
v	zsh	
v	fish	
v	powershell	
@	connect
a	1	0
#	connect	1
v	postgresql	
v	mysql	
v	redis	
v	mongodb	
@	delete
a	1	0
@	docs
@	down
o	-e|--environment	Environment to delete from	v
@	environment
a	1	0
#	environment	1
v	production	
v	preview	
@	help
a	1	0
@	init
@	link
a	1	0
@	list
@	login
o	--browserless	Login without opening a browser	
@	logout
@	logs
o	-n|--lines	Output a specific number of lines	v
@	open
s	live	Open the live project
s	metrics	Open project metrics
s	settings	Open project settings
@	open live
@	open metrics
@	open settings
@	run
o	-e|--environment	Environment to run in	v
o	-s|--service	Define specific service	v
@	shell
o	-s|--service	Deploy app to specific service	v
@	status
@	unlink
@	up
o	-d|--detach	Detach from build logs	
o	-e|--environment	Environment to run in	
o	-s|--service	Deploy app to specific service	v
a	1	0
#	up	1
t	folders
@	variables
s	delete	Delete variable
s	get	Get variable value
s	set	Set variable value
o	-e|--environment	Environment	
o	-s|--service	Deploy app to specific service	v
@	variables delete
a	1	0
@	variables get
a	1	0
@	variables set
a	2	0
@	version
@	whoami

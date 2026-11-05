@	
s	app	Commands to create and link Encore apps
s	auth	Commands to authenticate with Encore
s	check	Checks your application for compile-time errors using Encore's compiler
s	daemon	Starts the encore daemon
s	db	Database management commands
s	eject	Eject provides ways to eject your application to migrate away from using Encore
s	gen	Code generation commands
s	logs	Streams logs from your application
s	run	Runs your application
s	secret	Secret management commands
s	test	Tests your application
s	version	Reports the current version of the encore application
s	vpn	VPN management commands
s	help	Help about any command
o	--verbose|-v	Verbose output	vp
o	--help|-h	Display help	p
@	app
s	clone	Clone an Encore app to your computer
s	create	Create a new Encore app
s	link	Link an Encore app with the server
@	app clone
@	app create
o	--example	URL to example code to use	v
@	app link
o	--force|-f	Force link even if the app is already linked	
@	auth
s	login	Log in to Encore
s	logout	Logs out the currently logged in user
s	signup	Create a new Encore account
s	whoami	Show the current logged in user
@	auth login
o	--auth-key|-k	Auth Key to use for login	v
@	auth logout
@	auth signup
@	auth whoami
@	check
o	--codegen-debug	Dump generated code (for debugging Encore's code generation)	
@	daemon
s	env	Prints Encore environment information
o	--foreground|-f	Start the daemon in the foreground	
@	daemon env
@	db
s	conn-uri	Outputs the database connection string
s	proxy	Sets up a proxy tunnel to the database
s	reset	Resets the databases for the given services. Use --all to reset all databases
s	shell	Connects to the database via psql shell
@	db conn-uri
o	--env|-e	Environment name to connect to (such as "prod")	v
@	db proxy
o	--env|-e	Environment name to connect to (such as "prod")	v
o	--port|-p	Port to listen on (defaults to a random port)	v
@	db reset
o	--all	Reset all services in the application	
@	db shell
o	--env|-e	Environment name to connect to (such as "prod")	v
@	eject
s	docker	Docker builds a portable docker image of your Encore application
@	eject docker
o	--base	Base image to build from	v
o	--push|-p	Push image to remote repository	
@	gen
s	client	Generates an API client for your app
s	wrappers	Generates user-facing wrapper code
@	gen client
o	--env|-e	The environment to fetch the API for (defaults to the primary environment)	v
o	--lang|-l	The language to generate code for ("typescript" and "go" are supported)	v
o	--output|-o	The filename to write the generated client code to	v
=	gen client	--output
t	filepaths
@	gen wrappers
@	logs
o	--env|-e	Environment name to stream logs from (defaults to the production environment)	v
o	--json	Whether to print logs in raw JSON format	
@	run
o	--debug	Compile for debugging (disables some optimizations)	
o	--listen	Address to listen on (for example "0.0.0.0:4000")	v
o	--port|-p	Port to listen on	v
o	--tunnel	Create a tunnel to your machine for others to test against	
o	--watch|-w	Watch for changes and live-reload	
@	secret
s	set	Sets a secret value
@	secret set
o	--dev|-d	To set the secret for development use	
o	--prod|-p	To set the secret for production use	
@	test
@	version
s	update	Checks for an update of encore and, if one is available, runs the appropriate command to update it
@	version update
@	vpn
s	start	Sets up a secure connection to private environments
s	status	Determines the status of the VPN connection
s	stop	Stops the VPN connection
@	vpn start
@	vpn status
@	vpn stop
@	help
s	app	Commands to create and link Encore apps
s	auth	Commands to authenticate with Encore
s	check	Checks your application for compile-time errors using Encore's compiler
s	daemon	Starts the encore daemon
s	db	Database management commands
s	eject	Eject provides ways to eject your application to migrate away from using Encore
s	gen	Code generation commands
s	logs	Streams logs from your application
s	run	Runs your application
s	secret	Secret management commands
s	test	Tests your application
s	version	Reports the current version of the encore application
s	vpn	VPN management commands
@	help app
s	clone	Clone an Encore app to your computer
s	create	Create a new Encore app
s	link	Link an Encore app with the server
@	help app clone
@	help app create
@	help app link
@	help auth
s	login	Log in to Encore
s	logout	Logs out the currently logged in user
s	signup	Create a new Encore account
s	whoami	Show the current logged in user
@	help auth login
@	help auth logout
@	help auth signup
@	help auth whoami
@	help check
@	help daemon
s	env	Prints Encore environment information
@	help daemon env
@	help db
s	conn-uri	Outputs the database connection string
s	proxy	Sets up a proxy tunnel to the database
s	reset	Resets the databases for the given services. Use --all to reset all databases
s	shell	Connects to the database via psql shell
@	help db conn-uri
@	help db proxy
@	help db reset
@	help db shell
@	help eject
s	docker	Docker builds a portable docker image of your Encore application
@	help eject docker
@	help gen
s	client	Generates an API client for your app
s	wrappers	Generates user-facing wrapper code
@	help gen client
@	help gen wrappers
@	help logs
@	help run
@	help secret
s	set	Sets a secret value
@	help secret set
@	help test
@	help version
s	update	Checks for an update of encore and, if one is available, runs the appropriate command to update it
@	help version update
@	help vpn
s	start	Sets up a secure connection to private environments
s	status	Determines the status of the VPN connection
s	stop	Stops the VPN connection
@	help vpn start
@	help vpn status
@	help vpn stop

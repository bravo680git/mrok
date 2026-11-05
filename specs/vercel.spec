@	
s	deploy	Performs a deployment (default)
s	dev	Start a local development server
s	env	Manages the Environment Variables for your current Project
s	init	Initialize an example project
s	list	Lists deployments
s	ls	Lists deployments
s	inspect	Displays information related to a deployment
s	login	Logs into your account or creates a new one
s	logout	Logs out of your account
s	switch	Switches between teams and your personal account
s	help	Displays complete help for [cmd]
s	rm	Removes a deployment
s	remove	Removes a deployment
s	domains	Manages your domain names
s	dns	Manages your DNS records
s	certs	Manages your SSL certificates
s	secrets	Manages your global Secrets, for use in Environment Variables
s	logs	Displays the logs for a deployment
s	teams	Manages your teams
s	whoami	Shows the username of the currently logged in user
s	alias	Apply custom domains based on git branches, or other heuristics
s	link	Links your local directory to a Project
s	billing	Manage payment methods
o	-h|--help	Output usage information	
o	-v|--version	Output the version number	
o	-V|--platform-version	Set the platform version to deploy to	
o	-A|--local-config	Path to the local 'vercel.json' file	v
o	-Q|--global-config	Path to the global '.vercel' directory	v
o	-d|--debug	Provides more verbose output	
o	-f|--force	Force a new deployment even if nothing has changed	
o	-with-cache	Retain build cache when using --force	
o	-t|--token	Execute command with an auth token	v
o	-p|--public	Deployment is public ('/_src' is exposed)	
o	-e|--env	Include an env var during run time (e.g.: '-e KEY=value'). Can appear many times	
o	-b|--build-env	Similar to `--env` but for build time only	
o	-m|--meta	Add metadata for the deployment (e.g.: `-m KEY=value`). Can appear many times	
o	-C|--no-clipboard	Do not attempt to copy URL to clipboard	
o	-S|--scope	Set a custom scope	v
o	--regions	Set default regions to enable the deployment on	
o	--prod	Create a production deployment	
o	-c|--confirm	Confirm default options and skip questions	
a	1	0
=		-A
t	filepaths
=		-Q
t	folders
#		1
t	folders
@	deploy
a	1	0
#	deploy	1
t	folders
@	dev
o	--listen	Specifies which port to run on	
@	env
s	add	Add an environment variable
s	rm	Remove an environment variable
s	pull	Download dev env variables from cloud and write to .env
s	ls	List environment variables for a specific environment
@	env add
a	2	0
#	env add	2
v	production	
v	preview	
v	development	
@	env rm
a	2	0
#	env rm	2
v	production	
v	preview	
v	development	
@	env pull
a	1	0
#	env pull	1
t	filepaths
@	env ls
a	1	0
@	init
a	2	0
@	list
o	-m|--meta	Filters results based on project metadata	v
a	1	0
@	ls
a	1	0
@	inspect
a	1	0
@	login
@	logout
@	switch
a	1	0
@	help
a	1	0
@	rm
o	-s|--safe	Skip removal of deployments with an active preview URL or production domain	
o	-y|--yes	Skip confirmation step for a deployment or project removal	
a	1	0
@	remove
a	1	0
@	domains
s	ls	List all domains under an account
s	inspect	Retrieves information about a domain
s	add	Add a domain to an account
s	rm	Removes a domain from an account
s	buy	Buy a domain for an account
s	move	Removes a domain from an account
s	transfer-in	Transfers in a domain to an account
s	verify	Verifies a domain for an account
@	domains ls
@	domains inspect
a	1	0
@	domains add
a	1	0
@	domains rm
a	1	0
@	domains buy
a	1	0
@	domains move
a	2	0
@	domains transfer-in
a	1	0
@	domains verify
a	1	0
@	dns
s	add	Add DNS record for a domain
@	dns add
a	4	0
#	dns add	3
v	A	A record
v	AAAA	AAAA record
v	ALIAS	ALIAS record
v	CNAME	CName record
v	TXT	TXT record
@	certs
s	ls	List all certificates under an account
s	issue	Issue certificates for multiple domains
s	rm	Remove a certificate by id
o	--challenge-only	Show challenges needed to issue a certificate	
o	--crt	Include path to .crt	v
o	--key	Include path to .key	v
o	--ca	Include path to .ca	v
=	certs	--crt
t	filepaths
=	certs	--key
t	filepaths
=	certs	--ca
t	filepaths
@	certs ls
@	certs issue
a	1	1
@	certs rm
a	1	0
@	secrets
s	list	List all secrets
s	add	Add a new secret
s	rename	Rename a secret
s	remove	Remove a secret
@	secrets list
@	secrets add
a	2	0
@	secrets rename
a	2	0
@	secrets remove
a	1	0
@	logs
o	-a|--all	Receive access logs in addition to regular logs	
o	-f|--follow	Watch for additional logs output	
o	-n|--number	Specify number of log lines to output	v
o	-o|--output	Specifies format of logs output as 'short' or 'raw'	v
o	--since	Return logs after a specific ISO 8601 date	v
o	-q|--query	Return logs against a search query	v
o	--until	Return logs up to a specific ISO 8601 date	v
a	1	0
@	teams
s	list	List all teams under an account
s	add	Create a new team
s	invite	Invite a new member to the team
@	teams list
@	teams add
@	teams invite
a	1	0
@	whoami
@	alias
s	set	Assign a custom domain to a deployment
s	rm	Remove a custom domain from a deployment
s	ls	List custom domains that were assigned to deployments
@	alias set
a	2	0
@	alias rm
a	1	0
@	alias ls
@	link
a	1	0
#	link	1
t	folders
@	billing
s	ls	List all the payment methods of the active account
s	add	Interactively add a new credit card
s	rm	Remove a credit card by ID
s	set-default	Select which credit card should be default
@	billing ls
@	billing add
@	billing rm
a	1	0
@	billing set-default
a	1	0

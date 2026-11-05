@	
s	accounts|account	Manage Meroxa Accounts
s	api	Invoke Meroxa API
s	app|apps	Manage Turbine Data Applications
s	auth	Authentication commands for Meroxa
s	billing	Open your billing page in a web browser
s	build|builds	Inspect Process Builds on Meroxa
s	completion	Generate completion script
s	cfg|config	Manage your Meroxa CLI configuration
s	env|environment|environments	Manage environments on Meroxa
s	login	Login or Sign up to the Meroxa Platform
s	logout	Clears local login credentials of the Meroxa Platform
s	open	Open in a web browser
s	resource|resources	Manage resources on Meroxa
s	transform|transforms	Manage transforms on Meroxa
s	version	Display the Meroxa CLI version
s	whoami	Display the current logged in user
s	help	Help about any command
o	--cli-config-file	Meroxa configuration file	vp
o	--debug	Display any debugging information	p
o	--json	Output json	p
o	--timeout	Set the duration of the client timeout in seconds	vp
o	--help|-h	Display help	p
=		--cli-config-file
t	filepaths
@	accounts
s	ls|list	List Meroxa Accounts
s	set	Set active account
@	accounts ls
o	--no-headers	Display output without headers	
@	accounts set
@	api
@	app
s	deploy	Deploy a Turbine Data Application
s	describe	Describe a Turbine Data Application
s	init	Initialize a Turbine Data Application
s	ls|list	List Turbine Data Applications
s	log|logs	View relevant logs to the state of the given Turbine Data Application
s	open	Open the link to a Turbine Data Application in the Dashboard
s	rm|delete|remove	Remove a Turbine Data Application
s	run	Execute a Turbine Data Application locally
s	upgrade	Upgrade a Turbine Data Application
@	app deploy
o	--env	Environment (name or UUID) where application will be deployed to	v
o	--path	Path to the app directory (default is local directory)	v
o	--skip-collection-validation	Skips unique destination collection and looping validations	
=	app deploy	--path
t	folders
@	app describe
o	--path	Path to the app directory (default is local directory)	v
=	app describe	--path
t	folders
@	app init
o	--lang|-l	Language to use (js|go|py) (required)	v
o	--mod-vendor	Whether to download modules to vendor or globally while initializing a Go application	
o	--path	Path where application will be initialized (current directory as default)	v
o	--skip-mod-init	Whether to run 'go mod init' while initializing a Go application	
=	app init	--lang
v	js	
v	go	
v	py	
=	app init	--path
t	folders
@	app ls
o	--no-headers	Display output without headers	
@	app log
o	--path	Path to the app directory (default is local directory)	v
=	app log	--path
t	folders
@	app open
o	--path	Path to the app directory (default is local directory)	v
=	app open	--path
t	folders
@	app rm
o	--force|-f	Skip confirmation	
o	--path	Path to the app directory (default is local directory)	v
=	app rm	--path
t	folders
@	app run
o	--path	Path of application to run	v
=	app run	--path
t	folders
@	app upgrade
o	--path	Path where application exists (current directory as default)	v
=	app upgrade	--path
t	folders
@	auth
s	login	Login or Sign up to the Meroxa Platform
s	logout	Clears local login credentials of the Meroxa Platform
s	whoami	Display the current logged in user
@	auth login
@	auth logout
@	auth whoami
@	billing
@	build
s	describe	Describe a Meroxa Process Build
s	log|logs	List a Meroxa Process Build's Logs
@	build describe
@	build log
@	completion
@	cfg
s	describe	Show Meroxa CLI configuration details
s	set	Update your Meroxa CLI configuration file with a specific key=value
@	cfg describe
@	cfg set
@	env
s	create	Create an environment
s	describe	Describe environment
s	ls|list	List environments
s	rm|delete|remove	Remove environment
s	repair	Repair environment
s	update	Update an environment
@	env create
o	--config|-c	Environment configuration based on type and provider (e.g.: --config…	v
o	--provider	Environment cloud provider to use	v
o	--region	Environment region	v
o	--type	Environment type, when not specified	v
o	--yes|-y	Skip confirmation prompt	
@	env describe
@	env ls
o	--no-headers	Display output without headers	
@	env rm
o	--force|-f	Skip confirmation	
@	env repair
@	env update
o	--config|-c	Updated environment configuration based on type and provider (e.g.: --config…	v
o	--name	Updated environment name, when specified	v
o	--yes|-y	Skip confirmation prompt	
@	login
@	logout
@	open
s	billing	Open your billing page in a web browser
@	open billing
@	resource
s	add|create	Add a resource to your Meroxa resource catalog
s	describe	Describe resource
s	ls|list	List resources and resource types
s	rm|delete|remove	Remove resource
s	rotate-tunnel-key	Rotate the tunnel key for a resource
s	update	Update a resource
s	validate	Validate a resource
@	resource add
o	--ca-cert	Trusted certificates for verifying resource	v
o	--client-cert	Client certificate for authenticating to the resource	v
o	--client-key	Client private key for authenticating to the resource	v
o	--env	Environment (name or UUID) where resource will be created	v
o	--metadata|-m	Resource metadata	v
o	--password	Password	v
o	--private-key-file	Path to private key file	v
o	--ssh-private-key	SSH tunneling private key	v
o	--ssh-url	SSH tunneling address	v
o	--ssl	Use SSL	
o	--token	API Token	v
o	--type	Resource type (required)	v
o	--url|-u	Resource url	v
o	--username	Username	v
@	resource describe
@	resource ls
o	--no-headers	Display output without headers	
o	--types	List resource types	
@	resource rm
o	--force|-f	Skip confirmation	
@	resource rotate-tunnel-key
o	--force|-f	Skip confirmation	
@	resource update
o	--ca-cert	Trusted certificates for verifying resource	v
o	--client-cert	Client certificate for authenticating to the resource	v
o	--client-key	Client private key for authenticating to the resource	v
o	--metadata|-m	New resource metadata	v
o	--name	New resource name	v
o	--password	Password	v
o	--ssh-url	SSH tunneling address	v
o	--ssl	Use SSL	
o	--url|-u	New resource url	v
o	--username	Username	v
@	resource validate
@	transform
s	ls|list	List transforms
@	transform ls
o	--no-headers	Display output without headers	
@	version
@	whoami
@	help
s	accounts|account	Manage Meroxa Accounts
s	api	Invoke Meroxa API
s	app|apps	Manage Turbine Data Applications
s	auth	Authentication commands for Meroxa
s	billing	Open your billing page in a web browser
s	build|builds	Inspect Process Builds on Meroxa
s	completion	Generate completion script
s	cfg|config	Manage your Meroxa CLI configuration
s	env|environment|environments	Manage environments on Meroxa
s	login	Login or Sign up to the Meroxa Platform
s	logout	Clears local login credentials of the Meroxa Platform
s	open	Open in a web browser
s	resource|resources	Manage resources on Meroxa
s	transform|transforms	Manage transforms on Meroxa
s	version	Display the Meroxa CLI version
s	whoami	Display the current logged in user
@	help accounts
s	ls|list	List Meroxa Accounts
s	set	Set active account
@	help accounts ls
@	help accounts set
@	help api
@	help app
s	deploy	Deploy a Turbine Data Application
s	describe	Describe a Turbine Data Application
s	init	Initialize a Turbine Data Application
s	ls|list	List Turbine Data Applications
s	log|logs	View relevant logs to the state of the given Turbine Data Application
s	open	Open the link to a Turbine Data Application in the Dashboard
s	rm|delete|remove	Remove a Turbine Data Application
s	run	Execute a Turbine Data Application locally
s	upgrade	Upgrade a Turbine Data Application
@	help app deploy
@	help app describe
@	help app init
@	help app ls
@	help app log
@	help app open
@	help app rm
@	help app run
@	help app upgrade
@	help auth
s	login	Login or Sign up to the Meroxa Platform
s	logout	Clears local login credentials of the Meroxa Platform
s	whoami	Display the current logged in user
@	help auth login
@	help auth logout
@	help auth whoami
@	help billing
@	help build
s	describe	Describe a Meroxa Process Build
s	log|logs	List a Meroxa Process Build's Logs
@	help build describe
@	help build log
@	help completion
@	help cfg
s	describe	Show Meroxa CLI configuration details
s	set	Update your Meroxa CLI configuration file with a specific key=value
@	help cfg describe
@	help cfg set
@	help env
s	create	Create an environment
s	describe	Describe environment
s	ls|list	List environments
s	rm|delete|remove	Remove environment
s	repair	Repair environment
s	update	Update an environment
@	help env create
@	help env describe
@	help env ls
@	help env rm
@	help env repair
@	help env update
@	help login
@	help logout
@	help open
s	billing	Open your billing page in a web browser
@	help open billing
@	help resource
s	add|create	Add a resource to your Meroxa resource catalog
s	describe	Describe resource
s	ls|list	List resources and resource types
s	rm|delete|remove	Remove resource
s	rotate-tunnel-key	Rotate the tunnel key for a resource
s	update	Update a resource
s	validate	Validate a resource
@	help resource add
@	help resource describe
@	help resource ls
@	help resource rm
@	help resource rotate-tunnel-key
@	help resource update
@	help resource validate
@	help transform
s	ls|list	List transforms
@	help transform ls
@	help version
@	help whoami

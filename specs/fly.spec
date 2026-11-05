@	
s	agent	Commands that manage the Fly agent, a background process that manages flyctl wireguard connections
s	apps	Manage apps
s	auth	Manage authentication
s	autoscale	Autoscaling app resources
s	builds	Manage application builds
s	certs	Manage certificates
s	checks	Manage health checks
s	completion	Generate the autocompletion script for the specified shell
s	config	Manage an app's configuration
s	create	Create a new application
s	curl	Run a performance test against a URL
s	dash|dashboard	Open web browser on Fly Web UI for this app
s	deploy	Deploy Fly applications
s	destroy	Permanently destroys an app
s	dig	Make DNS requests against Fly.io's internal DNS server
s	dns-records	Manage DNS records
s	docs	View Fly documentation
s	doctor	The DOCTOR command allows you to debug your Fly environment
s	domains	Manage domains
s	history	List an app's change history
s	img|image	Manage app image
s	info	Show detailed app information
s	ips	Manage IP addresses for apps
s	launch	Launch a new app
s	logs	View app logs
s	machines|m|machine	Commands that manage machines
s	monitor	Monitor currently running application deployments
s	move	Move an app to another organization
s	open	Open browser to current deployed application
s	orgs	Commands for managing Fly organizations
s	ping	Test connectivity with ICMP ping messages
s	platform	Fly platform information
s	pg|postgres	Manage postgres clusters
s	proxy	Proxies connections to a fly VM
s	regions	Manage regions
s	releases	List app releases
s	resume	Resume an application
s	scale	Scale app resources
s	secrets	Manage app secrets
s	ssh	Commands that manage SSH credentials
s	status	Show app status
s	suspend	Suspend an application
s	turboku	Launches heroku apps
s	version	Show version information for the flyctl command
s	vm	Commands that manage VM instances
s	vol|volumes	Volume management commands
s	wg|wireguard	Commands that manage WireGuard peer connections
s	help	Help about any command
o	--access-token|-t	Fly API Access Token	vp
o	--json|-j	Json output	p
o	--verbose	Verbose output	p
o	--help|-h	Display help	p
@	agent
s	ping	Ping the Fly agent
s	restart	Restart the Fly agent
s	daemon-start|run	Run the Fly agent in the foreground
s	start	Start the Fly agent
s	stop	Stop the Fly agent
@	agent ping
@	agent restart
@	agent daemon-start
@	agent start
@	agent stop
@	apps
s	create	Create a new application
s	destroy	Permanently destroys an app
s	list	List applications
s	move	Move an app to another organization
s	open	Open browser to current deployed application
s	releases	List app releases
s	restart	Restart an application
@	apps create
o	--generate-name	Generate a name for the app	
o	--name	The app name to use	v
o	--network	Specify custom network id	v
o	--org|-o	The organization to operate on	v
=	apps create	--org
d
@	apps destroy
o	--yes|-y	Accept all confirmations	
@	apps list
@	apps move
o	--org|-o	The organization to operate on	v
o	--yes|-y	Accept all confirmations	
=	apps move	--org
d
@	apps open
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	apps open	--app
d
=	apps open	--config
t	filepaths
@	apps releases
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--image	Display the Docker image reference of the release	
=	apps releases	--app
d
=	apps releases	--config
t	filepaths
@	apps restart
o	-f|--force	Will issue a restart against each Machine even if there are errors. ( Machines only )	
o	--skip-health-checks	Restarts app without waiting for health checks. ( Machines only )	
a	1	0
#	apps restart	1
d
@	auth
s	docker	Authenticate docker
s	login	Log in a user
s	logout	Logs out the currently logged in user
s	signup	Create a new fly account
s	token	Show the current auth token
s	whoami	Displays the users email address/service identity currently authenticated and in use
@	auth docker
@	auth login
o	--email	Login email	v
o	--interactive|-i	Log in with an email and password interactively	
o	--otp	One time password	v
o	--password	Login password	v
@	auth logout
@	auth signup
@	auth token
@	auth whoami
@	autoscale
s	balanced	Configure a traffic balanced app with params (min=int max=int)
s	disable	Disable autoscaling
s	set	Set current models autoscaling parameters
s	show	Show current autoscaling configuration
s	standard	Configure a standard balanced app with params (min=int max=int)
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	autoscale	--app
d
=	autoscale	--config
t	filepaths
@	autoscale balanced
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	autoscale balanced	--app
d
=	autoscale balanced	--config
t	filepaths
@	autoscale disable
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	autoscale disable	--app
d
=	autoscale disable	--config
t	filepaths
@	autoscale set
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	autoscale set	--app
d
=	autoscale set	--config
t	filepaths
@	autoscale show
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	autoscale show	--app
d
=	autoscale show	--config
t	filepaths
@	autoscale standard
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	autoscale standard	--app
d
=	autoscale standard	--config
t	filepaths
@	builds
s	list	List builds
@	builds list
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	builds list	--app
d
=	builds list	--config
t	filepaths
@	certs
s	create|add	Add a certificate for an app
s	check	Checks DNS configuration
s	list	List certificates for an app
s	delete|remove	Removes a certificate from an app
s	show	Shows certificate information
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	certs	--app
d
=	certs	--config
t	filepaths
@	certs create
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	certs create	--app
d
=	certs create	--config
t	filepaths
@	certs check
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	certs check	--app
d
=	certs check	--config
t	filepaths
@	certs list
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	certs list	--app
d
=	certs list	--config
t	filepaths
@	certs delete
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--yes|-y	Accept all confirmations	
=	certs delete	--app
d
=	certs delete	--config
t	filepaths
@	certs show
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	certs show	--app
d
=	certs show	--config
t	filepaths
@	checks
s	handlers	Manage health check handlers
s	list	List app health checks
@	checks handlers
s	create	Create a health check handler
s	delete	Delete a health check handler
s	list	List health check handlers
@	checks handlers create
o	--organization|-o	The organization to add the handler to	v
o	--type	The type of handler to create, can be slack or pagerduty	v
@	checks handlers delete
@	checks handlers list
@	checks list
o	--app|-a	App name to operate on	v
o	--check-name	Filter checks by name	v
o	--config|-c	Path to an app config file or directory containing one	v
=	checks list	--app
d
=	checks list	--config
t	filepaths
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	config
s	display	Display an app's configuration
s	env	Display an app's runtime environment variables
s	save	Save an app's config file
s	validate	Validate an app's config file
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	config	--app
d
=	config	--config
t	filepaths
@	config display
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	config display	--app
d
=	config display	--config
t	filepaths
@	config env
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	config env	--app
d
=	config env	--config
t	filepaths
@	config save
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	config save	--app
d
=	config save	--config
t	filepaths
@	config validate
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	config validate	--app
d
=	config validate	--config
t	filepaths
@	create
o	--generate-name	Generate a name for the app	
o	--name	The app name to use	v
o	--network	Specify custom network id	v
o	--org|-o	The organization to operate on	v
=	create	--org
d
@	curl
@	dash
s	metrics	Open web browser on Fly Web UI for this app's metrics
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	dash	--app
d
=	dash	--config
t	filepaths
@	dash metrics
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	dash metrics	--app
d
=	dash metrics	--config
t	filepaths
@	deploy
o	--app|-a	Application name	v
o	--build-arg	Set of build time variables in the form of NAME=VALUE pairs. Can be specified multiple times	v
o	--build-only	Build but do not deploy	
o	--build-target	Set the target build stage to build if the Dockerfile has more than one stage	v
o	--config|-c	Path to application configuration file	v
o	--detach	Return immediately instead of monitoring deployment progress	
o	--dockerfile	Path to a Dockerfile. Defaults to the Dockerfile in the working directory	v
o	--env|-e	Set of environment variables in the form of NAME=VALUE pairs. Can be specified multiple times	v
o	--image|-i	The image tag or ID to deploy	v
o	--image-label	Image label to use when tagging and pushing to the fly registry. Defaults to…	v
o	--local-only	Only perform builds locally using the local docker daemon	
o	--nix	Build with Nix	
o	--no-cache	Do not use the build cache when building the image	
o	--now	Deploy now without confirmation	
o	--push	Push image to registry after build is complete	
o	--region|-r	The region to operate on	v
o	--remote-only	Perform builds on a remote builder instance instead of using the local docker daemon	
o	--strategy	The strategy for replacing running instances. Options are canary, rolling, bluegreen, or…	v
=	deploy	--app
d
=	deploy	--config
t	filepaths
@	destroy
o	--yes|-y	Accept all confirmations	
@	dig
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--org|-o	The organization to operate on	v
o	--short|-s	Just print the answers, not DNS record details	
=	dig	--app
d
=	dig	--config
t	filepaths
=	dig	--org
d
@	dns-records
s	export	Export DNS records
s	import	Import DNS records
s	list	List DNS records
@	dns-records export
o	--overwrite		
@	dns-records import
@	dns-records list
@	docs
@	doctor
s	diag	Send diagnostic information about your applications back to Fly.io
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	doctor	--app
d
=	doctor	--config
t	filepaths
@	doctor diag
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--force	Send diagnostics even if we can't find your local Fly.io app	
=	doctor diag	--app
d
=	doctor diag	--config
t	filepaths
@	domains
s	add	Add a domain
s	list	List domains
s	register	Register a domain
s	show	Show domain
@	domains add
@	domains list
@	domains register
@	domains show
@	history
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	history	--app
d
=	history	--config
t	filepaths
@	img
s	show	Show image details
s	update	Updates the app's image to the latest available version. (Fly Postgres only)
@	img show
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	img show	--app
d
=	img show	--config
t	filepaths
@	img update
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--detach	Return immediately instead of monitoring update progress	
o	--yes|-y	Accept all confirmations	
=	img update	--app
d
=	img update	--config
t	filepaths
@	info
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--host	Returns just the hostname	
o	--name|-n	Returns just the appname	
=	info	--app
d
=	info	--config
t	filepaths
@	ips
s	allocate-v4	Allocate an IPv4 address
s	allocate-v6	Allocate an IPv6 address
s	list	List allocated IP addresses
s	private	List instances private IP addresses
s	release	Release an IP address
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	ips	--app
d
=	ips	--config
t	filepaths
@	ips allocate-v4
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--region	The region where the address should be allocated	v
=	ips allocate-v4	--app
d
=	ips allocate-v4	--config
t	filepaths
@	ips allocate-v6
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--region	The region where the address should be allocated	v
=	ips allocate-v6	--app
d
=	ips allocate-v6	--config
t	filepaths
@	ips list
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	ips list	--app
d
=	ips list	--config
t	filepaths
@	ips private
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	ips private	--app
d
=	ips private	--config
t	filepaths
@	ips release
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	ips release	--app
d
=	ips release	--config
t	filepaths
@	launch
o	--copy-config	Use the configuration file if present without prompting	
o	--dockerfile	Path to a Dockerfile. Defaults to the Dockerfile in the working directory	v
o	--generate-name	Always generate a name for the app	
o	--image	The image to launch	v
o	--name	The name of the new app	v
o	--no-deploy	Do not prompt for deployment	
o	--now	Deploy now without confirmation	
o	--org	The organization that will own the app	v
o	--path	Path to app code and where a fly.toml file will be saved	v
o	--region	The region to launch the new app in	v
o	--remote-only	Perform builds remotely without using the local docker daemon	
=	launch	--org
d
@	logs
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--instance|-i	Filter by instance ID	v
o	--region|-r	The region to operate on	v
=	logs	--app
d
=	logs	--config
t	filepaths
@	machines
s	clone	Clones a Fly Machine
s	kill	Kill (SIGKILL) a Fly machine
s	list	List Fly machines
s	rm|remove	Remove a Fly machine
s	run	Run a machine
s	start	Start a Fly machine
s	status	Show current status of a running machine
s	stop	Stop a Fly machine
@	machines clone
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--detach|-d	Detach from the machine's logs	
o	--name|-n	The name of the new machine	v
o	--org|-o	The organization to operate on	v
o	--region|-r	The region to operate on	v
=	machines clone	--app
d
=	machines clone	--config
t	filepaths
=	machines clone	--org
d
@	machines kill
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	machines kill	--app
d
=	machines kill	--config
t	filepaths
@	machines list
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--quiet|-q	Only list machine ids	
=	machines list	--app
d
=	machines list	--config
t	filepaths
@	machines rm
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--force|-f	Force kill machine if it's running	
=	machines rm	--app
d
=	machines rm	--config
t	filepaths
@	machines run
o	--app|-a	Application name	v
o	--build-arg	Set of build time variables in the form of NAME=VALUE pairs. Can be specified multiple times	v
o	--build-local-only	Only perform builds locally using the local docker daemon	
o	--build-only		
o	--build-remote-only	Perform builds remotely without using the local docker daemon	
o	--build-target	Set the target build stage to build if the Dockerfile has more than one stage	v
o	--config|-c	Path to application configuration file	v
o	--cpu-kind	Kind of CPU to use (shared, dedicated)	v
o	--cpus	Number of CPUs	v
o	--detach|-d	Detach from the machine's logs	
o	--dockerfile	Path to a Dockerfile. Defaults to the Dockerfile in the working directory	v
o	--entrypoint	ENTRYPOINT replacement	v
o	--env|-e	Set of environment variables in the form of NAME=VALUE pairs. Can be specified multiple times	v
o	--id	Machine ID, if previously known	v
o	--image-label	Image label to use when tagging and pushing to the fly registry. Defaults to…	v
o	--memory	Memory (in megabytes) to attribute to the machine	v
o	--name|-n	Machine name, will be generated if missing	v
o	--no-build-cache	Do not use the cache when building the image	
o	--org	The organization that will own the app	v
o	--port|-p	Exposed port mappings (format: edgePort[:machinePort]/[protocol[:handler]])	v
o	--region|-r	The region to operate on	v
o	--size|-s	Preset guest cpu and memory for a machine	v
o	--volume|-v	Volumes to mount in the form of <volume_id_or_name>:/path/inside/machine[:<options>]	v
=	machines run	--app
d
=	machines run	--config
t	filepaths
=	machines run	--org
d
@	machines start
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	machines start	--app
d
=	machines start	--config
t	filepaths
@	machines status
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	machines status	--app
d
=	machines status	--config
t	filepaths
@	machines stop
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--signal|-s	Signal to stop the machine with (default: SIGINT)	v
o	--time	Seconds to wait before killing the machine	v
=	machines stop	--app
d
=	machines stop	--config
t	filepaths
@	monitor
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	monitor	--app
d
=	monitor	--config
t	filepaths
@	move
o	--org|-o	The organization to operate on	v
o	--yes|-y	Accept all confirmations	
=	move	--org
d
@	open
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	open	--app
d
=	open	--config
t	filepaths
@	orgs
s	builder	Manage remote builder
s	create	Create an organization
s	delete	Delete an organization
s	invite	Invite user (by email) to organization
s	list	Lists organizations for current user
s	remove	Remove a user from an organization
s	show	Show information about an organization
@	orgs builder
s	show	Show details about an organization's remote builder image
s	update	Update an organization's remote builder image
@	orgs builder show
@	orgs builder update
@	orgs create
@	orgs delete
o	--yes|-y	Accept all confirmations	
@	orgs invite
@	orgs list
@	orgs remove
@	orgs show
@	ping
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--count|-n	Number of probes to send (0=indefinite)	v
o	--interval|-i	Interval between ping probes	v
o	--org|-o	The organization to operate on	v
o	--size|-s	Size of probe to send (not including headers)	v
=	ping	--app
d
=	ping	--config
t	filepaths
=	ping	--org
d
@	platform
s	regions	List regions
s	status	Show current platform status
s	vm-sizes	List VM Sizes
@	platform regions
@	platform status
@	platform vm-sizes
@	pg
s	attach	Attach a postgres cluster to an app
s	connect	Connect to the Postgres console
s	create	Create a postgres cluster
s	db	Manage databases in a cluster
s	detach	Detach a postgres cluster from an app
s	list	List postgres clusters
s	users	Manage users in a cluster
@	pg attach
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--database-name	Database to use, defaults to a new database with the same name as the app	v
o	--database-user	The database user to create, defaults to creating a user with the same name as the consuming app	v
o	--postgres-app	The postgres cluster to attach to the app	v
o	--variable-name	The env variable name that will be added to the app. Defaults to DATABASE_URL	v
=	pg attach	--app
d
=	pg attach	--config
t	filepaths
@	pg connect
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--database	The postgres database to connect to	v
o	--password	The postgres user password	v
o	--user	The postgres user to connect with	v
=	pg connect	--app
d
=	pg connect	--config
t	filepaths
@	pg create
o	--initial-cluster-size	The size of the initial postgres cluster	v
o	--name	The name of the new app	v
o	--organization	The organization that will own the app	v
o	--password	The superuser password. one will be generated for you if you leave this blank	v
o	--region	The region to launch the new app in	v
o	--snapshot-id	Creates the volume with the contents of the snapshot	v
o	--vm-size	The size of the VM	v
o	--volume-size	The size in GB for volumes	v
@	pg db
s	list	List databases in a cluster
@	pg db list
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	pg db list	--app
d
=	pg db list	--config
t	filepaths
@	pg detach
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--postgres-app	The postgres cluster to detach from the app	v
=	pg detach	--app
d
=	pg detach	--config
t	filepaths
@	pg list
@	pg users
s	list	List users in a cluster
@	pg users list
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	pg users list	--app
d
=	pg users list	--config
t	filepaths
@	proxy
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--org|-o	The organization to operate on	v
o	--select|-s	Prompt to select from available instances from the current application	
=	proxy	--app
d
=	proxy	--config
t	filepaths
=	proxy	--org
d
@	regions
s	add	Allow the app to run in the provided regions
s	backup	Sets the backup region pool with provided regions
s	list	Shows the list of regions the app is allowed to run in
s	remove	Prevent the app from running in the provided regions
s	set	Sets the region pool with provided regions
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	regions	--app
d
=	regions	--config
t	filepaths
@	regions add
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--group	The process group to add the region to	v
=	regions add	--app
d
=	regions add	--config
t	filepaths
@	regions backup
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	regions backup	--app
d
=	regions backup	--config
t	filepaths
@	regions list
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	regions list	--app
d
=	regions list	--config
t	filepaths
@	regions remove
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--group	The process group to remove the region from	v
=	regions remove	--app
d
=	regions remove	--config
t	filepaths
@	regions set
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--group	The process group to set regions for	v
=	regions set	--app
d
=	regions set	--config
t	filepaths
@	releases
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--image	Display the Docker image reference of the release	
=	releases	--app
d
=	releases	--config
t	filepaths
@	resume
@	scale
s	count	Change an app's VM count to the given value
s	memory	Set VM memory
s	show	Show current resources
s	vm	Change an app's VM to a named size (eg. shared-cpu-1x, dedicated-cpu-1x, dedicated-cpu-2x...)
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	scale	--app
d
=	scale	--config
t	filepaths
@	scale count
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--max-per-region	Max number of VMs per region	v
=	scale count	--app
d
=	scale count	--config
t	filepaths
@	scale memory
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--group	The process group to apply the memory size to	v
=	scale memory	--app
d
=	scale memory	--config
t	filepaths
@	scale show
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	scale show	--app
d
=	scale show	--config
t	filepaths
@	scale vm
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--group	The process group to apply the VM size to	v
o	--memory	Memory in MB for the VM	v
=	scale vm	--app
d
=	scale vm	--config
t	filepaths
@	secrets
s	import	Read secrets in name=value from stdin
s	list	Lists the secrets available to the app
s	set	Set one or more encrypted secrets for an app
s	unset	Remove encrypted secrets from an app
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	secrets	--app
d
=	secrets	--config
t	filepaths
@	secrets import
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--detach	Return immediately instead of monitoring deployment progress	
=	secrets import	--app
d
=	secrets import	--config
t	filepaths
@	secrets list
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	secrets list	--app
d
=	secrets list	--config
t	filepaths
@	secrets set
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--detach	Return immediately instead of monitoring deployment progress	
=	secrets set	--app
d
=	secrets set	--config
t	filepaths
@	secrets unset
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--detach	Return immediately instead of monitoring deployment progress	
=	secrets unset	--app
d
=	secrets unset	--config
t	filepaths
@	ssh
s	console	Connect to a running instance of the current app
s	establish	Create a root SSH certificate for your organization
s	issue	Issue a new SSH credential
s	log	Log of all issued certs
@	ssh console
o	--app|-a	App name to operate on	v
o	--command|-C	Command to run on SSH session	v
o	--config|-c	Path to an app config file or directory containing one	v
o	--probe|-p	Test WireGuard connection after establishing	
o	--region|-r	Region to create WireGuard connection in	v
o	--select|-s	Select available instances	
=	ssh console	--app
d
=	ssh console	--config
t	filepaths
@	ssh establish
@	ssh issue
o	--agent	Add key to SSH agent	
o	--dotssh|-d	Store keys in ~/.ssh, like normal keys	
o	--hours	Expiration, in hours (<72)	v
o	--overwrite|-o	Overwrite existing SSH keys in same location, if we generated them	
o	--username|-u	Unix username for SSH cert	v
@	ssh log
@	status
s	instance	Show instance status
o	--all	Show completed instances	
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--deployment	Always show deployment status	
o	--rate	Refresh Rate for --watch	v
o	--watch	Refresh details	
=	status	--app
d
=	status	--config
t	filepaths
@	status instance
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	status instance	--app
d
=	status instance	--config
t	filepaths
@	suspend
@	turboku
o	--heroku-token	Heroku API token	v
o	--keep	Keep the app directory after deployment	
o	--name	The name of the new app	v
o	--now	Deploy now without confirmation	
o	--org	The organization that will own the app	v
o	--region	The region to launch the new app in	v
=	turboku	--org
d
@	version
s	update	Checks for available updates and automatically updates
o	--saveinstall|-s	Save parameter in config	v
@	version update
@	vm
s	restart	Restart a VM
s	status	Show a VM's status
s	stop	Stop a VM
@	vm restart
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	vm restart	--app
d
=	vm restart	--config
t	filepaths
@	vm status
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	vm status	--app
d
=	vm status	--config
t	filepaths
@	vm stop
o	--app|-a	App name to operate on	v
o	--config|-c	Path to an app config file or directory containing one	v
=	vm stop	--app
d
=	vm stop	--config
t	filepaths
@	vol
s	create	Create new volume for app
s	delete	Delete a volume from the app
s	list	List the volumes for app
s	show	Show details of an app's volume
s	snaps|snapshots	Manage volume snapshots
@	vol create
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
o	--no-encryption	Do not encrypt the volume contents	
o	--region|-r	The region to operate on	v
o	--require-unique-zone	Require volume to be placed in separate hardware zone from existing volumes	
o	--size|-s	Size of volume in gigabytes	v
=	vol create	--app
d
=	vol create	--config
t	filepaths
@	vol delete
o	--yes|-y	Accept all confirmations	
@	vol list
o	--app|-a	Application name	v
o	--config|-c	Path to application configuration file	v
=	vol list	--app
d
=	vol list	--config
t	filepaths
@	vol show
@	vol snaps
s	list	List snapshots
@	vol snaps list
@	wg
s	create	Add a WireGuard peer connection
s	list	List all WireGuard peer connections
s	remove	Remove a WireGuard peer connection
s	reset	Reset WireGuard peer connection for an organization
s	status	Get status a WireGuard peer connection
s	token	Commands that managed WireGuard delegated access tokens
s	websockets	Enable or disable WireGuard tunneling over WebSockets
@	wg create
@	wg list
@	wg remove
@	wg reset
@	wg status
@	wg token
s	create	Create a new WireGuard token
s	delete	Delete a WireGuard token; token is name:<name> or token:<token>
s	list	List all WireGuard tokens
s	start	Start a new WireGuard peer connection associated with a token (set FLY_WIREGUARD_TOKEN)
s	update	Rekey a WireGuard peer connection associated with a token (set FLY_WIREGUARD_TOKEN)
@	wg token create
@	wg token delete
@	wg token list
@	wg token start
@	wg token update
@	wg websockets
@	help
s	Use	Short
s	agent	Commands that manage the Fly agent, a background process that manages flyctl wireguard connections
s	apps	Manage apps
s	auth	Manage authentication
s	autoscale	Autoscaling app resources
s	builds	Manage application builds
s	certs	Manage certificates
s	checks	Manage health checks
s	completion	Generate the autocompletion script for the specified shell
s	config	Manage an app's configuration
s	create	Create a new application
s	curl	Run a performance test against a URL
s	dash|dashboard	Open web browser on Fly Web UI for this app
s	deploy	Deploy Fly applications
s	destroy	Permanently destroys an app
s	dig	Make DNS requests against Fly.io's internal DNS server
s	dns-records	Manage DNS records
s	docs	View Fly documentation
s	doctor	The DOCTOR command allows you to debug your Fly environment
s	domains	Manage domains
s	history	List an app's change history
s	img|image	Manage app image
s	info	Show detailed app information
s	ips	Manage IP addresses for apps
s	launch	Launch a new app
s	ls|list	Lists your Fly resources
s	logs	View app logs
s	machines|m|machine	Commands that manage machines
s	monitor	Monitor currently running application deployments
s	move	Move an app to another organization
s	open	Open browser to current deployed application
s	orgs	Commands for managing Fly organizations
s	ping	Test connectivity with ICMP ping messages
s	platform	Fly platform information
s	pg|postgres	Manage postgres clusters
s	proxy	Proxies connections to a fly VM
s	regions	Manage regions
s	releases	List app releases
s	restart	Restart an application
s	resume	Resume an application
s	scale	Scale app resources
s	secrets	Manage app secrets
s	ssh	Commands that manage SSH credentials
s	status	Show app status
s	suspend	Suspend an application
s	turboku	Launches heroku apps
s	version	Show version information for the flyctl command
s	vm	Commands that manage VM instances
s	vol|volumes	Volume management commands
s	wg|wireguard	Commands that manage WireGuard peer connections
@	help Use
@	help agent
s	ping	Ping the Fly agent
s	restart	Restart the Fly agent
s	daemon-start|run	Run the Fly agent in the foreground
s	start	Start the Fly agent
s	stop	Stop the Fly agent
@	help agent ping
@	help agent restart
@	help agent daemon-start
@	help agent start
@	help agent stop
@	help apps
s	create	Create a new application
s	destroy	Permanently destroys an app
s	list	List applications
s	move	Move an app to another organization
s	open	Open browser to current deployed application
s	releases	List app releases
s	restart	Restart an application
@	help apps create
@	help apps destroy
@	help apps list
@	help apps move
@	help apps open
@	help apps releases
@	help apps restart
@	help auth
s	docker	Authenticate docker
s	login	Log in a user
s	logout	Logs out the currently logged in user
s	signup	Create a new fly account
s	token	Show the current auth token
s	whoami	Displays the users email address/service identity currently authenticated and in use
@	help auth docker
@	help auth login
@	help auth logout
@	help auth signup
@	help auth token
@	help auth whoami
@	help autoscale
s	balanced	Configure a traffic balanced app with params (min=int max=int)
s	disable	Disable autoscaling
s	set	Set current models autoscaling parameters
s	show	Show current autoscaling configuration
s	standard	Configure a standard balanced app with params (min=int max=int)
@	help autoscale balanced
@	help autoscale disable
@	help autoscale set
@	help autoscale show
@	help autoscale standard
@	help builds
s	list	List builds
@	help builds list
@	help certs
s	create|add	Add a certificate for an app
s	check	Checks DNS configuration
s	list	List certificates for an app
s	delete|remove	Removes a certificate from an app
s	show	Shows certificate information
@	help certs create
@	help certs check
@	help certs list
@	help certs delete
@	help certs show
@	help checks
s	handlers	Manage health check handlers
s	list	List app health checks
@	help checks handlers
s	create	Create a health check handler
s	delete	Delete a health check handler
s	list	List health check handlers
@	help checks handlers create
@	help checks handlers delete
@	help checks handlers list
@	help checks list
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help config
s	display	Display an app's configuration
s	env	Display an app's runtime environment variables
s	save	Save an app's config file
s	validate	Validate an app's config file
@	help config display
@	help config env
@	help config save
@	help config validate
@	help create
@	help curl
@	help dash
s	metrics	Open web browser on Fly Web UI for this app's metrics
@	help dash metrics
@	help deploy
@	help destroy
@	help dig
@	help dns-records
s	export	Export DNS records
s	import	Import DNS records
s	list	List DNS records
@	help dns-records export
@	help dns-records import
@	help dns-records list
@	help docs
@	help doctor
s	diag	Send diagnostic information about your applications back to Fly.io
@	help doctor diag
@	help domains
s	add	Add a domain
s	list	List domains
s	register	Register a domain
s	show	Show domain
@	help domains add
@	help domains list
@	help domains register
@	help domains show
@	help history
@	help img
s	show	Show image details
s	update	Updates the app's image to the latest available version. (Fly Postgres only)
@	help img show
@	help img update
@	help info
@	help ips
s	allocate-v4	Allocate an IPv4 address
s	allocate-v6	Allocate an IPv6 address
s	list	List allocated IP addresses
s	private	List instances private IP addresses
s	release	Release an IP address
@	help ips allocate-v4
@	help ips allocate-v6
@	help ips list
@	help ips private
@	help ips release
@	help launch
@	help ls
s	apps	Lists all your apps
s	orgs	List all your organizations
@	help ls apps
@	help ls orgs
@	help logs
@	help machines
s	clone	Clones a Fly Machine
s	kill	Kill (SIGKILL) a Fly machine
s	list	List Fly machines
s	rm|remove	Remove a Fly machine
s	run	Run a machine
s	start	Start a Fly machine
s	status	Show current status of a running machine
s	stop	Stop a Fly machine
@	help machines clone
@	help machines kill
@	help machines list
@	help machines rm
@	help machines run
@	help machines start
@	help machines status
@	help machines stop
@	help monitor
@	help move
@	help open
@	help orgs
s	builder	Manage remote builder
s	create	Create an organization
s	delete	Delete an organization
s	invite	Invite user (by email) to organization
s	list	Lists organizations for current user
s	remove	Remove a user from an organization
s	show	Show information about an organization
@	help orgs builder
s	show	Show details about an organization's remote builder image
s	update	Update an organization's remote builder image
@	help orgs builder show
@	help orgs builder update
@	help orgs create
@	help orgs delete
@	help orgs invite
@	help orgs list
@	help orgs remove
@	help orgs show
@	help ping
@	help platform
s	regions	List regions
s	status	Show current platform status
s	vm-sizes	List VM Sizes
@	help platform regions
@	help platform status
@	help platform vm-sizes
@	help pg
s	attach	Attach a postgres cluster to an app
s	connect	Connect to the Postgres console
s	create	Create a postgres cluster
s	db	Manage databases in a cluster
s	detach	Detach a postgres cluster from an app
s	list	List postgres clusters
s	users	Manage users in a cluster
@	help pg attach
@	help pg connect
@	help pg create
@	help pg db
s	list	List databases in a cluster
@	help pg db list
@	help pg detach
@	help pg list
@	help pg users
s	list	List users in a cluster
@	help pg users list
@	help proxy
@	help regions
s	add	Allow the app to run in the provided regions
s	backup	Sets the backup region pool with provided regions
s	list	Shows the list of regions the app is allowed to run in
s	remove	Prevent the app from running in the provided regions
s	set	Sets the region pool with provided regions
@	help regions add
@	help regions backup
@	help regions list
@	help regions remove
@	help regions set
@	help releases
@	help restart
@	help resume
@	help scale
s	count	Change an app's VM count to the given value
s	memory	Set VM memory
s	show	Show current resources
s	vm	Change an app's VM to a named size (eg. shared-cpu-1x, dedicated-cpu-1x, dedicated-cpu-2x...)
@	help scale count
@	help scale memory
@	help scale show
@	help scale vm
@	help secrets
s	import	Read secrets in name=value from stdin
s	list	Lists the secrets available to the app
s	set	Set one or more encrypted secrets for an app
s	unset	Remove encrypted secrets from an app
@	help secrets import
@	help secrets list
@	help secrets set
@	help secrets unset
@	help ssh
s	console	Connect to a running instance of the current app
s	establish	Create a root SSH certificate for your organization
s	issue	Issue a new SSH credential
s	log	Log of all issued certs
@	help ssh console
@	help ssh establish
@	help ssh issue
@	help ssh log
@	help status
s	instance	Show instance status
@	help status instance
@	help suspend
@	help turboku
@	help version
s	update	Checks for available updates and automatically updates
@	help version update
@	help vm
s	restart	Restart a VM
s	status	Show a VM's status
s	stop	Stop a VM
@	help vm restart
@	help vm status
@	help vm stop
@	help vol
s	create	Create new volume for app
s	delete	Delete a volume from the app
s	list	List the volumes for app
s	show	Show details of an app's volume
s	snaps|snapshots	Manage volume snapshots
@	help vol create
@	help vol delete
@	help vol list
@	help vol show
@	help vol snaps
s	list	List snapshots
@	help vol snaps list
@	help wg
s	create	Add a WireGuard peer connection
s	list	List all WireGuard peer connections
s	remove	Remove a WireGuard peer connection
s	reset	Reset WireGuard peer connection for an organization
s	status	Get status a WireGuard peer connection
s	token	Commands that managed WireGuard delegated access tokens
s	websockets	Enable or disable WireGuard tunneling over WebSockets
@	help wg create
@	help wg list
@	help wg remove
@	help wg reset
@	help wg status
@	help wg token
s	create	Create a new WireGuard token
s	delete	Delete a WireGuard token; token is name:<name> or token:<token>
s	list	List all WireGuard tokens
s	start	Start a new WireGuard peer connection associated with a token (set FLY_WIREGUARD_TOKEN)
s	update	Rekey a WireGuard peer connection associated with a token (set FLY_WIREGUARD_TOKEN)
@	help wg token create
@	help wg token delete
@	help wg token list
@	help wg token start
@	help wg token update
@	help wg websockets

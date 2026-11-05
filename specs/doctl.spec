@	
s	completion	Configure your terminal's shell so that doctl commands autocomplete when you press the TAB key
s	help	Display help about commands
s	1-click	The commands under `doctl 1-click` are for interacting with DigitalOcean 1-Click applications
s	account	The subcommands of `doctl account` retrieve information about DigitalOcean accounts
s	apps	Display commands for working with apps
s	auth	Display commands for authenticating doctl with an account
s	balance	Display commands for retrieving your account balance
s	billing-history	Display commands for retrieving your billing history
s	compute	Display commands that manage infrastructure
s	databases	Display commands that manage databases
s	invoice	Display commands for retrieving invoices for your account
s	kubernetes	Displays commands to manage Kubernetes clusters and configurations
s	monitoring	[Beta] Display commands to manage monitoring
s	projects	Manage projects and assign resources to them
s	registry	Display commands for working with container registries
s	vpcs	Display commands that manage VPCs
o	-h|--help	Help for doctl	
o	-v|--verbose	Enable verbose output	
o	-o|--output	Desired output format	v
o	--trace	Show a log of network activity while performing a command	
o	-c|--config	Specify a custom config file (default "$HOME/config.yaml")	
o	-u|--api-url	Override default API endpoint	
o	-t|--access-token	API V2 access token	
o	version	Show the current version	
=		-o
v	text	
v	json	
@	completion
a	1	0
#	completion	1
v	bash	
v	zsh	
v	fish	
@	help
a	1	0
@	1-click
s	list	
@	1-click list
@	account
s	get	Retrieve account profile details
s	ratelimit	Retrieve your API usage and the remaining quota
@	account get
@	account ratelimit
@	apps
s	create	Create an app
s	create-deployment	Create a deployment
s	delete	Deletes an app
s	get	Get an app
s	get-deployment	Get a deployment
s	list	List all apps
s	list-alerts	List alerts on an app
s	list-deployments	List all deployments
s	list-regions	List App Platform regions
s	logs	Get logs
s	propose	Propose an app spec
s	spec	Display commands for working with app specs
s	tier	Display commands for working with app tiers
s	update	Update an app
s	update-alert-destinations	Update alert destinations
@	apps create
@	apps create-deployment
@	apps delete
@	apps get
@	apps get-deployment
@	apps list
@	apps list-alerts
@	apps list-deployments
@	apps list-regions
@	apps logs
@	apps propose
@	apps spec
@	apps tier
@	apps update
@	apps update-alert-destinations
@	auth
s	init	Initialize doctl to use a specific account
s	list	List available authentication contexts
s	remove	Remove authentication contexts
s	switch	Switches between authentication contexts
@	auth init
@	auth list
@	auth remove
@	auth switch
@	balance
s	get	Retrieve your account balance
@	balance get
@	billing-history
s	list	Retrieve a paginated billing history for a user
@	billing-history list
@	compute
s	action	Display commands for retrieving resource action history
s	cdn	Display commands that manage CDNs
s	certificate	Display commands that manage SSL certificates and private keys
s	domain	Display commands that manage domains
s	droplet	Manage virtual machines (Droplets)
s	droplet-action	Display Droplet action commands
s	firewall	Display commands to manage cloud firewalls
s	floating-ip	Display commands to manage floating IP addresses
s	floating-ip-action	Display commands to associate floating IP addresses with Droplets
s	image	Display commands to manage images
s	image-action	Display commands to perform actions on images
s	load-balancer	Display commands to manage load balancers
s	region	Display commands to list datacenter regions
s	size	List available Droplet sizes
s	snapshot	Access and manage snapshots
s	ssh	Access a Droplet using SSH
s	ssh-key	Display commands to manage SSH keys on your account
s	tag	Display commands to manage tags
s	volume	Display commands to manage block storage volumes
s	volume-action	Display commands to perform actions on a volume
@	compute action
@	compute cdn
@	compute certificate
@	compute domain
@	compute droplet
@	compute droplet-action
@	compute firewall
@	compute floating-ip
@	compute floating-ip-action
@	compute image
@	compute image-action
@	compute load-balancer
@	compute region
@	compute size
@	compute snapshot
@	compute ssh
@	compute ssh-key
@	compute tag
@	compute volume
@	compute volume-action
@	databases
s	backups	List database cluster backups
s	connection	Retrieve connection details for a database cluster
s	create	Create a database cluster
s	db	Display commands for managing individual databases within a cluster
s	delete	Delete a database cluster
s	firewalls	Display commands to manage firewall rules (called `trusted sources` in the control panel) for…
s	get	Get details for a database cluster
s	list	List your database clusters
s	maintenance-window	Display commands for scheduling automatic maintenance on your database cluster
s	migrate	Migrate a database cluster to a new region
s	pool	Display commands for managing connection pools
s	replica	Display commands to manage read-only database replicas
s	resize	Resize a database cluster
s	sql-mode	Display commands to configure a MySQL database cluster's SQL modes
s	user	Display commands for managing database users
@	databases backups
@	databases connection
@	databases create
@	databases db
@	databases delete
@	databases firewalls
@	databases get
@	databases list
@	databases maintenance-window
@	databases migrate
@	databases pool
@	databases replica
@	databases resize
@	databases sql-mode
@	databases user
@	invoice
s	csv	Download a CSV file of an invoice
s	get	Retrieve a list of all the items on an invoice
s	list	List all of the invoices for your account
s	pdf	Download a PDF file of an invoice
s	summary	Get a summary of an invoice
@	invoice csv
@	invoice get
@	invoice list
@	invoice pdf
@	invoice summary
@	kubernetes
s	1-click	Display commands that pertain to kubernetes 1-click applications
s	cluster	Display commands for managing Kubernetes clusters
s	options	List possible option values for use inside Kubernetes commands
@	kubernetes 1-click
@	kubernetes cluster
@	kubernetes options
@	monitoring
s	alert	Display commands for managing alert policies
@	monitoring alert
@	projects
s	create	Create a new project
s	delete	Delete the specified project
s	get	Retrieve details for a specific project
s	list	List existing projects
s	resources	Manage resources assigned to a project
s	update	Update an existing project
@	projects create
@	projects delete
@	projects get
@	projects list
@	projects resources
@	projects update
@	registry
s	create	Create a private container registry
s	delete	Delete a container registry
s	docker-config	Generate a docker auth configuration for a registry
s	garbage-collection	Display commands for garbage collection for a container registry
s	get	Retrieve details about a container registry
s	kubernetes-manifest	Generate a Kubernetes secret manifest for a registry
s	login	Log in Docker to a container registry
s	logout	Log out Docker from a container registry
s	options	List available container registry options
s	repository	Display commands for working with repositories in a container registry
@	registry create
@	registry delete
@	registry docker-config
@	registry garbage-collection
@	registry get
@	registry kubernetes-manifest
@	registry login
@	registry logout
@	registry options
@	registry repository
@	vpcs
s	create	Create a new VPC
s	delete	Permanently delete a VPC
s	get	Retrieve a VPC
s	list	List VPCs
s	update	Update a VPC's configuration
@	vpcs create
@	vpcs delete
@	vpcs get
@	vpcs list
@	vpcs update

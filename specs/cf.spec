@	
s	app|a	Display health and status for app
s	ssh	Display health and status for app
s	env	Show all env variables for an app
s	orgs	List all orgs
s	version|-v|--version	Print the version of cf
s	login	Log user in
s	logout	Log user out
s	password	Change user password
s	target	Set or view the targeted org or space
s	api	Set or view target api url
s	auth	Auth user non-interactively
s	apps	List all apps in the target space
s	push	Push a new app or sync changes to an existing app
s	scale	Change or view the instance count, disk space limit, and memory limit for an app
s	delete	Delete an app
s	rename	Rename an app
s	start	Start an app
s	stop	Stop an app
s	restart	Stop all instances of the app, then start them again. This may cause downtime
s	restage	Recreate the app's executable artifact using the latest pushed app files and the latest…
s	restart-app-instance	Terminate the running application Instance at the given index and instantiate a new instance of…
s	run-task	Run a one-off task on an app
s	tasks	List tasks of an app
s	terminate-task	Terminate a running task of an app
s	events	Show recent app events
s	files	Print out a list of files in a directory or the contents of a specific file of an app running on…
s	logs	Trail or show recent logs for an app
s	set-env	Set an environment variable for an app
s	unset-env	Remove an environment variable
s	stacks	List all stacks (a stack is a pre-built file system, including an operating system, that can run…
s	copy-source	Copies the source code of an application to another existing application (and restarts that…
s	create-app-manifest	Create an app manifest for an app that has been pushed successfully
s	get-health-check	Show the type of health check performed on an app
s	set-health-check	Change type of health check performed on an app
s	enable-ssh	Enable ssh for the application
s	disable-ssh	Disable ssh for the application
s	ssh-enabled	Reports whether SSH is enabled on an application container instance
s	marketplace	List available offerings in the marketplace
s	services|s	List all service instances in the target space
s	create-service	Create a service instance
s	update-service	Update a service instance
s	delete-service	Delete a service instance
s	rename-service	Rename a service instance
s	create-service-key	Create key for a service instance
s	service-keys	List keys for a service instance
s	service-key	Show service key info
s	delete-service-key	Delete a service key
s	bind-service	Bind a service instance to an app
s	unbind-service	Unbind a service instance from an app
s	bind-route-service	Bind a service instance to an HTTP route
s	unbind-route-service	Unbind a service instance from an HTTP route
s	create-user-provided-service	Make a user-provided service instance available to CF apps
s	update-user-provided-service	Update user-provided service instance
s	org	Show org info
s	create-org	Create an org
s	delete-org	Delete an org
s	rename-org	Rename an org
s	spaces	List all spaces in an org
s	space	Show space info
s	create-space	Create a space
s	delete-space	Delete a space
s	rename-space	Rename a space
s	allow-space-ssh	Allow SSH access for the space
s	disallow-space-ssh	Disallow SSH access for the space
s	space-ssh-allowed	Reports whether SSH is allowed in a space
s	domains	List domains in the target org
s	create-domain	Create a domain in an org for later use
s	delete-domain	Delete a domain
s	create-shared-domain	Create a domain that can be used by all orgs (admin-only)
s	delete-shared-domain	Delete a shared domain
s	router-groups	List router groups
s	routes	List all routes in the current space or the current organization
s	create-route	Create a url route in a space for later use
s	check-route	Perform a simple check to determine whether a route currently exists or not
s	map-route	Add a url route to an app
s	unmap-route	Remove a url route from an app
s	delete-route	Delete a route
s	delete-orphaned-routes	Delete all orphaned routes (i.e. those that are not mapped to an app)
s	create-user	Create a new user
s	delete-user	Delete a user
s	org-users	Show org users by role
s	set-org-role	Assign an org role to a user
s	unset-org-role	Remove an org role from a user
s	space-users	Show space users by role
s	set-space-role	Assign a space role to a user
s	unset-space-role	Remove a space role from a user
s	quotas	List available usage quotas
s	quota	Show quota info
s	set-quota	Assign a quota to an org
s	create-quota	Define a new resource quota
s	delete-quota	Delete a quota
s	update-quota	Update an existing resource quota
s	space-quotas	List available space resource quotas
s	space-quota	Show space quota info
s	create-space-quota	Define a new space resource quota
s	update-space-quota	Update an existing space quota
s	delete-space-quota	Delete a space quota definition and unassign the space quota from all spaces
s	set-space-quota	Assign a space quota definition to a space
s	unset-space-quota	Unassign a quota from a space
s	curl	Executes a request to the targeted API endpoint
s	oauth-token	Retrieve and display the OAuth token for the current session
s	ssh-code	Get a one time password for ssh clients
s	add-plugin-repo	Add a new plugin repository
s	remove-plugin-repo	Remove a plugin repository
s	list-plugin-repos	List all the added plugin repositories
s	repo-plugins	List all available plugins in specified repository or in all added repositories
s	plugins	List all available plugin commands
s	install-plugin	Install CLI plugin
s	uninstall-plugin	Uninstall the plugin defined in command argument
o	--help|-h	Show help for Cloud Foundry command line tool	
o	-v	Print API request diagnostics to stdout	
@	app
o	--guid	Retrieve and display the given app's guid. All other health and status output for the app is…	
a	1	0
#	app	1
d
@	ssh
o	-v	Verbose output	
a	1	0
#	ssh	1
d
@	env
a	1	0
#	env	1
d
@	orgs
@	version
@	login
o	-a	API endpoint (e.g. https://api.example.com)	v
o	-o	Org	v
o	-s	Space	v
o	-p	Password	v
o	-u	Username	v
=	login	-o
d
=	login	-s
d
@	logout
@	password
@	target
o	-o	Org	v
o	-s	Space	v
=	target	-o
d
=	target	-s
d
@	api
o	--skip-ssl-validation	Skip verification of the API endpoint. Not recommended!	
o	--unset	Remove all api endpoint targeting	
a	1	0
@	auth
a	2	0
@	apps
@	push
o	-b	Custom buildpack by name or git url	v
o	-c	Startup command, set to null to reset to default start command	V
o	-d	Domain	v
o	-o|--docker-image	Docker image	v
o	-f	Path to manifest	v
o	-n|--host-name	Hostname	v
o	-i	Number of instances	v
o	-k	Disk limit	v
o	-m	Memory limit	v
@	scale
o	-f	Force restart of app without prompt	
o	-i	Number of instances	v
o	-k	Disk limit	v
o	-m	Memory limit	v
@	delete
o	-f	Force deletion without confirmation	
o	-r	Also delete any mapped routes	
a	1	0
#	delete	1
d
@	rename
a	2	0
#	rename	1
d
@	start
a	1	0
#	start	1
d
@	stop
a	1	0
#	stop	1
d
@	restart
a	1	0
#	restart	1
d
@	restage
a	1	0
#	restage	1
d
@	restart-app-instance
a	2	0
#	restart-app-instance	1
d
@	run-task
o	-k	Disk limit	v
o	-m	Memory limit	v
o	--name	Name for task	v
a	2	0
#	run-task	1
d
@	tasks
a	1	0
#	tasks	1
d
@	terminate-task
a	2	0
#	terminate-task	1
d
@	events
a	1	0
#	events	1
d
@	files
o	-i	Instance	v
a	2	0
#	files	1
d
@	logs
o	--recent	Dump recent logs instead of tailing	
a	1	0
#	logs	1
d
@	set-env
a	3	0
#	set-env	1
d
@	unset-env
a	2	0
#	unset-env	1
d
@	stacks
@	copy-source
o	-s	Space that contains the target application	v
o	-o	Org that contains the target application	v
o	--no-restart	Override restart of the application in target environment after copy-source completes	
a	2	0
=	copy-source	-s
d
=	copy-source	-o
d
@	create-app-manifest
o	-p	Path for file creation	v
a	1	0
#	create-app-manifest	1
d
@	get-health-check
a	1	0
#	get-health-check	1
d
@	set-health-check
a	2	0
#	set-health-check	1
d
@	enable-ssh
a	1	0
#	enable-ssh	1
d
@	disable-ssh
a	1	0
#	disable-ssh	1
d
@	ssh-enabled
a	1	0
#	ssh-enabled	1
d
@	marketplace
o	-s	Show plan details for a particular service offering	v
@	services
@	create-service
o	-c	Valid JSON object containing service-specific configuration parameters, provided either in-line or…	v
o	-t	User provided tags	v
a	3	0
@	update-service
o	-c	Valid JSON object containing service-specific configuration parameters, provided either in-line or…	v
o	-p	Change service plan for a service instance	v
o	-t	User provided tags	v
a	1	0
#	update-service	1
d
@	delete-service
o	-f	Force deletion without confirmation	
a	1	0
#	delete-service	1
d
@	rename-service
a	2	0
#	rename-service	1
d
@	create-service-key
o	-c	Valid JSON object containing service-specific configuration parameters, provided either in-line or…	v
a	2	0
#	create-service-key	1
d
@	service-keys
a	1	0
#	service-keys	1
d
@	service-key
a	2	0
#	service-key	1
d
@	delete-service-key
o	-f	Force deletion without confirmation	
a	2	0
#	delete-service-key	1
d
@	bind-service
o	-c	Valid JSON object containing service-specific configuration parameters, provided either in-line or…	v
a	2	0
#	bind-service	1
d
#	bind-service	2
d
@	unbind-service
a	2	0
#	unbind-service	1
d
#	unbind-service	2
d
@	bind-route-service
o	-c	Valid JSON object containing service-specific configuration parameters, provided either in-line or…	v
o	-n|--hostname	Hostname used in combination with DOMAIN to specify the route to bind	v
o	--path	Path used in combination with HOSTNAME and DOMAIN to specify the route to bind	v
a	2	0
#	bind-route-service	2
d
@	unbind-route-service
o	-f	Force unbinding without confirmation	
o	-n|--hostname	Hostname used in combination with DOMAIN to specify the route to bind	v
o	--path	Path used in combination with HOSTNAME and DOMAIN to specify the route to bind	v
a	2	0
#	unbind-route-service	2
d
@	create-user-provided-service
o	-p	Credentials, provided inline or in a file, to be exposed in the VCAP_SERVICES environment variable…	v
o	-l	URL to which logs for bound applications will be streamed	v
o	-r	URL to which requests for bound routes will be forwarded. Scheme for this URL must be https	v
a	1	0
@	update-user-provided-service
o	-p	Credentials, provided inline or in a file, to be exposed in the VCAP_SERVICES environment variable…	v
o	-l	URL to which logs for bound applications will be streamed	v
o	-r	URL to which requests for bound routes will be forwarded. Scheme for this URL must be https	v
a	1	0
@	org
o	--guid	Retrieve and display the given org's guid. All other output for the org is suppressed	
a	1	0
#	org	1
d
@	create-org
o	-p	Quota to assign to the newly created org (excluding this option results in assignment of default…	v
a	1	0
@	delete-org
o	-f	Force deletion without confirmation	
a	1	0
#	delete-org	1
d
@	rename-org
a	2	0
#	rename-org	1
d
@	spaces
@	space
o	--guid	Retrieve and display the given org's guid. All other output for the org is suppressed	
o	--security-group-rules	Retrieve the rules for all the security groups associated with the space's guid. All other output…	
a	1	0
#	space	1
d
@	create-space
o	-o	Org	v
o	-p	Quota to assign to the newly created space	v
a	1	0
=	create-space	-o
d
@	delete-space
o	-o	Delete space within specified org	v
o	-f	Force deletion without confirmation	
a	1	0
=	delete-space	-o
d
#	delete-space	1
d
@	rename-space
a	2	0
#	rename-space	1
d
@	allow-space-ssh
a	1	0
#	allow-space-ssh	1
d
@	disallow-space-ssh
a	1	0
#	disallow-space-ssh	1
d
@	space-ssh-allowed
a	1	0
#	space-ssh-allowed	1
d
@	domains
@	create-domain
a	2	0
#	create-domain	1
d
@	delete-domain
o	-f	Force deletion without confirmation	
a	1	0
#	delete-domain	1
d
@	create-shared-domain
o	--router-group	Routes for this domain will be configured only on the specified router group	
a	1	0
@	delete-shared-domain
o	-f	Force deletion without confirmation	
a	1	0
@	router-groups
@	routes
o	--orglevel	List all the routes for all spaces of current organization	
@	create-route
o	--hostname|-n	Hostname for the HTTP route (required for shared domains)	v
o	--path	Path for the HTTP route	v
o	--port	Port for the TCP route	v
o	--random-port	Create a random port for the TCP route	
a	2	0
#	create-route	1
d
@	check-route
o	--path	Path for the route	v
a	2	0
@	map-route
o	--hostname|-n	Hostname for the HTTP route (required for shared domains)	v
o	--path	Path for the HTTP route	v
o	--port	Port for the TCP route	v
o	--random-port	Create a random port for the TCP route	
a	2	0
#	map-route	1
d
@	unmap-route
o	--hostname|-n	Hostname used to identify the HTTP route	v
o	--path	Path used to identify the HTTP route	v
o	--port	Port used to identify the TCP route	v
a	2	0
#	unmap-route	1
d
@	delete-route
o	--hostname|-n	Hostname used to identify the HTTP route	v
o	--path	Path used to identify the HTTP route	v
o	--port	Port used to identify the TCP route	v
o	-f	Force deletion without confirmation	
a	1	0
@	delete-orphaned-routes
o	-f	Force deletion without confirmation	
@	create-user
o	--origin	Origin for mapping a user account to a user in an external identity provider	v
a	2	0
@	delete-user
o	-f	Force deletion without confirmation	
a	1	0
@	org-users
o	-a	List all users in the org	
a	1	0
#	org-users	1
d
@	set-org-role
a	3	0
#	set-org-role	2
d
@	unset-org-role
a	3	0
#	unset-org-role	2
d
@	space-users
@	set-space-role
a	4	0
#	set-space-role	2
d
#	set-space-role	3
d
@	unset-space-role
a	4	0
#	unset-space-role	2
d
#	unset-space-role	3
d
@	quotas
@	quota
a	1	0
@	set-quota
a	2	0
#	set-quota	1
d
@	create-quota
o	-a	Total number of application instances	v
o	-i	Maximum amount of memory an application instance can have	v
o	-m	Total amount of memory a space can have	v
o	--reserved-route-ports	Maximum number of routes that may be created with reserved ports (Default: 0)	v
o	-s	Total number of service instances	v
o	-r	Total number of routes	v
o	--allow-paid-service-plans	Can provision instances of paid service plans	
a	1	0
@	delete-quota
o	-f	Force deletion without confirmation	
a	1	0
@	update-quota
o	-a	Total number of application instances	v
o	-i	Maximum amount of memory an application instance can have	v
o	-m	Total amount of memory a space can have	v
o	--reserved-route-ports	Maximum number of routes that may be created with reserved ports (Default: 0)	v
o	-s	Total number of service instances	v
o	-r	Total number of routes	v
o	-n	New name	v
o	--allow-paid-service-plans	Can provision instances of paid service plans	
o	--disallow-paid-service-plans	Cannot provision instances of paid service plans	
a	1	0
@	space-quotas
@	space-quota
a	1	0
@	create-space-quota
o	-a	Total number of application instances	v
o	-i	Maximum amount of memory an application instance can have	v
o	-m	Total amount of memory a space can have	v
o	--reserved-route-ports	Maximum number of routes that may be created with reserved ports (Default: 0)	v
o	-s	Total number of service instances	v
o	-r	Total number of routes	v
o	--allow-paid-service-plans	Can provision instances of paid service plans	
a	1	0
@	update-space-quota
o	-a	Total number of application instances	v
o	-i	Maximum amount of memory an application instance can have	v
o	-m	Total amount of memory a space can have	v
o	--reserved-route-ports	Maximum number of routes that may be created with reserved ports (Default: 0)	v
o	-s	Total number of service instances	v
o	-r	Total number of routes	v
o	-n	New name	v
o	--allow-paid-service-plans	Can provision instances of paid service plans	
o	--disallow-paid-service-plans	Cannot provision instances of paid service plans	
a	1	0
@	delete-space-quota
o	-f	Force deletion without confirmation	
a	1	0
@	set-space-quota
a	2	0
#	set-space-quota	1
d
@	unset-space-quota
a	2	0
#	unset-space-quota	1
d
@	curl
o	-H	Custom headers to include in the request, flag can be specified multiple times	v
o	-X	HTTP method (GET,POST,PUT,DELETE,etc)	v
o	-d	HTTP data to include in the request body, or '@' followed by a file name to read the data from	v
o	--output	Write curl body to FILE instead of stdout	v
o	-i	Include response headers in the output	
a	1	0
@	oauth-token
@	ssh-code
@	add-plugin-repo
a	2	0
@	remove-plugin-repo
a	1	0
@	list-plugin-repos
@	repo-plugins
o	-r	Name of a registered repository	v
@	plugins
o	--checksum	Compute and show the sha1 value of the plugin binary file	
@	install-plugin
o	-r	Name of a registered repository where the specified plugin is located	v
o	-f	Force install of plugin without confirmation	
a	2	0
@	uninstall-plugin
a	1	0

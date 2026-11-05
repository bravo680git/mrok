@	
s	config	Manage your profile to store access settings for your MongoDB deployment
s	auth	Manage the CLI's authentication state
s	quickstart	Create and access an Atlas Cluster
s	project|projects	Project operations
s	organization|orgs|org|organizations	Organization operations
s	globalapikeys|global-api-keys|globalApiKey|globalapikey|global-api-key|globalApiKeys	Global API Keys operations
s	globalaccesslists|global-access-lists|globalAccessList|globalaccesslist|global-access-list|globalWhitelists|globalwhitelists|global-whitelists|globalWhitelist|globalwhitelist|global-whitelist|globalAccessLists	Manage IP access list for Global API Key
s	user|users	Users operations
s	team|teams	Teams operations
s	cluster|clusters	Manage clusters for your project
s	dbuser|dbusers	Manage database users for your project
s	customdbroles|custom-db-roles|customDbRole|customdbrole|custom-db-role|customDBRoles|customDbRoles	Manage custom database roles for your project
s	accesslists|access-lists|accessList|accesslist|access-list|whitelists|whitelist|accessLists	Manage the access IP access list for your project
s	datalakes|data-lakes|dataLake|datalake|data-lake|dataLakes	Manage Atlas Data Lakes for your project
s	alert|alerts	Manage alerts for your project
s	backup|backups	Manage cloud backups for your project
s	event|events	Manage events for your organization or project
s	metric|measurements|measurement|metrics	Get metrics on the MongoDB process
s	performanceadvisor|performance-advisor|performanceAdvisor	Performance Advisor operations
s	log|logs	Download host logs for your project
s	process|processes	Manage MongoDB processes for your project
s	privateendpoints|private-endpoints|privateEndpoint|privateendpoint|private-endpoint|privateEndpoints	Manage Atlas private endpoints
s	networking	Networking operations
s	security	Manage security configuration for your project
s	integration|integrations	Third party integration operations
s	maintenancewindows|maintenance-windows|maintenanceWindow|maintenancewindow|maintenance-window|maintenanceWindows	Manage Atlas maintenance windows
s	customdns|custom-dns|customDn|customdn|custom-dn|customDns	Manage DNS configuration of Atlas project’s clusters deployed to AWS
s	cloudproviders|cloud-providers|cloudProvider|cloudprovider|cloud-provider|cloudProviders	Manage unified IAM role access in Atlas
s	sl|serverless	Manage serverless instances for your project
s	livemigrations|live-migrations|liveMigration|livemigration|live-migration|lm|liveMigrations	Manage a Live Migration to Atlas for your organization
s	accesslogs|access-logs|accessLog|accesslog|access-log|accessLogs	Manage the access logs of a cluster
s	completion	Generate the autocompletion script for the specified shell
s	help	Help about any command
o	--profile|-P	Profile to use from your configuration file	vp
o	--help|-h	Display help	p
@	config
s	init	Configure a profile to store access settings for your MongoDB deployment
s	set	Configure specific properties of a profile
s	ls|list	List available profiles
s	get|describe	Return a specific profile
s	mv|rename	Rename a profile
s	rm|delete	Delete a profile
@	config init
o	--gov	Create a default profile for atlas for gov	
@	config set
@	config ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	config get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	config mv
@	config rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	auth
s	login	Authenticate with MongoDB Atlas
s	whoami	Verifies and displays information about your authentication state
s	logout	Log out of the CLI
@	auth login
o	--cm	Log in to Cloud Manager	
o	--gov	Log in to Atlas for Government	
o	--noBrowser	Don't try to open a browser session	
@	auth whoami
@	auth logout
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	quickstart
o	--accessListIp	IP address to be allowed to access the deployment	v
o	--clusterName	Name of the cluster	v
o	--default|-Y	Flag that indicates whether to run the Quickstart command with all the auto-generated values to…	
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--password	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of your cloud service provider. Valid values are AWS, AZURE, or GCP	v
o	--region|-r	Physical location of your MongoDB cluster. For a complete list of supported AWS regions, see…	v
o	--skipMongosh	Indicates whether to skip accessing your deployment with MongoDB Shell	
o	--skipSampleData	Indicates whether to skip loading sample data into your Atlas Cluster	
o	--tier	Tier for each data-bearing server in the cluster	v
o	--username	Username for authenticating to MongoDB	v
@	project
s	ls|list	List projects
s	create	Create a project
s	rm|delete	Delete a project
s	show|get|describe	Describe a project
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Manage API Keys for your project
s	user|users	Manage users for a project
s	team|teams	Teams operations
s	invitation|invitations	Invitation operations
@	project ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	project create
o	--govCloudRegionsOnly	Only for AtlasGov projects. If specified, designates that the project uses only the AWS GovCloud…	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ownerId	Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the…	v
o	--withoutDefaultAlertSettings	Flag that indicates whether to create the new project with the default alert settings enabled…	
@	project rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	project show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	project apikeys
s	ls|list	List API Keys for your project
s	create	Create an API Key for your project
s	rm|delete	Delete an API Key for your project
s	update|assign	Assign an API Key to a project
@	project apikeys ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project apikeys create
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	List of roles for the API key	v
@	project apikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project apikeys update
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	List of roles for the API key	v
@	project user
s	ls|list	List all users for a project
s	rm|delete	Delete user from a project
@	project user ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project user rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project team
s	ls|list	Get all teams in a project
s	add	Add team to a project
s	rm|delete	Delete team from a project
s	updates|update	Update roles for a team in a project
@	project team ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project team add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	Project role you want to assign to the team	v
@	project team rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project team updates
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	Project role you want to assign to the team	v
@	project invitation
s	ls|list	Retrieves all pending invitations to the specified project
s	get|describe	Retrieve details for one pending invitation to the specified project
s	rm|delete	Deletes one pending invitation to the specified project
s	create|invite	Invites one user to the project that you specify
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
@	project invitation ls
o	--email	User's email address	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project invitation get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project invitation rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	project invitation create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles for the associated organization	v
o	--teamId	Unique identification of the team	v
@	project invitation updates
o	--email	User's email address	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles for the associated organization	v
@	organization
s	ls|list	List organizations
s	show|describe	Describe an organizations
s	create	Create an organization
s	rm|delete	Delete an organization
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Organization API Keys operations
s	user|users	Users operations
s	invitation|invitations	Invitation operations
@	organization ls
o	--includeDeleted	If specified, Atlas includes the deleted organizations	
o	--limit	Number of items per page	v
o	--name	Performs a case-insensitive search for organizations which exactly match the specified name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	organization show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	organization create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	organization rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	organization apikeys
s	ls|list	List API Keys for your organization
s	show|describe	Get a specific Organization API Key
s	updates|assign	Update an Organization API Key
s	create	Create an Organization API Key
s	rm|delete	Delete an Organization API Key
s	accesslists|access-lists|accessList|accesslist|access-list|whitelists|whitelist|accessLists	Manage the IP access list for your API Key
@	organization apikeys ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	organization apikeys show
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	organization apikeys updates
o	--desc	Description of the API key	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	organization apikeys create
o	--desc	Description of the API key	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	organization apikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	organization apikeys accesslists
s	ls|list	List IP access list entries for your API Key
s	create	Create an IP access list for your API Key
s	rm|delete	Delete an IP access list from your API Key
@	organization apikeys accesslists ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	organization apikeys accesslists create
o	--apiKey	API Key	v
o	--cidr	Whitelist entry in CIDR notation to be added for a given API key	v
o	--ip	IP address to be allowed for a given API key	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	organization apikeys accesslists rm
o	--apiKey	API Key	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	organization user
s	ls|list	List users in a organization
@	organization user ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	organization invitation
s	ls|list	Retrieves all pending invitations to the specified organization
s	get|describe	Retrieve details for one pending invitation to the specified organization
s	rm|delete	Deletes one pending invitation to the specified organization
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
s	create|invite	Invites one user to the organization that you specify
@	organization invitation ls
o	--email	User's email address	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	organization invitation get
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	organization invitation rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	organization invitation updates
o	--email	User's email address	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	User's roles for the associated organization	v
@	organization invitation create
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	User's roles for the associated organization	v
o	--teamId	Unique identification of the team	v
@	globalapikeys
s	ls|list	List Global API Keys
s	show|describe	Get a specific Global API Key
s	create	Create a Global API Key
s	update	Update a Global API Key
s	rm|delete	Delete a Global API Key
@	globalapikeys ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	globalapikeys show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	globalapikeys create
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	globalapikeys update
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	globalapikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	globalaccesslists
s	ls|list	List Atlas IP access list entries for Global API Key
s	show|describe	Return one Global IP access list entry
s	create	Create an IP access list for Global API Key
s	rm|delete	Delete an IP access list from Global API Key
@	globalaccesslists ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	globalaccesslists show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	globalaccesslists create
o	--cidr	Whitelist entry in CIDR notation to be added for a given API key	v
o	--desc	IP address to be allowed for a given API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	globalaccesslists rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	user
s	invite	Invite a user
s	get|describe	Get a user by username or id
s	rm|delete	Delete an Ops Manager user
@	user invite
o	--country	The ISO 3166-1 alpha two-letter country code of the user's country of residence	v
o	--email	User's email address	v
o	--firstName	User's first name	v
o	--lastName	User's last name	v
o	--mobile	The user's mobile or cell phone number	v
o	--orgRole	User's roles for the associated organization	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password	User's password	v
o	--projectRole	User's roles for the associated project	v
o	--username	Username of the user	v
@	user get
o	--id	Unique identifier of the user	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--username	Username of the user	v
@	user rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	team
s	ls|list	Get all teams in an organization
s	get|describe	Get a team in an organization
s	create	Create a team in an organization
s	user|users	Users operations
s	rm|delete	Delete a team from an organization
@	team ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	team get
o	--id	Unique identification of the team	v
o	--name	Name of the team	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	team create
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--username	List of usernames to add to the new team	v
@	team user
s	ls|list	List users of a team
s	add	Add a user to a team
s	rm|delete	Delete user from a team
@	team user ls
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--teamId	Unique identification of the team	v
@	team user add
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--teamId	Unique identification of the team	v
@	team user rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--teamId	Unique identification of the team	v
@	team rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster
s	ls|list	List clusters for your project
s	get|describe	Describe a cluster
s	create	Create one cluster in the specified project
s	watch	Watch for a cluster to be available
s	update	Update a MongoDB cluster
s	pause	Pause a running MongoDB cluster in Atlas
s	start	Start a paused MongoDB cluster in Atlas
s	rm|delete	Delete a cluster from your project
s	loadSampleData	Load sample data into a MongoDB cluster in Atlas
s	index|indexes	Manage cluster rolling indexes for your project
s	fts|search	Manage Atlas Search for your cluster
s	onlinearchives|online-archives|onlineArchive|onlinearchive|online-archive|onlineArchives	Manage online archives for your cluster
s	connectionstrings|connection-strings|connectionString|connectionstring|connection-string|cs|connectionStrings	Manage MongoDB cluster connection string
@	cluster ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster create
o	--backup	If true, enables Continuous Cloud Backup for your deployment	
o	--biConnector	If true, enables BI Connector for Atlas on the deployment	
o	--diskSizeGB	Capacity, in gigabytes, of the host's root volume	v
o	--file|-f	File name to use, optional file with a json cluster configuration	v
o	--mdbVersion	MongoDB version of the cluster to deploy	v
o	--members|-m	Number of members in the replica set	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of your cloud service provider. Valid values are AWS, AZURE, or GCP	v
o	--region|-r	Physical location of your MongoDB cluster. For a complete list of supported AWS regions, see…	v
o	--shards|-s	Number of shards in the cluster	v
o	--tier	Tier for each data-bearing server in the cluster	v
o	--type	Type of the cluster that you want to create. Valid values are REPLICASET or SHARDED	v
=	cluster create	--file
t	filepaths
@	cluster watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster update
o	--diskSizeGB	Capacity, in gigabytes, of the host's root volume	v
o	--file|-f	File name to use, optional file with a json cluster configuration	v
o	--mdbVersion	MongoDB version of the cluster to deploy	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--tier	Tier for each data-bearing server in the cluster	v
=	cluster update	--file
t	filepaths
@	cluster pause
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster start
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster loadSampleData
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster index
s	create	Create a rolling index for your MongoDB cluster
@	cluster index create
o	--clusterName	Name of the cluster	v
o	--collection	Collection name	v
o	--db	Database name	v
o	--key	Field to be indexed and the type of index in the following format: field:type	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--sparse	Flag that indicates whether Atlas should create a sparse index	
@	cluster fts
s	index|indexes	Manage Atlas Search indexes for your cluster
@	cluster fts index
s	ls|list	List Atlas search indexes for a cluster
s	create	Create a search index for a cluster
s	describe	Describe a search index for a cluster
s	update	Update a search index for a cluster
s	rm|delete	Delete a search index from a cluster
@	cluster fts index ls
o	--clusterName	Name of the cluster	v
o	--collection	Collection name	v
o	--db	Database name	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster fts index create
o	--clusterName	Name of the cluster	v
o	--file|-f	File name to use, file with a json index configuration	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cluster fts index create	--file
t	filepaths
@	cluster fts index describe
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster fts index update
o	--clusterName	Name of the cluster	v
o	--file|-f	File name to use, file with a json index configuration	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cluster fts index update	--file
t	filepaths
@	cluster fts index rm
o	--clusterName	Name of the cluster	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives
s	ls|list	List online archives for a cluster
s	describe	Describe an online archive for a cluster
s	create	Create an online archive for a cluster
s	update	Update an online archive for a cluster
s	start	Start a paused online archive from a cluster
s	pause	Pause an online archive from a cluster
s	rm|delete	Delete an online archive from a cluster
s	watch	Watch for an archive to be available
@	cluster onlinearchives ls
o	--clusterName	Name of the cluster	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives describe
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives create
o	--archiveAfter	Number of days that specifies the age limit for the data in the live Atlas cluster	v
o	--clusterName	Name of the cluster	v
o	--collection	Collection name	v
o	--dateField	Name of an already indexed date field from the documents	v
o	--dateFormat	Date format for the date field. Valid values are ISODATE, EPOCH_SECONDS, EPOCH_MILLIS, or…	v
o	--db	Database name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--partition	Fields to use to partition data. You can specify up to two frequently queried fields to use for…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives update
o	--archiveAfter	Number of days that specifies the age limit for the data in the live Atlas cluster	v
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives start
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives pause
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives rm
o	--clusterName	Name of the cluster	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster onlinearchives watch
o	--clusterName	Name of the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cluster connectionstrings
s	get|describe	Retrieve the SRV connection string of your MongoDB cluster
@	cluster connectionstrings get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	When set to 'private', retrieves the connection string for the network peering endpoint	v
@	dbuser
s	ls|list	List Atlas database users for your project
s	get|describe	Return a single Atlas database user for your project
s	create	Create a database user for your project
s	rm|delete	Delete a database user for your project
s	update	Update a database user for your project
s	cert|certs	Manage Atlas x509 certificates for your database users
@	dbuser ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	dbuser get
o	--authDB	Authentication database name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	dbuser create
o	--awsIAMType	AWS IAM method by which the provided username is authenticated. Valid values are NONE, USER, or ROLE	v
o	--deleteAfter	Timestamp in ISO 8601 in UTC after which Atlas deletes the user	v
o	--ldapType	LDAP method by which the provided username is authenticated. Valid values are NONE, USER, or GROUP	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password|-p	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles and the databases or collections on which the roles apply	v
o	--scope	Array of clusters and Atlas Data Lakes that this user has access to	v
o	--username|-u	Username for authenticating to MongoDB	v
o	--x509Type	X.509 method by which the provided username is authenticated. Valid values are NONE, MANAGED, or…	v
@	dbuser rm
o	--authDB	Authentication database name	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	dbuser update
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password|-p	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles and the databases or collections on which the roles apply	v
o	--scope	Array of clusters and Atlas Data Lakes that this user has access to	v
o	--username|-u	Username for authenticating to MongoDB	v
@	dbuser cert
s	ls|list	List of all Atlas-managed, unexpired certificates for a database user
s	create	Create a new Atlas-managed X.509 certificate for the specified database user
@	dbuser cert ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	dbuser cert create
o	--monthsUntilExpiration	Number of months that the certificate is valid for	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--username	Username of a database user	v
@	customdbroles
s	create	Create a custom database role for your project
s	get|describe	Return a single custom database role for your project
s	ls|list	List custom database roles for your project
s	rm|delete	Delete a custom database role for your project
s	update	Update a custom database role for your project
@	customdbroles create
o	--inheritedRole	List of inherited roles and the database on which the role is granted	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privilege	List of actions per database and collection. If no database or collections are provided, cluster…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdbroles get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdbroles ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdbroles rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdbroles update
o	--append	The input action and inheritedRoles that will be appended to the existing role	
o	--inheritedRole	List of inherited roles and the database on which the role is granted	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privilege	List of actions per database and collection. If no database or collections are provided, cluster…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	accesslists
s	get|describe	Describe an IP access list entry
s	ls|list	List Atlas IP access list entries for your project
s	create	Create an IP access list for your project
s	rm|delete	Delete an IP access list from your project
@	accesslists get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	accesslists ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	accesslists create
o	--comment	Optional description or comment for the entry	v
o	--currentIp	Flag that indicates whether to use the IP Address from the host that is currently executing the…	
o	--deleteAfter	ISO-8601-formatted UTC date after which Atlas removes the value from the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of access list entry. Valid values are cidrBlock, ipAddress, or awsSecurityGroup	v
@	accesslists rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	datalakes
s	ls|list	List Atlas Data Lakes for your project
s	describe	Return a specific data lake
s	create	Create a new data lake for your project
s	rm|delete	Delete a data lake from your project
s	update	Update a data lake for your project
@	datalakes ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	datalakes describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	datalakes create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	Amazon Resource Name (ARN) of the role which Atlas Data Lake uses for accessing the data stores	v
o	--testBucket	Name of an Amazon S3 data bucket which Atlas Data Lake uses to validate the provided role	v
@	datalakes rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	datalakes update
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Name of the region to which Atlas Data Lake routes client connections for data processing	v
o	--role	Amazon Resource Name (ARN) of the role which Atlas Data Lake uses for accessing the data stores	v
o	--testBucket	Name of an Amazon S3 data bucket which Atlas Data Lake uses to validate the provided role	v
@	alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	alert config create
o	--apiKey	Datadog API Key, Opsgenie API Key, VictorOps API key	v
o	--enabled	If set to true, the alert configuration is enabled	
o	--event	Type of the event that triggered the alert	v
o	--matcherFieldName	Name of the field in the target object to match on	v
o	--matcherOperator	Operator to test the field's value	v
o	--matcherValue	Value to test with the specified operator	v
o	--metricMode	If specified, Atlas computes the current metric value as an average	v
o	--metricName	Name of the metric against which Atlas checks the configured alert	v
o	--metricOperator	Operator to apply when checking the current metric value against the threshold value	v
o	--metricThreshold	Threshold value outside of which an alert will be triggered	v
o	--metricUnits	Units for the threshold value	v
o	--notificationChannelName	Slack channel name. Required for the SLACK notifications type	v
o	--notificationDelayMin	Number of minutes to wait after an alert condition is detected before sending out the first…	v
o	--notificationEmailAddress	Email address to which alert notifications are sent	v
o	--notificationEmailEnabled	Flag indicating whether email notifications should be sent	
o	--notificationFlowName	Flowdock Flow name in lower-case letters for sending alert notifications	v
o	--notificationIntervalMin	Number of minutes to wait between successive notifications for unacknowledged alerts that are not…	v
o	--notificationMobileNumber	Mobile number to which alert notifications are sent	v
o	--notificationOrgName	Flowdock organization's name in lower-case letters	v
o	--notificationRegion	Region that indicates which API URL to use	v
o	--notificationServiceKey	PagerDuty service key	v
o	--notificationSmsEnabled	Flag indicating whether text message notifications should be sent	
o	--notificationTeamId	Unique identifier of a team	v
o	--notificationToken	Slack API token, Bot token, or Flowdock personal API token	v
o	--notificationType	Type of alert notification. The values are DATADOG, EMAIL, FLOWDOCK, GROUP (Project), ORG…	v
o	--notificationUsername	Name of the Atlas user to which to send notifications	v
o	--notificationVictorOpsRoutingKey	VictorOps routing key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	alert config ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	alert config rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	alert config field
s	types|type	Lists available field types for your alert configurations
@	alert config field types
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	alert config update
o	--apiKey	Datadog API Key, Opsgenie API Key, VictorOps API key	v
o	--enabled	If set to true, the alert configuration is enabled	
o	--event	Type of the event that triggered the alert	v
o	--matcherFieldName	Name of the field in the target object to match on	v
o	--matcherOperator	Operator to test the field's value	v
o	--matcherValue	Value to test with the specified operator	v
o	--metricMode	If specified, Atlas computes the current metric value as an average	v
o	--metricName	Name of the metric against which Atlas checks the configured alert	v
o	--metricOperator	Operator to apply when checking the current metric value against the threshold value	v
o	--metricThreshold	Threshold value outside of which an alert will be triggered	v
o	--metricUnits	Units for the threshold value	v
o	--notificationChannelName	Slack channel name. Required for the SLACK notifications type	v
o	--notificationDelayMin	Number of minutes to wait after an alert condition is detected before sending out the first…	v
o	--notificationEmailAddress	Email address to which alert notifications are sent	v
o	--notificationEmailEnabled	Flag indicating whether email notifications should be sent	
o	--notificationFlowName	Flowdock Flow name in lower-case letters for sending alert notifications	v
o	--notificationIntervalMin	Number of minutes to wait between successive notifications for unacknowledged alerts that are not…	v
o	--notificationMobileNumber	Mobile number to which alert notifications are sent	v
o	--notificationOrgName	Flowdock organization's name in lower-case letters	v
o	--notificationRegion	Region that indicates which API URL to use	v
o	--notificationServiceKey	PagerDuty service key	v
o	--notificationSmsEnabled	Flag indicating whether text message notifications should be sent	
o	--notificationTeamId	Unique identifier of a team	v
o	--notificationToken	Slack API token, Bot token, or Flowdock personal API token	v
o	--notificationType	Type of alert notification. The values are DATADOG, EMAIL, FLOWDOCK, GROUP (Project), ORG…	v
o	--notificationUsername	Name of the Atlas user to which to send notifications	v
o	--notificationVictorOpsRoutingKey	VictorOps routing key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	alert get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	alert ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	alert ack
o	--comment	Optional description or comment for the entry	v
o	--forever|-F	Acknowledges an alert 'forever'	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--until	Time, in ISO 8601 format, until which the alert has been acknowledged. mongocli returns this value…	v
@	alert unack
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	alert global ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	backup
s	snapshot|snapshots	Manage cloud backup snapshots for your project
s	restore|restores	Manage cloud backup restore jobs for your project
@	backup snapshot
s	ls|list	List cloud backup snapshots for your project and cluster
s	take|create	Create a backup snapshot for your project and cluster
s	describe	Get a specific snapshot for your project
s	watch	Watch for a snapshot to be available
s	rm|delete	Delete a backup snapshot
@	backup snapshot ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	backup snapshot take
o	--desc	Description of the on-demand snapshot	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--retention	Cloud provider region in which you want to create the private endpoint connection	v
@	backup snapshot describe
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	backup snapshot watch
o	--clusterName	Name of the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	backup snapshot rm
o	--clusterName	Name of the cluster	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	backup restore
s	ls|list	List cloud backup restore jobs for your project and cluster
s	start	Start a restore job for your project and cluster
@	backup restore ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	backup restore start
o	--clusterName	Name of the cluster	v
o	--oplogInc	32-bit incrementing ordinal that represents operations within a given second. When paired with…	v
o	--oplogTs	Oplog timestamp given as a timestamp in the number of seconds that have elapsed since the UNIX…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pointInTimeUTCMillis	Timestamp in the number of milliseconds that have elapsed since the UNIX epoch that represents the…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--snapshotId	Unique identifier of the snapshot to restore	v
o	--targetClusterName	Name of the target cluster. For use only with automated restore jobs	v
o	--targetProjectId	Unique identifier of the project that contains the destination cluster for the restore job	v
@	event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	event ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	event organization
s	ls|list	Return all events for an organization
@	event organization ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--type	Type of the event that triggered the alert	v
@	event project
s	ls|list	Return all events for a project
@	event project ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	metric
s	process|processes	Get MongoDB process metrics for a given host
s	disk|disks	List available disks or disk metrics for a given host
s	database|databases	List available databases or database metrics for a given host
@	metric process
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	metric disk
s	ls|list	List available disks or disk partitions for a given host
s	describe	Describe disk partition metrics for a disk partition on a specified host
@	metric disk ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	metric disk describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	metric database
s	ls|list	List available databases or database metrics for a given host
s	describe	Describe database metrics for a database on a specific host
@	metric database ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	metric database describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	performanceadvisor namespace ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	performanceadvisor slowquerylogs ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nLog	Maximum number of log lines to return	v
o	--namespaces	Namespaces from which to retrieve suggested slow query logs	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	performanceadvisor suggestedindexes ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nExamples	Maximum number of example queries to provide that will be improved by a suggested index	v
o	--nIndexes	Maximum number of indexes to suggest	v
o	--namespaces	Namespaces from which to retrieve suggested indexes	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	performanceadvisor slowOT ls
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	performanceadvisor slowOT disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	log
s	download	Download a host mongodb logs
@	log download
o	--end	End of the period, in UNIX Epoch format, until which to retrieve logs	v
o	--force	Overwrites the destination file	
o	--out	Optional output file name. Uses the log name if the output file's name is not specified	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the date and time, in UNIX Epoch format, from which to retrieve logs	v
=	log download	--out
t	filepaths
@	process
s	ls|list	List MongoDB processes for your project
@	process ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints
s	ls|list	List Atlas Private Endpoints for your project
s	get|describe	Return a specific Private Endpoints for your project
s	create	Create a new private endpoint for your project
s	rm|delete	Delete a private endpoint from your project
s	watch	Watch for a private endpoint to be available
s	interface|interfaces	Manage Atlas private endpoint interfaces
s	aws	Manage AWS Private Endpoints
s	azure	Manage Azure Private Endpoints
s	gcp	Manage GCP private endpoints
s	regionalmodes|regional-modes|regionalMode|regionalmode|regional-mode|regionalModes	Manage regionalized private endpoint setting for your Atlas project
s	datalakes|data-lakes|dataLake|datalake|data-lake|dataLakes	Manage Data Lake private endpoints
s	onlinearchive|online-archive|onlineArchive	Manage Online Archive private endpoints
@	privateendpoints ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of the cloud provider you want to create the private endpoint connection for	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	privateendpoints rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of the cloud provider you want to create the private endpoint connection for	v
@	privateendpoints interface
s	add|create	Add a new interface to a private endpoint
s	get|describe	Return a specific private endpoint interface for your project
s	rm|delete	Delete a private endpoint interface from your project
@	privateendpoints interface add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints interface get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints interface rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws
s	ls|list	List AWS Private Endpoints for your project
s	get|describe	Return a specific AWS Private Endpoints for your project
s	create	Create a new AWS Private Endpoint for your project
s	rm|delete	Delete a specific AWS Private Endpoint for your project
s	watch	Watch for a specific AWS Private Endpoint to be available
s	interface|interfaces	Manage Atlas AWS private endpoint interfaces
@	privateendpoints aws ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	privateendpoints aws rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws interface
s	add|create	Add a new interface to a AWS private endpoint
s	get|describe	Return a specific AWS private endpoint interface for your project
s	rm|delete	Delete a specific AWS private endpoint interface and the related endpoint service for your project
@	privateendpoints aws interface add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws interface get
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints aws interface rm
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure
s	ls|list	List Azure Private Endpoints for your project
s	get|describe	Return a specific Azure Private Endpoints for your project
s	create	Create a new Azure Private Endpoint for your project
s	rm|delete	Delete a specific Azure Private Endpoint for your project
s	watch	Watch for a specific Azure Private Endpoint to be available
s	interface|interfaces	Manage Atlas Azure private endpoint interfaces
@	privateendpoints azure ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	privateendpoints azure rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure interface
s	add|create	Add a new Azure interface to a private endpoint
s	get|describe	Return a specific Azure private endpoint interface for your project
s	rm|delete	Delete a specific Azure private endpoint interface and related service for your project
@	privateendpoints azure interface add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the Azure private endpoint resource	v
o	--privateEndpointIpAddress	Private IP address of the private endpoint network interface you created in your Azure VNet	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure interface get
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints azure interface rm
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp
s	create	Create a new GCP private endpoint for your project
s	rm|delete	Delete a GCP private endpoint for your project
s	ls|list	List GCP private endpoints for your project
s	get|describe	Return a specific GCP private endpoint for your project
s	watch	Watch the specified GCP private endpoint to detect changes in the endpoint's state
s	interface|interfaces	Manage Atlas GCP private endpoint interfaces
@	privateendpoints gcp create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	privateendpoints gcp rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp interface
s	get|describe	Return a specific GCP private endpoint interface for your project
s	rm|delete	Delete a specific GCP private endpoint interface for your project
s	add|create	Create a GCP private endpoint interface
@	privateendpoints gcp interface get
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp interface rm
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints gcp interface add
o	--endpoint	List of GCP endpoints in the group separated by commas, such as…	v
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--gcpProjectId	Unique identifier of the GCP project in which the network peer resides	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints regionalmodes
s	enable	Enable the regionalized private endpoint setting for your Atlas project
s	disable	Disable the regionalized private endpoint setting for your Atlas project
s	get|describe	Get the regionalized private endpoint setting for your Atlas project
@	privateendpoints regionalmodes enable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints regionalmodes disable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints regionalmodes get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints datalakes
s	aws	Manage AWS private endpoints
@	privateendpoints datalakes aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	privateendpoints datalakes aws create
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints datalakes aws ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints datalakes aws get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints datalakes aws rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints onlinearchive
s	aws	Manage AWS private endpoints
@	privateendpoints onlinearchive aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	privateendpoints onlinearchive aws create
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints onlinearchive aws ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints onlinearchive aws get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	privateendpoints onlinearchive aws rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	networking
s	container|containers	Manage Network Peering containers
s	peering	Manage Network Peering connections
@	networking container
s	ls|list	List network peering containers in an Atlas project
s	rm|delete	Remove one network peering container in an Atlas project
@	networking container ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of your cloud service provider. Valid values are AWS, AZURE, or GCP	v
@	networking container rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	networking peering
s	ls|list	Retrieve details for all network peering connections in one Atlas project
s	create	Create a connection with AWS, Azure and Google Cloud
s	watch	Watch for a peering connection to be available
s	rm|delete	Delete a peering connection from an Atlas project
@	networking peering ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of your cloud service provider. Valid values are AWS, AZURE, or GCP	v
@	networking peering create
s	azure	Create a connection with Azure
s	aws	Create a connection with AWS
s	gcp	Create a connection with GCP
@	networking peering create azure
o	--atlasCidrBlock	CIDR block that Atlas uses for your clusters	v
o	--directoryId	Unique identifier for an Azure AD directory	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Atlas region where the container resides	v
o	--resourceGroup	Name of your Azure resource group	v
o	--subscriptionId	Unique identifier of the Azure subscription in which the VNet resides	v
o	--vnet	Name of your Azure VNet	v
@	networking peering create aws
o	--accountId	Account ID of the owner of the peer VPC	v
o	--atlasCidrBlock	CIDR block that Atlas uses for your clusters	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Atlas region where the container resides	v
o	--routeTableCidrBlock	Peer VPC CIDR block or subnet	v
o	--vpcId	Unique identifier of the peer VPC	v
@	networking peering create gcp
o	--atlasCidrBlock	CIDR block that Atlas uses for your clusters	v
o	--gcpProjectId	Unique identifier of the GCP project in which the network peer resides	v
o	--network	Unique identifier of the Network Peering connection in the Atlas project	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	List of Atlas regions where the container resides	v
@	networking peering watch
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	networking peering rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security
s	customercerts|customer-certs|customerCert|customercert|customer-cert|certs|customerCerts	Manage customer x509 certificates for your project
s	ldap	LDAP operations
@	security customercerts
s	describe	Get the current customer-managed X.509 configuration details for an Atlas project
s	create	Saves a customer-managed X.509 configuration for an Atlas project
s	disable	Disables customer-managed X.509 for a project
@	security customercerts describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security customercerts create
o	--casFile	Path to a PEM file containing one or more CAs for database user authentication	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security customercerts disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security ldap
s	verify	Request verification of an LDAP configuration
s	save	Save an LDAP configuration
s	rm|delete	Delete an LDAP configuration userToDNMapping from an LDAP configuration
s	get	Get an LDAP configuration
@	security ldap verify
s	status	Get the status of an LDAP configuration request
o	--authzQueryTemplate	An LDAP query template that Atlas executes to obtain the LDAP groups to which the authenticated…	v
o	--bindPassword	Password used to authenticate the bindUsername	v
o	--bindUsername	The user distinguished name (DN) that Atlas uses to connect to the LDAP server	v
o	--caCertificate	CA certificate used to verify the identify of the LDAP server	v
o	--hostname	Hostname or IP address of the LDAP server	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--port	Port to which the LDAP server listens to for client connections	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security ldap verify status
s	watch	Watch for an LDAP configuration request to complete
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security ldap verify status watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security ldap save
o	--authenticationEnabled	Specifies whether user authentication with LDAP is enabled	
o	--authorizationEnabled	Specifies whether user authorization with LDAP is enabled	
o	--authzQueryTemplate	An LDAP query template that Atlas executes to obtain the LDAP groups to which the authenticated…	v
o	--bindPassword	Password used to authenticate the bindUsername	v
o	--bindUsername	The user distinguished name (DN) that Atlas uses to connect to the LDAP server	v
o	--caCertificate	CA certificate used to verify the identify of the LDAP server	v
o	--hostname	Hostname or IP address of the LDAP server	v
o	--mappingLdapQuery	An LDAP query formatting template that inserts the authentication name matched by the match regex…	v
o	--mappingMatch	An ECMAScript-formatted regular expression (regex) to match against a provided username	v
o	--mappingSubstitution	An LDAP distinguished name (DN) formatting template that converts the authentication name matched…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--port	Port to which the LDAP server listens to for client connections	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security ldap rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	security ldap get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	integration
s	update|create	Create operations
s	ls|list	List third party integrations
s	rm|delete	Delete a third party integration
s	describe	Get a third party integration
@	integration update
s	new_relic|newRelic|NEW_RELIC	Create or update the New Relic integration
s	ops_genie|opsGenie|OPS_GENIE	Create or update the Ops Genie integration
s	pager_duty|pagerDuty|PAGER_DUTY	Create or update the PagerDuty integration
s	datadog|DATADOG	Create or update the Datadog integration
s	victor_ops|victorOps|VICTOR_OPS	Create or update the VictorOps integrations
s	flowdock|FLOWDOCK	Create or update the Flowdock integration
s	webhook|WEBHOOK	Create or update the Webhook integration
@	integration update new_relic
o	--accountId	Unique identifier of your New Relic account	v
o	--licenceKey	Your License Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--readToken	Your Insights Query Key	v
o	--writeToken	Your Insights Insert Key	v
@	integration update ops_genie
o	--apiKey	API Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Indicates which API URL to use, either US or EU. The integration service will use US by default	v
@	integration update pager_duty
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--serviceKey	Your Service Key	v
@	integration update datadog
o	--apiKey	API Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Indicates which API URL to use, either US or EU. The integration service will use US by default	v
@	integration update victor_ops
o	--apiKey	API Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--routingKey	An optional field for your Routing Key	v
@	integration update flowdock
o	--apiToken	Your API Token	v
o	--flowName	Flowdock Flow name	v
o	--orgName	Your Flowdock organization's name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	integration update webhook
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--secret	An optional field for your webhook secret	v
o	--url	Your webhook URL	v
@	integration ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	integration rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	integration describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	maintenancewindows
s	update	Update the maintenance window
s	rm|delete|clear	Clear the maintenance window
s	defer	Defer the maintenance window
s	get|describe	Get a maintenance window
@	maintenancewindows update
o	--dayOfWeek	Day of the week that you want the maintenance window to start, as a 1-based integer	v
o	--hourOfDay	Hour of the day that you want the maintenance window to start. This parameter uses the 24-hour…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startASAP	Flag that, if specified, indicates to start maintenance immediately upon receiving this request	
@	maintenancewindows rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	maintenancewindows defer
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	maintenancewindows get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdns
s	aw|aws	Manage DNS configuration of an Atlas project’s cluster deployed to AWS
@	customdns aw
s	enable	Enable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	disable	Disable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	get|describe	Describe the custom DNS configuration of an Atlas project’s cluster deployed to AWS
@	customdns aw enable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdns aw disable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	customdns aw get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cloudproviders
s	accessroles|access-roles|accessRole|accessrole|access-role|accessRoles	Manage AWS IAM role access in Atlas
@	cloudproviders accessroles
s	aws	Manage AWS IAM role access in Atlas
s	ls|list	List AWS IAM role access in Atlas
@	cloudproviders accessroles aws
s	create	Create an AWS IAM role
s	authorize	Authorize an AWS IAM role
s	deauthorize	Deauthorize an AWS IAM role
@	cloudproviders accessroles aws create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cloudproviders accessroles aws authorize
o	--iamAssumedRoleArn	Role ARN that Atlas assumes to access your AWS account	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cloudproviders accessroles aws authorize	--iamAssumedRoleArn
t	filepaths
@	cloudproviders accessroles aws deauthorize
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cloudproviders accessroles ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	sl
s	ls|list	Return all serverless instances in the specified project
s	get|describe	Return one serverless instance in the specified project
s	rm|delete	Remove a serverless instance from your project
s	create	Creates one serverless instance in the specified project
s	watch	Monitor the status of serverless instance
@	sl ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	sl get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	sl rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	sl create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Cloud service provider that applies to the provisioned serverless instance	v
o	--region	Human-readable label that identifies the physical location of your MongoDB serverless instance…	v
@	sl watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	livemigrations
s	link	Manage the link-token for your organization
s	validation	Manage a Live Migration validation job for your project
s	create	Create one new migration
s	get|describe	Return one migration job
s	cutover	Start the cutover and confirm when the cutover completes. When the cutover completes, the…
@	livemigrations link
s	create	Create one new link-token
s	rm|delete	Delete one link-token
@	livemigrations link create
o	--accessListIp	IP address access list entries that are associated with the link-token	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	livemigrations link rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	livemigrations validation
s	create	Create one new validation request
s	get|describe	Return one validation job
@	livemigrations validation create
o	--clusterName	Human-readable label that identifies the Atlas destination cluster	v
o	--drop	Flag that indicates whether this process should drop existing collections from the destination…	
o	--migrationHost	List of hosts running the MongoDB Agent that can transfer your MongoDB data from the source (Cloud…	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--sourceCACertificatePath	Path to the CA certificate that signed TLS certificates use to authenticate to the source Cloud…	v
o	--sourceClusterName	Human-readable label that identifies the source Cloud Manager or Ops Manager cluster	v
o	--sourceManagedAuthentication	Flag that indicates whether MongoDB Automation manages authentication to the source Cloud Manager…	
o	--sourcePassword|-p	Password that authenticates the username to the source Cloud Manager or Ops Manager cluster. Omit…	v
o	--sourceProjectId	Unique 24-hexadecimal digit string that identifies the source project	v
o	--sourceSsl	Flag that indicates whether data source has TLS enabled	
o	--sourceUsername|-u	Human-readable label that identifies the SCRAM-SHA user that connects to the source Cloud Manager…	v
@	livemigrations validation get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--validationId	Unique 24-hexadecimal digit string that identifies the validation job	v
@	livemigrations create
o	--clusterName	Human-readable label that identifies the Atlas destination cluster	v
o	--drop	Flag that indicates whether this process should drop existing collections from the destination…	
o	--migrationHost	List of hosts running the MongoDB Agent that can transfer your MongoDB data from the source (Cloud…	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--sourceCACertificatePath	Path to the CA certificate that signed TLS certificates use to authenticate to the source Cloud…	v
o	--sourceClusterName	Human-readable label that identifies the source Cloud Manager or Ops Manager cluster	v
o	--sourceManagedAuthentication	Flag that indicates whether MongoDB Automation manages authentication to the source Cloud Manager…	
o	--sourcePassword|-p	Password that authenticates the username to the source Cloud Manager or Ops Manager cluster. Omit…	v
o	--sourceProjectId	Unique 24-hexadecimal digit string that identifies the source project	v
o	--sourceSsl	Flag that indicates whether data source has TLS enabled	
o	--sourceUsername|-u	Human-readable label that identifies the SCRAM-SHA user that connects to the source Cloud Manager…	v
@	livemigrations get
o	--liveMigrationId	Unique 24-hexadecimal digit string that identifies the live migration job	v
@	livemigrations cutover
o	--liveMigrationId	Unique 24-hexadecimal digit string that identifies the live migration job	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	accesslogs
s	ls|list	Retrieve the access logs of a cluster identified by the cluster's name or hostname
@	accesslogs ls
o	--authResult	Flag that indicates whether to return either successful or failed authentication attempts. When…	v
o	--clusterName	Name of the cluster	v
o	--end	Timestamp in the number of milliseconds that have elapsed, since the UNIX Epoch, for the first…	v
o	--hostname	The fully qualified domain name (FQDN) of the target node that should receive the authentication…	v
o	--ip	IP address that attempted to authenticate with the database. Atlas filters the returned logs to…	v
o	--nLog	Maximum number of log lines to return	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Timestamp in the number of milliseconds that have elapsed, since the UNIX Epoch, for the first…	v
@	completion
s	bash	Generate the autocompletion script for bash
s	zsh	Generate the autocompletion script for zsh
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	help
s	config	Manage your profile to store access settings for your MongoDB deployment
s	auth	Manage the CLI's authentication state
s	quickstart	Create and access an Atlas Cluster
s	project|projects	Project operations
s	organization|orgs|org|organizations	Organization operations
s	globalapikeys|global-api-keys|globalApiKey|globalapikey|global-api-key|globalApiKeys	Global API Keys operations
s	globalaccesslists|global-access-lists|globalAccessList|globalaccesslist|global-access-list|globalWhitelists|globalwhitelists|global-whitelists|globalWhitelist|globalwhitelist|global-whitelist|globalAccessLists	Manage IP access list for Global API Key
s	user|users	Users operations
s	team|teams	Teams operations
s	cluster|clusters	Manage clusters for your project
s	dbuser|dbusers	Manage database users for your project
s	customdbroles|custom-db-roles|customDbRole|customdbrole|custom-db-role|customDBRoles|customDbRoles	Manage custom database roles for your project
s	accesslists|access-lists|accessList|accesslist|access-list|whitelists|whitelist|accessLists	Manage the access IP access list for your project
s	datalakes|data-lakes|dataLake|datalake|data-lake|dataLakes	Manage Atlas Data Lakes for your project
s	alert|alerts	Manage alerts for your project
s	backup|backups	Manage cloud backups for your project
s	event|events	Manage events for your organization or project
s	metric|measurements|measurement|metrics	Get metrics on the MongoDB process
s	performanceadvisor|performance-advisor|performanceAdvisor	Performance Advisor operations
s	log|logs	Download host logs for your project
s	process|processes	Manage MongoDB processes for your project
s	privateendpoints|private-endpoints|privateEndpoint|privateendpoint|private-endpoint|privateEndpoints	Manage Atlas private endpoints
s	networking	Networking operations
s	security	Manage security configuration for your project
s	integration|integrations	Third party integration operations
s	maintenancewindows|maintenance-windows|maintenanceWindow|maintenancewindow|maintenance-window|maintenanceWindows	Manage Atlas maintenance windows
s	customdns|custom-dns|customDn|customdn|custom-dn|customDns	Manage DNS configuration of Atlas project’s clusters deployed to AWS
s	cloudproviders|cloud-providers|cloudProvider|cloudprovider|cloud-provider|cloudProviders	Manage unified IAM role access in Atlas
s	sl|serverless	Manage serverless instances for your project
s	livemigrations|live-migrations|liveMigration|livemigration|live-migration|lm|liveMigrations	Manage a Live Migration to Atlas for your organization
s	accesslogs|access-logs|accessLog|accesslog|access-log|accessLogs	Manage the access logs of a cluster
s	completion	Generate the autocompletion script for the specified shell
@	help config
s	init	Configure a profile to store access settings for your MongoDB deployment
s	set	Configure specific properties of a profile
s	ls|list	List available profiles
s	get|describe	Return a specific profile
s	mv|rename	Rename a profile
s	rm|delete	Delete a profile
@	help config init
@	help config set
@	help config ls
@	help config get
@	help config mv
@	help config rm
@	help auth
s	login	Authenticate with MongoDB Atlas
s	whoami	Verifies and displays information about your authentication state
s	logout	Log out of the CLI
@	help auth login
@	help auth whoami
@	help auth logout
@	help quickstart
@	help project
s	ls|list	List projects
s	create	Create a project
s	rm|delete	Delete a project
s	show|get|describe	Describe a project
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Manage API Keys for your project
s	user|users	Manage users for a project
s	team|teams	Teams operations
s	invitation|invitations	Invitation operations
@	help project ls
@	help project create
@	help project rm
@	help project show
@	help project apikeys
s	ls|list	List API Keys for your project
s	create	Create an API Key for your project
s	rm|delete	Delete an API Key for your project
s	update|assign	Assign an API Key to a project
@	help project apikeys ls
@	help project apikeys create
@	help project apikeys rm
@	help project apikeys update
@	help project user
s	ls|list	List all users for a project
s	rm|delete	Delete user from a project
@	help project user ls
@	help project user rm
@	help project team
s	ls|list	Get all teams in a project
s	add	Add team to a project
s	rm|delete	Delete team from a project
s	updates|update	Update roles for a team in a project
@	help project team ls
@	help project team add
@	help project team rm
@	help project team updates
@	help project invitation
s	ls|list	Retrieves all pending invitations to the specified project
s	get|describe	Retrieve details for one pending invitation to the specified project
s	rm|delete	Deletes one pending invitation to the specified project
s	create|invite	Invites one user to the project that you specify
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
@	help project invitation ls
@	help project invitation get
@	help project invitation rm
@	help project invitation create
@	help project invitation updates
@	help organization
s	ls|list	List organizations
s	show|describe	Describe an organizations
s	create	Create an organization
s	rm|delete	Delete an organization
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Organization API Keys operations
s	user|users	Users operations
s	invitation|invitations	Invitation operations
@	help organization ls
@	help organization show
@	help organization create
@	help organization rm
@	help organization apikeys
s	ls|list	List API Keys for your organization
s	show|describe	Get a specific Organization API Key
s	updates|assign	Update an Organization API Key
s	create	Create an Organization API Key
s	rm|delete	Delete an Organization API Key
s	accesslists|access-lists|accessList|accesslist|access-list|whitelists|whitelist|accessLists	Manage the IP access list for your API Key
@	help organization apikeys ls
@	help organization apikeys show
@	help organization apikeys updates
@	help organization apikeys create
@	help organization apikeys rm
@	help organization apikeys accesslists
s	ls|list	List IP access list entries for your API Key
s	create	Create an IP access list for your API Key
s	rm|delete	Delete an IP access list from your API Key
@	help organization apikeys accesslists ls
@	help organization apikeys accesslists create
@	help organization apikeys accesslists rm
@	help organization user
s	ls|list	List users in a organization
@	help organization user ls
@	help organization invitation
s	ls|list	Retrieves all pending invitations to the specified organization
s	get|describe	Retrieve details for one pending invitation to the specified organization
s	rm|delete	Deletes one pending invitation to the specified organization
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
s	create|invite	Invites one user to the organization that you specify
@	help organization invitation ls
@	help organization invitation get
@	help organization invitation rm
@	help organization invitation updates
@	help organization invitation create
@	help globalapikeys
s	ls|list	List Global API Keys
s	show|describe	Get a specific Global API Key
s	create	Create a Global API Key
s	update	Update a Global API Key
s	rm|delete	Delete a Global API Key
@	help globalapikeys ls
@	help globalapikeys show
@	help globalapikeys create
@	help globalapikeys update
@	help globalapikeys rm
@	help globalaccesslists
s	ls|list	List Atlas IP access list entries for Global API Key
s	show|describe	Return one Global IP access list entry
s	create	Create an IP access list for Global API Key
s	rm|delete	Delete an IP access list from Global API Key
@	help globalaccesslists ls
@	help globalaccesslists show
@	help globalaccesslists create
@	help globalaccesslists rm
@	help user
s	invite	Invite a user
s	get|describe	Get a user by username or id
s	rm|delete	Delete an Ops Manager user
@	help user invite
@	help user get
@	help user rm
@	help team
s	ls|list	Get all teams in an organization
s	get|describe	Get a team in an organization
s	create	Create a team in an organization
s	user|users	Users operations
s	rm|delete	Delete a team from an organization
@	help team ls
@	help team get
@	help team create
@	help team user
s	ls|list	List users of a team
s	add	Add a user to a team
s	rm|delete	Delete user from a team
@	help team user ls
@	help team user add
@	help team user rm
@	help team rm
@	help cluster
s	ls|list	List clusters for your project
s	get|describe	Describe a cluster
s	create	Create one cluster in the specified project
s	watch	Watch for a cluster to be available
s	update	Update a MongoDB cluster
s	pause	Pause a running MongoDB cluster in Atlas
s	start	Start a paused MongoDB cluster in Atlas
s	rm|delete	Delete a cluster from your project
s	loadSampleData	Load sample data into a MongoDB cluster in Atlas
s	index|indexes	Manage cluster rolling indexes for your project
s	fts|search	Manage Atlas Search for your cluster
s	onlinearchives|online-archives|onlineArchive|onlinearchive|online-archive|onlineArchives	Manage online archives for your cluster
s	connectionstrings|connection-strings|connectionString|connectionstring|connection-string|cs|connectionStrings	Manage MongoDB cluster connection string
@	help cluster ls
@	help cluster get
@	help cluster create
@	help cluster watch
@	help cluster update
@	help cluster pause
@	help cluster start
@	help cluster rm
@	help cluster loadSampleData
@	help cluster index
s	create	Create a rolling index for your MongoDB cluster
@	help cluster index create
@	help cluster fts
s	index|indexes	Manage Atlas Search indexes for your cluster
@	help cluster fts index
s	ls|list	List Atlas search indexes for a cluster
s	create	Create a search index for a cluster
s	describe	Describe a search index for a cluster
s	update	Update a search index for a cluster
s	rm|delete	Delete a search index from a cluster
@	help cluster fts index ls
@	help cluster fts index create
@	help cluster fts index describe
@	help cluster fts index update
@	help cluster fts index rm
@	help cluster onlinearchives
s	ls|list	List online archives for a cluster
s	describe	Describe an online archive for a cluster
s	create	Create an online archive for a cluster
s	update	Update an online archive for a cluster
s	start	Start a paused online archive from a cluster
s	pause	Pause an online archive from a cluster
s	rm|delete	Delete an online archive from a cluster
s	watch	Watch for an archive to be available
@	help cluster onlinearchives ls
@	help cluster onlinearchives describe
@	help cluster onlinearchives create
@	help cluster onlinearchives update
@	help cluster onlinearchives start
@	help cluster onlinearchives pause
@	help cluster onlinearchives rm
@	help cluster onlinearchives watch
@	help cluster connectionstrings
s	get|describe	Retrieve the SRV connection string of your MongoDB cluster
@	help cluster connectionstrings get
@	help dbuser
s	ls|list	List Atlas database users for your project
s	get|describe	Return a single Atlas database user for your project
s	create	Create a database user for your project
s	rm|delete	Delete a database user for your project
s	update	Update a database user for your project
s	cert|certs	Manage Atlas x509 certificates for your database users
@	help dbuser ls
@	help dbuser get
@	help dbuser create
@	help dbuser rm
@	help dbuser update
@	help dbuser cert
s	ls|list	List of all Atlas-managed, unexpired certificates for a database user
s	create	Create a new Atlas-managed X.509 certificate for the specified database user
@	help dbuser cert ls
@	help dbuser cert create
@	help customdbroles
s	create	Create a custom database role for your project
s	get|describe	Return a single custom database role for your project
s	ls|list	List custom database roles for your project
s	rm|delete	Delete a custom database role for your project
s	update	Update a custom database role for your project
@	help customdbroles create
@	help customdbroles get
@	help customdbroles ls
@	help customdbroles rm
@	help customdbroles update
@	help accesslists
s	get|describe	Describe an IP access list entry
s	ls|list	List Atlas IP access list entries for your project
s	create	Create an IP access list for your project
s	rm|delete	Delete an IP access list from your project
@	help accesslists get
@	help accesslists ls
@	help accesslists create
@	help accesslists rm
@	help datalakes
s	ls|list	List Atlas Data Lakes for your project
s	describe	Return a specific data lake
s	create	Create a new data lake for your project
s	rm|delete	Delete a data lake from your project
s	update	Update a data lake for your project
@	help datalakes ls
@	help datalakes describe
@	help datalakes create
@	help datalakes rm
@	help datalakes update
@	help alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	help alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	help alert config create
@	help alert config ls
@	help alert config rm
@	help alert config field
s	types|type	Lists available field types for your alert configurations
@	help alert config field types
@	help alert config update
@	help alert get
@	help alert ls
@	help alert ack
@	help alert unack
@	help alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	help alert global ls
@	help backup
s	snapshot|snapshots	Manage cloud backup snapshots for your project
s	restore|restores	Manage cloud backup restore jobs for your project
@	help backup snapshot
s	ls|list	List cloud backup snapshots for your project and cluster
s	take|create	Create a backup snapshot for your project and cluster
s	describe	Get a specific snapshot for your project
s	watch	Watch for a snapshot to be available
s	rm|delete	Delete a backup snapshot
@	help backup snapshot ls
@	help backup snapshot take
@	help backup snapshot describe
@	help backup snapshot watch
@	help backup snapshot rm
@	help backup restore
s	ls|list	List cloud backup restore jobs for your project and cluster
s	start	Start a restore job for your project and cluster
@	help backup restore ls
@	help backup restore start
@	help event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	help event ls
@	help event organization
s	ls|list	Return all events for an organization
@	help event organization ls
@	help event project
s	ls|list	Return all events for a project
@	help event project ls
@	help metric
s	process|processes	Get MongoDB process metrics for a given host
s	disk|disks	List available disks or disk metrics for a given host
s	database|databases	List available databases or database metrics for a given host
@	help metric process
@	help metric disk
s	ls|list	List available disks or disk partitions for a given host
s	describe	Describe disk partition metrics for a disk partition on a specified host
@	help metric disk ls
@	help metric disk describe
@	help metric database
s	ls|list	List available databases or database metrics for a given host
s	describe	Describe database metrics for a database on a specific host
@	help metric database ls
@	help metric database describe
@	help performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	help performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	help performanceadvisor namespace ls
@	help performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	help performanceadvisor slowquerylogs ls
@	help performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	help performanceadvisor suggestedindexes ls
@	help performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	help performanceadvisor slowOT ls
@	help performanceadvisor slowOT disable
@	help log
s	download	Download a host mongodb logs
@	help log download
@	help process
s	ls|list	List MongoDB processes for your project
@	help process ls
@	help privateendpoints
s	ls|list	List Atlas Private Endpoints for your project
s	get|describe	Return a specific Private Endpoints for your project
s	create	Create a new private endpoint for your project
s	rm|delete	Delete a private endpoint from your project
s	watch	Watch for a private endpoint to be available
s	interface|interfaces	Manage Atlas private endpoint interfaces
s	aws	Manage AWS Private Endpoints
s	azure	Manage Azure Private Endpoints
s	gcp	Manage GCP private endpoints
s	regionalmodes|regional-modes|regionalMode|regionalmode|regional-mode|regionalModes	Manage regionalized private endpoint setting for your Atlas project
s	datalakes|data-lakes|dataLake|datalake|data-lake|dataLakes	Manage Data Lake private endpoints
s	onlinearchive|online-archive|onlineArchive	Manage Online Archive private endpoints
@	help privateendpoints ls
@	help privateendpoints get
@	help privateendpoints create
@	help privateendpoints rm
@	help privateendpoints watch
@	help privateendpoints interface
s	add|create	Add a new interface to a private endpoint
s	get|describe	Return a specific private endpoint interface for your project
s	rm|delete	Delete a private endpoint interface from your project
@	help privateendpoints interface add
@	help privateendpoints interface get
@	help privateendpoints interface rm
@	help privateendpoints aws
s	ls|list	List AWS Private Endpoints for your project
s	get|describe	Return a specific AWS Private Endpoints for your project
s	create	Create a new AWS Private Endpoint for your project
s	rm|delete	Delete a specific AWS Private Endpoint for your project
s	watch	Watch for a specific AWS Private Endpoint to be available
s	interface|interfaces	Manage Atlas AWS private endpoint interfaces
@	help privateendpoints aws ls
@	help privateendpoints aws get
@	help privateendpoints aws create
@	help privateendpoints aws rm
@	help privateendpoints aws watch
@	help privateendpoints aws interface
s	add|create	Add a new interface to a AWS private endpoint
s	get|describe	Return a specific AWS private endpoint interface for your project
s	rm|delete	Delete a specific AWS private endpoint interface and the related endpoint service for your project
@	help privateendpoints aws interface add
@	help privateendpoints aws interface get
@	help privateendpoints aws interface rm
@	help privateendpoints azure
s	ls|list	List Azure Private Endpoints for your project
s	get|describe	Return a specific Azure Private Endpoints for your project
s	create	Create a new Azure Private Endpoint for your project
s	rm|delete	Delete a specific Azure Private Endpoint for your project
s	watch	Watch for a specific Azure Private Endpoint to be available
s	interface|interfaces	Manage Atlas Azure private endpoint interfaces
@	help privateendpoints azure ls
@	help privateendpoints azure get
@	help privateendpoints azure create
@	help privateendpoints azure rm
@	help privateendpoints azure watch
@	help privateendpoints azure interface
s	add|create	Add a new Azure interface to a private endpoint
s	get|describe	Return a specific Azure private endpoint interface for your project
s	rm|delete	Delete a specific Azure private endpoint interface and related service for your project
@	help privateendpoints azure interface add
@	help privateendpoints azure interface get
@	help privateendpoints azure interface rm
@	help privateendpoints gcp
s	create	Create a new GCP private endpoint for your project
s	rm|delete	Delete a GCP private endpoint for your project
s	ls|list	List GCP private endpoints for your project
s	get|describe	Return a specific GCP private endpoint for your project
s	watch	Watch the specified GCP private endpoint to detect changes in the endpoint's state
s	interface|interfaces	Manage Atlas GCP private endpoint interfaces
@	help privateendpoints gcp create
@	help privateendpoints gcp rm
@	help privateendpoints gcp ls
@	help privateendpoints gcp get
@	help privateendpoints gcp watch
@	help privateendpoints gcp interface
s	get|describe	Return a specific GCP private endpoint interface for your project
s	rm|delete	Delete a specific GCP private endpoint interface for your project
s	add|create	Create a GCP private endpoint interface
@	help privateendpoints gcp interface get
@	help privateendpoints gcp interface rm
@	help privateendpoints gcp interface add
@	help privateendpoints regionalmodes
s	enable	Enable the regionalized private endpoint setting for your Atlas project
s	disable	Disable the regionalized private endpoint setting for your Atlas project
s	get|describe	Get the regionalized private endpoint setting for your Atlas project
@	help privateendpoints regionalmodes enable
@	help privateendpoints regionalmodes disable
@	help privateendpoints regionalmodes get
@	help privateendpoints datalakes
s	aws	Manage AWS private endpoints
@	help privateendpoints datalakes aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	help privateendpoints datalakes aws create
@	help privateendpoints datalakes aws ls
@	help privateendpoints datalakes aws get
@	help privateendpoints datalakes aws rm
@	help privateendpoints onlinearchive
s	aws	Manage AWS private endpoints
@	help privateendpoints onlinearchive aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	help privateendpoints onlinearchive aws create
@	help privateendpoints onlinearchive aws ls
@	help privateendpoints onlinearchive aws get
@	help privateendpoints onlinearchive aws rm
@	help networking
s	container|containers	Manage Network Peering containers
s	peering	Manage Network Peering connections
@	help networking container
s	ls|list	List network peering containers in an Atlas project
s	rm|delete	Remove one network peering container in an Atlas project
@	help networking container ls
@	help networking container rm
@	help networking peering
s	ls|list	Retrieve details for all network peering connections in one Atlas project
s	create	Create a connection with AWS, Azure and Google Cloud
s	watch	Watch for a peering connection to be available
s	rm|delete	Delete a peering connection from an Atlas project
@	help networking peering ls
@	help networking peering create
s	azure	Create a connection with Azure
s	aws	Create a connection with AWS
s	gcp	Create a connection with GCP
@	help networking peering create azure
@	help networking peering create aws
@	help networking peering create gcp
@	help networking peering watch
@	help networking peering rm
@	help security
s	customercerts|customer-certs|customerCert|customercert|customer-cert|certs|customerCerts	Manage customer x509 certificates for your project
s	ldap	LDAP operations
@	help security customercerts
s	describe	Get the current customer-managed X.509 configuration details for an Atlas project
s	create	Saves a customer-managed X.509 configuration for an Atlas project
s	disable	Disables customer-managed X.509 for a project
@	help security customercerts describe
@	help security customercerts create
@	help security customercerts disable
@	help security ldap
s	verify	Request verification of an LDAP configuration
s	save	Save an LDAP configuration
s	rm|delete	Delete an LDAP configuration userToDNMapping from an LDAP configuration
s	get	Get an LDAP configuration
@	help security ldap verify
s	status	Get the status of an LDAP configuration request
@	help security ldap verify status
s	watch	Watch for an LDAP configuration request to complete
@	help security ldap verify status watch
@	help security ldap save
@	help security ldap rm
@	help security ldap get
@	help integration
s	update|create	Create operations
s	ls|list	List third party integrations
s	rm|delete	Delete a third party integration
s	describe	Get a third party integration
@	help integration update
s	new_relic|newRelic|NEW_RELIC	Create or update the New Relic integration
s	ops_genie|opsGenie|OPS_GENIE	Create or update the Ops Genie integration
s	pager_duty|pagerDuty|PAGER_DUTY	Create or update the PagerDuty integration
s	datadog|DATADOG	Create or update the Datadog integration
s	victor_ops|victorOps|VICTOR_OPS	Create or update the VictorOps integrations
s	flowdock|FLOWDOCK	Create or update the Flowdock integration
s	webhook|WEBHOOK	Create or update the Webhook integration
@	help integration update new_relic
@	help integration update ops_genie
@	help integration update pager_duty
@	help integration update datadog
@	help integration update victor_ops
@	help integration update flowdock
@	help integration update webhook
@	help integration ls
@	help integration rm
@	help integration describe
@	help maintenancewindows
s	update	Update the maintenance window
s	rm|delete|clear	Clear the maintenance window
s	defer	Defer the maintenance window
s	get|describe	Get a maintenance window
@	help maintenancewindows update
@	help maintenancewindows rm
@	help maintenancewindows defer
@	help maintenancewindows get
@	help customdns
s	aw|aws	Manage DNS configuration of an Atlas project’s cluster deployed to AWS
@	help customdns aw
s	enable	Enable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	disable	Disable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	get|describe	Describe the custom DNS configuration of an Atlas project’s cluster deployed to AWS
@	help customdns aw enable
@	help customdns aw disable
@	help customdns aw get
@	help cloudproviders
s	accessroles|access-roles|accessRole|accessrole|access-role|accessRoles	Manage AWS IAM role access in Atlas
@	help cloudproviders accessroles
s	aws	Manage AWS IAM role access in Atlas
s	ls|list	List AWS IAM role access in Atlas
@	help cloudproviders accessroles aws
s	create	Create an AWS IAM role
s	authorize	Authorize an AWS IAM role
s	deauthorize	Deauthorize an AWS IAM role
@	help cloudproviders accessroles aws create
@	help cloudproviders accessroles aws authorize
@	help cloudproviders accessroles aws deauthorize
@	help cloudproviders accessroles ls
@	help sl
s	ls|list	Return all serverless instances in the specified project
s	get|describe	Return one serverless instance in the specified project
s	rm|delete	Remove a serverless instance from your project
s	create	Creates one serverless instance in the specified project
s	watch	Monitor the status of serverless instance
@	help sl ls
@	help sl get
@	help sl rm
@	help sl create
@	help sl watch
@	help livemigrations
s	link	Manage the link-token for your organization
s	validation	Manage a Live Migration validation job for your project
s	create	Create one new migration
s	get|describe	Return one migration job
s	cutover	Start the cutover and confirm when the cutover completes. When the cutover completes, the…
@	help livemigrations link
s	create	Create one new link-token
s	rm|delete	Delete one link-token
@	help livemigrations link create
@	help livemigrations link rm
@	help livemigrations validation
s	create	Create one new validation request
s	get|describe	Return one validation job
@	help livemigrations validation create
@	help livemigrations validation get
@	help livemigrations create
@	help livemigrations get
@	help livemigrations cutover
@	help accesslogs
s	ls|list	Retrieve the access logs of a cluster identified by the cluster's name or hostname
@	help accesslogs ls
@	help completion
s	bash	Generate the autocompletion script for bash
s	zsh	Generate the autocompletion script for zsh
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
@	help completion bash
@	help completion zsh
@	help completion fish
@	help completion powershell

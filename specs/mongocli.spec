@	
s	config	Configure a profile to store access settings for your MongoDB deployment
s	atlas	MongoDB Atlas operations
s	cm|cloud-manager	MongoDB Cloud Manager operations
s	om|ops-manager	MongoDB Ops Manager operations
s	iam	Organization and projects operations
s	auth	Manage the CLI's authentication state
s	completion	Generate the autocompletion script for the specified shell
s	help	Help about any command
o	--profile|-P	Profile to use from your configuration file	vp
o	--help|-h	Display help	p
@	config
s	set	Configure specific properties of a profile
s	ls|list	List available profiles
s	get|describe	Return a specific profile
s	mv|rename	Rename a profile
s	rm|delete	Delete a profile
o	--service	Type of MongoDB service. Valid values are cloud, cloudgov, cloud-manager, or ops-manager	v
@	config set
@	config ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	config get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	config mv
@	config rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	atlas
s	quickstart	Create and access an Atlas Cluster
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
@	atlas quickstart
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
@	atlas cluster
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
@	atlas cluster ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster create
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
=	atlas cluster create	--file
t	filepaths
@	atlas cluster watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster update
o	--diskSizeGB	Capacity, in gigabytes, of the host's root volume	v
o	--file|-f	File name to use, optional file with a json cluster configuration	v
o	--mdbVersion	MongoDB version of the cluster to deploy	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--tier	Tier for each data-bearing server in the cluster	v
=	atlas cluster update	--file
t	filepaths
@	atlas cluster pause
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster start
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster loadSampleData
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster index
s	create	Create a rolling index for your MongoDB cluster
@	atlas cluster index create
o	--clusterName	Name of the cluster	v
o	--collection	Collection name	v
o	--db	Database name	v
o	--key	Field to be indexed and the type of index in the following format: field:type	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--sparse	Flag that indicates whether Atlas should create a sparse index	
@	atlas cluster fts
s	index|indexes	Manage Atlas Search indexes for your cluster
@	atlas cluster fts index
s	ls|list	List Atlas search indexes for a cluster
s	create	Create a search index for a cluster
s	describe	Describe a search index for a cluster
s	update	Update a search index for a cluster
s	rm|delete	Delete a search index from a cluster
@	atlas cluster fts index ls
o	--clusterName	Name of the cluster	v
o	--collection	Collection name	v
o	--db	Database name	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster fts index create
o	--clusterName	Name of the cluster	v
o	--file|-f	File name to use, file with a json index configuration	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	atlas cluster fts index create	--file
t	filepaths
@	atlas cluster fts index describe
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster fts index update
o	--clusterName	Name of the cluster	v
o	--file|-f	File name to use, file with a json index configuration	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	atlas cluster fts index update	--file
t	filepaths
@	atlas cluster fts index rm
o	--clusterName	Name of the cluster	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives
s	ls|list	List online archives for a cluster
s	describe	Describe an online archive for a cluster
s	create	Create an online archive for a cluster
s	update	Update an online archive for a cluster
s	start	Start a paused online archive from a cluster
s	pause	Pause an online archive from a cluster
s	rm|delete	Delete an online archive from a cluster
s	watch	Watch for an archive to be available
@	atlas cluster onlinearchives ls
o	--clusterName	Name of the cluster	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives describe
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives create
o	--archiveAfter	Number of days that specifies the age limit for the data in the live Atlas cluster	v
o	--clusterName	Name of the cluster	v
o	--collection	Collection name	v
o	--dateField	Name of an already indexed date field from the documents	v
o	--dateFormat	Date format for the date field. Valid values are ISODATE, EPOCH_SECONDS, EPOCH_MILLIS, or…	v
o	--db	Database name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--partition	Fields to use to partition data. You can specify up to two frequently queried fields to use for…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives update
o	--archiveAfter	Number of days that specifies the age limit for the data in the live Atlas cluster	v
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives start
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives pause
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives rm
o	--clusterName	Name of the cluster	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster onlinearchives watch
o	--clusterName	Name of the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cluster connectionstrings
s	get|describe	Retrieve the SRV connection string of your MongoDB cluster
@	atlas cluster connectionstrings get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	When set to 'private', retrieves the connection string for the network peering endpoint	v
@	atlas dbuser
s	ls|list	List Atlas database users for your project
s	get|describe	Return a single Atlas database user for your project
s	create	Create a database user for your project
s	rm|delete	Delete a database user for your project
s	update	Update a database user for your project
s	cert|certs	Manage Atlas x509 certificates for your database users
@	atlas dbuser ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas dbuser get
o	--authDB	Authentication database name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas dbuser create
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
@	atlas dbuser rm
o	--authDB	Authentication database name	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas dbuser update
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password|-p	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles and the databases or collections on which the roles apply	v
o	--scope	Array of clusters and Atlas Data Lakes that this user has access to	v
o	--username|-u	Username for authenticating to MongoDB	v
@	atlas dbuser cert
s	ls|list	List of all Atlas-managed, unexpired certificates for a database user
s	create	Create a new Atlas-managed X.509 certificate for the specified database user
@	atlas dbuser cert ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas dbuser cert create
o	--monthsUntilExpiration	Number of months that the certificate is valid for	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--username	Username of a database user	v
@	atlas customdbroles
s	create	Create a custom database role for your project
s	get|describe	Return a single custom database role for your project
s	ls|list	List custom database roles for your project
s	rm|delete	Delete a custom database role for your project
s	update	Update a custom database role for your project
@	atlas customdbroles create
o	--inheritedRole	List of inherited roles and the database on which the role is granted	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privilege	List of actions per database and collection. If no database or collections are provided, cluster…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdbroles get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdbroles ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdbroles rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdbroles update
o	--append	The input action and inheritedRoles that will be appended to the existing role	
o	--inheritedRole	List of inherited roles and the database on which the role is granted	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privilege	List of actions per database and collection. If no database or collections are provided, cluster…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas accesslists
s	get|describe	Describe an IP access list entry
s	ls|list	List Atlas IP access list entries for your project
s	create	Create an IP access list for your project
s	rm|delete	Delete an IP access list from your project
@	atlas accesslists get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas accesslists ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas accesslists create
o	--comment	Optional description or comment for the entry	v
o	--currentIp	Flag that indicates whether to use the IP Address from the host that is currently executing the…	
o	--deleteAfter	ISO-8601-formatted UTC date after which Atlas removes the value from the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of access list entry. Valid values are cidrBlock, ipAddress, or awsSecurityGroup	v
@	atlas accesslists rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas datalakes
s	ls|list	List Atlas Data Lakes for your project
s	describe	Return a specific data lake
s	create	Create a new data lake for your project
s	rm|delete	Delete a data lake from your project
s	update	Update a data lake for your project
@	atlas datalakes ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas datalakes describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas datalakes create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	Amazon Resource Name (ARN) of the role which Atlas Data Lake uses for accessing the data stores	v
o	--testBucket	Name of an Amazon S3 data bucket which Atlas Data Lake uses to validate the provided role	v
@	atlas datalakes rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas datalakes update
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Name of the region to which Atlas Data Lake routes client connections for data processing	v
o	--role	Amazon Resource Name (ARN) of the role which Atlas Data Lake uses for accessing the data stores	v
o	--testBucket	Name of an Amazon S3 data bucket which Atlas Data Lake uses to validate the provided role	v
@	atlas alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	atlas alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	atlas alert config create
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
@	atlas alert config ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas alert config rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas alert config field
s	types|type	Lists available field types for your alert configurations
@	atlas alert config field types
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	atlas alert config update
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
@	atlas alert get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas alert ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	atlas alert ack
o	--comment	Optional description or comment for the entry	v
o	--forever|-F	Acknowledges an alert 'forever'	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--until	Time, in ISO 8601 format, until which the alert has been acknowledged. mongocli returns this value…	v
@	atlas alert unack
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	atlas alert global ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	atlas backup
s	snapshot|snapshots	Manage cloud backup snapshots for your project
s	restore|restores	Manage cloud backup restore jobs for your project
@	atlas backup snapshot
s	ls|list	List cloud backup snapshots for your project and cluster
s	take|create	Create a backup snapshot for your project and cluster
s	describe	Get a specific snapshot for your project
s	watch	Watch for a snapshot to be available
s	rm|delete	Delete a backup snapshot
@	atlas backup snapshot ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas backup snapshot take
o	--desc	Description of the on-demand snapshot	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--retention	Cloud provider region in which you want to create the private endpoint connection	v
@	atlas backup snapshot describe
o	--clusterName	Name of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas backup snapshot watch
o	--clusterName	Name of the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas backup snapshot rm
o	--clusterName	Name of the cluster	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas backup restore
s	ls|list	List cloud backup restore jobs for your project and cluster
s	start	Start a restore job for your project and cluster
@	atlas backup restore ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas backup restore start
o	--clusterName	Name of the cluster	v
o	--oplogInc	32-bit incrementing ordinal that represents operations within a given second. When paired with…	v
o	--oplogTs	Oplog timestamp given as a timestamp in the number of seconds that have elapsed since the UNIX…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pointInTimeUTCMillis	Timestamp in the number of milliseconds that have elapsed since the UNIX epoch that represents the…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--snapshotId	Unique identifier of the snapshot to restore	v
o	--targetClusterName	Name of the target cluster. For use only with automated restore jobs	v
o	--targetProjectId	Unique identifier of the project that contains the destination cluster for the restore job	v
@	atlas event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	atlas event ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	atlas event organization
s	ls|list	Return all events for an organization
@	atlas event organization ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--type	Type of the event that triggered the alert	v
@	atlas event project
s	ls|list	Return all events for a project
@	atlas event project ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	atlas metric
s	process|processes	Get MongoDB process metrics for a given host
s	disk|disks	List available disks or disk metrics for a given host
s	database|databases	List available databases or database metrics for a given host
@	atlas metric process
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	atlas metric disk
s	ls|list	List available disks or disk partitions for a given host
s	describe	Describe disk partition metrics for a disk partition on a specified host
@	atlas metric disk ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas metric disk describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	atlas metric database
s	ls|list	List available databases or database metrics for a given host
s	describe	Describe database metrics for a database on a specific host
@	atlas metric database ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas metric database describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	atlas performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	atlas performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	atlas performanceadvisor namespace ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	atlas performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	atlas performanceadvisor slowquerylogs ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nLog	Maximum number of log lines to return	v
o	--namespaces	Namespaces from which to retrieve suggested slow query logs	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	atlas performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	atlas performanceadvisor suggestedindexes ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nExamples	Maximum number of example queries to provide that will be improved by a suggested index	v
o	--nIndexes	Maximum number of indexes to suggest	v
o	--namespaces	Namespaces from which to retrieve suggested indexes	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	atlas performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	atlas performanceadvisor slowOT ls
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas performanceadvisor slowOT disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas log
s	download	Download a host mongodb logs
@	atlas log download
o	--end	End of the period, in UNIX Epoch format, until which to retrieve logs	v
o	--force	Overwrites the destination file	
o	--out	Optional output file name. Uses the log name if the output file's name is not specified	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the date and time, in UNIX Epoch format, from which to retrieve logs	v
=	atlas log download	--out
t	filepaths
@	atlas process
s	ls|list	List MongoDB processes for your project
@	atlas process ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints
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
@	atlas privateendpoints ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of the cloud provider you want to create the private endpoint connection for	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	atlas privateendpoints rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of the cloud provider you want to create the private endpoint connection for	v
@	atlas privateendpoints interface
s	add|create	Add a new interface to a private endpoint
s	get|describe	Return a specific private endpoint interface for your project
s	rm|delete	Delete a private endpoint interface from your project
@	atlas privateendpoints interface add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints interface get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints interface rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws
s	ls|list	List AWS Private Endpoints for your project
s	get|describe	Return a specific AWS Private Endpoints for your project
s	create	Create a new AWS Private Endpoint for your project
s	rm|delete	Delete a specific AWS Private Endpoint for your project
s	watch	Watch for a specific AWS Private Endpoint to be available
s	interface|interfaces	Manage Atlas AWS private endpoint interfaces
@	atlas privateendpoints aws ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	atlas privateendpoints aws rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws interface
s	add|create	Add a new interface to a AWS private endpoint
s	get|describe	Return a specific AWS private endpoint interface for your project
s	rm|delete	Delete a specific AWS private endpoint interface and the related endpoint service for your project
@	atlas privateendpoints aws interface add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws interface get
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints aws interface rm
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure
s	ls|list	List Azure Private Endpoints for your project
s	get|describe	Return a specific Azure Private Endpoints for your project
s	create	Create a new Azure Private Endpoint for your project
s	rm|delete	Delete a specific Azure Private Endpoint for your project
s	watch	Watch for a specific Azure Private Endpoint to be available
s	interface|interfaces	Manage Atlas Azure private endpoint interfaces
@	atlas privateendpoints azure ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	atlas privateendpoints azure rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure interface
s	add|create	Add a new Azure interface to a private endpoint
s	get|describe	Return a specific Azure private endpoint interface for your project
s	rm|delete	Delete a specific Azure private endpoint interface and related service for your project
@	atlas privateendpoints azure interface add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the Azure private endpoint resource	v
o	--privateEndpointIpAddress	Private IP address of the private endpoint network interface you created in your Azure VNet	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure interface get
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints azure interface rm
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp
s	create	Create a new GCP private endpoint for your project
s	rm|delete	Delete a GCP private endpoint for your project
s	ls|list	List GCP private endpoints for your project
s	get|describe	Return a specific GCP private endpoint for your project
s	watch	Watch the specified GCP private endpoint to detect changes in the endpoint's state
s	interface|interfaces	Manage Atlas GCP private endpoint interfaces
@	atlas privateendpoints gcp create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Cloud provider region in which you want to create the private endpoint connection	v
@	atlas privateendpoints gcp rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp interface
s	get|describe	Return a specific GCP private endpoint interface for your project
s	rm|delete	Delete a specific GCP private endpoint interface for your project
s	add|create	Create a GCP private endpoint interface
@	atlas privateendpoints gcp interface get
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp interface rm
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints gcp interface add
o	--endpoint	List of GCP endpoints in the group separated by commas, such as…	v
o	--endpointServiceId	Unique identifier of the private endpoint service for which you want to retrieve a private endpoint	v
o	--gcpProjectId	Unique identifier of the GCP project in which the network peer resides	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints regionalmodes
s	enable	Enable the regionalized private endpoint setting for your Atlas project
s	disable	Disable the regionalized private endpoint setting for your Atlas project
s	get|describe	Get the regionalized private endpoint setting for your Atlas project
@	atlas privateendpoints regionalmodes enable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints regionalmodes disable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints regionalmodes get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints datalakes
s	aws	Manage AWS private endpoints
@	atlas privateendpoints datalakes aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	atlas privateendpoints datalakes aws create
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints datalakes aws ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints datalakes aws get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints datalakes aws rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints onlinearchive
s	aws	Manage AWS private endpoints
@	atlas privateendpoints onlinearchive aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	atlas privateendpoints onlinearchive aws create
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--privateEndpointId	Unique identifier of the AWS PrivateLink connection	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints onlinearchive aws ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints onlinearchive aws get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas privateendpoints onlinearchive aws rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas networking
s	container|containers	Manage Network Peering containers
s	peering	Manage Network Peering connections
@	atlas networking container
s	ls|list	List network peering containers in an Atlas project
s	rm|delete	Remove one network peering container in an Atlas project
@	atlas networking container ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of your cloud service provider. Valid values are AWS, AZURE, or GCP	v
@	atlas networking container rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas networking peering
s	ls|list	Retrieve details for all network peering connections in one Atlas project
s	create	Create a connection with AWS, Azure and Google Cloud
s	watch	Watch for a peering connection to be available
s	rm|delete	Delete a peering connection from an Atlas project
@	atlas networking peering ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Name of your cloud service provider. Valid values are AWS, AZURE, or GCP	v
@	atlas networking peering create
s	azure	Create a connection with Azure
s	aws	Create a connection with AWS
s	gcp	Create a connection with GCP
@	atlas networking peering create azure
o	--atlasCidrBlock	CIDR block that Atlas uses for your clusters	v
o	--directoryId	Unique identifier for an Azure AD directory	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Atlas region where the container resides	v
o	--resourceGroup	Name of your Azure resource group	v
o	--subscriptionId	Unique identifier of the Azure subscription in which the VNet resides	v
o	--vnet	Name of your Azure VNet	v
@	atlas networking peering create aws
o	--accountId	Account ID of the owner of the peer VPC	v
o	--atlasCidrBlock	CIDR block that Atlas uses for your clusters	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Atlas region where the container resides	v
o	--routeTableCidrBlock	Peer VPC CIDR block or subnet	v
o	--vpcId	Unique identifier of the peer VPC	v
@	atlas networking peering create gcp
o	--atlasCidrBlock	CIDR block that Atlas uses for your clusters	v
o	--gcpProjectId	Unique identifier of the GCP project in which the network peer resides	v
o	--network	Unique identifier of the Network Peering connection in the Atlas project	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	List of Atlas regions where the container resides	v
@	atlas networking peering watch
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas networking peering rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security
s	customercerts|customer-certs|customerCert|customercert|customer-cert|certs|customerCerts	Manage customer x509 certificates for your project
s	ldap	LDAP operations
@	atlas security customercerts
s	describe	Get the current customer-managed X.509 configuration details for an Atlas project
s	create	Saves a customer-managed X.509 configuration for an Atlas project
s	disable	Disables customer-managed X.509 for a project
@	atlas security customercerts describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security customercerts create
o	--casFile	Path to a PEM file containing one or more CAs for database user authentication	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security customercerts disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security ldap
s	verify	Request verification of an LDAP configuration
s	save	Save an LDAP configuration
s	rm|delete	Delete an LDAP configuration userToDNMapping from an LDAP configuration
s	get	Get an LDAP configuration
@	atlas security ldap verify
s	status	Get the status of an LDAP configuration request
o	--authzQueryTemplate	An LDAP query template that Atlas executes to obtain the LDAP groups to which the authenticated…	v
o	--bindPassword	Password used to authenticate the bindUsername	v
o	--bindUsername	The user distinguished name (DN) that Atlas uses to connect to the LDAP server	v
o	--caCertificate	CA certificate used to verify the identify of the LDAP server	v
o	--hostname	Hostname or IP address of the LDAP server	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--port	Port to which the LDAP server listens to for client connections	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security ldap verify status
s	watch	Watch for an LDAP configuration request to complete
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security ldap verify status watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security ldap save
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
@	atlas security ldap rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas security ldap get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas integration
s	update|create	Create operations
s	ls|list	List third party integrations
s	rm|delete	Delete a third party integration
s	describe	Get a third party integration
@	atlas integration update
s	new_relic|newRelic|NEW_RELIC	Create or update the New Relic integration
s	ops_genie|opsGenie|OPS_GENIE	Create or update the Ops Genie integration
s	pager_duty|pagerDuty|PAGER_DUTY	Create or update the PagerDuty integration
s	datadog|DATADOG	Create or update the Datadog integration
s	victor_ops|victorOps|VICTOR_OPS	Create or update the VictorOps integrations
s	flowdock|FLOWDOCK	Create or update the Flowdock integration
s	webhook|WEBHOOK	Create or update the Webhook integration
@	atlas integration update new_relic
o	--accountId	Unique identifier of your New Relic account	v
o	--licenceKey	Your License Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--readToken	Your Insights Query Key	v
o	--writeToken	Your Insights Insert Key	v
@	atlas integration update ops_genie
o	--apiKey	API Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Indicates which API URL to use, either US or EU. The integration service will use US by default	v
@	atlas integration update pager_duty
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--serviceKey	Your Service Key	v
@	atlas integration update datadog
o	--apiKey	API Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--region	Indicates which API URL to use, either US or EU. The integration service will use US by default	v
@	atlas integration update victor_ops
o	--apiKey	API Key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--routingKey	An optional field for your Routing Key	v
@	atlas integration update flowdock
o	--apiToken	Your API Token	v
o	--flowName	Flowdock Flow name	v
o	--orgName	Your Flowdock organization's name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas integration update webhook
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--secret	An optional field for your webhook secret	v
o	--url	Your webhook URL	v
@	atlas integration ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas integration rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas integration describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas maintenancewindows
s	update	Update the maintenance window
s	rm|delete|clear	Clear the maintenance window
s	defer	Defer the maintenance window
s	get|describe	Get a maintenance window
@	atlas maintenancewindows update
o	--dayOfWeek	Day of the week that you want the maintenance window to start, as a 1-based integer	v
o	--hourOfDay	Hour of the day that you want the maintenance window to start. This parameter uses the 24-hour…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startASAP	Flag that, if specified, indicates to start maintenance immediately upon receiving this request	
@	atlas maintenancewindows rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas maintenancewindows defer
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas maintenancewindows get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdns
s	aw|aws	Manage DNS configuration of an Atlas project’s cluster deployed to AWS
@	atlas customdns aw
s	enable	Enable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	disable	Disable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	get|describe	Describe the custom DNS configuration of an Atlas project’s cluster deployed to AWS
@	atlas customdns aw enable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdns aw disable
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas customdns aw get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cloudproviders
s	accessroles|access-roles|accessRole|accessrole|access-role|accessRoles	Manage AWS IAM role access in Atlas
@	atlas cloudproviders accessroles
s	aws	Manage AWS IAM role access in Atlas
s	ls|list	List AWS IAM role access in Atlas
@	atlas cloudproviders accessroles aws
s	create	Create an AWS IAM role
s	authorize	Authorize an AWS IAM role
s	deauthorize	Deauthorize an AWS IAM role
@	atlas cloudproviders accessroles aws create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cloudproviders accessroles aws authorize
o	--iamAssumedRoleArn	Role ARN that Atlas assumes to access your AWS account	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	atlas cloudproviders accessroles aws authorize	--iamAssumedRoleArn
t	filepaths
@	atlas cloudproviders accessroles aws deauthorize
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas cloudproviders accessroles ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas sl
s	ls|list	Return all serverless instances in the specified project
s	get|describe	Return one serverless instance in the specified project
s	rm|delete	Remove a serverless instance from your project
s	create	Creates one serverless instance in the specified project
s	watch	Monitor the status of serverless instance
@	atlas sl ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas sl get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas sl rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas sl create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provider	Cloud service provider that applies to the provisioned serverless instance	v
o	--region	Human-readable label that identifies the physical location of your MongoDB serverless instance…	v
@	atlas sl watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas livemigrations
s	link	Manage the link-token for your organization
s	validation	Manage a Live Migration validation job for your project
s	create	Create one new migration
s	get|describe	Return one migration job
s	cutover	Start the cutover and confirm when the cutover completes. When the cutover completes, the…
@	atlas livemigrations link
s	create	Create one new link-token
s	rm|delete	Delete one link-token
@	atlas livemigrations link create
o	--accessListIp	IP address access list entries that are associated with the link-token	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	atlas livemigrations link rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas livemigrations validation
s	create	Create one new validation request
s	get|describe	Return one validation job
@	atlas livemigrations validation create
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
@	atlas livemigrations validation get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--validationId	Unique 24-hexadecimal digit string that identifies the validation job	v
@	atlas livemigrations create
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
@	atlas livemigrations get
o	--liveMigrationId	Unique 24-hexadecimal digit string that identifies the live migration job	v
@	atlas livemigrations cutover
o	--liveMigrationId	Unique 24-hexadecimal digit string that identifies the live migration job	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	atlas accesslogs
s	ls|list	Retrieve the access logs of a cluster identified by the cluster's name or hostname
@	atlas accesslogs ls
o	--authResult	Flag that indicates whether to return either successful or failed authentication attempts. When…	v
o	--clusterName	Name of the cluster	v
o	--end	Timestamp in the number of milliseconds that have elapsed, since the UNIX Epoch, for the first…	v
o	--hostname	The fully qualified domain name (FQDN) of the target node that should receive the authentication…	v
o	--ip	IP address that attempted to authenticate with the database. Atlas filters the returned logs to…	v
o	--nLog	Maximum number of log lines to return	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Timestamp in the number of milliseconds that have elapsed, since the UNIX Epoch, for the first…	v
@	cm
s	cluster|clusters	Manage clusters for your project
s	alert|alerts	Manage alerts for your project
s	backup|backups	Manage continuous backups for your project
s	server|servers	Manage automated servers for your project
s	automation	Manage automation configuration for your project
s	security	Manage security configuration for your project
s	dbuser|databaseUsers|databaseUser|dbusers	Manage database users for your project
s	event|events	Manage events for your organization or project
s	monitoring	Manage monitoring for your project
s	process|processes	Manage MongoDB processes for your project
s	metric|measurements|measurement|metrics	Get measurements on the state of the MongoDB process
s	log|logs	Manage log collection jobs for your project
s	agent|agents	Manage MongoDB Agents
s	maintenancewindows|maintenance-windows|maintenanceWindow|maintenancewindow|maintenance-window|maintenanceWindows	Manage Ops Manager/Cloud Manager maintenance windows
s	performanceadvisor|performance-advisor|performanceAdvisor	Performance Advisor operations
s	featurepolicies|feature-policies|featurePolicy|featurepolicy|feature-policy|featurePolicies	Manage feature control policies
s	livemigrations|live-migrations|liveMigration|livemigration|live-migration|lm|liveMigrations	Manage a Live Migration to Atlas for your organization
@	cm cluster
s	ls|list	List clusters for your project
s	describe	Describe a cluster
s	create	Create a MongoDB cluster
s	update	Update a MongoDB cluster
s	rm|delete	Completely removes a cluster from your project
s	apply	Apply a new cluster configuration for your project
s	index|indexes	Manage cluster rolling indexes for your project
s	unmanage	Stop managing a cluster via automation
s	restart	Restart a cluster for your project
s	startup	Start up a cluster for your project
s	shutdown	Shutdown a cluster for your project
s	rfs|reclaimFreeSpace	Reclaim unused space for a cluster
@	cm cluster ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster create
o	--file|-f	Filename to use to create the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cm cluster create	--file
t	filepaths
@	cm cluster update
o	--file|-f	Filename to use to update the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cm cluster update	--file
t	filepaths
@	cm cluster rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster apply
o	--file|-f	Filename to use to change the automation config	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cm cluster apply	--file
t	filepaths
@	cm cluster index
s	create	Create a rolling index for your MongoDB cluster
@	cm cluster index create
o	--MaxVariable	Flag that, if specified, determines which characters to ignore. This flag applies only if…	v
o	--alternate	Flag that, if specified, determines whether collation should consider whitespace and punctuation…	v
o	--backwards	Flag that, if set to true, strings with diacritics sort from the back to the front of the string	
o	--caseFirst	Flag that, if specified, determines the sort order of case differences during tertiary level…	v
o	--caseLevel	Flag that indicates whether the index uses case comparison. This flag applies only if the strength…	
o	--collectionName	Collection name	v
o	--db	Database name	v
o	--key	Field to be indexed and the type of index in the following format: field:type	v
o	--locale	Locale that the ICU defines	v
o	--normalization	Flag that, if set to true, collation checks if text requires normalization and performs…	
o	--numericOrdering	Flag that, if set to true, indicates that collation compares numeric strings as numbers. If set to…	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--rsName	The replica set that the index is built on	v
o	--sparse	Flag that indicates whether Atlas should create a sparse index	
o	--strength	Level of comparison to perform	v
@	cm cluster unmanage
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster restart
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster startup
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster shutdown
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm cluster rfs
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--timestamp	Timestamp in ISO 8601 format when the service reclaims the space. If not set, defaults to the…	v
@	cm alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	cm alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	cm alert config create
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
@	cm alert config ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm alert config rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm alert config field
s	types|type	Lists available field types for your alert configurations
@	cm alert config field types
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	cm alert config update
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
@	cm alert get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm alert ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	cm alert ack
o	--comment	Optional description or comment for the entry	v
o	--forever|-F	Acknowledges an alert 'forever'	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--until	Time, in ISO 8601 format, until which the alert has been acknowledged. mongocli returns this value…	v
@	cm alert unack
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	cm alert global ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	cm backup
s	snapshot|snapshots	Manage backup snapshots for your project
s	restore|restores	Manage restore jobs for your project
s	checkpoint|checkpoints	Manage backup checkpoints for your project
s	enable	Enable backup for a given hostname
s	disable	Disable backup for a given hostname
s	config	Manage backup configurations for your project
@	cm backup snapshot
s	ls|list	List snapshots for a project and cluster
s	schedule	Manage backup snapshot schedules for a cluster
@	cm backup snapshot ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup snapshot schedule
s	get|describe	Describe a snapshot schedule for a cluster
s	update	Update a snapshot schedule for a cluster
@	cm backup snapshot schedule get
o	--clusterId	Unique identifier of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup snapshot schedule update
o	--clusterCheckpointIntervalMin	Number of minutes between successive cluster checkpoints. Valid values are 15, 30, or 60	v
o	--clusterId	Unique identifier of the cluster	v
o	--dailySnapshotRetentionDays	Number of days to retain daily snapshots. Accepted values are between 1 and 365 inclusive	v
o	--monthlySnapshotRetentionMonths	Number of months to retain monthly snapshots. Accepted values are between 1 and 36 inclusive	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pointInTimeWindowHours	Number of hours in the past for which MongoDB should create a point-in-time snapshot	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--referenceHourOfDay	Hour of the day to schedule snapshots using a 24-hour clock. Accepted values are between 0 and 23…	v
o	--referenceMinuteOfHour	Minute of the hour to schedule snapshots. Accepted values are between 0 and 59 inclusive	v
o	--referenceTimeZoneOffset	The ISO-8601-formatted timezone offset where the Ops Manager host resides	v
o	--snapshotIntervalHours	Number of hours between snapshots. Valid values are 6, 8, 12, or 24	v
o	--snapshotRetentionDays	Number of days to keep recent snapshots. Accepted values are between 2 and 5 inclusive	v
o	--weeklySnapshotRetentionWeeks	Number of weeks to retain weekly snapshots. Accepted values are between 1 and 52 inclusive	v
@	cm backup restore
s	ls|list	Lists restore jobs for a project and cluster
s	start	Start a restore job for a project and cluster
@	cm backup restore ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup restore start
o	--checkpointId	Unique identifier for the sharded cluster checkpoint that represents the point in time to which…	v
o	--clusterId	Unique identifier of the cluster	v
o	--expirationHours	Number of hours the download URL is valid once the restore job is complete. For use only with…	v
o	--expires	Timestamp in ISO 8601 date and time format after which the URL is no longer available. For use…	v
o	--maxDownloads	Number of times the download URL can be used. This value must be 1 or greater. For use only with…	v
o	--oplogInc	32-bit incrementing ordinal that represents operations within a given second. When paired with…	v
o	--oplogTs	Oplog timestamp given as a timestamp in the number of seconds that have elapsed since the UNIX…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pointInTimeUTCMillis	Timestamp in the number of milliseconds that have elapsed since the UNIX epoch that represents the…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--snapshotId	Unique identifier of the snapshot to restore	v
o	--targetClusterId	Unique identifier of the target cluster. For use only with automated restore jobs	v
o	--targetProjectId	Unique identifier of the project that contains the destination cluster for the restore job	v
@	cm backup checkpoint
s	ls|list	List continuous backup checkpoints for your project
@	cm backup checkpoint ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup enable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup config
s	get|describe	Get a backup configuration
s	ls|list	List backup configurations for your project
s	update	Update a backup configuration
@	cm backup config get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup config ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm backup config update
o	--authMechanism	Authentication mechanism needed to connect to the sync source database	v
o	--encryption	Flag that indicates if encryption is enabled for the backup configuration	
o	--excludedNamespace	List of database names and collection names to omit from the backup	v
o	--includedNamespace	List of database names and collection names to include in the backup	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provisioned	Flag that indicates if Ops Manager has provisioned the resources needed to store a backup	
o	--ssl	Flag that indicates if TLS is enabled for the sync source database	
o	--status	Current (or desired) status of the backup configuration	v
o	--storageEngine	Storage engine used for the backup	v
o	--syncSource	Mongod instance from which you retrieve backup data	v
o	--username	Username of the user	v
@	cm server
s	ls|list	List all available servers running an automation agent for your project
@	cm server ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm automation
s	status	Show the current status of the automation config
s	show|get|describe	Get the current automation configuration for a project
s	update	Update the current automation configuration for a project
s	watch	Watch for automation changes to be completed
@	cm automation status
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm automation show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm automation update
o	--file|-f	Filename to use	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cm automation update	--file
t	filepaths
@	cm automation watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm security
s	enable	Enable authentication mechanisms for your project
@	cm security enable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm dbuser
s	create	Create a database user for your project
s	ls|list	List Atlas database users for your project
s	rm|delete	Delete a database user for your project
@	cm dbuser create
o	--authDB	Authentication database name	v
o	--mechanisms	Authentication mechanism. Valid values are SCRAM-SHA-1 or SCRAM-SHA-256	v
o	--password|-p	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles and the databases or collections on which the roles apply	v
o	--username|-u	Username for authenticating to MongoDB	v
@	cm dbuser ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm dbuser rm
o	--authDB	Authentication database name	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	cm event ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	cm event organization
s	ls|list	Return all events for an organization
@	cm event organization ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--type	Type of the event that triggered the alert	v
@	cm event project
s	ls|list	Return all events for a project
@	cm event project ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	cm monitoring
s	enable	Enable monitoring for a given hostname
s	disable	Disable monitoring for a given hostname
s	rm|stop	Stops monitoring the MongoDB process specified
@	cm monitoring enable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm monitoring disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm monitoring rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm process
s	ls|list	List MongoDB processes for your project
s	get|describe	Describe MongoDB processes for your project
@	cm process ls
o	--clusterId	Unique identifier of the cluster	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm process get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm metric
s	processes|process	Get measurements for a given host
s	disk|disks	List available disks or disks measurements for a given host
s	database|databases	List available databases or databases measurements for a given host
@	cm metric processes
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	cm metric disk
s	ls|list	List available disks for a given host
s	describe	Describe disks measurements for a given host partition
@	cm metric disk ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm metric disk describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	cm metric database
s	ls|list	List available databases for a given host
s	describe	Describe database measurements for a given host database
@	cm metric database ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm metric database describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	cm log
s	job|jobs	Manage log collection jobs for your project
@	cm log job
s	collect	Start a job to collect logs for your project
s	ls|list	List log collection jobs for your project
s	download	Download logs generated by a log collection job
s	rm|delete	Delete a log collection job from your project
@	cm log job collect
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--redacted	If set to true, emails, hostnames, IP addresses, and namespaces in API responses involving this…	
o	--sizeRequestedPerFileBytes	Size for each log file in bytes	v
o	--type	Array of strings specifying the types of logs to collect	v
@	cm log job ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--verbose	Flag that, if set to true, returns all child jobs in the response	
@	cm log job download
o	--force	Overwrites the destination file	
o	--out	Optional output file name. Uses the log name if the output file's name is not specified	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	cm log job download	--out
t	filepaths
@	cm log job rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm agent
s	ls|list	List available MongoDB Agents for your project
s	upgrade	Upgrade MongoDB Agents to the latest available version
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Agent API Keys operations
s	version|versions	Manage MongoDB Agents versions
@	cm agent ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm agent upgrade
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm agent apikeys
s	ls|list	List available MongoDB Agent API Keys for your project
s	create	Create an Agent API Key for your project
s	rm|delete	Delete an Agent API Key for your project
@	cm agent apikeys ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm agent apikeys create
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm agent apikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm agent version
s	ls|list	List MongoDB Agent versions in the provided project
@	cm agent version ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm maintenancewindows
s	create	Create a maintenance window
s	ls|list	List maintenance windows
s	rm|delete	Delete a maintenance window
s	describe	Get a maintenance window
s	update	Update a maintenance window
@	cm maintenancewindows create
o	--alertType	Alert types to silence during maintenance window. Valid values are HOST, REPLICA_SET, CLUSTER…	v
o	--desc	Description of the maintenance window	v
o	--endDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window ends	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window starts	v
@	cm maintenancewindows ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm maintenancewindows rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm maintenancewindows describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm maintenancewindows update
o	--alertType	Alert types to silence during maintenance window. Valid values are HOST, REPLICA_SET, CLUSTER…	v
o	--desc	Description of the maintenance window	v
o	--endDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window ends	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window starts	v
@	cm performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	cm performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	cm performanceadvisor namespace ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	cm performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	cm performanceadvisor slowquerylogs ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nLog	Maximum number of log lines to return	v
o	--namespaces	Namespaces from which to retrieve suggested slow query logs	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	cm performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	cm performanceadvisor suggestedindexes ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nExamples	Maximum number of example queries to provide that will be improved by a suggested index	v
o	--nIndexes	Maximum number of indexes to suggest	v
o	--namespaces	Namespaces from which to retrieve suggested indexes	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	cm performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	cm performanceadvisor slowOT ls
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm performanceadvisor slowOT disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm featurepolicies
s	ls|list	List feature control policies for your project
s	update	Update feature control policies for your project
@	cm featurepolicies ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm featurepolicies update
o	--name	Identifying label for the external system that manages this Ops Manager Project	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--policy	List of policies that the external system applies to this Ops Manager Project	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--systemId	Unique identifier of the external system that manages this Ops Manager Project	v
@	cm livemigrations
s	link	Manage the link-token for your organization
@	cm livemigrations link
s	create	Create one new organization link
s	rm|delete	Delete one link-token
s	get|describe	Return the status of the connection between the specified source organization and the target…
@	cm livemigrations link create
o	--linkToken	Link-token generated by Atlas	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm livemigrations link rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	cm livemigrations link get
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om
s	cluster|clusters	Manage clusters for your project
s	alert|alerts	Manage alerts for your project
s	backup|backups	Manage continuous backups for your project
s	server|servers	Manage automated servers for your project
s	automation	Manage automation configuration for your project
s	security	Manage security configuration for your project
s	dbuser|databaseUsers|databaseUser|dbusers	Manage database users for your project
s	owner	Manage Ops Manager owners
s	event|events	Manage events for your organization or project
s	monitoring	Manage monitoring for your project
s	process|processes	Manage MongoDB processes for your project
s	metric|measurements|measurement|metrics	Get measurements on the state of the MongoDB process
s	log|logs	Manage log collection jobs for your project
s	agent|agents	Manage MongoDB Agents
s	diagnosearchives|diagnose-archives|diagnoseArchive|diagnosearchive|diagnose-archive|diagnoseArchives	Manage diagnose archives
s	maintenancewindows|maintenance-windows|maintenanceWindow|maintenancewindow|maintenance-window|maintenanceWindows	Manage Ops Manager/Cloud Manager maintenance windows
s	performanceadvisor|performance-advisor|performanceAdvisor	Performance Advisor operations
s	versionmanifest|version-manifest|versionManifest	Manage Ops Manager version manifest
s	admin	Manage backup administration
s	softwarecomponents|software-components|softwareComponent|softwarecomponent|software-component|softwareComponents	Manage earliest and latest versions of MongoDB Agent, MongoDB Tools, and BI Connector in your…
s	featurepolicies|feature-policies|featurePolicy|featurepolicy|feature-policy|featurePolicies	Manage feature control policies
s	serverusage|server-usage|serverUsage	Manage your server usage
s	livemigrations|live-migrations|liveMigration|livemigration|live-migration|lm|liveMigrations	Manage a Live Migration to Atlas for your organization
@	om cluster
s	ls|list	List clusters for your project
s	describe	Describe a cluster
s	create	Create a MongoDB cluster
s	update	Update a MongoDB cluster
s	rm|delete	Completely removes a cluster from your project
s	apply	Apply a new cluster configuration for your project
s	index|indexes	Manage cluster rolling indexes for your project
s	unmanage	Stop managing a cluster via automation
s	restart	Restart a cluster for your project
s	startup	Start up a cluster for your project
s	shutdown	Shutdown a cluster for your project
s	rfs|reclaimFreeSpace	Reclaim unused space for a cluster
@	om cluster ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster create
o	--file|-f	Filename to use to create the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	om cluster create	--file
t	filepaths
@	om cluster update
o	--file|-f	Filename to use to update the cluster	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	om cluster update	--file
t	filepaths
@	om cluster rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster apply
o	--file|-f	Filename to use to change the automation config	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	om cluster apply	--file
t	filepaths
@	om cluster index
s	create	Create a rolling index for your MongoDB cluster
@	om cluster index create
o	--MaxVariable	Flag that, if specified, determines which characters to ignore. This flag applies only if…	v
o	--alternate	Flag that, if specified, determines whether collation should consider whitespace and punctuation…	v
o	--backwards	Flag that, if set to true, strings with diacritics sort from the back to the front of the string	
o	--caseFirst	Flag that, if specified, determines the sort order of case differences during tertiary level…	v
o	--caseLevel	Flag that indicates whether the index uses case comparison. This flag applies only if the strength…	
o	--collectionName	Collection name	v
o	--db	Database name	v
o	--key	Field to be indexed and the type of index in the following format: field:type	v
o	--locale	Locale that the ICU defines	v
o	--normalization	Flag that, if set to true, collation checks if text requires normalization and performs…	
o	--numericOrdering	Flag that, if set to true, indicates that collation compares numeric strings as numbers. If set to…	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--rsName	The replica set that the index is built on	v
o	--sparse	Flag that indicates whether Atlas should create a sparse index	
o	--strength	Level of comparison to perform	v
@	om cluster unmanage
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster restart
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster startup
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster shutdown
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om cluster rfs
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--timestamp	Timestamp in ISO 8601 format when the service reclaims the space. If not set, defaults to the…	v
@	om alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	om alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	om alert config create
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
@	om alert config ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om alert config rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om alert config field
s	types|type	Lists available field types for your alert configurations
@	om alert config field types
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om alert config update
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
@	om alert get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om alert ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	om alert ack
o	--comment	Optional description or comment for the entry	v
o	--forever|-F	Acknowledges an alert 'forever'	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--until	Time, in ISO 8601 format, until which the alert has been acknowledged. mongocli returns this value…	v
@	om alert unack
o	--comment	Optional description or comment for the entry	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	om alert global ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--status	Alert's status. The values are TRACKING, OPEN, CLOSED, and CANCELED	v
@	om backup
s	snapshot|snapshots	Manage backup snapshots for your project
s	restore|restores	Manage restore jobs for your project
s	checkpoint|checkpoints	Manage backup checkpoints for your project
s	enable	Enable backup for a given hostname
s	disable	Disable backup for a given hostname
s	config	Manage backup configurations for your project
@	om backup snapshot
s	ls|list	List snapshots for a project and cluster
s	schedule	Manage backup snapshot schedules for a cluster
@	om backup snapshot ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup snapshot schedule
s	get|describe	Describe a snapshot schedule for a cluster
s	update	Update a snapshot schedule for a cluster
@	om backup snapshot schedule get
o	--clusterId	Unique identifier of the cluster	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup snapshot schedule update
o	--clusterCheckpointIntervalMin	Number of minutes between successive cluster checkpoints. Valid values are 15, 30, or 60	v
o	--clusterId	Unique identifier of the cluster	v
o	--dailySnapshotRetentionDays	Number of days to retain daily snapshots. Accepted values are between 1 and 365 inclusive	v
o	--monthlySnapshotRetentionMonths	Number of months to retain monthly snapshots. Accepted values are between 1 and 36 inclusive	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pointInTimeWindowHours	Number of hours in the past for which MongoDB should create a point-in-time snapshot	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--referenceHourOfDay	Hour of the day to schedule snapshots using a 24-hour clock. Accepted values are between 0 and 23…	v
o	--referenceMinuteOfHour	Minute of the hour to schedule snapshots. Accepted values are between 0 and 59 inclusive	v
o	--referenceTimeZoneOffset	The ISO-8601-formatted timezone offset where the Ops Manager host resides	v
o	--snapshotIntervalHours	Number of hours between snapshots. Valid values are 6, 8, 12, or 24	v
o	--snapshotRetentionDays	Number of days to keep recent snapshots. Accepted values are between 2 and 5 inclusive	v
o	--weeklySnapshotRetentionWeeks	Number of weeks to retain weekly snapshots. Accepted values are between 1 and 52 inclusive	v
@	om backup restore
s	ls|list	Lists restore jobs for a project and cluster
s	start	Start a restore job for a project and cluster
@	om backup restore ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup restore start
o	--checkpointId	Unique identifier for the sharded cluster checkpoint that represents the point in time to which…	v
o	--clusterId	Unique identifier of the cluster	v
o	--expirationHours	Number of hours the download URL is valid once the restore job is complete. For use only with…	v
o	--expires	Timestamp in ISO 8601 date and time format after which the URL is no longer available. For use…	v
o	--maxDownloads	Number of times the download URL can be used. This value must be 1 or greater. For use only with…	v
o	--oplogInc	32-bit incrementing ordinal that represents operations within a given second. When paired with…	v
o	--oplogTs	Oplog timestamp given as a timestamp in the number of seconds that have elapsed since the UNIX…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pointInTimeUTCMillis	Timestamp in the number of milliseconds that have elapsed since the UNIX epoch that represents the…	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--snapshotId	Unique identifier of the snapshot to restore	v
o	--targetClusterId	Unique identifier of the target cluster. For use only with automated restore jobs	v
o	--targetProjectId	Unique identifier of the project that contains the destination cluster for the restore job	v
@	om backup checkpoint
s	ls|list	List continuous backup checkpoints for your project
@	om backup checkpoint ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup enable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup config
s	get|describe	Get a backup configuration
s	ls|list	List backup configurations for your project
s	update	Update a backup configuration
@	om backup config get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup config ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om backup config update
o	--authMechanism	Authentication mechanism needed to connect to the sync source database	v
o	--encryption	Flag that indicates if encryption is enabled for the backup configuration	
o	--excludedNamespace	List of database names and collection names to omit from the backup	v
o	--includedNamespace	List of database names and collection names to include in the backup	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--provisioned	Flag that indicates if Ops Manager has provisioned the resources needed to store a backup	
o	--ssl	Flag that indicates if TLS is enabled for the sync source database	
o	--status	Current (or desired) status of the backup configuration	v
o	--storageEngine	Storage engine used for the backup	v
o	--syncSource	Mongod instance from which you retrieve backup data	v
o	--username	Username of the user	v
@	om server
s	ls|list	List all available servers running an automation agent for your project
@	om server ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om automation
s	status	Show the current status of the automation config
s	show|get|describe	Get the current automation configuration for a project
s	update	Update the current automation configuration for a project
s	watch	Watch for automation changes to be completed
@	om automation status
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om automation show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om automation update
o	--file|-f	Filename to use	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	om automation update	--file
t	filepaths
@	om automation watch
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om security
s	enable	Enable authentication mechanisms for your project
@	om security enable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om dbuser
s	create	Create a database user for your project
s	ls|list	List Atlas database users for your project
s	rm|delete	Delete a database user for your project
@	om dbuser create
o	--authDB	Authentication database name	v
o	--mechanisms	Authentication mechanism. Valid values are SCRAM-SHA-1 or SCRAM-SHA-256	v
o	--password|-p	User's password	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles and the databases or collections on which the roles apply	v
o	--username|-u	Username for authenticating to MongoDB	v
@	om dbuser ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om dbuser rm
o	--authDB	Authentication database name	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om owner
s	create	Create the first user for Ops Manager
@	om owner create
o	--accessListIp	IP addresses to add to the new user's access list	v
o	--email	User's email address	v
o	--firstName	User's first name	v
o	--lastName	User's last name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--password|-p	User's password	v
@	om event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	om event ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	om event organization
s	ls|list	Return all events for an organization
@	om event organization ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--type	Type of the event that triggered the alert	v
@	om event project
s	ls|list	Return all events for a project
@	om event project ls
o	--limit	Number of items per page	v
o	--maxDate	Returns events whose created date is less than or equal to it	v
o	--minDate	Returns events whose created date is greater than or equal to it	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--type	Type of the event that triggered the alert	v
@	om monitoring
s	enable	Enable monitoring for a given hostname
s	disable	Disable monitoring for a given hostname
s	rm|stop	Stops monitoring the MongoDB process specified
@	om monitoring enable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om monitoring disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om monitoring rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om process
s	ls|list	List MongoDB processes for your project
s	get|describe	Describe MongoDB processes for your project
@	om process ls
o	--clusterId	Unique identifier of the cluster	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om process get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om metric
s	processes|process	Get measurements for a given host
s	disk|disks	List available disks or disks measurements for a given host
s	database|databases	List available databases or databases measurements for a given host
@	om metric processes
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	om metric disk
s	ls|list	List available disks for a given host
s	describe	Describe disks measurements for a given host partition
@	om metric disk ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om metric disk describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	om metric database
s	ls|list	List available databases for a given host
s	describe	Describe database measurements for a given host database
@	om metric database ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om metric database describe
o	--end	End of the period, in UNIX Epoch format, until which to retrieve measurements	v
o	--granularity	Duration in ISO 8601 notation that specifies the interval between measurement data points. Only…	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--period	Duration in ISO 8601 that specifies how far back in the past to retrieve measurements	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--start	Beginning of the period, in UNIX Epoch format, from which to start retrieving measurements	v
o	--type	Measurements to return. If it is not specified, all measurements are returned	v
@	om log
s	job|jobs	Manage log collection jobs for your project
@	om log job
s	collect	Start a job to collect logs for your project
s	ls|list	List log collection jobs for your project
s	download	Download logs generated by a log collection job
s	rm|delete	Delete a log collection job from your project
@	om log job collect
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--redacted	If set to true, emails, hostnames, IP addresses, and namespaces in API responses involving this…	
o	--sizeRequestedPerFileBytes	Size for each log file in bytes	v
o	--type	Array of strings specifying the types of logs to collect	v
@	om log job ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--verbose	Flag that, if set to true, returns all child jobs in the response	
@	om log job download
o	--force	Overwrites the destination file	
o	--out	Optional output file name. Uses the log name if the output file's name is not specified	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	om log job download	--out
t	filepaths
@	om log job rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om agent
s	ls|list	List available MongoDB Agents for your project
s	upgrade	Upgrade MongoDB Agents to the latest available version
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Agent API Keys operations
s	version|versions	Manage MongoDB Agents versions
@	om agent ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om agent upgrade
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om agent apikeys
s	ls|list	List available MongoDB Agent API Keys for your project
s	create	Create an Agent API Key for your project
s	rm|delete	Delete an Agent API Key for your project
@	om agent apikeys ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om agent apikeys create
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om agent apikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om agent version
s	ls|list	List MongoDB Agent versions in the provided project
@	om agent version ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om diagnosearchives
s	get|download	Download diagnose archives
@	om diagnosearchives get
o	--limit	Max number of entries for the diagnose archive	v
o	--minutes	Beginning of the period, in UNIX Epoch format, from which to start retrieving the diagnose…	v
o	--out	Optional output file name. Uses diagnose-archive.tar.gz if the output file's name is not specified	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
=	om diagnosearchives get	--out
t	filepaths
@	om maintenancewindows
s	create	Create a maintenance window
s	ls|list	List maintenance windows
s	rm|delete	Delete a maintenance window
s	describe	Get a maintenance window
s	update	Update a maintenance window
@	om maintenancewindows create
o	--alertType	Alert types to silence during maintenance window. Valid values are HOST, REPLICA_SET, CLUSTER…	v
o	--desc	Description of the maintenance window	v
o	--endDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window ends	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window starts	v
@	om maintenancewindows ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om maintenancewindows rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om maintenancewindows describe
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om maintenancewindows update
o	--alertType	Alert types to silence during maintenance window. Valid values are HOST, REPLICA_SET, CLUSTER…	v
o	--desc	Description of the maintenance window	v
o	--endDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window ends	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startDate	Timestamp in ISO 8601 date and time format in UTC when the maintenance window starts	v
@	om performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	om performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	om performanceadvisor namespace ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	om performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	om performanceadvisor slowquerylogs ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nLog	Maximum number of log lines to return	v
o	--namespaces	Namespaces from which to retrieve suggested slow query logs	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	om performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	om performanceadvisor suggestedindexes ls
o	--duration	Length of time from the since parameter, in milliseconds, for which you want to receive results	v
o	--hostId	Unique identifier for the host of a MongoDB process	v
o	--nExamples	Maximum number of example queries to provide that will be improved by a suggested index	v
o	--nIndexes	Maximum number of indexes to suggest	v
o	--namespaces	Namespaces from which to retrieve suggested indexes	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--processName	Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--since	Point in time, specified as milliseconds since the Unix Epoch, from which you want to receive…	v
@	om performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	om performanceadvisor slowOT ls
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om performanceadvisor slowOT disable
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om versionmanifest
s	update	Update Ops Manager version manifest
@	om versionmanifest update
o	--force	If specified, skips Ops Manager version check	
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om admin
s	backup|backups	Manage backup administration
@	om admin backup
s	blockstore|blockstores	Manage backup blockstore configurations
s	filesystems|file-systems|fileSystem|filesystem|file-system|fileSystems	Manage file system configurations
s	s3	Manage backup s3 blockstore configurations
s	oplog	Manage backup oplog configurations
s	sync	Manage backup sync configurations
@	om admin backup blockstore
s	ls|list	List backup blockstore configurations
s	get|describe	Get a backup blockstore configuration
s	create	Create a backup blockstore configuration
s	update	Update a backup blockstore configuration
s	rm|delete	Delete a backup blockstore configuration
@	om admin backup blockstore ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	om admin backup blockstore get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om admin backup blockstore create
o	--assignment	Flag indicating whether this blockstore can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--maxCapacityGB	The maximum amount of data in GB this blockstore can store	v
o	--name	Unique name that labels this blockstore	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ssl	Flag indicating whether this blockstore only accepts connections encrypted using TLS	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup blockstore update
o	--assignment	Flag indicating whether this blockstore can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--maxCapacityGB	The maximum amount of data in GB this blockstore can store	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ssl	Flag indicating whether this blockstore only accepts connections encrypted using TLS	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup blockstore rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	om admin backup filesystems
s	ls|list	List file system configurations
s	get|describe	Get a file system configuration
s	rm|delete	Delete a file system configuration
s	create	Create a file system configuration
s	update	Update a file system configuration
@	om admin backup filesystems ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	om admin backup filesystems get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om admin backup filesystems rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	om admin backup filesystems create
o	--assignment	Flag indicating whether this file system store can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--mmapv1CompressionSetting	The compression setting for the MMAPv1 storage engine snaphots	v
o	--name	Unique name that labels this file system store configuration	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--storePath	The location where file system-based backups are stored on the file system store host	v
o	--wtCompressionSetting	The compression setting for the WiredTiger storage engine snaphots	v
@	om admin backup filesystems update
o	--assignment	Flag indicating whether this file system store can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--mmapv1CompressionSetting	The compression setting for the MMAPv1 storage engine snaphots	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--storePath	The location where file system-based backups are stored on the file system store host	v
o	--wtCompressionSetting	The compression setting for the WiredTiger storage engine snaphots	v
@	om admin backup s3
s	ls|list	List backup s3 blockstore configurations
s	rm|delete	Delete a backup s3 blockstore configuration
s	create	Create a backup S3 blockstore configuration
s	update	Update a backup S3 blockstore configuration
s	get|describe	Get a backup s3 blockstore configuration
@	om admin backup s3 ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	om admin backup s3 rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	om admin backup s3 create
o	--acceptedTos	Flag indicating whether or not you accepted the terms of service for using Amazon S3-compatible…	
o	--assignment	Flag indicating whether this blockstore can be assigned backup jobs	
o	--awsAccessKey	AWS Access Key ID that can access the Amazon S3 bucket specified in s3BucketName	v
o	--awsSecretKey	AWS Secret Access Key that can access the Amazon S3 bucket specified in s3BucketName	v
o	--disableProxyS3	Flag indicating whether the HTTP proxy should be used when connecting to Amazon S3	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--name	Unique name that labels this blockstore	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pathStyleAccessEnabled	Flag indicating the style of this endpoint	
o	--s3AuthMethod	Method used to authorize access to the Amazon S3 bucket specified in s3BucketName. Valid values…	v
o	--s3BucketEndpoint	URL that Ops Manager uses to access this Amazon S3 or S3-compatible bucket	v
o	--s3BucketName	Name of the Amazon S3 bucket that hosts the S3 blockstore	v
o	--s3MaxConnections	Positive integer indicating the maximum number of connections to this Amazon S3 blockstore	v
o	--sseEnabled	Flag indicating whether this Amazon S3 blockstore enables server-side encryption	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup s3 update
o	--acceptedTos	Flag indicating whether or not you accepted the terms of service for using Amazon S3-compatible…	
o	--assignment	Flag indicating whether this blockstore can be assigned backup jobs	
o	--awsAccessKey	AWS Access Key ID that can access the Amazon S3 bucket specified in s3BucketName	v
o	--awsSecretKey	AWS Secret Access Key that can access the Amazon S3 bucket specified in s3BucketName	v
o	--disableProxyS3	Flag indicating whether the HTTP proxy should be used when connecting to Amazon S3	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--pathStyleAccessEnabled	Flag indicating the style of this endpoint	
o	--s3AuthMethod	Method used to authorize access to the Amazon S3 bucket specified in s3BucketName. Valid values…	v
o	--s3BucketEndpoint	URL that Ops Manager uses to access this Amazon S3 or S3-compatible bucket	v
o	--s3BucketName	Name of the Amazon S3 bucket that hosts the S3 blockstore	v
o	--s3MaxConnections	Positive integer indicating the maximum number of connections to this Amazon S3 blockstore	v
o	--sseEnabled	Flag indicating whether this Amazon S3 blockstore enables server-side encryption	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup s3 get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om admin backup oplog
s	ls|list	List backup oplog configurations
s	get|describe	Get a backup oplog configuration
s	create	Create a backup oplog configuration
s	update	Update a backup oplog configuration
s	rm|delete	Delete a backup oplog configuration
@	om admin backup oplog ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	om admin backup oplog get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om admin backup oplog create
o	--assignment	Flag indicating whether this oplog can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--maxCapacityGB	The maximum amount of data in GB this blockstore can store	v
o	--name	Unique name that labels this oplog store	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ssl	Flag indicating whether this oplog store only accepts connections encrypted using TLS	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup oplog update
o	--assignment	Flag indicating whether this oplog can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--maxCapacityGB	The maximum amount of data in GB this blockstore can store	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ssl	Flag indicating whether this oplog store only accepts connections encrypted using TLS	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup oplog rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	om admin backup sync
s	ls|list	List backup sync configurations
s	rm|delete	Delete a backup sync configuration
s	create	Create a backup sync configuration
s	update	Update a backup sync configuration
s	get|describe	Get a backup sync configuration
@	om admin backup sync ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	om admin backup sync rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	om admin backup sync create
o	--assignment	Flag indicating whether this sync store can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--maxCapacityGB	The maximum amount of data in GB this blockstore can store	v
o	--name	Unique name that labels this sync store	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ssl	Flag indicating whether this blockstore only accepts connections encrypted using TLS	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup sync update
o	--assignment	Flag indicating whether this sync store can be assigned backup jobs	
o	--encryptedCredentials	Flag indicating whether the username and password were encrypted using the credentials tool	
o	--label	Array of tags to manage which backup jobs Ops Manager can assign to which blockstores	v
o	--loadFactor	A positive, non-zero integer that expresses how much backup work this snapshot store should…	v
o	--maxCapacityGB	The maximum amount of data in GB this blockstore can store	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ssl	Flag indicating whether this blockstore only accepts connections encrypted using TLS	
o	--uri	A comma-separated list of hosts in the <hostname:port> format that can be used to access this…	v
o	--writeConcern	The write concern used for this blockstore	v
@	om admin backup sync get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om softwarecomponents
s	ls|list	List versions of MongoDB Agent, MongoDB Tools, and BI Connector in your environment
@	om softwarecomponents ls
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om featurepolicies
s	ls|list	List feature control policies for your project
s	update	Update feature control policies for your project
@	om featurepolicies ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om featurepolicies update
o	--name	Identifying label for the external system that manages this Ops Manager Project	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--policy	List of policies that the external system applies to this Ops Manager Project	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--systemId	Unique identifier of the external system that manages this Ops Manager Project	v
@	om serverusage
s	project|projects	Manage your server usage for a project
s	organization|organizations	Manage your server usage for an organization
s	capture	Capture a snapshot of usage for the processes Ops Manager manages
s	download	Download the server usage report
@	om serverusage project
s	servertype|server-type|serverType	Manage your server type for a project
s	host|hosts	Manage host assignment for a project
@	om serverusage project servertype
s	get|describe	Get the default server type for a project
s	set	Set the default server type for a project
@	om serverusage project servertype get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om serverusage project servertype set
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	om serverusage project host
s	ls|list	List all host assignments for one project
@	om serverusage project host ls
o	--endDate	Timestamp, in ISO 8601 date format, when the list of host assignments ends	v
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--startDate	Timestamp, in ISO 8601 date format, when the list of host assignments starts	v
@	om serverusage organization
s	servertype|server-type|serverType	Manage your server type for an organization
s	host|hosts	Manage host assignment for an organization
@	om serverusage organization servertype
s	get|describe	Get the default server type for an organization
s	set	Set the default server type for an organization
@	om serverusage organization servertype get
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	om serverusage organization servertype set
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	om serverusage organization host
s	ls|list	List all host assignments for one organization
@	om serverusage organization host ls
o	--endDate	Timestamp, in ISO 8601 date format, when the list of host assignments ends	v
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--startDate	Timestamp, in ISO 8601 date format, when the list of host assignments starts	v
@	om serverusage capture
@	om serverusage download
o	--endDate	Timestamp, in ISO 8601 date format, when the list of host assignments ends	v
o	--force	Overwrites the destination file	
o	--format	Compression format of the resulting report. Valid values are ZIP, TAR, or .GZ	v
o	--out	Optional output file name. Uses the log name if the output file's name is not specified	v
o	--startDate	Timestamp, in ISO 8601 date format, when the list of host assignments starts	v
@	om livemigrations
s	link	Manage the link-token for your organization
@	om livemigrations link
s	create	Create one new organization link
s	rm|delete	Delete one link-token
s	get|describe	Return the status of the connection between the specified source organization and the target…
@	om livemigrations link create
o	--linkToken	Link-token generated by Atlas	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	om livemigrations link rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	om livemigrations link get
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam
s	project|projects	Project operations
s	organization|orgs|org|organizations	Organization operations
s	globalapikeys|global-api-keys|globalApiKey|globalapikey|global-api-key|globalApiKeys	Global API Keys operations
s	globalaccesslists|global-access-lists|globalAccessList|globalaccesslist|global-access-list|globalWhitelists|globalwhitelists|global-whitelists|globalWhitelist|globalwhitelist|global-whitelist|globalAccessLists	Manage IP access list for Global API Key
s	user|users	Users operations
s	team|teams	Teams operations
@	iam project
s	ls|list	List projects
s	create	Create a project
s	rm|delete	Delete a project
s	show|get|describe	Describe a project
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Manage API Keys for your project
s	user|users	Manage users for a project
s	team|teams	Teams operations
s	invitation|invitations	Invitation operations
@	iam project ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam project create
o	--govCloudRegionsOnly	Only for AtlasGov projects. If specified, designates that the project uses only the AWS GovCloud…	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--ownerId	Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the…	v
o	--withoutDefaultAlertSettings	Flag that indicates whether to create the new project with the default alert settings enabled…	
@	iam project rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	iam project show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam project apikeys
s	ls|list	List API Keys for your project
s	create	Create an API Key for your project
s	rm|delete	Delete an API Key for your project
s	update|assign	Assign an API Key to a project
@	iam project apikeys ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project apikeys create
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	List of roles for the API key	v
@	iam project apikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project apikeys update
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	List of roles for the API key	v
@	iam project user
s	ls|list	List all users for a project
s	rm|delete	Delete user from a project
@	iam project user ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project user rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project team
s	ls|list	Get all teams in a project
s	add	Add team to a project
s	rm|delete	Delete team from a project
s	updates|update	Update roles for a team in a project
@	iam project team ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project team add
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	Project role you want to assign to the team	v
@	iam project team rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project team updates
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	Project role you want to assign to the team	v
@	iam project invitation
s	ls|list	Retrieves all pending invitations to the specified project
s	get|describe	Retrieve details for one pending invitation to the specified project
s	rm|delete	Deletes one pending invitation to the specified project
s	create|invite	Invites one user to the project that you specify
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
@	iam project invitation ls
o	--email	User's email address	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project invitation get
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project invitation rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam project invitation create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles for the associated organization	v
o	--teamId	Unique identification of the team	v
@	iam project invitation updates
o	--email	User's email address	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--projectId	Project ID to use. Overrides the settings in the configuration file or environment variable	v
o	--role	User's roles for the associated organization	v
@	iam organization
s	ls|list	List organizations
s	show|describe	Describe an organizations
s	create	Create an organization
s	rm|delete	Delete an organization
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Organization API Keys operations
s	user|users	Users operations
s	invitation|invitations	Invitation operations
@	iam organization ls
o	--includeDeleted	If specified, Atlas includes the deleted organizations	
o	--limit	Number of items per page	v
o	--name	Performs a case-insensitive search for organizations which exactly match the specified name	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam organization show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam organization create
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam organization rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	iam organization apikeys
s	ls|list	List API Keys for your organization
s	show|describe	Get a specific Organization API Key
s	updates|assign	Update an Organization API Key
s	create	Create an Organization API Key
s	rm|delete	Delete an Organization API Key
s	accesslists|access-lists|accessList|accesslist|access-list|whitelists|whitelist|accessLists	Manage the IP access list for your API Key
@	iam organization apikeys ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam organization apikeys show
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam organization apikeys updates
o	--desc	Description of the API key	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	iam organization apikeys create
o	--desc	Description of the API key	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	iam organization apikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam organization apikeys accesslists
s	ls|list	List IP access list entries for your API Key
s	create	Create an IP access list for your API Key
s	rm|delete	Delete an IP access list from your API Key
@	iam organization apikeys accesslists ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam organization apikeys accesslists create
o	--apiKey	API Key	v
o	--cidr	Whitelist entry in CIDR notation to be added for a given API key	v
o	--ip	IP address to be allowed for a given API key	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam organization apikeys accesslists rm
o	--apiKey	API Key	v
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam organization user
s	ls|list	List users in a organization
@	iam organization user ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam organization invitation
s	ls|list	Retrieves all pending invitations to the specified organization
s	get|describe	Retrieve details for one pending invitation to the specified organization
s	rm|delete	Deletes one pending invitation to the specified organization
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
s	create|invite	Invites one user to the organization that you specify
@	iam organization invitation ls
o	--email	User's email address	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam organization invitation get
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam organization invitation rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
@	iam organization invitation updates
o	--email	User's email address	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	User's roles for the associated organization	v
@	iam organization invitation create
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	User's roles for the associated organization	v
o	--teamId	Unique identification of the team	v
@	iam globalapikeys
s	ls|list	List Global API Keys
s	show|describe	Get a specific Global API Key
s	create	Create a Global API Key
s	update	Update a Global API Key
s	rm|delete	Delete a Global API Key
@	iam globalapikeys ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam globalapikeys show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam globalapikeys create
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	iam globalapikeys update
o	--desc	Description of the API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--role	List of roles for the API key	v
@	iam globalapikeys rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	iam globalaccesslists
s	ls|list	List Atlas IP access list entries for Global API Key
s	show|describe	Return one Global IP access list entry
s	create	Create an IP access list for Global API Key
s	rm|delete	Delete an IP access list from Global API Key
@	iam globalaccesslists ls
o	--limit	Number of items per page	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam globalaccesslists show
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam globalaccesslists create
o	--cidr	Whitelist entry in CIDR notation to be added for a given API key	v
o	--desc	IP address to be allowed for a given API key	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam globalaccesslists rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	iam user
s	invite	Invite a user
s	get|describe	Get a user by username or id
s	rm|delete	Delete an Ops Manager user
@	iam user invite
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
@	iam user get
o	--id	Unique identifier of the user	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--username	Username of the user	v
@	iam user rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
@	iam team
s	ls|list	Get all teams in an organization
s	get|describe	Get a team in an organization
s	create	Create a team in an organization
s	user|users	Users operations
s	rm|delete	Delete a team from an organization
@	iam team ls
o	--limit	Number of items per page	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--page	Page number	v
@	iam team get
o	--id	Unique identification of the team	v
o	--name	Name of the team	v
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
@	iam team create
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--username	List of usernames to add to the new team	v
@	iam team user
s	ls|list	List users of a team
s	add	Add a user to a team
s	rm|delete	Delete user from a team
@	iam team user ls
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--teamId	Unique identification of the team	v
@	iam team user add
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--output|-o	Output format. Valid values are json, json-path, go-template, or go-template-file	v
o	--teamId	Unique identification of the team	v
@	iam team user rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
o	--teamId	Unique identification of the team	v
@	iam team rm
o	--force	If specified, skips asking for confirmation before proceeding with a requsted action	
o	--orgId	Organization ID to use. Overrides the settings in the configuration file or environment variable	v
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
s	config	Configure a profile to store access settings for your MongoDB deployment
s	atlas	MongoDB Atlas operations
s	cm|cloud-manager	MongoDB Cloud Manager operations
s	om|ops-manager	MongoDB Ops Manager operations
s	iam	Organization and projects operations
s	auth	Manage the CLI's authentication state
s	completion	Generate the autocompletion script for the specified shell
@	help config
s	set	Configure specific properties of a profile
s	ls|list	List available profiles
s	get|describe	Return a specific profile
s	mv|rename	Rename a profile
s	rm|delete	Delete a profile
@	help config set
@	help config ls
@	help config get
@	help config mv
@	help config rm
@	help atlas
s	quickstart	Create and access an Atlas Cluster
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
@	help atlas quickstart
@	help atlas cluster
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
@	help atlas cluster ls
@	help atlas cluster get
@	help atlas cluster create
@	help atlas cluster watch
@	help atlas cluster update
@	help atlas cluster pause
@	help atlas cluster start
@	help atlas cluster rm
@	help atlas cluster loadSampleData
@	help atlas cluster index
s	create	Create a rolling index for your MongoDB cluster
@	help atlas cluster index create
@	help atlas cluster fts
s	index|indexes	Manage Atlas Search indexes for your cluster
@	help atlas cluster fts index
s	ls|list	List Atlas search indexes for a cluster
s	create	Create a search index for a cluster
s	describe	Describe a search index for a cluster
s	update	Update a search index for a cluster
s	rm|delete	Delete a search index from a cluster
@	help atlas cluster fts index ls
@	help atlas cluster fts index create
@	help atlas cluster fts index describe
@	help atlas cluster fts index update
@	help atlas cluster fts index rm
@	help atlas cluster onlinearchives
s	ls|list	List online archives for a cluster
s	describe	Describe an online archive for a cluster
s	create	Create an online archive for a cluster
s	update	Update an online archive for a cluster
s	start	Start a paused online archive from a cluster
s	pause	Pause an online archive from a cluster
s	rm|delete	Delete an online archive from a cluster
s	watch	Watch for an archive to be available
@	help atlas cluster onlinearchives ls
@	help atlas cluster onlinearchives describe
@	help atlas cluster onlinearchives create
@	help atlas cluster onlinearchives update
@	help atlas cluster onlinearchives start
@	help atlas cluster onlinearchives pause
@	help atlas cluster onlinearchives rm
@	help atlas cluster onlinearchives watch
@	help atlas cluster connectionstrings
s	get|describe	Retrieve the SRV connection string of your MongoDB cluster
@	help atlas cluster connectionstrings get
@	help atlas dbuser
s	ls|list	List Atlas database users for your project
s	get|describe	Return a single Atlas database user for your project
s	create	Create a database user for your project
s	rm|delete	Delete a database user for your project
s	update	Update a database user for your project
s	cert|certs	Manage Atlas x509 certificates for your database users
@	help atlas dbuser ls
@	help atlas dbuser get
@	help atlas dbuser create
@	help atlas dbuser rm
@	help atlas dbuser update
@	help atlas dbuser cert
s	ls|list	List of all Atlas-managed, unexpired certificates for a database user
s	create	Create a new Atlas-managed X.509 certificate for the specified database user
@	help atlas dbuser cert ls
@	help atlas dbuser cert create
@	help atlas customdbroles
s	create	Create a custom database role for your project
s	get|describe	Return a single custom database role for your project
s	ls|list	List custom database roles for your project
s	rm|delete	Delete a custom database role for your project
s	update	Update a custom database role for your project
@	help atlas customdbroles create
@	help atlas customdbroles get
@	help atlas customdbroles ls
@	help atlas customdbroles rm
@	help atlas customdbroles update
@	help atlas accesslists
s	get|describe	Describe an IP access list entry
s	ls|list	List Atlas IP access list entries for your project
s	create	Create an IP access list for your project
s	rm|delete	Delete an IP access list from your project
@	help atlas accesslists get
@	help atlas accesslists ls
@	help atlas accesslists create
@	help atlas accesslists rm
@	help atlas datalakes
s	ls|list	List Atlas Data Lakes for your project
s	describe	Return a specific data lake
s	create	Create a new data lake for your project
s	rm|delete	Delete a data lake from your project
s	update	Update a data lake for your project
@	help atlas datalakes ls
@	help atlas datalakes describe
@	help atlas datalakes create
@	help atlas datalakes rm
@	help atlas datalakes update
@	help atlas alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	help atlas alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	help atlas alert config create
@	help atlas alert config ls
@	help atlas alert config rm
@	help atlas alert config field
s	types|type	Lists available field types for your alert configurations
@	help atlas alert config field types
@	help atlas alert config update
@	help atlas alert get
@	help atlas alert ls
@	help atlas alert ack
@	help atlas alert unack
@	help atlas alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	help atlas alert global ls
@	help atlas backup
s	snapshot|snapshots	Manage cloud backup snapshots for your project
s	restore|restores	Manage cloud backup restore jobs for your project
@	help atlas backup snapshot
s	ls|list	List cloud backup snapshots for your project and cluster
s	take|create	Create a backup snapshot for your project and cluster
s	describe	Get a specific snapshot for your project
s	watch	Watch for a snapshot to be available
s	rm|delete	Delete a backup snapshot
@	help atlas backup snapshot ls
@	help atlas backup snapshot take
@	help atlas backup snapshot describe
@	help atlas backup snapshot watch
@	help atlas backup snapshot rm
@	help atlas backup restore
s	ls|list	List cloud backup restore jobs for your project and cluster
s	start	Start a restore job for your project and cluster
@	help atlas backup restore ls
@	help atlas backup restore start
@	help atlas event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	help atlas event ls
@	help atlas event organization
s	ls|list	Return all events for an organization
@	help atlas event organization ls
@	help atlas event project
s	ls|list	Return all events for a project
@	help atlas event project ls
@	help atlas metric
s	process|processes	Get MongoDB process metrics for a given host
s	disk|disks	List available disks or disk metrics for a given host
s	database|databases	List available databases or database metrics for a given host
@	help atlas metric process
@	help atlas metric disk
s	ls|list	List available disks or disk partitions for a given host
s	describe	Describe disk partition metrics for a disk partition on a specified host
@	help atlas metric disk ls
@	help atlas metric disk describe
@	help atlas metric database
s	ls|list	List available databases or database metrics for a given host
s	describe	Describe database metrics for a database on a specific host
@	help atlas metric database ls
@	help atlas metric database describe
@	help atlas performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	help atlas performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	help atlas performanceadvisor namespace ls
@	help atlas performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	help atlas performanceadvisor slowquerylogs ls
@	help atlas performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	help atlas performanceadvisor suggestedindexes ls
@	help atlas performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	help atlas performanceadvisor slowOT ls
@	help atlas performanceadvisor slowOT disable
@	help atlas log
s	download	Download a host mongodb logs
@	help atlas log download
@	help atlas process
s	ls|list	List MongoDB processes for your project
@	help atlas process ls
@	help atlas privateendpoints
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
@	help atlas privateendpoints ls
@	help atlas privateendpoints get
@	help atlas privateendpoints create
@	help atlas privateendpoints rm
@	help atlas privateendpoints watch
@	help atlas privateendpoints interface
s	add|create	Add a new interface to a private endpoint
s	get|describe	Return a specific private endpoint interface for your project
s	rm|delete	Delete a private endpoint interface from your project
@	help atlas privateendpoints interface add
@	help atlas privateendpoints interface get
@	help atlas privateendpoints interface rm
@	help atlas privateendpoints aws
s	ls|list	List AWS Private Endpoints for your project
s	get|describe	Return a specific AWS Private Endpoints for your project
s	create	Create a new AWS Private Endpoint for your project
s	rm|delete	Delete a specific AWS Private Endpoint for your project
s	watch	Watch for a specific AWS Private Endpoint to be available
s	interface|interfaces	Manage Atlas AWS private endpoint interfaces
@	help atlas privateendpoints aws ls
@	help atlas privateendpoints aws get
@	help atlas privateendpoints aws create
@	help atlas privateendpoints aws rm
@	help atlas privateendpoints aws watch
@	help atlas privateendpoints aws interface
s	add|create	Add a new interface to a AWS private endpoint
s	get|describe	Return a specific AWS private endpoint interface for your project
s	rm|delete	Delete a specific AWS private endpoint interface and the related endpoint service for your project
@	help atlas privateendpoints aws interface add
@	help atlas privateendpoints aws interface get
@	help atlas privateendpoints aws interface rm
@	help atlas privateendpoints azure
s	ls|list	List Azure Private Endpoints for your project
s	get|describe	Return a specific Azure Private Endpoints for your project
s	create	Create a new Azure Private Endpoint for your project
s	rm|delete	Delete a specific Azure Private Endpoint for your project
s	watch	Watch for a specific Azure Private Endpoint to be available
s	interface|interfaces	Manage Atlas Azure private endpoint interfaces
@	help atlas privateendpoints azure ls
@	help atlas privateendpoints azure get
@	help atlas privateendpoints azure create
@	help atlas privateendpoints azure rm
@	help atlas privateendpoints azure watch
@	help atlas privateendpoints azure interface
s	add|create	Add a new Azure interface to a private endpoint
s	get|describe	Return a specific Azure private endpoint interface for your project
s	rm|delete	Delete a specific Azure private endpoint interface and related service for your project
@	help atlas privateendpoints azure interface add
@	help atlas privateendpoints azure interface get
@	help atlas privateendpoints azure interface rm
@	help atlas privateendpoints gcp
s	create	Create a new GCP private endpoint for your project
s	rm|delete	Delete a GCP private endpoint for your project
s	ls|list	List GCP private endpoints for your project
s	get|describe	Return a specific GCP private endpoint for your project
s	watch	Watch the specified GCP private endpoint to detect changes in the endpoint's state
s	interface|interfaces	Manage Atlas GCP private endpoint interfaces
@	help atlas privateendpoints gcp create
@	help atlas privateendpoints gcp rm
@	help atlas privateendpoints gcp ls
@	help atlas privateendpoints gcp get
@	help atlas privateendpoints gcp watch
@	help atlas privateendpoints gcp interface
s	get|describe	Return a specific GCP private endpoint interface for your project
s	rm|delete	Delete a specific GCP private endpoint interface for your project
s	add|create	Create a GCP private endpoint interface
@	help atlas privateendpoints gcp interface get
@	help atlas privateendpoints gcp interface rm
@	help atlas privateendpoints gcp interface add
@	help atlas privateendpoints regionalmodes
s	enable	Enable the regionalized private endpoint setting for your Atlas project
s	disable	Disable the regionalized private endpoint setting for your Atlas project
s	get|describe	Get the regionalized private endpoint setting for your Atlas project
@	help atlas privateendpoints regionalmodes enable
@	help atlas privateendpoints regionalmodes disable
@	help atlas privateendpoints regionalmodes get
@	help atlas privateendpoints datalakes
s	aws	Manage AWS private endpoints
@	help atlas privateendpoints datalakes aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	help atlas privateendpoints datalakes aws create
@	help atlas privateendpoints datalakes aws ls
@	help atlas privateendpoints datalakes aws get
@	help atlas privateendpoints datalakes aws rm
@	help atlas privateendpoints onlinearchive
s	aws	Manage AWS private endpoints
@	help atlas privateendpoints onlinearchive aws
s	create	Create a new Data Lake private endpoint for your project
s	ls|list	List Data Lake private endpoints for your project
s	get|describe	Return a specific Data Lake private endpoint for your project
s	rm|delete	Delete a specific Data Lake private endpoint for your project
@	help atlas privateendpoints onlinearchive aws create
@	help atlas privateendpoints onlinearchive aws ls
@	help atlas privateendpoints onlinearchive aws get
@	help atlas privateendpoints onlinearchive aws rm
@	help atlas networking
s	container|containers	Manage Network Peering containers
s	peering	Manage Network Peering connections
@	help atlas networking container
s	ls|list	List network peering containers in an Atlas project
s	rm|delete	Remove one network peering container in an Atlas project
@	help atlas networking container ls
@	help atlas networking container rm
@	help atlas networking peering
s	ls|list	Retrieve details for all network peering connections in one Atlas project
s	create	Create a connection with AWS, Azure and Google Cloud
s	watch	Watch for a peering connection to be available
s	rm|delete	Delete a peering connection from an Atlas project
@	help atlas networking peering ls
@	help atlas networking peering create
s	azure	Create a connection with Azure
s	aws	Create a connection with AWS
s	gcp	Create a connection with GCP
@	help atlas networking peering create azure
@	help atlas networking peering create aws
@	help atlas networking peering create gcp
@	help atlas networking peering watch
@	help atlas networking peering rm
@	help atlas security
s	customercerts|customer-certs|customerCert|customercert|customer-cert|certs|customerCerts	Manage customer x509 certificates for your project
s	ldap	LDAP operations
@	help atlas security customercerts
s	describe	Get the current customer-managed X.509 configuration details for an Atlas project
s	create	Saves a customer-managed X.509 configuration for an Atlas project
s	disable	Disables customer-managed X.509 for a project
@	help atlas security customercerts describe
@	help atlas security customercerts create
@	help atlas security customercerts disable
@	help atlas security ldap
s	verify	Request verification of an LDAP configuration
s	save	Save an LDAP configuration
s	rm|delete	Delete an LDAP configuration userToDNMapping from an LDAP configuration
s	get	Get an LDAP configuration
@	help atlas security ldap verify
s	status	Get the status of an LDAP configuration request
@	help atlas security ldap verify status
s	watch	Watch for an LDAP configuration request to complete
@	help atlas security ldap verify status watch
@	help atlas security ldap save
@	help atlas security ldap rm
@	help atlas security ldap get
@	help atlas integration
s	update|create	Create operations
s	ls|list	List third party integrations
s	rm|delete	Delete a third party integration
s	describe	Get a third party integration
@	help atlas integration update
s	new_relic|newRelic|NEW_RELIC	Create or update the New Relic integration
s	ops_genie|opsGenie|OPS_GENIE	Create or update the Ops Genie integration
s	pager_duty|pagerDuty|PAGER_DUTY	Create or update the PagerDuty integration
s	datadog|DATADOG	Create or update the Datadog integration
s	victor_ops|victorOps|VICTOR_OPS	Create or update the VictorOps integrations
s	flowdock|FLOWDOCK	Create or update the Flowdock integration
s	webhook|WEBHOOK	Create or update the Webhook integration
@	help atlas integration update new_relic
@	help atlas integration update ops_genie
@	help atlas integration update pager_duty
@	help atlas integration update datadog
@	help atlas integration update victor_ops
@	help atlas integration update flowdock
@	help atlas integration update webhook
@	help atlas integration ls
@	help atlas integration rm
@	help atlas integration describe
@	help atlas maintenancewindows
s	update	Update the maintenance window
s	rm|delete|clear	Clear the maintenance window
s	defer	Defer the maintenance window
s	get|describe	Get a maintenance window
@	help atlas maintenancewindows update
@	help atlas maintenancewindows rm
@	help atlas maintenancewindows defer
@	help atlas maintenancewindows get
@	help atlas customdns
s	aw|aws	Manage DNS configuration of an Atlas project’s cluster deployed to AWS
@	help atlas customdns aw
s	enable	Enable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	disable	Disable the custom DNS configuration of an Atlas project’s cluster deployed to AWS
s	get|describe	Describe the custom DNS configuration of an Atlas project’s cluster deployed to AWS
@	help atlas customdns aw enable
@	help atlas customdns aw disable
@	help atlas customdns aw get
@	help atlas cloudproviders
s	accessroles|access-roles|accessRole|accessrole|access-role|accessRoles	Manage AWS IAM role access in Atlas
@	help atlas cloudproviders accessroles
s	aws	Manage AWS IAM role access in Atlas
s	ls|list	List AWS IAM role access in Atlas
@	help atlas cloudproviders accessroles aws
s	create	Create an AWS IAM role
s	authorize	Authorize an AWS IAM role
s	deauthorize	Deauthorize an AWS IAM role
@	help atlas cloudproviders accessroles aws create
@	help atlas cloudproviders accessroles aws authorize
@	help atlas cloudproviders accessroles aws deauthorize
@	help atlas cloudproviders accessroles ls
@	help atlas sl
s	ls|list	Return all serverless instances in the specified project
s	get|describe	Return one serverless instance in the specified project
s	rm|delete	Remove a serverless instance from your project
s	create	Creates one serverless instance in the specified project
s	watch	Monitor the status of serverless instance
@	help atlas sl ls
@	help atlas sl get
@	help atlas sl rm
@	help atlas sl create
@	help atlas sl watch
@	help atlas livemigrations
s	link	Manage the link-token for your organization
s	validation	Manage a Live Migration validation job for your project
s	create	Create one new migration
s	get|describe	Return one migration job
s	cutover	Start the cutover and confirm when the cutover completes. When the cutover completes, the…
@	help atlas livemigrations link
s	create	Create one new link-token
s	rm|delete	Delete one link-token
@	help atlas livemigrations link create
@	help atlas livemigrations link rm
@	help atlas livemigrations validation
s	create	Create one new validation request
s	get|describe	Return one validation job
@	help atlas livemigrations validation create
@	help atlas livemigrations validation get
@	help atlas livemigrations create
@	help atlas livemigrations get
@	help atlas livemigrations cutover
@	help atlas accesslogs
s	ls|list	Retrieve the access logs of a cluster identified by the cluster's name or hostname
@	help atlas accesslogs ls
@	help cm
s	cluster|clusters	Manage clusters for your project
s	alert|alerts	Manage alerts for your project
s	backup|backups	Manage continuous backups for your project
s	server|servers	Manage automated servers for your project
s	automation	Manage automation configuration for your project
s	security	Manage security configuration for your project
s	dbuser|databaseUsers|databaseUser|dbusers	Manage database users for your project
s	event|events	Manage events for your organization or project
s	monitoring	Manage monitoring for your project
s	process|processes	Manage MongoDB processes for your project
s	metric|measurements|measurement|metrics	Get measurements on the state of the MongoDB process
s	log|logs	Manage log collection jobs for your project
s	agent|agents	Manage MongoDB Agents
s	maintenancewindows|maintenance-windows|maintenanceWindow|maintenancewindow|maintenance-window|maintenanceWindows	Manage Ops Manager/Cloud Manager maintenance windows
s	performanceadvisor|performance-advisor|performanceAdvisor	Performance Advisor operations
s	featurepolicies|feature-policies|featurePolicy|featurepolicy|feature-policy|featurePolicies	Manage feature control policies
s	livemigrations|live-migrations|liveMigration|livemigration|live-migration|lm|liveMigrations	Manage a Live Migration to Atlas for your organization
@	help cm cluster
s	ls|list	List clusters for your project
s	describe	Describe a cluster
s	create	Create a MongoDB cluster
s	update	Update a MongoDB cluster
s	rm|delete	Completely removes a cluster from your project
s	apply	Apply a new cluster configuration for your project
s	index|indexes	Manage cluster rolling indexes for your project
s	unmanage	Stop managing a cluster via automation
s	restart	Restart a cluster for your project
s	startup	Start up a cluster for your project
s	shutdown	Shutdown a cluster for your project
s	rfs|reclaimFreeSpace	Reclaim unused space for a cluster
@	help cm cluster ls
@	help cm cluster describe
@	help cm cluster create
@	help cm cluster update
@	help cm cluster rm
@	help cm cluster apply
@	help cm cluster index
s	create	Create a rolling index for your MongoDB cluster
@	help cm cluster index create
@	help cm cluster unmanage
@	help cm cluster restart
@	help cm cluster startup
@	help cm cluster shutdown
@	help cm cluster rfs
@	help cm alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	help cm alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	help cm alert config create
@	help cm alert config ls
@	help cm alert config rm
@	help cm alert config field
s	types|type	Lists available field types for your alert configurations
@	help cm alert config field types
@	help cm alert config update
@	help cm alert get
@	help cm alert ls
@	help cm alert ack
@	help cm alert unack
@	help cm alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	help cm alert global ls
@	help cm backup
s	snapshot|snapshots	Manage backup snapshots for your project
s	restore|restores	Manage restore jobs for your project
s	checkpoint|checkpoints	Manage backup checkpoints for your project
s	enable	Enable backup for a given hostname
s	disable	Disable backup for a given hostname
s	config	Manage backup configurations for your project
@	help cm backup snapshot
s	ls|list	List snapshots for a project and cluster
s	schedule	Manage backup snapshot schedules for a cluster
@	help cm backup snapshot ls
@	help cm backup snapshot schedule
s	get|describe	Describe a snapshot schedule for a cluster
s	update	Update a snapshot schedule for a cluster
@	help cm backup snapshot schedule get
@	help cm backup snapshot schedule update
@	help cm backup restore
s	ls|list	Lists restore jobs for a project and cluster
s	start	Start a restore job for a project and cluster
@	help cm backup restore ls
@	help cm backup restore start
@	help cm backup checkpoint
s	ls|list	List continuous backup checkpoints for your project
@	help cm backup checkpoint ls
@	help cm backup enable
@	help cm backup disable
@	help cm backup config
s	get|describe	Get a backup configuration
s	ls|list	List backup configurations for your project
s	update	Update a backup configuration
@	help cm backup config get
@	help cm backup config ls
@	help cm backup config update
@	help cm server
s	ls|list	List all available servers running an automation agent for your project
@	help cm server ls
@	help cm automation
s	status	Show the current status of the automation config
s	show|get|describe	Get the current automation configuration for a project
s	update	Update the current automation configuration for a project
s	watch	Watch for automation changes to be completed
@	help cm automation status
@	help cm automation show
@	help cm automation update
@	help cm automation watch
@	help cm security
s	enable	Enable authentication mechanisms for your project
@	help cm security enable
@	help cm dbuser
s	create	Create a database user for your project
s	ls|list	List Atlas database users for your project
s	rm|delete	Delete a database user for your project
@	help cm dbuser create
@	help cm dbuser ls
@	help cm dbuser rm
@	help cm event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	help cm event ls
@	help cm event organization
s	ls|list	Return all events for an organization
@	help cm event organization ls
@	help cm event project
s	ls|list	Return all events for a project
@	help cm event project ls
@	help cm monitoring
s	enable	Enable monitoring for a given hostname
s	disable	Disable monitoring for a given hostname
s	rm|stop	Stops monitoring the MongoDB process specified
@	help cm monitoring enable
@	help cm monitoring disable
@	help cm monitoring rm
@	help cm process
s	ls|list	List MongoDB processes for your project
s	get|describe	Describe MongoDB processes for your project
@	help cm process ls
@	help cm process get
@	help cm metric
s	processes|process	Get measurements for a given host
s	disk|disks	List available disks or disks measurements for a given host
s	database|databases	List available databases or databases measurements for a given host
@	help cm metric processes
@	help cm metric disk
s	ls|list	List available disks for a given host
s	describe	Describe disks measurements for a given host partition
@	help cm metric disk ls
@	help cm metric disk describe
@	help cm metric database
s	ls|list	List available databases for a given host
s	describe	Describe database measurements for a given host database
@	help cm metric database ls
@	help cm metric database describe
@	help cm log
s	job|jobs	Manage log collection jobs for your project
@	help cm log job
s	collect	Start a job to collect logs for your project
s	ls|list	List log collection jobs for your project
s	download	Download logs generated by a log collection job
s	rm|delete	Delete a log collection job from your project
@	help cm log job collect
@	help cm log job ls
@	help cm log job download
@	help cm log job rm
@	help cm agent
s	ls|list	List available MongoDB Agents for your project
s	upgrade	Upgrade MongoDB Agents to the latest available version
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Agent API Keys operations
s	version|versions	Manage MongoDB Agents versions
@	help cm agent ls
@	help cm agent upgrade
@	help cm agent apikeys
s	ls|list	List available MongoDB Agent API Keys for your project
s	create	Create an Agent API Key for your project
s	rm|delete	Delete an Agent API Key for your project
@	help cm agent apikeys ls
@	help cm agent apikeys create
@	help cm agent apikeys rm
@	help cm agent version
s	ls|list	List MongoDB Agent versions in the provided project
@	help cm agent version ls
@	help cm maintenancewindows
s	create	Create a maintenance window
s	ls|list	List maintenance windows
s	rm|delete	Delete a maintenance window
s	describe	Get a maintenance window
s	update	Update a maintenance window
@	help cm maintenancewindows create
@	help cm maintenancewindows ls
@	help cm maintenancewindows rm
@	help cm maintenancewindows describe
@	help cm maintenancewindows update
@	help cm performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	help cm performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	help cm performanceadvisor namespace ls
@	help cm performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	help cm performanceadvisor slowquerylogs ls
@	help cm performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	help cm performanceadvisor suggestedindexes ls
@	help cm performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	help cm performanceadvisor slowOT ls
@	help cm performanceadvisor slowOT disable
@	help cm featurepolicies
s	ls|list	List feature control policies for your project
s	update	Update feature control policies for your project
@	help cm featurepolicies ls
@	help cm featurepolicies update
@	help cm livemigrations
s	link	Manage the link-token for your organization
@	help cm livemigrations link
s	create	Create one new organization link
s	rm|delete	Delete one link-token
s	get|describe	Return the status of the connection between the specified source organization and the target…
@	help cm livemigrations link create
@	help cm livemigrations link rm
@	help cm livemigrations link get
@	help om
s	cluster|clusters	Manage clusters for your project
s	alert|alerts	Manage alerts for your project
s	backup|backups	Manage continuous backups for your project
s	server|servers	Manage automated servers for your project
s	automation	Manage automation configuration for your project
s	security	Manage security configuration for your project
s	dbuser|databaseUsers|databaseUser|dbusers	Manage database users for your project
s	owner	Manage Ops Manager owners
s	event|events	Manage events for your organization or project
s	monitoring	Manage monitoring for your project
s	process|processes	Manage MongoDB processes for your project
s	metric|measurements|measurement|metrics	Get measurements on the state of the MongoDB process
s	log|logs	Manage log collection jobs for your project
s	agent|agents	Manage MongoDB Agents
s	diagnosearchives|diagnose-archives|diagnoseArchive|diagnosearchive|diagnose-archive|diagnoseArchives	Manage diagnose archives
s	maintenancewindows|maintenance-windows|maintenanceWindow|maintenancewindow|maintenance-window|maintenanceWindows	Manage Ops Manager/Cloud Manager maintenance windows
s	performanceadvisor|performance-advisor|performanceAdvisor	Performance Advisor operations
s	versionmanifest|version-manifest|versionManifest	Manage Ops Manager version manifest
s	admin	Manage backup administration
s	softwarecomponents|software-components|softwareComponent|softwarecomponent|software-component|softwareComponents	Manage earliest and latest versions of MongoDB Agent, MongoDB Tools, and BI Connector in your…
s	featurepolicies|feature-policies|featurePolicy|featurepolicy|feature-policy|featurePolicies	Manage feature control policies
s	serverusage|server-usage|serverUsage	Manage your server usage
s	livemigrations|live-migrations|liveMigration|livemigration|live-migration|lm|liveMigrations	Manage a Live Migration to Atlas for your organization
@	help om cluster
s	ls|list	List clusters for your project
s	describe	Describe a cluster
s	create	Create a MongoDB cluster
s	update	Update a MongoDB cluster
s	rm|delete	Completely removes a cluster from your project
s	apply	Apply a new cluster configuration for your project
s	index|indexes	Manage cluster rolling indexes for your project
s	unmanage	Stop managing a cluster via automation
s	restart	Restart a cluster for your project
s	startup	Start up a cluster for your project
s	shutdown	Shutdown a cluster for your project
s	rfs|reclaimFreeSpace	Reclaim unused space for a cluster
@	help om cluster ls
@	help om cluster describe
@	help om cluster create
@	help om cluster update
@	help om cluster rm
@	help om cluster apply
@	help om cluster index
s	create	Create a rolling index for your MongoDB cluster
@	help om cluster index create
@	help om cluster unmanage
@	help om cluster restart
@	help om cluster startup
@	help om cluster shutdown
@	help om cluster rfs
@	help om alert
s	config|settings	Manages alerts configuration for your project
s	get|describe	Retrieves one alert for the specified project
s	ls|list	Retrieves all alerts for the specified Atlas project
s	ack|acknowledge	Acknowledges one alert for the specified project
s	unack|unacknowledge	Unacknowledges one alert for the specified project
s	global	Retrieves all the global alerts for the specified Ops Manager project
@	help om alert config
s	create	Creates one alert configuration in the specified project
s	ls|list	Returns alert configurations for the specified project
s	rm|delete	Deletes the specified alert configuration in a specified project
s	field|fields	Manages alert configuration fields for your project
s	update	Updates one alert configuration in the specified project
@	help om alert config create
@	help om alert config ls
@	help om alert config rm
@	help om alert config field
s	types|type	Lists available field types for your alert configurations
@	help om alert config field types
@	help om alert config update
@	help om alert get
@	help om alert ls
@	help om alert ack
@	help om alert unack
@	help om alert global
s	ls|list	Returns all global alerts for the specified Ops Manager project
@	help om alert global ls
@	help om backup
s	snapshot|snapshots	Manage backup snapshots for your project
s	restore|restores	Manage restore jobs for your project
s	checkpoint|checkpoints	Manage backup checkpoints for your project
s	enable	Enable backup for a given hostname
s	disable	Disable backup for a given hostname
s	config	Manage backup configurations for your project
@	help om backup snapshot
s	ls|list	List snapshots for a project and cluster
s	schedule	Manage backup snapshot schedules for a cluster
@	help om backup snapshot ls
@	help om backup snapshot schedule
s	get|describe	Describe a snapshot schedule for a cluster
s	update	Update a snapshot schedule for a cluster
@	help om backup snapshot schedule get
@	help om backup snapshot schedule update
@	help om backup restore
s	ls|list	Lists restore jobs for a project and cluster
s	start	Start a restore job for a project and cluster
@	help om backup restore ls
@	help om backup restore start
@	help om backup checkpoint
s	ls|list	List continuous backup checkpoints for your project
@	help om backup checkpoint ls
@	help om backup enable
@	help om backup disable
@	help om backup config
s	get|describe	Get a backup configuration
s	ls|list	List backup configurations for your project
s	update	Update a backup configuration
@	help om backup config get
@	help om backup config ls
@	help om backup config update
@	help om server
s	ls|list	List all available servers running an automation agent for your project
@	help om server ls
@	help om automation
s	status	Show the current status of the automation config
s	show|get|describe	Get the current automation configuration for a project
s	update	Update the current automation configuration for a project
s	watch	Watch for automation changes to be completed
@	help om automation status
@	help om automation show
@	help om automation update
@	help om automation watch
@	help om security
s	enable	Enable authentication mechanisms for your project
@	help om security enable
@	help om dbuser
s	create	Create a database user for your project
s	ls|list	List Atlas database users for your project
s	rm|delete	Delete a database user for your project
@	help om dbuser create
@	help om dbuser ls
@	help om dbuser rm
@	help om owner
s	create	Create the first user for Ops Manager
@	help om owner create
@	help om event
s	ls|list	Return all events for an organization or project
s	organization|orgs|org|organizations	Organization operations
s	project|projects	Project operations
@	help om event ls
@	help om event organization
s	ls|list	Return all events for an organization
@	help om event organization ls
@	help om event project
s	ls|list	Return all events for a project
@	help om event project ls
@	help om monitoring
s	enable	Enable monitoring for a given hostname
s	disable	Disable monitoring for a given hostname
s	rm|stop	Stops monitoring the MongoDB process specified
@	help om monitoring enable
@	help om monitoring disable
@	help om monitoring rm
@	help om process
s	ls|list	List MongoDB processes for your project
s	get|describe	Describe MongoDB processes for your project
@	help om process ls
@	help om process get
@	help om metric
s	processes|process	Get measurements for a given host
s	disk|disks	List available disks or disks measurements for a given host
s	database|databases	List available databases or databases measurements for a given host
@	help om metric processes
@	help om metric disk
s	ls|list	List available disks for a given host
s	describe	Describe disks measurements for a given host partition
@	help om metric disk ls
@	help om metric disk describe
@	help om metric database
s	ls|list	List available databases for a given host
s	describe	Describe database measurements for a given host database
@	help om metric database ls
@	help om metric database describe
@	help om log
s	job|jobs	Manage log collection jobs for your project
@	help om log job
s	collect	Start a job to collect logs for your project
s	ls|list	List log collection jobs for your project
s	download	Download logs generated by a log collection job
s	rm|delete	Delete a log collection job from your project
@	help om log job collect
@	help om log job ls
@	help om log job download
@	help om log job rm
@	help om agent
s	ls|list	List available MongoDB Agents for your project
s	upgrade	Upgrade MongoDB Agents to the latest available version
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Agent API Keys operations
s	version|versions	Manage MongoDB Agents versions
@	help om agent ls
@	help om agent upgrade
@	help om agent apikeys
s	ls|list	List available MongoDB Agent API Keys for your project
s	create	Create an Agent API Key for your project
s	rm|delete	Delete an Agent API Key for your project
@	help om agent apikeys ls
@	help om agent apikeys create
@	help om agent apikeys rm
@	help om agent version
s	ls|list	List MongoDB Agent versions in the provided project
@	help om agent version ls
@	help om diagnosearchives
s	get|download	Download diagnose archives
@	help om diagnosearchives get
@	help om maintenancewindows
s	create	Create a maintenance window
s	ls|list	List maintenance windows
s	rm|delete	Delete a maintenance window
s	describe	Get a maintenance window
s	update	Update a maintenance window
@	help om maintenancewindows create
@	help om maintenancewindows ls
@	help om maintenancewindows rm
@	help om maintenancewindows describe
@	help om maintenancewindows update
@	help om performanceadvisor
s	namespace|namespaces	Retrieve namespaces for collections experiencing slow queries
s	slowquerylogs|slow-query-logs|slowQueryLog|slowquerylog|slow-query-log|slowQueryLogs	Get log lines for slow queries for a specified host
s	suggestedindexes|suggested-indexes|suggestedIndex|suggestedindex|suggested-index|suggestedIndexes	Get suggested indexes for collections experiencing slow queries
s	slowOT|sot|slowMS|slowOperationThreshold	Enable or disable management of the slow operation threshold for your cluster
@	help om performanceadvisor namespace
s	ls|list	Retrieve up to 20 namespaces for collections experiencing slow queries for a specified host
@	help om performanceadvisor namespace ls
@	help om performanceadvisor slowquerylogs
s	ls|list	Return log lines for slow queries that the Performance Advisor and Query Profiler identified
@	help om performanceadvisor slowquerylogs ls
@	help om performanceadvisor suggestedindexes
s	ls|list	Retrieve suggested indexes for collections experiencing slow queries
@	help om performanceadvisor suggestedindexes ls
@	help om performanceadvisor slowOT
s	ls|enable	Enable the application-managed slow operation threshold for your project
s	disable	Disable the application-managed slow operation threshold for your project
@	help om performanceadvisor slowOT ls
@	help om performanceadvisor slowOT disable
@	help om versionmanifest
s	update	Update Ops Manager version manifest
@	help om versionmanifest update
@	help om admin
s	backup|backups	Manage backup administration
@	help om admin backup
s	blockstore|blockstores	Manage backup blockstore configurations
s	filesystems|file-systems|fileSystem|filesystem|file-system|fileSystems	Manage file system configurations
s	s3	Manage backup s3 blockstore configurations
s	oplog	Manage backup oplog configurations
s	sync	Manage backup sync configurations
@	help om admin backup blockstore
s	ls|list	List backup blockstore configurations
s	get|describe	Get a backup blockstore configuration
s	create	Create a backup blockstore configuration
s	update	Update a backup blockstore configuration
s	rm|delete	Delete a backup blockstore configuration
@	help om admin backup blockstore ls
@	help om admin backup blockstore get
@	help om admin backup blockstore create
@	help om admin backup blockstore update
@	help om admin backup blockstore rm
@	help om admin backup filesystems
s	ls|list	List file system configurations
s	get|describe	Get a file system configuration
s	rm|delete	Delete a file system configuration
s	create	Create a file system configuration
s	update	Update a file system configuration
@	help om admin backup filesystems ls
@	help om admin backup filesystems get
@	help om admin backup filesystems rm
@	help om admin backup filesystems create
@	help om admin backup filesystems update
@	help om admin backup s3
s	ls|list	List backup s3 blockstore configurations
s	rm|delete	Delete a backup s3 blockstore configuration
s	create	Create a backup S3 blockstore configuration
s	update	Update a backup S3 blockstore configuration
s	get|describe	Get a backup s3 blockstore configuration
@	help om admin backup s3 ls
@	help om admin backup s3 rm
@	help om admin backup s3 create
@	help om admin backup s3 update
@	help om admin backup s3 get
@	help om admin backup oplog
s	ls|list	List backup oplog configurations
s	get|describe	Get a backup oplog configuration
s	create	Create a backup oplog configuration
s	update	Update a backup oplog configuration
s	rm|delete	Delete a backup oplog configuration
@	help om admin backup oplog ls
@	help om admin backup oplog get
@	help om admin backup oplog create
@	help om admin backup oplog update
@	help om admin backup oplog rm
@	help om admin backup sync
s	ls|list	List backup sync configurations
s	rm|delete	Delete a backup sync configuration
s	create	Create a backup sync configuration
s	update	Update a backup sync configuration
s	get|describe	Get a backup sync configuration
@	help om admin backup sync ls
@	help om admin backup sync rm
@	help om admin backup sync create
@	help om admin backup sync update
@	help om admin backup sync get
@	help om softwarecomponents
s	ls|list	List versions of MongoDB Agent, MongoDB Tools, and BI Connector in your environment
@	help om softwarecomponents ls
@	help om featurepolicies
s	ls|list	List feature control policies for your project
s	update	Update feature control policies for your project
@	help om featurepolicies ls
@	help om featurepolicies update
@	help om serverusage
s	project|projects	Manage your server usage for a project
s	organization|organizations	Manage your server usage for an organization
s	capture	Capture a snapshot of usage for the processes Ops Manager manages
s	download	Download the server usage report
@	help om serverusage project
s	servertype|server-type|serverType	Manage your server type for a project
s	host|hosts	Manage host assignment for a project
@	help om serverusage project servertype
s	get|describe	Get the default server type for a project
s	set	Set the default server type for a project
@	help om serverusage project servertype get
@	help om serverusage project servertype set
@	help om serverusage project host
s	ls|list	List all host assignments for one project
@	help om serverusage project host ls
@	help om serverusage organization
s	servertype|server-type|serverType	Manage your server type for an organization
s	host|hosts	Manage host assignment for an organization
@	help om serverusage organization servertype
s	get|describe	Get the default server type for an organization
s	set	Set the default server type for an organization
@	help om serverusage organization servertype get
@	help om serverusage organization servertype set
@	help om serverusage organization host
s	ls|list	List all host assignments for one organization
@	help om serverusage organization host ls
@	help om serverusage capture
@	help om serverusage download
@	help om livemigrations
s	link	Manage the link-token for your organization
@	help om livemigrations link
s	create	Create one new organization link
s	rm|delete	Delete one link-token
s	get|describe	Return the status of the connection between the specified source organization and the target…
@	help om livemigrations link create
@	help om livemigrations link rm
@	help om livemigrations link get
@	help iam
s	project|projects	Project operations
s	organization|orgs|org|organizations	Organization operations
s	globalapikeys|global-api-keys|globalApiKey|globalapikey|global-api-key|globalApiKeys	Global API Keys operations
s	globalaccesslists|global-access-lists|globalAccessList|globalaccesslist|global-access-list|globalWhitelists|globalwhitelists|global-whitelists|globalWhitelist|globalwhitelist|global-whitelist|globalAccessLists	Manage IP access list for Global API Key
s	user|users	Users operations
s	team|teams	Teams operations
@	help iam project
s	ls|list	List projects
s	create	Create a project
s	rm|delete	Delete a project
s	show|get|describe	Describe a project
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Manage API Keys for your project
s	user|users	Manage users for a project
s	team|teams	Teams operations
s	invitation|invitations	Invitation operations
@	help iam project ls
@	help iam project create
@	help iam project rm
@	help iam project show
@	help iam project apikeys
s	ls|list	List API Keys for your project
s	create	Create an API Key for your project
s	rm|delete	Delete an API Key for your project
s	update|assign	Assign an API Key to a project
@	help iam project apikeys ls
@	help iam project apikeys create
@	help iam project apikeys rm
@	help iam project apikeys update
@	help iam project user
s	ls|list	List all users for a project
s	rm|delete	Delete user from a project
@	help iam project user ls
@	help iam project user rm
@	help iam project team
s	ls|list	Get all teams in a project
s	add	Add team to a project
s	rm|delete	Delete team from a project
s	updates|update	Update roles for a team in a project
@	help iam project team ls
@	help iam project team add
@	help iam project team rm
@	help iam project team updates
@	help iam project invitation
s	ls|list	Retrieves all pending invitations to the specified project
s	get|describe	Retrieve details for one pending invitation to the specified project
s	rm|delete	Deletes one pending invitation to the specified project
s	create|invite	Invites one user to the project that you specify
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
@	help iam project invitation ls
@	help iam project invitation get
@	help iam project invitation rm
@	help iam project invitation create
@	help iam project invitation updates
@	help iam organization
s	ls|list	List organizations
s	show|describe	Describe an organizations
s	create	Create an organization
s	rm|delete	Delete an organization
s	apikeys|api-keys|apiKey|apikey|api-key|apiKeys	Organization API Keys operations
s	user|users	Users operations
s	invitation|invitations	Invitation operations
@	help iam organization ls
@	help iam organization show
@	help iam organization create
@	help iam organization rm
@	help iam organization apikeys
s	ls|list	List API Keys for your organization
s	show|describe	Get a specific Organization API Key
s	updates|assign	Update an Organization API Key
s	create	Create an Organization API Key
s	rm|delete	Delete an Organization API Key
s	accesslists|access-lists|accessList|accesslist|access-list|whitelists|whitelist|accessLists	Manage the IP access list for your API Key
@	help iam organization apikeys ls
@	help iam organization apikeys show
@	help iam organization apikeys updates
@	help iam organization apikeys create
@	help iam organization apikeys rm
@	help iam organization apikeys accesslists
s	ls|list	List IP access list entries for your API Key
s	create	Create an IP access list for your API Key
s	rm|delete	Delete an IP access list from your API Key
@	help iam organization apikeys accesslists ls
@	help iam organization apikeys accesslists create
@	help iam organization apikeys accesslists rm
@	help iam organization user
s	ls|list	List users in a organization
@	help iam organization user ls
@	help iam organization invitation
s	ls|list	Retrieves all pending invitations to the specified organization
s	get|describe	Retrieve details for one pending invitation to the specified organization
s	rm|delete	Deletes one pending invitation to the specified organization
s	updates|update	Updates one pending invitation by invitationId or email to the project that you specify
s	create|invite	Invites one user to the organization that you specify
@	help iam organization invitation ls
@	help iam organization invitation get
@	help iam organization invitation rm
@	help iam organization invitation updates
@	help iam organization invitation create
@	help iam globalapikeys
s	ls|list	List Global API Keys
s	show|describe	Get a specific Global API Key
s	create	Create a Global API Key
s	update	Update a Global API Key
s	rm|delete	Delete a Global API Key
@	help iam globalapikeys ls
@	help iam globalapikeys show
@	help iam globalapikeys create
@	help iam globalapikeys update
@	help iam globalapikeys rm
@	help iam globalaccesslists
s	ls|list	List Atlas IP access list entries for Global API Key
s	show|describe	Return one Global IP access list entry
s	create	Create an IP access list for Global API Key
s	rm|delete	Delete an IP access list from Global API Key
@	help iam globalaccesslists ls
@	help iam globalaccesslists show
@	help iam globalaccesslists create
@	help iam globalaccesslists rm
@	help iam user
s	invite	Invite a user
s	get|describe	Get a user by username or id
s	rm|delete	Delete an Ops Manager user
@	help iam user invite
@	help iam user get
@	help iam user rm
@	help iam team
s	ls|list	Get all teams in an organization
s	get|describe	Get a team in an organization
s	create	Create a team in an organization
s	user|users	Users operations
s	rm|delete	Delete a team from an organization
@	help iam team ls
@	help iam team get
@	help iam team create
@	help iam team user
s	ls|list	List users of a team
s	add	Add a user to a team
s	rm|delete	Delete user from a team
@	help iam team user ls
@	help iam team user add
@	help iam team user rm
@	help iam team rm
@	help auth
s	login	Authenticate with MongoDB Atlas
s	whoami	Verifies and displays information about your authentication state
s	logout	Log out of the CLI
@	help auth login
@	help auth whoami
@	help auth logout
@	help completion
s	bash	Generate the autocompletion script for bash
s	zsh	Generate the autocompletion script for zsh
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
@	help completion bash
@	help completion zsh
@	help completion fish
@	help completion powershell

@	
s	admin	Work with your Power Platform Admin Account
s	application	Commands for listing and installing available Dataverse applications from AppSource
s	auth	Manage how you authenticate to various services
s	canvas	Operating with Power Apps .msapp files
s	catalog	Commands for working with Catalog in Power Platform
s	connection	Commands for working with Dataverse connection
s	connector	Commands for working with Power Platform Connectors
s	copilot	Tools and utilities for copilot scenarios
s	data	Import and export data from Dataverse
s	help	Show help for the Microsoft Power Platform CLI
s	modelbuilder	Code Generator for Dataverse APIs and Tables
s	org	Work with your Dataverse organization
s	package	Commands for working with Dataverse package projects
s	pcf	Commands for working with Power Apps component framework projects
s	pipeline	Work with Pipelines
s	plugin	Commands for working with Dataverse plug-in class library
s	power-fx	(Preview) Commands for working with Power Fx
s	powerpages	Commands for working with Power Pages website
s	solution	Commands for working with Dataverse solution projects
s	telemetry	Manage telemetry settings
s	test	(Preview) Execution of automated tests for a Power App
s	tool	Power Platform tools that can be installed and launched
s	virtual-agent	Commands for working with Power Virtual Agent bots
@	admin
s	list	List all environments from your tenant
s	create	Creates a Dataverse instance in your tenant
s	backup	Takes a manual backup of your environment
s	set-backup-retention-period	Takes a manual backup of your environment
s	delete	Deletes the environment from your tenant
s	reset	Reset the environment from your tenant
s	list-backups	Lists all backups of your environment
s	restore	Restores an environment to a given backup
s	copy	Copy Source Environment to Destination Environment
s	status	This command lists the status of all the operations in progress
s	assign-user	Assign a user to a target Dataverse environment with specified security role
s	assign-group	Assign group to target Dataverse environment with specified security role
s	list-app-templates	Lists all supported Dataverse templates of model-driven apps in Dynamics 365
s	create-service-principal	Add Microsoft Entra ID application and associated application user to the Dataverse environment
s	list-service-principal	List Microsoft Entra ID applications which have access to Dataverse
s	set-governance-config	Enable, disable, and edit managed environments
s	list-tenant-settings	List tenant settings
s	update-tenant-settings	Update tenant settings
s	application	Work with Microsoft Entra ID applications
@	admin list
o	--environment|-env	List all environments that contain given string in their name or ID	v
o	--type|-t	List all environments with the given type	v
o	--name|-n	List all environments that contain given string in their name	v
o	--organization-id|-oi	List all environments that contain given string in their organization ID	v
o	--application|-a	List all environments that have specified application installed. To specify application, use…	v
=	admin list	--type
v	Trial	Trial
v	Sandbox	Sandbox
v	Production	Production
v	Developer	Developer
v	Teams	Teams
v	SubscriptionBasedTrial	SubscriptionBasedTrial
@	admin create
o	--name|-n	Sets the name of the environment	v
o	--region|-r	Sets the environment's region name. [defaults to unitedstates]	v
o	--type|-t	Sets the environment Type	v
o	--currency|-c	Sets the currency used for your environment. [defaults to USD]	v
o	--language|-l	Sets the language used for your environment. [defaults to English]	v
o	--templates|-tm	Sets the Dynamics 365 app that needs to be deployed, passed as comma separated values. For…	v
o	--domain|-d	The domain name is part of the environment URL. If domain name is already in use, a numeric value…	v
o	--input-file|-if	The verb arguments to be passed in a .json input file. For example: {'name' : 'contoso'}. The…	v
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
o	--team-id|-tid	Team ID as Guid	v
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
o	--user|-u	Object ID or user principal name (UPN) of Microsoft Entra ID user to be assigned to the environment	v
=	admin create	--region
v	unitedstates	Unitedstates
v	unitedstatesfirstrelease	Unitedstatesfirstrelease
v	europe	Europe
v	asia	Asia
v	australia	Australia
v	india	India
v	japan	Japan
v	canada	Canada
v	unitedkingdom	Unitedkingdom
v	southamerica	Southamerica
v	france	France
v	unitedarabemirates	Unitedarabemirates
v	germany	Germany
v	switzerland	Switzerland
v	norway	Norway
v	korea	Korea
=	admin create	--type
v	Trial	Trial
v	Sandbox	Sandbox
v	Production	Production
v	Developer	Developer
v	Teams	Teams
v	SubscriptionBasedTrial	SubscriptionBasedTrial
@	admin backup
o	--environment|-env	Environment URL or ID of the Environment that requires backup	v
o	--label|-l	Sets the backup label as provided	v
o	--notes|-n	**ignored**: Additional notes for this backup	v
@	admin set-backup-retention-period
o	--environment|-env	Environment URL or ID of the Environment that requires backup	v
o	--backup-retention-period|-br	Sets the backup retention period in days as provided. Valid values are: 7, 14, 21, 28	v
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
=	admin set-backup-retention-period	--backup-retention-period
v	7	7
v	14	14
v	21	21
v	28	28
@	admin delete
o	--environment|-env	Environment URL or ID of the Environment that needs to be deleted from your tenant	v
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
@	admin reset
o	--environment|-env	URL or ID of the Environment that needs to be reset	v
o	--currency|-c	Sets the currency used for your environment. [defaults to USD]	v
o	--domain|-d	The domain name is part of the environment URL. If domain name is already in use, a numeric value…	v
o	--name|-n	Sets the name of the environment	v
o	--language|-l	Sets the language used for your environment. [defaults to English]	v
o	--purpose|-p	Sets the description used to associate the environment with a specific intent	v
o	--templates|-tm	Sets the Dynamics 365 app that needs to be deployed, passed as comma separated values. For…	v
o	--input-file|-if	The verb arguments to be passed in a .json input file. For example: {'name' : 'contoso'}. The…	v
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
@	admin list-backups
o	--environment|-env	List all environments that contain a given string in their Environment ID or URL	v
@	admin restore
o	--source-env|-se	Environment URL or ID of the source environment required for restore	v
o	--target-env|-te	Environment URL or ID of the target environment required for restore. This would default to source…	v
o	--selected-backup|-sb	DateTime of the backup in 'mm/dd/yyyy hh:mm' format OR string 'latest'	v
o	--name|-n	Optional name of the restored environment	v
o	--skip-audit-data|-sa	Switch indicating whether audit data should be skipped	
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
@	admin copy
o	--source-env|-se	Environment URL or ID of the source environment that is being copied	v
o	--target-env|-te	Environment URL or ID of the target environment	v
o	--name|-n	Name of the target environment	v
o	--type|-t		v
o	--skip-audit-data|-sa	Switch indicating whether audit data should be skipped	
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
=	admin copy	--type
v	MinimalCopy	MinimalCopy
v	FullCopy	FullCopy
@	admin status
@	admin assign-user
o	--environment|-env	ID or URL of the environment to assign a user to	v
o	--user|-u	Object ID or user principal name (UPN) of Microsoft Entra ID user to be assigned to the…	v
o	--role|-r	Name or ID of security role to be applied to user	v
o	--application-user|-au	Specifies whether the input user is an application user. If a business unit isn't specified, the…	
o	--business-unit|-bu	ID of business unit to associate application user with	v
o	--async|-a	Optional boolean argument to run pac verbs asynchronously, defaults to false	
@	admin assign-group
o	--environment|-env	ID or URL of the environment to assign a user to	v
o	--group|-g	Microsoft Entra ID object ID of group to assign to target Dataverse environment	v
o	--group-name|-gn	Name of the group or team to create in Dataverse	v
o	--role|-r	Name or ID of security role to be applied to user	v
o	--team-type|-tt	Type of team	v
o	--membership-type|-mt	Team membership type	v
o	--business-unit|-bu	ID of business unit to associate application user with	v
=	admin assign-group	--team-type
v	Owner	Owner
v	Access	Access
v	AadSecurityGroup	AadSecurityGroup
v	AadOfficeGroup	AadOfficeGroup
=	admin assign-group	--membership-type
v	MembersAndGuests	MembersAndGuests
v	Members	Members
v	Owners	Owners
v	Guests	Guests
@	admin list-app-templates
o	--region|-r	Sets the environment's region name. [defaults to unitedstates]	v
=	admin list-app-templates	--region
v	unitedstates	Unitedstates
v	unitedstatesfirstrelease	Unitedstatesfirstrelease
v	europe	Europe
v	asia	Asia
v	australia	Australia
v	india	India
v	japan	Japan
v	canada	Canada
v	unitedkingdom	Unitedkingdom
v	southamerica	Southamerica
v	france	France
v	unitedarabemirates	Unitedarabemirates
v	germany	Germany
v	switzerland	Switzerland
v	norway	Norway
v	korea	Korea
@	admin create-service-principal
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
o	--name|-n	Application name to create in Entra ID	v
o	--role|-r	Name or ID of security role to be applied to application user. The default value is: 'System…	v
@	admin list-service-principal
o	--filter|-f	Application name 'starts with' filter	v
o	--max|-m	Max number of applications to show. Default: 20	v
@	admin set-governance-config
o	--environment|-env	URL or ID of the environment for which managed environments need to be enabled, disabled or edited	v
o	--protection-level|-pl	Set protection level : 'Standard' to enable managed environments, 'Basic' to disable managed…	v
o	--disable-group-sharing|-dgs	Disable group sharing	
o	--exclude-analysis|-ea	Exclude usage insights for the environment from the weekly digest email	
o	--include-insights|-ii	Include insights in the Power Platform Admin Center homepage cards	
o	--limit-sharing-mode|-lsm	Limit sharing mode	v
o	--max-limit-user-sharing|-ml	If group sharing is disabled, specify the number of people that makers can share canvas apps with	v
o	--solution-checker-mode|-scm	Solution checker validation mode	v
=	admin set-governance-config	--solution-checker-mode
v	none	None
v	warn	Warn
v	block	Block
@	admin list-tenant-settings
o	--settings-file|-s	The .json file to output tenant settings	v
@	admin update-tenant-settings
o	--settings-file|-s	The .json file with tenant settings	v
@	admin application
s	list	List Microsoft Entra ID applications registered under your tenant
s	register	Register Microsoft Entra ID application with your tenant
s	unregister	Unregister Microsoft Entra ID application from your tenant
@	admin application list
@	admin application register
o	--application-id|-a	Application Id	v
@	admin application unregister
o	--application-id|-a	Application Id	v
@	application
s	list	List available Dataverse applications from AppSource
s	install	Installs Dataverse application to given environment
@	application list
o	--environment|-env	List available Dataverse applications for given environment (by ID or url); if not specified, list…	v
o	--output|-o	Location of the JSON file to be created with list of the Dataverse applications from AppSource	v
o	--installState|-s	Filter by application install state	v
=	application list	--installState
v	NotInstalled	NotInstalled
v	Installed	Installed
v	All	All
@	application install
o	--environment|-env	List available Dataverse applications for given environment (by ID or url); if not specified, list…	v
o	--application-name|-an	Unique name of the application to install to the target environment	v
o	--application-list|-al	Location of the JSON file with list of the Dataverse applications from AppSource to be installed	v
@	auth
s	create	Create and store authentication profiles on this computer
s	list	List the authentication profiles stored on this computer
s	select	Select which authentication profile should be active
s	delete	Delete a particular authentication profile
s	update	Update name or target environment of an existing authentication profile
s	name	Name or rename an existing authentication profile
s	clear	Clear all authentication profiles stored on this computer
@	auth create
o	--name|-n	The name you want to give to this authentication profile (maximum 30 characters)	v
o	--kind|-k	The kind of authentication profile you're creating	v
o	--url|-u	The resource URL to connect to	v
o	--username|-un	Optional: The username to authenticate with; shows Microsoft Entra ID dialog if not specified	v
o	--password|-p	Optional: The password to authenticate with	v
o	--applicationId|-id	Optional: The application ID to authenticate with	v
o	--clientSecret|-cs	Optional: The client secret to authenticate with	v
o	--certificateDiskPath|-cdp	Optional: The certificate disk path to authenticate with	v
o	--certificatePassword|-cp	Optional: The certificate password to authenticate with	v
o	--tenant|-t	Tenant ID if using application ID/client secret or application ID/client certificate	v
o	--cloud|-ci	Optional: The cloud instance to authenticate with	v
o	--deviceCode|-dc	Use the Microsoft Entra ID Device Code flow for interactive sign-in	
o	--managedIdentity|-mi	Use Azure Managed Identity	
o	--environment|-env	Default environment (ID, url, unique name, or partial name)	v
=	auth create	--cloud
v	Public	Public
v	Preprod	Preprod
v	Test	Test
v	UsGov	UsGov
v	UsGovHigh	UsGovHigh
v	UsGovDod	UsGovDod
v	China	China
@	auth list
@	auth select
o	--index|-i	The index of the profile to be active	v
o	--name|-n	The name of the profile to be active	v
@	auth delete
o	--index|-i	The index of the profile to be deleted	v
o	--name|-n	The name of the profile to be active	v
@	auth update
o	--index|-i	The index of the profile to be named/renamed	v
o	--name|-n	The name you want to give to this authentication profile (maximum 30 characters)	v
o	--environment|-env	Default environment (ID, url, unique name, or partial name)	v
@	auth name
o	--index|-i	The index of the profile to be named/renamed	v
o	--name|-n	The name you want to give to this authentication profile (maximum 30 characters)	v
@	auth clear
@	canvas
s	download	Download canvas app as .msapp file
s	list	List canvas apps
s	pack	(Preview) Pack sources into an msapp file
s	unpack	(Preview) Extract an msapp file into sources
s	create	Generate a canvas app from a custom connector
@	canvas download
o	--name|-n	Canvas app exact, partial name, or App ID	v
o	--file-name|-f	File name (usually with .msapp extension). If not provided file is saved in current directory with…	v
o	--overwrite|-o	Allow file overwrite	
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	canvas list
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	canvas pack
o	--sources	Directory to sources to be packed	v
o	--msapp	Path to .msapp file	v
@	canvas unpack
o	--sources	Directory to sources to be unpacked	v
o	--msapp	Path to .msapp file	v
@	canvas create
o	--msapp	Path to .msapp file to be generated	v
o	--connector-id	The ID of the Connector to generate the Power App from	v
o	--connector-display-name	The display name of the Connector to generate the Power App from	v
o	--environment	The target Environment ID or URL. The default value is the environment of your currently active…	v
@	catalog
s	list	List all published catalog items from the current Dataverse organization
s	submit	Submit catalog approval request
s	install	Install a catalog item to the target environment
s	status	Get status of the catalog install/submit request
s	update	Update settings for the catalog
s	create-submission	Create catalog submission document. Note: This command will be removed in a future release
@	catalog list
o	--catalog-item-name|-n	Catalog item name to search for	v
o	--catalog-item-id|-cid	Catalog item ID to search for. When catalog item ID is used, catalog item name is ignored	v
o	--include-active|-ia	Include active items	
@	catalog submit
o	--path|-p	Path to catalog submission document	v
o	--package-zip|-pz	Path to package zip file	v
o	--solution-zip|-sz	Path to solution zip file	v
o	--poll-status|-ps	Poll to check status of your request	
@	catalog install
o	--catalog-item-id|-cid	Catalog item to be installed on the target environment	v
o	--target-url|-tu	Url of the target environment for catalog item installation	v
o	--settings|-s	Runtime Package Settings for the installation framework to execute. The format of the string must…	v
o	--target-version|-tv	Target version to install. If left empty, the published version is selected	v
o	--poll-status|-ps	Poll to check status of your request	
@	catalog status
o	--tracking-id|-id	Request tracking ID	v
o	--type|-t	Request type	v
@	catalog update
o	--path|-p	Path to catalog settings document	v
@	catalog create-submission
o	--path|-p	Path to catalog submission document	v
@	connection
s	create	Create new Dataverse connection
s	delete	Delete Dataverse connection
s	list	List all Connections
s	update	Update Dataverse connection
@	connection create
o	--tenant-id|-t	Tenant Id	v
o	--name|-n	Connection name	v
o	--application-id|-a	Application Id	v
o	--client-secret|-cs	Client Secret	v
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	connection delete
o	--connection-id|-id	Connection Id	v
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	connection list
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	connection update
o	--tenant-id|-t	Tenant Id	v
o	--connection-id|-id	Connection Id	v
o	--application-id|-a	Application Id	v
o	--client-secret|-cs	Client Secret	v
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	connector
s	list	List the Connectors registered in Dataverse
s	init	Initializes a new API Properties file for a Connector
s	create	Creates a new row in the Connector table in Dataverse
s	download	Download a Connector's OpenApiDefinition and API Properties file
s	update	Updates a Connector Entity in Dataverse
@	connector list
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
@	connector init
o	--connection-template|-ct	Generate an initial Connection Parameters set with the specified template	v
o	--generate-script-file	Generate an initial Connector Script file	
o	--generate-settings-file	Generate an initial Connector Settings file	
o	--outputDirectory|-o	Output directory	v
=	connector init	--connection-template
v	NoAuth	NoAuth
v	BasicAuth	BasicAuth
v	ApiKey	ApiKey
v	OAuthGeneric	OAuthGeneric
v	OAuthAAD	OAuthAAD
@	connector create
o	--api-definition-file|-df	The filename and path to read the Connector's OpenApiDefinition	v
o	--api-properties-file|-pf	The filename and path to read the Connector's API Properties file	v
o	--icon-file|-if	The filename and path to and Icon .png file	v
o	--script-file|-sf	The filename and path to a Script .csx file	v
o	--solution-unique-name|-sol	The unique name of the solution to add the connector to	v
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--settings-file	The filename and path Connector Settings file	v
@	connector download
o	--connector-id|-id	The ID of the Connector	v
o	--outputDirectory|-o	Output directory	v
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
@	connector update
o	--connector-id|-id	The ID of the Connector	v
o	--api-definition-file|-df	The filename and path to read the Connector's OpenApiDefinition	v
o	--api-properties-file|-pf	The filename and path to read the Connector's API Properties file	v
o	--icon-file|-if	The filename and path to and Icon .png file	v
o	--script-file|-sf	The filename and path to a Script .csx file	v
o	--solution-unique-name|-sol	The unique name of the solution to add the connector to	v
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--settings-file	The filename and path Connector Settings file	v
@	copilot
s	list	AI Builder models in the current environment
s	predict	Sends text or prompt to AI Model
s	prepare-fetch	Takes the FetchXML file from the AI Large Language Model (LLM) and prepares it for execution…
@	copilot list
@	copilot predict
o	--model-id|-id	AI Builder model Id	v
o	--model-name|-n	Full or partial AI Model name	v
o	--prompt|-p	Prompt to send to AI Model	v
o	--text|-t	Text to send to AI Model	v
@	copilot prepare-fetch
o	--inputFile|-i	Input FetchXML file that usually comes from AI LLM	v
o	--outputFile|-o	Output FetchXML file that is ready to execute against the current environment	v
@	data
s	export	Export data
s	import	Import data
@	data export
o	--schemaFile|-sf	Schema file name. It can be created using the Configuration Migration Tool	v
o	--dataFile|-df	File name for data zip file. Default data.zip	v
o	--overwrite|-o	Allow overwrite of the output data file if it already exists	
o	--verbose|-v	Output more diagnostic information during data import/export	
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	data import
o	--dataDirectory|-dd	Directory name with data for import	v
o	--data|-d	Zip file or directory name with data for import	v
o	--connection-count|-c	Number of parallel connections to use during import. Default: 5	v
o	--verbose|-v	Output more diagnostic information during data import/export	
o	--environment|-env	Environment (ID, org ID, url, unique name, or partial name)	v
@	help
@	modelbuilder
s	build	Builds a code model for Dataverse APIs and Tables
@	modelbuilder build
o	--suppressGeneratedCodeAttribute|-sgca	When set, this suppress all generated objects being tagged with the code generation engine and…	
o	--language|-l	The language to use for the generated proxy code. This value can be either 'CS' or 'VB'. The…	v
o	--namespace|-n	The namespace for the generated code. The default namespace is the global namespace	v
o	--serviceContextName|-sctx	The name for the generated service context. If a value is passed in, it's used for the Service…	v
o	--generatesdkmessages|-a	When set, emits Sdk message classes as part of code generation	
o	--emitentityetc|-etc	When set, includes the entity ETC ( entity type code ) in the generated code	
o	--emitvirtualattributes|-eva	When set, includes the Virtual Attributes of entities in the generated code	
o	--emitfieldsclasses|-efc	Generate a constants structure that contains all of the field names by entity at the time of code…	
o	--entitynamesfilter|-enf	Filters the list of entities are retrieved when reading data from Dataverse. Passed in as a…	v
o	--messagenamesfilter|-mnf	Filters the list of messages that are retrieved when reading data from Dataverse. Passed in as a…	v
o	--outdirectory|-o	Write directory for entity, message, and optionset files	v
o	--entitytypesfolder|-etf	Folder name that contains entities. The default name is 'Entities'	v
o	--messagestypesfolder|-mtf	Folder name that contains messages. The default name is 'Messages'	v
o	--optionsetstypesfolder|-otf	Folder name that contains option sets. The default name is 'OptionSets'	v
o	--generateGlobalOptionSets|-go	Emit all Global OptionSets. Note: If an entity contains a reference to a global optionset, it is…	v
o	--writesettingsTemplateFile|-wstf	When set, writes a settings file out to the output directory with the current passed settings or…	v
o	--settingsTemplateFile|-stf	Contains Settings to be used for this run of the Dataverse Model Builder, overrides any duplicate…	v
o	--suppressINotifyPattern	When enabled, doesn't write the INotify wrappers for properties and classes	v
o	--logLevel|-ll	Log level. The default value is 'Off'	v
=	modelbuilder build	--logLevel
v	Off	Off
v	Critical	Critical
v	Error	Error
v	Warning	Warning
v	Information	Information
v	Verbose	Verbose
v	ActivityTracing	ActivityTracing
v	All	All
@	org
s	who	Displays information about the current Dataverse organization
s	list	Lists all of the Dataverse organizations the user has access to
s	fetch	Performs FetchXML query against Dataverse
s	list-settings	List environment settings
s	update-settings	Update environment settings
s	select	Select default organization for current authentication profile
@	org who
@	org list
o	--filter|-f	Show only environments containing filter criteria	v
@	org fetch
o	--xml|-x	FetchXML query to run	v
o	--xmlFile|-xf	File with FetchXML query to run	v
@	org list-settings
o	--filter|-f	Show only settings containing filter criteria	v
@	org update-settings
o	--name|-n	Name of the setting to update	v
o	--value|-v	Value to which setting should be updated to	v
@	org select
o	--environment|-env	Default environment (ID, url, unique name, or partial name)	v
@	package
s	init	Initializes a directory with a new Dataverse package project
s	add-external-package	Adds a package that is external to the Dataverse solution system to a Package Deployer Package…
s	add-solution	Adds a prebuilt Dataverse solution file to a Package Deployer Package project
s	add-reference	Adds reference to Dataverse solution project
s	deploy	Deploys package to Dataverse
s	show	Shows details of Dataverse package
@	package init
o	--outputDirectory|-o	Output directory	v
o	--package-name	Sets the default name of the package. Applies to the generation of ImportExtension.GetNameOfImport	v
@	package add-external-package
o	--path|-p	Path to the external package	v
o	--package-type|-t	The type of the package being added. For example: 'xpp' for FnO packages	v
o	--import-order	A whole number that indicates the order to insert this item into the final ImportConfig.xml file…	v
o	--skip-validation|-sv	Adds the item to the project file even if the file doesn't exist or appears to be invalid. Note…	
@	package add-solution
o	--path|-p	Path to the Dataverse solution file. The file must be a compressed ZIP file	v
o	--import-order	A whole number that indicates the order to insert this item into the final ImportConfig.xml file…	v
o	--skip-validation|-sv	Adds the item to the project file even if the file doesn't exist or appears to be invalid. Note…	
o	--publish-workflows-activate-plugins	Explicitly indicates whether to publish the workflows and activate plug-ins when this solution is…	v
o	--overwrite-unmanaged-customizations	Explicitly indicates whether to overwrite unmanaged customizations when this solution is imported	v
o	--import-mode	Explicitly specifies the required mode when importing this solution	v
o	--missing-dependency-behavior	Specifies the behavior on import when a dependency of this solution is missing from the target…	v
o	--dependency-overrides	A semicolon delimited list of overrides. This value overrides any dependency information encoded…	v
=	package add-solution	--publish-workflows-activate-plugins
v	true	True
v	false	False
=	package add-solution	--overwrite-unmanaged-customizations
v	true	True
v	false	False
=	package add-solution	--import-mode
v	true	True
v	false	False
=	package add-solution	--missing-dependency-behavior
v	skip	Skip
v	fault	Fault
@	package add-reference
o	--path|-p	The path to the referenced Dataverse solution project	v
o	--import-order	A whole number that indicates the order to insert this item into the final ImportConfig.xml file…	v
o	--publish-workflows-activate-plugins	Explicitly indicates whether to publish the workflows and activate plug-ins when this solution is…	v
o	--overwrite-unmanaged-customizations	Explicitly indicates whether to overwrite unmanaged customizations when this solution is imported	v
o	--import-mode	Explicitly specifies the required mode when importing this solution	v
o	--missing-dependency-behavior	Specifies the behavior on import when a dependency of this solution is missing from the target…	v
o	--dependency-overrides	A semicolon delimited list of overrides. This value overrides any dependency information encoded…	v
=	package add-reference	--publish-workflows-activate-plugins
v	true	True
v	false	False
=	package add-reference	--overwrite-unmanaged-customizations
v	true	True
v	false	False
=	package add-reference	--import-mode
v	sync	Sync
v	async	Async
=	package add-reference	--missing-dependency-behavior
v	skip	Skip
v	fault	Fault
@	package deploy
o	--logFile|-lf	Log file path	v
o	--logConsole|-c	Output log to console	
o	--package|-p	Path to a package dll or zip file with a package	v
o	--settings|-s	Runtime Package Settings that are passed to the package that is being deployed. The format of the…	v
o	--verbose|-vdbg	Emit verbose logs to the log outputs	
@	package show
o	--package|-p	Path to a package dll or zip file with a package	v
o	--logFile|-lf	Log file path	v
o	--verbose|-vdbg	Emit verbose logs to the log outputs	
@	pcf
s	init	Initializes a directory with a new Power Apps component framework project
s	push	Import the Power Apps component framework project into the current Dataverse organization
s	version	Patch version for controls
@	pcf init
o	--namespace|-ns	The namespace for the component	v
o	--name|-n	The name for the component	v
o	--template|-t	Choose a template for the component	v
o	--framework|-fw	The rendering framework for control. The default value is 'none', which means HTML	v
o	--outputDirectory|-o	Output directory	v
o	--run-npm-install|-npm	Auto run 'npm install' after the control is created. The default value is 'false'	
=	pcf init	--template
v	field	Field
v	dataset	Dataset
=	pcf init	--framework
v	none	None
v	react	React
@	pcf push
o	--publisher-prefix|-pp	Customization prefix value for the Dataverse solution publisher	v
o	--verbosity|-v	Verbosity level for MSBuild when building the temporary solution wrapper	v
o	--force-import|-f	Force a full update of the control as part of a temporary solution	
o	--interactive|-i	Indicates that actions in the build are allowed to interact with the user. Don't use this argument…	
o	--incremental|-inc	Pushes only files which are diifferent using entity updates	
=	pcf push	--verbosity
v	minimal	Minimal
v	normal	Normal
v	detailed	Detailed
v	diagnostic	Diagnostic
@	pcf version
o	--strategy|-s	Updates patch version for 'ControlManifest.xml' files using specified strategy. If using gittags…	v
o	--patchversion|-pv	Patch version for controls	v
o	--path|-p	Absolute/Relative path of the 'ControlManifest.xml' for updating	v
o	--allmanifests|-a	Updates patch version for all 'ControlManifest.xml' files	
o	--updatetarget|-ut	Specify which target manifest needs to be updated	v
o	--filename|-fn	Tracker CSV file name to be used when using filetracking as a strategy. The default value is…	v
=	pcf version	--strategy
v	None	None
v	GitTags	GitTags
v	FileTracking	FileTracking
v	Manifest	Manifest
=	pcf version	--updatetarget
v	build	Build
v	project	Project
@	pipeline
s	list	List Pipelines
s	deploy	Start pipeline deployment
@	pipeline list
o	--pipeline|-p	Pipeline name or ID for which show list of details such as deployment stages	v
@	pipeline deploy
o	--solutionName|-sn	Solution Name	v
o	--stageId|-sid	Deployment Stage ID	v
o	--environment|-env	Deployment Environment	v
o	--currentVersion|-cv	Current solution version	v
o	--newVersion|-nv	New solution version	v
o	--wait|-w	Wait until the deployment finishes	
@	plugin
s	init	Initializes a directory with a new Dataverse plug-in class library
s	push	Import plug-in into Dataverse
@	plugin init
o	--signing-key-file-path|-sk	Relative path to the Dataverse plug-in assembly originator key file for signing	v
o	--outputDirectory|-o	Output directory	v
o	--author|-a	One or more authors of the Dataverse Plug-in Package	v
o	--skip-signing|-ss	Skip plug-in assembly signing that gives the plug-in assembly a strong name. The default value is…	
@	plugin push
o	--pluginId|-id	ID of plug-in assembly or plug-in package	v
o	--pluginFile|-pf	File name of plug-in assembly or plug-in package	v
o	--type|-t	Type of item if not specified explicitly through --pluginFile. The default value is: 'Nuget'	v
o	--configuration|-c	Build configuration. The default value is: 'Debug'	v
=	plugin push	--type
v	Nuget	Nuget
v	Assembly	Assembly
@	power-fx
s	repl	(Preview) Launch interactive Power Fx Read-Eval-Print Loop
s	run	(Preview) Run a file of Power Fx instructions
@	power-fx repl
@	power-fx run
o	--file|-f	Path of file to execute	v
o	--echo|-e	True if input commands should echo back to output	
@	powerpages
s	list	List all Power Pages websites from the current Dataverse environment
s	download	Download Power Pages website content from the current Dataverse environment
s	upload	Upload Power Pages website content to current Dataverse environment
s	bootstrap-migrate	Migrates HTML code from bootstrap V3 to V5
@	powerpages list
o	--verbose|-v	Enables verbose mode to provide more details	
@	powerpages download
o	--path|-p	Path where the Power Pages website content is downloaded	v
o	--webSiteId|-id	Power Pages website ID to download	v
o	--includeEntities|-ie	Download only the entities specified for this argument using comma separated entity logical names	v
o	--excludeEntities|-xe	Comma separated list of entity logical names to exclude downloading	v
o	--overwrite|-o	Power Pages website content to overwrite	
o	--modelVersion|-mv	Power Pages website data model version to download	v
@	powerpages upload
o	--path|-p	Path from where the Power Pages website content is uploaded	v
o	--deploymentProfile|-dp	Deployment profile name to be used. Defaults to 'default'	v
o	--forceUploadAll|-f	Upload all Power Pages website content to the current Dataverse environment	
o	--modelVersion|-mv	Power Pages website data model version to upload	v
@	powerpages bootstrap-migrate
o	--path|-p	Path of website content	v
@	solution
s	init	Initializes a directory with a new Dataverse solution project
s	add-reference	Adds a reference from the project in the current directory to the project at 'path'
s	list	List all Solutions from the current Dataverse organization
s	delete	Delete a solution from Dataverse in the current environment
s	online-version	Sets version for solution loaded in Dataverse
s	version	Update build or revision version for the solution
s	import	Import the solution into Dataverse
s	export	Export a solution from Dataverse
s	clone	Create a solution project based on an existing solution in your organization
s	publish	Publishes all customizations
s	upgrade	Apply solution upgrade
s	add-license	Add license and plan info to the solution
s	check	Upload a Dataverse solution project to run against the Power Apps Checker service
s	create-settings	Create a settings file from solution zip or solution folder
s	pack	Package solution components on local filesystem into solution.zip (SolutionPackager)
s	unpack	Extract solution components from solution.zip onto local filesystem (SolutionPackager)
s	add-solution-component	Add one or more solution components to the target unmanaged solution in Dataverse
s	sync	Sync the current Dataverse solution project to the current state of the solution in your…
@	solution init
o	--publisher-name|-pn	Name of the Dataverse solution publisher	v
o	--publisher-prefix|-pp	Customization prefix value for the Dataverse solution publisher	v
o	--outputDirectory|-o	Output directory	v
@	solution add-reference
o	--path|-p	The path to the referenced project	v
@	solution list
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
@	solution delete
o	--solution-name|-sn	Name of the solution	v
@	solution online-version
o	--solution-name|-sn	Name of the solution	v
o	--solution-version|-sv	Specify the solution version number	v
@	solution version
o	--strategy|-s	Updates build version for 'Solution.xml' file using specified strategy. If using gittags, set…	v
o	--patchversion|-pv	Patch version for the solution	v
o	--buildversion|-bv	Build version for the solution	v
o	--revisionversion|-rv	Revision version for the solution	v
o	--filename|-fn	Tracker CSV file name to be used when using filetracking as a strategy. The default value is…	v
o	--solutionPath|-sp	Path to Dataverse solution directory or Solution.xml file	v
=	solution version	--strategy
v	None	None
v	GitTags	GitTags
v	FileTracking	FileTracking
v	Solution	Solution
@	solution import
o	--path|-p	Path to solution zip file. If not specified, assumes the current folder is a cdsproj project	v
o	--activate-plugins|-ap	Activate plug-ins and workflows on the solution	
o	--force-overwrite|-f	Force an overwrite of unmanaged customizations	
o	--skip-dependency-check|-s	Skip dependency check against dependencies flagged as product update	
o	--import-as-holding|-h	Import the solution as a holding solution	
o	--stage-and-upgrade|-up	Import and upgrade the solution	
o	--publish-changes|-pc	Publish your changes upon a successful import	
o	--convert-to-managed|-cm	Convert to a managed solution	
o	--async|-a	Imports the solution asynchronously	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
o	--settings-file	The .json file with the deployment settings for connection references and environment variables	v
o	--skip-lower-version|-slv	Skip solution import if same or higher version is present in current environment	
=	solution import	--settings-file
t	filepaths
@	solution export
o	--name|-n	The name of the solution to be exported	v
o	--path|-p	Path where the exported solution zip file is written	v
o	--managed|-m	Whether the solution should be exported as a managed solution	
o	--targetversion|-v	The version that the exported solution will support	v
o	--include|-i	Which settings should be included in the solution being exported	v
o	--async|-a	Exports the solution asynchronously	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
o	--overwrite|-ow	The exported solution file can overwrite the solution zip file on the local file system	
@	solution clone
o	--name|-n	The name of the solution to be exported	v
o	--targetversion|-v	The version that the exported solution will support	v
o	--include|-i	Which settings should be included in the solution being exported	v
o	--outputDirectory|-o	Output directory	v
o	--async|-a	Exports the solution asynchronously	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
o	--processCanvasApps|-pca	(Preview) Pack/unpack any Canvas apps (.msapp) while processing the solution. The default value is…	
o	--packagetype|-p	Specifies the extraction type for the solution. Can be: 'Unmanaged', 'Managed' or 'Both'. The…	v
o	--localize|-loc	Extract or merge all string resources into .resx files	
=	solution clone	--packagetype
v	Unmanaged	Unmanaged
v	Managed	Managed
v	Both	Both
@	solution publish
o	--async|-a	Publishes all customizations asynchronously	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
@	solution upgrade
o	--solution-name|-sn	Name of the solution	v
o	--async|-a	Upgrades solution asynchronously	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
@	solution add-license
o	--planDefinitionFile|-pd	License plan definition file in CSV format; expected columns: Service ID, Display name, More info…	v
o	--planMappingFile|-pm	License plan mapping file in CSV format; expected columns: Service ID, Component name	v
@	solution check
o	--path|-p	Path where one or more solution files to be checked exist. The path can contain glob/wildcard…	v
o	--solutionUrl|-u	SAS Uri pointing to solution.zip to be analyzed	v
o	--outputDirectory|-o	Output directory	v
o	--geo|-g	Which geographical instance of the Power Apps Checker service to use	v
o	--customEndpoint|-ce	Specify a custom URL as the Power Apps Checker endpoint	v
o	--ruleLevelOverride|-rl	Path to a file containing a JSON array rules and levels to override. Accepted values for…	v
o	--ruleSet|-rs	Select a rule set that is executed as part of this build. Values: A valid Guid, 'AppSource…	v
o	--excludedFiles|-ef	Exclude Files from the Analysis. Pass as comma-separated values	v
o	--saveResults|-sav	Uses current environment to store solution analysis results that can be seen in Solution Health…	
=	solution check	--geo
v	PreviewUnitedStates	PreviewUnitedStates
v	UnitedStates	UnitedStates
v	Europe	Europe
v	Asia	Asia
v	Australia	Australia
v	Japan	Japan
v	India	India
v	Canada	Canada
v	SouthAmerica	SouthAmerica
v	UnitedKingdom	UnitedKingdom
v	France	France
v	SouthAfrica	SouthAfrica
v	Germany	Germany
v	UnitedArabEmirates	UnitedArabEmirates
v	Switzerland	Switzerland
v	Norway	Norway
v	Singapore	Singapore
v	Korea	Korea
v	USGovernment	USGovernment
v	USGovernmentL4	USGovernmentL4
v	USGovernmentL5DoD	USGovernmentL5DoD
v	China	China
@	solution create-settings
o	--solution-zip|-z	Path to solution zip file	v
o	--solution-folder|-f	Path to the local, unpacked solution folder: either the root of the 'Other/Solution.xml' file or a…	v
o	--settings-file|-s	The .json file with the deployment settings for connection references and environment variables	v
@	solution pack
o	--zipfile|-z	The full path to the solution ZIP file	v
o	--folder|-f	The path to the root folder on the local filesystem. When unpacking or extracting, this is written…	v
o	--packagetype|-p	When unpacking or extracting, use to specify dual Managed and Unmanaged operation. When packing…	v
o	--log|-l	The path to the log file	v
o	--errorlevel|-e	Minimum logging level for log output [Verbose|Info|Warning|Error|Off]. The default value is 'Info'	v
o	--singleComponent|-sc	Only perform action on a single component type [WebResource|Plugin|Workflow|None]. The default…	v
o	--allowDelete|-ad	Dictates if delete operations may occur. The default value is 'false'	
o	--allowWrite|-aw	Dictates if write operations may occur. The default value is 'false'	
o	--clobber|-c	Enables that files marked read-only can be deleted or overwritten. The default value is 'false'	
o	--map|-m	The full path to a mapping xml file from which to read component folders to pack	v
o	--sourceLoc|-src	Generates a template resource file. Valid only on extract. Possible values are 'auto', or language…	v
o	--localize|-loc	Extract or merge all string resources into .resx files	
o	--useLcid|-lcid	Use Language Code Identifier (LCID) values (1033) rather than International Organization for…	
o	--useUnmanagedFileForMissingManaged|-same	Use the same XML source file when packaging for Managed and only Unmanaged XML file is found…	
o	--disablePluginRemap|-dpm	Disabled plug-in fully qualified type name remapping. The default value is 'false'	
o	--processCanvasApps|-pca	(Preview) Pack/unpack any Canvas apps (.msapp) while processing the solution. The default value is…	
=	solution pack	--packagetype
v	Unmanaged	Unmanaged
v	Managed	Managed
v	Both	Both
@	solution unpack
o	--zipfile|-z	The full path to the solution ZIP file	v
o	--folder|-f	The path to the root folder on the local filesystem. When unpacking or extracting, this is written…	v
o	--packagetype|-p	When unpacking or extracting, use to specify dual Managed and Unmanaged operation. When packing…	v
o	--log|-l	The path to the log file	v
o	--errorlevel|-e	Minimum logging level for log output [Verbose|Info|Warning|Error|Off]. The default value is 'Info'	v
o	--singleComponent|-sc	Only perform action on a single component type [WebResource|Plugin|Workflow|None]. The default…	v
o	--allowDelete|-ad	Dictates if delete operations may occur. The default value is 'false'	
o	--allowWrite|-aw	Dictates if write operations may occur. The default value is 'false'	
o	--clobber|-c	Enables that files marked read-only can be deleted or overwritten. The default value is 'false'	
o	--map|-m	The full path to a mapping xml file from which to read component folders to pack	v
o	--sourceLoc|-src	Generates a template resource file. Valid only on extract. Possible values are 'auto', or language…	v
o	--localize|-loc	Extract or merge all string resources into .resx files	
o	--useLcid|-lcid	Use Language Code Identifier (LCID) values (1033) rather than International Organization for…	
o	--useUnmanagedFileForMissingManaged|-same	Use the same XML source file when packaging for Managed and only Unmanaged XML file is found…	
o	--disablePluginRemap|-dpm	Disabled plug-in fully qualified type name remapping. The default value is 'false'	
o	--processCanvasApps|-pca	(Preview) Pack/unpack any Canvas apps (.msapp) while processing the solution. The default value is…	
=	solution unpack	--packagetype
v	Unmanaged	Unmanaged
v	Managed	Managed
v	Both	Both
@	solution add-solution-component
o	--solutionUniqueName|-sn	Name of the solution	v
o	--component|-c	The schema name or ID of the component to add to the target solution	v
o	--componentType|-ct	The value that represents the solution component that you're adding	v
o	--AddRequiredComponents|-arc	Indicates whether other solution components required by the solution component that you're adding…	
o	--environment|-env	Environment URL or ID of the target environment	v
@	solution sync
o	--solution-folder|-f	Path to the local, unpacked solution folder: either the root of the 'Other/Solution.xml' file or a…	v
o	--include|-i	Which settings should be included in the solution being exported	v
o	--async|-a	Exports the solution asynchronously	
o	--max-async-wait-time|-wt	Max asynchronous wait time in minutes. The default value is 60 minutes	v
o	--processCanvasApps|-pca	(Preview) Pack/unpack any Canvas apps (.msapp) while processing the solution. The default value is…	
o	--packagetype|-p	When unpacking or extracting, use to specify dual Managed and Unmanaged operation. When packing…	v
o	--localize|-loc	Extract or merge all string resources into .resx files	
=	solution sync	--packagetype
v	Unmanaged	Unmanaged
v	Managed	Managed
v	Both	Both
@	telemetry
s	enable	Choose to send usage information to help Microsoft improve this product
s	disable	Choose to not send usage information to help Microsoft improve this product
s	status	Show the current status of telemetry
@	telemetry enable
@	telemetry disable
@	telemetry status
@	test
s	run	(Preview) Execute tests defined in a Test Plan file
@	test run
o	--test-plan-file|-test	Path to the Test Plan file	v
o	--environment-id|-env	Environment ID for the app to be tested	v
o	--tenant|-t	Tenant ID for the app being tested	v
o	--output-directory|-o	Path to save test output and logs	v
o	--domain|-d	The player domain for the app being tested	v
@	tool
s	list	List the launchable tools and their local install state and version
s	admin	Launch Power Platform Admin Center for the current environment
s	maker	Launch Power Apps Maker Portal for the current environment
s	prt	Launch Plug-in Registration Tool (PRT)
s	cmt	Launch Configuration Migration Tool (CMT)
s	pd	Launch Package Deployer (PD)
@	tool list
@	tool admin
@	tool maker
@	tool prt
o	--update|-u	Update tool to latest available version from nuget.org	
o	--clear|-c	Clear tool from local file cache	
@	tool cmt
o	--update|-u	Update tool to latest available version from nuget.org	
o	--clear|-c	Clear tool from local file cache	
@	tool pd
o	--update|-u	Update tool to latest available version from nuget.org	
o	--clear|-c	Clear tool from local file cache	
@	virtual-agent
s	list	List of Virtual Agents in the current or target Dataverse environment
s	status	Poll the deployment status of a specified Virtual Agent in the current or target Dataverse…
s	extract-translation	Extracts file containing localized content for one or more bots
s	merge-translation	Merge files containing localized content for one or more bots
s	extract-template	Extracts a template file from an existing bot in an environment
s	create	Creates a new bot using an existing template file as the reference
@	virtual-agent list
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
@	virtual-agent status
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--bot-id|-id	The ID of a Virtual Agent (Chatbot)	v
@	virtual-agent extract-translation
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--sourcedir|-src	Source solution directory. When specified, will ignore the connected environment when looking for…	v
o	--bot|-id	The Chatbot ID or schema name (unique name found in Bot Details or file name in solution explorer)	v
o	--outdir	The output directory to write to	v
o	--format	The file format in which to write localized files, either 'resx' or 'json'. The default is 'resx'	v
o	--all|-a	Write localization files for all supported languages. By default, only the primary language is…	
o	--overwrite|-o	Allow overwrite of the output data file if it already exists	
@	virtual-agent merge-translation
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--sourcedir|-src	Source solution directory. When specified, will ignore the connected environment when looking for…	v
o	--file|-f	The list of files that contain translations. Glob patterns are supported	v
o	--whatif	Does not execute the command, but outputs the details of what would happen	
o	--verbose	Output more diagnostic information during data import/export	
o	--solution|-s	Name of the solution	v
@	virtual-agent extract-template
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--bot|-id	The Chatbot ID or schema name (unique name found in Bot Details or file name in solution explorer)	v
o	--templateFileName	Location of the yaml file to write the bot template to	v
o	--overwrite|-o	Allow overwrite of the output data file if it already exists	
@	virtual-agent create
o	--environment|-env	The target Environment ID or URL. The default value is the environment of your currently active…	v
o	--schemaName	The schema name (unique name) of the new bot	v
o	--templateFileName	Source yaml file containing the bot template that was extracted using the extract-template command	v
o	--displayName	The display name of the new bot	v
o	--solution|-s	Name of the solution	v

@	
s	forward|fwd	Port-forwarding for Northflank services and addons
s	command-exec|exec	Command execution (exec) for Northflank services and jobs
s	login	Connect the CLI to your Northflank account
s	context|contexts|ctx	Retrieve and update local context settings
s	list	List Northflank resources
s	create	Create Northflank resources
s	get	Get information about Northflank resources
s	delete	Delete Northflank resources
s	scale	Scale Northflank resources
s	update	Update Northflank resource properties
s	backup	Backup Northflank resources
s	restore	Restore Northflank resources
s	import	Import Northflank resources
s	pause	Pause Northflank resources
s	resume	Resume Northflank resources
s	restart	Restart Northflank resources
s	abort	Abort Northflank resources
s	retain	Retain Northflank resources
s	start	Start Northflank resources
s	suspend	Suspend Northflank resources
s	add	Add Northflank resources
s	verify	Verify Northflank resources
s	assign	Assign Northflank resources
s	unassign	Unassign Northflank resources
s	run	Run Northflank resources
s	attach	Attach Northflank resources
s	detach	Detach Northflank resources
s	command-overview	Prints a tree view of all available commands
s	help	Display help for command
o	-v|--version	Print the current version of the Northflank cli	
o	-h|--help	Display help for command	
@	forward
s	all	Port-forwarding for all services and addons in the given project
s	service	Port-forwarding for the specified service
s	addon	Port-forwarding for the specified addon
s	help	Display help for command
o	-h|--help	Display help for command	
@	forward all
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for forwarding	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	--skipHostnames	Only expose on IP address, not on hostnames. With this option, no root permissions are required	
o	-h|--help	Display help for command	
@	forward service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for forwarding	V
o	--service|--serviceId	Service to forward	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	--skipHostnames	Only expose on IP address, not on hostnames. With this option, no root permissions are required	
o	-h|--help	Display help for command	
@	forward addon
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for forwarding	V
o	--addon|--addonId	Addon to forward	V
o	--skipHostnames	Only expose on IP address, not on hostnames. With this option, no root permissions are required	
o	-h|--help	Display help for command	
@	forward help
a	1	0
#	forward help	1
t	help
@	command-exec
s	service	Command exec for the specified service
s	job	Command exec for the specified job
s	help	Display help for command
o	-h|--help	Display help for command	
@	command-exec service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for exec	V
o	--service|--serviceId	Service to exec into	V
o	--container|--containerId	Container to exec into (random container will be chosen if not specified)	V
o	--shell-cmd	Run command with shell (e.g. bash,sh). If not set and no command is provided, several standard…	V
o	--user	Run command with this user	V
o	--group	Run command with this group	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	--cmd|--command	Command to execute, if --shell option is present, it will run in the specified shell, otherwise	V
o	-h|--help	Display help for command	
@	command-exec job
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for exec	V
o	--job|--jobId	Job to exec into	V
o	--container|--containerId	Container to exec into (random container will be chosen if not specified)	V
o	--shell-cmd	Run command with shell (e.g. bash,sh). If not set and no command is provided, several standard…	V
o	--user	Run command with this user	V
o	--group	Run command with this group	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	--cmd|--command	Command to execute, if --shell option is present, it will run in the specified shell, otherwise	V
o	-h|--help	Display help for command	
@	command-exec help
a	1	0
#	command-exec help	1
t	help
@	login
o	--token-login	Use manual login with API token	
o	--do-not-open-browser	Use browser login but only print URL which can be used to login	
o	-n|--name	Name for login context	V
o	-t|--token	Token for this context. When set, browser login is not used	V
o	--host	Host url for this context	V
o	--override	Override existing contexts (this will remove project and service context)	
o	-h|--help	Display help for command	
@	context
s	ls	List all available contexts
s	use	Switch between your local contexts
s	remove|delete|rm	Remove a context
s	update-token|set-token	Update token for current context
s	help	Display help for command
o	-h|--help	Display help for command	
@	context ls
o	--all	Shows full context information (including tokens)	
o	-h|--help	Display help for command	
@	context use
s	project	Change the default project in the current local context
s	job	Change the default job in the current local context
s	service	Change the default service in the current local context
s	help	Display help for command
o	-n|--name	Change current context to context identified by this name	V
o	-h|--help	Display help for command	
@	context use project
o	-i|--id	Project name (internal id) to use as default in context	V
o	-h|--help	Display help for command	
@	context use job
o	-i|--id	Job name (internal id) to use as default in context	V
o	-h|--help	Display help for command	
@	context use service
o	-i|--id	Service name (internal id) to use as default in context	V
o	-h|--help	Display help for command	
@	context use help
a	1	0
#	context use help	1
t	help
@	context remove
o	-i|--id	Local context name to remove	V
o	-h|--help	Display help for command	
@	context update-token
o	-t|--token	Token for this context	V
o	-h|--help	Display help for command	
@	context help
a	1	0
#	context help	1
t	help
@	list
s	projects|project|prj	Lists projects for the authenticated user or team
s	addons|addon|adn	Gets a list of addons belonging to the project
s	invoices|invoice|inv	Get a list of past invoices
s	providers	Lists supported cloud providers
s	integrations	Lists integrations for the authenticated user or team
s	clusters	Lists clusters for the authenticated user or team
s	jobs|job	Gets a list of jobs belonging to the project
s	log-sinks	Gets a list of log sinks added to this account
s	registries	Lists the container registry credentials saved to this account. Does not display secrets
s	domains|domain|dmn	Lists available domains
s	plans|plan|pln	Lists available billing plans
s	regions|region|rgn	Lists available project regions
s	vcs	Lists linked version control providers
s	pipelines	Lists all pipelines for a project
s	release-flow-runs	Lists runs of a release flow
s	secrets|secret|scrt	Gets a list of secrets belonging to the project
s	services|service|svc	Gets a list of services belonging to the project
s	templates|template|tpl	Get a list of templates
s	template-runs	Get a list of template runs
s	repos|repository|repositories|repo	Gets a list of repositories accessible to this account
s	branches|branch|brn	Gets a list of branches for the repo
s	volumes|volume|vol	Gets a list of volumes belonging to the project
s	help	Display help for command
o	-h|--help	Display help for command	
@	list projects
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list addons
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list invoices
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list providers
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list integrations
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list clusters
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list jobs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list log-sinks
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list registries
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list domains
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list plans
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list regions
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list vcs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list pipelines
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list release-flow-runs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--stage	Stage of the pipeline, example: development	v
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list secrets
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list services
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list templates
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list template-runs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--template|--templateId	ID of the template, example: example-template	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list repos
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--vcs_service	OPTIONAL: If provided, only returns repositories belonging to this version control provider…	v
o	--self_hosted_vcs_id	OPTIONAL: If provided, only returns repositories belonging to this self-hosted version control…	v
o	--account_login	OPTIONAL: If provided, only returns repositories that can be accessed by the linked version…	v
o	--vcs_link_id	OPTIONAL: If provided, only returns repositories belong to that VCS link	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list branches
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--repositoryName	Name of the repository, example: next-js-example	v
o	--repositoryOwner	Name of the owner of the repository, example: northflank-examples	v
o	--vcsService	Version control provider of the repository, example: github	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list volumes
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml|custom-columns=<column1>,<column2>,...'	v
o	-h|--help	Display help for command	
@	list help
a	1	0
#	list help	1
t	help
@	create
s	project|projects|prj	Creates a new project
s	addon|addons|adn	Creates a new addon
s	integration	Creates a new integration
s	cluster	Creates a new cluster
s	job|jobs	Job Northflank resources
s	log-sink	Creates a new log sink
s	domain|domains|dmn	Registers a new domain
s	secret|secrets|scrt	Creates a secret with the specified payload
s	service|services|svc	Service Northflank resources
s	custom-vcs	CustomVcs Northflank resources
s	volume|volumes|vol	Creates a volume with the specified payload
s	help	Display help for command
o	-h|--help	Display help for command	
@	create project
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create addon
s	backup-schedule	Create a new backup schedule for an addon
s	help	Display help for command
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create addon backup-schedule
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create addon help
a	1	0
#	create addon help	1
t	help
@	create integration
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create cluster
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create job
s	manual	Creates a new manual job that only runs when initiated via the UI, CLI, API or JS client
s	cron	Creates a new cron job
s	help	Display help for command
o	-h|--help	Display help for command	
@	create job manual
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create job cron
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create job help
a	1	0
#	create job help	1
t	help
@	create log-sink
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create domain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create secret
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create service
s	combined	Creates a new combined service
s	deployment	Creates a new deployment service
s	build	Creates a new build service
s	help	Display help for command
o	-h|--help	Display help for command	
@	create service combined
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create service deployment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create service build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create service help
a	1	0
#	create service help	1
t	help
@	create custom-vcs
s	token	Generate a token for a specific VCS link
s	help	Display help for command
o	-h|--help	Display help for command	
@	create custom-vcs token
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--vcsLink|--vcsLinkId	ID of the version control link, example: 63ebb6ce2ccc6c7affdbf253	v
o	--customVCS|--customVCSId	ID of the custom VCS, example: cdb3d41f-0dd8-49ad-92d5-7544c98c490b	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create custom-vcs help
a	1	0
#	create custom-vcs help	1
t	help
@	create volume
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	create help
a	1	0
#	create help	1
t	help
@	get
s	project|projects|prj	Get information about the given project
s	addon|addons|adn	Gets information about the given addon
s	invoice|invoices|inv	Get information about Northflank invoices
s	integration	Get information about the given integration
s	cluster	Get information about the given cluster
s	job|jobs	Gets information about the given job
s	log-sink	Gets details about a given log sink
s	registry	Views a set of registry credential data
s	domain|domains|dmn	Gets details about domain
s	subdomain	Gets details about the given subdomain
s	dns-id	Returns the partially random string used when generating host names for the authenticated account
s	pipeline	Get details about a pipeline
s	release-flow	Gets details about a release flow
s	release-flow-run	Get information about the given release flow run
s	secret|secrets|scrt	View a secret including its contents
s	secret-details	View a secret with details about its linked addons
s	secret-link	Get details about a given addon link
s	service|services|svc	Gets information about the given service
s	template|templates|tpl	Get information about the given template
s	template-run	Get information about the given template run
s	volume|volumes|vol	Retrieve a volume
s	help	Display help for command
o	-h|--help	Display help for command	
@	get project
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon
s	credentials|credential|cred	Returns the credentials for connecting to the given addon
s	logs|log	Get log for the specified addon
s	metrics|metric	Get metrics for the specified addon
s	types	Gets information about the available addon types
s	version	Gets details about the current addon version including available upgrades and upgrade history
s	backups	Returns a list of backups for the given addon
s	backup	Gets details about a given backup
s	restores	Gets a list of restores for the given backup
s	containers	Gets a list of containers for the given addon
s	backup-schedules	Gets details about an addon's backup schedules
s	pitr-window	Gets the valid window for performing a point-in-time restore (PITR) on this addon
s	help	Display help for command
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon credentials
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon logs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--addon|--addonId	Addon to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	-f|--tail	Tail will stream logs in real-time. Session will be kept open	
o	-l|--lineLimit	Number of lines to return	V
o	--startTime	Get logs generated after this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--endTime	Get logs generated before this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-d|--direction	Direction of logs. Ignored when tailing	v
o	--textIncludes	Filter log lines to include this text	v
o	--textNotIncludes	Filter log lines to not include this text	v
o	--regexIncludes	Filter log lines to match this regular expression	v
o	--regexNotIncludes	Filter log lines to not match this regular expression	v
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	-h|--help	Display help for command	
=	get addon logs	-d
v	backward	
v	forward	
=	get addon logs	-o
v	format	
v	json	
v	yaml	
@	get addon metrics
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--addon|--addonId	Addon to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	--startTime	Get metrics after this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--endTime	Get metrics before this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-t|--metricTypes	Which metric type to fetch	v
o	--timestamp	Get metrics at this exact timestamp, if no timestamp set most recent time is used. example…	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	-h|--help	Display help for command	
=	get addon metrics	-t
v	cpu	
v	memory	
v	networkIngress	
v	networkEgress	
v	tcpConnectionsOpen	
v	diskUsage	
v	requests	
v	http4xxResponses	
v	http5xxResponses	
=	get addon metrics	-o
v	format	
v	json	
v	yaml	
@	get addon types
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon version
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon backups
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon backup
s	download	Generates a temporary download link for downloading the given backup
s	help	Display help for command
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon backup download
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon backup help
a	1	0
#	get addon backup help	1
t	help
@	get addon restores
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon containers
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon backup-schedules
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon pitr-window
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get addon help
a	1	0
#	get addon help	1
t	help
@	get invoice
s	details	Get details about an invoice. If `timestamp` is passed in as a query parameter, this endpoint…
s	help	Display help for command
o	-h|--help	Display help for command	
@	get invoice details
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--timestamp	OPTIONAL: Timestamp of an invoice. If passed in, this endpoint will return details about the…	v
o	--projectId	OPTIONAL: ID of a project. If passed in, only details about that project will be returned…	v
o	--addonId	OPTIONAL: ID of a addon. If passed in, only details about that addon will be returned	v
o	--serviceId	OPTIONAL: ID of a service. If passed in, only details about that service will be returned…	v
o	--jobId	OPTIONAL: ID of a job. If passed in, only details about that job will be returned	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get invoice help
a	1	0
#	get invoice help	1
t	help
@	get integration
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--integration|--integrationId	ID of the provider integration, example: gcp-integration-1	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get cluster
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--cluster|--clusterId	ID of the cluster, example: gcp-cluster-1	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job
s	runs	Fetches run history for the given job
s	logs|log	Get log for the specified job
s	metrics|metric	Get metrics for the specified job
s	build-logs|build-log	Get log for the specified job
s	build-metrics|build-metric	Get metrics for the specified job
s	run	Returns data about the given job run
s	health-checks	Lists the health checks for the given job
s	builds	Lists builds for the given job
s	build	Gets information about a build for the job
s	build-arguments	Gets the build arguments of the given job. If the API key does not have the permission 'Project >…
s	build-argument-details	Get details about the build arguments accessible by the given job. Also requires the permission…
s	runtime-environment	Returns the runtime environment for the given job. If the API key does not have the permission…
s	runtime-environment-details	Get details about the runtime environment accessible by the given job. Also requires the…
s	deployment	Gets information about the deployment of the given job
s	containers	Gets a list of containers for the given job
s	branches|branch|brn	Gets information about the branches of the given job
s	pull-requests	Gets information about the pull-requests of the given job
s	help	Display help for command
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job runs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job logs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--job|--jobId	Job to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	-f|--tail	Tail will stream logs in real-time. Session will be kept open	
o	-l|--lineLimit	Number of lines to return	V
o	--startTime	Get logs generated after this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--endTime	Get logs generated before this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-d|--direction	Direction of logs. Ignored when tailing	v
o	--textIncludes	Filter log lines to include this text	v
o	--textNotIncludes	Filter log lines to not include this text	v
o	--regexIncludes	Filter log lines to match this regular expression	v
o	--regexNotIncludes	Filter log lines to not match this regular expression	v
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	--run|--runId	Job run id, example: 162b1977-6636-4000-929b-cc265b862ff0	V
o	-h|--help	Display help for command	
=	get job logs	-d
v	backward	
v	forward	
=	get job logs	-o
v	format	
v	json	
v	yaml	
@	get job metrics
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--job|--jobId	Job to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	--startTime	Get metrics after this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--endTime	Get metrics before this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-t|--metricTypes	Which metric type to fetch	v
o	--timestamp	Get metrics at this exact timestamp, if no timestamp set most recent time is used. example…	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	--run|--runId	Job run id, example: 162b1977-6636-4000-929b-cc265b862ff0	V
o	-h|--help	Display help for command	
=	get job metrics	-t
v	cpu	
v	memory	
v	networkIngress	
v	networkEgress	
v	tcpConnectionsOpen	
v	diskUsage	
v	requests	
v	http4xxResponses	
v	http5xxResponses	
=	get job metrics	-o
v	format	
v	json	
v	yaml	
@	get job build-logs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--job|--jobId	Job to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	-f|--tail	Tail will stream logs in real-time. Session will be kept open	
o	-l|--lineLimit	Number of lines to return	V
o	--startTime	Get logs generated after this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--endTime	Get logs generated before this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-d|--direction	Direction of logs. Ignored when tailing	v
o	--textIncludes	Filter log lines to include this text	v
o	--textNotIncludes	Filter log lines to not include this text	v
o	--regexIncludes	Filter log lines to match this regular expression	v
o	--regexNotIncludes	Filter log lines to not match this regular expression	v
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	--build|--buildId	Build to get logs from	V
o	--run|--runId	Job run id, example: 162b1977-6636-4000-929b-cc265b862ff0	V
o	-h|--help	Display help for command	
=	get job build-logs	-d
v	backward	
v	forward	
=	get job build-logs	-o
v	format	
v	json	
v	yaml	
@	get job build-metrics
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--job|--jobId	Job to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	--startTime	Get metrics after this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--endTime	Get metrics before this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-t|--metricTypes	Which metric type to fetch	v
o	--timestamp	Get metrics at this exact timestamp, if no timestamp set most recent time is used. example…	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	--build|--buildId	Build to get logs from	V
o	--run|--runId	Job run id, example: 162b1977-6636-4000-929b-cc265b862ff0	V
o	-h|--help	Display help for command	
=	get job build-metrics	-t
v	cpu	
v	memory	
v	networkIngress	
v	networkEgress	
v	tcpConnectionsOpen	
v	diskUsage	
v	requests	
v	http4xxResponses	
v	http5xxResponses	
=	get job build-metrics	-o
v	format	
v	json	
v	yaml	
@	get job run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--run|--runId	ID of the job run, example: d34582a4-35bd-4c71-8e7c-e36999b88723	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job health-checks
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job builds
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--build|--buildId	ID of the job build, example: joyous-view-6290	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job build-arguments
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--show	OPTIONAL: Which secrets to display - if set to `this` only the group's secrets are displayed, if…	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job build-argument-details
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job runtime-environment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--show	OPTIONAL: Which secrets to display - if set to `this` only the group's secrets are displayed, if…	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job runtime-environment-details
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job deployment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job containers
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job branches
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job pull-requests
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get job help
a	1	0
#	get job help	1
t	help
@	get log-sink
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--logSink|--logSinkId	ID of the log sink, example: example-log-sink	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get registry
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--credential|--credentialId	ID of the registry credential, example: example-credentials	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get domain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get subdomain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--subdomain	Name of the subdomain, example: app	v
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get dns-id
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get pipeline
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get release-flow
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--stage	Stage of the pipeline, example: development	v
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get release-flow-run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--run|--runId	ID of the release flow run, example: development	v
o	--stage	Stage of the pipeline, example: development	v
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get secret
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--show	OPTIONAL: Which secrets to display - if set to `this` only the group's secrets are displayed, if…	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get secret-details
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get secret-link
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service
s	deployment	Gets information about the deployment of the given service
s	logs|log	Get log for the specified service
s	metrics|metric	Get metrics for the specified service
s	build-logs|build-log	Get log for the specified service
s	build-metrics|build-metric	Get metrics for the specified service
s	ports	Lists the ports for the given service
s	health-checks	Lists the health checks for the given service
s	builds	Lists the builds for the service
s	build	Gets information about a build for the service
s	containers	Gets a list of containers for the given service
s	branches|branch|brn	Gets information about the branches of the given service
s	pull-requests	Gets information about the pull-requests of the given service
s	build-arguments	Gets the build arguments of the given service. If the API key does not have the permission…
s	build-argument-details	Get details about the build arguments accessible by the given service. Also requires the…
s	runtime-environment	Gets the runtime environment of the given service. If the API key does not have the permission…
s	runtime-environment-details	Get details about the runtime environment accessible by the given service. Also requires the…
s	help	Display help for command
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service deployment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service logs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--service|--serviceId	Service to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	-f|--tail	Tail will stream logs in real-time. Session will be kept open	
o	-l|--lineLimit	Number of lines to return	V
o	--startTime	Get logs generated after this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--endTime	Get logs generated before this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-d|--direction	Direction of logs. Ignored when tailing	v
o	--textIncludes	Filter log lines to include this text	v
o	--textNotIncludes	Filter log lines to not include this text	v
o	--regexIncludes	Filter log lines to match this regular expression	v
o	--regexNotIncludes	Filter log lines to not match this regular expression	v
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	-h|--help	Display help for command	
=	get service logs	-d
v	backward	
v	forward	
=	get service logs	-o
v	format	
v	json	
v	yaml	
@	get service metrics
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--service|--serviceId	Service to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	--startTime	Get metrics after this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--endTime	Get metrics before this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-t|--metricTypes	Which metric type to fetch	v
o	--timestamp	Get metrics at this exact timestamp, if no timestamp set most recent time is used. example…	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	-h|--help	Display help for command	
=	get service metrics	-t
v	cpu	
v	memory	
v	networkIngress	
v	networkEgress	
v	tcpConnectionsOpen	
v	diskUsage	
v	requests	
v	http4xxResponses	
v	http5xxResponses	
=	get service metrics	-o
v	format	
v	json	
v	yaml	
@	get service build-logs
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--service|--serviceId	Service to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	-f|--tail	Tail will stream logs in real-time. Session will be kept open	
o	-l|--lineLimit	Number of lines to return	V
o	--startTime	Get logs generated after this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--endTime	Get logs generated before this time, example: 2020-02-02T02:02:02Z (date string) or 1580608922…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-d|--direction	Direction of logs. Ignored when tailing	v
o	--textIncludes	Filter log lines to include this text	v
o	--textNotIncludes	Filter log lines to not include this text	v
o	--regexIncludes	Filter log lines to match this regular expression	v
o	--regexNotIncludes	Filter log lines to not match this regular expression	v
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	--build|--buildId	Build to get logs from	V
o	-h|--help	Display help for command	
=	get service build-logs	-d
v	backward	
v	forward	
=	get service build-logs	-o
v	format	
v	json	
v	yaml	
@	get service build-metrics
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	Project for logs	V
o	--service|--serviceId	Service to get logs from	V
o	--container|--containerId	Container to exec into (logs from all containers will be shown if not specified)	V
o	--startTime	Get metrics after this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--endTime	Get metrics before this timestamp, example: 2020-02-02T02:02:02Z (date string) or 1580608922 (unix…	v
o	--duration	Length of timespan in seconds. Only valid if not both, startTime and endTime are set	V
o	-t|--metricTypes	Which metric type to fetch	v
o	--timestamp	Get metrics at this exact timestamp, if no timestamp set most recent time is used. example…	V
o	--noDefaults	Don't use context default values, explicitly use options or ask	
o	-o|--output	Output formatting. Will use advanced formatting by default	V
o	--build|--buildId	Build to get logs from	V
o	-h|--help	Display help for command	
=	get service build-metrics	-t
v	cpu	
v	memory	
v	networkIngress	
v	networkEgress	
v	tcpConnectionsOpen	
v	diskUsage	
v	requests	
v	http4xxResponses	
v	http5xxResponses	
=	get service build-metrics	-o
v	format	
v	json	
v	yaml	
@	get service ports
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service health-checks
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service builds
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--build|--buildId	ID of the service build, example: joyous-view-6290	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service containers
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service branches
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service pull-requests
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service build-arguments
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--show	OPTIONAL: Which secrets to display - if set to `this` only the group's secrets are displayed, if…	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service build-argument-details
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service runtime-environment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--show	OPTIONAL: Which secrets to display - if set to `this` only the group's secrets are displayed, if…	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service runtime-environment-details
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get service help
a	1	0
#	get service help	1
t	help
@	get template
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--template|--templateId	ID of the template, example: example-template	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get template-run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--templateRun|--templateRunId	ID of the template run, example: 16cf800b-ab28-421a-8ff9-a935b5ee89ad	v
o	--template|--templateId	ID of the template, example: example-template	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get volume
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--volume|--volumeId	ID of the volume, example: example-volume	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	get help
a	1	0
#	get help	1
t	help
@	delete
s	project|projects|prj	Delete the given project. Fails if the project isn't empty
s	addon|addons|adn	Deletes the given addon
s	backup	Deletes a given backup
s	integration	Delete the given integration. Fails if the integration is associated with existing clusters
s	cluster	Delete the given cluster. Fails if the cluster has associated projects
s	job|jobs	Deletes the given job
s	log-sink	Deletes a log sink
s	registry	Deletes a set of registry credential data
s	domain|domains|dmn	Deletes a domain and each of its registered subdomains
s	subdomain	Removes a subdomain from a domain
s	secret|secrets|scrt	Delete a secret
s	secret-link	Unlinks an addon from the secret group
s	service|services|svc	Deletes the given service
s	template|templates|tpl	Delete a template
s	volume|volumes|vol	Deletes this volume and its associated data
s	help	Display help for command
o	-h|--help	Display help for command	
@	delete project
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete addon
s	backup-schedule	Deletes a backup schedule for an addon
s	help	Display help for command
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete addon backup-schedule
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--schedule|--scheduleId	ID of the backup schedule, example: 62d5729ab8593e3e33b65105	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete addon help
a	1	0
#	delete addon help	1
t	help
@	delete backup
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete integration
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--integration|--integrationId	ID of the provider integration, example: gcp-integration-1	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete cluster
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--cluster|--clusterId	ID of the cluster, example: gcp-cluster-1	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete job
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete log-sink
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--logSink|--logSinkId	ID of the log sink, example: example-log-sink	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete registry
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--credential|--credentialId	ID of the registry credential, example: example-credentials	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete domain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete subdomain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--subdomain	Name of the subdomain, example: app	v
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete secret
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete secret-link
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete template
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--template|--templateId	ID of the template, example: example-template	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete volume
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--volume|--volumeId	ID of the volume, example: example-volume	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	--force	OPTIONAL: Don't ask for confirmation	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	delete help
a	1	0
#	delete help	1
t	help
@	scale
s	addon|addons|adn	Modifies the allocated resources for the given addon
s	job|jobs	Modifies the scaling settings for the given job
s	service|services|svc	Modifies the scaling settings for the given service
s	help	Display help for command
o	-h|--help	Display help for command	
@	scale addon
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	scale job
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	scale service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	scale help
a	1	0
#	scale help	1
t	help
@	update
s	addon|addons|adn	Update Northflank addon properties
s	integration	Update information about the given integration
s	cluster	Update an existing cluster
s	job|jobs	Update Northflank job properties
s	log-sink	Updates the settings for a log sink
s	registry	Updates a set of registry credential data
s	release-flow	Updates a release flow
s	secret|secrets|scrt	Update a secret
s	secret-link	Link an addon to the secret group or edit the settings of the linked addon
s	service|services|svc	Update Northflank service properties
s	volume|volumes|vol	Update volume mounts and storage size
s	help	Display help for command
o	-h|--help	Display help for command	
@	update addon
s	version	Upgrades the addon to a new version
s	network-settings	Updates the network settings for the addon
s	security	Updates the security rules for the addon
s	help	Display help for command
o	-h|--help	Display help for command	
@	update addon version
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update addon network-settings
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update addon security
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update addon help
a	1	0
#	update addon help	1
t	help
@	update integration
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--integration|--integrationId	ID of the provider integration, example: gcp-integration-1	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update cluster
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--cluster|--clusterId	ID of the cluster, example: gcp-cluster-1	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job
s	settings	Updates settings for the job
s	health-checks	Updates health checks for the given job
s	build-options	Updates the build options for a given job
s	build-source	Updates the version control source for a given job
s	build-arguments	Sets build arguments for the given job
s	runtime-environment	Sets the runtime environment for the given job
s	deployment	Updates the deployment settings of the given job
s	help	Display help for command
o	-h|--help	Display help for command	
@	update job settings
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job health-checks
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job build-options
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job build-source
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job build-arguments
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job runtime-environment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job deployment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update job help
a	1	0
#	update job help	1
t	help
@	update log-sink
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--logSink|--logSinkId	ID of the log sink, example: example-log-sink	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update registry
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--credential|--credentialId	ID of the registry credential, example: example-credentials	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update release-flow
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--stage	Stage of the pipeline, example: development	v
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update secret
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update secret-link
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--secret|--secretId	ID of the secret, example: example-secret	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service
s	deployment	Updates the deployment settings of the given service
s	ports	Updates the list of ports for the given service
s	build-options	Updates the build options for a given service
s	build-source	Updates the version control source for a given build or combined service
s	health-checks	Updates health checks for the given service
s	build-arguments	Sets the build arguments for the given service
s	runtime-environment	Sets the runtime environment for the given service
s	help	Display help for command
o	-h|--help	Display help for command	
@	update service deployment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service ports
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service build-options
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service build-source
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service health-checks
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service build-arguments
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service runtime-environment
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update service help
a	1	0
#	update service help	1
t	help
@	update volume
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--volume|--volumeId	ID of the volume, example: example-volume	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	update help
a	1	0
#	update help	1
t	help
@	backup
s	addon|addons|adn	Initiates a backup for the given addon
s	help	Display help for command
o	-h|--help	Display help for command	
@	backup addon
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	backup help
a	1	0
#	backup help	1
t	help
@	restore
s	addon|addons|adn	Addon Northflank resources
s	help	Display help for command
o	-h|--help	Display help for command	
@	restore addon
s	backup	Restores the given addon to the given backup state
s	help	Display help for command
o	-h|--help	Display help for command	
@	restore addon backup
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	restore addon help
a	1	0
#	restore addon help	1
t	help
@	restore help
a	1	0
#	restore help	1
t	help
@	import
s	addon|addons|adn	Addon Northflank resources
s	help	Display help for command
o	-h|--help	Display help for command	
@	import addon
s	backup	Imports a database from an external archive or existing live database
s	help	Display help for command
o	-h|--help	Display help for command	
@	import addon backup
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	import addon help
a	1	0
#	import addon help	1
t	help
@	import help
a	1	0
#	import help	1
t	help
@	pause
s	addon|addons|adn	Pause the given addon
s	job|jobs	Pause the given job
s	log-sink	Pauses a given log sink
s	service|services|svc	Pause the given service
s	help	Display help for command
o	-h|--help	Display help for command	
@	pause addon
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	pause job
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	pause log-sink
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--logSink|--logSinkId	ID of the log sink, example: example-log-sink	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	pause service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	pause help
a	1	0
#	pause help	1
t	help
@	resume
s	addon|addons|adn	Resume the given addon if it is paused
s	job|jobs	Resumes the given job. Optionally takes several arguments to override resumed settings
s	log-sink	Resumes a paused log sink
s	service|services|svc	Resumes the given service. Optionally takes several arguments to override resumed settings
s	help	Display help for command
o	-h|--help	Display help for command	
@	resume addon
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	resume job
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	resume log-sink
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--logSink|--logSinkId	ID of the log sink, example: example-log-sink	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	resume service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	resume help
a	1	0
#	resume help	1
t	help
@	restart
s	addon|addons|adn	Restart the given addon
s	service|services|svc	Restarts the given service
s	help	Display help for command
o	-h|--help	Display help for command	
@	restart addon
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	restart service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	restart help
a	1	0
#	restart help	1
t	help
@	abort
s	addon|addons|adn	Addon Northflank resources
s	job|jobs	Job Northflank resources
s	release-flow-run	Abort the given release flow run
s	service|services|svc	Service Northflank resources
s	template-run	Abort the given template run
s	help	Display help for command
o	-h|--help	Display help for command	
@	abort addon
s	backup	Aborts the in progress backup
s	restore	Aborts an in-progress backup restore
s	help	Display help for command
o	-h|--help	Display help for command	
@	abort addon backup
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort addon restore
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort addon help
a	1	0
#	abort addon help	1
t	help
@	abort job
s	run	Aborts the given job run
s	build	Aborts the given job build
s	help	Display help for command
o	-h|--help	Display help for command	
@	abort job run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--run|--runId	ID of the job run, example: d34582a4-35bd-4c71-8e7c-e36999b88723	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort job build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--build|--buildId	ID of the job build, example: joyous-view-6290	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort job help
a	1	0
#	abort job help	1
t	help
@	abort release-flow-run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--run|--runId	ID of the release flow run, example: development	v
o	--stage	Stage of the pipeline, example: development	v
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort service
s	build	Aborts the given service build
s	help	Display help for command
o	-h|--help	Display help for command	
@	abort service build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--build|--buildId	ID of the service build, example: joyous-view-6290	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort service help
a	1	0
#	abort service help	1
t	help
@	abort template-run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--templateRun|--templateRunId	ID of the template run, example: 16cf800b-ab28-421a-8ff9-a935b5ee89ad	v
o	--template|--templateId	ID of the template, example: example-template	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	abort help
a	1	0
#	abort help	1
t	help
@	retain
s	addon|addons|adn	Addon Northflank resources
s	help	Display help for command
o	-h|--help	Display help for command	
@	retain addon
s	backup	Flags a temporary backup generated by a backup schedule to be retained indefinitely rather than…
s	help	Display help for command
o	-h|--help	Display help for command	
@	retain addon backup
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--backup|--backupId	ID of the backup, example: example-backup	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	retain addon help
a	1	0
#	retain addon help	1
t	help
@	retain help
a	1	0
#	retain help	1
t	help
@	start
s	addon|addons|adn	Addon Northflank resources
s	job|jobs	Job Northflank resources
s	service|services|svc	Service Northflank resources
s	help	Display help for command
o	-h|--help	Display help for command	
@	start addon
s	pitr	Restores an addon to a specific point in time
s	help	Display help for command
o	-h|--help	Display help for command	
@	start addon pitr
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--addon|--addonId	ID of the addon, example: example-addon	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	start addon help
a	1	0
#	start addon help	1
t	help
@	start job
s	run	Starts a new job run for the given job
s	build	Start a new build for the given job. Given a commit sha, it will build that commit
s	help	Display help for command
o	-h|--help	Display help for command	
@	start job run
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	start job build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	start job help
a	1	0
#	start job help	1
t	help
@	start service
s	build	Start a new build for the given combined or build service. If given a commit sha, it will build…
s	help	Display help for command
o	-h|--help	Display help for command	
@	start service build
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--service|--serviceId	ID of the service, example: example-service	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	start service help
a	1	0
#	start service help	1
t	help
@	start help
a	1	0
#	start help	1
t	help
@	suspend
s	job|jobs	Modify cron job to toggle suspending of its schedule
s	help	Display help for command
o	-h|--help	Display help for command	
@	suspend job
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--job|--jobId	ID of the job, example: example-job	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	suspend help
a	1	0
#	suspend help	1
t	help
@	add
s	registry	Adds a new set of container registry credentials to this account
s	domain|domains|dmn	Domain Northflank resources
s	help	Display help for command
o	-h|--help	Display help for command	
@	add registry
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	add domain
s	subdomain	Adds a new subdomain to the domain
s	help	Display help for command
o	-h|--help	Display help for command	
@	add domain subdomain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	add domain help
a	1	0
#	add domain help	1
t	help
@	add help
a	1	0
#	add help	1
t	help
@	verify
s	domain|domains|dmn	Attempts to verify the domain
s	subdomain	Gets details about the given subdomain
s	help	Display help for command
o	-h|--help	Display help for command	
@	verify domain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	verify subdomain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--subdomain	Name of the subdomain, example: app	v
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	verify help
a	1	0
#	verify help	1
t	help
@	assign
s	subdomain	Subdomain Northflank resources
s	help	Display help for command
o	-h|--help	Display help for command	
@	assign subdomain
s	service|services|svc	Assigns a service port to the given subdomain
s	help	Display help for command
o	-h|--help	Display help for command	
@	assign subdomain service
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--subdomain	Name of the subdomain, example: app	v
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	assign subdomain help
a	1	0
#	assign subdomain help	1
t	help
@	assign help
a	1	0
#	assign help	1
t	help
@	unassign
s	subdomain	Removes a subdomain from its assigned service
s	help	Display help for command
o	-h|--help	Display help for command	
@	unassign subdomain
o	--verbose	Verbose output	
o	--quiet	No console output	
o	--subdomain	Name of the subdomain, example: app	v
o	--domain	Name of the domain, example: example.com	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	unassign help
a	1	0
#	unassign help	1
t	help
@	run
s	release-flow	Runs a given release flow with given arguments. This endpoint can be used as part of a CI pipeline…
s	template|templates|tpl	Run a template
s	help	Display help for command
o	-h|--help	Display help for command	
@	run release-flow
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--stage	Stage of the pipeline, example: development	v
o	--pipeline|--pipelineId	ID of the pipeline, example: example-pipeline	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	run template
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--template|--templateId	ID of the template, example: example-template	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	run help
a	1	0
#	run help	1
t	help
@	attach
s	volume|volumes|vol	Attach a volume
s	help	Display help for command
o	-h|--help	Display help for command	
@	attach volume
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--volume|--volumeId	ID of the volume, example: example-volume	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	attach help
a	1	0
#	attach help	1
t	help
@	detach
s	volume|volumes|vol	Detach a volume
s	help	Display help for command
o	-h|--help	Display help for command	
@	detach volume
o	--verbose	Verbose output	
o	--quiet	No console output	
o	-f|--file	File to load resource json from	v
o	-i|--input	JSON-formatted resource definition, takes precedence over "--file"	v
o	--volume|--volumeId	ID of the volume, example: example-volume	v
o	--project|--projectId	ID of the project, example: default-project	v
o	--noDefaults	OPTIONAL: Don't use context default values, explicitly use options or ask	
o	-o|--output	OPTIONAL: Output formatting, options: '--output json|yaml'	v
o	-h|--help	Display help for command	
@	detach help
a	1	0
#	detach help	1
t	help
@	command-overview
o	--verbose	Print command descriptions	
o	-h|--help	Display help for command	
@	help
a	1	0
#	help	1
t	help

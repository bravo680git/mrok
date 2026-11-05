@	
s	search	Run a code search
s	api	Sourcegraph API Access
s	login	'src login' helps you authenticate 'src' to access a Sourcegraph instance with your user credentials
s	batch	'Batch gives you a declarative structure for finding and modifying code across all of your…
s	config	'src config' helps you configure 'src'
s	extsvc	Edit or view external service configuration on the Sourcegraph instance
s	lsif	Upload an LSIF dumps
s	orgs	Create, edit, view, or delete organizations and members
s	repos	View or delete repositories
s	serve-git	By default 'src serve-git' will recursively serve your current directory on the address ':3434'
s	users	Create, edit, view, tag, or delete users
s	validate	EXPERIMENTAL: Instance validation provides a quick way to check that a Sourcegraph instance…
o	--help|-h	Show help for src	
@	search
o	-display	Limit the number of results that are displayed. Only supported together with stream flag…	
o	-dump-requests	Log GraphQL requests and responses to stdout	
o	-explain-json	Explain the JSON output schema and exit	
o	-get-curl	Print the curl command for executing this query and exit. (WARNING: Includes printing your access…	
o	-insecure-skip-verify	Skip validation of TLD certificates against trusted chains	
o	-json	Whether or not to output results as JSON	
o	-less	Pipe output to `less -R` (only if stdout is terminal, and not json flag)	
o	-stream	Consume results as stream. Streaming search only supports a subset of flags and parameters: trace…	
o	-trace	Log the trace ID for requests	
o	-user-agent-telemetry	Include the operating system and architecture in the User-Agent sent with requests to Sourcegraph	
@	api
o	-get-curl	Print the curl command for executing this query and exit (WARNING: includes printing your access…	
o	-dump-requests	Log GraphQL requests and responses to stdout	
o	-insecure-skip-verify	Skip validation of TLS certificates against trusted chains	
o	-query	GraphQL query to execute, e.g. ‘query { currentUser { username } }’ (stdin otherwise)	
o	-trace	Log the trace ID for requests	
o	-user-agent-telemetry	Include the operating system and architecture in the User-Agent sent with requests to Sourcegraph	
o	-vars	GraphQL query variables to include as JSON string, e.g. ‘{“var”: “val”, “var2”: “val2”}’	
@	login
o	-dump-requests	Log GraphQL requests and responses to stdout	
o	-get-curl	Print the curl command for executing this query and exit (WARNING: includes printing your access…	
o	-insecure-skip-verify	Skip validation of TLS certificates against trusted chains	
o	-trace	Log the trace ID for requests	
o	-user-agent-telemetry	Include the operating system and architecture in the User-Agent sent with requests to Sourcegraph	
@	batch
s	apply	Apply batch
s	exec	Execute batch
s	new	New batch
s	preview	Preview batch
s	repositories	Repositories to batch
s	validate	Validate batch
@	batch apply
@	batch exec
@	batch new
@	batch preview
@	batch repositories
@	batch validate
@	config
s	edit	Edit config
s	get	Get configs
s	list	List configs
@	config edit
@	config get
@	config list
@	extsvc
s	edit	Edit external service configuration
s	list	List external service configurations
@	extsvc edit
@	extsvc list
@	lsif
s	upload	Upload LSIF dump
@	lsif upload
@	orgs
s	create	Create an organization
s	delete	Delete an organization
s	get	Get an organization
s	list	List organizations
s	members	List organization members
@	orgs create
@	orgs delete
@	orgs get
@	orgs list
@	orgs members
@	repos
s	delete	Delete repository
s	get	Get repository
s	list	List repositories
@	repos delete
@	repos get
@	repos list
@	serve-git
o	-addr	Address on which to server (end with : for unused port)	
o	-list	List found repository names	
@	users
s	create	Create user
s	delete	Delete user
s	get	Get user
s	list	List users
s	tag	Tag user
@	users create
@	users delete
@	users get
@	users list
@	users tag
@	validate
o	-context	Comma-separated list of key=value pairs to add to the script execution context	
o	-dump-requests	Log GraphQL requests and responses to stdout	
o	-get-curl	Print the curl command for executing this query and exit (WARNING: includes printing your access…	
o	-insecure-skip-verify	Skip validation of TLS certificates against trusted chains	
o	-secrets	Path to a file containing key=value lines. The key value pairs will be added to the script context	
o	-trace	Log the trace ID for requests	
o	-user-agent-telemetry	Include the operating system and architecture in the User-Agent sent with requests to Sourcegraph	

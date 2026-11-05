@	
s	generate	Generate a new worker project
s	kv:namespace	Interact with your Workers KV Namespaces
s	kv:key	Individually manage Workers KV key-value
s	kv:bulk	Interact with multiple Workers KV key-value pairs at once
s	route	List or delete worker routes
s	secret	Generate a secret that can be referenced in the worker script
s	init	Create a wrangler.toml for an existing project
s	build	Build your worker
s	preview	Preview your code temporarily on cloudflareworkers.com
s	dev	Start a local server for developing your worker
s	publish	Publish your worker to the orange cloud
s	config	Authenticate Wrangler with a Cloudflare API Token or Global API Key
s	subdomain	Configure your workers.dev subdomain
s	whoami	Retrieve your user info and test your auth config
s	tail	Aggregate logs from production worker
s	login	Authenticate Wrangler with your Cloudflare username and password
s	report	Report an error caught by Wrangler to Cloudflare
s	help	Prints this message or the help of the given subcommand(s)
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	-V|--version	Prints version information	
@	generate
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	-s|--site	Initializes a Workers Sites project. Overrides 'type'	V
o	-t|--type	The type of project you want generated	V
a	2	0
=	generate	-c
t	filepaths
@	kv:namespace
s	create	Create a new namespace
s	delete	Delete namespace
s	list	List all namespaces on your Cloudflare account
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	kv:namespace	-c
t	filepaths
@	kv:namespace create
a	1	0
@	kv:namespace delete
@	kv:namespace list
@	kv:key
s	delete	Delete a key and its value from a namespace
s	get	Get a key's value from a namespace
s	help	Prints this message or the help of the given subcommand(s)
s	list	List all keys in a namespace. Produces JSON output
s	put	Put a key-value pair into a namespace
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	kv:key	-c
t	filepaths
@	kv:key delete
o	-b|--binding	The binding of the namespace this action applies to	v
o	-n|--namespace-id	The ID of the namespace this action applies to	v
a	1	0
@	kv:key get
a	1	0
@	kv:key help
@	kv:key list
@	kv:key put
a	1	0
@	kv:bulk
s	delete	Delete multiple keys and their values from a namespace
s	help	Prints this message or the help of the given subcommand(s)
s	put	Upload multiple key-value pairs to a namespace
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	kv:bulk	-c
t	filepaths
@	kv:bulk delete
a	1	0
@	kv:bulk help
@	kv:bulk put
a	1	0
#	kv:bulk put	1
t	filepaths
@	route
s	delete	Delete a route by ID
s	list	List all routes associated with a zone (outputs json)
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	route	-c
t	filepaths
@	route delete
a	1	0
@	route list
@	secret
s	delete	Delete a secret variable from a script
s	list	List all secrets for a script
s	put	Create or update a secret variable for a script
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	secret	-c
t	filepaths
@	secret delete
a	1	0
@	secret list
@	secret put
a	1	0
@	init
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	-s|--site	Initializes a Workers Sites project. Overrides 'type'	
o	-t|--type	The type of project you want generated	V
a	1	0
=	init	-c
t	filepaths
@	build
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	build	-c
t	filepaths
@	preview
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	--headless	Don't open the browser on preview	
o	--watch	Watch your project for changes and update the preview	
o	-u|--url	URL to open in the worker preview	
a	2	0
=	preview	-c
t	filepaths
#	preview	1
v	get	
v	post	
@	dev
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--host	Host to forward requests to, defaults to the zone of	v
o	-i|--ip	IP to listen on. Defaults to 127.0.0.1	v
o	-p|--port	Port to listen on. Defaults to 8787	v
=	dev	-c
t	filepaths
@	publish
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	--delete-class	Delete all durable objects associated with a class in your script	v
o	--new-class	Allow durable objects to be created from a class in your script	v
o	--rename-class	Rename a durable object class in your script	v
o	--transfer-class	Transfer all durable objects associated with a class in another script to a class in this script	v
a	1	0
=	publish	-c
t	filepaths
#	publish	1
v	json	
@	config
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	--api-key	Use an email and global API key for authentication. This is not recommended; use API tokens (the…	
o	--no-verify	Do not verify provided credentials before writing out Wrangler config file	
=	config	-c
t	filepaths
@	subdomain
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
a	1	0
=	subdomain	-c
t	filepaths
@	whoami
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	whoami	-c
t	filepaths
@	tail
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	-f|--format	Specify an output format [default: json] [possible values: json, pretty]	v
o	--metrics	Provides endpoint for cloudflared metrics. Used to retrieve tunnel url	v
o	-p|--port	Port to accept tail log requests	v
=	tail	-c
t	filepaths
=	tail	-f
v	json	
v	pretty	
@	login
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
=	login	-c
t	filepaths
@	report
o	-c|--config	Path to configuration file [default: wrangler.toml]	v
o	-e|--env	Environment to perform a command on	v
o	-h|--help	Prints help information	
o	--verbose	Toggle verbose output (when applicable)	
o	log	Specifies a log to report (e.g. --log=1619728882567.log)	v
=	report	-c
t	filepaths
=	report	log
t	filepaths
@	help
a	1	0

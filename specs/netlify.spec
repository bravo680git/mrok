@	
s	addons:auth|addon:auth	Login to add-on provider
s	addons:config|addon:config	Configure add-on settings
s	addons:create|addon:create	Add an add-on extension to your site
s	addons:delete|addon:delete	Remove an add-on extension to your site
s	addons:list|addon:list	List currently installed add-ons for site
s	api	Run any Netlify API method
s	build	(Beta) Build on your local machine
s	completion	(Beta) Generate shell completion script
s	completion:generate	Generates completion script
s	completion:generate:alias	Generates completion script for alias
s	deploy	Create a new deploy from the contents of a folder
s	dev	Local dev server
s	dev:exec	Exec command
s	dev:trace	Trace command
s	env	(Beta) Control environment variables for the current site
s	env:get	Get resolved value of specified environment variable (includes netlify.toml)
s	env:import	Import and set environment variables from .env file
s	env:list	Lists resolved environment variables for site (includes netlify.toml)
s	env:set	Set value of environment variable
s	env:unset|env:delete|env:remove	Unset an environment variable which removes it from the UI
s	functions:build|function:build	Build functions locally
s	functions:create|function:create	Create a new function locally
s	functions:invoke|function:trigger	Trigger a function while in netlify dev with simulated data, good for testing function calls…
s	functions:list|function:list	List functions that exist locally
s	functions:serve|function:server	(Beta) Serve functions locally
s	init	Configure continuous deployment for a new or existing site. To create a new site without…
s	link	Link a local repo or project folder to an existing site on Netlify
s	lm	Handle Netlify Large Media operations
s	lm:info	Show large media requirements information
s	lm:install|lm:init	Configures your computer to use Netlify Large Media
s	lm:setup	Configures your site to use Netlify Large Media
s	login	Login to your Netlify account
s	open	Open settings for the site linked to the current folder
s	open:admin	Opens current site admin UI in Netlify
s	open:site	Opens current site url in browser
s	sites:create	Create an empty site (advanced)
s	sites:delete	Delete a site
s	sites:list	List all sites you have access to
s	status	Print status information
s	status:hooks	Print hook information of the linked site
s	unlink	Unlink a local folder from a Netlify site
s	watch	Watch for site deploy to finish
s	help	List available sub-commands
o	--telemetry-disable	Opt out of sharing usage data	
o	--telemetry-enable	Allow your usage to help shape development	
@	addons:auth
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	addons:config
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	addons:create
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	addons:delete
o	-f|--force	Delete without prompting (useful for CI)	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	addons:list
o	--json	Output return values as JSON	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	api
o	-d|--data	Data to use	v
o	--list	List out available API methods	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	build
o	-o|--offline	Disables any features that require network access	
o	--context	Build context	v
o	--dry	Dry run: show instructions without running them	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	completion
o	-s|--shell	Name of shell (bash|fish|zsh)	v
=	completion	-s
v	bash	
v	fish	
v	zsh	
@	completion:generate
o	-s|--shell	(required) Name of shell [bash|fish|zsh]	
@	completion:generate:alias
o	-s|--shell	(required) Name of shell [bash|fish|zsh]	
@	deploy
o	-a|--auth	Netlify auth token to deploy with	v
o	-b|--branch	Serves the same functionality as --alias. Deprecated and will be removed in future versions	v
o	-d|--dir	Specify a folder to deploy	v
o	-f|--functions	Specify a functions folder to deploy	v
o	-m|--message	A short message to include in the deploy log	v
o	-o|--open	Open site after deploy	
o	-p|--prod	Deploy to production	
o	-s|--site	A site ID to deploy to	v
o	--alias	Specifies the alias for deployment, the string at the beginning of the deploy subdomain	v
o	--build	Run build command before deploying	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
o	--json	Output deployment data as JSON	
o	--prodIfUnlocked	Deploy to production if unlocked, create a draft otherwise	
o	--skip-functions-cache	Ignore any functions created as part of a previous `build` or `deploy` commands, forcing them to…	
o	--timeout	Timeout to wait for deployment to finish	v
o	trigger	Trigger a new build of your site on Netlify without uploading local files	
=	deploy	-d
t	folders
=	deploy	-f
t	folders
@	dev
o	-c|--command	Command to run	v
o	-d|--dir	Dir with static files	v
o	-f|--functions	Specify a functions folder to serve	v
o	-l|--live	Start a public live session	
o	-o|--offline	Disables any features that require network access	
o	-p|--port	Port of netlify dev	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
o	--framework	Framework to use. Defaults to #auto which automatically detects a framework	v
o	--targetPort	Port of target app server	v
=	dev	-d
t	filepaths
=	dev	-f
t	folders
@	dev:exec
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	dev:trace
o	-H|--header	Request header, this flag can be used multiple times. Example: "Host: netlify.test"	v
o	-X|--request	Specifies a custom request method [default: GET]	v
o	-B|--cookie	Request cookie, this flag can be used multiple times. Example: "nf_jwt=token"	v
o	-w|--watch	Path to the publish directory	v
o	--debug	Print debugging information	
a	1	0
=	dev:trace	-w
t	filepaths
@	env
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	env:get
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	env:import
o	-r|--replaceExisting	Replace all existing variables instead of merging them with the current ones	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
#	env:import	1
t	filepaths
@	env:list
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	env:set
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	2	0
@	env:unset
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	functions:build
o	-f|--functions	Specify a functions directory to build to	v
o	-s|--src	Specify the source directory for the functions	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
=	functions:build	-f
t	folders
@	functions:create
o	-n|--name	Function name	v
o	-u|--url	Pull template from URL	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	functions:invoke
o	-f|--functions	Specify a functions folder to parse, overriding netlify.toml	v
o	-n|--name	Function name to invoke	v
o	-p|--payload	Supply POST payload in stringified json, or a path to a json file	v
o	-q|--querystring	Querystring to add to your function invocation	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
o	--identity	Simulate Netlify Identity authentication JWT	
o	--no-identity	Affirm unauthenticated request	
o	port	Port where netlify dev is accessible. e.g. 8888	v
a	1	0
=	functions:invoke	-f
t	folders
=	functions:invoke	-p
t	filepaths
@	functions:list
o	-f|--functions	Specify a functions directory to list	v
o	-n|--name	Name to print	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
o	--json	Output function data as JSON	
=	functions:list	-f
t	folders
@	functions:serve
o	-f|--functions	Specify a functions folder to deploy	v
o	-o|--offline	Disables any features that require network access	
o	-p|--port	Port of netlify dev	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
=	functions:serve	-f
t	folders
@	init
o	-m|--manual	Manually configure a git remote for CI	
o	--force	Reinitialize CI hooks if the linked site is already configured to use CI	
o	--gitRemoteName	Name of Git remote to use. e.g. "origin"	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	link
o	--gitRemoteName	Name of Git remote to use. e.g. "origin"	v
o	--id	ID of site to link to	v
o	--name	Name of site to link to	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	lm
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	lm:info
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	lm:install
o	-f|--force	Force the credentials helper installation	
@	lm:setup
o	-f|--force-install	Force the credentials helper installation	
o	-s|--skip-install	Skip the credentials helper installation check	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	login
o	--auth	Netlify auth token	v
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
o	--json	Output return values as JSON	
o	--new	Login to new Netlify account	
o	--silent	Silence CLI output	
@	open
o	--admin	Open Netlify site	
o	--site	Open site	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	open:admin
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	open:site
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	sites:create
o	-a|--account-slug	Account slug to create the site under	
o	-c|--with-ci	Initialize CI hooks during site creation	
o	-m|--manual	Force manual CI setup. Used --with-ci flag	
o	-n|--name	Name of site	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	sites:delete
o	-f|--force	Delete without prompting (useful for CI)	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
a	1	0
@	sites:list
o	--json	Output site data as JSON	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	status
o	verbose	Output system info	
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	status:hooks
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	unlink
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	watch
o	--debug	Print debugging information	
o	--httpProxy	Proxy server address to route requests through	v
o	--httpProxyCertificateFilename	Certificate file to use when connecting using a proxy server	v
@	help
a	1	0
#	help	1
v	addons:auth	Login to add-on provider
v	addon:auth	Login to add-on provider
v	addons:config	Configure add-on settings
v	addon:config	Configure add-on settings
v	addons:create	Add an add-on extension to your site
v	addon:create	Add an add-on extension to your site
v	addons:delete	Remove an add-on extension to your site
v	addon:delete	Remove an add-on extension to your site
v	addons:list	List currently installed add-ons for site
v	addon:list	List currently installed add-ons for site
v	api	Run any Netlify API method
v	build	(Beta) Build on your local machine
v	completion	(Beta) Generate shell completion script
v	completion:generate	Generates completion script
v	completion:generate:alias	Generates completion script for alias
v	deploy	Create a new deploy from the contents of a folder
v	dev	Local dev server
v	dev:exec	Exec command
v	dev:trace	Trace command
v	env	(Beta) Control environment variables for the current site
v	env:get	Get resolved value of specified environment variable (includes netlify.toml)
v	env:import	Import and set environment variables from .env file
v	env:list	Lists resolved environment variables for site (includes netlify.toml)
v	env:set	Set value of environment variable
v	env:unset	Unset an environment variable which removes it from the UI
v	env:delete	Unset an environment variable which removes it from the UI
v	env:remove	Unset an environment variable which removes it from the UI
v	functions:build	Build functions locally
v	function:build	Build functions locally
v	functions:create	Create a new function locally
v	function:create	Create a new function locally
v	functions:invoke	Trigger a function while in netlify dev with simulated data, good for testing function calls…
v	function:trigger	Trigger a function while in netlify dev with simulated data, good for testing function calls…
v	functions:list	List functions that exist locally
v	function:list	List functions that exist locally
v	functions:serve	(Beta) Serve functions locally
v	function:server	(Beta) Serve functions locally
v	init	Configure continuous deployment for a new or existing site. To create a new site without…
v	link	Link a local repo or project folder to an existing site on Netlify
v	lm	Handle Netlify Large Media operations
v	lm:info	Show large media requirements information
v	lm:install	Configures your computer to use Netlify Large Media
v	lm:init	Configures your computer to use Netlify Large Media
v	lm:setup	Configures your site to use Netlify Large Media
v	login	Login to your Netlify account
v	open	Open settings for the site linked to the current folder
v	open:admin	Opens current site admin UI in Netlify
v	open:site	Opens current site url in browser
v	sites:create	Create an empty site (advanced)
v	sites:delete	Delete a site
v	sites:list	List all sites you have access to
v	status	Print status information
v	status:hooks	Print hook information of the linked site
v	unlink	Unlink a local folder from a Netlify site
v	watch	Watch for site deploy to finish

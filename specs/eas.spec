@	
s	account:login|login	Log in with your Expo account
s	account:logout|logout	Log out
s	account:view|whoami	Show the username you are logged in as
s	analytics	Display or change analytics settings
s	autocomplete	Display autocomplete installation instructions
s	branch:create	Create a branch
s	branch:delete	Delete a branch
s	branch:list	List all branches
s	branch:rename	Rename a branch
s	branch:view	View a branch
s	build	Start a build
s	build:cancel	Cancel a build
s	build:configure	Configure the project to support EAS build
s	build:inspect	Inspect the state of the project at specific build stages, useful for troubleshooting
s	build:list	List all builds for your project
s	build:submit|submit	Submit app binary to App Store and/or Play Store
s	build:version:set	Update version of an app
s	build:version:sync	Update a version in native code with a value stored on EAS servers
s	build:view	View a build for your project
s	channel:create	Create a channel
s	channel:edit	Point a channel at a new branch
s	channel:list	List all channels
s	channel:view	View a channel
s	config	Display project configuration (app.json + eas.json)
s	credentials	Manage credentials
s	device:create	Register new Apple devices to use for internal distribution
s	device:delete	Remove a registered device from your account
s	device:list	List all registered devices for your account
s	device:view	View a device for your project
s	diagnostics	Display environment info
s	help	Display help for eas-cli
s	metadata:pull	Generate the local store configuration from the app stores
s	metadata:push	Sync the local store configuration to the app stores
s	open	Open the project page in a web browser
s	project:info	Information about the current project
s	project:init|init	Create or link an EAS project
s	secret:create	Create an environment secret on the current project or owner account
s	secret:delete	Delete an environment secret by ID
s	secret:list	List environment secrets available for your current app
s	update	Publish an update group
s	update:configure	Configure the project to support EAS update
s	update:delete	Delete all the updates in an update group
s	update:list	View the recent updates
s	update:view	Update group details
s	webhook:create	Create a webhook
s	webhook:delete	Delete a webhook
s	webhook:list	List webhooks
s	webhook:update	Update a webhook
s	webhook:view	View a webhook
@	account:login
@	account:logout
@	account:view
@	analytics
a	1	0
#	analytics	1
v	on	
v	off	
@	autocomplete
o	-r|--refresh-cache	Refresh cache (ignores displaying instructions)	
a	1	0
#	autocomplete	1
v	zsh	
v	bash	
@	branch:create
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	branch:delete
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	branch:list
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 50 and is capped at 100	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	v
=	branch:list	--limit
v	50	
v	51	
v	52	
v	53	
v	54	
v	55	
v	56	
v	57	
v	58	
v	59	
v	60	
v	61	
v	62	
v	63	
v	64	
v	65	
v	66	
v	67	
v	68	
v	69	
v	70	
v	71	
v	72	
v	73	
v	74	
v	75	
v	76	
v	77	
v	78	
v	79	
v	80	
v	81	
v	82	
v	83	
v	84	
v	85	
v	86	
v	87	
v	88	
v	89	
v	90	
v	91	
v	92	
v	93	
v	94	
v	95	
v	96	
v	97	
v	98	
v	99	
v	100	
@	branch:rename
o	--from	Current name of the branch	v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
o	--to	New name of the branch	v
@	branch:view
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 25 and is capped at 50	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	v
a	1	0
=	branch:view	--limit
v	25	
v	26	
v	27	
v	28	
v	29	
v	30	
v	31	
v	32	
v	33	
v	34	
v	35	
v	36	
v	37	
v	38	
v	39	
v	40	
v	41	
v	42	
v	43	
v	44	
v	45	
v	46	
v	47	
v	48	
v	49	
v	50	
@	build
o	-e|--profile	Name of the build profile from eas.json. Defaults to "production" if defined in eas.json	v
o	-m|--message	A short message describing the build	v
o	-p|--platform		v
o	--auto-submit	Submit on build complete using the submit profile with the same name as the build profile	
o	--auto-submit-with-profile	Submit on build complete using the submit profile with provided name	v
o	--clear-cache	Clear cache before the build	
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--local	Run build locally [experimental]	
o	--non-interactive	Run the command in non-interactive mode	
o	--output	Output path for local build	v
o	--no-wait	Don't wait for build(s) to complete	
o	--wait	Wait for build(s) to complete	
=	build	-p
v	android	
v	ios	
v	all	
@	build:cancel
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	build:configure
o	-p|--platform	Platform to configure	v
=	build:configure	-p
v	android	
v	ios	
v	all	
@	build:inspect
o	-e|--profile	Name of the build profile from eas.json. Defaults to "production" if defined in eas.json	v
o	-o|--output	(required) Output directory	v
o	-p|--platform	(required)	v
o	-s|--stage	(required) Stage of the build you want to inspect.	v
o	-v|--verbose		
o	--force	Delete OUTPUT_DIRECTORY if it already exists	
=	build:inspect	-p
v	android	
v	ios	
=	build:inspect	-s
v	archive	
v	pre-build	
v	post-build	
@	build:list
o	--appBuildVersion		v
o	--appIdentifier		v
o	--appVersion		v
o	--buildProfile		v
o	--channel		v
o	--distribution		v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 10 and is capped at 50	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	v
o	--platform		v
o	--runtimeVersion		v
o	--sdkVersion		v
o	--status		v
=	build:list	--distribution
v	store	
v	internal	
v	simulator	
=	build:list	--limit
v	10	
v	11	
v	12	
v	13	
v	14	
v	15	
v	16	
v	17	
v	18	
v	19	
v	20	
v	21	
v	22	
v	23	
v	24	
v	25	
v	26	
v	27	
v	28	
v	29	
v	30	
v	31	
v	32	
v	33	
v	34	
v	35	
v	36	
v	37	
v	38	
v	39	
v	40	
v	41	
v	42	
v	43	
v	44	
v	45	
v	46	
v	47	
v	48	
v	49	
v	50	
=	build:list	--platform
v	all	
v	android	
v	ios	
=	build:list	--status
v	new	
v	in-queue	
v	in-progress	
v	errored	
v	finished	
v	canceled	
@	build:submit
o	-e|--profile	Name of the submit profile from eas.json. Defaults to "production" if defined in eas.json	v
o	-p|--platform		v
o	--id	ID of the build to submit	v
o	--latest	Submit the latest build for specified platform	
o	--non-interactive	Run command in non-interactive mode	
o	--path	Path to the .apk/.aab/.ipa file	v
o	--url	App archive url	v
o	--verbose	Always print logs from Submission Service	
o	--no-wait	Don't wait for submission to complete	
o	--wait	Wait for submission to complete	
=	build:submit	-p
v	android	
v	ios	
v	all	
@	build:version:set
o	-e|--profile	Name of the build profile from eas.json. Defaults to "production" if defined in eas.json	v
o	-p|--platform		v
=	build:version:set	-p
v	android	
v	ios	
@	build:version:sync
o	-e|--profile	Name of the build profile from eas.json. Defaults to "production" if defined in eas.json	v
o	-p|--platform		v
=	build:version:sync	-p
v	android	
v	ios	
v	all	
@	build:view
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
a	1	0
@	channel:create
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	channel:edit
o	--branch	Name of the branch to point to	v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	channel:list
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 10 and is capped at 25	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	v
=	channel:list	--limit
v	10	
v	11	
v	12	
v	13	
v	14	
v	15	
v	16	
v	17	
v	18	
v	19	
v	20	
v	21	
v	22	
v	23	
v	24	
v	25	
@	channel:view
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 50 and is capped at 100	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	v
a	1	0
=	channel:view	--limit
v	50	
v	51	
v	52	
v	53	
v	54	
v	55	
v	56	
v	57	
v	58	
v	59	
v	60	
v	61	
v	62	
v	63	
v	64	
v	65	
v	66	
v	67	
v	68	
v	69	
v	70	
v	71	
v	72	
v	73	
v	74	
v	75	
v	76	
v	77	
v	78	
v	79	
v	80	
v	81	
v	82	
v	83	
v	84	
v	85	
v	86	
v	87	
v	88	
v	89	
v	90	
v	91	
v	92	
v	93	
v	94	
v	95	
v	96	
v	97	
v	98	
v	99	
v	100	
@	config
o	-e|--profile	Name of the build profile from eas.json. Defaults to "production" if defined in eas.json	v
o	-p|--platform		v
=	config	-p
v	android	
v	ios	
@	credentials
o	-p|--platform		v
=	credentials	-p
v	android	
v	ios	
@	device:create
@	device:delete
o	--apple-team-id	The Apple team ID on which to find the device	v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
o	--udid	The Apple device ID to disable	v
@	device:list
o	--apple-team-id		v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 50 and is capped at 100	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	v
=	device:list	--limit
v	50	
v	51	
v	52	
v	53	
v	54	
v	55	
v	56	
v	57	
v	58	
v	59	
v	60	
v	61	
v	62	
v	63	
v	64	
v	65	
v	66	
v	67	
v	68	
v	69	
v	70	
v	71	
v	72	
v	73	
v	74	
v	75	
v	76	
v	77	
v	78	
v	79	
v	80	
v	81	
v	82	
v	83	
v	84	
v	85	
v	86	
v	87	
v	88	
v	89	
v	90	
v	91	
v	92	
v	93	
v	94	
v	95	
v	96	
v	97	
v	98	
v	99	
v	100	
@	device:view
a	1	0
@	diagnostics
@	help
o	-n|--nested-commands	Include all nested commands in the output	
a	1	0
@	metadata:pull
o	-e|--profile	Name of the submit profile from eas.json. Defaults to "production" if defined in eas.json	v
@	metadata:push
o	-e|--profile	Name of the submit profile from eas.json. Defaults to "production" if defined in eas.json	
@	open
@	project:info
@	project:init
o	--force	Whether to overwrite any existing project ID	
o	--id	ID of the EAS project to link	v
o	--non-interactive	Run the command in non-interactive mode	
@	secret:create
o	--force	Delete and recreate existing secrets	
o	--name	Name of the secret	v
o	--non-interactive	Run the command in non-interactive mode	
o	--scope	[default: project] Scope for the secret	v
o	--type	The type of secret	v
o	--value	Text value or path to a file to store in the secret	v
=	secret:create	--scope
v	account	
v	project	
=	secret:create	--type
v	string	
v	file	
@	secret:delete
o	--id	ID of the secret to delete	v
o	--non-interactive	Run the command in non-interactive mode	
@	secret:list
@	update
o	-p|--platform	[default: all]	v
o	--auto	Use the current git branch and commit message for the EAS branch and update message	
o	--branch	Branch to publish the update group on	v
o	--group	Update group to republish	v
o	--input-dir	[default: dist] Location of the bundle	v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--message	A short message describing the update	v
o	--non-interactive	Run the command in non-interactive mode	
o	--private-key-path	File containing the PEM-encoded private key corresponding to the certificate in	v
o	--republish	Republish an update group	
o	--skip-bundler	Skip running Expo CLI to bundle the app before publishing	
=	update	-p
v	android	
v	ios	
v	all	
@	update:configure
o	-p|--platform	[default: all] Platform to configure	v
=	update:configure	-p
v	android	
v	ios	
v	all	
@	update:delete
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	update:list
o	--all	List updates on all branches	
o	--branch	List updates only on this branch	v
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
o	--limit	The number of items to fetch each query. Defaults to 25 and is capped at 50	v
o	--non-interactive	Run the command in non-interactive mode	
o	--offset	Start queries from specified index. Use for paginating results. Defaults to 0	
=	update:list	--limit
v	25	
v	26	
v	27	
v	28	
v	29	
v	30	
v	31	
v	32	
v	33	
v	34	
v	35	
v	36	
v	37	
v	38	
v	39	
v	40	
v	41	
v	42	
v	43	
v	44	
v	45	
v	46	
v	47	
v	48	
v	49	
v	50	
@	update:view
o	--json	Enable JSON output, non-JSON messages will be printed to stderr	
a	1	0
@	webhook:create
o	--event	Event type that triggers the webhook	v
o	--non-interactive	Run the command in non-interactive mode	
o	--secret	Secret used to create a hash signature of the request payload, provided in the 'Expo-Signature'…	v
o	--url	Webhook URL	v
=	webhook:create	--event
v	BUILD	
v	SUBMIT	
@	webhook:delete
o	--non-interactive	Run the command in non-interactive mode	
a	1	0
@	webhook:list
o	--event	Event type that triggers the webhook	v
=	webhook:list	--event
v	BUILD	
v	SUBMIT	
@	webhook:update
o	--event	Event type that triggers the webhook	v
o	--id	(required) Webhook ID	v
o	--non-interactive	Run the command in non-interactive mode	
o	--secret	Secret used to create a hash signature of the request payload, provided in the 'Expo-Signature'…	v
o	--url	Webhook URL	v
=	webhook:update	--event
v	BUILD	
v	SUBMIT	
@	webhook:view
a	1	0

@	
s	appdistribution:distribute	Upload a distribution
s	apps:android:sha:create	Add a SHA certificate hash for a given app id
s	apps:android:sha:delete	Delete a SHA certificate hash for a given app id
s	apps:create	Create a new Firebase app
s	auth:export	Export accounts from your Firebase project into a data file
s	auth:import	Import users into your Firebase project from a data file(.csv or .json)
s	database:get	Fetch and print JSON data at the specified path
s	database:instances:create	Create a realtime database instance
s	database:instances:list	List realtime database instances, optionally filtered by a specified location
s	database:profile	Profile the Realtime Database and generate a usage report
s	database:push	Add a new JSON object to a list of data in your Firebase
s	database:remove	Remove data from your Firebase at the specified path
s	database:set	Store JSON data at the specified path via STDIN, arg, or file
s	database:settings:get	Store JSON data at the specified path via STDIN, arg, or file
s	database:settings:set	Set the realtime database setting at path
s	database:update	Update some of the keys for the defined path in your Firebase
s	deploy	Deploy code and assets to your Firebase project
s	emulators:exec	Start the local Firebase emulators, run a test script, then shut down the emulators
s	emulators:export	Export data from running emulators
s	emulators:start	Start the local Firebase emulators
s	experimental:functions:shell	Launch full Node shell with emulated functions
s	ext:configure	Configure an existing extension instance
s	ext:info	List all the extensions that are installed in your Firebase project
s	ext:uninstall	Uninstall an extension that is installed in your Firebase project by instance ID
s	ext:update	Update an existing extension instance to the latest version
s	firestore:delete	Delete data from Cloud Firestore
s	firestore:indexes	List indexes in your project's Cloud Firestore database
s	functions:config:clone	Clone environment config from another project
s	functions:config:get	Fetch environment config stored at the given path
s	functions:config:set	Set environment config with key=value syntax
s	functions:log	Read logs from deployed functions
s	functions:shell	Launch full Node shell with emulated functions
s	help	Display help information
s	hosting:channel:create	Create a Firebase Hosting channel
s	hosting:channel:delete	Delete a Firebase Hosting channel
s	hosting:channel:deploy	Deploy to a specific Firebase Hosting channel
s	hosting:channel:list	List all Firebase Hosting channels for your project
s	hosting:channel:open	Opens the URL for a Firebase Hosting channel
s	hosting:clone	Clone a version from one site to another
s	hosting:disable	Stop serving web traffic to your Firebase Hosting site
s	hosting:sites:create	Create a Firebase Hosting site
s	hosting:sites:delete	Delete a Firebase Hosting site
s	hosting:sites:get	Print info about a Firebase Hosting site
s	hosting:sites:list	List Firebase Hosting sites
s	init	Setup a Firebase project in the current directory
s	login	Log the CLI into Firebase
s	login:add	Authorize the CLI for an additional account
s	login:ci	Generate an access token for use in non-interactive environments
s	login:list	List authorized CLI accounts
s	login:use	Set the default account to use for this project directory
s	logout	Log the CLI out of Firebase
s	open	Quickly open a browser to relevant project resources
s	projects:addfirebase	Add Firebase resources to a Google Cloud Platform project
s	projects:create	Creates a new Google Cloud Platform project, then adds Firebase resources to the project
s	projects:list	List all Firebase projects you have access to
s	remoteconfig:get	Get a Firebase project's Remote Config template
s	remoteconfig:rollback	Roll back a project's published Remote Config template to the one specified by the provided…
s	remoteconfig:versions:list	Get a list of Remote Config template versions that have been published for a Firebase project
s	serve	Start a local server for your static assets
s	setup:emulators:database	Downloads the database emulator
s	setup:emulators:firestore	Downloads the firestore emulator
s	setup:emulators:pubsub	Downloads the pubsub emulator
s	setup:emulators:ui	Downloads the ui emulator
s	target	Display configured deploy targets for the current project
s	target:apply	Apply a deploy target to a resource
s	target:clear	Clear all resources from a named resource target
s	target:remove	Remove a resource target
s	use	Set an active Firebase project for your working directory
@	appdistribution:distribute
o	--app	The app id of your Firebase app	v
o	--release-notes	Release notes to include with this distribution	
o	--release-notes-file	Path to file with release notes to include with this distribution	v
o	--testers	A comma separated list of tester emails to distribute to	v
o	--testers-file	Path to file with a comma separated list of tester emails to distribute to	v
o	--groups	A comma separated list of group aliases to distribute to	v
o	--groups-file	Path to file with a comma separated list of group aliases to distribute to	v
o	-h|--help	Output usage information	
a	1	0
@	apps:android:sha:create
o	-h|--help	Output usage information	
a	2	0
@	apps:android:sha:delete
o	-h|--help	Output usage information	
a	2	0
@	apps:create
o	-a|--package-name	Required package name for the Android app	v
o	-b|--bundle-id	Required bundle id for the iOS app	v
o	-s|--app-store-id	(optional) app store id for the iOS app	v
o	-h|--help	Output usage information	
a	2	0
@	auth:export
o	--format	Format of exported data (csv, json). Ignored if [dataFile] has format extension	v
o	-h|--help	Output usage information	
a	1	0
=	auth:export	--format
v	csv	
v	json	
#	auth:export	1
t	filepaths
@	auth:import
o	--hash-algo	Specify the hash algorithm used in password for these accounts	v
o	--hash-key	Specify the key used in hash algorithm	v
o	--salt-separator	Specify the salt separator which will be appended to salt when verifying password. only used by…	v
o	--rounds	Specify how many rounds for hash calculation	v
o	--mem-cost	Specify the memory cost for firebase scrypt, or cpu/memory cost for standard scrypt	v
o	--parallelization	Specify the parallelization for standard scrypt	v
o	--block-size	Specify the block size (normally is 8) for standard scrypt	v
o	--dk-len	Specify derived key length for standard scrypt	v
o	--hash-input-order	Specify the order of password and salt. Possible values are SALT_FIRST and PASSWORD_FIRST. MD5…	v
o	-h|--help	Output usage information	
a	1	0
#	auth:import	1
t	filepaths
@	database:get
a	1	0
@	database:instances:create
o	-l|--location	(optional) location for the database instance, defaults to us-central1	v
o	-h|--help	Output usage information	
a	1	0
@	database:instances:list
o	-h|--help	Output usage information	
@	database:profile
o	-o|--output	Save the output to the specified file	v
o	-d|--duration	Collect database usage information for the specified number of seconds	v
o	--raw	Output the raw stats collected as newline delimited json	v
o	--no-collapse	Prevent collapsing similar paths into $wildcard locations	
o	-i|--input	Generate the report based on the specified file instead of streaming logs from the database	v
o	--instance	Use the database <instance>.firebaseio.com (if omitted, use default database instance)	v
o	-h|--help	Output usage information	
@	database:push
o	-d|--data	Specify escaped JSON directly	v
o	--instance	Use the database <instance>.firebaseio.com (if omitted, use default database instance)	v
o	-h|--help	Output usage information	
a	1	0
#	database:push	1
t	filepaths
@	database:remove
o	-y|--confirm	Pass this option to bypass confirmation prompt	
o	--instance	Use the database <instance>.firebaseio.com (if omitted, use default database instance)	v
o	-h|--help	Output usage information	
a	1	0
#	database:remove	1
t	filepaths
@	database:set
o	-d|--data	Specify escaped JSON directly	v
o	-y|--confirm	Pass this option to bypass confirmation prompt	
o	--instance	Use the database <instance>.firebaseio.com (if omitted, use default database instance)	v
o	-h|--help	Output usage information	
a	1	0
#	database:set	1
t	filepaths
@	database:settings:get
o	--instance	Use the database <instance>.firebaseio.com (if omitted, uses default database instance)	v
o	-h|--help	Output usage information	
a	1	0
#	database:settings:get	1
t	filepaths
@	database:settings:set
o	--instance	Use the database <instance>.firebaseio.com (if omitted, use default database instance)	v
o	-h|--help	Output usage information	
a	2	0
@	database:update
o	-d|--data	Specify escaped JSON directly	v
o	-y|--confirm	Pass this option to bypass confirmation prompt	
o	--instance	Use the database <instance>.firebaseio.com (if omitted, use default database instance)	v
o	-h|--help	Output usage information	
a	1	0
#	database:update	1
t	filepaths
@	deploy
o	-p|--public	Override the Hosting public directory specified in firebase.json	
o	-m|--message	An optional message describing this deploy	v
o	-f|--force	Delete Cloud Functions missing from the current working directory without confirmation	
o	--only	Only deploy to specified, comma-separated targets (e.g. "hosting,storage"). For functions, can…	
o	--except	Deploy to all targets except specified (e.g. "database")	v
o	-h|--help	Output usage information	
@	emulators:exec
o	--only	Only specific emulators. This is a comma separated list of emulator names. Valid options are…	v
o	--inspect-functions	Emulate Cloud Functions in debug mode with the node inspector on the given port (9229 if not…	
o	--import	Import emulator data from a previous export (see emulators:export)	v
o	--export-on-exit	Automatically export emulator data (emulators:export) when the emulators make a clean exit…	
o	--ui	Run the Emulator UI	
o	-h|--help	Output usage information	
a	1	0
@	emulators:export
o	--only	Only specific emulators. This is a comma separated list of emulator names. Valid options are…	v
o	--force	Overwrite any export data in the target directory	
o	-h|--help	Output usage information	
a	1	0
#	emulators:export	1
t	filepaths
@	emulators:start
o	--only	Only specific emulators. This is a comma separated list of emulator names. Valid options are…	v
o	--inspect-functions	Emulate Cloud Functions in debug mode with the node inspector on the given port (9229 if not…	v
o	--import	Import emulator data from a previous export (see emulators:export)	
o	--export-on-exit	Automatically export emulator data (emulators:export) when the emulators make a clean exit…	
o	-h|--help	Output usage information	
@	experimental:functions:shell
o	-p|--port	The port on which to emulate functions (default: 5000) (default: 5000)	v
o	-h|--help	Output usage information	
@	ext:configure
o	--params	Path of params file with .env format	v
o	-h|--help	Output usage information	
a	1	0
@	ext:info
o	--markdown	Output info in Markdown suitable for constructing a README file	
o	-h|--help	Output usage information	
a	1	0
@	ext:uninstall
o	-f|--force	No confirmation. Otherwise, a confirmation prompt will appear	
o	-h|--help	Output usage information	
a	1	0
@	ext:update
o	-h|--help	Output usage information	
a	1	0
@	firestore:delete
o	-r|--recursive	Recursive. Delete all documents and subcollections at and under the specified level. May not be…	
o	--shallow	Shallow. Delete only documents at the specified level and ignore documents in subcollections. This…	
o	--all-collections	Delete all. Deletes the entire Firestore database, including all collections and documents. Any…	
o	-y|--yes	No confirmation. Otherwise, a confirmation prompt will appear	
o	-h|--help	Output usage information	
a	1	0
@	firestore:indexes
o	--pretty	Pretty print. When not specified the indexes are printed in the JSON specification format	
o	-h|--help	Output usage information	
@	functions:config:clone
o	--from	The project from which to clone configuration	v
o	--only	A comma-separated list of keys to clone	v
o	--except	A comma-separated list of keys to not clone	v
o	-h|--help	Output usage information	
@	functions:config:get
o	-h|--help	Output usage information	
a	1	0
@	functions:config:set
o	-h|--help	Output usage information	
a	1	1
@	functions:log
o	--only	Only show logs of specified, comma-separated functions (e.g. "funcA,funcB")	v
o	-n|--lines	Specify number of log lines to fetch	v
o	--open	Open logs page in web browser	
o	-h|--help	Output usage information	
@	functions:shell
o	-p|--port	The port on which to emulate functions	v
o	--inspect-functions	Emulate Cloud Functions in debug mode with the node inspector on the given port (9229 if not…	v
o	-h|--help	Output usage information	
@	help
o	-h|--help	Output usage information	
@	hosting:channel:create
o	-e|--expires	Duration string (e.g. 12h or 30d) for channel expiration, max 30d	v
o	--site	Site for which to create the channel	v
o	-h|--help	Output usage information	
a	1	0
@	hosting:channel:delete
o	--site	Site in which the channel exists	v
o	-f|--force	Delete without confirmation	
o	-h|--help	Output usage information	
a	1	0
@	hosting:channel:deploy
o	-e|--expires	Duration string (e.g. 12h, 30d) for channel expiration, max 30d; defaults to 7d	v
o	--only	Only create previews for specified targets	
o	--open	Open a browser to the channel after deploying	
o	--no-authorized-domains	Do not sync channel domains with Firebase Auth	
o	-h|--help	Output usage information	
a	1	0
@	hosting:channel:list
o	--site	List channels for the specified site	v
o	-h|--help	Output usage information	
@	hosting:channel:open
o	--site	The site to which the channel belongs	v
o	-h|--help	Output usage information	
a	1	0
@	hosting:clone
o	-h|--help	Output usage information	
a	2	0
@	hosting:disable
o	-y|--confirm	Skip confirmation	
o	-s|--site	The site to disable	v
o	-h|--help	Output usage information	
@	hosting:sites:create
o	--app	Specify an existing Firebase Web App ID	v
o	-h|--help	Output usage information	
a	1	0
@	hosting:sites:delete
o	-f|--force	Delete without confirmation	
o	-h|--help	Output usage information	
a	1	0
@	hosting:sites:get
o	-h|--help	Output usage information	
a	1	0
@	hosting:sites:list
o	-h|--help	Output usage information	
@	init
o	-h|--help	Output usage information	
@	login
o	--no-localhost	Copy and paste a code instead of starting a local server for authentication	
o	--reauth	Force reauthentication even if already logged in	
o	-h|--help	Output usage information	
@	login:add
o	--no-localhost	Copy and paste a code instead of starting a local server for authentication	
o	-h|--help	Output usage information	
a	1	0
@	login:ci
o	--no-localhost	Copy and paste a code instead of starting a local server for authentication	
o	-h|--help	Output usage information	
@	login:list
o	-h|--help	Output usage information	
@	login:use
o	-h|--help	Output usage information	
a	1	0
@	logout
o	-h|--help	Output usage information	
a	1	0
@	open
o	-h|--help	Output usage information	
a	1	0
@	projects:addfirebase
o	-h|--help	Output usage information	
a	1	0
@	projects:create
o	-n|--display-name	(optional) display name for the project	v
o	-o|--organization	(optional) ID of the parent Google Cloud Platform organization under which to create this project	v
o	-f|--folder	(optional) ID of the parent Google Cloud Platform folder in which to create this project	v
o	-h|--help	Output usage information	
a	1	0
@	projects:list
o	-h|--help	Output usage information	
@	remoteconfig:get
o	-v|--version-number	Grabs the specified version of the template	
o	-o|--output	Write config output to a filename (if omitted, will use the default file path)	v
o	-h|--help	Output usage information	
@	remoteconfig:rollback
o	-v|--version-number	Rollback to the specified version of the template	v
o	--force	Rollback template to the specified version without confirmation	
o	-h|--help	Output usage information	
@	remoteconfig:versions:list
o	--limit	Limit the number of versions being returned. Pass '0' to fetch all versions	v
o	-h|--help	Output usage information	
@	serve
o	-p|--port	The port on which to listen (default: 5000) (default: 5000)	v
o	-o|--host	The host on which to listen (default: localhost) (default: "localhost")	v
o	--only	Only serve specified targets (valid targets are: hosting, functions)	
o	--except	Serve all except specified targets (valid targets are: hosting, functions)	v
o	-h|--help	Output usage information	
@	setup:emulators:database
o	-h|--help	Output usage information	
@	setup:emulators:firestore
o	-h|--help	Output usage information	
@	setup:emulators:pubsub
o	-h|--help	Output usage information	
@	setup:emulators:ui
o	-h|--help	Output usage information	
@	target
o	-h|--help	Output usage information	
a	1	0
@	target:apply
o	-h|--help	Output usage information	
a	3	1
@	target:clear
o	-h|--help	Output usage information	
a	2	0
@	target:remove
o	-h|--help	Output usage information	
a	2	0
@	use
o	--add	Create a new project alias interactively	v
o	--alias	Create a new alias for the provided project id	v
o	--unalias	Remove an already created project alias	v
o	--clear	Clear the active project selection	
o	-h|--help	Output usage information	
a	1	0
#	use	1
d

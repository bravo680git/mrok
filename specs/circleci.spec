@	
s	completion	Generate shell completion scripts
s	config	Operate on build config files
s	context	Secure and share environment variables across projects
s	diagnostic	Check the status of your CircleCI CLI
s	follow	Attempt to follow the project for the current git repo
s	help	Help about any command
s	local	Debug jobs on the local machine
s	namespace	Operate on namespaces
s	open	Open the current project in the browser
s	orb	Operate on orbs
s	policy	Manage security policies
s	runner	Operate on runners
s	setup	Setup CLI with your credentials
s	update	Update and switch to new CLI version
s	version	Display CircleCI CLI version
o	--help|-h	Show help for CircleCI	p
o	--skip-update-check	Skip update check before every command	p
@	completion
s	bash	Generate bash completion scripts
s	zsh	Generate zsh completion scripts
@	completion bash
@	completion zsh
@	config
s	pack	Pack CircleCI config files into a single file
s	process	Validate and display extended config
s	validate	Checks that config is valid
@	config pack
@	config process
@	config validate
@	context
s	create	Create a new context
s	delete	Delete the named context
s	list	List all contexts
s	remove-secret	Remove environment variable from a context
s	show	Show a context
s	store-secret	Store environment variables
@	context create
a	3	0
#	context create	1
v	github	
v	bitbucket	
@	context delete
a	3	0
#	context delete	1
v	github	
v	bitbucket	
@	context list
a	2	0
#	context list	1
v	github	
v	bitbucket	
@	context remove-secret
a	4	0
#	context remove-secret	1
v	github	
v	bitbucket	
@	context show
a	3	0
#	context show	1
v	github	
v	bitbucket	
@	context store-secret
a	4	0
#	context store-secret	1
v	github	
v	bitbucket	
@	diagnostic
@	follow
@	help
@	local
s	execute	Run a job in a container on the local machine
@	local execute
@	namespace
s	create	Create a namespace
@	namespace create
@	open
@	orb
s	add-to-category	Add an orb to a category
s	create	Create an orb in a namespace
s	info	Show metadata of an orb
s	init	Initialize a new orb
s	list	List orbs
s	list-categories	List orb categories
s	pack	Pack an orb with local scripts
s	process	Validate an orb and print its form after all pre-registration processing is complete
s	publish	Publish an orb to the registry
s	remove-from-category	Remove an orb from a category
s	source	Show source code of an orb
s	unlist	Disable/enable an orb's listing in the registry
s	validate	Validate an orb.yml
@	orb add-to-category
a	2	0
@	orb create
o	--private	Specify that this orb is for private use within your org, unlisted from the public registry	
a	1	0
@	orb info
a	1	0
@	orb init
o	--private	Specify that this orb is for private use within your org, unlisted from the public registry	
a	1	0
@	orb list
o	--private	Specify that this orb is for private use within your org, unlisted from the public registry	
o	--sort	Specify the sorting	v
o	-u|--uncertified	Include uncertified orbs	
a	1	0
=	orb list	--sort
v	builds	
v	projects	
v	orgs	
@	orb list-categories
@	orb pack
a	1	0
@	orb process
a	1	0
@	orb publish
a	2	0
@	orb remove-from-category
a	2	0
@	orb source
a	1	0
@	orb unlist
a	2	0
#	orb unlist	2
v	true	
v	false	
@	orb validate
a	1	0
@	policy
s	decide	Make a decision
s	diff	Get diff between local and remote policy bundles
s	eval	Perform raw opa evaluation locally
s	fetch	Fetch policy bundle (or a single policy)
s	logs	Get policy decision logs / decision log (or policy bundle) by decision ID
s	push	Push policy bundle (or a single policy)
s	settings	Get/set policy decision settings (To read settings: run command without any settings flags)
@	policy decide
o	--input	Path to input file, i.e. ./.circleci/config.yml	v
o	--metafile	Path to decision metadata file	v
o	--owner-id	The id of the policy's owner	v
o	--strict	Return non-zero status code for decision resulting in HARD_FAIL	
o	--context	Policy context for decision, default is 'config'	v
a	1	0
@	policy diff
o	--context	Policy context for decision, default is 'config'	v
o	--owner-id	The id of the policy's owner	v
a	1	0
@	policy eval
o	--input	Path to input file, i.e. ./.circleci/config.yml	v
o	--metafile	Path to decision metadata file	v
o	--query	Policy decision query, default is 'data'	v
a	1	0
@	policy fetch
o	--context	Policy context for decision, default is 'config'	v
o	--owner-id	The id of the policy's owner	
a	1	0
@	policy logs
o	--after	Filter decision logs triggered AFTER this datetime	v
o	--before	Filter decision logs triggered BEFORE this datetime	v
o	--branch	Filter decision logs based on branch name	v
o	--context	Policy context for decision, default is 'config'	v
o	--owner-id	The id of the policy's owner	v
o	--out	Specify output file name	v
o	--policy-bundle	Get only the policy bundle for given decisionID	
o	--project-id	Filter decision logs based on project-id	v
o	--status	Filter decision logs based on their status	v
a	1	0
@	policy push
o	--context	Policy context for decision, default is 'config'	v
o	--owner-id	The id of the policy's owner	v
o	--no-prompt	Removes the prompt	
a	1	0
@	policy settings
o	--context	Policy context for decision, default is 'config'	
o	--enabled	Enable/disable policy decision evaluation in build pipeline	V=
o	--owner-id	The id of the policy's owner	v
=	policy settings	--enabled
v	true	
v	false	
@	runner
s	instance	Operate on runner instances
s	resource-class	Operate on runner resource-classes
s	token	Operate on runner tokens
@	runner instance
@	runner resource-class
@	runner token
@	setup
@	update
s	check	Check for new CLI version
s	install	Install new CLI version
@	update check
@	update install
@	version

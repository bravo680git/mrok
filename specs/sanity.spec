@	
s	help	Displays help information about Sanity
s	build	Builds the current Sanity configuration to a static bundle
s	codemod	Runs a code modification script
s	configcheck	Checks if the required configuration files for plugins exists and are up to date
s	cors	Interact with CORS-entries for your project
s	dataset	Interact with datasets in your project
s	debug	Gathers information on Sanity environment
s	deploy	Deploys a statically built Sanity studio
s	docs	Opens the Sanity documentation
s	documents	Interact with documents in your project
s	exec	Runs a script in Sanity context
s	graphql	Interact with GraphQL APIs
s	hook	Interact with hooks in your project
s	init	Initialize a new Sanity project or plugin
s	install	Installs a Sanity plugin to the current Sanity configuration
s	login	Authenticates against the Sanity.io API (no flag) or a third-party identity provider (with --sso…
s	logout	Logs out of the Sanity.io session
s	manage	Opens the Sanity project management UI
s	projects	Interact with projects connected to your logged in user
s	start	Starts a web server for the Content Studio
s	undeploy	Removes the deployed studio from <hostname>.sanity.studio
s	uninstall	Removes a Sanity plugin from the current Sanity configuration
s	upgrade	Upgrades all (or some) Sanity modules to their latest versions
s	users	Manage users of your project
s	versions	Shows the installed versions of Sanity CLI and core components
o	--help|-h	Show help for sanity	
@	help
a	1	0
#	help	1
t	help
@	build
o	--source-maps	Enable source maps for built bundles (increases size of bundle)	
o	--no-minify	Skip minifying built JavaScript (speeds up build, increases size of bundle)	
o	-y|--yes	Use unattended mode, accepting defaults and using only flags for choices	
@	codemod
o	--dry	Dry run (no changes are made to files)	
o	--extensions	Transform files with these file extensions (comma separated list) (default: js,ts,tsx)	v
o	--no-verify	Skip verification before running codemod	
@	configcheck
@	cors
s	add	Allow a new origin to use your project API through CORS
s	delete	Delete an existing CORS-origin from your project
s	list	List all origins allowed to access the API for this project
@	cors add
o	--credentials	Allow credentials (token/cookie) to be sent from this origin	
o	--no-credentials	Disallow credentials (token/cookie) to be sent from this origin	
a	1	0
@	cors delete
a	1	0
@	cors list
@	dataset
s	alias	You can manage your dataset alias using this command
s	copy	Manages dataset copying, including starting a new copy job, listing copy jobs and following the…
s	create	Create a new dataset within your project
s	delete	Delete a dataset within your project
s	export	Export dataset to local filesystem as a gzipped tarball
s	import	Import documents to given dataset from ndjson file
s	list	List datasets of your project
s	visibility	Set visibility of a dataset
@	dataset alias
s	create	
s	delete	
s	link	
s	unlink	
@	dataset alias create
a	2	0
@	dataset alias delete
a	1	0
@	dataset alias link
o	--force	Skips security prompt and forces link command	
a	2	0
@	dataset alias unlink
a	1	0
@	dataset copy
o	--detach	Start the copy without waiting for it to finish	
o	--attach	Attach to the running copy process to show progress	v
o	--skip-history	Don't preserve document history on copy	
o	--list	Lists all dataset copy jobs corresponding to a certain criteria	
o	--offset	Start position in the list of jobs. Default 0. With --list	v
o	--limit	Maximum number of jobs returned. Default 10. Maximum 1000. With --list	v
a	2	0
@	dataset create
o	--visibility	Set visibility for this dataset (public/private)	v
a	1	0
=	dataset create	--visibility
v	public	
v	private	
@	dataset delete
a	1	0
@	dataset export
o	--raw	Extract only documents, without rewriting asset references	
o	--no-assets	Export only non-asset documents and remove references to image assets	
o	--no-drafts	Export only published versions of documents	
o	--no-compress	Skips compressing tarball entries (still generates a gzip file)	
o	--types	Defines which document types to export	v
o	--overwrite	Overwrite any file with the same name	
o	--asset-concurrency	Concurrent number of asset downloads	v
a	2	0
#	dataset export	2
t	folders
@	dataset import
o	--missing	On duplicate document IDs, skip importing document in question	
o	--replace	On duplicate document IDs, replace existing document with imported document	
o	--allow-failing-assets	Skip assets that cannot be fetched/uploaded	
o	--replace-assets	Skip reuse of existing assets	
a	2	0
#	dataset import	1
t	filepaths
@	dataset list
@	dataset visibility
a	2	0
#	dataset visibility	2
v	get	
v	set	
@	debug
o	--secrets	Include API keys in output	
@	deploy
o	--source-maps	Enable source maps for built bundles (increases size of bundle)	
o	--no-minify	Skip minifying built JavaScript (speeds up build, increases size of bundle)	
o	--no-build	Don't build the studio prior to deploy, instead deploying the version currently in `dist/`	
a	1	0
#	deploy	1
t	folders
@	docs
@	documents
s	create	Create one or more documents
s	delete	Delete a document by ID
s	get	Get and print a document by ID
s	query	Query for documents
@	documents create
o	--replace	On duplicate document IDs, replace existing document with specified document(s)	
o	--missing	On duplicate document IDs, don't modify the target document(s)	
o	--watch	Write the documents whenever the target file or buffer changes	
o	--json5	Use JSON5 file type to allow a "simplified" version of JSON	
o	--id	Specify a document ID to use. Will fetch remote document ID and populate editor	v
o	--dataset	NAME to override dataset	v
a	1	0
#	documents create	1
t	filepaths
@	documents delete
o	--dataset	NAME to override dataset	v
a	1	1
@	documents get
o	--pretty	Colorized JSON output	
o	--dataset	NAME to override dataset	v
a	1	0
@	documents query
o	--pretty	Colorized JSON output	
o	--dataset	NAME to override dataset	v
o	--api-version	API version to use (defaults to `v1`)	v
a	1	0
@	exec
o	--with-user-token	Preload access token from CLI config into 'part:@sanity/base/client' part	
o	--mock-browser-env	Mocks a browser-like environment using jsdom	
a	1	0
#	exec	1
t	filepaths
@	graphql
s	deploy	Deploy a GraphQL API from the current Sanity schema
s	list	Lists all the GraphQL endpoints deployed for this project
s	undeploy	Remove a deployed GraphQL API
@	graphql deploy
o	--dataset	Deploy API for the given dataset	v
o	--tag	Deploy API to given tag (defaults to 'default')	v
o	--generation	API generation to deploy (defaults to 'gen3')	v
o	--non-null-document-fields	Set document interface fields (_id, _type etc) as non-null	
o	--playground	Deploy a GraphQL playground for easily testing queries (public)	
o	--no-playground	Skip playground prompt (do not deploy a playground)	
o	--force	Deploy API without confirming breaking changes	
@	graphql list
@	graphql undeploy
o	--dataset	Delete GraphQL API for the given dataset	v
o	--tag	Delete GraphQL API for the given tag (defaults to 'default')	v
@	hook
s	attempt	Print details of a given webhook delivery attempt
s	create	Create a new hook for the given dataset
s	delete	Delete a hook within your project
s	list	List hooks for a given project
s	logs	List latest log entries for a given hook
@	hook attempt
a	1	0
@	hook create
@	hook delete
a	1	0
@	hook list
@	hook logs
a	1	0
@	init
o	-y|--yes	Use unattended mode, accepting defaults and using only flags for choices	
o	--project	Project ID to use for the studio	v
o	--organization	Organization ID to use for the project	v
o	--dataset	Dataset name for the studio	v
o	--dataset-default	Set up a project with a public dataset named "production"	
o	--output-path	Path to write studio project to	v
o	--template	Project template to use [default: "clean"]	v
o	--provider	Login provider to use	v
o	--visibility	Visibility mode for dataset (public/private)	v
o	--create-project	Create a new project with the given name	v
o	--project-plan	Optionally select a plan for a new project	v
o	--coupon	Optionally select a coupon for a new project (cannot be used with --project-plan)	v
o	--reconfigure	Reconfigure Sanity studio in current folder with new project/dataset	
=	init	--visibility
v	public	
v	private	
@	install
a	1	0
@	login
o	--sso	Authenticate against a third-party identity provider	v
@	logout
@	manage
@	projects
s	list	Lists projects connected to your user
@	projects list
o	--sort	Sort output by specified column	v
o	--order	Sort output ascending/descending	v
=	projects list	--order
v	asc	
v	desc	
@	start
o	--port	TCP port to start server on. [default: 3333]	v
o	--host	The local network interface at which to listen. [default: "127.0.0.1"]	v
@	undeploy
@	uninstall
a	1	0
@	upgrade
o	--range	Version range to upgrade to, eg '^2.2.7' or '2.1.x'	v
o	--tag	Tagged release to upgrade to, eg 'canary' or 'some-feature'	v
o	--save-exact	Pin the resolved version numbers in package.json (no ^ prefix)	
@	users
s	invite	Invite a new user to the project
s	list	List users of the project
@	users invite
o	--role	Role to invite the user as	v
a	1	0
@	users list
o	--no-invitations	Don't include pending invitations	
o	--no-robots	Don't include robots (token users)	
o	--sort	Sort users by specified column: id, name, role, date	v
o	--order	Sort output ascending/descending	v
=	users list	--sort
v	id	
v	name	
v	role	
v	date	
=	users list	--order
v	asc	
v	desc	
@	versions

@	
s	completion	Generate the autocompletion script for the specified shell
s	db	Manage local Postgres databases
s	functions	Manage Supabase Edge functions
s	gen	Run code generation tools
s	init	Initialize a local project
s	link	Link to a Supabase project
s	login	Authenticate using an access token
s	migration	Manage database migration scripts
s	orgs	Manage Supabase organizations
s	projects	Manage Supabase projects
s	secrets	Manage Supabase secrets
s	start	Start containers for Supabase local development
s	status	Show status of local Supabase containers
s	stop	Stop all local Supabase containers
s	help	Help about any command
o	--debug	Output debug logs to stderr	p
o	--help|-h	Display help	p
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	db
s	branch	Manage local database branches
s	diff	Diffs the local database for schema changes
s	dump	Dumps data or schemas from the remote database
s	lint	Checks local database for typing error
s	pull	Pull schema from the remote database
s	push	Push new migrations to the remote database
s	remote	Manage remote databases
s	reset	Resets the local database to current migrations
@	db branch
s	create	Create a branch
s	delete	Delete a branch
s	list	List branches
s	switch	Switch the active branch
@	db branch create
@	db branch delete
@	db branch list
@	db branch switch
@	db diff
o	--file|-f	Saves schema diff to a file	v
o	--schema|-s	List of schema to include	v
o	--use-migra	Use migra to generate schema diff	
=	db diff	--file
t	filepaths
@	db dump
o	--data-only	Dumps only data records	
o	--db-url	Dumps from the database specified by the connection string (must be percent-encoded)	v
o	--dry-run	Prints the pg_dump script that would be executed	
o	--file|-f	File path to save the dumped contents	v
o	-h|--help	Help for dump	
o	--keep-comments	Keeps commented lines from pg_dump output	
o	--linked	Dumps from the linked project. (default true)	
o	--local	Dumps from the local database	
o	--password|-p	Password to your remote Postgres database	v
o	--role-only	Dumps only cluster roles	
o	--schema|-s	Comma separated list of schema to include. (default all)	v
o	--use-copy	Uses copy statements in place of inserts	
=	db dump	--file
t	filepaths
@	db lint
o	--level	Error level to emit	v
o	--schema|-s	List of schema to include	v
@	db pull
@	db push
o	--dry-run	Print the migrations that would be applied, but don't actually apply them	
o	--password|-p	Password to your remote Postgres database	v
@	db remote
s	changes	Show changes on the remote database
s	commit	Commit remote changes as a new migration
o	--password|-p	Password to your remote Postgres database	vp
@	db remote changes
@	db remote commit
@	db reset
@	functions
s	delete	Delete a Function from Supabase
s	deploy	Deploy a Function to Supabase
s	new	Create a new Function locally
s	serve	Serve a Function locally
@	functions delete
o	--project-ref	Project ref of the Supabase project	v
@	functions deploy
o	--no-verify-jwt	Disable JWT verification for the Function	
o	--project-ref	Project ref of the Supabase project	v
@	functions new
@	functions serve
o	--env-file	Path to an env file to be populated to the Function environment	v
o	--no-verify-jwt	Disable JWT verification for the Function	
=	functions serve	--env-file
t	filepaths
@	gen
s	types	Generate types from Postgres schema
@	gen types
s	typescript	Generate types for TypeScript
@	gen types typescript
o	--db-url	Generate types from a database url	v
o	--local	Generate types from the local dev database	
@	init
@	link
o	--password|-p	Password to your remote Postgres database	v
o	--project-ref	Project ref of the Supabase project	v
@	login
@	migration
s	list	List local and remote migrations
s	new	Create an empty migration script
s	repair	Repair the migration history table
s	squash	Squash migrations to a single file
s	up	Apply pending migrations to local database
@	migration list
o	--password|-p	Password to your remote Postgres database	v
o	--local	Lists migrations applied to the local database	
o	--linked	Lists migrations applied to the linked project (default true)	
o	--db-url	Database URL to connect to	v
@	migration new
a	1	0
@	migration repair
o	--status	Version status to update	v
o	--password|-p	Password to your remote Postgres database	v
o	--local	Repairs the migration history of the local database	
o	--linked	Repairs the migration history of the linked project (default true)	
o	--db-url	Database URL to connect to	v
a	1	0
=	migration repair	--status
v	applied	
v	reverted	
@	migration squash
o	--password|-p	Password to your remote Postgres database	v
o	--local	Squashes the migration history of the local database	
o	--version	Squash up to the specified version	v
o	--linked	Squashes the migration history of the linked project (default true)	
o	--db-url	Database URL to connect to	v
@	migration up
@	orgs
s	list	List all organizations
@	orgs list
@	projects
s	create	Create a project on Supabase
s	list	List all Supabase projects
@	projects create
o	--db-password	Database password of the project	v
o	--interactive|-i	Enables interactive mode	
o	--org-id	Organization ID to create the project in	v
o	--plan	Select a plan that suits your needs	v
o	--region	Select a region close to you for the best performance	v
@	projects list
@	secrets
s	list	List all secrets on Supabase
s	set	Set a secret(s) on Supabase
s	unset	Unset a secret(s) on Supabase
@	secrets list
@	secrets set
o	--env-file	Read secrets from a .env file	v
=	secrets set	--env-file
t	filepaths
@	secrets unset
@	start
@	status
@	stop
@	help
s	completion	Generate the autocompletion script for the specified shell
s	db	Manage local Postgres databases
s	functions	Manage Supabase Edge functions
s	gen	Run code generation tools
s	init	Initialize a local project
s	link	Link to a Supabase project
s	login	Authenticate using an access token
s	migration	Manage database migration scripts
s	orgs	Manage Supabase organizations
s	projects	Manage Supabase projects
s	secrets	Manage Supabase secrets
s	start	Start containers for Supabase local development
s	status	Show status of local Supabase containers
s	stop	Stop all local Supabase containers
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help db
s	branch	Manage local database branches
s	diff	Diffs the local database for schema changes
s	lint	Checks local database for typing error
s	push	Push new migrations to the remote database
s	remote	Manage remote databases
s	reset	Resets the local database to current migrations
@	help db branch
s	create	Create a branch
s	delete	Delete a branch
s	list	List branches
s	switch	Switch the active branch
@	help db branch create
@	help db branch delete
@	help db branch list
@	help db branch switch
@	help db diff
@	help db lint
@	help db push
@	help db remote
s	changes	Show changes on the remote database
s	commit	Commit remote changes as a new migration
@	help db remote changes
@	help db remote commit
@	help db reset
@	help functions
s	delete	Delete a Function from Supabase
s	deploy	Deploy a Function to Supabase
s	new	Create a new Function locally
s	serve	Serve a Function locally
@	help functions delete
@	help functions deploy
@	help functions new
@	help functions serve
@	help gen
s	types	Generate types from Postgres schema
@	help gen types
s	typescript	Generate types for TypeScript
@	help gen types typescript
@	help init
@	help link
@	help login
@	help migration
s	list	List local and remote migrations
s	new	Create an empty migration script
@	help migration list
@	help migration new
@	help orgs
s	list	List all organizations
@	help orgs list
@	help projects
s	create	Create a project on Supabase
s	list	List all Supabase projects
@	help projects create
@	help projects list
@	help secrets
s	list	List all secrets on Supabase
s	set	Set a secret(s) on Supabase
s	unset	Unset a secret(s) on Supabase
@	help secrets list
@	help secrets set
@	help secrets unset
@	help start
@	help status
@	help stop

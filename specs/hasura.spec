@	
s	actions	Manage Hasura actions
s	completions	Generate auto completion code
s	console	Open the console to manage the database and try out APIs
s	init	Initialize a directory for Hasura GraphQL engine migrations
s	md|metadata	
s	migrate	Manage migrations on the database
s	plugin|plugins	Manage plugins for the CLI
s	scripts	Execute helper scripts to manage Hasura projects
s	sd|seed|seeds	Manage seed data
s	update-cli	Update the CLI to latest or a specific version
s	version	Print the CLI version
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=		--envfile
t	filepaths
=		--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=		--project
t	folders
@	actions
s	codegen	Generate code for actions
s	create	Create a Hasura action
s	use-codegen	Use the codegen to generate code for Hasura actions
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	actions	--certificate-authority
t	filepaths
=	actions	--envfile
t	filepaths
=	actions	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	actions	--project
t	folders
@	actions codegen
o	--derive-from	Derive action from a hasura operation	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	1
=	actions codegen	--certificate-authority
t	filepaths
=	actions codegen	--envfile
t	filepaths
=	actions codegen	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	actions codegen	--project
t	folders
@	actions create
o	--derive-from	Derive action from a Hasura operation	v
o	--kind	Kind to use in action	V
o	--webhook	Webhook to use in action	V
o	--with-codegen	Create action along with codegen	
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	actions create	--kind
v	synchronous	
v	asynchronous	
=	actions create	--certificate-authority
t	filepaths
=	actions create	--envfile
t	filepaths
=	actions create	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	actions create	--project
t	folders
@	actions use-codegen
o	--framework	Framework to be used by codegen	v
o	--output-dir	Directory to create the codegen files	v
o	--with-starter-kit	Clone starter kit for a framework	
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	actions use-codegen	--output-dir
t	folders
=	actions use-codegen	--certificate-authority
t	filepaths
=	actions use-codegen	--envfile
t	filepaths
=	actions use-codegen	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	actions use-codegen	--project
t	folders
@	completions
o	--file	File to which output has to be written	v
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	completions	--file
t	filepaths
=	completions	--envfile
t	filepaths
=	completions	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	completions	--project
t	folders
#	completions	1
v	bash	
v	zsh	
@	console
o	--address	Address to serve console and migration API from	V
o	--api-port	Port for serving migrate api	V
o	--browser	Open console in a specific browser	v
o	--console-port	Port for serving console	V
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--no-browser	Do not automatically open console in browser	
o	--static-dir	Directory where static assets mentioned in the console html template can be served from	v
o	--use-server-assets	When rendering console, use assets provided by HGE server	
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	console	--static-dir
t	folders
=	console	--certificate-authority
t	filepaths
=	console	--envfile
t	filepaths
=	console	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	console	--project
t	folders
@	init
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--install-manifest	Install manifest to be cloned	v
o	--version	Config version to be used	v
a	1	0
@	md
s	apply	Apply Hasura metadata on a database
s	clear	Clear Hasura GraphQL engine metadata on the database
s	diff	Show a highlighted diff of Hasura metadata
s	export	Export Hasura GraphQL engine metadata from the database
s	ic|inconsistency|inconsistencies	Manage inconsistent objects in Hasura metadata
s	reload	Reload Hasura GraphQL engine metadata on the database
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md	--certificate-authority
t	filepaths
=	md	--envfile
t	filepaths
=	md	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md	--project
t	folders
@	md apply
o	--dry-run	Show metadata generated from project directory without applying to server	
o	-o|--output	Specify an output format to show applied metadata	V
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md apply	-o
v	json	
v	yaml	
=	md apply	--certificate-authority
t	filepaths
=	md apply	--envfile
t	filepaths
=	md apply	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md apply	--project
t	folders
@	md clear
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md clear	--certificate-authority
t	filepaths
=	md clear	--envfile
t	filepaths
=	md clear	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md clear	--project
t	folders
@	md diff
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	2	0
=	md diff	--certificate-authority
t	filepaths
=	md diff	--envfile
t	filepaths
=	md diff	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md diff	--project
t	folders
#	md diff	1
t	filepaths
#	md diff	2
t	filepaths
@	md export
o	-o|--output	Specify an output format for exported metadata	v
@	md ic
s	drop	Drop inconsistent objects from the metadata
s	ls|list	List all inconsistent objects from the metadata
s	status	Check if the metadata is inconsistent or not
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md ic	--certificate-authority
t	filepaths
=	md ic	--envfile
t	filepaths
=	md ic	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md ic	--project
t	folders
@	md ic drop
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md ic drop	--certificate-authority
t	filepaths
=	md ic drop	--envfile
t	filepaths
=	md ic drop	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md ic drop	--project
t	folders
@	md ic ls
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md ic ls	--certificate-authority
t	filepaths
=	md ic ls	--envfile
t	filepaths
=	md ic ls	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md ic ls	--project
t	folders
@	md ic status
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md ic status	--certificate-authority
t	filepaths
=	md ic status	--envfile
t	filepaths
=	md ic status	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md ic status	--project
t	folders
@	md reload
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	md reload	--certificate-authority
t	filepaths
=	md reload	--envfile
t	filepaths
=	md reload	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	md reload	--project
t	folders
@	migrate
s	apply	Apply migrations on the database
s	create	Create files required for a migration
s	delete	Clear migrations from local project and server
s	squash	Squash multiple migrations into a single one
s	status	Display current status of migrations on a database
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	migrate	--certificate-authority
t	filepaths
=	migrate	--envfile
t	filepaths
=	migrate	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	migrate	--project
t	folders
@	migrate apply
o	--up	Apply all or N up migration steps	V
o	--down	Apply all or N up migration steps	V
o	goto	Apply migration chain up to to the version specified	v
o	--version	Only apply this particular migration	v
o	--skip-execution	Skip executing the migration action, but mark them as applied	
o	--type	Type of migration to be used with version flag	v
o	--dry-run	Print the names of migrations which are going to be applied	
o	--all-databases	Set this flag to attempt to apply migrations on all databases present on server	
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	migrate apply	--type
v	up	
v	down	
=	migrate apply	--certificate-authority
t	filepaths
=	migrate apply	--envfile
t	filepaths
=	migrate apply	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	migrate apply	--project
t	folders
@	migrate create
o	--down-sql	Sql string/query that is to be used to create a down migration	v
o	--from-server	Take pg_dump of schema and Hasura metadata from the server	
o	--metadata-from-file	Path to a hasura metadata file to be used for up actions	v
o	--metadata-from-server	Take metadata from the server and write it as an up migration file	
o	--schema	Name of Postgres schema to export as a migration	v
o	--sql-from-file	Path to an SQL file which contains the SQL statements	v
o	--sql-from-server	Take pg_dump from the server and save it as a migration	
o	--up-sql	Sql string/query that is to be used to create an up migration	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	migrate create	--metadata-from-file
t	filepaths
=	migrate create	--sql-from-file
t	filepaths
=	migrate create	--certificate-authority
t	filepaths
=	migrate create	--envfile
t	filepaths
=	migrate create	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	migrate create	--project
t	folders
@	migrate delete
o	--all	Clears all migrations for selected database	
o	--force	Executes operation without any confirmation	
o	--version	Deletes the specified version in migrations	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	migrate delete	--certificate-authority
t	filepaths
=	migrate delete	--envfile
t	filepaths
=	migrate delete	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	migrate delete	--project
t	folders
@	migrate squash
o	--delete-source	Delete the source files after squashing without any confirmation	
o	--from	Start squashing from this version	v
o	--name	Name for the new squashed migration	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	migrate squash	--certificate-authority
t	filepaths
=	migrate squash	--envfile
t	filepaths
=	migrate squash	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	migrate squash	--project
t	folders
@	migrate status
@	plugin
s	install	Install a plugin from the index
s	list	List all available plugins from index, versions and installation status
s	uninstall	Uninstall a plugin
s	upgrade	Upgrade a plugin to a newer version
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	plugin	--envfile
t	filepaths
=	plugin	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	plugin	--project
t	folders
@	plugin install
o	--version	Version to be installed	v
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	plugin install	--envfile
t	filepaths
=	plugin install	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	plugin install	--project
t	folders
@	plugin list
o	--dont-update-index	Do not update the plugin index local cache, only show the list	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	plugin list	--envfile
t	filepaths
=	plugin list	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	plugin list	--project
t	folders
@	plugin uninstall
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	plugin uninstall	--envfile
t	filepaths
=	plugin uninstall	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	plugin uninstall	--project
t	folders
@	plugin upgrade
o	--version	Version to be upgraded	v
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	plugin upgrade	--envfile
t	filepaths
=	plugin upgrade	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	plugin upgrade	--project
t	folders
@	scripts
s	update-project-v2	Update the Hasura project from config v1 to v2
s	update-project-v3	Update the Hasura project from config v2 to v3
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	scripts	--envfile
t	filepaths
=	scripts	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	scripts	--project
t	folders
@	scripts update-project-v2
o	--metadata-dir	Metadata directory	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	scripts update-project-v2	--metadata-dir
t	folders
=	scripts update-project-v2	--certificate-authority
t	filepaths
=	scripts update-project-v2	--envfile
t	filepaths
=	scripts update-project-v2	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	scripts update-project-v2	--project
t	folders
@	scripts update-project-v3
o	--database-name	Database name for which the current migrations / seeds belong to	v
o	--force	Do not ask for confirmation	
o	--move-state-only	Do only a state migration from old hdb_catalog	
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	scripts update-project-v3	--certificate-authority
t	filepaths
=	scripts update-project-v3	--envfile
t	filepaths
=	scripts update-project-v3	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	scripts update-project-v3	--project
t	folders
@	sd
s	apply	Apply seed data
s	create	Create a new seed file
o	--database-name	Database name for which the current migrations / seeds belong to	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	sd	--certificate-authority
t	filepaths
=	sd	--envfile
t	filepaths
=	sd	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	sd	--project
t	folders
@	sd apply
o	-f|--file	Seed file to apply	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	sd apply	-f
t	filepaths
=	sd apply	--certificate-authority
t	filepaths
=	sd apply	--envfile
t	filepaths
=	sd apply	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	sd apply	--project
t	folders
@	sd create
o	--from-table	Name of table from which seed file has to be initialized	v
o	--admin-secret	Admin secret for Hasura GraphQL engine	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--endpoint	Http(s) endpoint for Hasura GraphQL engine (env `HASURA_GRAPHQL_ENDPOINT`)	v
o	--insecure-skip-tls-verify	Skip TLS verification and disable cert checking	
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
a	1	0
=	sd create	--certificate-authority
t	filepaths
=	sd create	--envfile
t	filepaths
=	sd create	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	sd create	--project
t	folders
@	update-cli
o	--version	A specific version to install	V
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	update-cli	--envfile
t	filepaths
=	update-cli	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	update-cli	--project
t	folders
@	version
o	--envfile	.env filename to load ENV vars from	v
o	-h|--help	Help for hasura	
o	--log-level	Log level	v
o	--no-color	Do not colorize output	
o	--project	Directory where commands are executed	v
o	--skip-update-check	Skip automatic update check on command execution	
=	version	--envfile
t	filepaths
=	version	--log-level
v	DEBUG	
v	INFO	
v	WARN	
v	ERROR	
v	FATAL	
=	version	--project
t	folders

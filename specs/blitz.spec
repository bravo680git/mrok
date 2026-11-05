@	
s	build|b	Creates a production build
s	codegen|cg	Generates Routes Manifest
s	console|c	Run the Blitz console REPL
s	db	Run database commands
s	dev|d	Start a development server
s	export|e	Exports a static page
s	generate|g	Generate new files for your Blitz project
s	help|h	Display help for <%= config.bin %>
s	install|i	Install a Recipe into your Blitz app
s	new	Create a new Blitz project
s	prisma|p	Loads env variables then proxies all args to Prisma CLI
s	routes|r	Display all Blitz URL Routes
s	start|s	Start the production server
s	autocomplete	Display autocomplete installation instructions
@	build
o	--help|-h	Show help for command	
@	codegen
o	--help|-h	Show help for command	
@	console
o	--help|-h	Show help for command	
@	db
o	--help|-h	Show help for command	
a	1	0
#	db	1
v	seed	Generates seeded data in database via Prisma 2. You need db/seeds.ts or db/seeds/index.ts
@	dev
o	--help|-h	Show help for command	
o	-p|--port	Set port number	v
o	-H|--hostname	Set server hostname	v
o	--inspect	Enable the Node.js inspector	
o	--no-incremental-build	Disable incremental build and start from a fresh cache	
@	export
o	--help|-h	Show help for command	
o	-o|--outdir	Set the output dir (defaults to 'out')	v
@	generate
o	--help|-h	Show help for command	
o	-c|--context	Provide a context folder within which we'll place the generated files for better code…	v
o	-p|--parent	Specify a parent model to be used for generating nested routes for dependent data when generating…	v
o	-d|--dry-run	Show what files will be created without writing them to disk	
a	2	0
#	generate	1
v	all	
v	crud	
v	model	
v	pages	
v	queries	
v	query	
v	mutations	
v	mutation	
v	resource	
@	help
o	--all	See all commands in CLI	
a	1	0
@	install
o	--help|-h	Show help for command	
a	2	0
@	new
o	--help|-h	Show help for command	
o	--npm	Use npm as the package manager	
o	--yarn	Use yarn as the package manager	
o	--form	A form library	v
o	-d|--dry-run	Show what files will be created without writing them to disk	
o	--no-git	Skip git repository creation	
o	--skip-upgrade	Skip blitz upgrade if outdated	
a	1	0
=	new	--form
v	react-final-form	
v	react-hook-form	
v	formik	
@	prisma
s	init	Setup Prisma for your app
s	generate	Generate artifacts (e.g. Prisma Client)
s	studio	Open Prisma Studio
s	format	Format your schema
s	migrate	Migrate your database
s	db	Manage your database schema and lifecycle (Preview)
s	version|-v	Print current version of Prisma components
@	prisma init
o	-h|--help	Display this help message	
o	--datasource-provider	Define the datasource provider to use	v
o	--url	Define a custom datasource url	v
=	prisma init	--datasource-provider
v	PostgreSQL	
v	MySQL	
v	SQLite	
v	SQLServer	
v	MongoDB	
v	CockroachDB	
=	prisma init	--url
t	filepaths
@	prisma generate
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--data-proxy	Enable the Data Proxy in the Prisma Client	
o	--no-hints	Hides the hint messages but still outputs errors and warnings	
o	--no-engine	Generate a client for use with Accelerate only	
o	--watch	Watch the Prisma schema and rerun after a change	
o	--allow-no-models	Allow generating a client without models	
=	prisma generate	--schema
t	filepaths
@	prisma studio
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	-p|--port	Port to start Studio on	v
o	-b|--browser	Browser to open Studio in	v
o	-n|--hostname	Hostname to bind the Express server to	v
=	prisma studio	--schema
t	filepaths
=	prisma studio	-b
v	firefox	
v	chrome	
v	safari	
v	none	
@	prisma format
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	prisma format	--schema
t	filepaths
@	prisma migrate
s	dev	The migrate dev command updates your database using migrations files during development
s	reset	Reset your database and apply all migrations, all data will be lost
s	deploy	Apply pending migrations to update the database schema in production/staging
s	resolve	Resolve issues with database migrations in deployment databases
s	status	Check the status of your database migrations
s	diff	Compares the database schema from two arbitrary sources, and outputs the differences either as a…
@	prisma migrate dev
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--skip-seed	Skip triggering seed	
o	--skip-generate	Skip triggering generators (e.g. Prisma Client)	
o	--create-only	Create a new migration but do not apply it. The migration will be empty if there are no changes in…	
o	-n|--name	The name of the migration. If no name is provided, the CLI will prompt you	V
=	prisma migrate dev	--schema
t	filepaths
@	prisma migrate reset
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--skip-seed	Skip triggering seed	
o	--skip-generate	Skip triggering generators (e.g. Prisma Client)	
o	-f|--force	Skip the confirmation prompt	
=	prisma migrate reset	--schema
t	filepaths
@	prisma migrate deploy
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	prisma migrate deploy	--schema
t	filepaths
@	prisma migrate resolve
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--applied	Record a specific migration as applied	v
o	--rolled-back	Record a specific migration as rolled back	v
=	prisma migrate resolve	--schema
t	filepaths
=	prisma migrate resolve	--applied
t	filepaths
=	prisma migrate resolve	--rolled-back
t	filepaths
@	prisma migrate status
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	prisma migrate status	--schema
t	filepaths
@	prisma migrate diff
o	-h|--help	Display this help message	
o	--from-url	A datasource url	v
o	--to-url	A datasource url	v
o	--from-empty	Flag to assume from is an empty datamodel	
o	--to-empty	Flag to assume to is an empty datamodel	
o	--from-schema-datamodel	Path to a Prisma schema file, uses the 'datamodel' for the diff	v
o	--to-schema-datamodel	Path to a Prisma schema file, uses the 'datamodel' for the diff	v
o	--from-schema-datasource	Path to a Prisma schema file, uses the 'datasource url' for the diff	v
o	--to-schema-datasource	Path to a Prisma schema file, uses the 'datasource url' for the diff	v
o	--from-migrations	Path to the Prisma Migrate migrations directory	v
o	--to-migrations	Path to the Prisma Migrate migrations directory	v
o	--shadow-database-url	URL for the shadow database. Only required if using --from-migrations or --to-migrations	v
o	--script	Render a SQL script to stdout instead of the default human readable summary (not supported on…	v
o	--exit-code	Change the exit code behavior to signal if the diff is empty or not (Empty: 0, Error: 1, Not…	
=	prisma migrate diff	--from-url
t	filepaths
=	prisma migrate diff	--to-url
t	filepaths
=	prisma migrate diff	--from-schema-datamodel
t	filepaths
=	prisma migrate diff	--to-schema-datamodel
t	filepaths
=	prisma migrate diff	--from-schema-datasource
t	filepaths
=	prisma migrate diff	--to-schema-datasource
t	filepaths
=	prisma migrate diff	--from-migrations
t	folders
=	prisma migrate diff	--to-migrations
t	folders
=	prisma migrate diff	--shadow-database-url
t	filepaths
=	prisma migrate diff	--script
t	filepaths
@	prisma db
s	pull	
s	push	This command pushes the state of your Prisma schema file to the database without using migrations…
s	seed	Seed your database
s	execute	Execute native commands to your database
@	prisma db pull
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--force	Ignore current Prisma schema file	
o	--print	Print the introspected Prisma schema to stdout	
o	--url	The datasource url	v
o	--composite-type-depth	Specify the depth for introspecting composite types (e.g. Embedded Documents in MongoDB). Number…	v
=	prisma db pull	--schema
t	filepaths
=	prisma db pull	--url
t	filepaths
@	prisma db push
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--skip-generate	Skip generation of artifacts such as Prisma Client	
o	--force-reset	Resets the database and then updates the schema - useful if you need to start from scratch due to…	
o	--accept-data-loss	Ignore data loss warnings. This option is required if as a result of making the schema changes…	
=	prisma db push	--schema
t	filepaths
@	prisma db seed
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	prisma db seed	--schema
t	filepaths
@	prisma db execute
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--url	The datasource url	v
o	--file	Path to a file. The content will be sent as the script to be executed	v
o	--stdin	Use the terminal standard input as the script to be executed	
=	prisma db execute	--schema
t	filepaths
=	prisma db execute	--url
t	filepaths
=	prisma db execute	--file
t	filepaths
@	prisma version
s	--json	Output JSON
@	prisma version --json
@	routes
o	--help|-h	Show help for command	
@	start
o	--help|-h	Show help for command	
o	-p|--port	Set port number	v
o	-H|--hostname	Set server hostname	v
o	--inspect	Enable the Node.js inspector	
@	autocomplete
o	-r|--refresh-cache	Refresh cache (ignores displaying instructions)	
a	1	0
#	autocomplete	1
v	zsh	
v	bash	

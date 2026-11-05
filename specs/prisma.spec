@	
s	init	Setup Prisma for your app
s	generate	Generate artifacts (e.g. Prisma Client)
s	studio	Open Prisma Studio
s	format	Format your schema
s	migrate	Migrate your database
s	db	Manage your database schema and lifecycle (Preview)
s	version|-v	Print current version of Prisma components
@	init
o	-h|--help	Display this help message	
o	--datasource-provider	Define the datasource provider to use	v
o	--url	Define a custom datasource url	v
=	init	--datasource-provider
v	PostgreSQL	
v	MySQL	
v	SQLite	
v	SQLServer	
v	MongoDB	
v	CockroachDB	
=	init	--url
t	filepaths
@	generate
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--data-proxy	Enable the Data Proxy in the Prisma Client	
o	--no-hints	Hides the hint messages but still outputs errors and warnings	
o	--no-engine	Generate a client for use with Accelerate only	
o	--watch	Watch the Prisma schema and rerun after a change	
o	--allow-no-models	Allow generating a client without models	
=	generate	--schema
t	filepaths
@	studio
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	-p|--port	Port to start Studio on	v
o	-b|--browser	Browser to open Studio in	v
o	-n|--hostname	Hostname to bind the Express server to	v
=	studio	--schema
t	filepaths
=	studio	-b
v	firefox	
v	chrome	
v	safari	
v	none	
@	format
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	format	--schema
t	filepaths
@	migrate
s	dev	The migrate dev command updates your database using migrations files during development
s	reset	Reset your database and apply all migrations, all data will be lost
s	deploy	Apply pending migrations to update the database schema in production/staging
s	resolve	Resolve issues with database migrations in deployment databases
s	status	Check the status of your database migrations
s	diff	Compares the database schema from two arbitrary sources, and outputs the differences either as a…
@	migrate dev
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--skip-seed	Skip triggering seed	
o	--skip-generate	Skip triggering generators (e.g. Prisma Client)	
o	--create-only	Create a new migration but do not apply it. The migration will be empty if there are no changes in…	
o	-n|--name	The name of the migration. If no name is provided, the CLI will prompt you	V
=	migrate dev	--schema
t	filepaths
@	migrate reset
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--skip-seed	Skip triggering seed	
o	--skip-generate	Skip triggering generators (e.g. Prisma Client)	
o	-f|--force	Skip the confirmation prompt	
=	migrate reset	--schema
t	filepaths
@	migrate deploy
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	migrate deploy	--schema
t	filepaths
@	migrate resolve
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--applied	Record a specific migration as applied	v
o	--rolled-back	Record a specific migration as rolled back	v
=	migrate resolve	--schema
t	filepaths
=	migrate resolve	--applied
t	filepaths
=	migrate resolve	--rolled-back
t	filepaths
@	migrate status
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	migrate status	--schema
t	filepaths
@	migrate diff
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
=	migrate diff	--from-url
t	filepaths
=	migrate diff	--to-url
t	filepaths
=	migrate diff	--from-schema-datamodel
t	filepaths
=	migrate diff	--to-schema-datamodel
t	filepaths
=	migrate diff	--from-schema-datasource
t	filepaths
=	migrate diff	--to-schema-datasource
t	filepaths
=	migrate diff	--from-migrations
t	folders
=	migrate diff	--to-migrations
t	folders
=	migrate diff	--shadow-database-url
t	filepaths
=	migrate diff	--script
t	filepaths
@	db
s	pull	
s	push	This command pushes the state of your Prisma schema file to the database without using migrations…
s	seed	Seed your database
s	execute	Execute native commands to your database
@	db pull
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--force	Ignore current Prisma schema file	
o	--print	Print the introspected Prisma schema to stdout	
o	--url	The datasource url	v
o	--composite-type-depth	Specify the depth for introspecting composite types (e.g. Embedded Documents in MongoDB). Number…	v
=	db pull	--schema
t	filepaths
=	db pull	--url
t	filepaths
@	db push
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--skip-generate	Skip generation of artifacts such as Prisma Client	
o	--force-reset	Resets the database and then updates the schema - useful if you need to start from scratch due to…	
o	--accept-data-loss	Ignore data loss warnings. This option is required if as a result of making the schema changes…	
=	db push	--schema
t	filepaths
@	db seed
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
=	db seed	--schema
t	filepaths
@	db execute
o	-h|--help	Display this help message	
o	--schema	Custom path to your Prisma schema	v
o	--url	The datasource url	v
o	--file	Path to a file. The content will be sent as the script to be executed	v
o	--stdin	Use the terminal standard input as the script to be executed	
=	db execute	--schema
t	filepaths
=	db execute	--url
t	filepaths
=	db execute	--file
t	filepaths
@	version
s	--json	Output JSON
@	version --json

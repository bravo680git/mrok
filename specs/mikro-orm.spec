@	
s	cache:clear	Clear metadata cache
s	cache:generate	Generate metadata cache for production
s	generate-entities	Generate entities based on current database schema
s	database:create	Create your database if it does not exist
s	database:import	Imports the SQL file to the database
s	seeder:run	Seed the database using the seeder class
s	seeder:create	Create a new seeder class
s	schema:create	Create database schema based on current metadata
s	schema:drop	Drop database schema based on current metadata
s	schema:update	Update database schema based on current metadata
s	schema:fresh	Drop and recreate database schema based on current metadata
s	migration:create	Create new migration with current schema diff
s	migration:up	Migrate up to the latest version
s	migration:down	Migrate one step down
s	migration:list	List all executed migrations
s	migration:pending	List all pending migrations
s	migration:fresh	Clear the database and rerun all migrations
s	debug	Debug CLI configuration
o	-v|--version	Show version number	
o	-h|--help	Show help	
@	cache:clear
@	cache:generate
@	generate-entities
o	-s|--save	Saves entities to directory defined by --path	
o	-d|--dump	Dumps all entities to console	
o	-p|--path	Sets path to directory where to save entities	v
o	--schema	Generates entities only for given schema	v
=	generate-entities	-p
t	folders
@	database:create
@	database:import
a	1	0
#	database:import	1
t	filepaths
@	seeder:run
@	seeder:create
o	--class	Seeder class to run	
@	schema:create
o	-r|--run	Runs queries	
o	-d|--dump	Dumps all queries to console	
o	--fk-checks	Do not skip foreign key checks	
o	--schema	Set the current schema for wildcard schema entities	v
o	--seed	Allows to seed the database on create or drop and recreate	v
@	schema:drop
o	-r|--run	Runs queries	
o	-d|--dump	Dumps all queries to console	
o	--fk-checks	Do not skip foreign key checks	
o	--schema	Set the current schema for wildcard schema entities	v
o	--drop-migrations-table	Drop also migrations table	
o	--drop-db	Drop the whole database	
@	schema:update
o	-r|--run	Runs queries	
o	-d|--dump	Dumps all queries to console	
o	--fk-checks	Do not skip foreign key checks	
o	--schema	Set the current schema for wildcard schema entities	v
o	--safe	Allows to disable table and column dropping	
o	--drop-tables	Allows to disable table dropping	
@	schema:fresh
o	-r|--run	Runs queries	
o	--schema	Set the current schema for wildcard schema entities	v
o	--seed	Allows to seed the database on create or drop and recreate	v
@	migration:create
o	-b|--blank	Create blank migration	
o	-i|--initial	Create initial migration	
o	-d|--dump	Dumps all queries to console	
o	-p|--path	Sets path to directory where to save entities	v
=	migration:create	-p
t	folders
@	migration:up
o	-t|--to	Migrate up to specific version	
o	-f|--from	Start migration from specific version	
o	-o|--only	Migrate only specified versions	
@	migration:down
o	-t|--to	Migrate down to specific version	
o	-f|--from	Start migration from specific version	
o	-o|--only	Migrate only specified versions	
@	migration:list
@	migration:pending
@	migration:fresh
o	--seed	Allows to seed the database on create or drop and recreate	v
@	debug

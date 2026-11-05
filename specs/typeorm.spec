@	
s	schema:sync	Synchronizes your entities with database schema
s	schema:log	Shows sql to be executed by schema:sync command
s	schema:drop	Drops all tables in the database on your default connection
s	query	Executes given SQL query on a default connection
s	entity:create	Generates a new entity
s	subscriber:create	Generates a new subscriber
s	migration:create	Creates a new migration file
s	migration:generate	Generates a new migration file with sql needs to be executed to update schema
s	migration:run	Runs all pending migrations
s	migration:show	Show all migrations and whether they have been run or not
s	migration:revert	Reverts last executed migration
s	version	Prints TypeORM version this project uses
s	cache:clear	Clears all data stored in query runner cache
s	init	Generates initial TypeORM project structure
o	--help	Show help for command	
o	-v|--version	Show the version	
@	schema:sync
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which schema synchronization needs to to run	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	schema:sync	-f
t	filepaths
@	schema:log
o	--help	Show help for command	
o	-c|--connection	Name of the connection of which schema sync log should be shown	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	schema:log	-f
t	filepaths
@	schema:drop
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to drop all tables	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	schema:drop	-f
t	filepaths
@	query
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
a	1	0
=	query	-f
t	filepaths
@	entity:create
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-n|--name	Name of the entity class	v
o	-d|--dir	Directory where entity should be created	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	entity:create	-d
t	folders
=	entity:create	-f
t	filepaths
@	subscriber:create
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-n|--name	Name of the subscriber class	v
o	-d|--dir	Directory where subscriber should be created	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	subscriber:create	-d
t	folders
=	subscriber:create	-f
t	filepaths
@	migration:create
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-n|--name	Name of the migration class	v
o	-d|--dir	Directory where migration should be created	v
o	-f|--config	Name of the file with connection configuration	v
o	-o|--outputJs	Generate a migration file on Javascript instead of Typescript	
o	-v|--version	Show the version	
=	migration:create	-d
t	folders
=	migration:create	-f
t	filepaths
@	migration:generate
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-n|--name	Name of the migration class	v
o	-d|--dir	Directory where migration should be created	v
o	-p|--pretty	Pretty-print generated SQL	
o	-f|--config	Name of the file with connection configuration	v
o	-o|--outputJs	Generate a migration file on Javascript instead of Typescript	
o	--dr|--dryrun	Prints out the contents of the migration instead of writing it to a file	
o	--ch|--check	Verifies that the current database is up to date and that no migrations are needed	
o	-v|--version	Show the version	
=	migration:generate	-d
t	folders
=	migration:generate	-f
t	filepaths
@	migration:run
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-t|--transaction	Indicates if transaction should be used or not for migration run	
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	migration:run	-f
t	filepaths
@	migration:show
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	migration:show	-f
t	filepaths
@	migration:revert
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-t|--transaction	Indicates if transaction should be used or not for migration revert	
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	migration:revert	-f
t	filepaths
@	version
o	--help	Show help for command	
o	-v|--version	Show the version	
@	cache:clear
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-f|--config	Name of the file with connection configuration	v
o	-v|--version	Show the version	
=	cache:clear	-f
t	filepaths
@	init
o	--help	Show help for command	
o	-c|--connection	Name of the connection on which to run a query	v
o	-n|--name	Name of the project directory	v
o	--db|--database	Database type you'll use in your project	v
o	--express	Indicates if express should be included in the project	
o	--docker	Set to true if docker-compose must be generated as well	
o	--pm|--manager	Install packages	v
o	-v|--version	Show the version	
=	init	--db
v	mysql	
v	mariadb	
v	postgres	
v	cockroachdb	
v	sqlite	
v	mssql	
v	oracle	
v	cordova	
v	nativescript	
v	react-native	
v	expo	
v	mongodb	
=	init	--pm
v	npm	
v	yarn	

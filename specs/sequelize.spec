@	
s	db:migrate	Run pending migrations
s	db:migrate:schema:timestamps:add	Update migration table to have timestamps
s	db:migrate:status	List the status of all migrations
s	db:migrate:undo	Reverts a migration
s	db:migrate:undo:all	Revert all migrations ran
s	db:seed	Run specified seeder
s	db:seed:undo	Deletes data from the database
s	db:seed:all	Run every seeder
s	db:seed:undo:all	Deletes data from the database
s	db:create	Create database specified by configuration
s	db:drop	Drop database specified by configuration
s	init	Initializes project
s	init:config	Initializes configuration
s	init:migrations	Initializes migrations
s	init:models	Initializes models
s	init:seeders	Initializes seeders
s	migration:generate|migration:create	Generates a new migration file
s	model:generate|model:create	Generates a model and its migration
s	seed:generate|seed:create	Generates a new seed file
o	--help	Show help	
o	--version	Show version number	
@	db:migrate
o	--to	Migration name to run migrations until	v
o	--from	Migration name to start migrations from (excluding)	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:migrate	--config
t	filepaths
=	db:migrate	--options-path
t	filepaths
=	db:migrate	--migrations-path
t	folders
=	db:migrate	--seeders-path
t	folders
=	db:migrate	--models-path
t	folders
@	db:migrate:schema:timestamps:add
o	--to	Migration name to run migrations until	v
o	--from	Migration name to start migrations from (excluding)	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:migrate:schema:timestamps:add	--config
t	filepaths
=	db:migrate:schema:timestamps:add	--options-path
t	filepaths
=	db:migrate:schema:timestamps:add	--migrations-path
t	folders
=	db:migrate:schema:timestamps:add	--seeders-path
t	folders
=	db:migrate:schema:timestamps:add	--models-path
t	folders
@	db:migrate:status
o	--to	Migration name to run migrations until	v
o	--from	Migration name to start migrations from (excluding)	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:migrate:status	--config
t	filepaths
=	db:migrate:status	--options-path
t	filepaths
=	db:migrate:status	--migrations-path
t	folders
=	db:migrate:status	--seeders-path
t	folders
=	db:migrate:status	--models-path
t	folders
@	db:migrate:undo
o	--name	Name of the migration to undo	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:migrate:undo	--config
t	filepaths
=	db:migrate:undo	--options-path
t	filepaths
=	db:migrate:undo	--migrations-path
t	folders
=	db:migrate:undo	--seeders-path
t	folders
=	db:migrate:undo	--models-path
t	folders
@	db:migrate:undo:all
o	--to	Revert to the provided migration	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:migrate:undo:all	--config
t	filepaths
=	db:migrate:undo:all	--options-path
t	filepaths
=	db:migrate:undo:all	--migrations-path
t	folders
=	db:migrate:undo:all	--seeders-path
t	folders
=	db:migrate:undo:all	--models-path
t	folders
@	db:seed
o	--seed	List of seed files	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:seed	--seed
t	filepaths
=	db:seed	--config
t	filepaths
=	db:seed	--options-path
t	filepaths
=	db:seed	--migrations-path
t	folders
=	db:seed	--seeders-path
t	folders
=	db:seed	--models-path
t	folders
@	db:seed:undo
o	--seed	List of seed files	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:seed:undo	--seed
t	filepaths
=	db:seed:undo	--config
t	filepaths
=	db:seed:undo	--options-path
t	filepaths
=	db:seed:undo	--migrations-path
t	folders
=	db:seed:undo	--seeders-path
t	folders
=	db:seed:undo	--models-path
t	folders
@	db:seed:all
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:seed:all	--config
t	filepaths
=	db:seed:all	--options-path
t	filepaths
=	db:seed:all	--migrations-path
t	folders
=	db:seed:all	--seeders-path
t	folders
=	db:seed:all	--models-path
t	folders
@	db:seed:undo:all
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:seed:undo:all	--config
t	filepaths
=	db:seed:undo:all	--options-path
t	filepaths
=	db:seed:undo:all	--migrations-path
t	folders
=	db:seed:undo:all	--seeders-path
t	folders
=	db:seed:undo:all	--models-path
t	folders
@	db:create
o	--charset	Pass charset option to dialect, MYSQL only	v
o	--collate	Pass collate option to dialect	v
o	--encoding	Pass encoding option to dialect, PostgreSQL only	v
o	--ctype	Pass ctype option to dialect, PostgreSQL only	v
o	--template	Pass template option to dialect, PostgreSQL only	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:create	--config
t	filepaths
=	db:create	--options-path
t	filepaths
=	db:create	--migrations-path
t	folders
=	db:create	--seeders-path
t	folders
=	db:create	--models-path
t	folders
@	db:drop
o	--charset	Pass charset option to dialect, MYSQL only	v
o	--collate	Pass collate option to dialect	v
o	--encoding	Pass encoding option to dialect, PostgreSQL only	v
o	--ctype	Pass ctype option to dialect, PostgreSQL only	v
o	--template	Pass template option to dialect, PostgreSQL only	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	db:drop	--config
t	filepaths
=	db:drop	--options-path
t	filepaths
=	db:drop	--migrations-path
t	folders
=	db:drop	--seeders-path
t	folders
=	db:drop	--models-path
t	folders
@	init
o	--force	Will drop the existing config folder and re-create it	
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	init	--config
t	filepaths
=	init	--options-path
t	filepaths
=	init	--migrations-path
t	folders
=	init	--seeders-path
t	folders
=	init	--models-path
t	folders
@	init:config
o	--force	Will drop the existing config folder and re-create it	
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	init:config	--config
t	filepaths
=	init:config	--options-path
t	filepaths
=	init:config	--migrations-path
t	folders
=	init:config	--seeders-path
t	folders
=	init:config	--models-path
t	folders
@	init:migrations
o	--force	Will drop the existing config folder and re-create it	
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	init:migrations	--config
t	filepaths
=	init:migrations	--options-path
t	filepaths
=	init:migrations	--migrations-path
t	folders
=	init:migrations	--seeders-path
t	folders
=	init:migrations	--models-path
t	folders
@	init:models
o	--force	Will drop the existing config folder and re-create it	
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	init:models	--config
t	filepaths
=	init:models	--options-path
t	filepaths
=	init:models	--migrations-path
t	folders
=	init:models	--seeders-path
t	folders
=	init:models	--models-path
t	folders
@	init:seeders
o	--force	Will drop the existing config folder and re-create it	
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	init:seeders	--config
t	filepaths
=	init:seeders	--options-path
t	filepaths
=	init:seeders	--migrations-path
t	folders
=	init:seeders	--seeders-path
t	folders
=	init:seeders	--models-path
t	folders
@	migration:generate
o	--name	Defines the name of the migration	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	migration:generate	--config
t	filepaths
=	migration:generate	--options-path
t	filepaths
=	migration:generate	--migrations-path
t	folders
=	migration:generate	--seeders-path
t	folders
=	migration:generate	--models-path
t	folders
@	model:generate
o	--name	Defines the name of the new model	v
o	--attributes	A list of attributes	v
o	--force	Forcefully re-creates model with the same name	
o	--underscored	Use snake case for the timestamp's attribute names	
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	model:generate	--config
t	filepaths
=	model:generate	--options-path
t	filepaths
=	model:generate	--migrations-path
t	folders
=	model:generate	--seeders-path
t	folders
=	model:generate	--models-path
t	folders
@	seed:generate
o	--name	Defines the name of the seed	v
o	--env	The environment to run the command in	v
o	--config	The path to the config file	v
o	--options-path	The path to a JSON file with additional options	v
o	--migrations-path	The path to the migrations folder	v
o	--seeders-path	The path to the seeders folder	v
o	--models-path	The path to the models folder	v
o	--url	The database connection string to use	v
o	--debug	When available show various debug information	
o	--help	Show help	
o	--version	Show version number	
=	seed:generate	--config
t	filepaths
=	seed:generate	--options-path
t	filepaths
=	seed:generate	--migrations-path
t	folders
=	seed:generate	--seeders-path
t	folders
=	seed:generate	--models-path
t	folders

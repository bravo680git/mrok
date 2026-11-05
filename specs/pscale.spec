@	
s	audit-log	List audit logs
s	auth	Login and logout via the PlanetScale API
s	backup	Create, list, show, and delete branch backups
s	branch	Create, delete, diff, and manage branches
s	completion	Generate completion script for your shell
s	connect	Create a secure connection to a database and branch for a local client
s	database|db	Create, read, delete, and dump/restore databases
s	deploy-request|dr	Create, review, diff, and manage deploy requests
s	help	Help about any command
s	org	List, show, and switch organizations
s	password	Create, list, and delete branch passwords
s	region	List regions
s	service-token	Create, list, and manage access for service tokens
s	shell	Open a MySQL shell instance to a database and branch
s	signup|register|sign-up	Signup for a new PlanetScale account
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--version	Show pscale version	
=		--config
t	filepaths
=		--format
v	human	
v	json	
v	csv	
@	audit-log
s	list|ls	List all audit logs of an organization
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	audit-log	--config
t	filepaths
=	audit-log	--format
v	human	
v	json	
v	csv	
@	audit-log list
@	auth
s	login	Authenticate with the PlanetScale API
s	logout	Log out of the PlanetScale API
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	auth	--config
t	filepaths
=	auth	--format
v	human	
v	json	
v	csv	
@	auth login
o	--client-id	The client ID for the PlanetScale CLI application	
o	--client-secret	The client ID for the PlanetScale CLI application	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	auth login	--config
t	filepaths
=	auth login	--format
v	human	
v	json	
v	csv	
@	auth logout
o	--client-id	The client ID for the PlanetScale CLI application	
o	--client-secret	The client ID for the PlanetScale CLI application	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	auth logout	--config
t	filepaths
=	auth logout	--format
v	human	
v	json	
v	csv	
@	backup
s	create|b	Backup a branch's data and schema
s	delete|rm	Delete a branch backup
s	list|ls	List all backups of a branch
s	restore	Restore a backup to a new branch
s	show	Show a specific backup of a branch
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	backup	--config
t	filepaths
=	backup	--format
v	human	
v	json	
v	csv	
@	backup create
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	backup create	--config
t	filepaths
=	backup create	--format
v	human	
v	json	
v	csv	
@	backup delete
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	backup delete	--config
t	filepaths
=	backup delete	--format
v	human	
v	json	
v	csv	
@	backup list
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	backup list	--config
t	filepaths
=	backup list	--format
v	human	
v	json	
v	csv	
@	backup restore
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	backup restore	--config
t	filepaths
=	backup restore	--format
v	human	
v	json	
v	csv	
@	backup show
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	backup show	--config
t	filepaths
=	backup show	--format
v	human	
v	json	
v	csv	
@	branch
s	create|b	Create a new branch from a database
s	delete|rm	Delete a branch from a database
s	diff	Show the diff of a branch
s	list|ls	List all branches of a database
s	promote|p	Promote a new branch from a database
s	refresh-schema	Refresh the schema for a database branch
s	schema	Show the schema of a branch
s	show	Show a specific branch of a database
s	switch	Switches the current project to use the specified branch
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	branch	--config
t	filepaths
=	branch	--format
v	human	
v	json	
v	csv	
@	branch create
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--from	Branch to be created from	
o	--region	Region for the database	
o	--restore	Backup to restore into the branch	
o	--web|-w	Create a branch in your web browser	
a	2	0
=	branch create	--config
t	filepaths
=	branch create	--format
v	human	
v	json	
v	csv	
@	branch delete
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--force	Delete a branch without confirmation	
a	2	0
=	branch delete	--config
t	filepaths
=	branch delete	--format
v	human	
v	json	
v	csv	
@	branch diff
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--web	Open in web browser	
a	2	0
=	branch diff	--config
t	filepaths
=	branch diff	--format
v	human	
v	json	
v	csv	
@	branch list
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--web	List branches in your web browser	
a	1	0
=	branch list	--config
t	filepaths
=	branch list	--format
v	human	
v	json	
v	csv	
@	branch promote
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	branch promote	--config
t	filepaths
=	branch promote	--format
v	human	
v	json	
v	csv	
@	branch refresh-schema
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	branch refresh-schema	--config
t	filepaths
=	branch refresh-schema	--format
v	human	
v	json	
v	csv	
@	branch schema
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--web	Open in web browser	
a	2	0
=	branch schema	--config
t	filepaths
=	branch schema	--format
v	human	
v	json	
v	csv	
@	branch show
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--web	Open in web browser	
a	2	0
=	branch show	--config
t	filepaths
=	branch show	--format
v	human	
v	json	
v	csv	
@	branch switch
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--create	If enabled, will automatically create the branch if it does not exist	
o	--database	The database this project is using	v
o	--parent-branch	Parent branch to inherit from if a new branch is being created (default "main")	v
a	1	0
=	branch switch	--config
t	filepaths
=	branch switch	--format
v	human	
v	json	
v	csv	
@	completion
o	--web	Open in web browser	
o	--help|-h	Show help	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	completion	--config
t	filepaths
=	completion	--format
v	human	
v	json	
v	csv	
@	connect
o	--help|-h	Show help	
o	--execute	Run this command after successfully connecting to the database	v
o	--execute-env-url	Environment variable name that contains the exposed Database URL. (default "DATABASE_URL")	v
o	--execute-protocol	Protocol for the exposed URL (by default DATABASE_URL) value in execute (default "mysql2")	v
o	--host	Local host to bind and listen for connections (default "127.0.0.1")	v
o	--org	The organization for the current user	v
o	--port	Local port to bind and listen for connections (default "3306")	v
o	--remote-addr	PlanetScale Database remote network address. By default the remote address is populated…	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	connect	--config
t	filepaths
=	connect	--format
v	human	
v	json	
v	csv	
@	database
s	create	Create a database instance
s	delete|rm	Delete a database instance
s	dump	Backup and dump your database
s	list|ls	List databases
s	restore-dump	Restore your database from a local dump directory
s	show	Retrieve information about a database
o	--org	The organization for the current user	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	database	--config
t	filepaths
=	database	--format
v	human	
v	json	
v	csv	
@	database create
o	--notes	Notes for the database	v
o	--region	Region for the database	
o	--web	Open in web browser	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	database create	--config
t	filepaths
=	database create	--format
v	human	
v	json	
v	csv	
@	database delete
o	--force	Delete a database without confirmation	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	database delete	--config
t	filepaths
=	database delete	--format
v	human	
v	json	
v	csv	
@	database dump
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--local-addr	Local address to bind and listen for connections. By default the proxy binds to 127.0.0.1 with a…	v
o	--output	Output director of the dump. By default the dump is stored to a folder in the current directory	v
o	--tables	Comma separated string of tables to dump. By default all tables are dumped	v
a	2	0
=	database dump	--config
t	filepaths
=	database dump	--format
v	human	
v	json	
v	csv	
@	database list
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--web	Open in web browser	
=	database list	--config
t	filepaths
=	database list	--format
v	human	
v	json	
v	csv	
@	database restore-dump
o	--dir	Directory that contains the files to be used for restoration (required)	v
o	--local-addr	Local address to bind and listen for connections. By default the proxy binds to 127.0.0.1 with a…	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	database restore-dump	--config
t	filepaths
=	database restore-dump	--format
v	human	
v	json	
v	csv	
@	database show
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--web	Open in web browser	
a	1	0
=	database show	--config
t	filepaths
=	database show	--format
v	human	
v	json	
v	csv	
@	deploy-request
s	close	Close a deploy request
s	create	Create a deploy request from a branch
s	deploy	Deploy a specific deploy request
s	diff	Show the diff of a deploy request
s	list|ls	List all deploy requests for a database
s	review	Review a deploy request (approve, comment, etc...)
s	show	Show a specific deploy request
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--org	The organization for the current user	v
=	deploy-request	--config
t	filepaths
=	deploy-request	--format
v	human	
v	json	
v	csv	
@	deploy-request close
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	deploy-request close	--config
t	filepaths
=	deploy-request close	--format
v	human	
v	json	
v	csv	
@	deploy-request create
o	--deploy-to	Branch to deploy the branch. By default it's set to 'main'	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	deploy-request create	--config
t	filepaths
=	deploy-request create	--format
v	human	
v	json	
v	csv	
@	deploy-request deploy
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	deploy-request deploy	--config
t	filepaths
=	deploy-request deploy	--format
v	human	
v	json	
v	csv	
@	deploy-request diff
o	--web	Open in web browser	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	deploy-request diff	--config
t	filepaths
=	deploy-request diff	--format
v	human	
v	json	
v	csv	
@	deploy-request list
o	--web	Open in web browser	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	deploy-request list	--config
t	filepaths
=	deploy-request list	--format
v	human	
v	json	
v	csv	
@	deploy-request review
o	--approve	Approve a deploy request	
o	--comment	Comment on a deploy request	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	deploy-request review	--config
t	filepaths
=	deploy-request review	--format
v	human	
v	json	
v	csv	
@	deploy-request show
o	--web	Open in web browser	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	2	0
=	deploy-request show	--config
t	filepaths
=	deploy-request show	--format
v	human	
v	json	
v	csv	
@	help
@	org
s	list|ls	List the currently active organizations
s	show	Display the currently active organization
s	switch	Switch the currently active organization
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	org	--config
t	filepaths
=	org	--format
v	human	
v	json	
v	csv	
@	org list
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	org list	--config
t	filepaths
=	org list	--format
v	human	
v	json	
v	csv	
@	org show
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	org show	--config
t	filepaths
=	org show	--format
v	human	
v	json	
v	csv	
@	org switch
o	--save-config	Path to store the organization. By default the configuration is deducted automatically based on…	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	org switch	--config
t	filepaths
=	org switch	--format
v	human	
v	json	
v	csv	
@	password
s	create|p	Create password to access a branch's data
s	delete|rm	Delete a branch password
s	list|ls	List all passwords of a database
o	--org	The organization for the current user	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	password	--config
t	filepaths
=	password	--format
v	human	
v	json	
v	csv	
@	password create
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	password create	--config
t	filepaths
=	password create	--format
v	human	
v	json	
v	csv	
@	password delete
o	--force	Delete a password without confirmation	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	password delete	--config
t	filepaths
=	password delete	--format
v	human	
v	json	
v	csv	
@	password list
o	--web	Open in web browser	
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	password list	--config
t	filepaths
=	password list	--format
v	human	
v	json	
v	csv	
@	region
s	list|ls	List regions
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	region	--config
t	filepaths
=	region	--format
v	human	
v	json	
v	csv	
@	region list
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	region list	--config
t	filepaths
=	region list	--format
v	human	
v	json	
v	csv	
@	service-token
s	add-access	Ddd access to a service token in the organization
s	create	Create a service token for the organization
s	delete	Delete an entire service token in an organization
s	delete-access	Delete access granted to a service token in the organization
s	list	List service tokens for the organization
s	show-access	Fetch a service token and it's accesses
o	--org	The organization for the current user	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	service-token	--config
t	filepaths
=	service-token	--format
v	human	
v	json	
v	csv	
@	service-token add-access
o	--database	The database this project is using	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	service-token add-access	--config
t	filepaths
=	service-token add-access	--format
v	human	
v	json	
v	csv	
@	service-token create
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	service-token create	--config
t	filepaths
=	service-token create	--format
v	human	
v	json	
v	csv	
@	service-token delete
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	service-token delete	--config
t	filepaths
=	service-token delete	--format
v	human	
v	json	
v	csv	
@	service-token delete-access
o	--database	The database this project is using	v
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	3	0
=	service-token delete-access	--config
t	filepaths
=	service-token delete-access	--format
v	human	
v	json	
v	csv	
@	service-token list
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	service-token list	--config
t	filepaths
=	service-token list	--format
v	human	
v	json	
v	csv	
@	service-token show-access
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
a	1	0
=	service-token show-access	--config
t	filepaths
=	service-token show-access	--format
v	human	
v	json	
v	csv	
@	shell
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
o	--port	Local port to bind and listen for connections (default "3306")	v
o	--remote-addr	PlanetScale Database remote network address. By default the remote address is populated…	v
o	--local-addr	Local address to bind and listen for connections. By default the proxy binds to 127.0.0.1 with a…	v
a	2	0
=	shell	--config
t	filepaths
=	shell	--format
v	human	
v	json	
v	csv	
@	signup
o	--help|-h	Show help	
o	--api-token	The API token to use for authenticating against the PlanetScale API	v
o	--api-url	The base URL for the PlanetScale API. (default "https://api.planetscale.com/")	v
o	--config	Config file (default is $HOME/.config/planetscale/pscale.yml)	v
o	--debug	Enable debug mode	
o	--format|-f	Show output in a specific format. Possible values: [human, json, csv] (default "human")	v
o	--no-color	Disable color output	
o	--service-token	Service Token for authenticating	v
o	--service-token-name	The Service Token name for authenticating	v
=	signup	--config
t	filepaths
=	signup	--format
v	human	
v	json	
v	csv	

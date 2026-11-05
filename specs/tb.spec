@	
s	check	Check file syntax
s	dependencies	Print all data sources dependencies
s	diff	Diffs local datafiles to the corresponding remote files in the workspace
s	drop-prefix	Drop all the resources inside a project with prefix. This command is dangerous because it removes…
s	fmt	Formats a .datasource, .pipe or .incl file
s	init	Initialize folder layout
s	materialize	[BETA] Given a local Pipe datafile path (FILENAME) and optionally a Materialized View name…
s	prompt	Learn how to include info about the CLI in your shell PROMPT
s	pull	Retrieve latest versions for project files from Tinybird
s	push	Push files to Tinybird
s	sql	Run SQL query over data sources and pipes
o	--debug	Prints internal representation, can be combined with any command to get more information	
o	--no-debug	Prints internal representation, can be combined with any command to get more information	
o	--token	Use auth token, defaults to TB_TOKEN envvar, then to the .tinyb file	v
o	--host	Use custom host, defaults to TB_HOST envvar, then to https://api.tinybird.co	v
o	--gcp-project-id	The Google Cloud project ID	v
o	--gcs-bucket	The Google Cloud Storage bucket to write temp files when using the connectors	v
o	--google-application-credentials	Set GOOGLE_APPLICATION_CREDENTIALS	v
o	--sf-account	The Snowflake Account (e.g. your-domain.west-europe.azure)	v
o	--sf-warehouse	The Snowflake warehouse name	v
o	--sf-database	The Snowflake database name	v
o	--sf-schema	The Snowflake schema name	v
o	--sf-role	The Snowflake role name	v
o	--sf-user	The Snowflake user name	v
o	--sf-password	The Snowflake password	v
o	--sf-storage-integration	The Snowflake GCS storage integration name (leave empty to auto-generate one)	v
o	--sf-stage	The Snowflake GCS stage name (leave empty to auto-generate one)	v
o	--with-headers	Flag to enable connector to export with headers	
o	--version-warning	Don't print version warning message if there's a new available version. You can use…	
o	--no-version-warning	Don't print version warning message if there's a new available version. You can use…	
o	--hide-tokens	Disable the output of tokens	
o	--version	Show the version and exit	
o	--help	Show this message and exit	
@	check
o	--debug	Print internal representation	
o	--help	Show this message and exit	
a	1	0
#	check	1
t	folders,filepaths
@	dependencies
o	--no-deps	Print only data sources with no pipes using them	
o	--match	Retrieve any resource matching the pattern	v
o	--pipe	Retrieve any resource used by pipe	v
o	--datasource	Retrieve resources depending on this Data Source	v
o	--check-for-partial-replace	Retrieve dependant Data Sources that will have their data replaced if a partial replace is…	
o	--recursive	Calculate recursive dependencies	
o	--help	Show this message and exit	
@	diff
o	--fmt	Format files before doing the diff, default is True so both files match the format	
o	--no-fmt	Format files before doing the diff, default is True so both files match the format	
o	--no-color	Don't colorize diff	
o	--main	Diffs local datafiles to the corresponding remote files in the main workspace. Only works when…	
o	--help	Show this message and exit	
a	1	1
#	diff	1
t	folders,filepaths
@	drop-prefix
o	--yes	Do not ask for confirmation	
o	--dry-run	Run the command without removing anything	
o	--help	Show this message and exit	
a	1	0
@	fmt
o	--line-length	A number indicating the maximum characters per line in the node SQL, lines will be splitted based…	v
o	--dry-run	Don't ask to override the local file	
o	--yes	Do not ask for confirmation to overwrite the local file	
o	--help	Show this message and exit	
a	1	1
#	fmt	1
t	folders,filepaths
@	init
o	--generate-datasources	Generate datasources based on CSV, NDJSON and Parquet files in this folder	
o	--folder	Folder where files will be placed	v
o	--force	Overrides existing files	
o	--help	Show this message and exit	
=	init	--folder
t	folders
@	materialize
o	--prefix	Use prefix for all the resources	v
o	--push-deps	Push dependencies, disabled by default	
o	--workspace_map		v
o	--workspace	Add a workspace path to the list of external workspaces, usage: --workspace name path/to/folder	v
o	--no-versions	When set, resource dependency versions are not used, it pushes the dependencies as-is	
o	--verbose	Prints more log	
o	--force-populate	Subset or full	v
o	--unlink-on-populate-error	If the populate job fails the Materialized View is unlinked and new data won't be ingested in the…	
o	--override-pipe	Override pipe if exists or prompt	
o	--override-datasource	Override data source if exists or prompt	
o	--help	Show this message and exit	
a	2	0
#	materialize	1
t	folders,filepaths
@	prompt
o	--help	Show this message and exit	
@	pull
o	--folder	Folder where files will be placed	v
o	--auto	Saves datafiles automatically into their default directories (/datasources or /pipes)	
o	--match	Retrieve any resourcing matching the pattern. eg --match _test	v
o	--prefix	Download only resources with this prefix	v
o	--force	Override existing files	
o	--help	Show this message and exit	
=	pull	--folder
t	folders
@	push
o	--prefix	Use prefix for all the resources	v
o	--dry-run	Run the command without creating resources on the Tinybird account or any side effect	
o	--check	Enable/Disable output checking, enabled by default	
o	--no-check	Enable/Disable output checking, enabled by default	
o	--push-deps	Push dependencies, disabled by default	
o	--debug	Prints internal representation, can be combined with any command to get more information	
o	-f|--force	Override pipes when they already exist	
o	--override-datasource	When pushing a pipe with a Materialized node if the target Data Source exists it will try to…	
o	--populate	Populate materialized nodes when pushing them	
o	--subset	Populate with a subset percent of the data (limited to a maximum of 2M rows), this is useful to…	v
o	--sql-condition	Populate with a SQL condition to be applied to the trigger Data Source of the Materialized View…	v
o	--unlink-on-populate-error	If the populate job fails the Materialized View is unlinked and new data won't be ingested in the…	
o	--fixtures	Append fixtures to data sources	
o	--wait	To be used along with --populate command. Waits for populate jobs to finish, showing a progress…	
o	--yes	Do not ask for confirmation	
o	--only-response-times	Checks only response times, when --force push a pipe	
o	--workspace_map		v
o	--workspace	Add a workspace path to the list of external workspaces, usage: --workspace name path/to/folder	v
o	--no-versions	When set, resource dependency versions are not used, it pushes the dependencies as-is	
o	--timeout	Timeout you want to use for the job populate	v
o	-l|--limit	Number of requests to validate	v
o	--sample-by-params	When set, we will aggregate the pipe_stats_rt requests by extractURLParameterNames(assumeNotNull(ur…	v
o	-ff|--failfast	When set, the checker will exit as soon one test fails	
o	--ignore-order	When set, the checker will ignore the order of list properties	
o	--validate-processed-bytes	When set, the checker will validate that the new version doesn't process more than 25% than the…	
o	--last-requests-from-main	When set, the checker will get top requests requests from main	
o	--help	Show this message and exit	
a	1	1
#	push	1
t	folders,filepaths
@	sql
o	--rows_limit	Max number of rows retrieved	v
o	--pipeline	The name of the Pipe to run the SQL Query	v
o	--pipe	The path to the .pipe file to run the SQL Query of a specific NODE	v
o	--node	The NODE name	v
o	--format	Output format	v
o	--stats	Show query stats	
o	--no-stats	Show query stats	
o	--help	Show this message and exit	
a	1	0
=	sql	--format
v	json	
v	csv	
v	human	

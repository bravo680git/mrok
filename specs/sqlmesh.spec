@	
s	init	Create a new SQLMesh repository
s	render	Render a model's query, optionally expanding referenced models
s	evaluate	Evaluate a model and return a dataframe with a default limit of 1000
s	format	Format all SQL models and audits
s	diff	Show the diff between the local state and the target environment
s	plan	Apply local changes to the target environment
s	run	Evaluate missing intervals for the target environment
s	invalidate	Invalidate the target environment, forcing its removal during the next run of the janitor process
s	janitor	Run the janitor process on-demand
s	dag	Render the DAG as an html file
s	create_test	Generate a unit test fixture for a given model
s	test	Run model unit tests
s	audit	Run audits for the target model(s)
s	ui	Start a browser-based SQLMesh UI
s	migrate	Migrate SQLMesh to the current running version
s	rollback	Rollback SQLMesh to the previous migration
s	create_external_models	Create a schema file containing external model schemas
o	--paths	Paths to SQLMesh project files	v
o	--config	Path to config file	v
o	--gateway	The name of the gateway	v
o	--ignore-warnings	Ignore warnings	
o	--debug	Enable debug mode	
o	--log-to-stdout	Display logs in stdout	
o	--log-file-dir	The directory to write log files to	v
=		--paths
t	folders
=		--config
t	filepaths
=		--log-file-dir
t	folders
@	init
o	-t|--template	Project template. Supported values: airflow, dbt, dlt, default, empty	v
o	--dlt-pipeline	DLT pipeline for which to generate a SQLMesh project. Use alongside template: dlt	v
a	1	0
=	init	-t
v	airflow	
v	dbt	
v	dlt	
v	default	
v	empty	
@	render
o	--dialect	The SQL dialect to render the query as	v
o	--no-format	Disable fancy formatting of the query	
o	--start	Start time for the render	v
o	--end	End time for the render	v
o	--execution-time	Execution time for the render	v
o	--expand	Expand referenced models	v
a	1	0
@	evaluate
o	--start	Start time for evaluation	v
o	--end	End time for evaluation	v
o	--execution-time	Execution time for evaluation	v
o	--limit	The number of rows which the query should be limited to	v
a	1	0
@	format
o	-t|--transpile	Transpile project models to the specified dialect	v
o	--append-newline	Include a newline at the end of each file	
o	--no-rewrite-casts	Preserve the existing casts, without rewriting them to use the :: syntax	
o	--normalize	Whether or not to normalize identifiers to lowercase	
o	--pad	Determines the pad size in a formatted string	v
o	--indent	Determines the indentation size in a formatted string	v
o	--normalize-functions	Whether or not to normalize all function names	v
o	--leading-comma	Determines whether or not the comma is leading or trailing in select expressions	
o	--max-text-width	The max number of characters in a segment before creating new lines in pretty mode	v
o	--check	Whether or not to check formatting (but not actually format anything)	
a	1	1
=	format	--normalize-functions
v	upper	
v	lower	
#	format	1
t	filepaths
@	diff
a	1	0
@	plan
o	--create-from	The environment to create the target environment from if it doesn't exist. Default: prod	v
o	--skip-tests	Skip tests prior to generating the plan if they are defined	
o	--restate-model	Restate data for specified models and models downstream from the one specified	v
o	--no-gaps	Ensure that new snapshots have no data gaps when comparing to existing snapshots	
o	--skip-backfill	Skip the backfill step and only create a virtual update for the plan	
o	--empty-backfill	Produce empty backfill	
o	--forward-only	Create a plan for forward-only changes	
o	--allow-destructive-model	Allow destructive forward-only changes to models whose names match the expression	v
o	--effective-from	The effective date from which to apply forward-only changes on production	v
o	--no-prompts	Disable interactive prompts for the backfill time range	
o	--auto-apply	Automatically apply the new plan after creation	
o	--no-auto-categorization	Disable automatic change categorization	
o	--include-unmodified	Include unmodified models in the target environment	
o	--select-model	Select specific model changes that should be included in the plan	v
o	--backfill-model	Backfill only the models whose names match the expression	v
o	--no-diff	Hide text differences for changed models	
o	--run	Run latest intervals as part of the plan application (prod environment only)	
o	--enable-preview	Enable preview for forward-only models when targeting a development environment	
o	--verbose	Enable verbose output	
a	1	0
@	run
o	--start	Start time for the run	v
o	--end	End time for the run	v
o	--skip-janitor	Skip the janitor task	
o	--ignore-cron	Run for all missing intervals, ignoring individual cron schedules	
o	--select-model	Select specific models to run. Note: this always includes upstream dependencies	v
o	--exit-on-env-update	Exit with specified code if the run is interrupted by an update to the target environment	v
o	--no-auto-upstream	Do not automatically include upstream models. Only applicable when --select-model is used	
a	1	0
@	invalidate
o	-s|--sync	Wait for the environment to be deleted before returning	
a	1	0
@	janitor
o	--ignore-ttl	Cleanup snapshots that are not referenced in any environment, regardless of when they're set to…	
@	dag
o	--select-model	Select specific models to include in the dag	v
a	1	0
@	create_test
o	-q|--query	Queries that will be used to generate data for the model's dependencies	v
o	-o|--overwrite	When true, the fixture file will be overwritten in case it already exists	
o	-v|--var	Key-value pairs that will define variables needed by the model	v
o	-p|--path	The file path corresponding to the fixture, relative to the test directory	v
o	-n|--name	The name of the test that will be created	v
o	--include-ctes	When true, CTE fixtures will also be generated	
a	1	0
@	test
o	-k|--match-pattern	Only run tests matching pattern	v
o	--verbose	Enable verbose output	
o	--preserve-fixtures	Preserve the fixture tables in the testing database, useful for debugging	
a	1	1
@	audit
o	--model	A model to audit	v
o	--start	Start time for the audit	v
o	--end	End time for the audit	v
o	--execution-time	Execution time for the audit	v
@	ui
o	--host	Bind socket to this host	v
o	--port	Bind socket to this port	v
o	--mode	Mode to start the UI in	v
=	ui	--mode
v	ide	
v	catalog	
v	docs	
v	plan	
@	migrate
@	rollback
@	create_external_models
o	--strict	Raise an error if the external model is missing in the database	

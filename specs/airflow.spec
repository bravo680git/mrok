@	
s	celery	Celery components
s	cheat-sheet	Display cheat sheet
s	config	View configuration
s	connections	Manage connections
s	dag-processor	Start a standalone Dag Processor instance
s	dags	Manage DAGs
s	db	Database operations
s	info	Show information about current Airflow and environment
s	jobs	Manage jobs
s	kerberos	Start a kerberos ticket renewer
s	kubernetes	Tools to help run the KubernetesExecutor
s	plugins	Dump information about loaded plugins
s	pools	Manage pools
s	providers	Display providers
s	roles	Manage roles
s	rotate-fernet-key	Rotate encrypted connection credentials and variables
s	scheduler	Start a scheduler instance
s	standalone	Run an all-in-one copy of Airflow
s	sync-perm	Update permissions for existing roles and optionally DAGs
s	tasks	Manage tasks
s	triggerer	Start a triggerer instance
s	users	Manage users
s	variables	Manage variables
s	version	Show the version
s	webserver	Start a Airflow webserver instance
o	-h|--help	Show this help message and exit	
@	celery
s	flower	Start a Celery Flower
s	stop	Stop the Celery worker gracefully
s	worker	Start a Celery worker node
o	-h|--help	Show this help message and exit	
@	celery flower
o	-h|--help	Show this help message and exit	
o	-A|--basic-auth	Securing Flower with Basic Authentication. Accepts user:password pairs separated by a comma…	v
o	-a|--broker-api	Broker API	v
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-c|--flower-conf	Configuration file for flower	v
o	-H|--hostname	Set the hostname on which to run the server	v
o	-l|--log-file	Location of the log file	v
o	--pid	PID file location	V
o	-p|--port	The port on which to run the server	v
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
o	-u|--url-prefix	URL prefix for Flower	v
=	celery flower	-A
d
@	celery stop
o	-h|--help	Show this help message and exit	
o	--pid	PID file location	V
@	celery worker
o	-h|--help	Show this help message and exit	
o	-a|--autoscale	Minimum and Maximum number of worker to autoscale	v
o	-H|--celery-hostname	Set the hostname of celery worker if you have multiple workers on a single machine	v
o	-c|--concurrency	The number of worker processes	v
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-l|--log-file	Location of the log file	v
o	--pid	PID file location	V
o	-q|--queues	Comma delimited list of queues to serve	v
o	-s|--skip-serve-logs	Don't start the serve logs process along with the workers	
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
o	-u|--umask	Set the umask of celery worker in daemon mode	v
o	--without-gossip	Don't subscribe to other workers events	
o	--without-mingle	Don't synchronize with other workers at start-up	
@	cheat-sheet
o	-h|--help	Show this help message and exit	
o	-v|--verbose	Make logging output more verbose	
@	config
s	get-value	Print the value of the configuration
s	list	List options for the configuration
o	-h|--help	Show this help message and exit	
@	config get-value
o	-h|--help	Show this help message and exit	
a	2	0
@	config list
o	-h|--help	Show this help message and exit	
o	--color	Do emit colored output (default: auto)	v
=	config list	--color
v	off	
v	auto	
v	on	
@	connections
s	add	Add a connection
s	delete	Delete a connection
s	export	Export all connections
s	get	Get a connection
s	import	Import connections from a file
s	list	List connections
o	-h|--help	Show this help message and exit	
@	connections add
o	-h|--help	Show this help message and exit	
o	--conn-description	Connection description, optional when adding a connection	v
o	--conn-extra	Connection `Extra` field, optional when adding a connection	v
o	--conn-host	Connection host, optional when adding a connection	v
o	--conn-json	Connection JSON, required to add a connection using JSON representation	v
o	--conn-login	Connection login, optional when adding a connection	v
o	--conn-password	Connection password, optional when adding a connection	v
o	--conn-port	Connection port, optional when adding a connection	v
o	--conn-schema	Connection schema, optional when adding a connection	v
o	--conn-type	Connection type, required to add a connection without conn_uri	v
o	--conn-uri	Connection URI, required to add a connection without conn_type	v
a	1	0
@	connections delete
o	-h|--help	Show this help message and exit	
o	--color	Do emit colored output (default: auto)	v
a	1	0
=	connections delete	--color
v	off	
v	auto	
v	on	
@	connections export
o	-h|--help	Show this help message and exit	
o	--file-format	File format for the export	v
o	--format	Deprecated -- use `--file-format` instead. File format to use for the export	v
o	--serialization-format	When exporting as `.env` format, defines how connections should be serialized. Default is `uri`	v
a	1	0
=	connections export	--file-format
v	json	
v	yaml	
v	env	
=	connections export	--format
v	json	
v	yaml	
v	env	
=	connections export	--serialization-format
v	json	
v	uri	
@	connections get
o	-h|--help	Show this help message and exit	
o	--color	Do emit colored output (default: auto)	v
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
a	1	0
=	connections get	--color
v	off	
v	auto	
v	on	
=	connections get	-o
v	table	
v	json	
v	yaml	
v	plain	
@	connections import
o	-h|--help	Show this help message and exit	
a	1	0
@	connections list
o	-h|--help	Show this help message and exit	
o	--conn-id	If passed, only items with the specified connection ID will be displayed	v
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	connections list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	dag-processor
o	-h|--help	Show this help message and exit	
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-p|--do-pickle	Attempt to pickle the DAG object to send over to the workers, instead of letting workers run their…	
o	-l|--log-file	Location of the log file	v
o	-n|--num-runs	Set the number of runs to execute before exiting	v
o	--pid	PID file location	V
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
@	dags
s	backfill	Run subsections of a DAG for a specified date range
s	delete	Delete all DB records related to the specified DAG
s	list	List all the DAGs
s	list-import-errors	List all the DAGs that have import errors
s	list-jobs	List the jobs
s	list-runs	List DAG runs given a DAG id
s	next-execution	Get the next execution datetimes of a DAG
s	pause	Pause a DAG
s	report	Show DagBag loading report
s	reserialize	Reserialize all DAGs by parsing the DagBag files
s	show	Displays DAG's tasks with their dependencies
s	show-dependencies	Displays DAGs with their dependencies
s	state	Get the status of a dag run
s	test	Execute one single DagRun
s	trigger	Trigger a DAG run
s	unpause	Resume a paused DAG
o	-h|--help	Show this help message and exit	
@	dags backfill
o	-h|--help	Show this help message and exit	
o	-c|--conf	JSON string that gets pickled into the DagRun's conf attribute	v
o	--continue-on-failures	If set, the backfill will keep going even if some of the tasks failed	
o	--delay-on-limit	Amount of time in seconds to wait when the limit on maximum active dag runs (max_active_runs) has…	v
o	-x|--donot-pickle	Do not attempt to pickle the DAG object to send over to the workers, just tell the workers to run…	
o	-n|--dry-run	Perform a dry run for each task. Only renders Template Fields for each task, nothing else	
o	-e|--end-date	Override end_date YYYY-MM-DD	v
o	-i|--ignore-dependencies	Skip upstream tasks, run only the tasks matching the regexp. Only works in conjunction with…	
o	-I|--ignore-first-depends-on-past	Ignores depends_on_past dependencies for the first set of tasks only (subsequent executions in the…	
o	-l|--local	Run the task using the LocalExecutor	
o	-m|--mark-success	Mark jobs as succeeded without running them	
o	--pool	Resource pool to use	v
o	--rerun-failed-tasks	If set, the backfill will auto-rerun all the failed tasks for the backfill date range instead of…	
o	--reset-dagruns	If set, the backfill will delete existing backfill-related DAG runs and start anew with fresh…	
o	-B|--run-backwards	If set, the backfill will run tasks from the most recent day first. if there are tasks that…	
o	-s|--start-date	Override start_date YYYY-MM-DD	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-t|--task-regex	The regex to filter specific task_ids to backfill (optional)	v
o	--treat-dag-as-regex	If set, dag_id will be treated as regex instead of an exact string	
o	-v|--verbose	Make logging output more verbose	
o	-y|--yes	Do not prompt to confirm. Use with care!	
a	1	0
@	dags delete
o	-h|--help	Show this help message and exit	
o	-y|--yes	Do not prompt to confirm. Use with care!	
a	1	0
@	dags list
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-v|--verbose	Make logging output more verbose	
=	dags list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	dags list-import-errors
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-v|--verbose	Make logging output more verbose	
=	dags list-import-errors	-o
v	table	
v	json	
v	yaml	
v	plain	
@	dags list-jobs
o	-h|--help	Show this help message and exit	
o	-d|--dag-id	The id of the dag	v
o	--limit	Return a limited number of records	v
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	--state	Only list the dag runs corresponding to the state	v
o	-v|--verbose	Make logging output more verbose	
=	dags list-jobs	-o
v	table	
v	json	
v	yaml	
v	plain	
@	dags list-runs
o	-h|--help	Show this help message and exit	
o	-d|--dag-id	The id of the dag	v
o	-e|--end-date	Override end_date YYYY-MM-DD	v
o	--no-backfill	Filter all the backfill dagruns given the dag id	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-s|--start-date	Override start_date YYYY-MM-DD	v
o	--state	Only list the dag runs corresponding to the state	v
o	-v|--verbose	Make logging output more verbose	
=	dags list-runs	-o
v	table	
v	json	
v	yaml	
v	plain	
@	dags next-execution
o	-h|--help	Show this help message and exit	
o	-n|--num-executions	The number of next execution datetimes to show	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	1	0
@	dags pause
o	-h|--help	Show this help message and exit	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	1	0
@	dags report
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-v|--verbose	Make logging output more verbose	
=	dags report	-o
v	table	
v	json	
v	yaml	
v	plain	
@	dags reserialize
o	-h|--help	Show this help message and exit	
o	--clear-only	If passed, serialized DAGs will be cleared but not reserialized	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
@	dags show
o	-h|--help	Show this help message and exit	
o	--imgcat	Displays graph using the imgcat tool	
o	-s|--save	Saves the result to the indicated file	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	1	0
@	dags show-dependencies
o	-h|--help	Show this help message and exit	
o	--imgcat	Displays graph using the imgcat tool	
o	-s|--save	Saves the result to the indicated file	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
@	dags state
o	-h|--help	Show this help message and exit	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	2	0
@	dags test
o	-h|--help	Show this help message and exit	
o	-c|--conf	JSON string that gets pickled into the DagRun's conf attribute	v
o	--imgcat-dagrun	After completing the dag run, prints a diagram on the screen for the current DAG Run using the…	
o	--save-dagrun	After completing the backfill, saves the diagram for current DAG Run to the indicated file.	v
o	--show-dagrun	After completing the backfill, shows the diagram for current DAG Run.	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	2	0
@	dags trigger
o	-h|--help	Show this help message and exit	
o	-c|--conf	JSON string that gets pickled into the DagRun's conf attribute	v
o	-e|--exec-date	The execution date of the DAG	v
o	-r|--run-id	Helps to identify this run	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	1	0
@	dags unpause
o	-h|--help	Show this help message and exit	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	1	0
@	db
s	check	Check if the database can be reached
s	check-migrations	Check if migration have finished
s	clean	Purge old records in metastore tables
s	downgrade	Downgrade the schema of the metadata database
s	init	Initialize the metadata database
s	reset	Burn down and rebuild the metadata database
s	shell	Runs a shell to access the database
s	upgrade	Upgrade the metadata database to latest version
o	-h|--help	Show this help message and exit	
@	db check
o	-h|--help	Show this help message and exit	
@	db check-migrations
o	-h|--help	Show this help message and exit	
o	-t|--migration-wait-timeout	Timeout to wait for db to migrate	v
@	db clean
o	-h|--help	Show this help message and exit	
o	--clean-before-timestamp	The date or timestamp before which data should be purged.	v
o	--dry-run	Perform a dry run	
o	--skip-archive	Don't preserve purged records in an archive table	
o	-t|--tables	Table names to perform maintenance on (use comma-separated list).	v
o	-v|--verbose	Make logging output more verbose	
o	-y|--yes	Do not prompt to confirm. Use with care!	
@	db downgrade
o	-h|--help	Show this help message and exit	
o	--from-revision	(Optional) If generating sql, may supply a *from* Alembic revision	v
o	--from-version	(Optional) If generating sql, may supply a *from* version	v
o	-s|--show-sql-only	Don't actually run migrations; just print out sql scripts for offline migration. Required if using…	
o	-r|--to-revision	The Alembic revision to downgrade to. Note: must provide either `--to-revision` or `--to-version`	v
o	-n|--to-version	(Optional) If provided, only run migrations up to this version	v
o	-y|--yes	Do not prompt to confirm. Use with care!	
@	db init
o	-h|--help	Show this help message and exit	
@	db reset
o	-h|--help	Show this help message and exit	
o	-s|--skip-init	Only remove tables; do not perform db init	
o	-y|--yes	Do not prompt to confirm. Use with care!	
@	db shell
o	-h|--help	Show this help message and exit	
@	db upgrade
o	-h|--help	Show this help message and exit	
o	--from-revision	(Optional) If generating sql, may supply a *from* Alembic revision	v
o	--from-version	(Optional) If generating sql, may supply a *from* version	v
o	-s|--show-sql-only	Don't actually run migrations; just print out sql scripts for offline migration. Required if using…	
o	-r|--to-revision	(Optional) If provided, only run migrations up to and including this Alembic revision	v
o	-n|--to-version	(Optional) The airflow version to upgrade to. Note: must provide either `--to-revision` or…	v
@	info
o	-h|--help	Show this help message and exit	
o	--anonymize	Minimize any personal identifiable information. Use it when sharing output with others	
o	--file-io	Send output to file.io service and returns link	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	info	-o
v	table	
v	json	
v	yaml	
v	plain	
@	jobs
s	check	Checks if job(s) are still alive
o	-h|--help	Show this help message and exit	
@	jobs check
o	-h|--help	Show this help message and exit	
o	--allow-multiple	If passed, this command will be successful even if multiple matching alive jobs are found	
o	--hostname	The hostname of job(s) that will be checked	v
o	--job-type	The type of job(s) that will be checked	v
o	--limit	The number of recent jobs that will be checked. To disable limit, set 0	v
=	jobs check	--job-type
v	BackfillJob	
v	LocalTaskJob	
v	SchedulerJob	
v	TriggererJob	
@	kerberos
o	-h|--help	Show this help message and exit	
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-k|--keytab	Keytab	V
o	-l|--log-file	Location of the log file	v
o	--pid	PID file location	V
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
a	1	0
@	kubernetes
s	cleanup-pods	Clean up Kubernetes pods (created by KubernetesExecutor/KubernetesPodOperator) in…
s	generate-dag-yaml	Generate YAML files for all tasks in DAG. Useful for debugging tasks without launching into a…
o	-h|--help	Show this help message and exit	
@	kubernetes cleanup-pods
o	-h|--help	Show this help message and exit	
o	--min-pending-minutes	Pending pods created before the time interval are to be cleaned up, measured in minutes. Default…	v
o	--namespace	Kubernetes Namespace. Default value is `[kubernetes] namespace` in configuration	v
@	kubernetes generate-dag-yaml
o	-h|--help	Show this help message and exit	
o	-o|--output-path	The output for generated yaml files	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	2	0
@	plugins
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	plugins	-o
v	table	
v	json	
v	yaml	
v	plain	
@	pools
s	delete	Delete pool
s	export	Export all pools
s	get	Get pool size
s	import	Import pools
s	list	List pools
s	set	Configure pool
o	-h|--help	Show this help message and exit	
@	pools delete
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
a	1	0
=	pools delete	-o
v	table	
v	json	
v	yaml	
v	plain	
@	pools export
o	-h|--help	Show this help message and exit	
a	1	0
@	pools get
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
a	1	0
=	pools get	-o
v	table	
v	json	
v	yaml	
v	plain	
@	pools import
o	-h|--help	Show this help message and exit	
o	-v|--verbose	Make logging output more verbose	
a	1	0
@	pools list
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	pools list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	pools set
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
a	3	0
=	pools set	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers
s	auth	Get information about API auth backends provided
s	behaviours	Get information about registered connection types with custom behaviours
s	get	Get detailed information about a provider
s	hooks	List registered provider hooks
s	links	List extra links registered by the providers
s	list	List installed providers
s	logging	Get information about task logging handlers provided
s	secrets	Get information about secrets backends provided
s	widgets	Get information about registered connection form widgets
o	-h|--help	Show this help message and exit	
@	providers auth
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers auth	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers behaviours
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers behaviours	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers get
o	-h|--help	Show this help message and exit	
o	--color	Do emit colored output (default: auto)	v
o	-f|--full	Full information about the provider, including documentation information	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
a	1	0
=	providers get	--color
v	off	
v	auto	
v	on	
=	providers get	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers hooks
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers hooks	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers links
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers links	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers list
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers logging
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers logging	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers secrets
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers secrets	-o
v	table	
v	json	
v	yaml	
v	plain	
@	providers widgets
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	providers widgets	-o
v	table	
v	json	
v	yaml	
v	plain	
@	roles
s	create	Create role
s	delete	Delete role
s	export	Export roles (without permissions) from db to JSON file
s	import	Import roles (without permissions) from JSON file to db
s	list	List roles
o	-h|--help	Show this help message and exit	
@	roles create
o	-h|--help	Show this help message and exit	
o	-v|--verbose	Make logging output more verbose	
a	1	1
@	roles delete
o	-h|--help	Show this help message and exit	
o	-v|--verbose	Make logging output more verbose	
a	1	1
@	roles export
o	-h|--help	Show this help message and exit	
o	-p|--pretty	Format output JSON file by sorting role names and indenting by 4 spaces	
o	-v|--verbose	Make logging output more verbose	
a	1	0
@	roles import
o	-h|--help	Show this help message and exit	
o	-v|--verbose	Make logging output more verbose	
a	1	0
@	roles list
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	roles list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	rotate-fernet-key
o	-h|--help	Show this help message and exit	
@	scheduler
o	-h|--help	Show this help message and exit	
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-p|--do-pickle	Attempt to pickle the DAG object to send over to the workers, instead of letting workers run their…	
o	-l|--log-file	Location of the log file	v
o	-n|--num-runs	Set the number of runs to execute before exiting	v
o	--pid	PID file location	V
o	-s|--skip-serve-logs	Don't start the serve logs process along with the workers	
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
@	standalone
o	-h|--help	Show this help message and exit	
@	sync-perm
o	-h|--help	Show this help message and exit	
o	--include-dags	If passed, DAG specific permissions will also be synced	
@	tasks
s	clear	Clear a set of task instance, as if they never ran
s	failed-deps	Returns the unmet dependencies for a task instance
s	list	List the tasks within a DAG
s	render	Render a task instance's template(s)
s	run	Run a single task instance
s	state	Get the status of a task instance
s	states-for-dag-run	Get the status of all task instances in a dag run
s	test	Test a task instance
o	-h|--help	Show this help message and exit	
@	tasks clear
o	-h|--help	Show this help message and exit	
o	-R|--dag-regex	Search dag_id as regex instead of exact string	
o	-d|--downstream	Include downstream tasks	
o	-e|--end-date	Override end_date YYYY-MM-DD	v
o	-X|--exclude-parentdag	Exclude ParentDAGS if the task cleared is a part of a SubDAG	
o	-x|--exclude-subdags	Exclude subdags	
o	-f|--only-failed	Only failed jobs	
o	-r|--only-running	Only running jobs	
o	-s|--start-date	Override start_date YYYY-MM-DD	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-t|--task-regex	The regex to filter specific task_ids to backfill (optional)	v
o	-u|--upstream	Include upstream tasks	
o	-y|--yes	Do not prompt to confirm. Use with care!	
a	1	0
@	tasks failed-deps
o	-h|--help	Show this help message and exit	
o	--map-index	Mapped task index	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	3	0
@	tasks list
o	-h|--help	Show this help message and exit	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-t|--tree	Tree view	
o	-v|--verbose	Make logging output more verbose	
a	1	0
@	tasks render
o	-h|--help	Show this help message and exit	
o	--map-index	Mapped task index	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-v|--verbose	Make logging output more verbose	
a	3	0
@	tasks run
o	-h|--help	Show this help message and exit	
o	--cfg-path	Path to config file to use instead of airflow.cfg	v
o	-f|--force	Ignore previous task instance state, rerun regardless if task already succeeded/failed	
o	-A|--ignore-all-dependencies	Ignores all non-critical dependencies, including ignore_ti_state and ignore_task_deps	
o	-i|--ignore-dependencies	Ignore task-specific dependencies, e.g. upstream, depends_on_past, and retry delay dependencies	
o	-I|--ignore-depends-on-past	Ignore depends_on_past dependencies (but respect upstream dependencies)	
o	-N|--interactive	Do not capture standard output and error streams (useful for interactive debugging)	
o	-l|--local	Run the task using the LocalExecutor	
o	--map-index	Mapped task index	v
o	-m|--mark-success	Mark jobs as succeeded without running them	
o	-p|--pickle	Serialized pickle object of the entire dag (used internally)	v
o	--pool	Resource pool to use	v
o	--ship-dag	Pickles (serializes) the DAG and ships it to the worker	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
a	3	0
@	tasks state
o	-h|--help	Show this help message and exit	
o	--map-index	Mapped task index	v
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-v|--verbose	Make logging output more verbose	
a	3	0
@	tasks states-for-dag-run
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
a	2	0
=	tasks states-for-dag-run	-o
v	table	
v	json	
v	yaml	
v	plain	
@	tasks test
o	-h|--help	Show this help message and exit	
o	-n|--dry-run	Perform a dry run for each task. Only renders Template Fields for each task, nothing else	
o	--env-vars	Set env var in both parsing time and runtime for each of entry supplied in a JSON dict	v
o	--map-index	Mapped task index	v
o	-m|--post-mortem	Open debugger on uncaught exception	
o	-S|--subdir	File location or directory from which to look for the dag. Defaults to '[AIRFLOW_HOME]/dags' where…	v
o	-t|--task-params	Sends a JSON params dict to the task	v
a	3	0
@	triggerer
o	-h|--help	Show this help message and exit	
o	--capacity	The maximum number of triggers that a Triggerer will run at one time	v
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-l|--log-file	Location of the log file	v
o	--pid	PID file location	V
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
@	users
s	add-role	Add role to a user
s	create	Create a user
s	delete	Delete a user
s	export	Export all users
s	import	Import users
s	list	List users
s	remove-role	Remove role from a user
o	-h|--help	Show this help message and exit	
@	users add-role
o	-h|--help	Show this help message and exit	
o	-e|--email	Email of the user	v
o	-r|--role	Role of the user. Existing roles include Admin, User, Op, Viewer, and Public	v
o	-u|--username	Username of the user	v
@	users create
o	-h|--help	Show this help message and exit	
o	-e|--email	Email of the user	v
o	-f|--firstname	First name of the user	v
o	-l|--lastname	Last name of the user	v
o	-p|--password	Password of the user, required to create a user without --use-random-password	v
o	-r|--role	Role of the user. Existing roles include Admin, User, Op, Viewer, and Public	v
o	--use-random-password	Do not prompt for password. Use random string instead. Required to create a user without --password	
o	-u|--username	Username of the user	v
@	users delete
o	-h|--help	Show this help message and exit	
o	-e|--email	Email of the user	v
o	-u|--username	Username of the user	v
@	users export
o	-h|--help	Show this help message and exit	
a	1	0
@	users import
o	-h|--help	Show this help message and exit	
a	1	0
@	users list
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	users list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	users remove-role
o	-h|--help	Show this help message and exit	
o	-e|--email	Email of the user	v
o	-r|--role	Role of the user. Existing roles include Admin, User, Op, Viewer, and Public	v
o	-u|--username	Username of the user	v
@	variables
s	delete	Delete variable
s	export	Export all variables
s	get	Get variable
s	import	Import variables
s	list	List variables
s	set	Set variable
o	-h|--help	Show this help message and exit	
@	variables delete
o	-h|--help	Show this help message and exit	
a	1	0
@	variables export
o	-h|--help	Show this help message and exit	
a	1	0
@	variables get
o	-h|--help	Show this help message and exit	
o	-d|--default	Default value returned if variable does not exist	v
o	-j|--json	Deserialize JSON variable	
o	-v|--verbose	Make logging output more verbose	
a	1	0
@	variables import
o	-h|--help	Show this help message and exit	
a	1	0
@	variables list
o	-h|--help	Show this help message and exit	
o	-o|--output	Output format. Allowed values: json, yaml, plain, table (default: table)	v
o	-v|--verbose	Make logging output more verbose	
=	variables list	-o
v	table	
v	json	
v	yaml	
v	plain	
@	variables set
o	-h|--help	Show this help message and exit	
o	-j|--json	Serialize JSON variable	
a	2	0
@	version
o	-h|--help	Show this help message and exit	
@	webserver
o	-h|--help	Show this help message and exit	
o	-A|--access-logfile	The logfile to store the webserver access log. Use '-' to print to stderr	v
o	-L|--access-logformat	The access log format for gunicorn logs	v
o	-D|--daemon	Daemonize instead of running in the foreground	
o	-d|--debug	Use the server that ships with Flask in debug mode	
o	-E|--error-logfile	The logfile to store the webserver error log. Use '-' to print to stderr	v
o	-H|--hostname	Set the hostname on which to run the web server	v
o	-l|--log-file	Location of the log file	v
o	--pid	PID file location	V
o	-p|--port	The port on which to run the server	v
o	--ssl-cert	Path to the SSL certificate for the webserver	v
o	--ssl-key	Path to the key to use with the SSL certificate	v
o	--stderr	Redirect stderr to this file	v
o	--stdout	Redirect stdout to this file	v
o	-t|--worker-timeout	The timeout for waiting on webserver workers	v
o	-k|--workerclass	The worker class to use for Gunicorn	v
o	-w|--workers	Number of workers to run the webserver on	v
=	webserver	-k
v	sync	
v	eventlet	
v	gevent	
v	tornado	

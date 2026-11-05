@	
s	build	Run models, test tests, snapshot snapshots, and seed seeds
s	run	Runs the models in a project
s	debug	Debugs dbt connections and projects
s	init	Initializes a new dbt project
s	compile	Compiles (but does not run) the models in a project
s	test	Executes tests defined in a project
s	deps	Downloads dependencies for a project
s	snapshot	Executes 'snapshot' jobs defined in a project
s	clean	Deletes artifacts present in the dbt project
s	seed	Loads CSV files into the database
s	docs	Generates documentation for a project
s	source	Provides tools for working with source data (including validating that sources are 'fresh')
s	run-operation	Runs arbitrary maintenance SQL against the database
s	rpc	Runs an RPC server that clients can submit queries to
s	ls|list	Lists resources defined in a dbt project
s	parse	Parse dbt project and write detailed timing information
o	--version	Currently installed version	
o	-r|--record-timing-info	Create a new file to record timing info	v
o	-d|--debug	Redirect debug logs to standard out	
o	--log-format	Specify how dbt's logs should be formatted	v
o	--no-write-json	Prevent dbt from writing JSOn artifacts to the 'target/' directory	
o	-S|--strict	Perform extra validation of dbt objects and internal consistency checks during compilation. Use…	
o	--warn-error	Convert dbt warnings into errors	
o	--partial-parse	Configure partial parsing for your project	
o	--no-partial-parse	Turn off partial parsing for your project	
o	--use-colors	Default value -- colorize run logs	
o	--no-use-colors	Disable log colorizing	
=		--log-format
v	text	
v	json	
v	default	
@	build
o	--full-refresh	Treat incremental models as table models	
o	-x|--fail-fast	Exit immediately if a single model fails to build	
o	--profiles-dir	Set the profiles directory	v
o	--profile	Use the selected profile	v
o	--target	Target profile configuration i.e. prod/dev	v
o	--vars	Variable values to override dbt_project.yml	v
o	--threads	Number of concurrent database jobs	v
o	-s|--select	Select subset of models	v
o	--exclude	Exclude subset of models	v
o	--bypass-cache	Bypass the cache	
=	build	--profiles-dir
v	profiles	
t	folders
=	build	--profile
v	default	
=	build	--target
v	dev	
v	prod	
=	build	-s
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	build	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	run
o	--full-refresh	Treat incremental models as table models	
o	-x|--fail-fast	Exit immediately if a single model fails to build	
o	--use-colors	Default value -- colorize run logs	
o	--no-use-colors	Disable log colorizing	
o	--profiles-dir	Set the profiles directory	v
o	--profile	Select the profile to use	v
o	--target	The target profile	v
o	--vars	Variable values to override dbt_project.yml	v
o	--threads	Number of concurrent database jobs	v
o	-s|--select	Select subset of models	v
o	--exclude	Exclude subset of models	v
o	--bypass-cache	Bypass the cache	
=	run	--profiles-dir
v	profiles	
t	folders
=	run	--profile
v	default	
=	run	--target
v	dev	
v	prod	
=	run	-s
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	run	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	debug
o	--config-dir		
@	init
o	--adapter	Add an adapter	v
a	1	0
@	compile
o	--profiles-dir	Set the profiles directory	v
o	--profile	Select the profile to use	v
o	--target	The target profile	v
o	--vars	Variable values to override dbt_project.yml	v
o	--threads	Number of concurrent database jobs	v
o	--select	Select subset of models	v
o	--exclude	Exclude subset of models	v
o	--bypass-cache	Bypass the cache	
o	--selector	This flag specifies one or more named selectors, defined in a <selector name>.yml file	v
o	--defer	Defer	
=	compile	--profiles-dir
v	profiles	
t	folders
=	compile	--profile
v	default	
=	compile	--target
v	dev	
v	prod	
=	compile	--select
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	compile	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	test
o	-x|--fail-fast	Exit immediately if a single model fails to build	
o	--profiles-dir	Set the profiles directory	v
o	--profile	Select the profile to use	v
o	--data	Run only custom data tests	
o	--schema	Run only schema tests	
o	-s|--select	Select subset of models	v
o	--exclude	Exclude subset of models	v
o	--bypass-cache	Bypass the cache	
o	--selector	This flag specifies one or more named selectors, defined in a <selector name>.yml file	v
o	--defer	Defer	
=	test	--profiles-dir
v	profiles	
t	folders
=	test	--profile
v	default	
=	test	-s
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	test	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	deps
@	snapshot
o	--profiles-dir	Set the profiles directory	v
o	-x|--fail-fast	Exit immediately if a single model fails to build	
o	--profile	Select the profile to use	v
o	--target	The target profile	v
o	--vars	Variable values to override dbt_project.yml	v
o	--threads	Number of concurrent database jobs	v
o	--select	Select subset of models	v
o	--exclude	Exclude subset of models	v
o	--bypass-cache	Bypass the cache	
=	snapshot	--profiles-dir
v	profiles	
t	folders
=	snapshot	--profile
v	default	
=	snapshot	--target
v	dev	
v	prod	
=	snapshot	--select
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	snapshot	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	clean
@	seed
o	--profiles-dir	Set the profiles directory	v
o	--profile	Select the profile to use	v
o	-x|--fail-fast	Exit immediately if a single model fails to build	
o	--select	Run specific seeds	v
o	--exclude	Exclude subset of models	v
o	--bypass-cache	Bypass the cache	
o	--selector	This flag specifies one or more named selectors, defined in a <selector name>.yml file	v
=	seed	--profiles-dir
v	profiles	
t	folders
=	seed	--profile
v	default	
=	seed	--select
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	seed	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	docs
s	generate	Generate your project's documentation website
s	serve	Serve your documentation on a local webserver (default prot 8000)
@	docs generate
o	--no-compile	Skip re-compilation	
@	docs serve
o	--profiles-dir	Skip re-compilation	v
o	--profile	Choose a profile	v
o	--target	The target profile	v
o	--port	Choose a port	v
=	docs serve	--profiles-dir
t	folders
=	docs serve	--target
v	dev	
v	prod	
@	source
s	snapshot-freshness	
@	source snapshot-freshness
o	-o|--output	Override the destination for sources.json	v
o	--select	This flag specifies one or more selection-type arguments used to filter the nodes returned by the…	v
=	source snapshot-freshness	-o
t	filepaths
=	source snapshot-freshness	--select
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
@	run-operation
o	--args	Supply arguments to the macro	v
a	1	0
@	rpc
o	--host	Specify the host to listen on	v
o	--port	The port to use	v
@	ls
o	--resource-type	This flag limits the 'resource types' that dbt will return in the dbt ls command. By default, the…	v
o	-s|--select	This flag specifies one or more selection-type arguments used to filter the nodes returned by the…	v
o	--exclude	Specify selectors that should be excluded from the list of returned nodes	v
o	--selector	This flag specifies one or more named selectors, defined in a <selector name>.yml file	v
o	--output	This flag controls the format of output from the dbt ls command	v
=	ls	--resource-type
v	source	
v	analysis	
v	model	
v	snapshot	
v	test	
v	seed	
v	default	
v	all	
=	ls	-s
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	ls	--exclude
v	path:	
v	tag:	
v	config:	
v	test_type:	
v	test_name:	
=	ls	--output
v	json	
v	name	
v	path	
v	selector	
@	parse

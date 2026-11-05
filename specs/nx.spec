@	
s	init	Adds nx.json file and installs nx if not installed already
s	generate	Runs a generator that creates and/or modifies files based on a generator from a collection
s	run	Runs an Architect target with an optional custom builder configuration defined in your project
s	daemon	Prints information about the Nx Daemon process or starts a daemon process
s	graph	Graph dependencies within workspace
s	run-many	Run target for multiple listed projects
s	affected	Run target for affected projects
s	affected:graph	Graph dependencies affected by changes
s	print-affected	Prints information about the projects and targets affected by changes
s	format:check	Check for un-formatted files
s	format:write	Overwrite un-formatted files
s	migrate	Creates a migrations file or runs migrations from the migrations file
s	report	Reports useful version numbers to copy into the Nx issue template
s	list	
s	workspace-generator	Runs a workspace generator from the tools/generators directory
s	connect	Connect workspace to Nx Cloud
s	reset	Clears all the cached Nx artifacts and metadata about the workspace and shuts down the Nx Daemon
s	repair	Repair any configuration that is no longer supported by Nx
s	exec	Executes any command as if it was a target on the project
s	watch	Watch for changes within projects, and execute commands
s	show	Show information about the workspace (e.g., list of projects)
s	view-logs	Enables you to view and interact with the logs via the advanced analytic UI from Nx Cloud to help…
@	init
o	--help	Show help	
o	--version	Show version number	
@	generate
o	--defaults	When true, disables interactive input prompts for options with a default	
o	--dryRun	When true, preview the changes without updating files	
o	--force	When true, forces overwriting of existing files	
o	--help	Show help	
o	--interactive	Enable/disable prompts	
o	--version	Show version number	
a	1	0
#	generate	1
d
@	run
o	--configuration|-c	A named builder configuration, defined in the "configurations" section of the workspace…	v
o	--help	Show help	
o	--version	Show version number	
a	1	0
=	run	--configuration
d
#	run	1
d
@	daemon
o	--help	Show help	
o	--start		
o	--stop		
o	--version	Show version number	
@	graph
o	--exclude	Exclude certain projects from being processed	v
o	--file	Output file (e.g. --file=output.json or --file=dep-graph.html)	v
o	--focus	Use to show the project graph for a particular project and every node that is either an ancestor…	v
o	--groupByFolder	Group projects by folder in the project graph	
o	--help	Show help	
o	--host	Bind the project graph server to a specific ip address	v
o	--open	Open the project graph in the browser	
o	--port	Bind the project graph server to a specific port	v
o	--targets	Targets (comma/space delimited)	v
o	--version	Show version number	
o	--view	Choose whether to view the projects or task graph	v
o	--watch	Watch for changes to project graph and update in-browser	
=	graph	--exclude
d
=	graph	--focus
d
=	graph	--targets
d
=	graph	--view
v	projects	
v	tasks	
@	run-many
o	--all	All projects	
o	--configuration|-c	A named builder configuration, defined in the "configurations" section of the workspace…	v
o	--exclude	Exclude certain projects from being processed	v
o	--graph	Show the task graph of the command	
o	--help	Show help	
o	--nx-bail	Stop command execution after the first failed task	
o	--nx-ignore-cycles	Ignore cycles in the task graph	
o	--output-style	Defines how Nx emits outputs tasks logs	v
o	--parallel	Max number of parallel processes [default is 3]	v
o	--projects	Projects (comma/space delimited)	v
o	--runner	This is the name of the tasks runner configured in nx.json	v
o	--skip-nx-cache	Rerun the tasks even when the results are available in the cache	
o	--targets	Targets (comma/space delimited)	v
o	--verbose	Prints additional information about the commands (e.g., stack traces)	
o	--version	Show version number	
=	run-many	--configuration
d
=	run-many	--exclude
d
=	run-many	--output-style
v	dynamic	
v	static	
v	stream	
v	stream-without-prefixes	
v	compact	
=	run-many	--projects
d
=	run-many	--targets
d
@	affected
o	--all	All projects	
o	--base	Base of the current branch (usually main)	v
o	--configuration|-c	A named builder configuration, defined in the "configurations" section of the workspace…	v
o	--exclude	Exclude certain projects from being processed	v
o	--files	Change the way Nx is calculating the affected command by providing directly changed files, list of…	v
o	--graph	Show the task graph of the command	
o	--head	Latest commit of the current branch (usually HEAD)	v
o	--help	Show help	
o	--nx-bail	Stop command execution after the first failed task	
o	--nx-ignore-cycles	Ignore cycles in the task graph	
o	--output-style	Defines how Nx emits outputs tasks logs	v
o	--parallel	Max number of parallel processes [default is 3]	v
o	--runner	This is the name of the tasks runner configured in nx.json	v
o	--skip-nx-cache	Rerun the tasks even when the results are available in the cache	
o	--targets	Targets (comma/space delimited)	v
o	--uncommitted	Uncommitted changes	
o	--untracked	Untracked changes	
o	--verbose	Prints additional information about the commands (e.g., stack traces)	
o	--version	Show version number	
=	affected	--configuration
d
=	affected	--exclude
d
=	affected	--output-style
v	dynamic	
v	static	
v	stream	
v	stream-without-prefixes	
v	compact	
=	affected	--targets
d
@	affected:graph
o	--all	All projects	
o	--base	Base of the current branch (usually main)	v
o	--exclude	Exclude certain projects from being processed	v
o	--file	Output file (e.g. --file=output.json or --file=dep-graph.html)	v
o	--files	Change the way Nx is calculating the affected command by providing directly changed files, list of…	v
o	--focus	Use to show the project graph for a particular project and every node that is either an ancestor…	v
o	--groupByFolder	Group projects by folder in the project graph	
o	--head	Latest commit of the current branch (usually HEAD)	v
o	--help	Show help	
o	--host	Bind the project graph server to a specific ip address	v
o	--open	Open the project graph in the browser	
o	--port	Bind the project graph server to a specific port	v
o	--targets	Targets (comma/space delimited)	v
o	--uncommitted	Uncommitted changes	
o	--untracked	Untracked changes	
o	--version	Show version number	
o	--view	Choose whether to view the projects or task graph	v
o	--watch	Watch for changes to project graph and update in-browser	
=	affected:graph	--exclude
d
=	affected:graph	--focus
d
=	affected:graph	--targets
d
=	affected:graph	--view
v	projects	
v	tasks	
@	print-affected
o	--all	All projects	
o	--base	Base of the current branch (usually main)	v
o	--configuration|-c	A named builder configuration, defined in the "configurations" section of the workspace…	v
o	--exclude	Exclude certain projects from being processed	v
o	--files	Change the way Nx is calculating the affected command by providing directly changed files, list of…	v
o	--head	Latest commit of the current branch (usually HEAD)	v
o	--help	Show help	
o	--select	Select the subset of the returned json document (e.g., --select=projects)	v
o	--targets	Targets (comma/space delimited)	v
o	--type	Select the type of projects to be returned (e.g., --type=app)	v
o	--uncommitted	Uncommitted changes	
o	--untracked	Untracked changes	
o	--version	Show version number	
=	print-affected	--configuration
d
=	print-affected	--exclude
d
=	print-affected	--targets
d
=	print-affected	--type
v	app	
v	lib	
@	format:check
o	--all	All projects	
o	--base	Base of the current branch (usually main)	v
o	--exclude	Exclude certain projects from being processed	v
o	--files	Change the way Nx is calculating the affected command by providing directly changed files, list of…	v
o	--head	Latest commit of the current branch (usually HEAD)	v
o	--help	Show help	
o	--libs-and-apps	Format only libraries and applications files	
o	--projects	Projects (comma/space delimited)	v
o	--uncommitted	Uncommitted changes	
o	--untracked	Untracked changes	
o	--version	Show version number	
=	format:check	--exclude
d
=	format:check	--projects
d
@	format:write
o	--all	All projects	
o	--base	Base of the current branch (usually main)	v
o	--exclude	Exclude certain projects from being processed	v
o	--files	Change the way Nx is calculating the affected command by providing directly changed files, list of…	v
o	--head	Latest commit of the current branch (usually HEAD)	v
o	--help	Show help	
o	--libs-and-apps	Format only libraries and applications files	
o	--projects	Projects (comma/space delimited)	v
o	--uncommitted	Uncommitted changes	
o	--untracked	Untracked changes	
o	--version	Show version number	
=	format:write	--exclude
d
=	format:write	--projects
d
@	migrate
o	--commitPrefix	Commit prefix to apply to the commit for each migration, when --create-commits is enabled	v
o	--createCommits	Automatically create a git commit after each migration runs	
o	--excludeAppliedMigrations	Exclude migrations that should have been applied on previous updates. To be used with --from	
o	--from	Use the provided versions for packages instead of the ones installed in node_modules (e.g…	v
o	--help	Show help	
o	--ifExists	Run migrations only if the migrations file exists, if not continues successfully	
o	--interactive	Enable/disable prompts	
o	--runMigrations	Execute migrations from a file (when the file isn't provided, execute migrations from…	v
o	--to	Use the provided versions for packages instead of the ones calculated by the migrator (e.g…	v
o	--version	Show version number	
a	1	0
#	migrate	1
v	latest	
@	report
o	--help	Show help	
o	--version	Show version number	
@	list
o	--help	Show help	
o	--version	Show version number	
a	1	0
#	list	1
d
@	workspace-generator
o	--help	Show help	
o	--list-generators	List the available workspace-generators	
o	--version	Show version number	
a	1	0
#	workspace-generator	1
d
@	connect
o	--help	Show help	
o	--version	Show version number	
@	reset
o	--help	Show help	
o	--version	Show version number	
@	repair
o	--help	Show help	
o	--verbose	Prints additional information about the commands (e.g., stack traces)	
o	--version	Show version number	
@	exec
o	--configuration|-c	A named builder configuration, defined in the "configurations" section of the workspace…	v
o	--exclude	Exclude certain projects from being processed	v
o	--graph	Show the task graph of the command	
o	--help	Show help	
o	--nx-bail	Stop command execution after the first failed task	
o	--nx-ignore-cycles	Ignore cycles in the task graph	
o	--output-style	Defines how Nx emits outputs tasks logs	v
o	--parallel	Max number of parallel processes [default is 3]	v
o	--project	Target project	v
o	--runner	This is the name of the tasks runner configured in nx.json	v
o	--skip-nx-cache	Rerun the tasks even when the results are available in the cache	
o	--verbose	Prints additional information about the commands (e.g., stack traces)	
o	--version	Show version number	
=	exec	--configuration
d
=	exec	--exclude
d
=	exec	--output-style
v	dynamic	
v	static	
v	stream	
v	stream-without-prefixes	
v	compact	
=	exec	--project
d
@	watch
o	--all	All projects	
o	--help	Show help	
o	--includeDependentProjects	When watching selected projects, include dependent projects as well	
o	--projects	Projects (comma/space delimited)	v
o	--verbose	Prints additional information about the commands (e.g., stack traces)	
o	--version	Show version number	
=	watch	--projects
d
@	show
o	--help	Show help	
o	--version	Show version number	
a	1	0
#	show	1
v	projects	
@	view-logs
o	--help	Show help	
o	--version	Show version number	

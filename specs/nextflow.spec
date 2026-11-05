@	
s	clean	Clean up project cache and work directories (Default: last run)
s	clone	Clone a project into a folder
s	config	Print a project configuration
s	console	Launch Nextflow interactive console
s	drop	Delete the local copy of a project
s	help	Print the usage help for a command
s	info	Print project and system runtime information
s	kuberun	Execute a workflow in a Kubernetes cluster (experimental)
s	list	List all downloaded projects
s	log	Print executions log and runtime info
s	pull	Download or update a project
s	run	Execute a pipeline project
s	secrets	Handle and manage sensitive information for pipeline execution in a safe manner
s	self-update	Update nextflow runtime to the latest available version
s	view	View project script file(s)
o	-C	Use the specified configuration file(s) overriding any defaults	v
o	-D	Set JVM properties	v
o	-bg	Execute nextflow in background	
o	-c|-config	Add the specified file to configuration set	v
o	-d|-dockerize	Launch nextflow via Docker (experimental)	
o	-h	Print this help	
o	-log	Set nextflow log file path	
o	-q|-quiet	Do not print information messages	
o	-syslog	Send logs to syslog server (eg. localhost:514)	
o	-v|-version	Print the program version	
=		-C
t	filepaths
=		-c
t	filepaths
@	clean
o	-after	Clean up runs executed after the specified one	v
o	-before	Clean up runs executed before the specified one	v
o	-but	Clean up all runs except the specified one	v
o	-n|-dry-run	Print names of file to be removed without deleting them (Default: false)	
o	-f|-force	Force clean command (Default: false)	
o	-h|-help	Print the command usage (Default: false)	
o	-k|-keep-logs	Removes only temporary files but retains execution log entries and metadata (Default: false)	
o	-q|-quiet	Do not print names of files removed (Default: false)	
a	1	0
=	clean	-after
d
=	clean	-before
d
=	clean	-but
d
#	clean	1
d
@	clone
o	-h|-help	Print the command usage (Default: false)	
o	-hub	Service hub where the project is hosted (Default: GitHub)	v
o	-r	Revision to clone - It can be a git branch, tag or revision number	v
o	-user	Private repository user name	v
a	1	0
@	config
o	-flat	Print config using flat notation (Default: false)	
o	-h|-help	Print the command usage (Default: false)	
o	-profile	Choose a configuration profile	
o	-properties	Prints config using Java properties notatio (Default: false)	
o	-a|-show-profiles	Show all configuration profiles	
o	-sort	Sort config attributes (Default: false)	
a	1	0
#	config	1
d
@	console
o	-h|-help	Print the command usage (Default: false)	
@	drop
o	-h|-help	Print the command usage (Default: false)	
o	-f	Delete the repository without taking care of local changes (Default: false)	
a	1	0
#	drop	1
d
@	help
o	-h|-help	Print the command usage (Default: false)	
@	info
o	-u|-check-updates	Check for remote updates (Default: false)	
o	-d	Show detailed information (Default: false)	
o	-h|-help	Print the command usage (Default: false)	
o	-o	Output format, either: text (default), json, yaml	
a	1	0
#	info	1
d
@	kuberun
o	-E	Exports all current system environment (Default: false)	
o	-ansi-log	Enable/disable ANSI console logging	
o	-bucket-dir	Remote bucket where intermediate result files are stored	v
o	-cache	Enable/disable processes caching	
o	-disable-jobs-cancellation	Prevent the cancellation of child jobs on execution termination	
o	-dsl1	Execute the workflow using DSL1 syntax (Default: false)	
o	-dsl2	Execute the workflow using DSL2 syntax (Default: false)	
o	-dump-channels	Dump channels for debugging purpose	
o	-dump-hashes	Dump task hash keys for debugging purpose (Default: false)	
o	-e	Add the specified variable to execution environment. Syntax: -e.key=value (Default: {})	v
o	-entry	Entry workflow name to be executed	v
o	-head-cpus	Specify number of CPUs requested for the Nextflow pod (Default: 0)	
o	-head-memory	Specify amount of memory requested for the Nextflow pod	
o	-h|-help	Print the command usage (Default: false)	
o	-hub	Service hub where the project is hosted (Default: github)	v
o	-latest	Pull latest changes before run (Default: false)	
o	-lib	Library extension path	v
o	-main-script	The script file to be executed when launching a project directory or repository	v
o	-name	Assign a mnemonic name to the a pipeline run	v
o	-n|-namespace	Specify the K8s namespace to use	
o	-offline	Do not check for remote project updates (Default: false)	
o	-params-file	Load script parameters from a JSON/YAML file	v
o	-plugins	Specify the plugins to be applied for this run e.g. nf-amazon,nf-tower	v
o	-pod-image	Specify the container image for the Nextflow pod	
o	-process	Set process options. Syntax: -process.key=value (Default: {}	v
o	-profile	Choose a configuration profile	v
o	-qs|-queue-size	Max number of processes that can be executed in parallel by each executor	v
o	-remoteProfile	Choose a configuration profile in the remoteConfig	
o	-resume	Execute the script using the cached results, useful to continue executions that was stopped by an…	
o	-r|-revision	Revision of the project to run (either a git branch, tag or commit SHA number)	v
o	-stub-run|-stub	Execute the workflow replacing process scripts with command stubs (Default: false)	
o	-test	Test a script function with the name specified	v
o	-user	Private repository user name	v
o	-v|-volume-mount	Volume claim mounts eg. my-pvc:/mnt/path	
o	-with-charliecloud	Enable process execution in a Charliecloud container runtime	
o	-with-conda	Use the specified Conda environment package or file (must end with .yml|.yaml suffix)	v
o	-with-dag	Create pipeline DAG file	v
o	-with-docker	Enable process execution in a Docker container	V
o	-N|-with-notification	Send a notification email on workflow completion to the specified recipients	v
o	-with-podman	Enable process execution in a Podman container	
o	-with-report	Create processes execution html report	v
o	-with-singularity	Enable process execution in a Singularity container	
o	-with-timeline	Create processes execution timeline file	v
o	-with-tower	Monitor workflow execution with Seqera Tower service	
o	-with-trace	Create processes execution tracing file	v
o	-with-weblog	Send workflow status messages via HTTP to target URL	v
o	-without-docker	Disable process execution with Docker (Default: false)	
o	-without-podman	Disable process execution in a Podman container	
o	-w|-work-dir	Directory where intermediate result files are stored	v
a	1	0
=	kuberun	-params-file
t	filepaths
=	kuberun	-with-docker
d
#	kuberun	1
d
@	list
o	-h|-help	Print the command usage (Default: false)	
@	log
o	-after	Show log entries for runs executed after the specified one	v
o	-before	Show log entries for runs executed before the specified one	v
o	-but	Show log entries of all runs except the specified one	v
o	-f|-fields	Comma separated list of fields to include in the printed log -- Use the `-l` option to show the…	v
o	-F|filter	Filter log entries by a custom expression e.g. process =~ /foo.*/ && status == 'COMPLETED'	v
o	-h|-help	Print the command usage (Default: false)	
o	-l|-list-fields	Show all available fields (Default: false)	
o	-q|-quiet	Show only run names (Default: false)	
o	-s	Character used to separate column values (Default: )	v
o	-t|-template	Text template used to each record in the log	v
a	1	0
=	log	-after
d
=	log	-before
d
=	log	-but
d
#	log	1
d
@	pull
o	-all	Update all downloaded projects (Default: false)	
o	-h|-help	Print the command usage (Default: false)	
o	-hub	Service hub where the project is hosted	
o	-r|-revision	Revision of the project to run (either a git branch, tag or commit SHA number)	
o	-user	Private repository user name	
a	1	0
#	pull	1
d
@	run
o	-E	Exports all current system environment (Default: false)	
o	-ansi-log	Enable/disable ANSI console logging	
o	-bucket-dir	Remote bucket where intermediate result files are stored	v
o	-cache	Enable/disable processes caching	
o	-disable-jobs-cancellation	Prevent the cancellation of child jobs on execution termination	
o	-dsl1	Execute the workflow using DSL1 syntax (Default: false)	
o	-dsl2	Execute the workflow using DSL2 syntax (Default: false)	
o	-dump-channels	Dump channels for debugging purpose	
o	-dump-hashes	Dump task hash keys for debugging purpose (Default: false)	
o	-e.	Add the specified variable to execution environment. Syntax: -e.key=value (Default: {})	v
o	-entry	Entry workflow name to be executed	v
o	-h|-help	Print the command usage (Default: false)	
o	-hub	Service hub where the project is hosted (Default: github)	v
o	-latest	Pull latest changes before run (Default: false)	
o	-lib	Library extension path	v
o	-main-script	The script file to be executed when launching a project directory or repository	v
o	-name	Assign a mnemonic name to the a pipeline run	v
o	-offline	Do not check for remote project updates (Default: false)	
o	-params-file	Load script parameters from a JSON/YAML file	v
o	-plugins	Specify the plugins to be applied for this run e.g. nf-amazon,nf-tower	v
o	-process.	Set process options. Syntax: -process.key=value (Default: {}	v
o	-profile	Choose a configuration profile	v
o	-qs|-queue-size	Max number of processes that can be executed in parallel by each executor	v
o	-resume	Execute the script using the cached results, useful to continue executions that was stopped by an…	V
o	-r|-revision	Revision of the project to run (either a git branch, tag or commit SHA number)	v
o	-stub-ru|-stub	Execute the workflow replacing process scripts with command stubs (Default: false)	
o	-test	Test a script function with the name specified	v
o	-user	Private repository user name	v
o	-with-charliecloud	Enable process execution in a Charliecloud container runtime	
o	-with-conda	Use the specified Conda environment package or file (must end with .yml|.yaml suffix)	v
o	-with-dag	Create pipeline DAG file	v
o	-with-docker	Enable process execution in a Docker container	V
o	-N|-with-notification	Send a notification email on workflow completion to the specified recipients	v
o	-with-podman	Enable process execution in a Podman container	
o	-with-report	Create processes execution html report	v
o	-with-singularity	Enable process execution in a Singularity container	
o	-with-timeline	Create processes execution timeline file	v
o	-with-tower	Monitor workflow execution with Seqera Tower service	
o	-with-trace	Create processes execution tracing file	v
o	-with-weblog	Send workflow status messages via HTTP to target URL	v
o	-without-docker	Disable process execution with Docker (Default: false)	
o	-without-podman	Disable process execution in a Podman container	
o	-w|-work-dir	Directory where intermediate result files are stored	v
a	1	0
=	run	-params-file
t	filepaths
=	run	-resume
d
=	run	-with-docker
d
#	run	1
d
@	secrets
o	list	List secrets available in the current store e.g. nextflow secrets list	
o	get	Allows retrieving a secret value e.g. nextflow secrets get FOO	v
o	set	Allows creating creating a new secret or overriding an existing one e.g. nextflow secrets set FOO…	v
o	delete	Allows deleting an existing secret e.g. nextflow secrets delete FOO	v
=	secrets	get
d
=	secrets	set
d
=	secrets	delete
d
@	self-update
o	-h|-help	Print the command usage (Default: false)	
@	view
o	-h|-help	Print the command usage (Default: false)	
o	-l	List repository content (Default: false)	
o	-q	Hide header line (Default: false)	
a	1	0
#	view	1
d

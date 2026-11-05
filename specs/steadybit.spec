@	
s	config	Show/modify the CLI configuration and authentication profiles
s	def-repo	Change versions and verify a task/policy definition repository state
s	service|service-definition	Configure or verify service definitions
o	--help|-h	Display usage information	
@	config
s	show	Show the active CLI configuration. Warning: Prints secrets!
s	profile	Configure authentication profiles
@	config show
@	config profile
s	add	Interactively configure a new profile
s	list|ls	List all configured profiles
s	remove	Interactively remove an existing profile
s	select	Interactively change the currently active profile
@	config profile add
@	config profile list
@	config profile remove
@	config profile select
@	def-repo
s	set-version	Set the versions in policies and task references
s	check	Checks that the tasks and policies are valid
@	def-repo set-version
o	-v|--version	Version to set	v
o	-d|--directory	The directory to search for task and policy files	v
=	def-repo set-version	-d
t	folders
@	def-repo check
o	-v|--version	The version to check	v
o	-d|--directory	The directory to search for task and policy files	v
=	def-repo check	-d
t	folders
@	service
s	apply	Upload a service definition
s	delete	Delete a service definition
s	init	Initialize a service definition file
s	open	Open the service in the Steadybit UI
s	verify	Read the current service definition and state
s	show	Show a list of tasks and policies referenced by this service
@	service apply
o	-f|--file	Path to the service definition file	v
=	service apply	-f
t	filepaths
@	service delete
o	-f|--file	Path to the service definition file	v
o	-i|--id	ID of the service definition to delete	v
=	service delete	-f
t	filepaths
@	service init
@	service open
o	-f|--file	Path to the service definition file	v
=	service open	-f
t	filepaths
@	service verify
o	-f|--file	Path to the service definition file	v
o	-pp|--print-parameters	Print task parameters when listing tasks	
o	-pm|--print-matrix-context	Print the matrix execution context information when listing tasks	
=	service verify	-f
t	filepaths
@	service show
o	-f|--file	Path to the service definition file	v
o	-n|--name	Optional task name to filter the result list	v
o	-v|--version	Optional task version to filter the result list	v
=	service show	-f
t	filepaths

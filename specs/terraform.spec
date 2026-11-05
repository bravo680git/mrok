@	
s	init	Prepare your working directory for other commands
s	validate	Check whether the configuration is valid
s	plan	Show changes required by the current configuration
s	apply	Create or update infrastructure
s	destroy	Destroy previously-created infrastructure
s	console	Try Terraform expressions at an interactive command prompt
s	fmt	Reformat your configuration in the standard style
s	force-unlock	Release a stuck lock on the current workspace
s	get	Install or upgrade remote Terraform modules
s	graph	Generate a Graphviz graph of the steps in an operation
s	import	Associate existing infrastructure with a Terraform resource
s	login	Obtain and save credentials for a remote hos
s	logout	Remove locally-stored credentials for a remote host
s	output	Show output values from your root module
s	providers	Show the providers required for this configuration
s	refresh	Update the state to match remote systems
s	show	Show the current state or a saved plan
s	state	Advanced state management
s	taint	Mark a resource instance as not fully functional
s	untaint	Remove the 'tainted' state from a resource instance
s	workspace	Workspace management
s	-install-autocomplete	Install bash/zsh tab completion
s	-uninstall-autocomplete	Uninstall bash/zsh tab completion
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=		-chdir
t	filepaths
@	init
o	-upgrade	Opt to upgrade modules and plugins as part of their respective installation steps	
o	-lock	Lock the state file when locking is supported. Defaults to true	v=
o	-force	Delete the workspace even if its state is not empty. Defaults to false	v=
o	-lock-timeout	Duration to retry a state lock. Default 0s	v=
o	-input	Ask for input for variables if not directly set	v=
o	-no-color	Disables output with coloring	
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	init	-lock
v	true	
v	false	
=	init	-force
v	true	
v	false	
=	init	-input
v	true	
v	false	
=	init	-chdir
t	filepaths
@	validate
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	validate	-chdir
t	filepaths
@	plan
o	-compact-warnings	If Terraform produces any warnings that are not accompanied by errors, show them in a more compact…	
o	-destroy	If set, generates a plan to destroy all the known resources	
o	-detailed-exitcode	Return a detailed exit code when the command exits	
o	-out	The path to save the generated execution plan	=
o	-parallelism	Limit the number of concurrent operation as Terraform walks the graph. Defaults to 10	v
o	-refresh	Update the state prior to checking for differences	v=
o	-state	Path to the state file. Defaults to 'terraform.tfstate'. Ignored when remote state is used	v=
o	-target	A Resource Address to target. This flag can be used multiple times	
o	-var	Set a variable in the Terraform configuration. This flag can be set multiple times	v
o	-var-file	Set variables in the Terraform configuration from a variable file	v=
o	-lock	Lock the state file when locking is supported. Defaults to true	v=
o	-force	Delete the workspace even if its state is not empty. Defaults to false	v=
o	-lock-timeout	Duration to retry a state lock. Default 0s	v=
o	-input	Ask for input for variables if not directly set	v=
o	-no-color	Disables output with coloring	
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	plan	-refresh
v	true	
v	false	
=	plan	-state
t	filepaths
=	plan	-var-file
t	filepaths
=	plan	-lock
v	true	
v	false	
=	plan	-force
v	true	
v	false	
=	plan	-input
v	true	
v	false	
=	plan	-chdir
t	filepaths
@	apply
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	apply	-chdir
t	filepaths
@	destroy
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	destroy	-chdir
t	filepaths
@	console
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	console	-chdir
t	filepaths
@	fmt
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	fmt	-chdir
t	filepaths
@	force-unlock
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	force-unlock	-chdir
t	filepaths
@	get
o	-update	If specified, modules that are already downloaded will be checked for updates and the updates will…	
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	get	-chdir
t	filepaths
@	graph
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	graph	-chdir
t	filepaths
@	import
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	import	-chdir
t	filepaths
@	login
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	login	-chdir
t	filepaths
@	logout
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	logout	-chdir
t	filepaths
@	output
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	output	-chdir
t	filepaths
@	providers
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	providers	-chdir
t	filepaths
@	refresh
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	refresh	-chdir
t	filepaths
@	show
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	show	-chdir
t	filepaths
@	state
@	taint
o	-allow-missing	If specified, the command will succeed (exit code 0) even if the resource is missing. The command…	
o	-lock	Disables Terraform's default behavior of attempting to take a read/write lock on the state for the…	v=
o	-lock-timeout	Unless locking is disabled with -lock=false, instructs Terraform to retry acquiring a lock for a…	v=
o	-ignore-remote-version	When using the enhanced remote backend with Terraform Cloud, continue even if remote and local…	v
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
a	1	0
=	taint	-lock
v	true	
v	false	
=	taint	-chdir
t	filepaths
#	taint	1
d
@	untaint
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	untaint	-chdir
t	filepaths
@	workspace
s	new	Create a new workspace
s	show	Display the current workspace
s	list	List the workspace
s	delete	Delete the specified workspace
s	select	Change the current working workspace
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	workspace	-chdir
t	filepaths
@	workspace new
o	-lock	Lock the state file when locking is supported. Defaults to true	v
o	-lock-timeout	Duration to retry a stae lock. Default 0s	v
o	-state	Path to an existing state file to initialize the state of this environment	v=
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
a	1	0
=	workspace new	-lock
v	true	
v	false	
=	workspace new	-state
t	filepaths
=	workspace new	-chdir
t	filepaths
@	workspace show
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	workspace show	-chdir
t	filepaths
@	workspace list
o	-help	Show this help output, or the help for a specified subcommand	
o	-chdir	Switch to a different working directory before executing the given subcommand	v=
o	-version	Show the current Terraform version	
=	workspace list	-chdir
t	filepaths
@	workspace delete
o	-lock	Lock the state file when locking is supported. Defaults to true	v=
o	-force	Delete the workspace even if its state is not empty. Defaults to false	v=
o	-lock-timeout	Duration to retry a state lock. Default 0s	v=
o	-input	Ask for input for variables if not directly set	v=
o	-no-color	Disables output with coloring	
a	1	0
=	workspace delete	-lock
v	true	
v	false	
=	workspace delete	-force
v	true	
v	false	
=	workspace delete	-input
v	true	
v	false	
#	workspace delete	1
d
@	workspace select
a	1	0
#	workspace select	1
d
@	-install-autocomplete
@	-uninstall-autocomplete

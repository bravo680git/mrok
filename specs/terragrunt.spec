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
s	run-all	Run a terraform command against a 'stack' by running the specified command in each subfolder…
s	terragrunt-info	Emits limited terragrunt state on stdout and exits
s	validate-inputs	Checks if the terragrunt configured inputs align with the terraform defined variables
s	graph-dependencies	Prints the terragrunt dependency graph to stdout
s	hclfmt	Recursively find hcl files and rewrite them into a canonical format
s	aws-provider-patch	Overwrite settings on nested AWS providers to work around a Terraform bug (issue #13018)
s	render-json	Render the final terragrunt config, with all variables, includes, and functions resolved, as json…
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=		--terragrunt-config
t	filepaths
=		--terragrunt-tfpath
t	filepaths
=		--terragrunt-working-dir
t	folders
=		--terragrunt-download-dir
t	folders
=		--terragrunt-source
t	folders
=		--terragrunt-exclude-dir
t	folders
=		--terragrunt-include-dir
t	folders
=		--terragrunt-hclfmt-file
t	filepaths
=		--terragrunt-json-out
t	filepaths
=		--terragrunt-modules-that-include
t	filepaths
@	init
o	-upgrade	Opt to upgrade modules and plugins as part of their respective installation steps	
o	-lock	Lock the state file when locking is supported. Defaults to true	v=
o	-force	Delete the workspace even if its state is not empty. Defaults to false	v=
o	-lock-timeout	Duration to retry a state lock. Default 0s	v=
o	-input	Ask for input for variables if not directly set	v=
o	-no-color	Disables output with coloring	
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	init	-lock
v	true	
v	false	
=	init	-force
v	true	
v	false	
=	init	-input
v	true	
v	false	
=	init	--terragrunt-config
t	filepaths
=	init	--terragrunt-tfpath
t	filepaths
=	init	--terragrunt-working-dir
t	folders
=	init	--terragrunt-download-dir
t	folders
=	init	--terragrunt-source
t	folders
=	init	--terragrunt-exclude-dir
t	folders
=	init	--terragrunt-include-dir
t	folders
=	init	--terragrunt-hclfmt-file
t	filepaths
=	init	--terragrunt-json-out
t	filepaths
=	init	--terragrunt-modules-that-include
t	filepaths
@	validate
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	validate	--terragrunt-config
t	filepaths
=	validate	--terragrunt-tfpath
t	filepaths
=	validate	--terragrunt-working-dir
t	folders
=	validate	--terragrunt-download-dir
t	folders
=	validate	--terragrunt-source
t	folders
=	validate	--terragrunt-exclude-dir
t	folders
=	validate	--terragrunt-include-dir
t	folders
=	validate	--terragrunt-hclfmt-file
t	filepaths
=	validate	--terragrunt-json-out
t	filepaths
=	validate	--terragrunt-modules-that-include
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
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
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
=	plan	--terragrunt-config
t	filepaths
=	plan	--terragrunt-tfpath
t	filepaths
=	plan	--terragrunt-working-dir
t	folders
=	plan	--terragrunt-download-dir
t	folders
=	plan	--terragrunt-source
t	folders
=	plan	--terragrunt-exclude-dir
t	folders
=	plan	--terragrunt-include-dir
t	folders
=	plan	--terragrunt-hclfmt-file
t	filepaths
=	plan	--terragrunt-json-out
t	filepaths
=	plan	--terragrunt-modules-that-include
t	filepaths
@	apply
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	apply	--terragrunt-config
t	filepaths
=	apply	--terragrunt-tfpath
t	filepaths
=	apply	--terragrunt-working-dir
t	folders
=	apply	--terragrunt-download-dir
t	folders
=	apply	--terragrunt-source
t	folders
=	apply	--terragrunt-exclude-dir
t	folders
=	apply	--terragrunt-include-dir
t	folders
=	apply	--terragrunt-hclfmt-file
t	filepaths
=	apply	--terragrunt-json-out
t	filepaths
=	apply	--terragrunt-modules-that-include
t	filepaths
@	destroy
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	destroy	--terragrunt-config
t	filepaths
=	destroy	--terragrunt-tfpath
t	filepaths
=	destroy	--terragrunt-working-dir
t	folders
=	destroy	--terragrunt-download-dir
t	folders
=	destroy	--terragrunt-source
t	folders
=	destroy	--terragrunt-exclude-dir
t	folders
=	destroy	--terragrunt-include-dir
t	folders
=	destroy	--terragrunt-hclfmt-file
t	filepaths
=	destroy	--terragrunt-json-out
t	filepaths
=	destroy	--terragrunt-modules-that-include
t	filepaths
@	console
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	console	--terragrunt-config
t	filepaths
=	console	--terragrunt-tfpath
t	filepaths
=	console	--terragrunt-working-dir
t	folders
=	console	--terragrunt-download-dir
t	folders
=	console	--terragrunt-source
t	folders
=	console	--terragrunt-exclude-dir
t	folders
=	console	--terragrunt-include-dir
t	folders
=	console	--terragrunt-hclfmt-file
t	filepaths
=	console	--terragrunt-json-out
t	filepaths
=	console	--terragrunt-modules-that-include
t	filepaths
@	fmt
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	fmt	--terragrunt-config
t	filepaths
=	fmt	--terragrunt-tfpath
t	filepaths
=	fmt	--terragrunt-working-dir
t	folders
=	fmt	--terragrunt-download-dir
t	folders
=	fmt	--terragrunt-source
t	folders
=	fmt	--terragrunt-exclude-dir
t	folders
=	fmt	--terragrunt-include-dir
t	folders
=	fmt	--terragrunt-hclfmt-file
t	filepaths
=	fmt	--terragrunt-json-out
t	filepaths
=	fmt	--terragrunt-modules-that-include
t	filepaths
@	force-unlock
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	force-unlock	--terragrunt-config
t	filepaths
=	force-unlock	--terragrunt-tfpath
t	filepaths
=	force-unlock	--terragrunt-working-dir
t	folders
=	force-unlock	--terragrunt-download-dir
t	folders
=	force-unlock	--terragrunt-source
t	folders
=	force-unlock	--terragrunt-exclude-dir
t	folders
=	force-unlock	--terragrunt-include-dir
t	folders
=	force-unlock	--terragrunt-hclfmt-file
t	filepaths
=	force-unlock	--terragrunt-json-out
t	filepaths
=	force-unlock	--terragrunt-modules-that-include
t	filepaths
@	get
o	-update	If specified, modules that are already downloaded will be checked for updates and the updates will…	
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	get	--terragrunt-config
t	filepaths
=	get	--terragrunt-tfpath
t	filepaths
=	get	--terragrunt-working-dir
t	folders
=	get	--terragrunt-download-dir
t	folders
=	get	--terragrunt-source
t	folders
=	get	--terragrunt-exclude-dir
t	folders
=	get	--terragrunt-include-dir
t	folders
=	get	--terragrunt-hclfmt-file
t	filepaths
=	get	--terragrunt-json-out
t	filepaths
=	get	--terragrunt-modules-that-include
t	filepaths
@	graph
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	graph	--terragrunt-config
t	filepaths
=	graph	--terragrunt-tfpath
t	filepaths
=	graph	--terragrunt-working-dir
t	folders
=	graph	--terragrunt-download-dir
t	folders
=	graph	--terragrunt-source
t	folders
=	graph	--terragrunt-exclude-dir
t	folders
=	graph	--terragrunt-include-dir
t	folders
=	graph	--terragrunt-hclfmt-file
t	filepaths
=	graph	--terragrunt-json-out
t	filepaths
=	graph	--terragrunt-modules-that-include
t	filepaths
@	import
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	import	--terragrunt-config
t	filepaths
=	import	--terragrunt-tfpath
t	filepaths
=	import	--terragrunt-working-dir
t	folders
=	import	--terragrunt-download-dir
t	folders
=	import	--terragrunt-source
t	folders
=	import	--terragrunt-exclude-dir
t	folders
=	import	--terragrunt-include-dir
t	folders
=	import	--terragrunt-hclfmt-file
t	filepaths
=	import	--terragrunt-json-out
t	filepaths
=	import	--terragrunt-modules-that-include
t	filepaths
@	login
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	login	--terragrunt-config
t	filepaths
=	login	--terragrunt-tfpath
t	filepaths
=	login	--terragrunt-working-dir
t	folders
=	login	--terragrunt-download-dir
t	folders
=	login	--terragrunt-source
t	folders
=	login	--terragrunt-exclude-dir
t	folders
=	login	--terragrunt-include-dir
t	folders
=	login	--terragrunt-hclfmt-file
t	filepaths
=	login	--terragrunt-json-out
t	filepaths
=	login	--terragrunt-modules-that-include
t	filepaths
@	logout
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	logout	--terragrunt-config
t	filepaths
=	logout	--terragrunt-tfpath
t	filepaths
=	logout	--terragrunt-working-dir
t	folders
=	logout	--terragrunt-download-dir
t	folders
=	logout	--terragrunt-source
t	folders
=	logout	--terragrunt-exclude-dir
t	folders
=	logout	--terragrunt-include-dir
t	folders
=	logout	--terragrunt-hclfmt-file
t	filepaths
=	logout	--terragrunt-json-out
t	filepaths
=	logout	--terragrunt-modules-that-include
t	filepaths
@	output
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	output	--terragrunt-config
t	filepaths
=	output	--terragrunt-tfpath
t	filepaths
=	output	--terragrunt-working-dir
t	folders
=	output	--terragrunt-download-dir
t	folders
=	output	--terragrunt-source
t	folders
=	output	--terragrunt-exclude-dir
t	folders
=	output	--terragrunt-include-dir
t	folders
=	output	--terragrunt-hclfmt-file
t	filepaths
=	output	--terragrunt-json-out
t	filepaths
=	output	--terragrunt-modules-that-include
t	filepaths
@	providers
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	providers	--terragrunt-config
t	filepaths
=	providers	--terragrunt-tfpath
t	filepaths
=	providers	--terragrunt-working-dir
t	folders
=	providers	--terragrunt-download-dir
t	folders
=	providers	--terragrunt-source
t	folders
=	providers	--terragrunt-exclude-dir
t	folders
=	providers	--terragrunt-include-dir
t	folders
=	providers	--terragrunt-hclfmt-file
t	filepaths
=	providers	--terragrunt-json-out
t	filepaths
=	providers	--terragrunt-modules-that-include
t	filepaths
@	refresh
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	refresh	--terragrunt-config
t	filepaths
=	refresh	--terragrunt-tfpath
t	filepaths
=	refresh	--terragrunt-working-dir
t	folders
=	refresh	--terragrunt-download-dir
t	folders
=	refresh	--terragrunt-source
t	folders
=	refresh	--terragrunt-exclude-dir
t	folders
=	refresh	--terragrunt-include-dir
t	folders
=	refresh	--terragrunt-hclfmt-file
t	filepaths
=	refresh	--terragrunt-json-out
t	filepaths
=	refresh	--terragrunt-modules-that-include
t	filepaths
@	show
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	show	--terragrunt-config
t	filepaths
=	show	--terragrunt-tfpath
t	filepaths
=	show	--terragrunt-working-dir
t	folders
=	show	--terragrunt-download-dir
t	folders
=	show	--terragrunt-source
t	folders
=	show	--terragrunt-exclude-dir
t	folders
=	show	--terragrunt-include-dir
t	folders
=	show	--terragrunt-hclfmt-file
t	filepaths
=	show	--terragrunt-json-out
t	filepaths
=	show	--terragrunt-modules-that-include
t	filepaths
@	state
@	taint
o	-allow-missing	If specified, the command will succeed (exit code 0) even if the resource is missing. The command…	
o	-lock	Disables Terraform's default behavior of attempting to take a read/write lock on the state for the…	v=
o	-lock-timeout	Unless locking is disabled with -lock=false, instructs Terraform to retry acquiring a lock for a…	v=
o	-ignore-remote-version	When using the enhanced remote backend with Terraform Cloud, continue even if remote and local…	v
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
a	1	0
=	taint	-lock
v	true	
v	false	
=	taint	--terragrunt-config
t	filepaths
=	taint	--terragrunt-tfpath
t	filepaths
=	taint	--terragrunt-working-dir
t	folders
=	taint	--terragrunt-download-dir
t	folders
=	taint	--terragrunt-source
t	folders
=	taint	--terragrunt-exclude-dir
t	folders
=	taint	--terragrunt-include-dir
t	folders
=	taint	--terragrunt-hclfmt-file
t	filepaths
=	taint	--terragrunt-json-out
t	filepaths
=	taint	--terragrunt-modules-that-include
t	filepaths
#	taint	1
d
@	untaint
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	untaint	--terragrunt-config
t	filepaths
=	untaint	--terragrunt-tfpath
t	filepaths
=	untaint	--terragrunt-working-dir
t	folders
=	untaint	--terragrunt-download-dir
t	folders
=	untaint	--terragrunt-source
t	folders
=	untaint	--terragrunt-exclude-dir
t	folders
=	untaint	--terragrunt-include-dir
t	folders
=	untaint	--terragrunt-hclfmt-file
t	filepaths
=	untaint	--terragrunt-json-out
t	filepaths
=	untaint	--terragrunt-modules-that-include
t	filepaths
@	workspace
s	new	Create a new workspace
s	show	Display the current workspace
s	list	List the workspace
s	delete	Delete the specified workspace
s	select	Change the current working workspace
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	workspace	--terragrunt-config
t	filepaths
=	workspace	--terragrunt-tfpath
t	filepaths
=	workspace	--terragrunt-working-dir
t	folders
=	workspace	--terragrunt-download-dir
t	folders
=	workspace	--terragrunt-source
t	folders
=	workspace	--terragrunt-exclude-dir
t	folders
=	workspace	--terragrunt-include-dir
t	folders
=	workspace	--terragrunt-hclfmt-file
t	filepaths
=	workspace	--terragrunt-json-out
t	filepaths
=	workspace	--terragrunt-modules-that-include
t	filepaths
@	workspace new
o	-lock	Lock the state file when locking is supported. Defaults to true	v
o	-lock-timeout	Duration to retry a stae lock. Default 0s	v
o	-state	Path to an existing state file to initialize the state of this environment	v=
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
a	1	0
=	workspace new	-lock
v	true	
v	false	
=	workspace new	-state
t	filepaths
=	workspace new	--terragrunt-config
t	filepaths
=	workspace new	--terragrunt-tfpath
t	filepaths
=	workspace new	--terragrunt-working-dir
t	folders
=	workspace new	--terragrunt-download-dir
t	folders
=	workspace new	--terragrunt-source
t	folders
=	workspace new	--terragrunt-exclude-dir
t	folders
=	workspace new	--terragrunt-include-dir
t	folders
=	workspace new	--terragrunt-hclfmt-file
t	filepaths
=	workspace new	--terragrunt-json-out
t	filepaths
=	workspace new	--terragrunt-modules-that-include
t	filepaths
@	workspace show
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	workspace show	--terragrunt-config
t	filepaths
=	workspace show	--terragrunt-tfpath
t	filepaths
=	workspace show	--terragrunt-working-dir
t	folders
=	workspace show	--terragrunt-download-dir
t	folders
=	workspace show	--terragrunt-source
t	folders
=	workspace show	--terragrunt-exclude-dir
t	folders
=	workspace show	--terragrunt-include-dir
t	folders
=	workspace show	--terragrunt-hclfmt-file
t	filepaths
=	workspace show	--terragrunt-json-out
t	filepaths
=	workspace show	--terragrunt-modules-that-include
t	filepaths
@	workspace list
o	-h|--help	Show this help output, or the help for a specified subcommand	
o	-v|--version	Show the current Terragrunt version	
o	--terragrunt-config	Path to the Terragrunt config file. Default is terragrunt.hcl	v
o	--terragrunt-tfpath	Path to the Terraform binary. Default is terraform (on PATH)	v
o	--terragrunt-no-auto-init	Don't automatically run 'terraform init' during other terragrunt commands. You must run…	
o	--terragrunt-no-auto-retry	Don't automatically re-run command in case of transient errors	
o	--terragrunt-non-interactive	Assume 'yes' for all prompts	
o	--terragrunt-working-dir	The path to the Terraform templates. Default is current directory	v
o	--terragrunt-download-dir	The path where to download Terraform code. Default is .terragrunt-cache in the working directory	v
o	--terragrunt-source	Download Terraform configurations from the specified source into a temporary folder, and run…	v
o	--terragrunt-source-map	Replaces any source URL (including the source URL of a config pulled in with dependency blocks)…	
o	--terragrunt-source-update	Delete the contents of the temporary folder to clear out any old, cached source code before…	
o	--terragrunt-ignore-dependency-errors	*-all commands continue processing components even if a dependency fails	
o	--terragrunt-iam-role	Assume the specified IAM role before executing Terraform. Can also be set via the…	v
o	--terragrunt-iam-assume-role-duration	Session duration for IAM Assume Role session. Can also be set via the…	v
o	--terragrunt-iam-assume-role-session-name	Name for the IAM Assummed Role session. Can also be set via TERRAGRUNT_IAM_ASSUME_ROLE_SESSION_NAME…	v
o	--terragrunt-exclude-dir	Unix-style glob of directories to exclude when running *-all commands	v
o	--terragrunt-include-dir	Unix-style glob of directories to include when running *-all commands	v
o	--terragrunt-strict-include	Only modules under the directories passed in with –terragrunt-include-dir will be included. All…	
o	--terragrunt-strict-validate	Sets strict mode for the validate-inputs command. By default, strict mode is off. When this flag…	
o	--terragrunt-ignore-dependency-order	*-all commands will be run disregarding the dependencies	
o	--terragrunt-ignore-external-dependencies	*-all commands will not attempt to include external dependencies	
o	--terragrunt-include-external-dependencies	*-all commands will include external dependencies	
o	--terragrunt-parallelism	*-all commands parallelism set to at most N modules	v
o	--terragrunt-debug	Write terragrunt-debug.tfvars to working folder to help root-cause issues	
o	--terragrunt-log-level	Sets the logging level for Terragrunt. Supported levels: panic, fatal, error, warn (default)…	
o	--terragrunt-check	Enable check mode in the hclfmt command	
o	--terragrunt-hclfmt-file	The path to a single hcl file that the hclfmt command should run on	v
o	--terragrunt-override-attr	A key=value attribute to override in a provider block as part of the aws-provider-patch command…	v
o	--terragrunt-json-out	The file path that terragrunt should use when rendering the terragrunt.hcl config as json. Only…	v
o	--terragrunt-modules-that-include	When passed in, run-all will only run the command against Terragrunt modules that include the…	v
=	workspace list	--terragrunt-config
t	filepaths
=	workspace list	--terragrunt-tfpath
t	filepaths
=	workspace list	--terragrunt-working-dir
t	folders
=	workspace list	--terragrunt-download-dir
t	folders
=	workspace list	--terragrunt-source
t	folders
=	workspace list	--terragrunt-exclude-dir
t	folders
=	workspace list	--terragrunt-include-dir
t	folders
=	workspace list	--terragrunt-hclfmt-file
t	filepaths
=	workspace list	--terragrunt-json-out
t	filepaths
=	workspace list	--terragrunt-modules-that-include
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
@	run-all
@	terragrunt-info
@	validate-inputs
@	graph-dependencies
@	hclfmt
@	aws-provider-patch
@	render-json

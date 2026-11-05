@	
s	analytics	Enable / Disable analytics
s	build	Build (and optionally push) a Docker image
s	completion	Generate the autocompletion script for the specified shell
s	ctx|context	Set the default context
s	doctor	Generate a zip file with the okteto logs
s	down	Deactivate your development container
s	exec	Execute a command in your development container
s	init	Automatically generate your okteto manifest file
s	kubeconfig	Download credentials for the Kubernetes cluster selected via 'okteto context'
s	ns|namespace	Configure the current namespace of the okteto context
s	pipeline	Pipeline management commands
s	preview	Preview environment management commands
s	push	Build, push and redeploy source code to the target app
s	restart	Restart the deployments listed in the services field of the okteto manifest
s	stack	Stack management commands
s	status	Status of the synchronization process
s	up	Activate your development container
s	update	Update okteto version
s	version	View the version of the okteto binary
s	help	Help about any command
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for okteto	
@	analytics
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--disable|-d	Disable analytics	
o	--help|-h	Help for analytics	
@	build
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--build-arg	Set build-time variables	v
o	--cache-from	Cache source images	v
o	--file|-f	Name of the Dockerfile (Default is 'PATH/Dockerfile')	v
o	--namespace	Namespace against which the image will be consumed. Default is the one defined at okteto context…	v
o	--no-cache	Do not use cache when building the image	
o	--progress	Show plain/tty build output	v
o	--secret	Secret files exposed to the build. Format: id=mysecret,src=/local/secret	v
o	--tag|-t	Name and optionally a tag in the 'name:tag' format (it is automatically pushed)	v
o	--target	Set the target build stage to build	v
o	--help|-h	Help for build	
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for completion	
@	completion bash
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for bash	
@	completion fish
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for fish	
@	completion powershell
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for powershell	
@	completion zsh
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for zsh	
@	ctx
s	delete	Delete a context
s	ls|list	List available contexts
s	show	Print the current context
s	use	Set the default context
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--builder|-b	Url of the builder service	v
o	--namespace|-n	Namespace of your okteto context	v
o	--okteto	Only shows okteto cluster options	
o	--token|-t	API token for authentication	v
o	--help|-h	Help for context	
@	ctx delete
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for delete	
a	1	0
#	ctx delete	1
d
@	ctx ls
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for list	
@	ctx show
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for show	
@	ctx use
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--builder|-b	Url of the builder service	v
o	--namespace|-n	Namespace of your okteto context	v
o	--okteto	Only shows okteto cluster options	
o	--token|-t	API token for authentication	v
o	--help|-h	Help for use	
a	1	0
#	ctx use	1
d
@	doctor
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context where the up command was executing	v
o	--file|-f	Path to the manifest file	v
o	--namespace|-n	Namespace where the up command was executing	v
o	--help|-h	Help for doctor	
@	down
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context where the down command is executed	v
o	--file|-f	Path to the manifest file	v
o	--namespace|-n	Namespace where the down command is executed	v
o	--volumes|-v	Remove persistent volume	
o	--help|-h	Help for down	
@	exec
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context where the exec command is executed	v
o	--file|-f	Path to the manifest file	v
o	--namespace|-n	Namespace where the exec command is executed	v
o	--help|-h	Help for exec	
@	init
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context target for generating the okteto manifest	v
o	--file|-f	Path to the manifest file	v
o	--namespace|-n	Namespace target for generating the okteto manifest	v
o	--overwrite	Overwrite existing manifest file	
o	--help|-h	Help for init	
@	kubeconfig
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for kubeconfig	
@	ns
s	create	Create a namespace
s	delete	Delete a namespace
s	ls|list	List namespaces managed by Okteto in your current context
s	ns|use	Configure the current namespace of the okteto context
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--personal	Load personal account	
o	--help|-h	Help for namespace	
@	ns create
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--members|-m	Members of the namespace, it can the username or email	v
o	--help|-h	Help for create	
@	ns delete
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for delete	
a	1	0
#	ns delete	1
d
@	ns ls
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for list	
@	ns ns
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--personal	Load personal account	
o	--help|-h	Help for use	
a	1	0
#	ns ns	1
d
@	pipeline
s	deploy	Deploy an okteto pipeline
s	destroy	Destroy an okteto pipeline
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for pipeline	
@	pipeline deploy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--branch|-b	The branch to deploy (defaults to the current branch)	v
o	--file|-f	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--filename	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--name|-p	Name of the pipeline (defaults to the git config name)	v
o	--namespace|-n	Namespace where the up command is executed (defaults to the current namespace)	v
o	--repository|-r	The repository to deploy (defaults to the current repository)	v
o	--skip-if-exists	Skip the pipeline deployment if the pipeline already exists in the namespace (defaults to false)	
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--var|-v	Set a pipeline variable (can be set more than once)	v
o	--wait|-w	Wait until the pipeline finishes (defaults to false)	
o	--help|-h	Help for deploy	
@	pipeline destroy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--name|-p	Name of the pipeline (defaults to the git config name)	v
o	--namespace|-n	Namespace where the up command is executed (defaults to the current namespace)	v
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--volumes|-v	Destroy persistent volumes created by the pipeline (defaults to false)	
o	--wait|-w	Wait until the pipeline finishes (defaults to false)	
o	--help|-h	Help for destroy	
@	preview
s	deploy	Deploy a preview environment
s	destroy	Destroy a preview environment
s	endpoints	Show endpoints for a preview environment
s	list	List all preview environments
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for preview	
@	preview deploy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--branch|-b	The branch to deploy (defaults to the current branch)	v
o	--file|-f	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--filename	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--repository|-r	The repository to deploy (defaults to the current repository)	v
o	--scope|-s	The scope of preview environment to create. Accepted values are ['personal', 'global']	v
o	--sourceUrl	The URL of the original pull/merge request	v
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--var|-v	Set a pipeline variable (can be set more than once)	v
o	--wait|-w	Wait until the preview environment deployment finishes (defaults to false)	
o	--help|-h	Help for deploy	
@	preview destroy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for destroy	
@	preview endpoints
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for endpoints	
@	preview list
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for list	
@	push
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context where the push command is executed	v
o	--deploy|-d	Create deployment when the app doesn't exist in a namespace	
o	--file|-f	Path to the manifest file	v
o	--name	Name of the app to push to	v
o	--namespace|-n	Namespace where the push command is executed	v
o	--no-cache	Do not use cache when building the image	
o	--progress	Show plain/tty build output	v
o	--tag|-t	Image tag to build, push and redeploy	v
o	--help|-h	Help for push	
@	restart
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context where the restart command is executed	v
o	--file|-f	Path to the manifest file	v
o	--namespace|-n	Namespace where the restart command is executed	v
o	--help|-h	Help for restart	
@	stack
s	deploy	Deploy a stack
s	destroy	Destroy a stack
s	endpoints	Show endpoints for a stack
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for stack	
@	stack deploy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--build	Build images before starting any Stack service	
o	--file|-f	Path to the stack manifest files. If more than one is passed the latest will overwrite the fields…	v
o	--name	Overwrites the stack name	v
o	--namespace|-n	Overwrites the stack namespace where the stack is deployed	v
o	--no-cache	Do not use cache when building the image	
o	--progress	Show plain/tty build output (default "tty")	v
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--wait	Wait until a minimum number of containers are in a ready state for every service	
o	--help|-h	Help for deploy	
@	stack destroy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--file|-f	Path to the stack manifest file	v
o	--name	Overwrites the stack name	v
o	--namespace|-n	Overwrites the stack namespace where the stack is destroyed	v
o	--volumes|-v	Remove persistent volumes	
o	--help|-h	Help for destroy	
@	stack endpoints
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--file|-f	Path to the stack manifest files. If more than one is passed the latest will overwrite the fields…	v
o	--name	Overwrites the stack name	v
o	--namespace|-n	Overwrites the stack namespace where the stack is deployed	v
o	--help|-h	Help for endpoints	
@	status
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--context|-c	Context where the up command is executing	v
o	--file|-f	Path to the manifest file	v
o	--info|-i	Show syncthing links for troubleshooting the synchronization service	
o	--namespace|-n	Namespace where the up command is executing	v
o	--watch|-w	Watch for changes	
o	--help|-h	Help for status	
@	up
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--build	Build on-the-fly the dev image using the info provided by the 'build' okteto manifest field	
o	--context|-c	Context where the up command is executed	v
o	--deploy|-d	Create deployment when it doesn't exist in a namespace	
o	--file|-f	Path to the manifest file	v
o	--namespace|-n	Namespace where the up command is executed	v
o	--pull	Force dev image pull	
o	--remote|-r	Configures remote execution on the specified port	v
o	--reset	Reset the file synchronization database	
o	--help|-h	Help for up	
@	update
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for update	
@	version
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for version	
@	help
s	analytics	Enable / Disable analytics
s	build	Build (and optionally push) a Docker image
s	completion	Generate the autocompletion script for the specified shell
s	ctx|context	Set the default context
s	doctor	Generate a zip file with the okteto logs
s	down	Deactivate your development container
s	exec	Execute a command in your development container
s	init	Automatically generate your okteto manifest file
s	kubeconfig	Download credentials for the Kubernetes cluster selected via 'okteto context'
s	ns|namespace	Configure the current namespace of the okteto context
s	pipeline	Pipeline management commands
s	preview	Preview environment management commands
s	push	Build, push and redeploy source code to the target app
s	restart	Restart the deployments listed in the services field of the okteto manifest
s	stack	Stack management commands
s	status	Status of the synchronization process
s	up	Activate your development container
s	update	Update okteto version
s	version	View the version of the okteto binary
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for help	
@	help analytics
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for analytics	
@	help build
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for build	
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for completion	
@	help completion bash
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for bash	
@	help completion fish
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for fish	
@	help completion powershell
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for powershell	
@	help completion zsh
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for zsh	
@	help ctx
s	delete	Delete a context
s	ls|list	List available contexts
s	show	Print the current context
s	use	Set the default context
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for context	
@	help ctx delete
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for delete	
@	help ctx ls
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for list	
@	help ctx show
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for show	
@	help ctx use
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--builder|-b	Url of the builder service	v
o	--namespace|-n	Namespace of your okteto context	v
o	--okteto	Only shows okteto cluster options	
o	--token|-t	API token for authentication	v
o	--help|-h	Help for use	
@	help doctor
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for doctor	
@	help down
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for down	
@	help exec
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for exec	
@	help init
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for init	
@	help kubeconfig
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for kubeconfig	
@	help ns
s	create	Create a namespace
s	delete	Delete a namespace
s	ls|list	List namespaces managed by Okteto in your current context
s	ns|use	Configure the current namespace of the okteto context
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for namespace	
@	help ns create
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--members|-m	Members of the namespace, it can the username or email	v
o	--help|-h	Help for create	
@	help ns delete
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for delete	
@	help ns ls
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for list	
@	help ns ns
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--personal	Load personal account	
o	--help|-h	Help for use	
@	help pipeline
s	deploy	Deploy an okteto pipeline
s	destroy	Destroy an okteto pipeline
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for pipeline	
@	help pipeline deploy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--branch|-b	The branch to deploy (defaults to the current branch)	v
o	--file|-f	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--filename	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--name|-p	Name of the pipeline (defaults to the git config name)	v
o	--namespace|-n	Namespace where the up command is executed (defaults to the current namespace)	v
o	--repository|-r	The repository to deploy (defaults to the current repository)	v
o	--skip-if-exists	Skip the pipeline deployment if the pipeline already exists in the namespace (defaults to false)	
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--var|-v	Set a pipeline variable (can be set more than once)	v
o	--wait|-w	Wait until the pipeline finishes (defaults to false)	
o	--help|-h	Help for deploy	
@	help pipeline destroy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--name|-p	Name of the pipeline (defaults to the git config name)	v
o	--namespace|-n	Namespace where the up command is executed (defaults to the current namespace)	v
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--volumes|-v	Destroy persistent volumes created by the pipeline (defaults to false)	
o	--wait|-w	Wait until the pipeline finishes (defaults to false)	
o	--help|-h	Help for destroy	
@	help preview
s	deploy	Deploy a preview environment
s	destroy	Destroy a preview environment
s	endpoints	Show endpoints for a preview environment
s	list	List all preview environments
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for preview	
@	help preview deploy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--branch|-b	The branch to deploy (defaults to the current branch)	v
o	--file|-f	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--filename	Relative path within the repository to the manifest file (default to okteto-pipeline.yaml or…	v
o	--repository|-r	The repository to deploy (defaults to the current repository)	v
o	--scope|-s	The scope of preview environment to create. Accepted values are ['personal', 'global']	v
o	--sourceUrl	The URL of the original pull/merge request	v
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--var|-v	Set a pipeline variable (can be set more than once)	v
o	--wait|-w	Wait until the preview environment deployment finishes (defaults to false)	
o	--help|-h	Help for deploy	
@	help preview destroy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for destroy	
@	help preview endpoints
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for endpoints	
@	help preview list
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for list	
@	help push
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for push	
@	help restart
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for restart	
@	help stack
s	deploy	Deploy a stack
s	destroy	Destroy a stack
s	endpoints	Show endpoints for a stack
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for stack	
@	help stack deploy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--build	Build images before starting any Stack service	
o	--file|-f	Path to the stack manifest files. If more than one is passed the latest will overwrite the fields…	v
o	--name	Overwrites the stack name	v
o	--namespace|-n	Overwrites the stack namespace where the stack is deployed	v
o	--no-cache	Do not use cache when building the image	
o	--progress	Show plain/tty build output (default "tty")	v
o	--timeout|-t	The length of time to wait for completion, zero means never. Any other values should contain a…	v
o	--wait	Wait until a minimum number of containers are in a ready state for every service	
o	--help|-h	Help for deploy	
@	help stack destroy
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--file|-f	Path to the stack manifest file	v
o	--name	Overwrites the stack name	v
o	--namespace|-n	Overwrites the stack namespace where the stack is destroyed	v
o	--volumes|-v	Remove persistent volumes	
o	--help|-h	Help for destroy	
@	help stack endpoints
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--file|-f	Path to the stack manifest files. If more than one is passed the latest will overwrite the fields…	v
o	--name	Overwrites the stack name	v
o	--namespace|-n	Overwrites the stack namespace where the stack is deployed	v
o	--help|-h	Help for endpoints	
@	help status
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for status	
@	help up
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for up	
@	help update
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for update	
@	help version
o	--loglevel|-l	Amount of information outputted (debug, info, warn, error)	v
o	--output|-o	Output format (tty, plain, json)	v
o	--help|-h	Help for version	

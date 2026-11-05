@	
s	completion	Generate the autocompletion script for the specified shell
s	help	Help about any command
o	--bind|-b	Bind working directory to container, rather than copy	
o	--bug-report	Display system information for bug report	
o	--container-cap-add	Kernel capabilities to add to the workflow containers (e.g. --container-cap-add SYS_PTRACE)	v
o	--container-cap-drop	Kernel capabilities to remove from the workflow containers (e.g. --container-cap-drop SYS_PTRACE)	v
o	--defaultbranch	The name of the main branch	v
o	--detect-event	Use first event type from workflow as event that triggered the workflow	
o	--env	Env to make available to actions with optional value (e.g. --env myenv=foo or --env myenv)	v
o	--eventpath|-e	Path to event JSON file	v
o	--graph|-g	Draw workflows	
o	--job|-j	Run job	v
o	--list|-l	List workflows	
o	--platform|-P	Custom image to use per platform (e.g. -P ubuntu-18.04=nektos/act-environments-ubuntu:18.04)	v
o	--privileged	Use privileged mode	
o	--pull|-p	Pull docker image(s) even if already present	
o	--rebuild	Rebuild local action docker image(s) even if already present	
o	--remote-name	Git remote name that will be used to retrieve url of git repo	v
o	--reuse|-r	Don't remove container(s) on successfully completed workflow(s) to maintain state between runs	
o	--rm	Automatically remove container(s)/volume(s) after a workflow(s) failure	
o	--secret|-s	Secret to make available to actions with optional value (e.g. -s mysecret=foo or -s mysecret)	v
o	--use-gitignore	Controls whether paths specified in .gitignore should be copied into container	
o	--userns	User namespace to use	v
o	--watch|-w	Watch the contents of the local repo and run when files change	
o	--actor|-a	User that triggered the event	vp
o	--artifact-server-path	Defines the path where the artifact server stores uploads and retrieves downloads from. If not…	vp
o	--artifact-server-port	Defines the port where the artifact server listens (will only bind to localhost)	vp
o	--container-architecture	Architecture which should be used to run containers, e.g.: linux/amd64. If not specified, will use…	vp
o	--container-daemon-socket	Path to Docker daemon socket which will be mounted to containers	vp
o	--directory|-C	Working directory	vp
o	--dryrun|-n	Dryrun mode	p
o	--env-file	Environment file to read and use as env in the containers	vp
o	--github-instance	GitHub instance to use. Don't use this if you are not using GitHub Enterprise Server	vp
o	--insecure-secrets	NOT RECOMMENDED! Doesn't hide secrets while printing logs	p
o	--json	Output logs in json format	p
o	--no-recurse	Flag to disable running workflows from subdirectories of specified path in '--workflows'/'-W' flag	p
o	--no-skip-checkout	Do not skip actions/checkout	p
o	--quiet|-q	Disable logging of output from steps	p
o	--secret-file	File with list of secrets to read from (e.g. --secret-file .secrets)	vp
o	--verbose|-v	Verbose output	p
o	--workflows|-W	Path to workflow file(s)	vp
o	--help|-h	Display help	p
=		--directory
t	folders
=		--workflows
t	folders,filepaths
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	help
s	completion	Generate the autocompletion script for the specified shell
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh

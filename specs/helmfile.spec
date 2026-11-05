@	
s	apply	Apply all resources from state file only when there are changes
s	build	Build all resources from state file
s	cache	Cache management
s	charts	DEPRECATED: sync releases from state file (helm upgrade --install)
s	completion	Generate the autocompletion script for the specified shell
s	delete	The helmfile delete sub-command deletes all the releases defined in the manifests
s	deps	Update charts based on their requirements, it locks your helmfile state and local charts…
s	destroy	Destroys and then purges releases
s	diff	Diff releases defined in state file, it executes the helm-diff plugin across all of the…
s	fetch	Fetch charts from state file, it downloads or copies local charts to a local directory for debug…
s	help	Help about any command
s	init	Initialize the helmfile, includes version checking and installation of helm and plug-ins
s	lint	Lint charts from state file (helm lint)
s	list	List releases defined in state file
s	repos	Repos releases defined in state file
s	secrets	Causes the helm-secrets plugin to be executed to decrypt the file
s	status	Retrieve status of releases in state file
s	sync	Sync releases defined in state file
s	template	Template releases defined in state file
s	test	Test charts from state file (helm test)
s	version	Print the CLI version
s	 write-values	Write values files for releases. Similar to `helmfile template`, write values files instead of…
o	--help|-h	Do not exit with an error code if the provided selector has no matching releases	p
o	--allow-no-matching-release	Show help for helmfile	p
o	--chart|-c	Set chart. Uses the chart set in release by default, and is available in template as {{ .Chart }}	vp
o	--color	Output with color	p
o	--debug	Enable verbose output for Helm and set log-level to debug, this disables --quiet/-q effect	p
o	--enable-live-output	Show live output from the Helm binary Stdout/Stderr into Helmfile own Stdout/Stderr. It only…	p
o	--environment|-e	Specify the environment name. defaults to default	vp
o	--file|-f	Load config from file or directory. defaults to helmfile.yaml or `helmfile.d`(means…	vp
o	--helm-binary|-b	Path to the helm binary (default "helm")	vp
o	--interactive|-i	Request confirmation before attempting to modify clusters	p
o	--kube-context	Set kubectl context. Uses current context by default	vp
o	--log-level	Set log level, default info (default info)	vp
o	--namespace|-n	Set namespace. Uses the namespace set in the context by default, and is available in templates as…	vp
o	--no-color	Output without color	p
o	--quiet|-q	Silence output. Equivalent to log-level warn	p
o	--selector|-l	Only run using the releases that match labels. Labels can take the form of foo=bar or foo!=bar	vp
o	--state-values-file	Specify state values in a YAML file	vp
o	--state-values-set	Set state values on the command line (can specify multiple or separate values with commas…	vp
o	--version|-v	Version for helmfile	p
=		--file
t	filepaths
=		--state-values-file
t	filepaths
@	apply
@	build
@	cache
@	charts
@	completion
@	delete
@	deps
@	destroy
@	diff
@	fetch
@	help
@	init
@	lint
@	list
@	repos
@	secrets
@	status
@	sync
@	template
@	test
@	version
@	write-values

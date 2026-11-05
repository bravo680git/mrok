@	
s	apps|app	Operations with apps. Uses helm. Flags are prepended with 'helm' can also be accurately described…
s	catalog	Operations with catalogs
s	clusters|cluster	Operations on clusters
s	context	Operations for the context
s	globaldns	Operations on global DNS providers and entries
s	inspect	View details of resources
s	kubectl	Run kubectl commands
s	login|-l	Login to a Rancher server
s	machines|machine	Operations on machines
s	multiclusterapps|multiclusterapp	Operations with multi-cluster apps
s	namespaces|namespace	Operations on namespaces
s	nodes|node	Operations on nodes
s	projects|project	Operations on projects
s	ps	Show workloads in a project
s	server	Operations for the server
s	settings|setting	Show settings for the current server
s	ssh	SSH into a node
s	up	Apply compose config
s	wait	Wait for resources cluster, app, project, multiClusterApp
s	token	Authenticate and generate new kubeconfig token
s	help|h	Shows a list of commands or help for one command
o	--debug	Debug logging	
o	--config|-c	Path to rancher config (default: `$home/.rancher`) [$RANCHER_CONFIG_DIR]	v
o	--help|-h	Show help for rancher cli	
o	--version|-v	Print the version	
=		--config
t	folders
@	apps
s	ls	List all apps in the current Rancher server
s	delete	Delete an app
s	install	Install an app template
s	rollback	Rollback an app to a previous version
s	upgrade	Upgrade an existing app to a newer version
s	list-templates|lt	List templates available for installation
s	show-tempate|st	Show versions available to install for an app template
s	show-app|sa	Show an app's available versions and revisions
s	show-notes	Show contents of apps notes.txt
o	--format|-o	Output format: 'json', 'yaml' or custom format	v
o	--quiet|-q	Only display IDs or suppress help text	
o	--help|-h	Show help	
=	apps	--format
v	json	
v	yaml	
@	apps ls
@	apps delete
a	1	0
@	apps install
o	--answers|-a	Path to an answers file, the format of the file is a map with key:value. This supports JSON and YAML	v
o	--values|-v	Path to a helm values file	v
o	--namespace|-n	Namespace to install the app into	v
o	--set	Set answers for the template, can be used multiple times. Example: --set foo=bar	v
o	--set-string	Set string answers for the template (Skips Helm's type conversion), can be used multiple times…	v
o	--version	Version of the template to use	v
o	--no-prompt	Suppress asking questions and use the default values when required answers are not provided	
o	--helm-timeout	Amount of time for helm to wait for k8s commands (default is 300 secs). Example: --helm-timeout…	v
o	--helm-wait	Helm will wait for as long as timeout value, for installed resources to be ready (pods, PVCs…	
a	2	0
=	apps install	--answers
d
=	apps install	--values
t	filepaths
@	apps rollback
a	2	0
@	apps upgrade
@	apps list-templates
@	apps show-tempate
@	apps show-app
@	apps show-notes
@	catalog
s	ls	List all catalogs in the current Rancher server
s	add	Add a catalog
@	catalog ls
o	--format|-o	Output format: 'json', 'yaml' or custom format	v
o	--quiet|-q	Only display IDs or suppress help text	
o	--help|-h	Show help	
o	--verbose|-v		
=	catalog ls	--format
v	json	
v	yaml	
@	catalog add
o	--branch	Branch from the url to use (default: 'master')	v
o	--helm-version	Version of helm the app(s) in your catalog will use for deployment. Use 'v2' for helm 2 or 'v3'…	v
a	2	0
@	clusters
@	context
@	globaldns
@	inspect
@	kubectl
@	login
o	--token	API Bearer Token to authenticate Rancher CLI to your Rancher server	v
a	1	0
@	machines
@	multiclusterapps
@	namespaces
@	nodes
@	projects
@	ps
@	server
s	current	Display the current server
s	delete	⚠️ Delete a server from the local config
s	ls	List all servers
s	switch	Switch to a new server
@	server current
@	server delete
a	1	0
#	server delete	1
d
@	server ls
@	server switch
a	1	0
#	server switch	1
d
@	settings
s	ls	List settings
s	get	Print a setting
s	set	Set the value for a setting
@	settings ls
@	settings get
a	1	0
@	settings set
o	--format|-o	Output format: 'json', 'yaml' or custom format	v
o	--quiet|-q	Only display IDs or suppress help text	
o	--help|-h	Show help	
o	--default	Reset the setting back to it's default value. If the default value is (blank) it will be set to that	
a	2	0
=	settings set	--format
v	json	
v	yaml	
@	ssh
@	up
@	wait
@	token
@	help

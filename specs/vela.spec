@	
s	show	Show the reference doc for component, trait or workflow types
s	env	Manage environments for vela applications to run
s	init	Create scaffold for vela application
s	up	Deploy one application
s	cluster	Manage Kubernetes Clusters for Continuous Delivery
s	workflow	Operate the Workflow during Application Delivery
s	addon	Manage addons for extension
s	uischema|ui	Manage UI schema for addons
s	def	Manage X-Definition for addons
s	registry	Manage Registry of X-Definitions for extension
s	component|comp|components	List component types installed and discover more registry
s	trait|traits	List trait types installed and discover more in registry
s	uninstall	Uninstalls KubeVela from a Kubernetes cluster
s	install	Installs KubeVela into a Kubernetes cluster
s	completion	Output shell completion code for the specified shell (bash or zsh). The shell code must be…
s	export	Export deploy manifests from appfile or application
s	version	Prints the version
o	--help|-h	Show help for vela	
@	show
o	-e|--env	Specify environment name for application	v
o	--help|-h	Help for show command	
o	-n|--namespace	Specify the Kubernetes namespace to use	v
a	1	1
#	show	1
t	history
@	env
s	delete	Delete an environment
s	init	Delete an environment
s	ls|list	List all environments for vela applications to run
s	set|sw	Set an environment as the default one for running vela applications
@	env delete
a	1	1
#	env delete	1
t	history
@	env init
o	--namespace	Specify K8s namespace for env	v
a	1	1
#	env init	1
t	history
@	env ls
a	1	1
#	env ls	1
t	history
@	env set
a	1	1
#	env set	1
t	history
@	init
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
o	--render-only	Rendering vela.yaml in current dir and do not deploy	
@	up
o	--env|-e	The environment name for the CLI request	v
o	--file|-f	The file path for appfile or application. It could be a remote url	v
o	--namespace|-n	If present, the namespace scope for this CLI request	v
o	--publish-version|-v	The publish version for deploying application	v
o	--revision|-r	The revision to use for deploying the application, if empty, the current application configuration…	v
a	1	1
=	up	--file
t	filepaths
#	up	1
t	history
@	cluster
s	alias	Alias a named cluster
s	detach	Detach managed cluster
s	join	Join managed cluster by kubeconfig
s	labels	Manage Kubernetes Cluster Labels
s	list|ls	List managed clusters
s	probe	Health probe managed cluster
s	rename	Rename managed cluster
@	cluster alias
@	cluster detach
o	--kubeconfig-path|-p	Specify the kubeconfig path of managed cluster. If you use ocm to manage your cluster, you must…	v
=	cluster detach	--kubeconfig-path
t	filepaths
@	cluster join
o	--create-namespace	Specifies the namespace need to create in managedCluster (default "vela-system")	v
o	--name|-n	Specify the cluster name. If empty, it will use the cluster name in config file. Default to be empty	v
@	cluster labels
s	add	Add labels to managed cluster
s	del	Delete labels for managed cluster
@	cluster labels add
@	cluster labels del
@	cluster list
@	cluster probe
@	cluster rename
@	workflow
s	restart	Restart an application workflow
s	resume	Resume a suspend application workflow
s	rollback	Rollback an application workflow to the latest revision
s	suspend	Suspend an application workflow
s	terminate	Terminate an application workflow
@	workflow restart
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
@	workflow resume
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
@	workflow rollback
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
@	workflow suspend
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
@	workflow terminate
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
@	addon
s	disable	Disable an addon
s	enable	Enable an addon
s	list	List addons
s	registry	Manage addon registry
s	status	Get addon status
s	upgrade	Upgrade an addon
@	addon disable
o	--force|-f	Skip checking if applications are still using this addon	
@	addon enable
o	--clusters|-c	Specify the runtime-clusters to enable	v
@	addon list
@	addon registry
s	add	Add an addon registry
s	delete	Delete an addon registry
s	get	Get an addon registry
s	list	List addon registries
s	update	Update an addon registry
@	addon registry add
o	--bucket	Specify the OSS bucket name	v
o	--endpoint	Specify the addon registry endpoint	v
o	--gitToken	Specify the github repo token	v
o	--path	Specify the addon registry OSS path	v
o	--type	Specify the addon registry type	v
@	addon registry delete
@	addon registry get
@	addon registry list
@	addon registry update
o	--bucket	Specify the OSS bucket name	v
o	--endpoint	Specify the addon registry endpoint	v
o	--gitToken	Specify the github repo token	v
o	--path	Specify the addon registry OSS path	v
o	--type	Specify the addon registry type	v
@	addon status
@	addon upgrade
@	uischema
s	apply	Apply UI schema from a file or dir
@	uischema apply
@	def
s	apply	Apply X-Definition
s	del	Delete X-Definition
s	doc-gen	Generate documentation of definitions (Only Terraform typed definitions are supported)
s	edit	Edit X-Definition
s	get	Get X-Definition
s	init	Init a new definition
s	list	List X-Definition
s	render	Render X-Definition
s	vet	Validate X-Definition
@	def apply
o	--dry-run	Only build definition from CUE into CRB object without applying it to kubernetes clusters	
o	--namespace|-n	Specify which namespace to apply. (default "vela-system")	v
a	1	1
#	def apply	1
t	filepaths,folders
@	def del
o	--namespace|-n	Specify which namespace to apply. (default "vela-system")	v
o	--type|-t	Specify the definition type of target. Valid types: workflow-step, component, trait, policy…	v
a	1	1
#	def del	1
t	filepaths,folders
@	def doc-gen
o	--type|-t	Specify the definition type of target. Valid types: workflow-step, component, trait, policy…	v
@	def edit
o	--namespace|-n	Specify which namespace to apply. (default "vela-system")	v
o	--type|-t	Specify the definition type of target. Valid types: workflow-step, component, trait, policy…	v
@	def get
o	--namespace|-n	Specify which namespace to apply. (default "vela-system")	v
o	--type|-t	Specify the definition type of target. Valid types: workflow-step, component, trait, policy…	v
@	def init
o	--desc|-d	Specify the description of the new definition	v
o	--interactive|-i	Specify whether use interactive process to help generate definitions	
o	--git	Specify which git repository the configuration(HCL) is stored in. Valid when --provider/-p is set	v
o	--local	Specify the local path of the configuration(HCL) file. Valid when --provider/-p is set	v
o	--output|-o	Specify the output path of the generated definition. If empty, the definition will be printed in…	v
o	--path	Specify which path the configuration(HCL) is stored in the Git repository. Valid when --git is set	v
o	--provider|-p	Specify which provider the cloud resource definition belongs to. Only alibaba, `aws`, `azure` are…	v
o	--template-yaml|-f	Specify the template yaml file that definition will use to build the schema. If empty, a default…	v
o	--type|-t	Specify the type of the new definition. Valid types: scope, workflow-step, component, trait…	v
=	def init	--template-yaml
t	filepaths
@	def list
o	--namespace|-n	Specify which namespace to apply. (default "vela-system")	v
o	--type|-t	Specify the definition type of target. Valid types: workflow-step, component, trait, policy…	v
@	def render
o	--message	Specify the header message of the generated YAML file. For example, declaring author information	v
o	--output|-o	Specify the output path of the rendered definition YAML. If empty, the definition will be printed…	v
=	def render	--output
t	folders
@	def vet
a	1	1
#	def vet	1
t	filepaths,folders
@	registry
s	config	Configure (add if not exist) a registry, default is local (built-in capabilities)
s	ls	List all configured registry
s	remove|rm	Remove specified registry
@	registry config
o	--token|-t	Github Repo token	v
@	registry ls
@	registry remove
@	component
s	get	Get component from type
o	--discover	Discover more registry	v
o	--label	A label to filter components, the format is --label type=terraform	v
o	--registry	Specify the registry name (default "default")	v
o	--token	Specify token when using --url to specify registry url	v
o	--url	Specify the registry url	v
@	component get
o	--registry	Specify the registry name (default "default")	v
o	--token	Specify token when using --url to specify registry url	v
o	--url	Specify the registry url	v
@	trait
s	get	Get trait from registry
o	--discover	Discover traits in registries	
o	--registry	Specify the registry name (default "default")	v
o	--token	Specify token when using --url to specify registry url	v
o	--url	Specify the registry url	v
@	trait get
o	--registry	Specify the registry name (default "default")	v
o	--token	Specify token when using --url to specify registry url	v
o	--url	Specify the registry url	v
@	uninstall
o	--force|-f	Force uninstall whole vela include all addons	
o	--detail|-d	Show detail log of uninstall information	
o	--namespace|-n	Namespace scope for installing KubeVela Core. (default "vela-system")	v
@	install
o	--file|-f	Custom the chart path of KubeVela control plane	v
o	--detail|-d	Show detail log of install information	
o	--namespace|-n	Namespace scope for installing KubeVela Core	v
o	--reuse|-r	Will re-use the user's last supplied values. (default true)	v
o	--version|-v	Specify the version of KubeVela to install	v
=	install	--file
t	filepaths
@	completion
s	bash	Output bash completion code
s	zsh	Output zsh completion code
@	completion bash
@	completion zsh
@	export
o	--file|-f	Specify the appfile path	v
o	--env|-e	Specify environment name for application	v
o	--namespace|-n	Specify the Kubernetes namespace to use	v
=	export	--file
t	filepaths
@	version
s	list	List all available versions
@	version list

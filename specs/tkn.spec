@	
s	tkb|bundles|bundle	Manage Tekton Bundles
s	chains|chain	Manage Chains
s	ct|clustertasks|clustertask	Manage ClusterTasks
s	ctb|clustertriggerbindings|clustertriggerbinding	Manage ClusterTriggerBindings
s	completion	Prints shell completion scripts
s	el|eventlisteners|eventlistener	Manage EventListeners
s	hub	Interact with tekton hub
s	p|pipelines|pipeline	Manage pipelines
s	pr|pipelineruns|pipelinerun	Manage PipelineRuns
s	res|resources|resource	Manage pipeline resources
s	t|tasks|task	Manage Tasks
s	tr|taskruns|taskrun	Manage TaskRuns
s	tb|triggerbindings|triggerbinding	Manage TriggerBindings
s	tt|triggertemplates|triggertemplate	Manage TriggerTemplates
s	version	Prints version information
s	help	Help about any command
o	--help|-h	Display help	p
@	tkb
s	list	List and print a Tekton bundle's contents
s	push	Create or replace a Tekton bundle
o	--no-color|-C	Disable coloring (default: false)	p
@	tkb list
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--cache-dir	A directory to cache Tekton bundles in	v
o	--no-cache	If set to true, pulls a Tekton bundle from the remote even its exact digest is available in the…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--remote-bearer	A Bearer token to authenticate against the repository	v
o	--remote-password	A password to pass to the registry for basic auth. Must be used with --remote-username	v
o	--remote-skip-tls	If set to true, skips TLS check when connecting to the registry	
o	--remote-username	A username to pass to the registry for basic auth. Must be used with --remote-password	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tkb list	--template
t	filepaths
@	tkb push
o	--filenames|-f	List of fully-qualified file paths containing YAML or JSON defined Tekton objects to include in…	v
o	--remote-bearer	A Bearer token to authenticate against the repository	v
o	--remote-password	A password to pass to the registry for basic auth. Must be used with --remote-username	v
o	--remote-skip-tls	If set to true, skips TLS check when connecting to the registry	
o	--remote-username	A username to pass to the registry for basic auth. Must be used with --remote-password	v
@	chains
s	payload	Print Tekton Chains' payload for a specific taskrun
s	signature	Print Tekton Chains' signature for a specific taskrun
o	--chains-namespace	Namespace in which chains is installed	vp
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	chains payload
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--skip-verify|-S	Skip verifying the payload'signature	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	chains payload	--template
t	filepaths
@	chains signature
@	ct
s	create	Create a ClusterTask from Task
s	rm|delete	Delete ClusterTasks in a cluster
s	desc|describe	Describe a ClusterTask
s	ls|list	Lists ClusterTasks
s	logs	Show ClusterTask logs
s	start	Start ClusterTasks
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	ct create
o	--from	Create a ClusterTask from Task in a particular namespace	v
@	ct rm
o	--all	Delete all ClusterTasks (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
o	--trs	Whether to delete ClusterTask(s) and related resources (TaskRuns) (default: false)	
=	ct rm	--template
t	filepaths
@	ct desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	ct desc	--template
t	filepaths
@	ct ls
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	ct ls	--template
t	filepaths
@	ct logs
o	--all|-a	Show all logs including init steps injected by tekton	
o	--follow|-f	Stream live logs	
o	--last|-L	Show logs for last TaskRun	
o	--limit	Lists number of TaskRuns	v
o	--timestamps|-t	Show logs with timestamp	
@	ct start
o	--dry-run	Preview TaskRun without running it	
o	--inputresource|-i	Pass the input resource name and ref as name=ref	v
o	--labels|-l	Pass labels as label=value	v
o	--last|-L	Re-run the ClusterTask using last TaskRun values	
o	--output	Format of TaskRun (yaml or json)	v
o	--outputresource|-o	Pass the output resource name and ref as name=ref	v
o	--param|-p	Pass the param as key=value for string type, or key=value1,value2,... for array type	v
o	--pod-template	Local or remote file containing a PodTemplate definition	v
o	--prefix-name	Specify a prefix for the TaskRun name (must be lowercase alphanumeric characters)	v
o	--serviceaccount|-s	Pass the serviceaccount name	v
o	--showlog	Show logs right after starting the ClusterTask	
o	--skip-optional-workspace	Skips the prompt for optional workspaces	
o	--timeout	Timeout for TaskRun	v
o	--use-param-defaults	Use default parameter values without prompting for input	
o	--use-taskrun	Specify a TaskRun name to use its values to re-run the TaskRun	v
o	--workspace|-w	Pass one or more workspaces to map to the corresponding physical volumes	v
@	ctb
s	rm|delete	Delete ClusterTriggerBindings
s	desc|describe	Describes a ClusterTriggerBinding
s	ls|list	Lists ClusterTriggerBindings in a namespace
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	ctb rm
o	--all	Delete all ClusterTriggerBindings (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	ctb rm	--template
t	filepaths
@	ctb desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	ctb desc	--template
t	filepaths
@	ctb ls
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	ctb ls	--template
t	filepaths
@	completion
@	el
s	rm|delete	Delete EventListeners in a namespace
s	desc|describe	Describe EventListener in a namespace
s	ls|list	Lists EventListeners in a namespace
s	logs	Show EventListener logs
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	el rm
o	--all	Delete all EventListeners in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	el rm	--template
t	filepaths
@	el desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	el desc	--template
t	filepaths
@	el ls
o	--all-namespaces|-A	List EventListeners from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	el ls	--template
t	filepaths
@	el logs
o	--tail|-t	Number of most recent log lines to show. Specify -1 for all logs from each pod	v
@	hub
s	check-upgrade	Check for upgrades of resources if present
s	downgrade	Downgrade an installed resource
s	get	Get resource manifest by its name, kind, catalog, and version
s	info	Display info of resource by its name, kind, catalog, and version
s	install	Install a resource from a catalog by its kind, name and version
s	reinstall	Reinstall a resource by its kind and name
s	search	Search resource by a combination of name, kind, categories, platforms, and tags
s	upgrade	Upgrade an installed resource
o	--api-server	Hub API Server URL (default 'https://api.hub.tekton.dev' for 'tekton' type; default…	vp
o	--type	The type of Hub from where to pull the resource. Either 'artifact' or 'tekton' (default 'tekton')	vp
@	hub check-upgrade
s	task	Check updates for Task installed via Hub CLI
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
@	hub check-upgrade task
@	hub downgrade
s	task	Downgrade an installed Task by its name to a lower version
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--to	Version of Resource	vp
@	hub downgrade task
@	hub get
s	pipeline	Get Pipeline by name, catalog and version
s	task	Get Task by name, catalog and version
o	--from	Name of Catalog to which resource belongs to	vp
o	--version	Version of Resource	vp
@	hub get pipeline
@	hub get task
o	--as-clustertask	Get the Task as ClusterTask	
@	hub info
s	task	Display info of Task by its name, catalog and version
o	--from	Name of Catalog to which resource belongs	vp
o	--version	Version of Resource	vp
@	hub info task
@	hub install
s	task	Install Task from a catalog by its name and version
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--from	Name of Catalog to which resource belongs	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--version	Version of Resource	vp
@	hub install task
@	hub reinstall
s	task	Reinstall a Task by its name
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--from	Name of Catalog to which resource belongs	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--version	Version of Resource	vp
@	hub reinstall task
@	hub search
o	--categories	Accepts a comma separated list of categories	v
o	--kinds	Accepts a comma separated list of kinds	v
o	--limit|-l	Max number of resources to fetch	v
o	--match	Accept type of search. 'exact' or 'contains'	v
o	--output|-o	Accepts output format: [table, json, wide]	v
o	--platforms	Accepts a comma separated list of platforms	v
o	--tags	Accepts a comma separated list of tags	v
@	hub upgrade
s	task	Upgrade a Task by its name
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--to	Version of Resource	vp
@	hub upgrade task
@	p
s	rm|delete	Delete Pipelines in a namespace
s	desc|describe	Describes a Pipeline in a namespace
s	export	Export Pipeline
s	ls|list	Lists Pipelines in a namespace
s	logs	Show Pipeline logs
s	sign	Sign Tekton Pipeline
s	start	Start Pipelines
s	verify	Verify Tekton Pipeline
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	p rm
o	--all	Delete all Pipelines in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--prs	Whether to delete Pipeline(s) and related resources (PipelineRuns) (default: false)	
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	p rm	--template
t	filepaths
@	p desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	p desc	--template
t	filepaths
@	p export
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	p export	--template
t	filepaths
@	p ls
o	--all-namespaces|-A	List Pipelines from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	p ls	--template
t	filepaths
@	p logs
o	--all|-a	Show all logs including init steps injected by tekton	
o	--follow|-f	Stream live logs	
o	--last|-L	Show logs for last PipelineRun	
o	--limit	Lists number of PipelineRuns	v
o	--timestamps|-t	Show logs with timestamp	
@	p sign
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--file-name|-f	Fle name of the signed pipeline, using the original file name will overwrite the file	v
o	--key-file|-K	Key file	v
o	--kms-key|-m	KMS key url	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	p sign	--template
t	filepaths
@	p start
o	--dry-run	Preview PipelineRun without running it	
o	--filename|-f	Local or remote file name containing a Pipeline definition to start a PipelineRun	v
o	--finally-timeout	Timeout for Finally TaskRuns	v
o	--labels|-l	Pass labels as label=value	v
o	--last|-L	Re-run the Pipeline using last PipelineRun values	
o	--output|-o	Format of PipelineRun (yaml, json or name)	v
o	--param|-p	Pass the param as key=value for string type, or key=value1,value2,... for array type	v
o	--pipeline-timeout	Timeout for PipelineRun	v
o	--pod-template	Local or remote file containing a PodTemplate definition	v
o	--prefix-name	Specify a prefix for the PipelineRun name (must be lowercase alphanumeric characters)	v
o	--resource|-r	Pass the resource name and ref as name=ref	v
o	--serviceaccount|-s	Pass the serviceaccount name	v
o	--showlog	Show logs right after starting the Pipeline	
o	--skip-optional-workspace	Skips the prompt for optional workspaces	
o	--task-serviceaccount	Pass the service account corresponding to the task	v
o	--tasks-timeout	Timeout for Pipeline TaskRuns	v
o	--use-param-defaults	Use default parameter values without prompting for input	
o	--use-pipelinerun	Use this pipelinerun values to re-run the pipeline	v
o	--workspace|-w	Pass one or more workspaces to map to the corresponding physical volumes	v
@	p verify
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--key-file|-K	Key file	v
o	--kms-key|-m	KMS key url	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	p verify	--template
t	filepaths
@	pr
s	cancel	Cancel a PipelineRun in a namespace
s	rm|delete	Delete PipelineRuns in a namespace
s	desc|describe	Describe a PipelineRun in a namespace
s	export	Export PipelineRun
s	ls|list	Lists PipelineRuns in a namespace
s	logs	Show the logs of a PipelineRun
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	pr cancel
o	--grace	Gracefully cancel a PipelineRun To use this, you need to change the feature-flags configmap…	v
@	pr rm
o	--all	Delete all PipelineRuns in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--ignore-running|-i	Ignore running PipelineRun (default: true)	
o	--keep	Keep n most recent number of PipelineRuns	v
o	--keep-since	When deleting all PipelineRuns keep the ones that has been completed since n minutes	v
o	--label	A selector (label query) to filter on when running with --all, supports '=', '==', and '!='	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--pipeline|-p	The name of a Pipeline whose PipelineRuns should be deleted (does not delete the Pipeline)	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	pr rm	--template
t	filepaths
@	pr desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--fzf|-F	Use fzf to select a PipelineRun to describe	
o	--last|-L	Show description for last PipelineRun	
o	--limit	Lists number of PipelineRuns when selecting a PipelineRun to describe	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	pr desc	--template
t	filepaths
@	pr export
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	pr export	--template
t	filepaths
@	pr ls
o	--all-namespaces|-A	List PipelineRuns from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--label	A selector (label query) to filter on, supports '=', '==', and '!='	v
o	--limit	Limit PipelineRuns listed (default: return all PipelineRuns)	v
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--reverse	List PipelineRuns in reverse order	
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	pr ls	--template
t	filepaths
@	pr logs
o	--all|-a	Show all logs including init steps injected by tekton	
o	--follow|-f	Stream live logs	
o	--fzf|-F	Use fzf to select a PipelineRun	
o	--last|-L	Show logs for last PipelineRun	
o	--limit	Lists number of PipelineRuns	v
o	--prefix	Prefix each log line with the log source (task name and step name)	
o	--task|-t	Show logs for mentioned Tasks only	v
o	--timestamps	Show logs with timestamp	
@	res
s	create	Create a pipeline resource in a namespace
s	rm|delete	Delete pipeline resources in a namespace
s	desc|describe	Describes a pipeline resource in a namespace
s	ls|list	Lists pipeline resources in a namespace
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	res create
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	res create	--template
t	filepaths
@	res rm
o	--all	Delete all PipelineResources in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	res rm	--template
t	filepaths
@	res desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	res desc	--template
t	filepaths
@	res ls
o	--all-namespaces|-A	List pipeline resources from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
o	--type|-t	Pipeline resource type	v
=	res ls	--template
t	filepaths
@	t
s	create	Create a Task from ClusterTask
s	rm|delete	Delete Tasks in a namespace
s	desc|describe	Describe a Task in a namespace
s	ls|list	Lists Tasks in a namespace
s	logs	Show Task logs
s	sign	Sign Tekton Task
s	start	Start Tasks
s	verify	Verify Tekton Task
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	t create
o	--from	Create a ClusterTask from Task in a particular namespace	v
@	t rm
o	--all	Delete all Tasks in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
o	--trs	Whether to delete Task(s) and related resources (TaskRuns) (default: false)	
=	t rm	--template
t	filepaths
@	t desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	t desc	--template
t	filepaths
@	t ls
o	--all-namespaces|-A	List Tasks from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	t ls	--template
t	filepaths
@	t logs
o	--all|-a	Show all logs including init steps injected by tekton	
o	--follow|-f	Stream live logs	
o	--last|-L	Show logs for last TaskRun	
o	--limit	Lists number of TaskRuns	v
o	--timestamps|-t	Show logs with timestamp	
@	t sign
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--file-name|-f	File name of the signed task, using the original file name will overwrite the file	v
o	--key-file|-K	Key file	v
o	--kms-key|-m	KMS key url	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	t sign	--template
t	filepaths
@	t start
o	--dry-run	Preview TaskRun without running it	
o	--filename|-f	Local or remote file name containing a Task definition to start a TaskRun	v
o	--inputresource|-i	Pass the input resource name and ref as name=ref	v
o	--labels|-l	Pass labels as label=value	v
o	--last|-L	Re-run the Task using last TaskRun values	
o	--output	Format of TaskRun (yaml or json)	v
o	--outputresource|-o	Pass the output resource name and ref as name=ref	v
o	--param|-p	Pass the param as key=value for string type, or key=value1,value2,... for array type	v
o	--pod-template	Local or remote file containing a PodTemplate definition	v
o	--prefix-name	Specify a prefix for the TaskRun name (must be lowercase alphanumeric characters)	v
o	--serviceaccount|-s	Pass the serviceaccount name	v
o	--showlog	Show logs right after starting the Task	
o	--skip-optional-workspace	Skips the prompt for optional workspaces	
o	--timeout	Timeout for TaskRun	v
o	--use-param-defaults	Use default parameter values without prompting for input	
o	--use-taskrun	Specify a TaskRun name to use its values to re-run the TaskRun	v
o	--workspace|-w	Pass one or more workspaces to map to the corresponding physical volumes	v
@	t verify
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--key-file|-K	Key file	v
o	--kms-key|-m	KMS key url	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	t verify	--template
t	filepaths
@	tr
s	cancel	Cancel a TaskRun in a namespace
s	rm|delete	Delete TaskRuns in a namespace
s	desc|describe	Describe a TaskRun in a namespace
s	export	Export TaskRun
s	ls|list	Lists TaskRuns in a namespace
s	logs	Show TaskRuns logs
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	tr cancel
@	tr rm
o	--all	Delete all TaskRuns in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--clustertask	The name of a ClusterTask whose TaskRuns should be deleted (does not delete the ClusterTask)	v
o	--force|-f	Whether to force deletion (default: false)	
o	--ignore-running|-i	Ignore running TaskRun (default: true)	
o	--ignore-running-pipelinerun	Ignore deleting taskruns of a running PipelineRun (default: true)	
o	--keep	Keep n most recent number of TaskRuns	v
o	--keep-since	When deleting all TaskRuns keep the ones that has been completed since n minutes	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--task|-t	The name of a Task whose TaskRuns should be deleted (does not delete the task)	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tr rm	--template
t	filepaths
@	tr desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--fzf|-F	Use fzf to select a taskrun to describe	
o	--last|-L	Show description for last TaskRun	
o	--limit	Lists number of TaskRuns when selecting a TaskRun to describe	v
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tr desc	--template
t	filepaths
@	tr export
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tr export	--template
t	filepaths
@	tr ls
o	--all-namespaces|-A	List TaskRuns from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--label	A selector (label query) to filter on, supports '=', '==', and '!='	v
o	--limit	Limit TaskRuns listed (default: return all TaskRuns)	v
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--reverse	List TaskRuns in reverse order	
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tr ls	--template
t	filepaths
@	tr logs
o	--all|-a	Show all logs including init steps injected by tekton	
o	--follow|-f	Stream live logs	
o	--fzf|-F	Use fzf to select a TaskRun	
o	--last|-L	Show logs for last TaskRun	
o	--limit	Lists number of TaskRuns	v
o	--prefix	Prefix each log line with the log source (step name)	
o	--step|-s	Show logs for mentioned steps only	v
o	--timestamps|-t	Show logs with timestamp	
@	tb
s	rm|delete	Delete TriggerBindings in a namespace
s	desc|describe	Describes a TriggerBinding in a namespace
s	ls|list	Lists TriggerBindings in a namespace
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	tb rm
o	--all	Delete all TriggerBindings in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tb rm	--template
t	filepaths
@	tb desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tb desc	--template
t	filepaths
@	tb ls
o	--all-namespaces|-A	List TriggerBindings from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tb ls	--template
t	filepaths
@	tt
s	rm|delete	Delete TriggerTemplates in a namespace
s	desc|describe	Describes a TriggerTemplate in a namespace
s	ls|list	Lists TriggerTemplates in a namespace
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	tt rm
o	--all	Delete all TriggerTemplates in a namespace (default: false)	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--force|-f	Whether to force deletion (default: false)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tt rm	--template
t	filepaths
@	tt desc
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tt desc	--template
t	filepaths
@	tt ls
o	--all-namespaces|-A	List TriggerTemplates from all namespaces	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--no-headers	Do not print column headers with output (default print column headers with output)	
o	--output|-o	Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile…	v
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v
=	tt ls	--template
t	filepaths
@	version
o	--check	Check if a newer version is available	
o	--component	Provide a particular component name for its version (client|chains|pipeline|triggers|dashboard)	v
o	--context|-c	Name of the kubeconfig context to use (default: kubectl config current-context)	vp
o	--kubeconfig|-k	Kubectl config file (default: $HOME/.kube/config)	vp
o	--namespace|-n	Namespace to use (default: from $KUBECONFIG)	vp
o	--no-color|-C	Disable coloring (default: false)	p
@	help
s	tkb|bundles|bundle	Manage Tekton Bundles
s	chains|chain	Manage Chains
s	ct|clustertasks|clustertask	Manage ClusterTasks
s	ctb|clustertriggerbindings|clustertriggerbinding	Manage ClusterTriggerBindings
s	completion	Prints shell completion scripts
s	el|eventlisteners|eventlistener	Manage EventListeners
s	hub	Interact with tekton hub
s	p|pipelines|pipeline	Manage pipelines
s	pr|pipelineruns|pipelinerun	Manage PipelineRuns
s	res|resources|resource	Manage pipeline resources
s	t|tasks|task	Manage Tasks
s	tr|taskruns|taskrun	Manage TaskRuns
s	tb|triggerbindings|triggerbinding	Manage TriggerBindings
s	tt|triggertemplates|triggertemplate	Manage TriggerTemplates
s	version	Prints version information
@	help tkb
s	list	List and print a Tekton bundle's contents
s	push	Create or replace a Tekton bundle
@	help tkb list
@	help tkb push
@	help chains
s	payload	Print Tekton Chains' payload for a specific taskrun
s	signature	Print Tekton Chains' signature for a specific taskrun
@	help chains payload
@	help chains signature
@	help ct
s	create	Create a ClusterTask from Task
s	rm|delete	Delete ClusterTasks in a cluster
s	desc|describe	Describe a ClusterTask
s	ls|list	Lists ClusterTasks
s	logs	Show ClusterTask logs
s	start	Start ClusterTasks
@	help ct create
@	help ct rm
@	help ct desc
@	help ct ls
@	help ct logs
@	help ct start
@	help ctb
s	rm|delete	Delete ClusterTriggerBindings
s	desc|describe	Describes a ClusterTriggerBinding
s	ls|list	Lists ClusterTriggerBindings in a namespace
@	help ctb rm
@	help ctb desc
@	help ctb ls
@	help completion
@	help el
s	rm|delete	Delete EventListeners in a namespace
s	desc|describe	Describe EventListener in a namespace
s	ls|list	Lists EventListeners in a namespace
s	logs	Show EventListener logs
@	help el rm
@	help el desc
@	help el ls
@	help el logs
@	help hub
s	check-upgrade	Check for upgrades of resources if present
s	downgrade	Downgrade an installed resource
s	get	Get resource manifest by its name, kind, catalog, and version
s	info	Display info of resource by its name, kind, catalog, and version
s	install	Install a resource from a catalog by its kind, name and version
s	reinstall	Reinstall a resource by its kind and name
s	search	Search resource by a combination of name, kind, categories, platforms, and tags
s	upgrade	Upgrade an installed resource
@	help hub check-upgrade
s	task	Check updates for Task installed via Hub CLI
@	help hub check-upgrade task
@	help hub downgrade
s	task	Downgrade an installed Task by its name to a lower version
@	help hub downgrade task
@	help hub get
s	pipeline	Get Pipeline by name, catalog and version
s	task	Get Task by name, catalog and version
@	help hub get pipeline
@	help hub get task
@	help hub info
s	task	Display info of Task by its name, catalog and version
@	help hub info task
@	help hub install
s	task	Install Task from a catalog by its name and version
@	help hub install task
@	help hub reinstall
s	task	Reinstall a Task by its name
@	help hub reinstall task
@	help hub search
@	help hub upgrade
s	task	Upgrade a Task by its name
@	help hub upgrade task
@	help p
s	rm|delete	Delete Pipelines in a namespace
s	desc|describe	Describes a Pipeline in a namespace
s	export	Export Pipeline
s	ls|list	Lists Pipelines in a namespace
s	logs	Show Pipeline logs
s	sign	Sign Tekton Pipeline
s	start	Start Pipelines
s	verify	Verify Tekton Pipeline
@	help p rm
@	help p desc
@	help p export
@	help p ls
@	help p logs
@	help p sign
@	help p start
@	help p verify
@	help pr
s	cancel	Cancel a PipelineRun in a namespace
s	rm|delete	Delete PipelineRuns in a namespace
s	desc|describe	Describe a PipelineRun in a namespace
s	export	Export PipelineRun
s	ls|list	Lists PipelineRuns in a namespace
s	logs	Show the logs of a PipelineRun
@	help pr cancel
@	help pr rm
@	help pr desc
@	help pr export
@	help pr ls
@	help pr logs
@	help res
s	create	Create a pipeline resource in a namespace
s	rm|delete	Delete pipeline resources in a namespace
s	desc|describe	Describes a pipeline resource in a namespace
s	ls|list	Lists pipeline resources in a namespace
@	help res create
@	help res rm
@	help res desc
@	help res ls
@	help t
s	create	Create a Task from ClusterTask
s	rm|delete	Delete Tasks in a namespace
s	desc|describe	Describe a Task in a namespace
s	ls|list	Lists Tasks in a namespace
s	logs	Show Task logs
s	sign	Sign Tekton Task
s	start	Start Tasks
s	verify	Verify Tekton Task
@	help t create
@	help t rm
@	help t desc
@	help t ls
@	help t logs
@	help t sign
@	help t start
@	help t verify
@	help tr
s	cancel	Cancel a TaskRun in a namespace
s	rm|delete	Delete TaskRuns in a namespace
s	desc|describe	Describe a TaskRun in a namespace
s	export	Export TaskRun
s	ls|list	Lists TaskRuns in a namespace
s	logs	Show TaskRuns logs
@	help tr cancel
@	help tr rm
@	help tr desc
@	help tr export
@	help tr ls
@	help tr logs
@	help tb
s	rm|delete	Delete TriggerBindings in a namespace
s	desc|describe	Describes a TriggerBinding in a namespace
s	ls|list	Lists TriggerBindings in a namespace
@	help tb rm
@	help tb desc
@	help tb ls
@	help tt
s	rm|delete	Delete TriggerTemplates in a namespace
s	desc|describe	Describes a TriggerTemplate in a namespace
s	ls|list	Lists TriggerTemplates in a namespace
@	help tt rm
@	help tt desc
@	help tt ls
@	help version

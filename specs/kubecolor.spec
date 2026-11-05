@	
s	alpha	These commands correspond to alpha features that are not enabled in Kubernetes clusters by default
s	annotate	Update the annotations on one or more resources
s	api-resources	Print the supported API resources on the server
s	api-versions	Print the supported API versions on the server, in the form of "group/version"
s	apply	Apply a configuration to a resource by filename or stdin. The resource name must be specified…
s	attach	Attach to a process that is already running inside an existing container
s	auth	Inspect authorization
s	autoscale	Creates an autoscaler that automatically chooses and sets the number of pods that run in a…
s	certificate	Modify certificate resources
s	cluster-info	Display addresses of the master and services with label kubernetes.io/cluster-service=true To…
s	completion	Output shell completion code for the specified shell (bash or zsh). The shell code must be…
s	config	Modify kubeconfig files using subcommands like "kubectl config set current-context my-context"
s	convert	Convert config files between different API versions. Both YAML and JSON formats are accepted
s	cordon	Mark node as unschedulable
s	cp	Copy files and directories to and from containers
s	create	Create a resource from a file or from stdin
s	delete	Delete resources by filenames, stdin, resources and names, or by resources and label selector
s	describe	Show details of a specific resource or group of resources
s	diff	Diff configurations specified by filename or stdin between the current online configuration, and…
s	drain	Drain node in preparation for maintenance
s	edit	Edit a resource from the default editor
s	exec	Execute a command in a container
s	explain	List the fields for supported resources
s	expose	Expose a resource as a new Kubernetes service
s	get	Display one or many resources
s	kustomize	Print a set of API resources generated from instructions in a kustomization.yaml file
s	label	Update the labels on a resource
s	logs	Print the logs for a container in a pod or specified resource. If the pod has only one container…
s	patch	Update field(s) of a resource using strategic merge patch, a JSON merge patch, or a JSON patch
s	plugin	Provides utilities for interacting with plugins
s	port-forward	Forward one or more local ports to a pod. This command requires the node to have 'socat' installed
s	proxy	Creates a proxy server or application-level gateway between localhost and the Kubernetes API…
s	replace	Replace a resource by filename or stdin
s	rollout	Manage the rollout of a resource
s	run	Create and run a particular image in a pod
s	scale	Set a new size for a Deployment, ReplicaSet, Replication Controller, or StatefulSet
s	set	Configure application resources
s	taint	Update the taints on one or more nodes
s	top	Display Resource (CPU/Memory/Storage) usage
s	uncordon	Mark node as schedulable
s	version	Print the client and server version information for the current context
s	wait	Experimental: Wait for a specific condition on one or many resources
o	-n|--namespace	If present, the namespace scope for this CLI request	v
@	alpha
s	debug	Tools for debugging Kubernetes resources
@	alpha debug
o	--arguments-only	If specified, everything after -- will be passed to the new container as Args instead of Command	v
o	--attach	If true, wait for the Pod to start running, and then attach to the Pod as if 'kubectl attach ...'…	v
o	--container	Container name to use for debug container	v
o	--env	Environment variables to set in the container	v
o	--image	Container image to use for debug container	v
o	--image-pull-policy	The image pull policy for the container	v
o	--quiet	If true, suppress prompt messages	v
o	-i|--stdin	Keep stdin open on the container(s) in the pod, even if nothing is attached	v
o	--target	Target processes in this container name	v
o	-t|--tty	Allocated a TTY for each container in the pod	v
@	annotate
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--resource-version	If non-empty, the annotation update will only succeed if this is the current resource-version for…	v=
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	--field-selector	Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector…	v=
o	--local	If true, annotation will NOT contact api-server but run locally	
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--overwrite	If true, allow annotations to be overwritten, otherwise reject annotation updates that overwrite…	
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
a	3	1
=	annotate	-f
t	filepaths
=	annotate	-k
t	folders
=	annotate	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	annotate	--dry-run
v	none	
v	server	
v	client	
#	annotate	1
d
#	annotate	2
d
@	api-resources
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--api-group	Limit to resources in the specified API group	v
o	--cached	Use the cached list of resources if available	
o	--namespaced	If false, non-namespaced resources will be returned, otherwise returning namespaced resources by…	
o	--no-headers	When using the default or custom-column output format, don't print headers (default print headers)	
o	--sort-by	If non-empty, sort nodes list using specified field. The field can be either 'name' or 'kind'	v=
o	--verbs	Limit to resources that support the specified verbs	v=
=	api-resources	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	api-versions
@	apply
s	edit-last-applied	Edit the latest last-applied-configuration annotations of resources from the default editor
s	set-last-applied	Set the latest last-applied-configuration annotations by setting it to match the contents of a…
s	view-last-applied	View the latest last-applied-configuration annotations by type/name or file
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--resource-version	If non-empty, the annotation update will only succeed if this is the current resource-version for…	v=
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	--field-selector	Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector…	v=
o	--local	If true, annotation will NOT contact api-server but run locally	
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--overwrite	If true, allow annotations to be overwritten, otherwise reject annotation updates that overwrite…	
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--cascade	If true, cascade the deletion of the resources managed by this resource (e.g. Pods created by a…	
o	--field-manager	Name of the manager used to track field ownership	v=
o	--force	If true, immediately remove resources from API and bypass graceful deletion. Note that immediate…	
o	--force-conflicts	If true, server-side apply will force the changes against conflicts	
o	--grace-period	Period of time in seconds given to the resource to terminate gracefully. Ignored if negative. Set…	v=
o	--openapi-patch	If true, use openapi to calculate diff when the openapi presents and the resource can be found in…	
o	--overwrite	Automatically resolve conflicts between the modified and live configuration by using values from…	
o	--prune	Automatically delete resource objects, including the uninitialized ones, that do not appear in the…	
o	--prune-whitelist	Overwrite the default whitelist with <group/version/kind> for --prune	v=
o	--server-side	If true, apply runs in the server instead of the client	
o	--timeout	The length of time to wait before giving up on a delete, zero means determine a timeout from the…	v=
o	--validate	If true, use a schema to validate the input before sending it	
o	--wait	If true, wait for resources to be gone before returning. This waits for finalizers	
=	apply	-f
t	filepaths
=	apply	-k
t	folders
=	apply	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	apply	--dry-run
v	none	
v	server	
v	client	
@	apply edit-last-applied
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--windows-line-endings	Defaults to the line ending native to your platform	
o	--field-manager	Name of the manager used to track field ownership	v
o	--show-manged-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
a	2	0
=	apply edit-last-applied	-f
t	filepaths
=	apply edit-last-applied	-k
t	folders
=	apply edit-last-applied	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	apply edit-last-applied	1
d
#	apply edit-last-applied	2
d
@	apply set-last-applied
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--show-manged-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--create-annotation	Will create 'last-applied-configuration' annotations if current objects doesn't have one	
=	apply set-last-applied	-f
t	filepaths
=	apply set-last-applied	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	apply view-last-applied
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
a	2	0
=	apply view-last-applied	-f
t	filepaths
=	apply view-last-applied	-k
t	folders
=	apply view-last-applied	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	apply view-last-applied	1
d
#	apply view-last-applied	2
d
@	attach
o	-c|--container	Container name. If omitted, the first container in the pod will be chosen	v
o	--pod-running-timeout	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running	v=
o	-i|--stdin	Pass stdin to the container	
o	-t|--tty	Stdin is a TTY	
a	1	0
=	attach	-c
d
#	attach	1
d
@	auth
s	can-i	Check whether an action is allowed
s	reconcile	Reconciles rules for RBAC Role, RoleBinding, ClusterRole, and ClusterRole binding objects
@	auth can-i
o	-A|--all-namespaces	If true, check the specified action in all namespaces	
o	--list	If true, prints all allowed actions	
o	--no-headers	If true, prints allowed actions without headers	
o	-q|--quiet	If true, suppress output and just return the exit code	
o	--subresource	SubResource such as pod/log or deployment/scale	v=
a	3	0
#	auth can-i	1
v	*	
v	get	
v	list	
v	watch	
v	delete	
v	create	
v	update	
v	patch	
#	auth can-i	2
d
#	auth can-i	3
d
@	auth reconcile
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--remove-extra-permissions	If true, removes extra permissions added to roles	
o	--remove-extra-subjects	If true, removes extra subjects added to rolebindings	
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
=	auth reconcile	--dry-run
v	none	
v	server	
v	client	
=	auth reconcile	-f
t	filepaths
=	auth reconcile	-k
t	folders
=	auth reconcile	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	autoscale
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--cpu-percent	The target average CPU utilization (represented as a percent of requested CPU) over all the pods…	v=
o	--generator	The name of the API generator to use. Currently there is only 1 generator	v=
o	--max	The upper limit for the number of pods that can be set by the autoscaler. Required	v=
o	--min	The lower limit for the number of pods that can be set by the autoscaler. If it's not specified or…	v=
o	--name	The name for the newly created object. If not specified, the name of the input resource will be used	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
a	2	0
=	autoscale	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	autoscale	--dry-run
v	none	
v	server	
v	client	
=	autoscale	-f
t	filepaths
=	autoscale	-k
t	folders
#	autoscale	1
d
#	autoscale	2
d
@	certificate
s	approve	Approve a certificate signing request
s	deny	Deny a certificate signing request
@	certificate approve
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--force	Update the CSR even if it is already approved	
a	1	0
=	certificate approve	-f
t	filepaths
=	certificate approve	-k
t	folders
=	certificate approve	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	certificate deny
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--force	Update the CSR even if it is already approved	
a	1	0
=	certificate deny	-f
t	filepaths
=	certificate deny	-k
t	folders
=	certificate deny	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	cluster-info
s	dump	Dumps cluster info out suitable for debugging and diagnosing cluster problems. By default, dumps…
@	cluster-info dump
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	-A|--all-namespaces	If true, dump all namespaces. If true, --namespaces is ignored	
o	--namespaces	A comma separated list of namespaces to dump	v
o	--output-directory	Where to output the files. If empty or '-' uses stdout, otherwise creates a directory hierarchy in…	v=
o	--pod-running-timeout	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running	v=
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
=	cluster-info dump	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	completion
@	config
s	current-context	Displays the current-context
s	delete-cluster	Delete the specified cluster from the kubeconfig
s	delete-context	Delete the specified context from the kubeconfig
s	get-clusters	Display clusters defined in the kubeconfig
s	get-contexts	Displays one or many contexts from the kubeconfig file
s	get-users	Display users defined in the kubeconfig
s	rename-context	Renames a context from the kubeconfig file
s	set	Sets an individual value in a kubeconfig file
s	set-cluster	Sets a cluster entry in kubeconfig
s	set-context	Sets a context entry in kubeconfig
s	set-credentials	Sets a user entry in kubeconfig
s	unset	Unsets an individual value in a kubeconfig file
s	use-context	Sets the current-context in a kubeconfig file
s	view	Display merged kubeconfig settings or a specified kubeconfig file
o	--kubeconfig		v=
=	config	--kubeconfig
t	filepaths
@	config current-context
@	config delete-cluster
a	1	0
#	config delete-cluster	1
d
@	config delete-context
a	1	0
#	config delete-context	1
d
@	config get-clusters
@	config get-contexts
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--no-headers	When using the default or custom-column output format, don't print headers (default print headers)	v
a	1	0
=	config get-contexts	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	config get-contexts	1
d
@	config get-users
@	config rename-context
a	2	0
#	config rename-context	1
d
@	config set
o	--set-raw-bytes	When writing a []byte PROPERTY_VALUE, write the given string directly without base64 decoding	v
a	2	0
@	config set-cluster
o	--embed-certs	Embed-certs for the cluster entry in kubeconfig	
o	--server		v=
o	--certificate-authority	Path to certificate authority	v=
o	--insecure-skip-tls-verify		v=
o	--tls-server-name		v=
a	1	0
=	config set-cluster	--certificate-authority
t	filepaths
=	config set-cluster	--insecure-skip-tls-verify
v	true	
v	false	
@	config set-context
o	--current	Modify the current context	
o	--cluster		v=
o	--user		v=
o	--namespace		v=
a	1	0
#	config set-context	1
d
@	config set-credentials
o	--client-certificate	Client cert for user entry	v=
o	--client-key	Client key for user entry	v=
o	--token	Bearer Token for user entry	v=
o	--username	Username for basic authentication	v=
o	--password	Password for basic authentication	v=
o	--auth-provider	Auth provider for the user entry in kubeconfig	v=
o	--auth-provider-arg	'key=value' arguments for the auth provider	v=
o	--embed-certs	Embed client cert/key for the user entry in kubeconfig	
o	--exec-api-version	API version of the exec credential plugin for the user entry in kubeconfig	v=
o	--exec-arg	New arguments for the exec credential plugin command for the user entry in kubeconfig	v=
o	--exec-command	Command for the exec credential plugin for the user entry in kubeconfig	v=
o	--exec-env	'key=value' environment values for the exec credential plugin	v=
a	1	0
=	config set-credentials	--client-certificate
t	filepaths
=	config set-credentials	--client-key
t	filepaths
#	config set-credentials	1
d
@	config unset
a	1	0
@	config use-context
a	1	0
#	config use-context	1
d
@	config view
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--flatten	Flatten the resulting kubeconfig file into self-contained output (useful for creating portable…	
o	--merge	Merge the full hierarchy of kubeconfig files	
o	--minify	Remove all information not used by current-context from the output	
o	--raw	Display raw byte data	
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
=	config view	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	convert
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--local	If true, convert will NOT try to contact api-server but run locally	
o	--output-version	Output the formatted object with the given group version (for ex: 'extensions/v1beta1')	v=
o	--validate	If true, use a schema to validate the input before sending it	
=	convert	-f
t	filepaths
=	convert	-k
t	folders
=	convert	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	cordon
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
a	1	0
=	cordon	--dry-run
v	none	
v	server	
v	client	
#	cordon	1
d
@	cp
o	-c|--container	Container name. If omitted, the first container in the pod will be chosen	v
o	--no-preserve	The copied file/directory's ownership and permissions will not be preserved in the container	v
a	1	0
@	create
s	clusterrole	Create a ClusterRole
s	clusterrolebinding	Create a ClusterRoleBinding for a particular ClusterRole
s	configmap	Create a configmap based on a file, directory, or specified literal value
s	cronjob	Create a cronjob with the specified name
s	deployment	Create a deployment with the specified name
s	ingress	Create an ingress with the specified name
s	job	Create a job with the specified name
s	namespace	Create a namespace with the specified name
s	poddisruptionbudget	Create a pod disruption budget with the specified name, selector, and desired minimum available pods
s	priorityclass	Create a priorityclass with the specified name, value, globalDefault and description
s	quota	Create a resourcequota with the specified name, hard limits and optional scopes
s	role	Create a role with single rule
s	rolebinding	Create a RoleBinding for a particular Role or ClusterRole
s	secret	Create a secret using specified subcommand
s	service	Create a service using specified subcommand
s	serviceaccount	Create a service account with the specified name
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--edit	Edit the API resource before creating	
o	--raw	Raw URI to POST to the server. Uses the transport specified by the kubeconfig file	
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
o	--windows-line-endings	Only relevant if --edit=true. Defaults to the line ending native to your platform	
=	create	--dry-run
v	none	
v	server	
v	client	
=	create	-f
t	filepaths
=	create	-k
t	folders
=	create	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create clusterrole
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--aggregation-rule	An aggregation label selector for combining ClusterRoles	v=
o	--non-resource-url	A partial url that user should have access to	v
o	--resource	Resource that the rule applies to	v=
o	--resource-name	Resource in the white list that the rule applies to, repeat this flag for multiple items	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
o	--verb	Verb that applies to the resources contained in the rule	v=
a	1	0
=	create clusterrole	--dry-run
v	none	
v	server	
v	client	
=	create clusterrole	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create clusterrole	--resource
d
=	create clusterrole	--verb
v	*	
v	get	
v	list	
v	watch	
v	delete	
v	create	
v	update	
v	patch	
@	create clusterrolebinding
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--clusterrole	ClusterRole this ClusterRoleBinding should reference	v=
o	--user		v=
o	--group	Groups to bind to the clusterrole	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--serviceaccount	Service accounts to bind to the clusterrole, in the format <namespace>:<name>	v
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create clusterrolebinding	--dry-run
v	none	
v	server	
v	client	
=	create clusterrolebinding	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create clusterrolebinding	--clusterrole
d
@	create configmap
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--append-hash	Append a hash of the configmap to its name	
o	--from-env-file	Specify the path to a file to read lines of key=val pairs to create a configmap (i.e. a Docker…	v=
o	--from-file	Key file can be specified using its file path, in which case file basename will be used as…	v=
o	--from-literal	Specify a key and literal value to insert in configmap (i.e. mykey=somevalue)	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create configmap	--dry-run
v	none	
v	server	
v	client	
=	create configmap	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create configmap	--from-env-file
t	filepaths
=	create configmap	--from-file
t	filepaths
@	create cronjob
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--image	Image name to run	v=
o	--restart	Job's restart policy. supported values: OnFailure, Never	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--schedule	A schedule in the Cron format the job should be run with	v
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create cronjob	--dry-run
v	none	
v	server	
v	client	
=	create cronjob	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create cronjob	--restart
v	OnFailure	
v	Never	
@	create deployment
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--image	Image name to run	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create deployment	--dry-run
v	none	
v	server	
v	client	
=	create deployment	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create ingress
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--annotation	Annotation to insert in the ingress object, in the format annotation=value	v
o	--class	Ingress Class to be used	v=
o	--default-backend	Default service for backend, in format of svcname:port	v=
o	--field-manager	Name of the manager used to track field ownership	v=
o	--rule	Rule in format host/path=service:port[,tls=secretname]. Paths containing the leading character '*'…	v=
o	--show-managed-fields	If true, keep the managedFields when printing objects in JSON or YAML format	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create ingress	--dry-run
v	none	
v	server	
v	client	
=	create ingress	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create job
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--from	The name of the resource to create a Job from (only cronjob is supported)	v=
o	--image	Image name to run	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	2	0
=	create job	--dry-run
v	none	
v	server	
v	client	
=	create job	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create job	--from
d
@	create namespace
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create namespace	--dry-run
v	none	
v	server	
v	client	
=	create namespace	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create poddisruptionbudget
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--max-unavailable	The maximum number or percentage of unavailable pods this budget requires	v
o	--min-available	The minimum number or percentage of available pods this budget requires	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create poddisruptionbudget	--dry-run
v	none	
v	server	
v	client	
=	create poddisruptionbudget	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create priorityclass
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--description	Description is an arbitrary string that usually provides guidelines on when this priority class…	v=
o	--global-default	Global-default specifies whether this PriorityClass should be considered as the default priority	
o	--preemption-policy	Preemption-policy is the policy for preempting pods with lower priority	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
o	--value	The value of this priority class	v=
a	1	0
=	create priorityclass	--dry-run
v	none	
v	server	
v	client	
=	create priorityclass	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create quota
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--field-manager	Name of the manager used to track field ownership	v=
o	--hard	A comma-delimited set of resource=quantity pairs that define a hard limit	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--scopes	A comma-delimited set of quota scopes that must all match each object tracked by the quota	v
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create quota	--dry-run
v	none	
v	server	
v	client	
=	create quota	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create role
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--resource	Resource that the rule applies to	v=
o	--resource-name	Resource in the white list that the rule applies to, repeat this flag for multiple items	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
o	--verb	Verb that applies to the resources contained in the rule	v=
a	1	0
=	create role	--dry-run
v	none	
v	server	
v	client	
=	create role	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create role	--resource
d
=	create role	--verb
v	get	
v	list	
v	watch	
v	delete	
@	create rolebinding
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--clusterrole	ClusterRole this RoleBinding should reference	v=
o	--group	Groups to bind to the role	v=
o	--role	Role this RoleBinding should reference	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--serviceaccount	Service accounts to bind to the role, in the format <namespace>:<name>	v=
o	--username		v=
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create rolebinding	--dry-run
v	none	
v	server	
v	client	
=	create rolebinding	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create rolebinding	--clusterrole
d
=	create rolebinding	--role
d
@	create secret
s	docker-registry	Create a new secret for use with Docker registries
s	generic	Create a secret based on a file, directory, or specified literal value
s	tls	Create a TLS secret from the given public/private key pair
@	create secret docker-registry
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--append-hash	Append a hash of the secret to its name	
o	--docker-email	Email for Docker registry	v=
o	--docker-password	Password for Docker registry authentication	v=
o	--docker-server	Server location for Docker registry	v=
o	--docker-username	Username for Docker registry authentication	v=
o	--from-file	Key files can be specified using their file path, in which case a default name will be given to…	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create secret docker-registry	--dry-run
v	none	
v	server	
v	client	
=	create secret docker-registry	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create secret docker-registry	--from-file
t	filepaths
@	create secret generic
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--append-hash	Append a hash of the secret to its name	
o	--from-env-file	Specify the path to a file to read lines of key=val pairs to create a secret (i.e. a Docker .env…	v=
o	--from-file	Key files can be specified using their file path, in which case a default name will be given to…	v=
o	--from-literal	Specify a key and literal value to insert in secret (i.e. mykey=somevalue)	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--type	The type of secret to create	v=
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create secret generic	--dry-run
v	none	
v	server	
v	client	
=	create secret generic	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create secret generic	--from-env-file
t	filepaths
=	create secret generic	--from-file
t	filepaths
@	create secret tls
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--append-hash	Append a hash of the secret to its name	
o	--cert	Path to PEM encoded public key certificate	v=
o	--key	Path to private key associated with given certificate	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create secret tls	--dry-run
v	none	
v	server	
v	client	
=	create secret tls	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create secret tls	--cert
t	filepaths
=	create secret tls	--key
t	filepaths
@	create service
s	clusterip	Create a ClusterIP service with the specified name
s	externalname	Create an ExternalName service with the specified name
s	loadbalancer	Create a LoadBalancer service with the specified name
s	nodeport	Create a NodePort service with the specified name
@	create service clusterip
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--clusterip	Assign your own ClusterIP or set to 'None' for a 'headless' service (no loadbalancing)	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--tcp	Port pairs can be specified as '<port>:<targetPort>'	v=
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create service clusterip	--dry-run
v	none	
v	server	
v	client	
=	create service clusterip	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	create service clusterip	--clusterip
v	None	
@	create service externalname
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--external-name	External name of service	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--tcp	Port pairs can be specified as '<port>:<targetPort>'	v=
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create service externalname	--dry-run
v	none	
v	server	
v	client	
=	create service externalname	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create service loadbalancer
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--tcp	Port pairs can be specified as '<port>:<targetPort>'	v=
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create service loadbalancer	--dry-run
v	none	
v	server	
v	client	
=	create service loadbalancer	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create service nodeport
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--node-port	Port used to expose the service on each node in a cluster	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--tcp	Port pairs can be specified as '<port>:<targetPort>'	v=
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create service nodeport	--dry-run
v	none	
v	server	
v	client	
=	create service nodeport	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	create serviceaccount
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	create serviceaccount	--dry-run
v	none	
v	server	
v	client	
=	create serviceaccount	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	delete
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	--field-selector	Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector…	v=
o	-A|--all-namespaces	If present, list the requested object(s) across all namespaces. Namespace in current context is…	
o	--cascade	If true, cascade the deletion of the resources managed by this resource (e.g. Pods created by a…	
o	--force	If true, immediately remove resources from API and bypass graceful deletion. Note that immediate…	
o	--grace-period	Period of time in seconds given to the resource to terminate gracefully. Ignored if negative. Set…	v
o	--ignore-not-found	Treat "resource not found" as a successful delete. Defaults to "true" when --all is specified	
o	--now	If true, resources are signaled for immediate shutdown (same as --grace-period=1)	
o	--raw	Raw URI to DELETE to the server. Uses the transport specified by the kubeconfig file	
o	--timeout	The length of time to wait before giving up on a delete, zero means determine a timeout from the…	v
o	--wait	If true, wait for resources to be gone before returning. This waits for finalizers	
a	2	0
=	delete	--dry-run
v	none	
v	server	
v	client	
=	delete	-f
t	filepaths
=	delete	-k
t	folders
=	delete	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	delete	1
d
#	delete	2
d
@	describe
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	-A|--all-namespaces	If present, list the requested object(s) across all namespaces. Namespace in current context is…	
o	--show-events	If true, display events related to the described object	
a	2	0
=	describe	-f
t	filepaths
=	describe	-k
t	folders
#	describe	1
d
#	describe	2
d
@	diff
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--field-manager	Name of the manager used to track field ownership	v
o	--force-conflicts	If true, server-side apply will force the changes against conflicts	
o	--server-side	If true, apply runs in the server instead of the client	
=	diff	-f
t	filepaths
=	diff	-k
t	folders
@	drain
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--delete-local-data	Continue even if there are pods using emptyDir (local data that will be deleted when the node is…	
o	--disable-eviction	Force drain to use delete, even if eviction is supported. This will bypass checking…	
o	--force	Continue even if there are pods not managed by a ReplicationController, ReplicaSet, Job, DaemonSet…	
o	--grace-period	Period of time in seconds given to each pod to terminate gracefully. If negative, the default…	v=
o	--ignore-daemonsets	Ignore DaemonSet-managed pods	
o	--pod-selector	Label selector to filter pods on the node	v=
o	--skip-wait-for-delete-timeout	If pod DeletionTimestamp older than N seconds, skip waiting for the pod. Seconds must be greater…	v
o	--timeout	The length of time to wait before giving up, zero means infinite	v=
a	1	0
=	drain	--dry-run
v	none	
v	server	
v	client	
#	drain	1
d
@	edit
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--output-patch	Output the patch if the resource is edited	v
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--validate	If true, use a schema to validate the input before sending it	
o	--windows-line-endings	Defaults to the line ending native to your platform	
a	2	0
=	edit	-f
t	filepaths
=	edit	-k
t	folders
=	edit	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	edit	1
d
#	edit	2
d
@	exec
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-c|--container	Container name. If omitted, the first container in the pod will be chosen	v
o	--pod-running-timeout	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running	v
o	-i|--stdin	Pass stdin to the container	
o	-t|--tty	Stdin is a TTY	
a	2	0
=	exec	-f
t	filepaths
=	exec	-c
d
#	exec	1
d
@	explain
o	--api-version	Get different explanations for particular API version	v
o	--recursive	Print the fields of fields (Currently only 1 level deep)	
a	1	0
#	explain	1
d
@	expose
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--cluster-ip	ClusterIP to be assigned to the service. Leave empty to auto-allocate, or set to 'None' to create…	v=
o	--external-ip	Additional external IP address (not managed by Kubernetes) to accept for the service. If this IP…	v=
o	--generator	The name of the API generator to use. There are 2 generators: 'service/v1' and 'service/v2'. The…	v=
o	-l|--labels	Labels to apply to the service created by this call	v=
o	--load-balancer-ip	IP to assign to the LoadBalancer. If empty, an ephemeral IP will be created and used…	v=
o	--name	The name for the newly created object	v=
o	--overrides	An inline JSON override for the generated object. If this is non-empty, it is used to override the…	v
o	--port	The port that the service should serve on. Copied from the resource being exposed, if unspecified	v=
o	--protocol	The network protocol for the service to be created. Default is 'TCP'	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--session-affinity	If non-empty, set the session affinity for the service to this; legal values: 'None', 'ClientIP'	v=
o	--target-port	Name or number for the port on the container that the service should direct traffic to. Optional	v=
o	--type	Type for this service: ClusterIP, NodePort, LoadBalancer, or ExternalName. Default is 'ClusterIP'	v=
a	2	0
=	expose	--dry-run
v	none	
v	server	
v	client	
=	expose	-f
t	filepaths
=	expose	-k
t	folders
=	expose	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	expose	--protocol
v	TCP	
v	UDP	
v	SCTP	
=	expose	--type
v	ClusterIP	
v	NodePort	
v	LoadBalancer	
v	ExternalName	
#	expose	1
d
#	expose	2
d
@	get
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--field-selector	Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	-A|--all-namespaces	If present, list the requested object(s) across all namespaces. Namespace in current context is…	
o	--chunk-size	Return large lists in chunks rather than all at once. Pass 0 to disable. This flag is beta and may…	v=
o	--ignore-not-found	If the requested object does not exist the command will return exit code 0	
o	-L|--label-columns	Accepts a comma separated list of labels that are going to be presented as columns. Names are…	v
o	--no-headers	When using the default or custom-column output format, don't print headers (default print headers)	
o	--output-watch-events	Output watch event objects when --watch or --watch-only is used. Existing objects are output as…	
o	--raw	Raw URI to request from the server. Uses the transport specified by the kubeconfig file	
o	--server-print	If true, have the server return the appropriate table output. Supports extension APIs and CRDs	
o	--show-kind	If present, list the resource type for the requested object(s)	
o	--show-labels	When printing, show all labels as the last column (default hide labels column)	
o	--sort-by	If non-empty, sort list types using this field specification. The field specification is expressed…	v=
o	-w|--watch	After listing/getting the requested object, watch for changes. Uninitialized objects are excluded…	
o	--watch-only	Watch for changes to the requested object(s), without listing/getting first	
a	2	0
=	get	-f
t	filepaths
=	get	-k
t	folders
=	get	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	get	1
d
#	get	2
d
@	kustomize
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--allow-id-changes	Enable changes to a resourceId	
o	--enable-alpha-plugins	Enable kustomize plugins	
o	--enable-managedby-label	Enable adding app.kubernetes.io/managed-by	
o	--env|-e	A list of environment variables to be used by functions	v=
o	--load-restrictor	If set to 'LoadRestrictionsNone', local kustomizations may load files from outside their root…	v=
o	--mount	A list of storage options read from the filesystem	v=
o	--network	Enable network access for functions that declare it	
o	--network-name	The docker network to run the container in	v=
o	--reorder	Reorder the resources just before output. Use 'legacy' to apply a legacy reordering (Namespaces…	=
a	1	0
=	kustomize	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	kustomize	--env
t	filepaths
#	kustomize	1
t	folders
@	label
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	--field-selector	Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--resource-version	If non-empty, the annotation update will only succeed if this is the current resource-version for…	v=
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	--list	If true, display the labels for a given resource	
o	--overwrite	If true, allow labels to be overwritten, otherwise reject label updates that overwrite existing…	
a	2	0
=	label	--dry-run
v	none	
v	server	
v	client	
=	label	-f
t	filepaths
=	label	-k
t	folders
=	label	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	label	1
d
#	label	2
d
@	logs
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--all-containers	Get all containers' logs in the pod(s)	
o	-c|--container	Print the logs of this container	v
o	-f|--follow	Specify if the logs should be streamed	
o	--ignore-errors	If watching / following pod logs, allow for any errors that occur to be non-fatal	
o	--insecure-skip-tls-verify-backend	Skip verifying the identity of the kubelet that logs are requested from. In theory, an attacker…	
o	--limit-bytes	Maximum bytes of logs to return. Defaults to no limit	v=
o	--max-log-requests	Specify maximum number of concurrent logs to follow when using by a selector. Defaults to 5	v=
o	--pod-running-timeout	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running	v=
o	--prefix	Prefix each log line with the log source (pod name and container name)	
o	-p|--previous	If true, print the logs for the previous instance of the container in a pod if it exists	
o	--since	Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs. Only one…	v=
o	--since-time	Only return logs after a specific date (RFC3339). Defaults to all logs. Only one of since-time /…	v=
o	--tail	Lines of recent log file to display. Defaults to -1 with no selector, showing all log lines…	v=
o	--timestamps	Include timestamps on each line in the log output	
a	2	0
#	logs	1
d
#	logs	2
d
@	patch
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	-p|--patch	The patch to be applied to the resource JSON file	v
o	--type	The type of patch being provided; one of [json merge strategic]	v=
a	2	0
=	patch	--dry-run
v	none	
v	server	
v	client	
=	patch	-f
t	filepaths
=	patch	-k
t	folders
=	patch	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	patch	--type
v	json	
v	merge	
v	strategic	
#	patch	1
d
#	patch	2
d
@	plugin
@	port-forward
o	--address	Addresses to listen on (comma separated). Only accepts IP addresses or localhost as a value. When…	v
o	--pod-running-timeout	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running	v=
a	3	1
#	port-forward	1
d
#	port-forward	2
d
@	proxy
o	--accept-hosts	Regular expression for hosts that the proxy should accept	v=
o	--accept-paths	Regular expression for paths that the proxy should accept	v=
o	--address	The IP address on which to serve on	v=
o	--api-prefix	Prefix to serve the proxied API under	v=
o	--disable-filter	If true, disable request filtering in the proxy. This is dangerous, and can leave you vulnerable…	
o	--keepalive	Keepalive specifies the keep-alive period for an active network connection. Set to 0 to disable…	v=
o	-p|--port	The port on which to run the proxy. Set to 0 to pick a random port	v=
o	--reject-methods	Regular expression for HTTP methods that the proxy should reject (example…	v=
o	--reject-paths	Regular expression for paths that the proxy should reject. Paths specified here will be rejected…	v=
o	-u|--unix-socket	Unix socket on which to run the proxy	v=
o	-w|--www	Also serve static files from the given directory under the specified prefix	v=
o	-P|--www-prefix	Prefix to serve static files under, if static file directory is specified	v=
@	replace
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--cascade	If true, cascade the deletion of the resources managed by this resource (e.g. Pods created by a…	
o	--force	If true, immediately remove resources from API and bypass graceful deletion. Note that immediate…	
o	--grace-period	Period of time in seconds given to the resource to terminate gracefully. Ignored if negative. Set…	v=
o	--raw	Raw URI to PUT to the server. Uses the transport specified by the kubeconfig file	v=
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--timeout	The length of time to wait before giving up on a delete, zero means determine a timeout from the…	v=
o	--validate	If true, use a schema to validate the input before sending it	
o	--wait	If true, wait for resources to be gone before returning. This waits for finalizers	
=	replace	--dry-run
v	none	
v	server	
v	client	
=	replace	-f
t	filepaths
=	replace	-k
t	folders
=	replace	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	rollout
s	history	View previous rollout revisions and configurations
s	pause	Mark the provided resource as paused
s	restart	Restart a resource
s	resume	Resume a paused resource
s	status	Show the status of the rollout
s	undo	Rollback to a previous rollout
@	rollout history
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--revision	See the details, including podTemplate of the revision specified	v=
a	1	0
=	rollout history	-f
t	filepaths
=	rollout history	-k
t	folders
=	rollout history	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	rollout history	1
d
@	rollout pause
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
a	1	0
=	rollout pause	-f
t	filepaths
=	rollout pause	-k
t	folders
=	rollout pause	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	rollout pause	1
d
@	rollout restart
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
a	1	0
=	rollout restart	-f
t	filepaths
=	rollout restart	-k
t	folders
=	rollout restart	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	rollout restart	1
d
@	rollout resume
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
a	1	0
=	rollout resume	-f
t	filepaths
=	rollout resume	-k
t	folders
=	rollout resume	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	rollout resume	1
d
@	rollout status
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--revision	Pin to a specific revision for showing its status. Defaults to 0 (last revision)	v=
o	--timeout	The length of time to wait before ending watch, zero means never. Any other values should contain…	v=
o	-w|--watch	Watch the status of the rollout until it's done	
a	1	0
=	rollout status	-f
t	filepaths
=	rollout status	-k
t	folders
#	rollout status	1
d
@	rollout undo
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	--to_revision		v=
o	--timeout	The length of time to wait before ending watch, zero means never. Any other values should contain…	v=
a	1	0
=	rollout undo	-f
t	filepaths
=	rollout undo	-k
t	folders
=	rollout undo	--dry-run
v	none	
v	server	
v	client	
#	rollout undo	1
d
@	run
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--annotations	Annotations to apply to the pod	v=
o	--attach	If true, wait for the Pod to start running, and then attach to the Pod as if 'kubectl attach ...'…	
o	--cascade	Must be "background", "orphan", or "foreground". Selects the deletion cascading strategy for the…	v
o	--command	If true and extra arguments are present, use them as the 'command' field in the container, rather…	
o	--env	Environment variables to set in the container	v=
o	--expose	If true, service is created for the container(s) which are run	
o	--force	If true, immediately remove resources from API and bypass graceful deletion. Note that immediate…	
o	--grace-period	Period of time in seconds given to the resource to terminate gracefully. Ignored if negative. Set…	v=
o	--hostport	The host port mapping for the container port. To demonstrate a single-machine container	v=
o	--image	The image for the container to run	v=
o	--image-pull-policy	The image pull policy for the container. If left empty, this value will not be specified by the…	v
o	-l|--labels	Comma separated labels to apply to the pod(s). Will override previous values	v=
o	--leave-stdin-open	If the pod is started in interactive mode or with stdin, leave stdin open after the first attach…	
o	--limits	The resource requirement limits for this container. For example, 'cpu=200m,memory=512Mi'. Note…	v=
o	--overrides	An inline JSON override for the generated object. If this is non-empty, it is used to override the…	v=
o	--pod-running-timeout	The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running	v=
o	--port	The port that this container exposes	v=
o	--quiet	If true, suppress prompt messages	
o	--requests	The resource requirement requests for this container. For example, 'cpu=100m,memory=256Mi'. Note…	v=
o	--restart	The restart policy for this Pod. Legal values [Always, OnFailure, Never]. If set to 'Always' a…	v=
o	--rm	If true, delete resources created in this command for attached containers	
o	--save-config	If true, the configuration of current object will be saved in its annotation. Otherwise, the…	
o	--serviceaccount	Service account to set in the pod spec	v=
o	-i|--stdin	Keep stdin open on the container(s) in the pod, even if nothing is attached	
o	--timeout	The length of time to wait before giving up on a delete, zero means determine a timeout from the…	v=
o	-t|--tty	Allocated a TTY for each container in the pod	
o	--wait	If true, wait for resources to be gone before returning. This waits for finalizers	
a	1	0
=	run	-f
t	filepaths
=	run	--dry-run
v	none	
v	server	
v	client	
=	run	-k
t	folders
=	run	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	run	--cascade
v	background	
v	orphan	
v	foreground	
=	run	--restart
v	Always	
v	OnFailure	
v	Never	
@	scale
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--resource-version	If non-empty, the annotation update will only succeed if this is the current resource-version for…	v=
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	--all	Select all resources in the namespace of the specified resource types	
o	--current-replicas	Precondition for current size. Requires that the current size of the resource match this value in…	v=
o	--replicas	The new desired number of replicas. Required	v=
o	--timeout	The length of time to wait before giving up on a scale operation, zero means don't wait. Any other…	v
a	2	0
=	scale	-f
t	filepaths
=	scale	-k
t	folders
=	scale	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
=	scale	--dry-run
v	none	
v	server	
v	client	
#	scale	1
d
#	scale	2
d
@	set
s	env	Update environment variables on a pod template
s	image	Update existing container image(s) of resources
s	resources	Specify compute resource requirements (cpu, memory) for any resource that defines a pod template…
s	selector	Set the selector on a resource. Note that the new selector will overwrite the old selector if the…
s	serviceaccount	Update ServiceAccount of pod template resources
s	subject	Update User, Group or ServiceAccount in a RoleBinding/ClusterRoleBinding
@	set env
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--all	If true, select all resources in the namespace of the specified resource types	
o	-c|--containers	The names of containers in the selected pod templates to change - may use wildcards	v=
o	-e|--env	Specify a key-value pair for an environment variable to set into each container	v=
o	--from	The name of a resource from which to inject environment variables	v=
o	--keys	Comma-separated list of keys to import from specified resource	v=
o	--list	If true, display the environment and any changes in the standard format. this flag will removed…	
o	--overwrite	If true, allow environment to be overwritten, otherwise reject updates that overwrite existing…	
o	--prefix	Prefix to append to variable names	v
o	--resolve	If true, show secret or configmap references when listing variables	
a	3	1
=	set env	--dry-run
v	none	
v	server	
v	client	
=	set env	-f
t	filepaths
=	set env	-k
t	folders
=	set env	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	set env	1
d
#	set env	2
d
@	set image
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
a	3	1
=	set image	--dry-run
v	none	
v	server	
v	client	
=	set image	-f
t	filepaths
=	set image	-k
t	folders
=	set image	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	set image	1
d
#	set image	2
d
@	set resources
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	-c|--containers	The names of containers in the selected pod templates to change, all containers are selected by…	v=
o	--limits	The resource requirement requests for this container. For example, 'cpu=100m,memory=256Mi'. Note…	v=
o	--requests	The resource requirement requests for this container. For example, 'cpu=100m,memory=256Mi'. Note…	v=
a	2	0
=	set resources	--dry-run
v	none	
v	server	
v	client	
=	set resources	-f
t	filepaths
=	set resources	-k
t	folders
=	set resources	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	set resources	1
d
#	set resources	2
d
@	set selector
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--resource-version	If non-empty, the annotation update will only succeed if this is the current resource-version for…	v=
o	--all	Select all resources in the namespace of the specified resource types	v
a	3	0
=	set selector	--dry-run
v	none	
v	server	
v	client	
=	set selector	-f
t	filepaths
=	set selector	-k
t	folders
=	set selector	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	set selector	1
d
#	set selector	2
d
@	set serviceaccount
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
a	2	0
=	set serviceaccount	--dry-run
v	none	
v	server	
v	client	
=	set serviceaccount	-f
t	filepaths
=	set serviceaccount	-k
t	folders
=	set serviceaccount	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	set serviceaccount	1
d
#	set serviceaccount	2
d
@	set subject
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	-k|--kustomize	Process the kustomization directory. This flag can't be used together with -f or -R	v
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--record	Record current kubectl command in the resource annotation. If set to false, do not record the…	
o	--all	Select all resources, including uninitialized ones, in the namespace of the specified resource types	
o	--group	Groups to bind to the role	v=
o	--serviceaccount	Service accounts to bind to the role	v=
a	2	0
=	set subject	--dry-run
v	none	
v	server	
v	client	
=	set subject	-f
t	filepaths
=	set subject	-k
t	folders
=	set subject	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	set subject	1
d
#	set subject	2
d
@	taint
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--all	Select all nodes in the cluster	
o	--overwrite	If true, allow taints to be overwritten, otherwise reject taint updates that overwrite existing…	
o	--validate	If true, use a schema to validate the input before sending it	
a	1	0
=	taint	--dry-run
v	none	
v	server	
v	client	
=	taint	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
#	taint	1
d
@	top
@	uncordon
o	--dry-run	Must be "none", "server", or "client". If client strategy, only print the object that would be…	v=
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
a	1	0
=	uncordon	--dry-run
v	none	
v	server	
v	client	
#	uncordon	1
d
@	version
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	--client	If true, shows client version only (no server required)	
=	version	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	
@	wait
o	--allow-missing-template-keys	If true, ignore any errors in templates when a field or map key is missing in the template. Only…	
o	--field-selector	Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector…	v=
o	-f|--filename	Filename, directory, or URL to files identifying the resource	v
o	--local	If true, annotation will NOT contact api-server but run locally	
o	-o|--output	Output format. One of: json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|j…	v
o	-R|--recursive	Process the directory used in -f, --filename recursively. Useful when you want to manage related…	
o	-l|--selector	Selector (label query) to filter on, not including uninitialized ones, supports '=', '==', and…	v
o	--template	Template string or path to template file to use when -o=go-template, -o=go-template-file. The…	v=
o	--all	Select all resources in the namespace of the specified resource types	
o	-A|--all-namespaces	If present, list the requested object(s) across all namespaces. Namespace in current context is…	v
o	--for	The condition to wait on: [delete|condition=condition-name]	v=
o	--timeout	The length of time to wait before giving up. Zero means check once and don't wait, negative means…	v=
a	1	0
=	wait	-f
t	filepaths
=	wait	-o
v	json	
v	yaml	
v	name	
v	go-template	
v	go-template-file	
v	template	
v	templatefile	
v	jsonpath	
v	jsonpath-file	

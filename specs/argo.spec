@	
s	archive	Manage the workflow archive
s	auth	Manage authentication settings
s	cluster-template|cwftmpl|cwft	Manipulate cluster workflow templates
s	completion	Output shell completion code for the specified shell (bash or zsh)
s	cp	Copy artifacts from workflow
s	cron	Manage cron workflows
s	delete	Delete workflows
s	executor-plugin	Manage executor plugins
s	get	Display details about a workflow
s	help	Help about any command
s	lint	Validate files or directories of manifests
s	list	List workflows
s	logs	View logs of a pod or workflow
s	node	Perform action on a node in a workflow
s	resubmit	Resubmit one or more workflows
s	resume	Resume zero or more workflows
s	retry	Retry zero or more workflows
s	server	Start the Argo Server
s	stop	Stop zero or more workflows allowing all exit handlers to run
s	submit	Submit a workflow
s	suspend	Suspend zero or more workflow
s	template	Manipulate workflow templates
s	terminate	Terminate zero or more workflows immediately
s	version	Print version information
s	wait	Waits for workflows to complete
s	watch	Watch a workflow until it completes
o	--argo-base-href	An path to use with HTTP client (e.g. due to BASE_HREF). Defaults to the ARGO_BASE_HREF…	vp
o	--argo-http1	If True, Use the HTTP client. Defaults to the ARGO_HTTP1 environment variable	p
o	--argo-server|-s	API server host:port. e.g. localhost:2746. Defaults to the ARGO_SERVER environment variable	vp
o	--as	Username to impersonate for the operation	vp
o	--as-group	Group to impersonate for the operation, This flag can be repeated to specify multiple groups	vp
o	--as-uid	UID to impersonate for the operation	vp
o	--certificate-authorityk	Path to a cert file for the certificate authority	vp
o	--client-certificate	Path to a client certificate file for TLS	vp
o	--client-key	Path to a client key file for TLS	vp
o	--cluster	The name of the kubeconfig cluster to use	vp
o	--context	The name of the kubeconfig context to use	vp
o	--gloglevel	Set the glog logging level	vp
o	--header|-H	Sets additional header to all requests made by Argo CLI. (Can be repeated multiple times to add…	vp
o	--help|-h	Help for argo	p
o	--insecure-skip-tls-verify	If True, The server's certificate will not be checked for validity. This will make your HTTPS…	p
o	--insecure-skip-verify|-k	If true the Argo Server's certificate will not be checked for validity. This will make your HTTPS…	p
o	--instanceid	Submit with a specific controller's instance id label. Default to the ARGO_INSTANCEID environment…	vp
o	--kubeconfig	Path to a kube config. Only required if out-of-cluster	vp
o	--loglevel	Set the logging level. One of: debug|info|warn|error (default "info")	vp
o	--namespace|-n	If present the namespace scope for this CLI request	vp
o	--password	Password for basic authentication to the API server	vp
o	--proxy-url	This URL will be used to connect via proxy	vp
o	--request-timeout	The length of time to wait before giving up on a single server request. Non-zero values should…	vp
o	--secure|-e	Whether or not the server is using TLS with the Argo Server. Defaults to the ARGO_SECURE…	p
o	--server	The address and port of the Kubernetes API server	vp
o	--tls-server-name	If Provided, This name will be used to validate server certificate. If this is not provided	vp
o	--token	Bearer token for authentication to the API server	vp
o	--user	The name of the kubeconfig user to use	vp
o	--username	Username for basic authentication to the API server	vp
o	--verbose|-v	Enabled verbose logging i.e. --loglevel debug	p
@	archive
s	delete	Delete a workflow in the archive
s	get	Get a workflow in the archive
s	list	List workflows in the archive
s	list-label-keys	List workflows label keys in the archive
s	list-label-values	Get workflow label values in the archive
s	resubmit	Resubmit one or more workflows
s	retry	Retry zero or more workflows
@	archive delete
a	1	0
@	archive get
o	--output|-o	Output format. One of: json|yaml|wide (default "wide")	v
a	1	0
@	archive list
o	--chunk-size	Return large lists in chunks rather than all at once. Pass 0 to disable	v
o	--help|-h	Help for list	
o	--output|-o	Output format. One of: json|yaml|wide (default "wide")	v
o	--selector|-l	Selector (label query) to filter on not including uninitialized ones supports '=' '==' and…	v
@	archive list-label-keys
@	archive list-label-values
o	--help|-h	Help for list-label-values	
o	--selector|-l		v
@	archive resubmit
o	--field-selector	Selector (field query) to filter on supports '=' '==' and '!='.(e.g. --field-selector…	v
o	--help|-h	Help for resubmit	
o	--log	Log the workflow until it completes	
o	--memoized	Re-use successful steps & outputs from the previous run	
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--parameter|-p	Input parameter to override on the original workflow spec	v
o	--priority	Workflow priority	v
o	--selector|-l	Selector (label query) to filter on not including uninitialized ones supports '=' '==' and…	v
o	--wait|-w	Wait for the workflow to complete only works when a single workflow is resubmitted	
o	--watch	Watch the workflow until it completes only works when a single workflow is resubmitted	
a	1	0
@	archive retry
o	--field-selector	Selector (field query) to filter on, supports '='	v
o	--help|-h	Help for retry	
o	--log	Log the workflow until it completes	
o	--node-field-selector	Selector of nodes to reset eg: --node-field-selector inputs.paramaters.myparam.value=abc	v
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--parameter|-p	Input parameter to override on the original workflow spec	v
o	--restart-successful	Indicates to restart successful nodes matching the --node-field-selector	
o	--selector|-l	Selector (label query) to filter on not including uninitialized ones supports '=' '=='	v
o	--wait|-w	Wait for the workflow to complete only works when a single workflow is retried	
o	--watch	Watch the workflow until it completes only works when a single workflow is retried	
a	1	0
@	auth
s	token	Print the auth token
@	auth token
@	cluster-template
s	create	Create a cluster workflow template
s	delete	Delete a cluster workflow template
s	get	Display details about a cluster workflow template
s	lint	Validate files or directories of cluster workflow template manifests
s	list	List cluster workflow templates
@	cluster-template create
o	--help|-h	Help for create	
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--strict	Perform strict workflow validation (default true)	
a	1	0
@	cluster-template delete
o	--all	Delete all cluster workflow templates	
o	--help|-h	Help for delete	
a	1	0
@	cluster-template get
o	--help|-h	Help for get	
o	--output|-o	Output format. One of: json|yaml|wide	v
a	2	0
@	cluster-template lint
o	--help|-h	Help for lint	
o	--output|-o	Linting results output format. One of: pretty|simple (default "pretty")	v
o	--strict	Perform strict workflow validation (default true)	
a	1	0
@	cluster-template list
o	--help|-h	Help for list	
o	--output|-o	Output format. One of: wide|name	v
@	completion
o	--help|-h	Help for completion	
a	1	0
@	cp
o	--artifact-name	Name of output artifact in workflow	v
o	--help|-h	Help for cp	
o	--node-id	Id of node in workflow	v
o	--path	Use variables {workflowName} {nodeId} {templateName} {artifactName} and {namespace} to create a…	v
o	--template-name	Name of template in workflow	v
a	2	0
@	cron
s	create	Create a cron workflow
s	delete	Delete a cron workflow
s	get	Display details about a cron workflow
s	lint	Validate files or directories of cron workflow manifests
s	list	List cron workflows
s	resume	Resume zero or more cron workflows
s	suspend	Suspend zero or more cron workflows
o	--help	Help for cron	
@	cron create
o	--entrypoint	Override entrypoint	v
o	--generate-name	Override metadata.generateName	v
o	--help|-h	Help for create	
o	--labels|-l	Comma separated labels to apply to the workflow. Will override previous values	v
o	--name	Override metadata.name	v
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--parameter|-p	Pass an input parameter	v
o	--parameter-file|-f	Pass a file containing all input parameters	v
o	--schedule	Override cron workflow schedule	v
o	--serviceaccount	Run all pods in the workflow using specified serviceaccount	v
o	--strict	Perform strict workflow validation (default true)	
a	1	0
@	cron delete
o	--all	Delete all cron workflows	
o	--help|-h	Help for delete	
a	1	0
@	cron get
o	--help|-h	Help for get	
o	--output|-o	Output format. One of: json|yaml|wide	v
a	1	0
@	cron lint
o	--help|-h	Help for lint	
o	--output|-o	Linting results output format. One of: pretty|simple (default "pretty")	v
o	--strict	Perform strict validation (default true)	
a	1	0
@	cron list
o	--all-namespaces|-A	Show workflows from all namespaces	
o	--chunk-size	Return large lists in chunks rather than all at once. Pass 0 to disable	v
o	--completed	Show completed workflows. Mutually exclusive with --running	
o	--field-selector	Selector (field query) to filter on. Supports '=' '==' and '!='.(e.g. --field-selector…	v
o	--help|-h	Help for list	
o	--no-headers	Don't print headers (default print headers)	
o	--older	List completed workflows finished before the specified duration (e.g. 10m 3h 1d)	v
o	--output|-o	Output format. One of: name|wide|yaml|json	v
o	--prefix	Filter workflows by prefix	v
o	--resubmitted	Show resubmitted workflows	
o	--running	Show running workflows. Mutually exclusive with --completed	
o	--selector|-l	Selector (label query) to filter on	v
o	--since	Show only workflows created after than a relative duration	v
o	--status	Filter by status (comma separated)	v
@	cron resume
a	1	0
@	cron suspend
a	1	0
@	delete
o	--all	Delete all workflows	
o	--all-namespaces|-A	Delete workflows from all namespaces	
o	--completed	Delete completed workflows	
o	--dry-run	Do not delete the workflow only print what would happen	
o	--field-selector	Selector (field query) to filter on supports '=' '==' and '!='.(e.g. --field-selector…	v
o	--force	Force delete workflows by removing finalizers	
o	--help|-h	Help for delete	
o	--older	Delete completed workflows finished before the specified duration (e.g. 10m 3h 1d)	v
o	--prefix	Delete workflows by prefix	v
o	--resubmitted	Delete resubmitted workflows	
o	--selector|-l	Selector (label query) to filter on not including uninitialized ones supports '=''=='and…	v
a	1	0
@	executor-plugin
s	build	Build an executor plugin
@	executor-plugin build
a	1	0
@	get
o	--help|-h	Help for get	
o	--no-color	Disable colorized output	
o	--no-utf8	Use plain 7-bits ascii characters	
o	--node-field-selector	Selector of node to display, Eg: --node-field-selector phase=abc	v
o	--output|-o	Output format. One of: json|yaml|short|wide	v
o	--status	Filter by status (Pending, Running, Succeeded, Skipped, Failed, Error)	v
a	1	0
@	help
@	lint
o	--help|-h	Help for lint	
o	--kinds	Which kinds will be linted. Can be: workflows|workflowtemplates|cronworkflows|clusterworkflowtempla…	v
o	--offline	Perform offline linting	
o	--output|-o	Linting results output format. One of: pretty|simple (default "pretty")	v
o	--strict	Perform strict workflow validation (default true)	
a	1	0
@	list
o	--all-namespaces|-A	Show workflows from all namespaces	
o	--chunk-size	Return large lists in chunks rather than all at once. Pass 0 to disable	v
o	--completed	Show completed workflows. Mutually exclusive with --running	
o	--field-selector	Selector (field query) to filter on supports '=' '==' and '!='.(e.g. --field-selector…	v
o	--help|-h	Help for list	
o	--no-headers	Don't print headers (default print headers)	
o	--older	List completed workflows finished before the specified duration (e.g. 10m 3h 1d)	v
o	--output|-o	Output format. One of: name|wide|yaml|json	v
o	--prefix	Filter workflows by prefix	v
o	--resubmitted	Show resubmitted workflows	
o	--running	Show running workflows. Mutually exclusive with --completed	
o	--selector|-l	Selector (label query) to filter on not including uninitialized ones supports '=' '==' and…	v
o	--since	Show only workflows created after than a relative duration	v
o	--status	Filter by status (comma separated)	v
@	logs
o	--container|-c	Print the logs of this container (default "main")	v
o	--follow|-f	Specify if the logs should be streamed	
o	--grep	Grep for lines	v
o	--help|-h	Help for logs	
o	--no-color	Disable colorized output	
o	--previous|-p	Specify if the previously terminated container logs should be returned	
o	--selector|-l	Log selector for some pod	v
o	--since	Only return logs newer than a relative duration like 5s 2m or 3h. Defaults to all logs. Only one…	v
o	--since-time	Only return logs after a specific date (RFC3339). Defaults to all logs. Only one of since-time /…	v
o	--tail	If set the number of lines from the end of the logs to show. If not specified logs are shown from…	v
o	--timestamps	Include timestamps on each line in the log output	
a	2	0
@	node
o	--help|-h	Help for node	
o	--message|-m	Set the message of a node eg: --message "Hello World"	v
o	--node-field-selector	Selector of node to set eg: --node-field-selector inputs.paramaters.myparam.value=abc	v
o	--output-parameter|-p	Set a "supplied" output parameter of node eg: --output-parameter parameter-name="Hello world!"	v
o	--phase	Phase to set the node to eg: --phase Succeeded	v
a	3	0
@	resubmit
o	--field-selector	Selector (field query) to filter on: supports '=' '==' and '!='.(e.g. --field-selector…	v
o	--help|-h	Help for resubmit	
o	--log	Log the workflow until it completes	
o	--memoized	Re-use successful steps & outputs from the previous run	
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--parameter|-p	Input parameter to override on the original workflow spec	v
o	--priority	Workflow priority	v
o	--selector|-l	Selector (label query) to filter on	v
o	--wait|-w	Wait for the workflow to complete - only works when a single workflow is resubmitted	
o	--watch	Watch the workflow until it completes - only works when a single workflow is resubmitted	
a	1	0
@	resume
o	--help|-h	Help for resume	
o	--node-field-selector	Selector of node to resume, Eg: --node-field-selector inputs.paramaters.myparam.value=abc	v
a	2	0
@	retry
o	--field-selector	Selector (field query) to filter on, Supports '='; '=='; and '!='.(e.g. --field-selector…	v
o	--help|-h	Help for retry	
o	--log	Log the workflow until it completes	
o	--node-field-selector	Selector of nodes to reset; eg: --node-field-selector inputs.paramaters.myparam.value=abc	v
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--parameter|-p	Input parameter to override on the original workflow spec	v
o	--restart-successful	Indicates to restart successful nodes matching the --node-field-selector	
o	--selector|-l	Selector (label query) to filter on; not including uninitialized ones supports '=' '==' and…	v
o	--wait|-w	Wait for the workflow to complete only works when a single workflow is retried	
o	--watch	Watch the workflow until it completes only works when a single workflow is retried	
a	1	0
@	server
o	--access-control-allow-origin	Set Access-Control-Allow-Origin header in HTTP responses	v
o	--allowed-link-protocol	Allowed link protocol in configMap. Used if the allowed configMap links protocol are different…	v
o	--api-rate-limit	Set limit per IP for api ratelimiter (default 1000)	v
o	--auth-mode	API server authentication mode. Any 1 or more length permutation of: client server sso (default…	v
o	--basehref	Value for base href in index.html. Used if the server is running behind reverse proxy under…	v
o	-b|--browser	Enable automatic launching of the browser [local mode]	
o	--configmap	Name of K8s configmap to retrieve workflow controller configuration (default…	v
o	--event-async-dispatch	Dispatch event async	
o	--event-operation-queue-size	How many events operations that can be queued at once (default 16)	v
o	--event-worker-count	How many event workers to run (default 4)	v
o	-h|--help	Help for server	
o	--hsts	Whether or not we should add a HTTP Secure Transport Security header. This only has effect if…	
o	--log-format	The formatter to use for logs. One of: text|json (default "text")	v
o	--managed-namespace	Namespace that watches default to the installation namespace	v
o	--namespaced	Run as namespaced mode	
o	-p|--port	Port to listen on (default 2746)	v
o	--tls-certificate-secret-name	The name of a Kubernetes secret that contains the server certificates	v
o	--x-frame-options	Set X-Frame-Options header in HTTP responses. (default "DENY")	v
@	stop
o	--dry-run	If true, only stop the workflows that would be stopped, without stopping them	
o	--field-selector	Selector (field query) to filter on supports '=' '==' and '!='.(e.g. --field-selector…	v
o	-h|--help	Help for stop	
o	--message	Message to add to previously running nodes	v
o	--node-field-selector	Selector of node to stop eg: --node-field-selector inputs.paramaters.myparam.value=abc	v
o	-l|--selector	Selector (label query) to filter on not including uninitialized ones supports '=' '==' and…	v
a	2	0
@	submit
o	--dry-run	Modify the workflow on the client-side without creating it	
o	--entrypoint	Override entrypoint	v
o	--from	Submit from an existing kind/name E.g. --from=cronwf/hello-world-cwf	v
o	--generate-name	Override metadata.generateName	v
o	-h|--help	Help for submit	
o	-l|--labels	Comma separated labels to apply to the workflow. Will override previous values	v
o	--log	Log the workflow until it completes	
o	--name	Override metadata.name	v
o	--node-field-selector	Selector of node to display eg: --node-field-selector phase=abc	v
o	-o|--output	Output format. One of: name|json|yaml|wide	v
o	-p|--parameter	Pass an input parameter	v
o	-f|--parameter-file	Pass a file containing all input parameters	v
o	--priority	Workflow priority	v
o	--scheduled-time	Override the workflow's scheduledTime parameter (useful for backfilling). The time must be RFC3339	v
o	--server-dry-run	Send request to server with dry-run flag which will modify the workflow without creating it	
o	--serviceaccount	Run all pods in the workflow using specified serviceaccount	v
o	--status	Filter by status (Pending Running Succeeded Skipped Failed Error). Should only be used with --watch	v
o	--strict	Perform strict workflow validation (default true)	
o	-w|--wait	Wait for the workflow to complete	
o	--watch	Watch the workflow until it completes	
a	1	0
@	suspend
o	-h|--help	Help for suspend	
a	2	0
@	template
s	create	Create a workflow template
s	delete	Delete a workflow template
s	get	Display details about a workflow template
s	lint	Validate a file or directory of workflow template manifests
s	list	List workflow templates
o	-h|--help	Help for template	
@	template create
o	--help|-h	Help for create	
o	--output|-o	Output format. One of: name|json|yaml|wide	v
o	--strict	Perform strict workflow validation (default true)	
a	2	0
@	template delete
o	--all	Delete all workflow templates	
o	-h|--help	Help for delete	
a	1	0
@	template get
o	-h|--help	Help for get	
o	-o|--output	Output format. One of: json|yaml|wide	v
a	1	0
@	template lint
o	--help|-h	Help for lint	
o	--output|-o	Linting results output format. One of: pretty|simple (default "pretty")	v
o	--strict	Perform strict workflow validation (default true)	
a	2	0
@	template list
o	--all-namespaces|-A	Show workflows from all namespaces	
o	--help|-h	Help for list	
o	--output|-o	Output format. One of: wide|name	v
@	terminate
o	--dry-run	Do not terminate the workflow only print what would happen	
o	--field-selector	Selector (field query) to filter on supports '=' '==' and '!='.(e.g. --field-selector…	v
o	-h|--help	Help for terminate	
o	-l|--selector	Selector (label query) to filter on not including uninitialized ones supports '=' '==' and…	v
a	1	0
@	version
o	--help|-h	Help for version	
o	--short	Print just the version number	
@	wait
o	-h|--help	Help for wait	
o	--ignore-not-found	Ignore the wait if the workflow is not found	
a	1	0
@	watch
o	-h|--help	Help for watch	
o	--node-field-selector	Selector of node to display eg: --node-field-selector phase=abc	v
o	--status	Filter by status (Pending, Running, Succeeded, Skipped, Failed, Error)	v
a	1	0

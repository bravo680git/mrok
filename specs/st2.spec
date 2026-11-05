@	
s	run	Invoke an action manually
s	action	An activity that happens as a response to the external event
s	action-alias	Action aliases
s	auth	Authenticate user and acquire access token
s	login	Authenticate user, acquire access token, and update CLI config directory
s	whoami	Display the currently authenticated user
s	apikey	API Keys
s	execution	An invocation of an action
s	inquiry	Inquiries provide an opportunity to ask a question and wait for a response in a workflow
s	key	Key value pair is used to store commonly used configuration for reuse in sensors, actions, and rules
s	pack	A group of related integration resources: actions, rules, and sensors
s	policy	Policy that is enforced on a resource
s	policy-type	Type of policy that can be applied to the resources
s	rule	A specification to invoke an 'action' on a 'trigger' selectively based on some criteria'
s	webhook	Webhooks
s	timer	Timers
s	runner	Runner is a type of handler for a specific class of actions
s	sensor	An adapter which allows you to integrate StackStorm with external system
s	trace	A group of executions, rules and triggerinstances that are related
s	trigger	An external event that is mapped to a st2 input. It is the st2 invocation point
s	trigger-instance	Actual instances of triggers received by st2
s	rule-enforcement	Models that represent enforcement of rules
s	workflow	An adapter which allows you to integrate StackStorm with external system
s	service-registry	Service registry group and membership related commands
s	role	RBAC roles
s	role-assignment	RBAC role assignments
o	--help|-h	Show this help message and exit	
o	--version	Show program's version number and exit	
o	--url	Base URL for the API servers. Assumes all servers use the same base URL and default ports are…	v
o	--auth-url	URL for the authentication service. Get ST2_AUTH_URL from the environment variables by default	v
o	--api-url	URL for the API server. Get ST2_API_URL from the environment variables by default	v
o	--stream-url	URL for the stream endpoint. Get ST2_STREAM_URLfrom the environment variables by default	v
o	--api-version	API version to use. Get ST2_API_VERSION from the environment variables by default	v
o	--cacert	Path to the CA cert bundle for the SSL endpoints. Get ST2_CACERT from the environment variables by…	v
o	--config-file	Path to the CLI config file	v
o	--print-config	Parse the config file and print the values	
o	--skip-config	Don't parse and use the CLI config file	
o	--debug	Enable debug mode	
@	run
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-h|--help	Show this help and exit	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	--delay	How long (in milliseconds) to delay the execution before scheduling	v
o	--tail	Automatically start tailing new execution	
o	--auto-dict	Automatically convert list items to dictionaries when colons are detected. (NOTE - this parameter…	
o	--trace-tag|--trace_tag	A trace tag string to track execution later	v
o	--trace-id	Existing trace id for this execution	v
o	-a|--async	Do not wait for action to finish	
o	-e|--inherit-env	Pass all the environment variables which are accessible to the CLI as 'env' parameter to the…	
o	-u|--user	User under which to run the action (admins only)	v
a	2	1
=	run	-u
d
@	action
s	list	Get the list of actions
s	get	Get individual action
s	create	Create a new action
s	update	Update an existing action
s	delete	Delete an existing action
s	enable	Enable an existing action
s	disable	Disable an existing action
s	execute	Invoke an action manually
@	action list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-p|--pack	Only return resources belonging to the provided pack	v
@	action get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	action create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	action create	1
t	filepaths
@	action update
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	2	0
#	action update	2
t	filepaths
@	action delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-r|--remove-files	Remove action files from disk	
a	1	0
@	action enable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	action disable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	action execute
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	--delay	How long (in milliseconds) to delay the execution before scheduling	v
o	--tail	Automatically start tailing new execution	
o	--auto-dict	Automatically convert list items to dictionaries when colons are detected. (NOTE - this parameter…	
o	--trace-tag|--trace_tag	A trace tag string to track execution later	v
o	--trace-id	Existing trace id for this execution	v
o	-a|--async	Do not wait for action to finish	
o	-e|--inherit-env	Pass all the environment variables which are accessible to the CLI as 'env' parameter to the…	
o	-u|--user	User under which to run the action (admins only)	v
a	2	1
=	action execute	-u
d
@	action-alias
s	list	Get the list of action aliases
s	get	Get the individual action aliases
s	create	Create a new action alias
s	update	Update an existing action alias
s	delete	Delete an existing action alias
s	match	Get the action alias that match the command text
s	execute	Execute the command text by finding a matching action alias
@	action-alias list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-p|--pack	Only return resources belonging to the provided pack	v
@	action-alias get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	action-alias create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	action-alias create	1
t	filepaths
@	action-alias update
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	2	0
#	action-alias update	2
t	filepaths
@	action-alias delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	action-alias match
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
a	1	0
@	action-alias execute
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-u|--user	User under which to run the action (admins only)	v
a	1	0
=	action-alias execute	-u
d
@	auth
o	-h|--help	Show this help and exit	
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-p	Password	v
o	-l|--ttl	The life span of the token in seconds. Max TTL configured by the admin supersedes this	v
o	-t|--only-token	On successful authentication, print only token to the console	
a	1	0
@	login
o	-h|--help	Show this help and exit	
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-p	Password	v
o	-l|--ttl	The life span of the token in seconds. Max TTL configured by the admin supersedes this	v
o	-w|--write-password	Write the password in plain text to the config file (default is to omit it)	
a	1	0
@	whoami
o	-h|--help	Show this help and exit	
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
@	apikey
s	list	Get the list of api keys
s	get	Get individual api key
s	create	Create a new api key
s	delete	Delete an existing api key
s	enable	Enable an existing api key
s	disable	Disable an existing api key
s	load	Load api key from a file
@	apikey list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-u|--user	User under which to run the action (admins only)	v
o	-d|--detail	Display full detail of the execution in table format	
o	--show-secrets	Full list of attributes	
=	apikey list	-u
d
@	apikey get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	0
@	apikey create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-u|--user	User under which to run the action (admins only)	v
o	-m|--metadata	Optional metadata to associate with the API Keys	v
o	-k|--only-key	Only print API Key to the console on creation	
=	apikey create	-u
d
@	apikey delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	apikey enable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	apikey disable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	apikey load
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	apikey load	1
t	filepaths
@	execution
s	list	Get the list of the 50 most recent action executions
s	get	Get individual action execution
s	re-run	Re-run a particular action
s	cancel	Cancel action executions
s	pause	Pause action executions (workflow executions only)
s	resume	Resume action executions (workflow executions only)
s	tail	Tail output of a particular execution
@	execution list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-n|--last	List N most recent; use -n -1 to fetch the full result set	v
o	-s|--sort	Sort action executions by start timestamp, asc|ascending (earliest first) or desc|descending…	v
o	-tg|timestamp-gt	Only return executions with timestamp greater than the one provided. Use time in the format…	v
o	-tl|timestamp-lt	Only return executions with timestamp lower than the one provided. Use time in the format…	v
o	-l|--showall	Show all attributes	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	--action	Action reference to filter the list	v
o	--status	Only return executions with the provided status. Possible values are 'succeeded', 'running'…	v
o	-u|--user	User under which to run the action (admins only)	v
o	--trigger_instance	Trigger instance id to filter the list	v
=	execution list	-n
v	10	
v	5	
v	1	
v	-1	
=	execution list	-s
v	desc	
v	descending	
v	asc	
v	ascending	
=	execution list	--status
v	succeeded	
v	running	
v	scheduled	
v	paused	
v	failed	
v	canceling	
v	canceled	
=	execution list	-u
d
@	execution get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-x|--exclude-result	Don't retrieve and display the result field	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	--delay	How long (in milliseconds) to delay the execution before scheduling	v
o	--tail	Automatically start tailing new execution	
o	--auto-dict	Automatically convert list items to dictionaries when colons are detected. (NOTE - this parameter…	
a	1	1
@	execution re-run
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--tasks	Name of the workflow tasks to re-run	v
o	--no-reset	Name of the with-items tasks to not reset. This only applies to Orquesta workflows. By default…	v
o	-a|--async	Do not wait for action to finish	
o	-e|--inherit-env	Pass all the environment variables which are accessible to the CLI as 'env' parameter to the…	
o	-h|--help	Show this help and exit	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	--delay	How long (in milliseconds) to delay the execution before scheduling	v
o	--tail	Automatically start tailing new execution	
o	--auto-dict	Automatically convert list items to dictionaries when colons are detected. (NOTE - this parameter…	
a	2	1
@	execution cancel
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	1
@	execution pause
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	--delay	How long (in milliseconds) to delay the execution before scheduling	v
o	--tail	Automatically start tailing new execution	
o	--auto-dict	Automatically convert list items to dictionaries when colons are detected. (NOTE - this parameter…	
a	1	1
@	execution resume
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
o	-k|--key	If result is type of JSON, then print specific key-value pair; dot notation for nested JSON is…	v
o	--delay	How long (in milliseconds) to delay the execution before scheduling	v
o	--tail	Automatically start tailing new execution	
o	--auto-dict	Automatically convert list items to dictionaries when colons are detected. (NOTE - this parameter…	
a	1	1
@	execution tail
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--type	Type of output to tail for. If not provided, defaults to all	v
o	--include-metadata	Include metadata (timestamp, output type) with the output	
a	1	0
@	inquiry
s	list	Get the list of the 50 most recent inquiries
s	get	Get individual inquiry
s	respond	Respond to an inquiry
@	inquiry list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-n|--last	List N most recent; use -n -1 to fetch the full result set	v
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
=	inquiry list	-n
v	10	
v	5	
v	1	
v	-1	
@	inquiry get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	inquiry respond
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-r|--response	Entire response payload as JSON string (bypass interactive mode)	v
a	1	0
@	key
s	list	Get the list of the 50 most recent key value pairs
s	get	Get individual key value pair
s	delete	Delete an existing key value pair
s	set	Set an existing key value pair
s	load	Load a list of key value pairs from file
s	delete_by_prefix	Delete KeyValue pairs which match the provided prefix
@	key list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	--prefix	Only return values with names starting with the provided prefix	v
o	-d|--decrypt	Decrypt secrets and displays plain text	
o	-s|--scope	Scope item is under. Example: 'user'	
o	-u|--user	User under which to run the action (admins only)	v
o	-n|--last	List N most recent; use -n -1 to fetch the full result set	v
=	key list	-u
d
=	key list	-n
v	10	
v	5	
v	1	
v	-1	
@	key get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--decrypt	Decrypt secrets and displays plain text	
o	-s|--scope	Scope item is under. Example: 'user'	
a	1	1
@	key delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-s|--scope	Scope item is under. Example: 'user'	
o	-u|--user	User under which to run the action (admins only)	v
a	1	0
=	key delete	-u
d
@	key set
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-e|--enrypt	Encrypt values before saving	
o	--enrypted	Value provided is already encrypted with the instance crypto key and should be stored as-is	
o	-l|--ttl	The life span of the token in seconds. Max TTL configured by the admin supersedes this	v
o	-s|--scope	Scope item is under. Example: 'user'	
o	-u|--user	User under which to run the action (admins only)	v
a	2	0
=	key set	-u
d
@	key load
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-c|--convert	Convert non-string types (hash, array, boolean, int, float) to a JSON string before loading it…	
a	1	0
#	key load	1
t	filepaths
@	key delete_by_prefix
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--prefix	Only return values with names starting with the provided prefix	v
a	1	0
@	pack
s	list	Get the list of packs
s	get	Get information about an installed pack
s	show	Get information about an available pack from the index
s	search	Search the index for a pack with any attribute matching the query
s	install	Install new packs
s	remove	Remove packs
s	register	Register pack(s): sync all file changes with DB
s	config	Configure a pack based on config schema
@	pack list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
@	pack get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	pack show
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	pack search
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
a	1	0
@	pack install
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-w|--width	Set the width of the columns in output	v
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
o	force	Force	
o	--skip-dependencies	Skip dependencies	
a	1	1
@	pack remove
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-w|--width	Set the width of the columns in output	v
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-d|--detail	Display full detail of the execution in table format	
a	1	1
@	pack register
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--types	Types of content to register	v
a	1	1
@	pack config
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	policy
s	list	Get the list of policies
s	get	Get individual policy
s	create	Create a new policy
s	update	Updating an existing policy
s	delete	Delete an existing policy
@	policy list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-p|--pack	Only return resources belonging to the provided pack	v
o	-r|--resource-ref	Return policies for the resource ref	v
o	-pt|--policy-type	Return policies of the policy type	v
@	policy get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	policy create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	policy create	1
t	filepaths
@	policy update
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	2	0
#	policy update	2
t	filepaths
@	policy delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	policy-type
s	list	Get the list of policy types
s	get	Get individual policy type
@	policy-type list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-r|--resource-type	Return policy types for the resource type	v
@	policy-type get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	0
@	rule
s	list	Get the list of the 50 most recent rules
s	get	Get individual rule
s	create	Create a new rule
s	update	Update an existing rule
s	delete	Delete an existing rule
s	enable	Enable an existing rule
s	disable	Disable an existing rule
@	rule list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-n|--last	List N most recent; use -n -1 to fetch the full result set	v
o	--iftt	Show trigger and action in display list	
o	-p|--pack	Only return resources belonging to the provided pack	v
o	--enabled	Show enabled	
o	--disabled	Show disabled	
o	--action	Action reference to filter the list	v
o	-g|--trigger	Trigger type reference to filter the list	v
=	rule list	-n
v	10	
v	5	
v	1	
v	-1	
@	rule get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	0
@	rule create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	rule create	1
t	filepaths
@	rule update
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	2	0
#	rule update	2
t	filepaths
@	rule delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	rule enable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	rule disable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
a	1	0
@	webhook
s	list	Get the list of webhooks
s	get	Get individual webhooks
@	webhook list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-p|--pack	Only return resources belonging to the provided pack	v
@	webhook get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	timer
s	list	Get the list of timers
s	get	Get individual timer
@	timer list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-ty|--timer-type	List timers type, example: 'core.st2.IntervalTimer', 'core.st2.DateTimer', 'core.st2.CronTimer'	v
=	timer list	-ty
v	core.st2.IntervalTimer	
v	core.st2.DateTimer	
v	core.st2.CronTimer	
@	timer get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	runner
s	list	List of commands for managing runners
s	get	Get individual runner
s	enable	Enable an existing runner
s	disable	Disable an existing runner
@	runner list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
@	runner get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	runner enable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	runner disable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	sensor
s	list	Get the list of sensortypes
s	get	Get individual sensor
s	enable	Enable an existing sensor
s	disable	Disalbe an existing sensor
@	sensor list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-p|--pack	Only return resources belonging to the provided pack	v
@	sensor get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	sensor enable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	sensor disable
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	trace
s	list	Get the list of the 50 most recent traces
s	get	Get individual trace
@	trace list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-n|--last	List N most recent; use -n -1 to fetch the full result set	v
o	-s|--sort	Sort action executions by start timestamp, asc|ascending (earliest first) or desc|descending…	v
o	--trace-tag|--trace_tag	A trace tag string to track execution later	v
o	-e|--execution	Execution to filter the list	v
o	-r|--rule	Rule to filter the list	v
o	--trigger_instance	Trigger instance id to filter the list	v
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
=	trace list	-n
v	10	
v	5	
v	1	
v	-1	
=	trace list	-s
v	desc	
v	descending	
v	asc	
v	ascending	
@	trace get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-e|--execution	Execution to filter the list	v
o	-r|--rule	Rule to filter the list	v
o	--trigger_instance	Trigger instance id to filter the list	v
o	--show-executions	Only show executions	
o	--show-rules	Only show rules	
o	-n|--hide-noop-triggers	Hide noop trigger instances	
a	1	1
@	trigger
s	list	Get the list of triggers
s	get	Get individual trigger
s	create	Create a new trigger
s	update	Updating an existing trigger
s	delete	Delete an existing trigger
s	getspecs	Return Trigger Specifications of a Trigger
@	trigger list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-p|--pack	Only return resources belonging to the provided pack	v
@	trigger get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	trigger create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	trigger create	1
t	filepaths
@	trigger update
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	2	0
#	trigger update	2
t	filepaths
@	trigger delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	trigger getspecs
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	trigger-instance
s	list	Get the list of the 50 most recent triggerinstances
s	get	Get individual trigger instance
s	re-emit	Re-emit a particular trigger instance
@	trigger-instance list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-n|--last	List N most recent; use -n -1 to fetch the full result set	v
o	-tg|timestamp-gt	Only return executions with timestamp greater than the one provided. Use time in the format…	v
o	-tl|timestamp-lt	Only return executions with timestamp lower than the one provided. Use time in the format…	v
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	-g|--trigger	Trigger type reference to filter the list	v
o	--status	Only return executions with the provided status. Possible values are 'succeeded', 'running'…	v
=	trigger-instance list	-n
v	10	
v	5	
v	1	
v	-1	
=	trigger-instance list	--status
v	succeeded	
v	running	
v	scheduled	
v	paused	
v	failed	
v	canceling	
v	canceled	
@	trigger-instance get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	trigger-instance re-emit
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	rule-enforcement
s	list	Get the list of the 50 most recent rule enforcements
s	get	Get individual rule enforcement
s	create	Create a new rule enforcement
s	update	Update an existing rule enforcement
s	delete	Delete an existing rule enforcement
@	rule-enforcement list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-tg|timestamp-gt	Only return executions with timestamp greater than the one provided. Use time in the format…	v
o	-tl|timestamp-lt	Only return executions with timestamp lower than the one provided. Use time in the format…	v
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	--trigger_instance	Trigger instance id to filter the list	v
o	-e|--execution	Execution to filter the list	v
o	-r|--rule	Rule to filter the list	v
@	rule-enforcement get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	rule-enforcement create
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
#	rule-enforcement create	1
t	filepaths
@	rule-enforcement update
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	2	0
#	rule-enforcement update	2
t	filepaths
@	rule-enforcement delete
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
a	1	0
@	workflow
s	inspect	Inspect workflow definition and return the list of errors if any
@	workflow inspect
o	-h|--help	Show this help and exit	
o	--file	Local file path to the workflow definition	v
o	--action	Action reference to filter the list	v
=	workflow inspect	--file
t	filepaths
@	service-registry
s	group	Manage service registry groups
s	member	Manage service registry members
@	service-registry group
s	list	Get list of groups
@	service-registry group list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
@	service-registry member
s	list	Get list of group members
@	service-registry member list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
o	--group-id	Group ID	v
@	role
s	list	Get the list of the roles
s	get	Get individual role
@	role list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-s|--system	Only display system roles	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
@	role get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
a	1	1
@	role-assignment
s	list	Get the list of role assignments
s	get	Get individual assignment
@	role-assignment list
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
@	role-assignment get
o	-h|--help	Show this help and exit	
o	-t|--token	Access token for user authentication. Get ST2_AUTH_TOKEN from the environment variables by default	v
o	--api-key	Api Key for user authentication. Get ST2_API_KEY from the environment variables by default	v
o	-j|--json	Print output in JSON format	
o	-y|--yaml	Print output in YAML format	
o	-r|--role	Role to filter on	v
o	-u|--user	User under which to run the action (admins only)	v
o	-s|--source	Source to filter on	v
o	--remote	Only display remote role assignments	
o	--attr	List of attributes to include in the output. 'all' or unspecified will return all attributes	v
o	-w|--width	Set the width of the columns in output	v
=	role-assignment get	-u
d

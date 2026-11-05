@	
s	about	Print information about the Pulumi environment
s	cancel	Cancel a stack’s currently running update, if any
s	config	Manage configuration
s	console	Opens the current stack in the Pulumi Console
s	destroy	Destroy an existing stack and its resources
s	import	Import resources into an existing stack
s	login	Log in to the Pulumi service
s	logout	Log out of the Pulumi service
s	logs	[PREVIEW] Show aggregated resource logs for a stack
s	new	Create a new Pulumi project
s	org	Manage Organization configuration
s	plugin	Manage language and resource provider plugins
s	policy	Manage resource policies
s	preview	Show a preview of updates to a stack’s resources
s	refresh	Refresh the resources in a stack
s	schema	Analyze package schemas
s	stack	Manage stacks
s	state	Edit the current stack’s state
s	up	Deploy code and/or resource changes
s	version	Print Pulumi’s version number
s	watch	[PREVIEW] Continuously update the resources in a stack
s	whoami	Displays the username of the currently logged in user
o	--help|-h	Show help	p
@	about
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	-t|--transitive	Include transitive dependencies	
=	about	--color
v	always	
v	never	
v	raw	
v	auto	
=	about	-C
t	folders
=	about	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	cancel
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
=	cancel	--color
v	always	
v	never	
v	raw	
v	auto	
=	cancel	-C
t	folders
=	cancel	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	cancel	-s
d
@	config
s	cp	Copy config to another stack
s	get	Get a single configuration value
s	refresh	Update the local configuration based on the most recent deployment of the stack
s	rm	Remove configuration value
s	rm-all	Remove multiple configuration values
s	set	Set configuration value
s	set-all	Set multiple configuration values
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	--show-secrets	Show secret values when listing config instead of displaying blinded values	
=	config	--color
v	always	
v	never	
v	raw	
v	auto	
=	config	-C
t	folders
=	config	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	config	-s
d
=	config	--config-file
t	filepaths,folders
@	config cp
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--path	The key contains a path to a property in a map or list to set	
o	-d|--dest	The name of the new stack to copy the config to	v
=	config cp	--color
v	always	
v	never	
v	raw	
v	auto	
=	config cp	-C
t	folders
=	config cp	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	config cp	-d
d
@	config get
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	--path	The key contains a path to a property in a map or list to get	
a	1	0
=	config get	--color
v	always	
v	never	
v	raw	
v	auto	
=	config get	-C
t	folders
=	config get	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	config refresh
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-f|--force	Overwrite configuration file, if it exists, without creating a backup	
=	config refresh	--color
v	always	
v	never	
v	raw	
v	auto	
=	config refresh	-C
t	folders
=	config refresh	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	config rm
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--path	The key contains a path to a property in a map or list to remove	
a	1	0
=	config rm	--color
v	always	
v	never	
v	raw	
v	auto	
=	config rm	-C
t	folders
=	config rm	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	config rm-all
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--path	Parse the keys as paths in a map or list rather than raw strings	
a	1	1
=	config rm-all	--color
v	always	
v	never	
v	raw	
v	auto	
=	config rm-all	-C
t	folders
=	config rm-all	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	config set
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--path	The key contains a path to a property in a map or list to set	
o	--plaintext	Save the value as plaintext (unencrypted)	
o	--secret	Encrypt the value instead of storing it in plaintext	
a	2	0
=	config set	--color
v	always	
v	never	
v	raw	
v	auto	
=	config set	-C
t	folders
=	config set	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	config set-all
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--path	Parse the keys as paths in a map or list rather than raw strings	
o	--plaintext	Marks a value as plaintext (unencrypted)	v
o	--secret	Marks a value as secret to be encrypted	v
a	1	0
=	config set-all	--color
v	always	
v	never	
v	raw	
v	auto	
=	config set-all	-C
t	folders
=	config set-all	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	console
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
=	console	--color
v	always	
v	never	
v	raw	
v	auto	
=	console	-C
t	folders
=	console	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	console	-s
d
@	destroy
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-p|--parallel	Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to…	v
o	-m|--message	Optional message to associate with the destroy operation	v
o	--diff	Display operation as a rich diff showing the overall change	
o	-d|--debug	Print detailed debugging output during resource operations	
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	--suppress-permalink	Suppress display of the state permalink	v
o	-t|--target	Specify a single resource URN to destroy. All resources necessary to destroy this target will also…	v
o	-j|--json	Serialize the update diffs, operations, and overall output as JSON	
o	-r|--refresh	Refresh the state of the stack's resources before this update	v
o	--show-config	Show configuration keys and variables	
o	--show-replacement-steps	Show detailed resource replacement creates and deletes instead of a single step	
o	--show-sames	Show resources that don't need to be updated because they haven't changed, alongside those that do	
o	--suppress-outputs	Suppress display of stack outputs (in case they contain sensitive values)	
o	--target-dependents	Allows destroying of dependent targets discovered but not specified in --target list	
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	-f|--skip-preview	Do not perform a preview before performing the destroy	
o	--exclude-protected	Do not destroy protected resources. Destroy all other resources	
=	destroy	--color
v	always	
v	never	
v	raw	
v	auto	
=	destroy	-C
t	folders
=	destroy	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	destroy	-s
d
=	destroy	-p
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
=	destroy	--config-file
t	filepaths,folders
=	destroy	--suppress-permalink
v	false	
v	true	
=	destroy	-r
v	false	
v	true	
@	import
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	-d|--debug	Print detailed debugging output during resource operations	
o	--diff	Display operation as a rich diff showing the overall change	
o	-m|--message	Optional message to associate with the destroy operation	v
o	-p|--parallel	Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to…	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	-f|--skip-preview	Do not perform a preview before performing the destroy	
o	--suppress-permalink	Suppress display of the state permalink	v
o	-f|--file	The path to a JSON-encoded file containing a list of resources to import	v
o	-o|--out	The path to the file that will contain the generated resource declarations	v
o	--parent	The name and URN of the parent resource in the format name=urn, where name is the variable name of…	v
o	--protect	Allow resources to be imported with protection from deletion enabled (default true)	
o	--provider	The name and URN of the provider to use for the import in the format name=urn, where name is the…	v
o	--suppress-outputs	Suppress display of stack outputs (in case they contain sensitive values)	
a	3	0
=	import	--color
v	always	
v	never	
v	raw	
v	auto	
=	import	-C
t	folders
=	import	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	import	--config-file
t	filepaths,folders
=	import	-p
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
=	import	-s
d
=	import	--suppress-permalink
v	false	
v	true	
=	import	-f
t	filepaths
@	login
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-l|--local	Use Pulumi in local-only mode	
o	-c|--cloud-url	A cloud URL to log in to	v
o	--default-org	A default org to associate with the login. Please note, currently, only the managed and…	v
a	1	0
=	login	--color
v	always	
v	never	
v	raw	
v	auto	
=	login	-C
t	folders
=	login	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	logout
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-l|--local	Use Pulumi in local-only mode	
o	--all	Logout of all backends	
o	-c|--cloud-url	A cloud URL to log out of (defaults to current cloud)	v
a	1	0
=	logout	--color
v	always	
v	never	
v	raw	
v	auto	
=	logout	-C
t	folders
=	logout	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	logs
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-j|--json	Emit output as JSON	
o	-f|--follow	Follow the log stream in real time (like tail -f)	
o	-r|--resource	Only return logs for the requested resource ('name', 'type::name' or full URN). Defaults to…	v
o	--since	Only return logs newer than a relative duration ('5s', '2m', '3h') or absolute timestamp. Defaults…	v
=	logs	--color
v	always	
v	never	
v	raw	
v	auto	
=	logs	-C
t	folders
=	logs	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	logs	--config-file
t	filepaths,folders
=	logs	-s
d
=	logs	--since
v	5s	
v	2m	
v	3h	
@	new
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	--secrets-provider	The type of the provider that should be used to encrypt and decrypt secrets (possible choices…	v
o	-c|--config	Config to save	v
o	--config-path	Config keys contain a path to a property in a map or list to set	
o	-d|--description	The project description; if not specified, a prompt will request it	v
o	--dir	The location to place the generated project; if not specified, the current directory is used	v
o	-f|--force	Forces content to be generated even if it would change existing files	
o	-g|--generate-only	Generate the project only; do not create a stack, save config, or install dependencies	
o	-n|--name	The project name; if not specified, a prompt will request it	v
o	-o|--offline	Use locally cached templates without making any network requests	
=	new	--color
v	always	
v	never	
v	raw	
v	auto	
=	new	-C
t	folders
=	new	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	new	-s
d
=	new	--secrets-provider
v	default	
v	passphrase	
v	awskms	
v	azurekeyvault	
v	gcpkms	
v	hashivault	
=	new	--dir
t	folders
@	org
s	get-default	Get the default org for the current backend
s	set-default	Set the default organization for the current backend
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	org	--color
v	always	
v	never	
v	raw	
v	auto	
=	org	-C
t	folders
=	org	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	org get-default
@	org set-default
a	1	0
@	plugin
s	install	Install one or more plugins
s	ls	List plugins
s	rm	Remove one or more plugins from the download cache
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	plugin	--color
v	always	
v	never	
v	raw	
v	auto	
=	plugin	-C
t	folders
=	plugin	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	plugin install
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--exact	Force installation of an exact version match (usually >= is accepted)	
o	-f|--file	Install a plugin from a tarball file, instead of downloading it	v
o	--reinstall	Reinstall a plugin even if it already exists	
o	--server	A URL to download plugins from	v
=	plugin install	--color
v	always	
v	never	
v	raw	
v	auto	
=	plugin install	-C
t	folders
=	plugin install	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	plugin install	-f
t	filepaths
@	plugin ls
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	-p|--project	List only the plugins used by the current project	
=	plugin ls	--color
v	always	
v	never	
v	raw	
v	auto	
=	plugin ls	-C
t	folders
=	plugin ls	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	plugin rm
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	-a|--all	Remove all plugins	
=	plugin rm	--color
v	always	
v	never	
v	raw	
v	auto	
=	plugin rm	-C
t	folders
=	plugin rm	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy
s	disable	Disable a Policy Pack for a Pulumi organization
s	enable	Enable a Policy Pack for a Pulumi organization
s	group	Manage policy groups
s	ls	List all Policy Packs for a Pulumi organization
s	new	Create a new Pulumi Policy Pack
s	publish	Publish a Policy Pack to the Pulumi service
s	rm	Removes a Policy Pack from a Pulumi organization
s	validate-config	Validate a Policy Pack configuration
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	policy	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy	-C
t	folders
=	policy	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy disable
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--policy-group	The Policy Group for which the Policy Pack will be disabled; if not specified, the default Policy…	v
o	--version	The version of the Policy Pack that will be disabled; if not specified, any enabled version of the…	v
a	1	0
=	policy disable	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy disable	-C
t	folders
=	policy disable	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy enable
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--policy-group	The Policy Group for which the Policy Pack will be enabled; if not specified, the default Policy…	v
o	--config	The file path for the Policy Pack configuration file	v
a	1	0
=	policy enable	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy enable	-C
t	folders
=	policy enable	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy group
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	policy group	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy group	-C
t	folders
=	policy group	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy ls
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
a	1	0
=	policy ls	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy ls	-C
t	folders
=	policy ls	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy new
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	-o|--offline	Use locally cached templates without making any network requests	
o	-g|--generate-only	Generate the Policy Pack only; do not install dependencies	
o	-f|--force	Forces content to be generated even if it would change existing files	
o	--dir	The location to place the generated Policy Pack; if not specified, the current directory is used	v
a	1	0
=	policy new	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy new	-C
t	folders
=	policy new	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	policy new	--dir
t	folders
@	policy publish
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
a	1	0
=	policy publish	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy publish	-C
t	folders
=	policy publish	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy rm
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
a	1	0
=	policy rm	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy rm	-C
t	folders
=	policy rm	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	policy validate-config
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--config	The file path for the Policy Pack configuration file	v
a	1	0
=	policy validate-config	--color
v	always	
v	never	
v	raw	
v	auto	
=	policy validate-config	-C
t	folders
=	policy validate-config	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	preview
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-p|--parallel	Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to…	v
o	-m|--message	Optional message to associate with the destroy operation	v
o	--diff	Display operation as a rich diff showing the overall change	
o	-d|--debug	Print detailed debugging output during resource operations	
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	--suppress-permalink	Suppress display of the state permalink	v
o	-t|--target	Specify a single resource URN to destroy. All resources necessary to destroy this target will also…	v
o	-j|--json	Serialize the update diffs, operations, and overall output as JSON	
o	-r|--refresh	Refresh the state of the stack's resources before this update	v
o	--show-config	Show configuration keys and variables	
o	--show-replacement-steps	Show detailed resource replacement creates and deletes instead of a single step	
o	--show-sames	Show resources that don't need to be updated because they haven't changed, alongside those that do	
o	--suppress-outputs	Suppress display of stack outputs (in case they contain sensitive values)	
o	--target-dependents	Allows destroying of dependent targets discovered but not specified in --target list	
o	-c|--config	Config to use during the preview	v
o	--config-path	Config keys contain a path to a property in a map or list to set	
o	--expect-no-changes	Return an error if any changes are proposed by this preview	
o	--policy-pack	Run one or more policy packs as part of this update	v
o	--policy-pack-config	Path to JSON file containing the config for the policy pack of the corresponding"--policy-pack" flag	v
o	--replace	Specify resources to replace. Multiple resources can be specified using --replace urn1 --replace…	v
o	--show-reads	Show resources that are being read in, alongside those being managed directly in the stack	
o	--target-replace	Specify a single resource URN to replace. Other resources will not be updated. Shorthand for…	v
=	preview	--color
v	always	
v	never	
v	raw	
v	auto	
=	preview	-C
t	folders
=	preview	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	preview	-s
d
=	preview	-p
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
=	preview	--config-file
t	filepaths,folders
=	preview	--suppress-permalink
v	false	
v	true	
=	preview	-r
v	false	
v	true	
@	refresh
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	-d|--debug	Print detailed debugging output during resource operations	
o	--diff	Display operation as a rich diff showing the overall change	
o	-m|--message	Optional message to associate with the destroy operation	v
o	-p|--parallel	Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to…	v
o	-f|--skip-preview	Do not perform a preview before performing the destroy	
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	--suppress-permalink	Suppress display of the state permalink	v
o	-t|--target	Specify a single resource URN to destroy. All resources necessary to destroy this target will also…	v
o	-j|--json	Serialize the refresh diffs, operations, and overall output as JSON	
o	--expect-no-changes	Return an error if any changes occur during this update	
o	--show-replacement-steps	Show detailed resource replacement creates and deletes instead of a single step	
o	--show-sames	Show resources that needn't be updated because they haven't changed, alongside those that do	
o	--suppress-outputs	Suppress display of stack outputs (in case they contain sensitive values)	
=	refresh	--color
v	always	
v	never	
v	raw	
v	auto	
=	refresh	-C
t	folders
=	refresh	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	refresh	--config-file
t	filepaths,folders
=	refresh	-p
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
=	refresh	-s
d
=	refresh	--suppress-permalink
v	false	
v	true	
@	schema
s	check	Check a Pulumi package schema for errors
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	schema	--color
v	always	
v	never	
v	raw	
v	auto	
=	schema	-C
t	folders
=	schema	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	schema check
@	stack
s	change-secrets-provider	Change the secrets provider for the current stack
s	export	Export a stack’s deployment to standard out
s	graph	Export a stack’s dependency graph to a file
s	history	[PREVIEW] Display history for a stack
s	import	Import a deployment from standard in into an existing stack
s	init	Create an empty stack with the given name, ready for updates
s	ls	List stacks
s	output	Show a stack’s output properties
s	rename	Rename an existing stack
s	rm	Remove a stack and its configuration
s	select	Switch the current workspace to the given stack
s	tag	Manage stack tags
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	--show-name	Display only the stack name	
o	--show-secrets	Display stack outputs which are marked as secret in plaintext	
o	-i|--show-ids	Display each resource's provider-assigned unique ID	
o	-u|--show-urns	Display each resource's Pulumi-assigned globally unique URN	
=	stack	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack	-C
t	folders
=	stack	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	stack	-s
d
@	stack change-secrets-provider
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
a	1	0
=	stack change-secrets-provider	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack change-secrets-provider	-C
t	folders
=	stack change-secrets-provider	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack export
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--file	A filename to write stack output to	v
o	--show-secrets	Emit secrets in plaintext in exported stack. Defaults to false	v
o	--version	Previous stack version to export. (If unset, will export the latest)	
=	stack export	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack export	-C
t	folders
=	stack export	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	stack export	--show-secrets
v	false	
v	true	
@	stack graph
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--dependency-edge-color	Sets the color of dependency edges in the graph (default "#246C60")	v
o	--ignore-dependency-edges	Ignores edges introduced by dependency resource relationships	
o	--ignore-parent-edges	Ignores edges introduced by parent/child resource relationships	
o	--parent-edge-color	Sets the color of parent edges in the graph (default #AA6639")	v
a	1	0
=	stack graph	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack graph	-C
t	folders
=	stack graph	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack history
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	--full-dates	Show full dates, instead of relative dates	
o	--page	Used with 'page-size' to paginate results (default 1)	v
o	--page-size	Used with 'page' to control number of results returned (default 10)	v
o	--show-secrets	Show secret values when listing config instead of displaying blinded values	
=	stack history	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack history	-C
t	folders
=	stack history	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack import
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-f|--force	Force the import to occur, even if apparent errors are discovered beforehand (not recommended)	
o	--file	A filename to read stack input from	v
=	stack import	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack import	-C
t	folders
=	stack import	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	stack import	--file
t	filepaths
@	stack init
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--secrets-provider	The type of the provider that should be used to encrypt and decrypt secrets (possible choices…	v
o	--copy-config-from	The name of the stack to copy existing config from	v
a	1	0
=	stack init	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack init	-C
t	folders
=	stack init	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	stack init	--secrets-provider
v	default	
v	passphrase	
v	awskms	
v	azurekeyvault	
v	gcpkms	
v	hashivault	
=	stack init	--copy-config-from
d
@	stack ls
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	-a|--all	List all stacks instead of just stacks for the current project	
o	-o|--organization	Filter returned stacks to those in a specific organization	v
o	-p|--project	Filter returned stacks to those with a specific project name	v
o	-t|--tag	Filter returned stacks to those in a specific tag (tag-name or tag-name=tag-value)	v
=	stack ls	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack ls	-C
t	folders
=	stack ls	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack output
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-j|--json	Emit output as JSON	
o	--show-secrets	Display outputs which are marked as secret in plaintext	
a	1	0
=	stack output	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack output	-C
t	folders
=	stack output	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack rename
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
a	1	0
=	stack rename	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack rename	-C
t	folders
=	stack rename	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack rm
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	-f|--force	Forces deletion of the stack, leaving behind any resources managed by the stack	
o	--preserve-config	Do not delete the corresponding Pulumi.<stack-name>.yaml configuration file for the stack	
a	1	0
=	stack rm	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack rm	-C
t	folders
=	stack rm	-v
v	1	
v	2	
v	3	
v	4	
v	5	
#	stack rm	1
d
@	stack select
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--secrets-provider	Use with --create flag, The type of the provider that should be used to encrypt and decrypt…	v
a	1	0
=	stack select	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack select	-C
t	folders
=	stack select	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	stack select	--secrets-provider
v	default	
v	passphrase	
v	awskms	
v	azurekeyvault	
v	gcpkms	
v	hashivault	
#	stack select	1
d
@	stack tag
s	get	Get a single stack tag value
s	ls	List all stack tags
s	rm	Remove a stack tag
s	set	Set a stack tag
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	stack tag	--color
v	always	
v	never	
v	raw	
v	auto	
=	stack tag	-C
t	folders
=	stack tag	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack tag get
s	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")
s	-C|--cwd	Run pulumi as if it had been started in another directory
s	--disable-integrity-checking	Disable integrity checking of checkpoint files
s	-e|--emoji	Enable emojis in the output
s	--logflow	Flow log settings to child processes (like plugins)
s	--logtostderr	Log to stderr instead of to files
s	--non-interactive	Disable interactive mode for all commands
s	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…
s	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
s	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose
a	1	0
@	stack tag get --color
a	1	0
#	stack tag get --color	1
v	always	
v	never	
v	raw	
v	auto	
@	stack tag get -C
a	1	0
#	stack tag get -C	1
t	folders
@	stack tag get --disable-integrity-checking
@	stack tag get -e
@	stack tag get --logflow
@	stack tag get --logtostderr
@	stack tag get --non-interactive
@	stack tag get --profiling
@	stack tag get --tracing
a	1	0
@	stack tag get -v
a	1	0
#	stack tag get -v	1
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack tag ls
s	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")
s	-C|--cwd	Run pulumi as if it had been started in another directory
s	--disable-integrity-checking	Disable integrity checking of checkpoint files
s	-e|--emoji	Enable emojis in the output
s	--logflow	Flow log settings to child processes (like plugins)
s	--logtostderr	Log to stderr instead of to files
s	--non-interactive	Disable interactive mode for all commands
s	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…
s	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
s	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose
s	-j|--json	Emit output as JSON
@	stack tag ls --color
a	1	0
#	stack tag ls --color	1
v	always	
v	never	
v	raw	
v	auto	
@	stack tag ls -C
a	1	0
#	stack tag ls -C	1
t	folders
@	stack tag ls --disable-integrity-checking
@	stack tag ls -e
@	stack tag ls --logflow
@	stack tag ls --logtostderr
@	stack tag ls --non-interactive
@	stack tag ls --profiling
@	stack tag ls --tracing
a	1	0
@	stack tag ls -v
a	1	0
#	stack tag ls -v	1
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack tag ls -j
@	stack tag rm
s	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")
s	-C|--cwd	Run pulumi as if it had been started in another directory
s	--disable-integrity-checking	Disable integrity checking of checkpoint files
s	-e|--emoji	Enable emojis in the output
s	--logflow	Flow log settings to child processes (like plugins)
s	--logtostderr	Log to stderr instead of to files
s	--non-interactive	Disable interactive mode for all commands
s	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…
s	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
s	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose
a	1	0
@	stack tag rm --color
a	1	0
#	stack tag rm --color	1
v	always	
v	never	
v	raw	
v	auto	
@	stack tag rm -C
a	1	0
#	stack tag rm -C	1
t	folders
@	stack tag rm --disable-integrity-checking
@	stack tag rm -e
@	stack tag rm --logflow
@	stack tag rm --logtostderr
@	stack tag rm --non-interactive
@	stack tag rm --profiling
@	stack tag rm --tracing
a	1	0
@	stack tag rm -v
a	1	0
#	stack tag rm -v	1
v	1	
v	2	
v	3	
v	4	
v	5	
@	stack tag set
s	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")
s	-C|--cwd	Run pulumi as if it had been started in another directory
s	--disable-integrity-checking	Disable integrity checking of checkpoint files
s	-e|--emoji	Enable emojis in the output
s	--logflow	Flow log settings to child processes (like plugins)
s	--logtostderr	Log to stderr instead of to files
s	--non-interactive	Disable interactive mode for all commands
s	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…
s	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
s	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose
a	1	0
@	stack tag set --color
a	1	0
#	stack tag set --color	1
v	always	
v	never	
v	raw	
v	auto	
@	stack tag set -C
a	1	0
#	stack tag set -C	1
t	folders
@	stack tag set --disable-integrity-checking
@	stack tag set -e
@	stack tag set --logflow
@	stack tag set --logtostderr
@	stack tag set --non-interactive
@	stack tag set --profiling
@	stack tag set --tracing
a	1	0
@	stack tag set -v
a	1	0
#	stack tag set -v	1
v	1	
v	2	
v	3	
v	4	
v	5	
@	state
s	delete	Deletes a resource from a stack’s state
s	unprotect	Unprotect resources in a stack’s state
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	state	--color
v	always	
v	never	
v	raw	
v	auto	
=	state	-C
t	folders
=	state	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	state delete
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	--force	Force deletion of protected resources	v
a	1	0
=	state delete	--color
v	always	
v	never	
v	raw	
v	auto	
=	state delete	-C
t	folders
=	state delete	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	state delete	-s
d
=	state delete	--force
d
@	state unprotect
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	--all	Unprotect all resources in the checkpoint	v
a	1	0
=	state unprotect	--color
v	always	
v	never	
v	raw	
v	auto	
=	state unprotect	-C
t	folders
=	state unprotect	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	state unprotect	-s
d
=	state unprotect	--all
d
@	up
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	-p|--parallel	Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to…	v
o	-m|--message	Optional message to associate with the destroy operation	v
o	--diff	Display operation as a rich diff showing the overall change	
o	-d|--debug	Print detailed debugging output during resource operations	
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	--suppress-permalink	Suppress display of the state permalink	v
o	-t|--target	Specify a single resource URN to destroy. All resources necessary to destroy this target will also…	v
o	-j|--json	Serialize the update diffs, operations, and overall output as JSON	
o	-r|--refresh	Refresh the state of the stack's resources before this update	v
o	--show-config	Show configuration keys and variables	
o	--show-replacement-steps	Show detailed resource replacement creates and deletes instead of a single step	
o	--show-sames	Show resources that don't need to be updated because they haven't changed, alongside those that do	
o	--suppress-outputs	Suppress display of stack outputs (in case they contain sensitive values)	
o	--target-dependents	Allows destroying of dependent targets discovered but not specified in --target list	
o	-y|--yes	Skip confirmation prompts, and proceed with cancellation anyway	
o	-f|--skip-preview	Do not perform a preview before performing the destroy	
o	--secrets-provider	The type of the provider that should be used to encrypt and decrypt secrets (possible choices…	v
o	-c|--config	Config to use during the update	v
o	--config-path	Config keys contain a path to a property in a map or list to set	
o	--expect-no-changes	Return an error if any changes occur during this update	
o	--policy-pack	Run one or more policy packs as part of this update	v
o	--policy-pack-config	Path to JSON file containing the config for the policy pack of the corresponding "--policy-pack"…	v
o	--replace	Specify resources to replace. Multiple resources can be specified using --replace urn1 --replace…	v
o	--show-reads	Show resources that are being read in, alongside those being managed directly in the stack	
o	--target-replace	Specify a single resource URN to replace. Other resources will not be updated. Shorthand for…	v
a	1	0
=	up	--color
v	always	
v	never	
v	raw	
v	auto	
=	up	-C
t	folders
=	up	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	up	-s
d
=	up	-p
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
=	up	--config-file
t	filepaths,folders
=	up	--suppress-permalink
v	false	
v	true	
=	up	-r
v	false	
v	true	
=	up	--secrets-provider
v	default	
v	passphrase	
v	awskms	
v	azurekeyvault	
v	gcpkms	
v	hashivault	
@	version
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	version	--color
v	always	
v	never	
v	raw	
v	auto	
=	version	-C
t	folders
=	version	-v
v	1	
v	2	
v	3	
v	4	
v	5	
@	watch
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
o	--config-file	Use the configuration values in the specified file rather than detecting the file name	v
o	-d|--debug	Print detailed debugging output during resource operations	
o	-m|--message	Optional message to associate with the destroy operation	v
o	-p|--parallel	Allow P resource operations to run in parallel at once (1 for no parallelism). Defaults to…	v
o	-s|--stack	The name of the stack to operate on. Defaults to the current stack	v
o	--secrets-provider	The type of the provider that should be used to encrypt and decrypt secrets (possible choices…	v
o	-c|--config	Config to use during the update	v
o	--config-path	Config keys contain a path to a property in a map or list to set	
o	--path	Specify one or more relative or absolute paths that need to be watched. A path can point to a…	v
o	--policy-pack	Run one or more policy packs as part of each update	v
o	--policy-pack-config	Path to JSON file containing the config for the policy pack of the corresponding "--policy-pack"…	v
o	-r|--refresh	Refresh the state of the stack's resources before each update	
o	--show-config	Show configuration keys and variables	
o	--show-replacement-steps	Show detailed resource replacement creates and deletes instead of a single step	
o	--show-sames	Show resources that don't need be updated because they haven't changed, alongside those that do	
=	watch	--color
v	always	
v	never	
v	raw	
v	auto	
=	watch	-C
t	folders
=	watch	-v
v	1	
v	2	
v	3	
v	4	
v	5	
=	watch	--config-file
t	filepaths,folders
=	watch	-p
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
=	watch	-s
d
=	watch	--secrets-provider
v	default	
v	passphrase	
v	awskms	
v	azurekeyvault	
v	gcpkms	
v	hashivault	
@	whoami
o	--color	Colorize output. Choices are: always, never, raw, auto (default "auto")	v
o	-C|--cwd	Run pulumi as if it had been started in another directory	v
o	--disable-integrity-checking	Disable integrity checking of checkpoint files	
o	-e|--emoji	Enable emojis in the output	
o	--logflow	Flow log settings to child processes (like plugins)	
o	--logtostderr	Log to stderr instead of to files	
o	--non-interactive	Disable interactive mode for all commands	
o	--profiling	Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}'…	
o	--tracing	Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file	v
o	-v|--verbose	Enable verbose logging (e.g., v=3); anything >3 is very verbose	v
=	whoami	--color
v	always	
v	never	
v	raw	
v	auto	
=	whoami	-C
t	folders
=	whoami	-v
v	1	
v	2	
v	3	
v	4	
v	5	

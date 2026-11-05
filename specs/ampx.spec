@	
s	sandbox	Deploy to your personal cloud sandbox
s	generate	Generate supplemental information or code
s	info	Generate system information for troubleshooting
s	pipeline-deploy	Deploy Amplify project in a CI/CD pipeline
o	--help	Display help information	
o	--version|-v	Display version information	
o	--profile	AWS profile name	v
@	sandbox
s	delete	Delete your personal cloud sandbox
s	secret	Manage backend secrets for your personal cloud sandbox
o	--dir-to-watch	Directory to watch for file changes	v
o	--exclude	Paths or glob patterns to ignore	v
o	--identifier	Name to distinguish between sandbox environments	v
o	--outputs-out-dir	Directory where client config file is written	v
o	--outputs-format	Format of the client config file	v
o	--outputs-version	Version of the configuration	v
o	--profile	AWS profile name	v
o	--stream-function-logs	Stream function execution logs	v
o	--logs-filter	Regex pattern to filter logs	v
o	--logs-out-file	File to append streaming logs	v
=	sandbox	--dir-to-watch
t	folders
=	sandbox	--outputs-out-dir
t	folders
=	sandbox	--outputs-format
v	json	
v	dart	
=	sandbox	--outputs-version
v	0	
v	1	
=	sandbox	--stream-function-logs
v	true	
v	false	
=	sandbox	--logs-out-file
t	filepaths
@	sandbox delete
o	--name	Name to distinguish between sandbox environments	v
o	--profile	AWS profile name	v
o	-y|--yes	Do not ask for confirmation before deleting	
@	sandbox secret
s	set	Set a secret
s	remove	Remove a secret
s	list	List all available secrets
s	get	View details of a secret
@	sandbox secret set
o	--profile	AWS profile name	v
a	1	0
@	sandbox secret remove
o	--profile	AWS profile name	v
a	1	0
@	sandbox secret list
o	--profile	AWS profile name	v
@	sandbox secret get
o	--profile	AWS profile name	v
a	1	0
@	generate
s	outputs	Generate backend outputs file
s	graphql-client-code	Generate GraphQL statements and types
s	forms	Generate React form components
o	--stack	CloudFormation stack name	v
o	--app-id	Amplify App ID	v
o	--branch	Git branch name	v
o	--profile	AWS profile name	v
@	generate outputs
o	--profile	AWS profile name	v
o	--format	Format of the configuration	v
o	--out-dir	Directory where config is written	v
o	--outputs-version	Version of the configuration	v
o	--branch	Git branch name	v
o	--app-id	Amplify App ID	v
=	generate outputs	--format
v	json	
v	dart	
=	generate outputs	--out-dir
t	folders
=	generate outputs	--outputs-version
v	0	
v	1	
@	generate graphql-client-code
o	--out	Directory where config is written	v
o	--format	Format of the GraphQL client code	v
o	--model-target	Modelgen export target	v
o	--statement-target	Graphql codegen statement export target	v
o	--type-target	Graphql-codegen type export target	v
o	--all	Show hidden options	
o	--profile	AWS profile name	v
o	--debug	Print debug logs to the console	
o	--statement-max-depth	Maximum depth of the generated GraphQL statements	v
=	generate graphql-client-code	--out
t	folders
=	generate graphql-client-code	--format
v	modelgen	
v	graphql-codegen	
v	introspection	
=	generate graphql-client-code	--model-target
v	java	
v	swift	
v	javascript	
v	typescript	
v	dart	
=	generate graphql-client-code	--statement-target
v	javascript	
v	graphql	
v	flow	
v	typescript	
v	angular	
=	generate graphql-client-code	--type-target
v	json	
v	swift	
v	typescript	
v	flow	
v	scala	
v	flow-modern	
v	angular	
@	generate forms
o	--out-dir	Directory where generated forms are written	v
o	--models	Model names to generate	v
o	--profile	AWS profile name	v
=	generate forms	--out-dir
t	folders
@	info
@	pipeline-deploy
o	--branch	Name of the git branch being deployed	v
o	--app-id	The app id of the target Amplify app	v
o	--outputs-out-dir	Directory where client config file is written	v
o	--outputs-version	Version of the configuration	v
=	pipeline-deploy	--outputs-out-dir
t	folders
=	pipeline-deploy	--outputs-version
v	0	
v	1	

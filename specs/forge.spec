@	
s	autocomplete	Configures autocomplete for the Forge CLI
s	create	Create an app
s	deploy	Deploy your app to an environment
s	feedback	Let us know what you think about Forge
s	install	Manage app installations
s	lint	Check the source files for common errors
s	login	Log in to your Atlassian account
s	logout	Log out of your Atlassian account
s	logs	View app logs
s	providers	Manage external providers
s	register	Register an app you didn't create so you can run commands for it
s	settings	Manage Forge CLI settings
s	tunnel	Start a tunnel to connect your local code with the app running in the development environment
s	uninstall	Uninstall the app from an Atlassian site
s	variables	Manage app environment variables
s	webtrigger	Get a web trigger URL
s	whoami	Display the account information of the logged in user
s	help	Display help for command
o	-V|--version	Output the version number	
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	autocomplete
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
a	1	0
#	autocomplete	1
v	install	
v	uninstall	
@	create
o	--verbose	Enable verbose mode	
o	-t|--template	Specify the template to use	v
o	-d|--directory	Specify the directory to create (uses the template name by default)	v
o	-h|--help	Display help for command	
a	1	0
@	deploy
o	--verbose	Enable verbose mode	
o	-f|--no-verify	Disable pre-deployment checks	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	--non-interactive	Run the command without input prompts	
o	-h|--help	Display help for command	
@	feedback
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	install
s	list	List app installations
s	help	Display help for command
o	--verbose	Enable verbose mode	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-s|--site	Site URL (example.atlassian.net)	V
o	-p|--product	Product (Jira, Confluence, Compass)	V
o	--upgrade	Upgrade an existing installation	
o	--confirm-scopes	Skip confirmation of scopes for the app before installing or upgrading the app	
o	--non-interactive	Run the command without input prompts	
o	-h|--help	Display help for command	
@	install list
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	install help
a	1	0
@	lint
o	--verbose	Enable verbose mode	
o	--fix	Attempt to automatically fix any issues encountered	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-h|--help	Display help for command	
@	login
o	--verbose	Enable verbose mode	
o	-u|--email	Specify the email to use	v
o	-t|--token	Specify the API token to use	v
o	--non-interactive	Run the command without input prompts	
o	-h|--help	Display help for command	
@	logout
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	logs
o	--verbose	Enable verbose mode	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-i|--invocation	View logs for a given invocation ID	v
o	-n|--limit	Number of invocations to return	v
o	-s|--since	View logs since the specified time. valid formats: YYYY-MM-DD, ISO 8061 timestamp or a relative…	v
o	-g|--grouped	Group logs by invocation ID	
o	-h|--help	Display help for command	
@	providers
s	configure	Configure provider credentials
s	help	Display help for command
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	providers configure
o	--verbose	Enable verbose mode	
o	-s|--oauth-client-secret	Client secret	V
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-h|--help	Display help for command	
a	1	0
@	providers help
a	1	0
@	register
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
a	1	0
@	settings
s	list	List Forge CLI settings
s	set	Update Forge CLI setting (choices: usage-analytics)
s	help	Display help for command
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	settings list
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	settings set
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
a	2	0
@	settings help
a	1	0
@	tunnel
o	--verbose	Enable verbose mode	
o	-d|--debug	Enable debugger mode	
o	-h|--help	Display help for command	
@	uninstall
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
a	1	0
@	variables
s	set	Set an environment variable
s	unset	Remove an environment variable
s	list	List the environment variables
s	help	Display help for command
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	variables set
o	--verbose	Enable verbose mode	
o	--encrypt	Encrypt variable	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-h|--help	Display help for command	
a	2	0
@	variables unset
o	--verbose	Enable verbose mode	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-h|--help	Display help for command	
a	1	0
@	variables list
o	--verbose	Enable verbose mode	
o	-e|--environment	Specify the environment from options: development, staging, production (default: development)	V
o	-h|--help	Display help for command	
@	variables help
a	1	0
@	webtrigger
o	--verbose	Enable verbose mode	
o	-f|--functionKey	Web trigger key from the manifest.yml file	V
o	-h|--help	Display help for command	
a	1	0
@	whoami
o	--verbose	Enable verbose mode	
o	-h|--help	Display help for command	
@	help
a	1	0

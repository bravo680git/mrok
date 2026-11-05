@	
s	register	Sign up for a new Okta account
s	login	Authorizes the Okta CLI tool
s	apps	Manage Okta apps
s	start	Creates an Okta Sample Application
s	help	Displays help information about the specified command
o	--help|-h	Show help for Okta CLI	
o	--version|-V	Print version information	
o	--verbose	Verbose logging	
o	--batch	Batch mode, will not prompt for user input	
@	register
o	--company	Company/organization used when registering a new Okta account	
o	--email	Email used when registering a new Okta account	
o	--first-name	First name used when registering a new Okta account	
o	--last-name	Last name used when registering a new Okta account	
@	login
@	apps
s	config	Show an Okta app's configuration
s	create	Create a new Okta app
s	delete	Deletes an Okta app
@	apps config
o	--app	The App ID	
@	apps create
o	--app-name	Application name to be created, defaults to current directory name	
o	--authorization-server-id	Okta Authorization Server Id	
o	--config-file	Application config file	
o	--redirect-uri	OIDC Redirect URI	
@	apps delete
o	-f|--force	Deactivate and delete applications without confirmation	
a	1	0
@	start
a	1	0
@	help
o	register	Sign up for a new Okta account	
o	login	Authorizes the Okta CLI tool	
o	apps	Manage Okta apps	
o	start	Creates an Okta Sample Application	
o	help	Displays help information about the specified command	
o	generate-completion	Generate bash/zsh completion script for Okta	

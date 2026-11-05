@	
s	flow	Commands for finding and running flows for a project
s	org	Commands for connecting and interacting with Salesforce orgs
s	plan	Commands for getting information about MetaDeploy plans
s	robot	Commands for working with Robot Framework
s	service	Commands for connecting services to the keychain
s	shell	Drop into a Python shell
s	task	Commands for finding and running tasks for a project
s	version	Print the current version of CumulusCI
s	error	Get or share information about an error
s	project	Commands for interacting with project repository configurations
o	--help	Help for cci	
@	flow
s	doc	Exports RST format documentation for all flows
s	info	Displays information for a flow
s	list	List available flows for the current context
s	run	Runs a flow
@	flow doc
o	--project	Include project-specific flows only	
o	--help	Help for flow doc	
@	flow info
o	--help	Help for flow info	
a	1	0
@	flow list
o	--plain	Print the table using plain ascii	
o	--json	Print a json string	
o	--help	Help for flow list	
@	flow run
o	--org	Specify the target org. By default, runs against the current default org	v
o	--delete-org	If set, deletes the scratch org after the flow completes	
o	--debug	Drops into pdb, the Python debugger, on an exception	
o	-o	Pass task specific options for the task as '-o taskname__option value'. You can specify more than…	v
o	--no-prompt	Disables all prompts. Set for non-interactive mode use such as calling from scripts or CI systems	
o	--help	Help for flow run	
a	1	0
@	org
s	browser	Opens a browser window and logs into the org using the stored OAuth credentials
s	connect	Connects a new org's credentials using OAuth Web Flow
s	default	Sets an org as the default org for tasks and flows
s	import	Import an org from Salesforce DX
s	info	Display information for a connected org
s	list	Lists all orgs in scope for the current project
s	prune	Removes all expired scratch orgs from the current project
s	remove	Removes an org from the keychain
s	scratch	Connects a Salesforce DX Scratch Org to the keychain
s	scratch_delete	Deletes a Salesforce DX Scratch Org leaving the config in the keychain for regeneration
s	shell	Drop into a Python shell with a simple_salesforce connection in `sf`, as well as the `org_config`…
@	org browser
o	--org	Alternate way to specify the target org. By default, runs against the current default org	v
o	-p|--path	Navigate to the specified page after logging in	v
o	-r|--url-only	Display the target URL, but don't open a browser	
o	--help	Help for org browser	
a	1	0
=	org browser	-p
t	filepaths
@	org connect
o	--org	Alternate way to specify the target org. One of ORGNAME (see above) or --org is required	v
o	--connected-app	Name of the connected_app service to use	v
o	--sandbox	If set, connects to a Salesforce sandbox org	
o	--login-url	If set, login to this hostname	v
o	--default	If set, sets the connected org as the new default org	
o	--global-org	If set, the connected org is available to all CumulusCI projects	
o	--help	Show this message and exit	
a	1	0
@	org default
o	--org	Alternate way to specify the target org. By default, runs against the current default org	v
o	--unset	Unset the org as the default org leaving no default org selected	
o	--help	Show this message and exit	
a	1	0
@	org import
o	--org	Alternate way to specify the target org. One of ORGNAME (see above) or --org is required	v
o	--help	Show this message and exit	
a	2	0
@	org info
o	--org	Alternate way to specify the target org. By default, runs against the current default org	v
o	--json	Print as JSON. Includes access token	
o	--help	Show this message and exit	
a	1	0
@	org list
o	--plain	Print the table using plain ascii	
o	--json	Output results in JSON format	
o	--help	Show this message and exit	
@	org prune
o	--include-active	Remove all scratch orgs, regardless of expiry	
o	--help	Show this message and exit	
@	org remove
o	--org	Alternate way to specify the target org. One of ORGNAME (see above) or --org is required	v
o	--global-org	Set this option to force remove a global org. Default behavior is to error if you attempt to…	
o	--help	Show this message and exit	
a	1	0
@	org scratch
o	--org	Alternate way to specify the target org. One of ORGNAME (see above) or --org is required	v
o	--default	If set, sets the connected org as the new default org	
o	--devhub	If provided, overrides the devhub used to create the scratch org	v
o	--days	If provided, overrides the scratch config default days value for how many days the scratch org…	v
o	--no-password	If set, don't set a password for the org	
o	--help	Show this message and exit	
a	2	0
@	org scratch_delete
o	--org	Alternate way to specify the target org. One of ORGNAME (see above) or --org is required	v
o	--help	Show this message and exit	
a	1	0
@	org shell
o	--org	Alternate way to specify the target org. By default, runs against the current default org	v
o	--script	Path to a script to run	v
o	--python	Python code to run directly	v
o	--help	Show this message and exit	
a	1	0
@	plan
s	info	Displays information for a MetaDeploy plan
s	list	List available plans for the current context
@	plan info
o	--messages	Show only plan messages	
o	--help	Help for plan info	
a	1	0
@	plan list
o	--json	Return the list of plans in JSON format	
o	--help	Help for plan list	
@	robot
s	install_playwright	Install libraries necessary to use playwright with robot framework
s	uninstall_playwright	Uninstalls the robotframework-browser package and node modules
@	robot install_playwright
o	-n|--dry_run	Dry run	
o	--help	Help for install_playwright	
@	robot uninstall_playwright
o	--help	Help for uninstall_playwright	
@	service
s	connect	Connect an external service to CumulusCI
s	default	Set the default service for a given service type
s	info	Show the details of a connected service
s	list	List services available for configuration and use
s	remove	Remove a service
s	rename	Rename a service
s	update	Allow users to update attribute values of a particular service
@	service connect
s	connected_app	Connect a Connected App service to CumulusCI
s	devhub	Connect a DevHub service to CumulusCI
s	github	Connect a GitHub service to CumulusCI
s	github_enterprise	Connect a GitHub Enterprise service to CumulusCI
s	marketing_cloud	Connect a Marketing Cloud service to CumulusCI
s	metaci	Connect a MetaCI service to CumulusCI
s	metadeploy	Connect a MetaDeploy service to CumulusCI
s	oauth2_client	Connect an OAuth2 Client service to CumulusCI
@	service connect connected_app
o	--login_url	Default Salesforce Login URL to be used with this Connected App	v
o	--callback_url	Callback URL configured on the Connected App	v
o	--client_id	Client ID/Consumer Key from the Connected App	v
o	--client_secret	Client Secret/Consumer Secret from the Connected App	v
o	--default	Set this service as the global default	
o	--help	Help for cci service connect connected_app	
a	1	0
@	service connect devhub
o	--username	Username or alias of the SFDX org to use as a Dev Hub	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service connect github
o	--username	The Github username to use for tasks	v
o	--email	The email address to used by Github tasks when an operation requires an email address	v
o	--token	Personal Access Token for GitHub. Leave blank to log in via browser	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service connect github_enterprise
o	--username	The GitHub Enterprise username to use for tasks	v
o	--email	The email address to used by GitHub tasks when an operation requires an email address	v
o	--server_domain	GitHub Enterprise domain (Example: git.ent.domain.com)	v
o	--token	Personal Access Token	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service connect marketing_cloud
o	--oauth2_client	The name of the oauth2_client service with which to establish a connection to Marketing Cloud	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service connect metaci
o	--app_name	The Heroku app name	v
o	--url	The main url to the MetaCI site	v
o	--token	Your API token to the MetaCI site (get from SITE_URL/api/token)	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service connect metadeploy
o	--url	The main url for your MetaDeploy instance	v
o	--token	Your API token to the MetaDeploy site (get from SITE_URL/admin/authtoken/token)	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service connect oauth2_client
o	--client_id	The client Id	v
o	--client_secret	The client secret	v
o	--auth_uri	The URI for where users are directed to login	v
o	--token_uri	The URI for where we request an access token	v
o	--callback_url	The URL that the auth server will callback to after authentication of the user	v
o	--default	Set this service as the global default	
o	--help	Show this message and exit	
a	1	0
@	service default
o	--project	Sets the service as the default for the current project	
o	--help	Help for cci service default	
a	2	0
@	service info
o	--json	Print a json string	
o	--help	Help for cci service info	
a	2	0
@	service list
o	--plain	Print the table using plain ascii	
o	--json	Print a json string	
o	--help	Help for cci service list	
@	service remove
o	--help	Help for cci service remove	
a	2	0
@	service rename
o	--help	Help for cci service remove	
a	3	0
@	service update
o	-s|--attribute	Provide values to update the service with directly. Using `--attribute foo var` will set the 'foo'…	v
o	--help	Help for cci service remove	
a	2	0
@	shell
o	--script	Path to a script to run	v
o	--python	Python code to run directly	v
o	--help	Show this message and exit	
=	shell	--script
t	filepaths
@	task
s	doc	Exports RST format documentation for all tasks
s	info	Displays information for a task
s	list	List available tasks for the current context
s	run	Runs a task
o	--help	Show this message and exit	
@	task doc
@	task info
a	1	0
@	task list
@	task run
a	1	0
@	version
o	--help	Show this message and exit	
@	error
s	gist	Creates a GitHub gist from the latest logfile
s	info	Outputs the most recent traceback (if one exists in the most recent logfile)
o	--help	Show this message and exit	
@	error gist
@	error info
@	project
s	dependencies	Displays the current dependencies for the project. If the dependencies section has references to…
s	info	Display information about the current project's configuration
s	init	Initialize a new project for use with the cumulusci toolbelt
@	project dependencies
o	--resolution-strategy	The resolution strategy to use. Defaults to production	v
o	--help	Show this message and exit	
@	project info
o	--help	Show this message and exit	
@	project init
o	--help	Show this message and exit	

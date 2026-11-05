@	
s	build	Run a command with secrets injected into the environment
s	config:get-token	Get all tokens
s	config:set	Update your onboardbase config
s	config:set-token	Set up Configuration token manually
s	destroy	Cleanup Onboardbase artifacts including backup and authentication
s	environment:create	Create an environment under a project
s	login	Describe the command here
s	logout	Log out of the CLI
s	project:create	Create a project
s	recommendation:create	Create a recommendation
s	secrets	Log secrets in JSON file
s	secrets:delete	Update secrets on Onboardbase
s	secrets:update	Update secrets on Onboardbase
s	secrets:upload	Upload secrets
s	setup	Setup the Onboardbase CLI for managing secrets
s	share	Share your local onboardbase.yaml secrets with a teammate
s	help	Display help for <%= config.bin %>
@	build
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-e|--environment	Environment to run by default	v
o	-c|--command	Command to run	v
o	-k|--prefix	Prefix	v
o	-s|--passphrase	Passphrase	v
a	1	0
@	config:get-token
o	-S|--scope	Scope	v
@	config:set
o	-s|--scope	Scope	v
o	-t|--token	Auth Token	v
o	-A|--api-host	API Host	v
o	-D|--dashboard-host	Dashboard Host	v
@	config:set-token
o	-S|--scope	Scope	v
a	1	0
@	destroy
@	environment:create
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-e|--environment	Environment Title	v
@	login
o	--overwrite		
@	logout
@	project:create
o	-h|--help	Show CLI help	
o	-t|--title	Name of project	v
o	-d|--description	Project description	v
o	-e|--environment	Environment to run by default	v
@	recommendation:create
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-n|--note	Note	v
a	1	0
@	secrets
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-e|--environment	Environment to run by default	v
o	-J|--json	JSON format	
@	secrets:delete
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-e|--environment	Environment to run by default	v
a	1	0
@	secrets:update
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-e|--environment	Environment to run by default	v
a	1	0
@	secrets:upload
o	-h|--help	Show CLI help	
o	-p|--project	Name of project	v
o	-e|--environment	Environment to run by default	v
a	1	0
@	setup
@	share
o	-h|--help	Show CLI help	
o	-p|--project	Project name	v
@	help
o	--all	See all commands in CLI	
a	1	0

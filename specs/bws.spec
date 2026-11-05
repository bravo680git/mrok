@	
s	config	Specify server settings for the Secrets Manager CLI
s	completions	Generate shell completions
s	project	Access, manipulate and create projects
s	secret	Access, manipulate and create secrets
s	--help|-h	Get help about using the Bitwarden Secrets Manager CLI tool
o	-o|--output	Output format [default: json]	vp
o	-c|--color	Use colors in the output [default: auto]	vp
o	-t|--access-token	Specify access token for the service account [env: BWS_ACCESS_TOKEN]	vp
o	-f|--config-file	Config file to use [default: ~/.bws.config]	vp
o	-p|--profile	Profile to use from the config file [env: BWS_PROFILE=]	vp
o	-u|--server-url	Override the server URL from the config file [env: BWS_SERVER_URL=]	vp
o	-h|--help	Print help	p
o	-V|--version	Print version	p
=		-o
v	json	Produce json output
v	yaml	Produce yaml output
v	env	Produce env output
v	table	Produce table output
v	tsv	Produce tsv output
v	none	Produce no output
=		-c
v	no	Do not color output
v	yes	Colorize output
v	auto	Use default terminal colors
=		-f
t	filepaths
@	config
o	--profile	Save specified value(s) to an alternate profile	v
o	--config-file	Save specified value(s) to an alternative config file	v
o	-h|--help	Display help for login command	
a	1	0
=	config	--config-file
t	filepaths
#	config	1
v	server-base	Base server URL
v	server-api	Server API endpoint URL
v	server-identity	Server Identity endpoint URL
v	state-file-dir	Server file storage location
@	completions
o	-h|--help	Display help for logout command	
a	1	0
#	completions	1
v	bash	Generate shell completions for bash
v	elvish	Generate shell completions for elvish
v	fish	Generate shell completions for fish
v	powershell	Generate shell completions for powershell
v	zsh	Generate shell completions for zsh
@	project
s	create	Create a new project
s	delete	Delete one or more existing projects
s	edit	Change the name of an existing project
s	get	Retrieve a specific project accessible to this service account
s	list	List projects accessible to this service account
o	-h|--help	Access, manipulate and create projects	
@	project create
a	1	0
@	project delete
a	1	0
@	project edit
a	2	0
@	project get
a	1	0
@	project list
@	secret
s	create	Create a new secret
s	delete	Delete an existing secret
s	edit	Edit an existing secret
s	get	Retrieve an existing secret
s	list	List the secrets this service account can access
o	-h|--help	Display help for unlock command	
@	secret create
o	--note	Optional notes about this secret	
a	3	0
@	secret delete
a	1	0
@	secret edit
o	key	Edit the Secret Key	
o	value	Edit the Secret Value	
o	project-id	Edit the ID of project this secret belongs to	
o	note	Edit the optional notes about this secret	
a	1	0
@	secret get
a	1	0
@	secret list
a	1	0
@	--help

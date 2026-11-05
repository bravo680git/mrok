@	
s	run	Run a cicada pipeline
s	init	Initialize a cicada project, you can optionally specify a pipeline to create
s	new	Create a cicada pipeline
s	update	Update cicada
s	completions	List all available completions
s	fig-completion	Create fig completions
s	open	Open a pipeline in your editor
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
o	-V|--version	Print version	
@	run
o	-s|--secret	Name of the secret to use, these come from environment variables	V
o	--dotenv	Load a custom .env file	V
o	--secrets-json	Load secrets from a json file	V
o	--oci-backend	The OCI backend to use	V
o	--no-dotenv	Do not load .env file	
o	--no-cache	Disable caching	
o	-h|--help	Print help (see more with '--help')	
a	1	0
=	run	--dotenv
t	filepaths
=	run	--secrets-json
t	filepaths
=	run	--oci-backend
v	docker	
v	podman	
#	run	1
t	filepaths
@	init
o	-h|--help	Print help	
a	1	0
@	new
o	-h|--help	Print help	
a	1	0
@	update
o	-h|--help	Print help	
@	completions
o	-h|--help	Print help	
a	1	0
#	completions	1
v	bash	
v	elvish	
v	fish	
v	powershell	
v	zsh	
@	fig-completion
o	-h|--help	Print help	
@	open
o	-h|--help	Print help	
a	1	0
#	open	1
t	filepaths
@	help
s	run	Run a cicada pipeline
s	init	Initialize a cicada project, you can optionally specify a pipeline to create
s	new	Create a cicada pipeline
s	update	Update cicada
s	completions	List all available completions
s	fig-completion	Create fig completions
s	open	Open a pipeline in your editor
s	help	Print this message or the help of the given subcommand(s)
@	help run
@	help init
@	help new
@	help update
@	help completions
@	help fig-completion
@	help open
@	help help

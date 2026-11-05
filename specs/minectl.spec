@	
s	completion	Generate the autocompletion script for the specified shell
s	create	Create an Minecraft Server
s	delete	Delete an Minecraft Server
s	list	List all Minecraft Server
s	plugins	Manage your plugins for a specific server
s	rcon	RCON client to your Minecraft server
s	update	Update an Minecraft Server
s	version	Display the clients version information
s	wizard	Calls the minectl wizard to create interactively a minectl 🗺 config
s	help	Help about any command
o	--headless	Set this value to if mincetl is called by a CI system. Enables logging and disables human-readable…	p
o	--log-encoding	Set the log encoding: console|json (default: console)	vp
o	--verbose	Enable verbose logging: debug|info|warn|error|dpanic|panic|fatal	vp
o	--help|-h	Display help	p
=		--log-encoding
v	console	
v	json	
=		--verbose
v	debug	
v	info	
v	warn	
v	error	
v	dpanic	
v	panic	
v	fatal	
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	create
o	--filename|-f	Location of the manifest file	v
o	--wait|-w	Wait for Minecraft Server is started	
=	create	--filename
t	filepaths
@	delete
o	--filename|-f	Location of the manifest file	v
o	--id	Contains the server id	v
o	--yes|-y	Automatically delete the server	
=	delete	--filename
t	filepaths
@	list
o	--provider|-p	The cloud provider - civo|scaleway|do|hetzner|akamai|ovh|equinix|gce|vultr|azure|oci|ionos|aws|vexx…	v
o	--region|-r	The region (gce: zone) for your cloud provider - civo|gce	v
=	list	--provider
v	civo	
v	scaleway	
v	do	
v	hetzner	
v	linode	
v	ovh	
v	equinix	
v	gce	
v	vultr	
v	azure	
v	oci	
v	ionos	
v	aws	
v	vexxhost	
v	multipass	
v	exoscale	
@	plugins
o	--destination|-d	Plugin destination folder	v
o	--filename|-f	Location of the manifest file	v
o	--id	Contains the server id	v
o	--plugin|-p	Location of the plugin	v
o	--ssh-key|-k	Specify a specific path for the SSH key	v
=	plugins	--destination
t	folders
=	plugins	--filename
t	filepaths
=	plugins	--plugin
t	filepaths
@	rcon
o	--filename|-f	Location of the manifest file	v
o	--id	Contains the server id	v
=	rcon	--filename
t	filepaths
@	update
o	--filename|-f	Location of the manifest file	v
o	--id	Contains the server id	v
o	--ssh-key|-k	Specify a specific path for the SSH key	v
=	update	--filename
t	filepaths
@	version
@	wizard
o	--output|-o	Output folder for the configuration file for minectl 🗺 (default: ~/.minectl)	v
=	wizard	--output
t	folders
@	help
s	completion	Generate the autocompletion script for the specified shell
s	create	Create an Minecraft Server
s	delete	Delete an Minecraft Server
s	list	List all Minecraft Server
s	plugins	Manage your plugins for a specific server
s	rcon	RCON client to your Minecraft server
s	update	Update an Minecraft Server
s	version	Display the clients version information
s	wizard	Calls the minectl wizard to create interactively a minectl 🗺 config
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help create
@	help delete
@	help list
@	help plugins
@	help rcon
@	help update
@	help version
@	help wizard

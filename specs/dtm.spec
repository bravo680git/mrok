@	
s	apply	Create or update DevOps tools according to DevStream configuration file
s	completion	Generate the autocompletion script for dtm for the specified shell
s	delete	Delete DevOps tools according to DevStream configuration file
s	destroy	Destroy DevOps tools deployment according to DevStream configuration file & state file
s	develop	Develop is used for develop a new plugin
s	init	Download needed plugins according to the config file
s	list	This command only supports listing plugins now
s	show	Show is used to print plugins' configuration templates or status
s	upgrade	Upgrade dtm to the latest release version
s	verify	Verify DevOps tools according to DevStream config file and state
s	version	Print the version number of DevStream
s	help	Help about any command
o	--debug	Debug level log	p
o	--help|-h	Display help	p
@	apply
o	--config-file|-f	Config file	v
o	--plugin-dir|-d	Plugins directory	v
o	--yes|-y	Apply directly without confirmation	
=	apply	--config-file
t	filepaths
d
=	apply	--plugin-dir
t	folders
@	completion
s	bash	Generate autocompletion script for bash
s	fish	Generate autocompletion script for fish
s	powershell	Generate autocompletion script for powershell
s	zsh	Generate autocompletion script for zsh
@	completion bash
@	completion fish
@	completion powershell
@	completion zsh
@	delete
o	--config-file|-f	Config file	v
o	--force	Force delete by config	
o	--plugin-dir|-d	Plugins directory	v
o	--yes|-y	Delete directly without confirmation	
=	delete	--config-file
t	filepaths
d
=	delete	--plugin-dir
t	folders
@	destroy
o	--config-file|-f	Config file	v
o	--force	Force destroy by config	
o	--plugin-dir|-d	Plugins directory	v
o	--yes|-y	Destroy directly without confirmation	
=	destroy	--config-file
t	filepaths
d
@	develop
s	create-plugin	Create a new plugin
s	validate-plugin	Validate a plugin
@	develop create-plugin
o	--name|-n	Specify name of the plugin to be created	vp
@	develop validate-plugin
o	--all|-a	Validate all plugins	p
o	--name|-n	Specify name of the plugin to be validated	vp
@	init
o	--all|-a	Download all plugins	
o	--arch	Download plugins for specific arch	v
o	--config-file|-f	Config file	v
o	--download-only	Download plugins only	
o	--os	Download plugins for specific os	v
o	--plugin-dir|-d	Plugins directory	v
o	--plugins|-p	The plugins to be downloaded	v
=	init	--config-file
t	filepaths
d
=	init	--plugin-dir
t	folders
@	list
s	plugins	List all plugins
@	list plugins
o	--filter|-r	Filter plugin by regex	vp
@	show
s	config	Show configuration information
s	status	Show status information
@	show config
o	--plugin|-p	Specify name with the plugin	v
o	--template|-t	Print a template config, e.g. quickstart/gitops/	v
=	show config	--plugin
d
@	show status
o	--all|-a	Show all instances of all plugins status	
o	--config-file|-f	Config file	v
o	--id|-i	Specify id with the plugin instance	v
o	--plugin|-p	Specify name with the plugin	v
o	--plugin-dir|-d	Plugins directory	v
@	upgrade
o	--yes|-y	Upgrade directly without confirmation	
@	verify
o	--config-file|-f	Config file	v
o	--plugin-dir|-d	Plugins directory	v
=	verify	--config-file
t	filepaths
d
=	verify	--plugin-dir
t	folders
@	version
@	help
s	apply	Create or update DevOps tools according to DevStream configuration file
s	completion	Generate the autocompletion script for dtm for the specified shell
s	delete	Delete DevOps tools according to DevStream configuration file
s	destroy	Destroy DevOps tools deployment according to DevStream configuration file & state file
s	develop	Develop is used for develop a new plugin
s	init	Download needed plugins according to the config file
s	list	This command only supports listing plugins now
s	show	Show is used to print plugins' configuration templates or status
s	upgrade	Upgrade dtm to the latest release version
s	verify	Verify DevOps tools according to DevStream config file and state
s	version	Print the version number of DevStream
@	help apply
@	help completion
s	bash	Generate autocompletion script for bash
s	fish	Generate autocompletion script for fish
s	powershell	Generate autocompletion script for powershell
s	zsh	Generate autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help delete
@	help destroy
@	help develop
s	create-plugin	Create a new plugin
s	validate-plugin	Validate a plugin
@	help develop create-plugin
@	help develop validate-plugin
@	help init
@	help list
s	plugins	List all plugins
@	help list plugins
@	help show
s	config	Show configuration information
s	status	Show status information
@	help show config
@	help show status
@	help upgrade
@	help verify
@	help version

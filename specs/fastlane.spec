@	
s	init	Helps you with your initial fastlane setup
s	action	Shows more information for a specific command
s	actions	Lists all available fastlane actions
s	add_plugin	Add a new plugin to your fastlane setup
s	docs	Generate a markdown based documentation based on the Fastfile
s	enable_auto_complete	Enable tab auto completion
s	env	Print your fastlane environment, use this when you submit an issue on GitHub
s	help	Display global or [command] help documentation
s	install_plugins	Install all plugins for this project
s	lanes	Lists all available lanes and shows their description
s	list	Lists all available lanes without description
s	new_action	Create a new custom action for fastlane
s	new_plugin	Create a new plugin that can be used with fastlane
s	run	Run a fastlane one-off action without a full lane
s	search_plugins	Search for plugins, search query is optional
s	socket_server	Starts local socket server and enables only a single local connection
s	trigger	Run a specific lane. Pass the lane name and optionally the platform first
s	update_fastlane	Update fastlane to the latest release
s	update_plugins	Update all plugin dependencies
o	--platform	Only show actions available on the given platform	vp
o	-h|--help	Show help for fastlane	p
o	-v|--version	Show version information for fastlane	
o	--verbose	Show version information for fastlane	p
o	--capture_output	Captures the output of the current run, and generates a markdown issue template	
o	--troubleshoot	Enables extended verbose mode. Use with caution, as this even includes ALL sensitive data. Cannot…	
o	--env	Add environment(s) to use with `dotenv`	
=		--platform
v	ios	
v	android	
v	mac	
@	init
s	swift	Fastlane configuration written in Swift (Beta). Swift setup is still in beta
o	-u|--user	Only iOS projects Your Apple ID	v
@	init swift
@	action
a	1	0
@	actions
@	add_plugin
a	1	0
@	docs
o	-f|--force	Overwrite the existing README.md in the ./fastlane folder	
@	enable_auto_complete
o	-c|--custom	Add custom command(s) for which tab auto complete should be enabled too	v
@	env
@	help
@	install_plugins
@	lanes
@	list
o	-j|--json	Output the lanes in JSON instead of text	
@	new_action
o	--name	Name of your new action	v
@	new_plugin
a	1	0
@	run
a	1	0
@	search_plugins
a	1	0
@	socket_server
o	-s|--stay_alive	Keeps socket server up even after error or disconnects, requires CTRL-C to kill	
o	-c|--connection_timeout	Sets connection established timeout	v
o	-p|--port	Sets the port on localhost for the socket connection	v
@	trigger
o	--disable_runner_upgrades	Prevents fastlane from attempting to update FastlaneRunner swift project	
o	--swift_server_port	Prevents fastlane from attempting to update FastlaneRunner swift project	v
a	1	0
@	update_fastlane
@	update_plugins

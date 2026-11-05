@	
s	init	Initializes a configuration file in the current directory
s	fmt	Formats the source files and writes the result to the file system
s	check	Checks for any files that haven't been formatted
s	config	Functionality related to the configuration file
s	output-file-paths	Prints the resolved file paths for the plugins based on the args and configuration
s	output-resolved-config	Prints the resolved configuration for the plugins based on the args and configuration
s	output-format-times	Prints the amount of time it takes to format each file. Use this for debugging
s	clear-cache	Deletes the plugin cache directory
s	upgrade	Upgrades the dprint executable
s	license	Outputs the software license
s	help	Prints the help of the given subcommand(s)
o	-c|--config	Path or url to JSON configuration file. Defaults to dprint.json or .dprint.json in current or…	vp
o	-h|--help	Prints help information	p
o	--plugins	List of urls or file paths of plugins to use. This overrides what is specified in the config file	vp
o	--verbose	Prints additional diagnostic information	p
=		--plugins
t	filepaths
@	init
@	fmt
o	--diff	Outputs a check-like diff of every formatted file	
o	--stdin	Format stdin and output the result to stdout. Provide an absolute file path to apply the inclusion…	v
o	--incremental	Only format files when they change. This may alternatively be specified in the configuration file	V
o	--excludes	List of file patterns or directories in quotes to exclude when formatting. This overrides what is…	v
o	--allow-node-modules	Allows traversing node module directories (unstable - This flag will be renamed to be non-node…	
a	1	1
=	fmt	--stdin
t	filepaths
=	fmt	--incremental
v	true	
v	false	
=	fmt	--excludes
t	filepaths,folders
@	check
o	--incremental	Only format files when they change. This may alternatively be specified in the configuration file	V
o	--excludes	List of file patterns or directories in quotes to exclude when formatting. This overrides what is…	v
o	--allow-node-modules	Allows traversing node module directories (unstable - This flag will be renamed to be non-node…	
a	1	1
=	check	--incremental
v	true	
v	false	
=	check	--excludes
t	filepaths,folders
@	config
s	add	Adds a plugin to the configuration file
s	init	Initializes a configuration file in the current directory
s	update	Updates the plugins in the configuration file
s	help	Prints the help of the given subcommand(s)
@	config add
a	1	0
@	config init
@	config update
o	-y|--yes	Upgrade process plugins without prompting to confirm checksums	
@	config help
a	1	1
@	output-file-paths
o	--excludes	List of file patterns or directories in quotes to exclude when formatting. This overrides what is…	v
o	--allow-node-modules	Allows traversing node module directories (unstable - This flag will be renamed to be non-node…	
a	1	1
=	output-file-paths	--excludes
t	filepaths,folders
@	output-resolved-config
@	output-format-times
o	--incremental	Only format files when they change. This may alternatively be specified in the configuration file	V
o	--excludes	List of file patterns or directories in quotes to exclude when formatting. This overrides what is…	v
o	--allow-node-modules	Allows traversing node module directories (unstable - This flag will be renamed to be non-node…	
a	1	1
=	output-format-times	--incremental
v	true	
v	false	
=	output-format-times	--excludes
t	filepaths,folders
@	clear-cache
@	upgrade
@	license
@	help
a	1	1

@	
s	alias	Create an alias
s	aliases	List available aliases
s	delete	Delete instances
s	exec	Run a command on an instance
s	find	Display available images to create instances from
s	get	Get a configuration setting
s	help	Display help about a command
s	info	Display information about instances
s	launch	Create and start an Ubuntu instance
s	list	List all available instances
s	mount	Mount a local directory in the instance
s	networks	List all available networks interfaces
s	purge	Purge all deleted instances permanently
s	recover	Recover deleted instances
s	restart	Restart instances
s	set	Set a configuration setting
s	shell	Open a shell on a running instance
s	start	Start instances
s	stop	Stop running instances
s	suspend	Suspend running instances
s	transfer	Transfer files between the host and instances
s	umount	Unmount a directory from an instance
s	unalias	Remove an alias
s	version	Show version details
o	-h|--help	Displays help on commandline options	p
o	--help-all	Displays help including Qt specific options	p
o	-v|--verbose	Increase logging verbosity. Repeat the 'v' in the short option for more detail. Maximum verbosity…	p
@	alias
a	3	0
@	aliases
o	--format	Output list in the requested format. Valid formats are: table (default), json, csv and yaml	v
=	aliases	--format
v	table	
v	json	
v	csv	
v	yaml	
@	delete
o	--all	Delete all instances	
o	-p|--purge	Purge instances immediately	
a	1	1
#	delete	1
d
@	exec
a	2	0
#	exec	1
d
@	find
o	--format	Output list in the requested format. Valid formats are: table (default), json, csv and yaml	v
o	--show-unsupported	Show unsupported cloud images as well	
a	1	0
=	find	--format
v	table	
v	json	
v	csv	
v	yaml	
@	get
o	--raw	Output in raw format. For now, this affects only the representation of empty values (i.e. ""…	
a	1	0
#	get	1
v	client.gui.autostart	
v	client.gui.hotkey	
v	client.primary-name	
v	local.bridged-network	
v	local.driver	
v	local.privileged-mounts	
@	help
a	1	0
@	info
o	--format	Output list in the requested format. Valid formats are: table (default), json, csv and yaml	v
o	--all	Display info for all instances	
a	1	1
=	info	--format
v	table	
v	json	
v	csv	
v	yaml	
#	info	1
d
@	launch
o	--timeout	Maximum time, in seconds, to wait for the command to complete. Note that some background…	v
o	-c|--cpus	Number of CPUs to allocate. Minimum: 1, default: 1	v
o	-d|--disk	Disk space to allocate. Positive integers, in bytes, or with K, M, G suffix Minimum: 512M…	v
o	-m|--mem	Amount of memory to allocate. Positive integers, in bytes, or with K, M, G suffix Minimum: 128M…	v
o	-n|--name	Name for the instance. If it is 'primary' (the configured primary instance name), the user's home…	v
o	--cloud-init	Path to a user-data cloud-init configuration, or '-' forstdin	v
o	--network	Add a network interface to the instance, where <spec> is in the "key=value,key=value" format	v
o	--bridged	Adds one `--network bridged` network	
a	1	0
#	launch	1
d
@	list
o	--format	Output list in the requested format. Valid formats are: table (default), json, csv and yaml	v
=	list	--format
v	table	
v	json	
v	csv	
v	yaml	
@	mount
o	-g|--gid-map	A mapping of group IDs for use in the mount. File and folder ownership will be mapped from <host>…	v
o	-u|--uid-map	A mapping of user IDs for use in the mount. File and folder ownership will be mapped from <host>…	v
a	2	1
#	mount	1
t	folders
@	networks
o	--format	Output list in the requested format. Valid formats are: table (default), json, csv and yaml	v
=	networks	--format
v	table	
v	json	
v	csv	
v	yaml	
@	purge
@	recover
o	--all	Recover all deleted instances	
a	1	1
#	recover	1
d
@	restart
o	--timeout	Maximum time, in seconds, to wait for the command to complete. Note that some background…	v
o	--all	Restart all instances	
a	1	1
#	restart	1
d
@	set
a	1	0
#	set	1
v	client.gui.autostart=	
v	client.gui.hotkey=	
v	client.primary-name=	
v	local.bridged-network=	
v	local.driver=	
v	local.privileged-mounts=	
@	shell
o	--timeout	Maximum time, in seconds, to wait for the command to complete. Note that some background…	v
a	1	1
#	shell	1
d
@	start
o	--timeout	Maximum time, in seconds, to wait for the command to complete. Note that some background…	v
o	--all	Start all instances	
a	1	1
#	start	1
d
@	stop
o	--all	Stop all instances	
o	-t|--time	Time from now, in minutes, to delay shutdown of the instance	v
o	-c|--cancel	Cancel a pending delayed shutdown	
a	1	1
#	stop	1
d
@	suspend
o	--all	Suspend all instances	
a	1	1
#	suspend	1
d
@	transfer
a	2	0
#	transfer	1
t	filepaths
#	transfer	2
t	filepaths
@	umount
a	1	1
@	unalias
a	1	0
@	version
o	--format	Output list in the requested format. Valid formats are: table (default), json, csv and yaml	v
=	version	--format
v	table	
v	json	
v	csv	
v	yaml	

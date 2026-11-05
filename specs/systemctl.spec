@	
s	list-units	List units currently in memory
s	list-sockets	List socket units currently in memory ordered by address
s	list-timers	List timer units currently in memory ordered by next elapse
s	is-active	Check whether units are active
s	is-failed	Check whether units are failed
s	status	Show runtime status of one or more units
s	show	Show properties of one or more
s	cat	Show files and drop-ins of specified units
s	help	Show manual for one or more units
s	list-dependencies	Recursively show units which are required or wanted by the units or by which those
s	start	Start (activate) one or more units
s	stop	Stop (deactivate) one or more units
s	reload	Reload one or more units
s	restart	Start or restart one or more units
s	try-restart	Restart one or more units if active
s	reload-or-restart	Reload one or more units if possible, otherwise start or restart
s	try-reload-or-restart	If active, reload one or more units, if supported, otherwise restart
s	isolate	Start one unit and stop all others
s	kill	Send signal to processes of a unit
s	clean	Clean runtime, cache, state, logs or configuration of unit
s	freeze	Freeze execution of unit processes
s	thaw	Resume execution of a frozen unit
s	set-property	Sets one or more properties of a unit
s	bind	Bind-mount a path from the host into a unit's namespace
s	mount-image	Mount an image from the host into a unit's namespace
s	service-log-level	Get/set logging threshold for service
s	service-log-target	Get/set logging target for service
s	reset-failed	Reset failed state for all, one, or more units
s	list-unit-files	List installed unit files
s	enable	Enable one or more unit files
s	disable	Disable one or more unit files
s	reenable	Reenable one or more unit files
s	preset	Enable/disable one or more unit files based on preset configuration
s	preset-all	Enable/disable all unit files based on preset configuration
s	mask	Mask one or more unit files
s	unmask	Unmask one or more unit files
s	link	Link one or more units files into the search path
s	revert	Revert one or more unit files to vendor version
s	add-wants	Add 'Wants' dependency for the target on specified one or more units
s	add-requires	Add 'Requires' dependency for the target on specified one or more units
s	edit	Edit one or more unit files
s	get-default	Get the name of the default target
s	set-default	Set the default target
s	list-jobs	List jobs
s	cancel	Cancel all, one, or more jobs
s	show-environment	Dump environment
s	set-environment	Set one or more environment variables
s	unset-environment	Unset one or more environment variables
s	import-environment	Import all or some environment variables
s	daemon-reload	Reload systemd manager configuration
s	daemon-reexec	Reexecute systemd manager
s	log-level	Get/set logging threshold for manager
s	log-target	Get/set logging target for manager
s	service-watchdogs	Get/set service watchdog state
s	is-system-running	Check whether system is fully running
s	default	Enter system default mode
s	rescue	Enter system rescue mode
s	emergency	Enter system emergency mode
s	halt	Shut down and halt the system
s	poweroff	Shut down and power-off the system
s	reboot	Shut down and reboot the system
s	kexec	Shut down and reboot the system with kexec
s	exit	Request user instance or container exit
s	switch-root	Change to a different root file system
s	suspend	Suspend the system
s	hibernate	Hibernate the system
s	hybrid-sleep	Hibernate and suspend the system
s	suspend-then-hibernate	Suspend the system, wake after a period of time, and hibernate
o	-h|--help	Show this help	
o	--version	Show package version	
o	--system	Connect to system manager	
o	--user	Connect to user service manager	
o	-H|--host	Operate on remote host	v
o	-M|--machine	Operate on a local container	v
o	-t|--type	List units of a particular type	v
o	--state	List units with particular LOAD or SUB or ACTIVE state	v
o	--failed	Shortcut for --state=failed	
o	-p|--property	Show only properties by this name	v
o	-P	Equivalent to --value --property=NAME	
o	-a|--all	Show all properties/all units currently in memory, including dead/empty ones. To list all units…	
o	-l|--full	Don't ellipsize unit names on output	
o	-r|--recursive	Show unit list of host and local containers	
o	--reverse	Show reverse dependencies with 'list-dependencies'	
o	--with-dependencies	Show unit dependencies with 'status', 'cat', 'list-units', and 'list-unit-files'	
o	--job-mode	Specify how to deal with already queued jobs, when queueing a new job	v
o	-T|--show-transaction	When enqueuing a unit job, show full transaction	
o	--show-types	When showing sockets, explicitly show their type	
o	--value	When showing properties, only print the value	
o	--check-inhibitors	Specify if checking inhibitors before shutting down sleeping or hibernating	v
o	-i	Shortcut for --check-inhibitors=no	
o	--kill-who	Whom to send signal to	v
o	-s|--signal	Which signal to send	v
o	--what	Which types of resources to remove	v
o	--now	Start or stop unit after enabling or disabling it	
o	--dry-run	Only print what would be done	
o	-q|--quiet	Supress output	
o	--wait	For (re)start, wait until service stopped again. For is-system-running, wait until startup is…	
o	--no-block	Do not wait until operation finished	
o	--no-wall	Don't send wall message before halt/power-off/reboot	
o	--no-reload	Don't reload daemon after en-/dis-abling unit files	
o	--legend	Enable/disable the legend (column headers and hints)	v
o	--no-pager	Do not pipe output into a pager	
o	--no-ask-password	Do not ask for system passwords	
o	--global	Edit/enable/disable/mask default user unit files globally	
o	--runtime	Edit/enable/disable/mask unit files temporarily until next reboot	
o	-f|--force	When enabling unit files, override existing symlinks. When shutting down, execute action immediately	
o	--preset-mode	Apply only enable, only disable, or all presets	v
o	--root	Edit/enable/disable/mask unit files in the specified root directory	v
o	-n|--lines	Number of journal entries to show	v
o	-o|--output	Change journal output mode	v
o	--firmware-setup	Tell the firmware to show the setup menu on next boot	
o	--boot-loader-menu	Boot into boot loader menu on next boot	v
o	--boot-loader-entry	Boot into a specific boot loader entry on next boot	v
o	--plain	Print unit dependencies as a list instead of a tree	
o	--timestamp	Change format of printed timestamps	v
o	--read-only	Create read-only bind mount	
o	--mkdir	Create directory before mounting, if missing	
o	--marked	Restart/reload previously marked units	
=		--legend
v	true	
v	false	
=		-o
v	short	
v	short-precise	
v	short-iso	
v	short-iso-precise	
v	short-full	
v	short-monotonic	
v	short-unix	
v	verbose	
v	export	
v	json	
v	json-pretty	
v	json-sse	
v	cat	
=		--timestamp
v	pretty	
v	unix	
v	us	
v	utc	
v	us+utc	
@	list-units
a	1	1
#	list-units	1
d
@	list-sockets
a	1	1
@	list-timers
a	1	1
@	is-active
a	1	1
#	is-active	1
d
@	is-failed
a	1	1
#	is-failed	1
d
@	status
a	1	1
#	status	1
d
@	show
a	1	1
#	show	1
d
@	cat
a	1	1
#	cat	1
d
@	help
a	1	1
#	help	1
d
@	list-dependencies
a	1	1
#	list-dependencies	1
d
@	start
a	1	1
#	start	1
d
@	stop
a	1	1
#	stop	1
d
@	reload
a	1	1
#	reload	1
d
@	restart
a	1	1
#	restart	1
d
@	try-restart
a	1	1
#	try-restart	1
d
@	reload-or-restart
a	1	1
@	try-reload-or-restart
a	1	1
#	try-reload-or-restart	1
d
@	isolate
a	1	0
#	isolate	1
d
@	kill
a	1	1
#	kill	1
d
@	clean
a	1	1
#	clean	1
d
@	freeze
a	1	1
@	thaw
a	1	1
@	set-property
a	2	0
#	set-property	1
d
@	bind
a	3	0
#	bind	1
d
#	bind	2
t	filepaths
#	bind	3
t	filepaths
@	mount-image
a	4	0
#	mount-image	1
d
#	mount-image	2
t	filepaths
#	mount-image	3
t	filepaths
@	service-log-level
a	2	0
@	service-log-target
a	2	0
@	reset-failed
a	1	1
@	list-unit-files
a	1	1
#	list-unit-files	1
d
@	enable
a	1	1
#	enable	1
d
@	disable
a	1	1
#	disable	1
d
@	reenable
a	1	1
#	reenable	1
d
@	preset
a	1	1
#	preset	1
d
@	preset-all
a	1	1
#	preset-all	1
d
@	mask
a	1	1
#	mask	1
d
@	unmask
a	1	1
#	unmask	1
d
@	link
a	1	1
#	link	1
t	filepaths
@	revert
a	1	1
#	revert	1
d
@	add-wants
a	2	1
@	add-requires
a	2	1
@	edit
a	1	1
#	edit	1
d
@	get-default
@	set-default
a	1	0
@	list-jobs
a	1	1
@	cancel
a	1	1
@	show-environment
@	set-environment
a	1	1
@	unset-environment
a	1	1
@	import-environment
a	1	1
@	daemon-reload
@	daemon-reexec
@	log-level
a	1	0
@	log-target
a	1	0
@	service-watchdogs
a	1	0
#	service-watchdogs	1
v	true	
v	false	
@	is-system-running
@	default
@	rescue
@	emergency
@	halt
@	poweroff
@	reboot
@	kexec
@	exit
a	1	0
@	switch-root
a	2	0
@	suspend
@	hibernate
@	hybrid-sleep
@	suspend-then-hibernate

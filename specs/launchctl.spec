@	
s	bootstrap	Bootstraps a domain or a service into a domain
s	bootout	Tears down a domain or removes a service from a domain
s	enable	Enables an existing service
s	disable	Disables an existing service
s	kickstart	Forces an existing service to start
s	attach	Attach the system's debugger to a service
s	debug	Configures the next invocation of a service for debugging
s	kill	Sends a signal to the service instance
s	blame	Prints the reason a service is running
s	print	Prints a description of a domain or service
s	print-cache	Prints information about the service cache
s	print-disabled	Prints which services are disabled
s	plist	Prints a property list embedded in a binary (targets the Info.plist by default)
s	procinfo	Prints port information about a process
s	hostinfo	Prints port information about the host
s	resolveport	Resolves a port name from a process to an endpoint in launchd
s	limit	Reads or modifies launchd's resource limits
s	runstats	Prints performance statistics for a service
s	examine	Runs the specified analysis tool against launchd in a non-re-entrant manner
s	config	Modifies persistent configuration parameters for launchd domains
s	dumpstate	Dumps launchd state to stdout
s	dumpjpcategory	Dumps the jetsam properties category for all services
s	reboot	Initiates a system reboot of the specified type
s	load	Recommended alternatives: bootstrap | enable. Bootstraps a service or directory of services
s	unload	Recommended alternatives: bootout | disable. Unloads a service or directory of services
s	remove	Unloads the specified service name
s	list	Lists information about services
s	start	Starts the specified service
s	stop	Stops the specified service if it is running
s	setenv	Sets the specified environment variables for all services within the domain
s	unsetenv	Unsets the specified environment variables for all services within the domain
s	getenv	Gets the value of an environment variable from within launchd
s	bsexec	Execute a program in another process' bootstrap context
s	asuser	Execute a program in the bootstrap context of a given user
s	submit	Submit a basic job from the command line
s	managerpid	Prints the PID of the launchd controlling the session
s	manageruid	Prints the UID of the current launchd session
s	managername	Prints the name of the current launchd session
s	error	Prints a description of an error
s	variant	Prints the launchd variant
s	version	Prints the launchd version
s	help	Prints the usage for a given subcommand
a	1	0
@	bootstrap
a	2	1
#	bootstrap	1
t	filepaths
#	bootstrap	2
t	filepaths
@	bootout
a	2	1
#	bootout	1
t	filepaths
#	bootout	2
t	filepaths
@	enable
a	1	0
@	disable
a	1	0
@	kickstart
o	-k	Kill instance before restarting	
o	-p	Print PID	
a	1	0
@	attach
o	-k	Kill instance	
o	-s	Force the service to start	
o	-x	Attach xpcproxy	
a	1	0
@	debug
o	--program	Use program path as executable	v
o	--guard-malloc	Turn on libgmalloc	
o	--malloc-stack-logging	Turn on malloc(3) stack logging	
o	--malloc-nano-allocator	Turn on malloc(3) nano allocator	
o	--debug-libraries	Set the DYLD_IMAGE_SUFFIX	
o	--introspection-libraries	Add introspection libraries to the DYLD_IMAGE_PATH	
o	--NSZombie	Enables NSZombie	
o	--32	Runs service on appropriate 32-bit architecture	
o	--stdin	Sets the stdin path	v
o	--stdout	Sets the stdout path	v
o	--stderr	Sets the stderr path	v
o	--environment	Sets environment variables	v
a	1	1
=	debug	--stdin
t	filepaths
=	debug	--stdout
t	filepaths
=	debug	--stderr
t	filepaths
@	kill
a	2	0
@	blame
a	1	0
@	print
a	1	0
#	print	1
t	filepaths
@	print-cache
@	print-disabled
a	1	0
@	plist
a	2	0
#	plist	2
t	filepaths
@	procinfo
a	1	0
@	hostinfo
@	resolveport
a	2	0
@	limit
o	cpu		v
o	filesize		v
o	data		v
o	stack		v
o	core		v
o	rss		v
o	memlock		v
o	maxproc		v
o	maxfiles		v
@	runstats
a	1	0
@	examine
a	2	1
@	config
a	3	0
#	config	1
v	system	
@	dumpstate
@	dumpjpcategory
@	reboot
o	system		
o	userspace		
o	halt		
o	logout		
o	apps		
@	load
o	-w	Enable if disabled	
o	-F	Force load	
o	-S	Session	v
o	-D	Load files from specified domain	v
a	1	1
#	load	1
t	filepaths
@	unload
o	-w	Enable if disabled	
o	-F	Force load	
o	-S	Session	v
o	-D	Load files from specified domain	v
a	1	1
#	unload	1
t	filepaths
@	remove
a	1	0
#	remove	1
d
@	list
a	1	0
#	list	1
d
@	start
a	1	0
#	start	1
d
@	stop
a	1	0
#	stop	1
d
@	setenv
a	2	0
@	unsetenv
a	1	0
@	getenv
a	1	0
@	bsexec
a	3	1
@	asuser
a	3	1
@	submit
o	-p	Program to execute	v
o	-o	Std out path	v
o	-e	Std err path	v
a	4	1
=	submit	-o
t	filepaths
=	submit	-e
t	filepaths
#	submit	2
d
@	managerpid
@	manageruid
@	managername
@	error
a	2	0
#	error	1
v	posix	
v	mach	
v	bootstrap	
@	variant
@	version
@	help

@	
s	create	Create a project
s	help	Get help for a command
s	telemetry	Turn telemetry collection on or off
s	config	Set, get, delete, edit, and list global cordova options
s	info	Generate project information
s	requirements	Checks and print out all the installation requirements for platforms specified
s	platform|platforms	Manage project platforms
s	plugin|plugins	Manage project plugins
s	prepare	Copy files into platform(s) for building
s	compile	Compile project for platform(s)
s	build	Build project for platform(s) (prepare + compile)
s	clean	Cleanup project from build artifacts
s	run	Run project (including prepare && compile)
s	serve	Run project with a local webserver (including prepare)
o	-d|--verbose	Pipe out more verbose output to your shell. You can also subscribe to log and warn events if you…	
o	-v|--version	Print out the version of your cordova-cli install	
o	--no-update-notifier	Will disable updates check	
o	--nohooks	Suppress executing hooks (taking RegExp hook patterns as parameters)	
o	--no-telemetry	Disable telemetry collection for the current command	
@	create
o	-d|--verbose	Pipe out more verbose output to your shell. You can also subscribe to log and warn events if you…	
o	-v|--version	Print out the version of your cordova-cli install	
o	--no-update-notifier	Will disable updates check	
o	--nohooks	Suppress executing hooks (taking RegExp hook patterns as parameters)	
o	--no-telemetry	Disable telemetry collection for the current command	
o	--template	Use a custom template located locally, in NPM, or GitHub	
a	3	0
#	create	1
t	folders
@	help
a	1	0
#	help	1
v	create	
v	help	
v	telemetry	
v	config	
v	info	
v	requirements	
v	platform	
v	plugin	
v	prepare	
v	compile	
v	build	
v	clean	
v	run	
v	serve	
@	telemetry
a	2	0
@	config
s	ls	Lists contents of config file
s	edit	Opens the config file in an editor
s	set	Sets the config key to the value. If value is omitted, then it sets it to "true"
s	get	Echo the config value to stdout
s	delete	Deletes the key from all configuration files
@	config ls
@	config edit
@	config set
a	2	0
@	config get
a	1	0
@	config delete
a	1	0
@	info
@	requirements
a	1	0
#	requirements	1
d
@	platform
s	add	Add specified platforms
s	remove|rm	Remove specified platforms
s	update	Update specified platforms
s	list|ls	List all installed and available platforms
@	platform add
o	--nosave	Do not save	
o	--link	When platform-spec is a local path, link the platform library directly instead of making a copy of…	v
a	1	1
=	platform add	--link
t	folders
#	platform add	1
v	android	
v	ios	
v	windows	
v	browser	
v	electron	
t	filepaths,folders
@	platform remove
o	--nosave	Do not delete specified platforms from	
a	1	1
#	platform remove	1
d
@	platform update
o	--save	Updates the version specified in **config.xml**	
@	platform list
@	plugin
s	add	Add specified plugins
s	remove	Remove plugins with the given IDs/name
s	list	List currently installed plugins
@	plugin add
o	--searchpath	When looking up plugins by ID, look in this directory and each of its subdirectories before…	v
o	--noregistry	Don't search the registry for plugins	
o	--link	When installing from a local path, creates a symbolic link instead of copying files. The extent to…	
o	--nosave	Do NOT save the <plugin-spec> as part of the plugin element into config.xml or package.json	
o	--force	Forces copying source files from the plugin even if the same file already exists in the target…	
a	1	1
=	plugin add	--searchpath
t	folders
#	plugin add	1
t	folders
@	plugin remove
o	--nosave	Do NOT remove the specified plugin from config.xml or package.json	
a	1	1
#	plugin remove	1
d
@	plugin list
@	prepare
a	1	0
#	prepare	1
d
@	compile
o	-d|--verbose	Pipe out more verbose output to your shell. You can also subscribe to log and warn events if you…	
o	-v|--version	Print out the version of your cordova-cli install	
o	--no-update-notifier	Will disable updates check	
o	--nohooks	Suppress executing hooks (taking RegExp hook patterns as parameters)	
o	--no-telemetry	Disable telemetry collection for the current command	
o	--debug	Perform a debug build. This typically translates to debug mode for the underlying platform being…	
o	--release	Perform a release build. This typically translates to release mode for the underlying platform…	
o	--device	Build it for a device	
o	--emulator	Build it for an emulator. In particular, the platform architecture might be different for a device…	
o	--buildConfig	Use the specified build configuration file. build.json file is used to specify parameters to…	v
a	1	0
=	compile	--buildConfig
t	filepaths,folders
#	compile	1
d
@	build
o	-d|--verbose	Pipe out more verbose output to your shell. You can also subscribe to log and warn events if you…	
o	-v|--version	Print out the version of your cordova-cli install	
o	--no-update-notifier	Will disable updates check	
o	--nohooks	Suppress executing hooks (taking RegExp hook patterns as parameters)	
o	--no-telemetry	Disable telemetry collection for the current command	
o	--debug	Perform a debug build. This typically translates to debug mode for the underlying platform being…	
o	--release	Perform a release build. This typically translates to release mode for the underlying platform…	
o	--device	Build it for a device	
o	--emulator	Build it for an emulator. In particular, the platform architecture might be different for a device…	
o	--buildConfig	Use the specified build configuration file. build.json file is used to specify parameters to…	v
a	1	0
=	build	--buildConfig
t	filepaths,folders
#	build	1
d
@	clean
a	1	0
#	clean	1
d
@	run
o	--list	Lists available targets. Displays both device and emulator deployment targets unless specified	
o	--debug	Deploy a debug build. This is the default behavior unless --release is specified	
o	--release	Deploy a release build	
o	--noprepare	Skip preparing (available in Cordova v6.2 or later)	
o	--nobuild	Skip building	
o	--device	Deploy to a device	
o	--emulator	Deploy to an emulator	
o	--target	Deploy to a specific target emulator/device. Use --list to display target options	v
o	--buildConfig	Use the specified build configuration file. build.json file is used to specify parameters to…	v
a	1	0
=	run	--buildConfig
t	filepaths
#	run	1
d
@	serve
a	1	0

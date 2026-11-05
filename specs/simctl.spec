@	
s	addmedia	Add photos, live photos, videos, or contacts to the library of a device
s	boot	Boot a device or device pair
s	clone	Clone an existing device
s	create	Create a new device
s	delete	Delete specified devices, unavailable devices, or all devices
s	diagnose	Collect diagnostic information and logs
s	erase	Erase a device's contents and settings
s	get_app_container	Print the path of the installed app's container
s	getenv	Print an environment variable from a running device
s	help	Prints the usage for a given subcommand
s	icloud_sync	Trigger iCloud sync on a device
s	install	Install an app on a device
s	install_app_data	Install an xcappdata package to a device, replacing the current contents of the container
s	io	Set up a device IO operation
s	keychain	Manipulate a device's keychain
s	launch	Launch an application by identifier on a device
s	list	List available devices, device types, runtimes, or device pairs
s	location	Control a device's simulated location
s	logverbose	Enable or disable verbose logging for a device.
s	openurl	Open a URL in a device
s	pair	Create a new watch and phone pair
s	pair_activate	Set a given pair as active
s	pbcopy	Copy standard input onto the device pasteboard
s	pbpaste	Print the contents of the device's pasteboard to standard output
s	pbsync	Sync the pasteboard content from one pasteboard to another
s	privacy	Grant, revoke, or reset privacy and permissions
s	push	Send a simulated push notification
s	rename	Rename a device
s	runtime	Perform operations on runtimes
s	shutdown	Shutdown a device
s	spawn	Spawn a process by executing a given executable on a device
s	status_bar	Set or clear status bar overrides
s	terminate	Terminate an application by identifier on a device
s	ui	Get or Set UI options
s	uninstall	Uninstall an app from a device
s	unpair	Unpair a watch and phone pair
s	upgrade	Upgrade a device to a newer runtime
@	addmedia
a	2	1
@	boot
o	--arch	Specify the architecture to use when booting the simulator (eg: 'arm64' or 'x86_64')	=
o	--disabledJob	Disables the given launchd job. Multiple jobs can be disabled by passing multiple flags	=
o	--enabledJob	Enables the given launchd job when it would normally be disabled. Multiple jobs can be enabled by…	=
a	1	0
@	clone
a	3	1
@	create
a	3	1
@	delete
a	3	0
@	diagnose
o	-b	Do NOT show the resulting archive in a Finder window upon completion	
o	-X	Run all diagnostics with no timeout. It ignores the --timeout value if it is specified	
o	--timeout	Specify a duration (in seconds) to wait for the log collection before timeout	=
o	--output	Specify the output directory. If not provided the temporary directory is used	=
o	--no-archive	Do not create an archive, leave the collected files uncompressed	
o	--all-logs	Include all device logs, even for non-booted devices	
o	--data-containers	Include booted device(s) data directory. Warning: May include private information, app data…	
o	--udid	Collect diagnostics only from the specified device. This option may be specified more than once to…	=
@	erase
a	2	0
@	get_app_container
a	3	0
#	get_app_container	3
v	app	The .app bundle
v	data	The application's data container
v	groups	The App Group containers
v	<group identifier>	A specific App Group container
@	getenv
a	2	0
@	help
@	icloud_sync
a	1	0
@	install
a	2	0
@	install_app_data
a	2	0
@	io
s	enumerate	Lists all available IO ports and descriptor states
s	poll	Polls all available IO ports for events
s	recordVideo	Records the display to a QuickTime movie at the specified file or url
s	screenshot	Saves a screenshot as a PNG to the specified file or url(use '-' for stdout)
a	1	0
@	io enumerate
o	--poll	Poll after enumeration	
@	io poll
@	io recordVideo
o	--codec	Specifies the codec type: 'h264' or 'hevc'. Default is 'hevc'	=
o	--display	iOS: supports 'internal' or 'external'. Default is 'internal'. tvOS: supports only 'external'…	=
o	--mask	For non-rectangular displays, handle the mask by policy: ignored: The mask is ignored and the…	=
o	--force	Force the output file to be written to, even if the file already exists	
a	1	0
@	io screenshot
o	--type	Can be 'png', 'tiff', 'bmp', 'gif', 'jpeg'. Default is png	=
o	--display	iOS: supports 'internal' or 'external'. Default is 'internal'. tvOS: supports only 'external'…	=
o	--mask	For non-rectangular displays, handle the mask by policy: ignored: The mask is ignored and the…	=
a	1	0
@	keychain
s	add-root-cert	Add a certificate to the trusted root store
s	add-cert	Add a certificate to the keychain
s	reset	Reset the keychain
@	keychain add-root-cert
a	1	0
@	keychain add-cert
a	1	0
@	keychain reset
@	launch
o	-w|--wait-for-debugger		
o	--console	Block and print the application's stdout and stderr to the current terminal. Signals received by…	
o	--console-pty	Block and print the application's stdout and stderr to the current terminal via a PTY. Signals…	
o	--stdout	Redirect the application's standard output to a file	v=
o	--stderr	Redirect the application's standard error to a file	v=
o	--terminate-running-process	Terminate any running copy of the application. Note: Log output is often directed to stderr, not…	
a	3	1
@	list
o	-j|--json	Print as JSON	
o	-e|--no-escape-slashes	Encode slashes without escapes in JSON output	
o	-v	More verbose output	
a	2	0
#	list	1
v	devices	
v	deviceTypes	
v	runtimes	
v	pairs	
#	list	2
v	available	
@	location
s	list	List available simulation scenarios
s	clear	Stop any running scenario and clear any simulated location
s	set	Set the location to a specific latitude and longitude
s	run	Run a simulated location scenario (use the list action to get a list of scenarios)
s	start	Set the location to a series of waypoints specified as 'lat,lon' pairs, interpolating between them…
a	2	0
@	location list
@	location clear
@	location set
a	1	0
@	location run
a	1	0
@	location start
o	speed		=
o	distance		=
o	interval		=
a	1	1
@	logverbose
a	2	0
#	logverbose	2
v	enable	
v	disable	
@	openurl
a	2	0
@	pair
a	2	0
@	pair_activate
a	1	0
@	pbcopy
o	-v		
a	1	0
@	pbpaste
o	-v		
a	1	0
@	pbsync
o	-p	Causes simctl to use promise data for secondary types. simctl will continue to run to provide that…	
o	-v		
a	2	0
@	privacy
a	4	0
#	privacy	2
v	grant	
v	revoke	
v	reset	
#	privacy	3
v	all	
v	calendar	
v	contacts-limited	
v	contacts	
v	location	
v	location-always	
v	photos-add	
v	photos	
v	media-library	
v	microphone	
v	motion	
v	reminders	
v	siri	
@	push
a	3	0
#	push	3
v	-	
@	rename
a	2	0
@	runtime
s	add	Add a runtime disk image to the secure storage area. The image will be staged, verified, and…
s	delete	Delete a simulator runtime from the secure storage area. If runtime is a disk image any booted…
s	verify	Re-verify the signature of a given runtime
s	list	
s	match list	List the SDK build to runtime build mapping rules for the selected Xcode. Preferred means the…
s	match set	Override the SDK to runtime build mapping. This controls which build of a given runtime Xcode will…
@	runtime add
o	-m|--move	Remove the original file if the image is added successfully. If the image cannot be staged or the…	
o	-a|--async	Print the UUID of the new image then exit, do not wait on the results of the add operation	
a	1	0
@	runtime delete
o	-d|--notUsedSinceDays	Delete images not used within the past <days> days	
o	-n|--dry-run	Print what images would be deleted without actually deleting anything	
a	1	0
@	runtime verify
a	1	0
@	runtime list
o	-v	Print more verbose output	
o	-j|--json	Print as JSON	
@	runtime match list
o	-v	Verbose mode. Includes the full preferred build map, user override map, and known SDK names	
o	-j|--json	Print as JSON	
@	runtime match set
o	--default	Clear the override for the given SDK and revert to default behavior	
o	--sdkBuild	Explicitly specify the SDK build, eg for an Xcode other than the selected Xcode	
a	2	0
@	shutdown
a	2	0
#	shutdown	2
v	all	
@	spawn
o	-w|--wait-for-debugger		
o	-s|--standalone		
o	-a|--arch		
a	3	1
@	status_bar
s	list	List existing overrides
s	clear	Clear all existing status bar overrides
s	override	Set status bar override values, according to these flags. You may specify any combination of these…
a	1	0
@	status_bar list
@	status_bar clear
@	status_bar override
o	--time	Set the date or time to a fixed value. If the string is a valid ISO date string it will also set…	
o	--dataNetwork	If specified must be one of 'hide', 'wifi', '3g', '4g', 'lte', 'lte-a', 'lte+', '5g', '5g+'…	
o	--wifiMode	If specified must be one of 'searching', 'failed', or 'active'	
o	--wifiBars	If specified must be 0-3	
o	--cellularMode	If specified must be one of 'notSupported', 'searching', 'failed', or 'active'	
o	--cellularBars	If specified must be 0-4	
o	--operatorName	Set the cellular operator/carrier name. Use '' for the empty string	
o	--batteryState	If specified must be one of 'charging', 'charged', or 'discharging'	
o	--batteryLevel	If specified must be 0-100	
@	terminate
a	2	0
@	ui
s	appearance	When invoked without arguments prints the current user interface appearance style:
s	increase_contrast	When invoked without arguments prints whether the Increase Contrast mode is currently enabled:
s	content_size	When invoked without arguments prints the current preferred content size category, from the…
a	1	0
@	ui appearance
@	ui increase_contrast
@	ui content_size
@	uninstall
a	2	0
@	unpair
a	1	0
@	upgrade
a	2	0

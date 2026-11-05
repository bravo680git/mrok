@	
o	-	Read from stdin (e.g. 'ps aux | grep code | code -')	
o	-d|--diff	Compare two files with each other	v
o	-m|--merge	Perform a three-way merge by providing paths for two modified versions of a file, the common…	v
o	-a|--add	Add folder(s) to the last active window	v
o	-g|--goto	Open a file at the path on the specified line and character position	v
o	-n|--new-window	Force to open a new window	
o	-r|--reuse-window	Force to open a file or folder in an already opened window	
o	-w|--wait	Wait for the files to be closed before returning	
o	--locale	The locale to use (e.g. en-US or zh-TW)	v
o	--user-data-dir	Specifies the directory that user data is kept in. Can be used to open multiple distinct instances…	v
o	--profile	Opens the provided folder or workspace with the given profile and associates the profile with the…	v
o	-h|--help	Print usage	
o	--extensions-dir	Set the root path for extensions	v
o	--list-extensions	List the installed extensions	
o	--show-versions	Show versions of installed extensions, when using --list-extensions	
o	--category	Filters installed extensions by provided category, when using --list-extensions	v
o	--install-extension	Installs or updates an extension. The argument is either an extension id or a path to a VSIX. The…	v
o	--pre-release	Installs the pre-release version of the extension, when using --install-extension	
o	--uninstall-extension	Uninstalls an extension	v
o	--enable-proposed-api	Enables proposed API features for extensions. Can receive one or more extension IDs to enable…	
o	-v|--version	Print version	
o	--verbose	Print verbose output (implies --wait)	
o	--log	Log level to use. Default is 'info' when unspecified	v
o	-s|--status	Print process usage and diagnostics information	
o	--prof-startup	Run CPU profiler during startup	
o	--disable-extensions	Disable all installed extensions	
o	--disable-extension	Disable an extension	v
o	--sync	Turn sync on or off	v
o	--inspect-extensions	Allow debugging and profiling of extensions. Check the developer tools for the connection URI	v
o	--inspect-brk-extensions	Allow debugging and profiling of extensions with the extension host being paused after start…	v
o	--disable-gpu	Disable GPU hardware acceleration	
o	--max-memory	Max memory size for a window (in Mbytes)	v
o	--telemetry	Shows all telemetry events which VS code collects	
a	1	1
=		-d
t	filepaths
=		-m
t	filepaths
=		-a
t	folders
=		-g
t	filepaths
=		--locale
v	en	English (US)
v	zh-CN	Simplified Chinese
v	zh-TW	Traditional Chinese
v	fr	French
v	de	German
v	it	Italian
v	es	Spanish
v	ja	Japanese
v	ko	Korean
v	ru	Russian
v	bg	Bulgarian
v	hu	Hungarian
v	pt-br	Portuguese (Brazil)
v	tr	Turkish
=		--user-data-dir
t	folders
=		--extensions-dir
t	folders
=		--category
v	azure	
v	data science	
v	debuggers	
v	extension packs	
v	education	
v	formatters	
v	keymaps	
v	language packs	
v	linters	
v	machine learning	
v	notebooks	
v	programming languages	
v	scm providers	
v	snippets	
v	testing	
v	themes	
v	visualization	
v	other	
=		--log
v	critical	
v	error	
v	warn	
v	info	
v	debug	
v	trace	
v	off	
=		--sync
v	on	
v	off	
#		1
t	filepaths,folders

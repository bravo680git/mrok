@	
s	check	Contains some verification checks
s	config	Print the site configuration
s	convert	Convert your content to different formats
s	deploy	Deploy your site to a Cloud provider
s	env	Print Hugo version and environment info
s	gen	A collection of several useful generators
s	help	Help about any command
s	import	Import your site from others
s	list	Listing out various types of content
s	mod	Various Hugo Modules helpers
s	new	Create new content for your site
s	server	A high performance webserver
s	version	Print the version number of Hugo
o	-h|--help	help for hugo	
o	-b|--baseURL	Hostname (and path) to the root, e.g. http://spf13.com/	v
o	-D|--buildDrafts	Include content marked as draft (default false)	v
o	-E|--buildExpired	Include expired content (default false)	v
o	-F|--buildFuture	Include content with publishdate in the future (default false)	v
o	--cacheDir	Filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/	v
o	--cleanDestinationDir	Remove files from destination not found in static directories (default false)	v
o	-c|--contentDir	Filesystem path to content directory	v
o	-d|--destination	Filesystem path to write files to	v
o	--disableKinds	Disable different kind of pages (home, RSS etc.)	v
o	--enableGitInfo	Add Git revision, date and author info to the pages (default false)	v
o	--forceSyncStatic	Copy all files when static is changed (default false)	v
o	--gc	Enable to run some cleanup tasks (remove unused cache files) after the build (default false)	v
o	--i18n-warnings	Print missing translations (default false)	v
o	--ignoreCache	Ignores the cache directory (default false)	v
o	-l|--layoutDir	Filesystem path to layout directory	v
o	--minify	Minify any supported output format (HTML, XML etc.) (default false)	v
o	--noChmod	Don't sync permission mode of files (default false)	v
o	--noTimes	Don't sync modification time of files (default false)	v
o	--path-warnings	Print warnings on duplicate target paths etc (default false)	v
o	--poll	Set this to a poll interval, e.g --poll 700ms, to use a poll based approach to watch for file…	v
o	--print-mem	Print memory usage to screen at intervals (default false)	v
o	--templateMetrics	Display metrics about template executions (default false)	v
o	--templateMetricsHints	Calculate some improvement hints when combined with --templateMetrics (default false)	v
o	-t|--theme	Themes to use (located in /themes/THEMENAME/)	v
o	--trace	Write trace to file (not useful in general)	v
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
o	-w|--watch	Watch filesystem for changes and recreate as needed (default true)	v
o	--renderToMemory	Render to memory (only useful for benchmark testing)	
=		--cacheDir
t	folders
=		-c
t	folders
=		-d
t	folders
=		--disableKinds
v	page	
v	home	
v	section	
v	taxonomy	
v	term	
v	RSS	
v	sitemap	
v	robotsTXT	
v	404	
=		-l
t	folders
=		--trace
t	filepaths
=		--config
t	filepaths
=		--configDir
t	folders
=		--logFile
t	filepaths
=		-s
t	filepaths
=		--themesDir
t	filepaths
@	check
s	ulimit	Check system ulimit settings
o	-h|--help	help for check	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
a	1	0
=	check	--config
t	filepaths
=	check	--configDir
t	folders
=	check	--logFile
t	filepaths
=	check	-s
t	filepaths
=	check	--themesDir
t	filepaths
@	check ulimit
o	-h|--help	help for ulimit	
@	config
s	mounts	Print the configured file mounts
o	-h|--help	help for config	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
=	config	--config
t	filepaths
=	config	--configDir
t	folders
=	config	--logFile
t	filepaths
=	config	-s
t	filepaths
=	config	--themesDir
t	filepaths
@	config mounts
o	-h|--help	help for mounts	
@	convert
s	toJSON	Convert front matter to JSON
s	toTOML	Convert front matter to TOML
s	toYAML	Convert front matter to YAML
o	-h|--help	help for convert	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
a	1	0
=	convert	--config
t	filepaths
=	convert	--configDir
t	folders
=	convert	--logFile
t	filepaths
=	convert	-s
t	filepaths
=	convert	--themesDir
t	filepaths
@	convert toJSON
o	-h|--help	help for toJSON	
o	-o|--output	Filesystem path to write files to	v
o	--unsafe	Enable less safe operations, please backup first	
=	convert toJSON	-o
t	folders
@	convert toTOML
o	-h|--help	help for toTOML	
o	-o|--output	Filesystem path to write files to	v
o	--unsafe	Enable less safe operations, please backup first	
=	convert toTOML	-o
t	folders
@	convert toYAML
o	-h|--help	help for toYAML	
o	-o|--output	Filesystem path to write files to	v
o	--unsafe	Enable less safe operations, please backup first	
=	convert toYAML	-o
t	folders
@	deploy
o	-h|--help	help for deploy	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
o	--confirm	Ask for confirmation before making changes to the target	
o	--dryRun	Dry run	
o	--force	Force upload of all files	
o	--invalidateCDN	Invalidate the CDN cache listed in the deployment target (default true)	
o	--maxDeletes	Maximum # of files to delete, or -1 to disable (default 256)	v
o	--target	Target deployment from deployments section in config file; defaults to the first one	v
=	deploy	--config
t	filepaths
=	deploy	--configDir
t	folders
=	deploy	--logFile
t	filepaths
=	deploy	-s
t	filepaths
=	deploy	--themesDir
t	filepaths
@	env
o	-h|--help	help for env	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
o	-v	Get a full dependency list	
=	env	--config
t	filepaths
=	env	--configDir
t	folders
=	env	--logFile
t	filepaths
=	env	-s
t	filepaths
=	env	--themesDir
t	filepaths
@	gen
s	autocomplete	Generate shell autocompletion script for Hugo (default outputs to stdout)
s	chromastyles	Generate CSS stylesheet for the Chroma code highlighter (default outputs to stdout)
s	doc	Generate Markdown documentation for the Hugo CLI (default '/tmp/hugodoc/')
s	man	Generate man pages for the Hugo CLI (default 'man/')
o	-h|--help	help for gen	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
a	1	0
=	gen	--config
t	filepaths
=	gen	--configDir
t	folders
=	gen	--logFile
t	filepaths
=	gen	-s
t	filepaths
=	gen	--themesDir
t	filepaths
@	gen autocomplete
o	-h|--help	help for autocomplete	
o	-f|--completionfile	Autocompletion file, defaults to stdout	v
o	-t|--type	Autocompletion type (bash, zsh, fish, or powershell) (default 'bash')	v
=	gen autocomplete	-f
t	filepaths
=	gen autocomplete	-t
v	bash	Default
v	zsh	
v	fish	
v	powershell	
@	gen chromastyles
o	-h|--help	help for chromastyles	
o	--highlightStyle	Style used for highlighting lines (see https://github.com/alecthomas/chroma) (default 'bg:#ffffcc')	v
o	--linesStyle	Style used for line numbers (see https://github.com/alecthomas/chroma)	v
o	--style	Highlighter style (see https://help.farbox.com/pygments.html) (default 'friendly')	v
=	gen chromastyles	--style
v	friendly	Default
v	abap	
v	algol	
v	algol_nu	
v	api	
v	arduino	
v	autumn	
v	base16-snazzy	
v	borland	
v	bw	
v	colorful	
v	doom-one	
v	doom-one2	
v	dracula	
v	emacs	
v	fruity	
v	github	
v	hr_dark	
v	hr_high_contrast	
v	igor	
v	lovelace	
v	manni	
v	monokai	
v	monokailight	
v	murphy	
v	native	
v	nord	
v	paraiso-dark	
v	paraiso-light	
v	pastie	
v	perldoc	
v	pygments	
v	rainbow_dash	
v	rrt	
v	solarized-dark	
v	solarized-dark256	
v	solarized-light	
v	swapoff	
v	tango	
v	trac	
v	vim	
v	vs	
v	vulcan	
v	xcode-dark	
v	xcode	
@	gen doc
o	-h|--help	help for doc	
o	--dir	The directory to write the doc. (default '/tmp/hugodoc/')	v
=	gen doc	--dir
t	folders
@	gen man
o	-h|--help	help for man	
o	--dir	The directory to write the man pages. (default 'man/')	v
=	gen man	--dir
t	folders
@	help
a	1	0
#	help	1
v	check	
v	config	
v	convert	
v	deploy	
v	env	
v	gen	
v	help	
v	import	
v	list	
v	mod	
v	new	
v	server	
v	version	
@	import
s	jekyll	Import from Jekyll requires two paths, e.g. ` + `hugo import jekyll jekyll_root_path target_path`
o	-h|--help	help for import	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
a	1	0
=	import	--config
t	filepaths
=	import	--configDir
t	folders
=	import	--logFile
t	filepaths
=	import	-s
t	filepaths
=	import	--themesDir
t	filepaths
@	import jekyll
o	-h|--help	help for jekyll	
o	--force	Allow import into non-empty target directory	
a	2	0
#	import jekyll	1
t	folders
#	import jekyll	2
t	folders
@	list
s	drafts	List all drafts
s	future	List all posts dated in the future
s	expired	List all posts already expired
s	all	List all posts
o	-h|--help	help for list	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
a	1	0
=	list	--config
t	filepaths
=	list	--configDir
t	folders
=	list	--logFile
t	filepaths
=	list	-s
t	filepaths
=	list	--themesDir
t	filepaths
@	list drafts
o	-h|--help	help for drafts	
@	list future
o	-h|--help	help for future	
@	list expired
o	-h|--help	help for expired	
@	list all
o	-h|--help	help for all	
@	mod
s	clean	Delete the Hugo Module cache for the current project
s	get	Resolves dependencies in your current Hugo Project
s	graph	Use `hugo mod graph` from the relevant module directory and it will print the dependency graph…
s	init	Initialize this project as a Hugo Module
s	npm	Various npm helpers
s	tidy	Remove unused entries in go.mod and go.sum
s	vendor	Vendor all module dependencies into the _vendor directory
s	verify	Verify dependencies
o	-h|--help	help for mod	
o	-b|--baseURL	Hostname (and path) to the root, e.g. http://spf13.com/	v
o	-D|--buildDrafts	Include content marked as draft (default false)	v
o	-E|--buildExpired	Include expired content (default false)	v
o	-F|--buildFuture	Include content with publishdate in the future (default false)	v
o	--cacheDir	Filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/	v
o	--cleanDestinationDir	Remove files from destination not found in static directories (default false)	v
o	-c|--contentDir	Filesystem path to content directory	v
o	-d|--destination	Filesystem path to write files to	v
o	--disableKinds	Disable different kind of pages (home, RSS etc.)	v
o	--enableGitInfo	Add Git revision, date and author info to the pages (default false)	v
o	--forceSyncStatic	Copy all files when static is changed (default false)	v
o	--gc	Enable to run some cleanup tasks (remove unused cache files) after the build (default false)	v
o	--i18n-warnings	Print missing translations (default false)	v
o	--ignoreCache	Ignores the cache directory (default false)	v
o	-l|--layoutDir	Filesystem path to layout directory	v
o	--minify	Minify any supported output format (HTML, XML etc.) (default false)	v
o	--noChmod	Don't sync permission mode of files (default false)	v
o	--noTimes	Don't sync modification time of files (default false)	v
o	--path-warnings	Print warnings on duplicate target paths etc (default false)	v
o	--poll	Set this to a poll interval, e.g --poll 700ms, to use a poll based approach to watch for file…	v
o	--print-mem	Print memory usage to screen at intervals (default false)	v
o	--templateMetrics	Display metrics about template executions (default false)	v
o	--templateMetricsHints	Calculate some improvement hints when combined with --templateMetrics (default false)	v
o	-t|--theme	Themes to use (located in /themes/THEMENAME/)	v
o	--trace	Write trace to file (not useful in general)	v
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
a	1	0
=	mod	--cacheDir
t	folders
=	mod	-c
t	folders
=	mod	-d
t	folders
=	mod	--disableKinds
v	page	
v	home	
v	section	
v	taxonomy	
v	term	
v	RSS	
v	sitemap	
v	robotsTXT	
v	404	
=	mod	-l
t	folders
=	mod	--trace
t	filepaths
=	mod	--config
t	filepaths
=	mod	--configDir
t	folders
=	mod	--logFile
t	filepaths
=	mod	-s
t	filepaths
=	mod	--themesDir
t	filepaths
@	mod clean
o	-h|--help	help for clean	
o	--all	Clean entire module cache	
o	--pattern	Pattern matching module paths to clean (all if not set)", "e.g. "**hugo*"	v
@	mod get
o	-h|--help	help for get	
o	-d	Download packages only and do not install	
o	-f	Valid only when -u is set, forces get -u not to verify that each package has been checked out from…	
o	-fix	Run the fix tool on downloaded packages before resolving dependencies or building the code	
o	-insecure	Permits fetching from repositories and resolving custom domains using insecure schemes such as…	
o	-t	Also download the packages required to build the tests for the specified packages	
o	-u	Recursively update modules. Use network to update the named packages and their dependencies. By…	
o	-v	Enables verbose progress and debug output	
@	mod graph
o	-h|--help	help for graph	
@	mod init
o	-h|--help	help for init	
@	mod npm
s	pack	Experimental: Prepares and writes a composite package.json file for your project
o	-h|--help	help for npm	
@	mod npm pack
o	-h|--help	help for pack	
@	mod tidy
o	-h|--help	help for tidy	
@	mod vendor
o	-h|--help	help for vendor	
@	mod verify
o	-h|--help	help for verify	
o	--clean	Delete module cache for dependencies that fail verification	
@	new
s	site	Create a new site (skeleton)
s	theme	Create a new theme
o	-h|--help	help for new	
o	-b|--baseURL	Hostname (and path) to the root, e.g. http://spf13.com/	v
o	-D|--buildDrafts	Include content marked as draft (default false)	v
o	-E|--buildExpired	Include expired content (default false)	v
o	-F|--buildFuture	Include content with publishdate in the future (default false)	v
o	--cacheDir	Filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/	v
o	--cleanDestinationDir	Remove files from destination not found in static directories (default false)	v
o	-c|--contentDir	Filesystem path to content directory	v
o	-d|--destination	Filesystem path to write files to	v
o	--disableKinds	Disable different kind of pages (home, RSS etc.)	v
o	--enableGitInfo	Add Git revision, date and author info to the pages (default false)	v
o	--forceSyncStatic	Copy all files when static is changed (default false)	v
o	--gc	Enable to run some cleanup tasks (remove unused cache files) after the build (default false)	v
o	--i18n-warnings	Print missing translations (default false)	v
o	--ignoreCache	Ignores the cache directory (default false)	v
o	-l|--layoutDir	Filesystem path to layout directory	v
o	--minify	Minify any supported output format (HTML, XML etc.) (default false)	v
o	--noChmod	Don't sync permission mode of files (default false)	v
o	--noTimes	Don't sync modification time of files (default false)	v
o	--path-warnings	Print warnings on duplicate target paths etc (default false)	v
o	--poll	Set this to a poll interval, e.g --poll 700ms, to use a poll based approach to watch for file…	v
o	--print-mem	Print memory usage to screen at intervals (default false)	v
o	--templateMetrics	Display metrics about template executions (default false)	v
o	--templateMetricsHints	Calculate some improvement hints when combined with --templateMetrics (default false)	v
o	-t|--theme	Themes to use (located in /themes/THEMENAME/)	v
o	--trace	Write trace to file (not useful in general)	v
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
o	-k|--kind	Content type to create	v
o	--editor	Edit new content with this editor, if provided	v
a	1	0
=	new	--cacheDir
t	folders
=	new	-c
t	folders
=	new	-d
t	folders
=	new	--disableKinds
v	page	
v	home	
v	section	
v	taxonomy	
v	term	
v	RSS	
v	sitemap	
v	robotsTXT	
v	404	
=	new	-l
t	folders
=	new	--trace
t	filepaths
=	new	--config
t	filepaths
=	new	--configDir
t	folders
=	new	--logFile
t	filepaths
=	new	-s
t	filepaths
=	new	--themesDir
t	filepaths
=	new	-k
d
@	new site
o	-h|--help	help for site	
o	--force	Init inside non-empty directory	
o	-f|--format	Config & frontmatter format (default "toml")	v
a	1	0
=	new site	-f
v	toml	Default
v	yaml	
v	json	
#	new site	1
t	folders
@	new theme
o	-h|--help	help for theme	
a	1	0
@	server
o	-h|--help	help for server	
o	-b|--baseURL	Hostname (and path) to the root, e.g. http://spf13.com/	v
o	-D|--buildDrafts	Include content marked as draft (default false)	v
o	-E|--buildExpired	Include expired content (default false)	v
o	-F|--buildFuture	Include content with publishdate in the future (default false)	v
o	--cacheDir	Filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/	v
o	--cleanDestinationDir	Remove files from destination not found in static directories (default false)	v
o	-c|--contentDir	Filesystem path to content directory	v
o	-d|--destination	Filesystem path to write files to	v
o	--disableKinds	Disable different kind of pages (home, RSS etc.)	v
o	--enableGitInfo	Add Git revision, date and author info to the pages (default false)	v
o	--forceSyncStatic	Copy all files when static is changed (default false)	v
o	--gc	Enable to run some cleanup tasks (remove unused cache files) after the build (default false)	v
o	--i18n-warnings	Print missing translations (default false)	v
o	--ignoreCache	Ignores the cache directory (default false)	v
o	-l|--layoutDir	Filesystem path to layout directory	v
o	--minify	Minify any supported output format (HTML, XML etc.) (default false)	v
o	--noChmod	Don't sync permission mode of files (default false)	v
o	--noTimes	Don't sync modification time of files (default false)	v
o	--path-warnings	Print warnings on duplicate target paths etc (default false)	v
o	--poll	Set this to a poll interval, e.g --poll 700ms, to use a poll based approach to watch for file…	v
o	--print-mem	Print memory usage to screen at intervals (default false)	v
o	--templateMetrics	Display metrics about template executions (default false)	v
o	--templateMetricsHints	Calculate some improvement hints when combined with --templateMetrics (default false)	v
o	-t|--theme	Themes to use (located in /themes/THEMENAME/)	v
o	--trace	Write trace to file (not useful in general)	v
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
o	-w|--watch	Watch filesystem for changes and recreate as needed (default true)	v
o	--appendPort	Append port to baseURL (default true)	v
o	--bind	Interface to which the server will bind (default '127.0.0.1')	v
o	--disableBrowserError	Do not show build errors in the browser (default false)	v
o	--disableFastRender	Enables full re-renders on changes (default false)	v
o	--disableLiveReload	Watch without enabling live browser reload on rebuild (default false)	v
o	--liveReloadPort	Port for live reloading (i.e. 443 in HTTPS proxy situations) (default -1)	v
o	--meminterval	Interval to poll memory usage (requires --memstats), valid time units are 'ns', 'us' (or 'µs')…	v
o	--memstats	Log memory usage to this file	v
o	--navigateToChanged	Navigate to changed content file on live browser reload (default false)	v
o	--noHTTPCache	Prevent HTTP caching (default false)	v
o	-p|--port	Port on which the server will listen (default 1313)	v
o	--renderToDisk	Render to Destination path (default is false: render to memory & serve from there)	v
=	server	--cacheDir
t	folders
=	server	-c
t	folders
=	server	-d
t	folders
=	server	--disableKinds
v	page	
v	home	
v	section	
v	taxonomy	
v	term	
v	RSS	
v	sitemap	
v	robotsTXT	
v	404	
=	server	-l
t	folders
=	server	--trace
t	filepaths
=	server	--config
t	filepaths
=	server	--configDir
t	folders
=	server	--logFile
t	filepaths
=	server	-s
t	filepaths
=	server	--themesDir
t	filepaths
=	server	--memstats
t	filepaths
@	version
o	-h|--help	help for version	
o	--config	Config file (default is path/config.yaml|json|toml)	v
o	--configDir	Config dir (default 'config')	v
o	--debug	Debug output (default false)	v
o	-e|--environment	Build environment	v
o	--ignoreVendor	Ignores any _vendor directory (default false)	v
o	--ignoreVendorPaths	Ignores any _vendor for module paths matching the given Glob pattern	v
o	--log	Enable Logging (default false)	v
o	--logFile	Log File path (if set, logging enabled automatically)	v
o	--quiet	Build in quiet mode (default false)	v
o	-s|--source	Filesystem path to read files relative from	v
o	--themesDir	Filesystem path to themes directory	v
o	-v|--verbose	Verbose output (default false)	v
o	--verboseLog	Verbose logging (default false)	v
=	version	--config
t	filepaths
=	version	--configDir
t	folders
=	version	--logFile
t	filepaths
=	version	-s
t	filepaths
=	version	--themesDir
t	filepaths

@	
s	start	Start Browsersync
s	init	Create a configuration file
s	reload	Send a reload event over HTTP protocol
s	recipe	Generate the files for a recipe
o	--version	Show version number	
o	--help	Show help	p
a	1	1
#		1
t	folders
@	start
o	-s|--server	Run a Local server (uses your cwd as the web root)	
o	--cwd	Working directory	v
o	--json	If true, certain logs will output as json only	
o	--serveStatic|--ss	Directories to serve static files from	v
o	--port	Specify a port to use	v
o	-p|--proxy	Proxy an existing server	
o	--ws	Proxy mode only - enable websocket proxying	
o	-b|--browser	Choose which browser should be auto-opened	v
o	-w|--watch	Watch files	
o	--ignore	Ignore patterns for file watchers	v
o	-f|--files	File paths to watch	v
o	--index	Specify which file should be used as the index page	v
o	--plugins	Load Browsersync plugins	v
o	--extensions	Specify file extension fallbacks	v
o	--startPath	Specify the start path for the opened browser	v
o	--single	If true, the connect-history-api-fallback middleware will be added	
o	--https	Enable SSL for local development	
o	--directory	Show a directory listing for the server	
o	--xip	Use xip.io domain routing	
o	--tunnel	Use a public URL	
o	--open	Choose which URL is auto-opened (local, external or tunnel), or provide a url	v
o	--cors	Add Access Control headers to every request	
o	-c|--config	Specify a path to a configuration file	v
o	--host	Specify a hostname to use	v
o	--listen	Specify a hostname bind to (this will prevent binding to all interfaces)	v
o	--logLevel	Set the logger output level (silent, info or debug)	v
o	--reload-delay	Time in milliseconds to delay the reload event following file changes	v
o	--reload-debounce	Restrict the frequency in which browser:reload events can be emitted to connected clients	v
o	--ui-port	Specify a port for the UI to use	v
o	--watchEvents	Specify which file events to respond to	v
o	--no-notify	Disable the notify element in browsers	
o	--no-open	Don't open a new browser window	
o	--no-snippet	Disable the snippet injection	
o	--no-online	Force offline usage	
o	--no-ui	Don't start the user interface	
o	--no-ghost-mode	Disable Ghost Mode	
o	--no-inject-changes	Reload on every file change	
o	--no-reload-on-restart	Don't auto-reload all browsers following a restart	
=	start	--cwd
t	folders
=	start	--serveStatic
t	folders
=	start	-f
t	filepaths
=	start	--index
t	filepaths
=	start	--open
v	local	
v	external	
v	tunnel	
=	start	-c
t	filepaths
=	start	--logLevel
v	silent	
v	info	
v	debug	
@	init
o	--cwd	Working directory	v
=	init	--cwd
t	folders
@	reload
o	-f|--files	File paths to reload	v
o	-p|--port	Target a running instance by port number	v
o	-u|--url	Provide the full URL to the running browsersync isntance	v
o	--cwd	Working directory	v
=	reload	-f
t	filepaths
=	reload	--cwd
t	folders
@	recipe
s	ls	List recipes
o	--cwd	Working directory	v
o	-o|--output	Specify an output directory	v
a	1	0
=	recipe	--cwd
t	folders
=	recipe	-o
t	folders
#	recipe	1
g	bash -c 'browser-sync recipe ls | tail -n +3 | sed -e '\''s/^[[:space:]]*//'\'''	\n
@	recipe ls

@	
s	create	Create a new project powered by vue-cli-service
s	add	Install a plugin and invoke its generator in an already created project
s	invoke	Invoke the generator of a plugin in an already created project
s	inspect	Inspect the webpack config in a project with vue-cli-service
s	serve	Serve a .js or .vue file in development mode with zero config
s	build	Build a .js or .vue file in production mode with zero config
s	ui	Start and open the vue-cli ui
s	init	Generate a project from a remote template (legacy API, requires @vue/cli-init)
s	config	Inspect and modify the config
s	outdated	(experimental) check for outdated vue cli service / plugins
s	upgrade	(experimental) upgrade vue cli service / plugins
s	migrate	(experimental) run migrator for an already-installed cli plugin
s	info	Print debugging information about your environment
o	-V|--version	Output the version number	
o	-h|--help	Output usage information	
@	create
o	-p|--preset	Skip prompts and use saved or remote preset	v
o	-d|--default	Skip prompts and use default preset	
o	-i|--inlinePreset	Skip prompts and use inline JSON string as preset	v
o	-m|--packageManager	Use specified npm client when installing dependencies	v
o	-r|--registry	Use specified npm registry when installing dependencies (only for npm)	v
o	-g|--git	Force git initialization with initial commit message	v
o	-n|--no-git	Skip git initialization	
o	-f|--force	Overwrite target directory if it exists	
o	--merge	Merge target directory if it exists	
o	-c|--clone	Use git clone when fetching remote preset	
o	-X|--proxy	Use specified proxy when creating project	v
o	-b|--bar	Scaffold project without beginner instructions	
o	--skipGetStarted	Skip displaying "Get started" instructions	
o	-h|--help	Output usage information	
a	1	0
@	add
o	--registry	Use specified npm registry when installing dependencies (only for npm)	v
o	-h|--help	Output usage information	
a	1	0
@	invoke
o	--registry	Use specified npm registry when installing dependencies (only for npm)	v
o	-h|--help	Output usage information	
a	1	0
@	inspect
o	--mode		v
o	--rule	Inspect a specific module rule	v
o	--plugin	Inspect a specific plugin	v
o	--rules	List all module rule names	
o	--plugins	List all plugin names	
o	-v|--verbose	Show full function definitions in output	
o	-h|--help	Output usage information	
a	1	0
@	serve
o	-o|--open	Open browser	
o	-c|--copy	Copy local url to clipboard	
o	-p|--port	Port used by the server (default: 8080 or next available port)	v
o	-h|--help	Output usage information	
a	1	0
#	serve	1
t	filepaths
@	build
o	-t|--target	Build target (app | lib | wc | wc-async, default: app)	v
o	-n|--name	Name for lib or web-component mode (default: entry filename)	v
o	-d|--destination	Output directory (default: dist)	v
o	-h|--help	Output usage information	
a	1	0
#	build	1
t	filepaths
@	ui
o	-H|--host	Host used for the UI server (default: localhost)	v
o	-p|--port	Port used for the UI server (by default search for available port)	v
o	-D|--dev	Run in dev mode	
o	--quiet	Don't output starting messages	
o	--headless	Don't open browser on start and output port	
o	-h|--help	Output usage information	
@	init
o	-c|--clone	Use git clone when fetching remote template	
o	--offline	Use cached template	
o	-h|--help	Output usage information	
a	2	0
@	config
o	-g|--get	Get value from option	v
o	-s|--set	Set option value	v
o	-d|--delete	Delete option from config	v
o	-e|--edit	Open config with default editor	
o	--json	Outputs JSON result only	
o	-h|--help	Output usage information	
a	1	0
@	outdated
o	--next	Also check for alpha / beta / rc versions when upgrading	
o	-h|--help	Output usage information	
@	upgrade
o	-t|--to	Upgrade <package-name> to a version that is not latest	v
o	-f|--from	Skip probing installed plugin, assuming it is upgraded from the designated version	v
o	-r|--registry	Use specified npm registry when installing dependencies	v
o	--all	Upgrade all plugins	
o	--next	Also check for alpha / beta /rc versions when upgrading	
o	-h|--help	Output usage information	
a	1	0
@	migrate
o	-f|--from	The base version for the migrator to migrate from	v
o	-h|--help	Output usage information	
a	1	0
@	info
o	-h|--help	Output usage information	

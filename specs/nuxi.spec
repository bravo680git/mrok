@	
s	info	The info command logs information about the current or specified Nuxt project
s	init|create	The init command initializes a fresh Nuxt project
s	add|new	Generate a entity into your Nuxt application
s	analyze	The analyze command builds Nuxt and analyzes the production bundle (experimental)
s	build	The build command creates a .output directory with all your application, server and dependencies…
s	dev	The dev command starts a development server with hot module replacement at http://localhost:3000
s	prepare	The prepare command creates a .nuxt directory in your application and generates ts types
s	preview	The preview command starts a server to preview your Nuxt application after running the build command
s	generate	Build Nuxt and prerender static routes
s	clean|cleanup	The cleanup command removes common generated Nuxt files and caches including .nuxt/, .output/…
s	test	Run the test files for your Nuxt application
s	upgrade	The upgrade command upgrades Nuxt 3 to the latest version
s	typecheck	The typecheck command runs vue-tsc to check types throughout your app
s	usage	The usage command shows the usage of the Nuxt CLI
o	--help	Show help	p
@	info
a	1	0
#	info	1
t	folders
@	init
o	--verbose|-v	Log information about the installation process	
o	--template|-t	Specify a Git repository to use as a template	
o	--force	Force clone to any existing directory	
o	--prefer-offline	Try local cache first to download templates	
o	--shell	Open shell in cloned directory (experimental)	
a	1	0
@	add
o	--cwd	The current working directory of the target application	
o	--force	Force override file if it already exists	
a	2	0
#	add	1
v	component	Generate a nuxt component
v	composable	Generate a nuxt composable
v	layout	Generate a nuxt layout
v	plugin	Generate a nuxt plugin
v	page	Generate a nuxt page
v	middleware	Generate a nuxt middleware
v	api	Generate a nuxt api
@	analyze
a	1	0
#	analyze	1
t	folders
@	build
o	--dotenv	Point to another .env file to load, relative to the root directory	
o	--prerender	Pre-render every route of your application. (note: This is an experimental flag. The behavior…	
a	1	0
#	build	1
t	folders
@	dev
o	--dotenv	Point to another .env file to load, relative to the root directory	
o	--clipboard	Copy URL to clipboard	
o	--open|-o	Open URL in browser	
o	--no-clear	Does not clear the console after startup	
o	--port|-p	Port to listen	
o	--host|-h	Hostname of the server	
o	--https	Listen with https protocol with a self-signed certificate by default	
o	--ssl-cert	Specify a certificate for https	
o	--ssl-key	Specify the key for the https certificate	
a	1	0
#	dev	1
t	folders
@	prepare
@	preview
o	--dotenv	Point to another .env file to load, relative to the root directory	
a	1	0
#	preview	1
t	folders
@	generate
a	1	0
#	generate	1
t	folders
@	clean
a	1	0
#	clean	1
t	folders
@	test
o	--dev	Run tests in development mode	
o	--watch	Actively watch for changes and rerun tests	
a	1	0
#	test	1
t	folders
@	upgrade
o	--force|-f	Removes node_modules and lock files before upgrade	
@	typecheck
a	1	0
#	typecheck	1
t	folders
@	usage

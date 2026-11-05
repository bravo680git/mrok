@	
s	config	Get or set configurations
s	help	Displays a help for each command
s	init	Create a new Hexo folder
s	new	Create a new article
s	generate	Generate static files
s	publish	Publish a draft
s	server	Start a local server. By default, this is at http://localhost:4000/
s	deploy	Deploy your website
s	render	Render files with renderer plugins (e.g. Markdown) and save them at the specified path
s	migrate	Migrate content from other blog systems
s	clean	Clean the cache file (`db.json`) and generated files (`public`)
s	list	List all routes
s	version	Display version information
o	--config	Uses a custom config file (instead of `_config.yml`). Also accepts a comma-separated list (no…	vp
o	--safe	Disable loading plugins and scripts	p
o	--debug	Log verbose messages to the terminal and to `debug.log`	p
o	--silent	Silence output to the terminal	p
o	--draft	Display draft posts (stored in the `source/_drafts` folder)	p
o	--cwd	Customize the path of current working directory	vp
=		--config
t	filepaths
=		--cwd
t	folders
@	config
a	2	0
@	help
a	1	0
#	help	1
t	help
@	init
o	--no-clone	Copy files instead of cloning from GitHub	
o	--no-install	Skip npm install	
a	1	0
#	init	1
t	folders
@	new
o	-p|--path	Post path. Customize the path of the post	v
o	-r|--replace	Replace the current post if it existed	
o	-s|--slug	Post slug. Customize the URL of the post	v
a	2	0
=	new	-p
t	filepaths
#	new	1
v	post	
v	page	
v	draft	
@	generate
o	-d|--deploy	Deploy after generation finishes	
o	-f|--force	Force regenerate	
o	-w|--watch	Watch file changes	
o	-b|--bail	Raise an error if any unhandled exception is thrown during generation	
o	-c|--concurrency	Maximum number of files to be generated in parallel. Default is infinity	V
@	publish
a	2	0
#	publish	1
v	post	
v	page	
v	draft	
#	publish	2
d
@	server
o	-i|--ip	Override the default server IP. Bind to all IP address by default	v
o	-p|--port	Override default port	v
o	-s|--static	Serve static files from the given directory	
o	-l|--log	Enable logger. Override logger format	V
o	-o|--open	Immediately open the server url in your default web browser	
=	server	-l
v	combined	
v	common	
v	tiny	
v	dev	
v	short	
@	deploy
o	--setup	Setup without deployment	
o	-g|--generate	Generate static files before deploying	
@	render
o	--engine	Specify render engine	
o	-o|--output	Output destination. Result will be printed in the terminal if the output destination is not set	v
o	--pretty	Prettify JSON output	
a	1	1
=	render	-o
t	folders
#	render	1
t	filepaths
@	migrate
a	1	0
@	clean
@	list
a	1	0
#	list	1
v	post	
v	route	
v	page	
v	tag	
v	category	
@	version

@	
s	help	Print this message or the help of the given subcommand(s)
s	build	Generates a model or place file from the Rojo project
s	doc	Open Rojo's documentation in your browser
s	fmt-project	Reformat a Rojo project using the standard JSON formatting rules
s	init	Initializes a new Rojo project
s	plugin	Install Rojo's plugin
s	serve	Expose a Rojo project to the Rojo Studio plugin
s	sourcemap	Generates a sourcemap file from the Rojo project
s	upload	Builds the project and uploads it to Roblox
o	--help|-h	Print help information	p
o	--color	Set color behavior. Valid values are auto, always, and never [default: auto]	vp
o	--verbose|-v	Sets verbosity level. Can be specified multiple times	p
o	--version|-V	Print version information	
=		--color
v	auto	
v	always	
v	never	
@	help
a	1	0
#	help	1
t	help
@	build
o	--output|-o	Where to output the result. Should end in .rbxm, .rbxl, .rbxmx, or .rbxlx	v
o	--watch	Whether to automatically rebuild when any input files change	
a	1	0
=	build	--output
d
@	doc
@	fmt-project
a	1	0
@	init
o	--kind	The kind of project to create, 'place' or 'model'. Defaults to place	v
a	1	0
=	init	--kind
v	place	
v	model	
@	plugin
@	serve
o	address	The IP address to listen on. Defaults to `127.0.0.1`	v
@	sourcemap
o	--include-non-scripts	If non-script files should be included or not. Defaults to false	
o	--output|-o	Where to output the sourcemap. Omit this to use stdout instead of writing to a file. Should end in…	v
a	1	0
=	sourcemap	--output
d
@	upload
o	--api-key	API key obtained from create.roblox.com/credentials. Rojo will use the Open Cloud API when this is…	v
o	--asset_id	Asset ID to upload to	v
o	--cookie	Authenication cookie to use. If not specified, Rojo will attempt to find one from the system…	v
o	--universe_id	The Universe ID of the given place. Required when using the Open Cloud API	v
a	1	0

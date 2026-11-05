@	
s	build	Build for production
s	optimize	Pre-bundle dependencies
s	preview	Locally preview the production build
o	-h|--help	Show help message	p
o	--host	Specify the hostname	V
o	--port	Specify the port	v
o	--https	Use TLS + HTTP/2	
o	--open	Open browser on startup	V
o	--cors	Enable CORS	
o	--strictPort	Exit if the port is already in use	
o	--force	For the optimizer to re-bundle	
o	-c|--config	Use the specified config file	vp
o	--base	Public base path	vp
o	-l|--logLevel	Set the log level	vp
o	--clearScreen	Enable screen clearing when logging	p
o	-d|--debug	Show debug logs	Vp
o	-f|--filter	Filter debug logs	vp
o	-m|--mode	Set env mode	vp
o	-v|--version	Display version number	
a	1	0
=		--open
t	filepaths
=		-c
t	filepaths
=		-l
v	info	
v	warn	
v	error	
v	silent	
=		-m
d
#		1
t	folders
@	build
o	--target	Transpile target (must be a valid esbuild target)	v
o	--outDir	Output directory	v
o	--assetsDir	Directory under outDir to place assets in	v
o	--assetsInlineLimit	Static asset base64 inline threshold in bytes	v
o	--ssr	Build specified entry for server-side rendering	V
o	--sourcemap	Output sourcemaps for build	
o	--minify	Enable minification	V
o	--manifest	Emit build manifest json	V
o	--ssrManifest	Emit ssr manifest json	V
o	--emptyOutDir	Force empty outDir when it's outside of root	
o	-w|--watch	Rebuilds when modules have changed on disk	
a	1	0
=	build	--outDir
t	folders
=	build	--assetsDir
t	folders
=	build	--ssr
t	filepaths
=	build	--minify
v	terser	
v	esbuild	
#	build	1
t	folders
@	optimize
o	--force	For the optimizer to re-bundle	
a	1	0
#	optimize	1
t	folders
@	preview
o	--host	Specify the hostname	V
o	--port	Specify the port	v
o	--https	Use TLS + HTTP/2	
o	--open	Open browser on startup	V
o	--strictPort	Exit if the port is already in use	
a	1	0
=	preview	--open
t	filepaths
#	preview	1
t	folders

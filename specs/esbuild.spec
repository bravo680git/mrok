@	
o	--bundle	Bundle all dependencies into the output files	
o	--define	Replace variable names with a literal value, eg. --define:DEBUG=true	v
o	--external	Exclude modules from the build	v
o	--format	The output format	v=
o	--loader	For a given file extension, specify a loader	v
o	--minify	Minify the output (sets all the --minify-* options)	
o	--outdir	The output directory for multiple entrypoints	v=
o	--outfile	The output file for one entrypoint	v=
o	--platform	The platform target	v=
o	--serve	Start a local HTTP server on this host:port	V=
o	--splitting	Enable code splitting	
o	--target	Set the environment target. Can be a particular ES version or browser version, eg. chrome101	v=
o	--watch	Rebuild on file system changes	V=
o	--allow-overwrite	Allow output files to overwrite input files	
o	--analyze	Print a report about the contents of the bundle	V=
o	--asset-names	Path template for 'file' loader files	v=
o	--banner	Text to be prepended to each output file type	v
o	--charset	Use UTF-8 instead of escaped codepoints in ASCII	v=
o	--chunk-names	Path template to use for code splitting chunks	v=
o	--color	Force use of terminal colors	v=
o	--drop	Remove certain constructs	v
o	--entry-names	Path template to use for entry point output paths	v=
o	--footer	Text to be appended to each file type	v
o	--global-name	The name of the global if using --format=iife	v=
o	--ignore-annotations	Enable this to work with packages that have incorrect tree-shaking annotations	
o	--inject	Import the file into all input files, automatically replace matching globals	v
o	--jsx-factory	What to use for the JSX factory	v=
o	--jsx-fragment	What to use for the JS Fragment factory	v=
o	--jsx	Preserve JSX instead of transforming	v=
o	--jsx-dev	Toggles development mode for the automatic runtime	
o	--jsx-import-source	Overrides the root import for runtime functions (default: react)	v=
o	--keep-names	Preserve 'name' on functions and classes	
o	--legal-comments	Where to place legal comments	v=
o	--log-level	Set the log level	v=
o	--log-limit	Maximum message count, 0 to disable	v=
o	--log-override	For a particular identifier, set the log level	v
o	--main-fields	Override the main file order in package.json	v=
o	--mangle-cache	Save 'mangle props' decisions to a JSON file	v=
o	--mangle-props	Rename all properties matching a regular expression	v=
o	--mangle-quoted	Enable mangling (renaming) quoted properties	v=
o	--metafile	Write metadata about the build to a JSON file	v=
o	--minify-whitespace	Remove unnecessary whitespace in output files	
o	--minify-identifiers	Shorten identifiers in output files	
o	--minify-syntax	Use equivalent but shorter syntax in output files	
o	--out-extension	Use a custom output extension for each extension	v
o	--outbase	Base path used to determine entrypoint output paths, for multiple entrypoints	v=
o	--preserve-symlinks	Disable symlink resolution	
o	--public-path	Set the base URL for the 'file' loader	v=
o	--pure	Mark the name as a pure function for tree shaking	v
o	--reserve-props	Do not mangle these properties	v=
o	--resolve-extensions	Comma-separated list of implicit extensions	v=
o	--servedir	What to serve in addition to the generated output files	v=
o	--source-root	Set the sourceRoot field in generated source maps	v=
o	--sourcefile	Set the source file for the source map if there's no file name to use	v=
o	--sourcemap	Generate source maps?	V=
o	--sources-content	Omit the sourcesContent field in generated source maps	v=
o	--supported	Consider a given syntax to be supported	v
o	--tree-shaking	Force tree shaking on or off	v=
o	--tsconfig	Use this TypeScript config instead of the default	v=
o	--version	Print the current version and exit	
a	1	1
=		--format
v	iife	
v	cjs	
v	esm	
=		--loader
d
=		--outdir
t	folders
=		--outfile
t	filepaths
=		--platform
v	browser	
v	node	
v	neutral	
=		--target
d
=		--watch
v	forever	
=		--analyze
v	verbose	
=		--banner
d
=		--color
v	true	
v	false	
=		--drop
v	console	
v	debugger	
=		--footer
d
=		--inject
t	filepaths
=		--jsx-factory
v	React.createElement	
v	h	
v	preact.h	
=		--jsx-fragment
v	React.Fragment	
v	Fragment	
=		--jsx
v	preserve	Preserve JSX instead of transforming
v	automatic	Use React's new automatic JSX transform
=		--legal-comments
v	none	
v	inline	
v	eof	
v	linked	
v	external	
=		--log-level
v	verbose	
v	debug	
v	info	
v	warning	
v	error	
v	silent	
=		--log-override
d
=		--mangle-cache
t	filepaths
=		--mangle-quoted
v	true	
v	false	
=		--metafile
t	filepaths
=		--out-extension
d
=		--outbase
t	folders
=		--public-path
t	folders
=		--resolve-extensions
d
=		--servedir
t	folders
=		--sourcemap
v	external	Generate a separate .map.js file with no comment
v	inline	Append source maps to JS files
=		--sources-content
v	false	
=		--supported
d
=		--tree-shaking
v	true	
v	false	
=		--tsconfig
t	filepaths
#		1
t	filepaths

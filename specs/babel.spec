@	
o	-f|--filename	The filename to use when reading from stdin. This will be used in source-maps, errors etc	v
o	--presets	A comma-separated list of preset names	v
o	--plugins	A comma-separated list of plugin names	v
o	--config-file	Path to a .babelrc file to use	v
o	--env-name	The name of the 'env' to use when loading configs and plugins. Defaults to the value of BABEL_ENV…	v
o	--root-mode	The project-root resolution mode	v
o	--source-type		v
o	--no-babelrc	Whether or not to look up .babelrc and .babelignore files	
o	--ignore	List of glob paths to **not** compile	v
o	--only	List of glob paths to **only** compile	v
o	--no-highlight-code	Enable or disable ANSI syntax highlighting of code frames	
o	--no-comments	Write comments to generated output	
o	--retain-lines	Retain line numbers. This will result in really ugly code	
o	--compact	Do not include superfluous whitespace characters and line terminators	v
o	--minified	Save as many bytes when printing. (false by default)	
o	--auxiliary-comment-before	Print a comment before any injected non-user code	v
o	--auxiliary-comment-after	Print a comment after any injected non-user code	v
o	-s|--source-maps		v
o	--source-map-target	Set `file` on returned source map	v
o	--source-file-name	Set `sources[0]` on returned source map	v
o	--source-root	The root from which all sources are relative	v
o	-x|--extensions	Comma separated list of extensions to compile when a directory has been the input. [js,ts,jsx,tsx]	v
o	--keep-file-extension	Preserve the file extensions of the input files	
o	-w|--watch	Recompile files on changes	
o	--skip-initial-build	Do not compile files before watching	
o	-o|--out-file	Compile all input files into a single file	v
o	-d|--out-dir	Compile an input directory of modules into an output directory	v
o	--relative	Compile into an output directory relative to input directory or file	
o	-D|--copy-files	When compiling a directory copy over non-compilable files	
o	--include-dotfiles	Include dotfiles when compiling and copying non-compilable files	
o	--no-copy-ignored	Exclude ignored files when copying non-compilable files	
o	--verbose	Log everything. This option conflicts with --quiet	
o	--quiet	Don't log anything. This option conflicts with --verbose	
o	--delete-dir-on-start	Delete the out directory before compilation	
o	--out-file-extension	Use a specific extension for the output files	v
o	-V|--version	Output the version number	
o	-h|--help	Output usage information	
=		--config-file
t	filepaths
=		--env-name
v	production	
v	development	
=		--root-mode
v	root	Passes the "root" value through as unchanged
v	upward	Walks upward from the "root" directory, looking for a directory containing a babel.config.json…
v	upward-optional	Walk upward from the "root" directory, looking for a directory containing a babel.config.json…
=		--source-type
v	script	
v	module	
=		--compact
v	true	
v	false	
v	auto	
=		-s
v	true	
v	false	
v	inline	
v	both	
=		-o
t	filepaths
=		-d
t	folders
=		--out-file-extension
v	.es6	
v	.js	
v	.es	
v	.jsx	
v	.mjs	

@	
o	--filename|-f	Filename to use when reading from stdin. This will be used in source maps and errors	v
o	--config-file	Path to a .swcrc file to use	v
o	--env-name	The name of the 'env' to use when loading configs and plugins. Defaults to the value of SWC_ENV…	v
o	--no-swcrc	Whether or not to look up .swcrc files	
o	--ignore	List of glob paths to not compile	v
o	--only	List of glob paths to only compile	v
o	--watch|-w	Watch for changes and recompile	
o	--quiet|-q	Suppress compilation output	
o	--source-maps|-s	Generate source maps	v
o	--source-map-target	Define the file for the source map	v
o	--source-file-name	Set sources[0] on returned source map	
o	--source-root	The root from which all sources are relative	
o	--out-file|-o	Compile all input files into a single file	v
o	--out-dir|-d	Compile an input directory of modules into an output directory	v
o	--copy-files|-D	When compiling a directory, copy over non-compilable files	
o	--include-dotfiles	Include dotfiles when compiling and copying non-compilable files	
o	--config|-C	Override a config from .swcrc file	v
o	--sync	Invoke swc synchronously. Useful for debugging	
o	--log-watch-compilation	Log a message when a watched file is successfully compiled	
o	--extensions	Log a message when a watched file is successfully compiled	
=		--filename
t	filepaths
=		--config-file
t	filepaths
=		--env-name
v	production	
v	development	
v	test	
=		--ignore
t	filepaths,folders
=		--only
t	filepaths,folders
=		--source-maps
v	true	
v	false	
v	inline	
v	both	
=		--source-map-target
t	filepaths
=		--out-file
t	filepaths
=		--out-dir
t	folders
=		--config
t	filepaths

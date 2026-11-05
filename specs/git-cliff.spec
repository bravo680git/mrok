@	
o	--verbose|-v	Increases the logging verbosity	
o	--init|-i	Writes the default configuration file to cliff.toml	
o	--latest|-l	Processes the commits starting from the latest tag	
o	--current	Processes the commits that belong to the current tag	
o	--unreleased|-u	Processes the commits that do not belong to a tag	
o	--date-order	Sorts the tags chronologically	
o	--context	Prints changelog context as JSON	
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--config|-c	Sets the configuration file	v
o	--workdir|-w	Sets the working directory	v
o	--repository|-r	Sets the git repository	v
o	--include-path	Sets the path to include related commits	v
o	--exclude-path	Sets the path to exclude related commits	v
o	--with-commit	Sets custom commit messages to include in the changelog	v
o	--prepend|-p	Prepends entries to the given changelog file	v
o	--output|-o	Writes output to the given file	v
o	--tag|-t	Sets the tag for the latest version	v
o	--body|-b	Sets the template for the changelog body	v
o	--strip|-s	Strips the given parts from the changelog	v
o	--sort	Sets sorting of the commits inside sections	v
a	1	0
=		--config
t	filepaths
=		--workdir
t	folders
=		--repository
t	folders
=		--prepend
t	filepaths
=		--output
t	filepaths
=		--strip
v	header	
v	footer	
v	all	
=		--sort
v	oldest	
v	newest	
#		1
d

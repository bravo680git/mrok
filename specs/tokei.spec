@	
o	-f|--files	Will print out statistics on individual files	
o	-h|--help	Prints help information	
o	--hidden	Count hidden files	
o	-l|--languages	Prints out supported languages and their extensions	
o	--no-ignore	Don't respect ignore files (.gitignore, .ignore, etc.)	
o	--no-ignore-dot	Don't respect .ignore and .tokeignore files, including those in parent directories	
o	--no-ignore-parent	Don't respect ignore files (.gitignore, .ignore, etc.) in parent directories	
o	--no-ignore-vcs	Don't respect VCS ignore files (.gitignore, .hgignore, etc.), including those in parent directories	
o	-V|--version	Prints version information	
o	-v|--verbose	Set log output level:	
o	-c|--columns	Sets a strict column width of the output, only available for terminal output	v
o	-e|--exclude	Ignore all files & directories matching the pattern	v
o	-i|--input	Gives statistics from a previous tokei run. Can be given a file path, or "stdin" to read from stdin	v
o	-o|--output	Outputs Tokei in a specific format	v
o	-s|--sort	Sort languages based on column	v
o	-t|--type	Filters output by language type, seperated by a comma. i.e. -t=Rust,Markdown	v
=		-e
t	filepaths
=		-i
v	stdin	
t	filepaths
=		-o
v	cbor	
v	json	
v	yaml	
=		-s
v	files	
v	lines	
v	blanks	
v	code	
v	comments	
=		-t
g	tokei --languages	\n

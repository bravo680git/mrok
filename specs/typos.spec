@	
o	-c|--config	Custom config file	v
o	--isolated	Ignore implicit configuration files	
o	--diff	Print a diff of what would change	
o	-w|--write-changes	Write fixes out	
o	--files	Debug: Print each file that would be spellchecked	
o	--identifiers	Debug: Print each identifier that would be spellchecked	
o	--words	Debug: Print each word that would be spellchecked	
o	--dump-config	Write the current configuration to file with `-` for stdout	v
o	--type-list	Show all supported file types	
o	--format	Set the output format	v
o	-j|--threads	The approximate number of threads to use	v
o	--exclude	Ignore files & directories matching the glob	v
o	--hidden	Search hidden files and directories	
o	--no-ignore	Don't respect ignore files	
o	--no-ignore-dot	Don't respect .ignore files	
o	--no-ignore-global	Don't respect global ignore files	
o	--no-ignore-parent	Don't respect ignore files in parent directories	
o	--no-ignore-vcs	Don't respect ignore files in vcs directories	
o	--binary	Search binary files	
o	--no-check-filenames	Skip verifying spelling in file names	
o	--no-check-files	Skip verifying spelling in files	
o	--no-unicode	Only allow ASCII characters in identifiers	
o	--locale	Set the locale to use	v
o	--color	Controls when to use color	v
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help information	
o	-V|--version	Print version information	
a	1	1
=		-c
t	filepaths
=		--dump-config
t	filepaths
=		--format
v	silent	
v	brief	
v	long	
v	json	
=		--locale
v	en	
v	en-us	
v	en-gb	
v	en-ca	
v	en-au	
=		--color
v	auto	
v	always	
v	never	
#		1
t	filepaths,folders

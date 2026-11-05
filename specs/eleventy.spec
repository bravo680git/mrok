@	
o	-h|--help	Show help message and exit	
o	-v|--version	Show program's version number and exit	
o	--quiet	Don’t print all written files	
o	--watch	Wait for files to change and automatically rewrite	
o	--dryrun	Don’t write any files	
o	--input	Input template files	v
o	--output	Write HTML output to this folder	v
o	--serve	Run web server on port and watch them too	
o	--port	Run Web Server on specified port	v
o	--formats	Whitelist only certain template types	v
o	--config	Override the eleventy config file path	v
o	--pathprefix	Change all url template filters to use this subdirectory	v
a	1	0
=		--input
t	filepaths
=		--output
t	folders
=		--formats
v	md	
v	html	
v	ejs	
=		--config
t	filepaths
=		--pathprefix
t	folders
#		1
t	folders

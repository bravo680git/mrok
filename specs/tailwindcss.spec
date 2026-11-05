@	
s	init	Creates Tailwind config file. Default: tailwind.config.js
s	build	Build CSS file
o	-i|--input	Specify input file	v
o	-o|--output	Specify output file	v
o	-c|--config	Specify config file to use	v
o	--postcss	Load custom PostCSS configuration	V
o	--purge	Content paths to use for removing unused classes. [Deprecated]: use `--content` instead	
o	--content	Content paths to use for removing unused classes	
o	--watch|-w	Watch for changes and rebuild as needed	
o	--minify|-m	Minify the output	
o	--no-autoprefixer	Disable autoprefixer	
o	--help|-h	Display usage information	
=		-i
t	filepaths
=		-o
t	filepaths
=		-c
t	filepaths
=		--postcss
t	filepaths
@	init
o	-p|--postcss	Initialize a 'postcss.config.js' file	
o	-f|--full	Initialize a full 'tailwind.config.js' file	
o	--help|-h	Display usage information	
a	1	0
@	build
o	-i|--input	Specify input file	v
o	-o|--output	Specify output file	v
o	-c|--config	Specify config file to use	v
o	--postcss	Load custom PostCSS configuration	V
o	--purge	Content paths to use for removing unused classes. [Deprecated]: use `--content` instead	
o	--content	Content paths to use for removing unused classes	
o	--watch|-w	Watch for changes and rebuild as needed	
o	--minify|-m	Minify the output	
o	--no-autoprefixer	Disable autoprefixer	
o	--help|-h	Display usage information	
=	build	-i
t	filepaths
=	build	-o
t	filepaths
=	build	-c
t	filepaths
=	build	--postcss
t	filepaths

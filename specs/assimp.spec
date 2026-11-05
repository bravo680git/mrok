@	
s	listext	List all known file extensions available for import
s	listexport	List all supported export formats
s	knowext	List all known file extensions available for import
s	exportinfo	Show basic information on a specific export format
s	info	Load a model file and print basic statistics. Full postprocessing is applied unless the `-r`…
s	export	Export a file to one of the supported output formats
s	extract	Extract embedded texture images
s	dump	Convert models to a binary or textual dump (ASSBIN/ASSXML)
s	cmpdump	Compare dumps created using 'assimp dump <file> -s ...'
s	version	Display Assimp version
o	-h|--help	Display some basic help	
@	listext
@	listexport
@	knowext
a	1	0
#	knowext	1
d
@	exportinfo
a	1	0
#	exportinfo	1
d
@	info
o	-r|--raw	No postprocessing, do a raw import	
o	-v|--verbose	Print verbose info such as node transform data	
o	-s|--silent	Print only minimal info	
o	-h|--help	Detailed help on a command	
a	1	1
#	info	1
t	filepaths
@	export
o	-f|--format	Export file formats supported by Assimp	v
o	-h|--help	Detailed help on a command	
a	2	0
=	export	-f
d
#	export	1
t	filepaths
#	export	2
t	folders
@	extract
o	-t|--texture	Zero-based index of the texture to be extracted	v
o	-ba|–-bmp-with-alpha	Specifies whether output BMPs contain an alpha channel or not	
o	-f|--format	Specifies the output file format. Supported formats are BMP and TGA. The default value is BMP (if…	v
o	-s|–-nosuffix	Prevents the tool from adding the _img<n> suffix to all filenames. This option must be specified…	
o	-cfast	Fast post processing preset, runs just a few important steps	
o	-cdefault	Default post processing: runs all recommended steps	
o	-cfull	Fires almost all post processing steps	
o	-h|--help	Detailed help on a command	
a	2	0
=	extract	-f
v	bmp	
v	tga	
#	extract	1
t	filepaths
#	extract	2
t	folders
@	dump
o	-b|--binary	If true, the dump is written in binary format	
o	-s|--short	If true, the dump is shortened to include only min/max values for all vertex components and…	
o	-z|--compressed	If true, Compressed	
o	-cfast	Fast post processing preset, runs just a few important steps	
o	-cdefault	Default post processing: runs all recommended steps	
o	-cfull	Fires almost all post processing steps	
o	-h|--help	Detailed help on a command	
a	2	0
#	dump	1
t	filepaths
#	dump	2
t	folders
@	cmpdump
o	-h|--help	Detailed help on a command	
a	2	0
#	cmpdump	1
t	filepaths
#	cmpdump	2
t	filepaths
@	version

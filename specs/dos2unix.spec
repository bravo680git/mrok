@	
o	-h|--help	Show help for dos2unix	
o	--	Treat all following options as file names. Use this option if you want to convert files whose…	
o	--allow-chown	Allow file ownership change in old file mode	
o	-ascii	Convert only line breaks. This is the default conversion mode	
o	-iso	Conversion between DOS and ISO-8859-1 character set	
o	-1252	Use Windows code page 1252 (Western European)	
o	-437	Use DOS code page 437 (US). This is the default code page used for ISO conversion	
o	-850	Use DOS code page 850 (Western European)	
o	-860	Use DOS code page 860 (Portuguese)	
o	-863	Use DOS code page 863 (French Canadian)	
o	-865	Use DOS code page 865 (Nordic)	
o	-7	Convert 8 bit characters to 7 bit space	
o	-b|--keep-bom	Keep Byte Order Mark (BOM). When the input file has a BOM, write a BOM in the output file	
o	-c|--convmode	Set conversion mode	v
o	-D|--display-enc	Set encoding of displayed text	v
o	-f|--force	Force conversion of binary files	
o	-gb|--gb18030	On Windows UTF-16 files are by default converted to UTF-8, regardless of the locale setting	
o	-i	Display file information. No conversion is done	v
o	--info	Display file information. No conversion is done	v=
o	-k|--keepdate		
o	-L|--license	Display program's license	
o	-l|--newline	Add additional newline	
o	-m|--add-bom	Write a Byte Order Mark (BOM) in the output file. By default an UTF-8 BOM is written	
o	--newfile	New file mode. Convert file INFILE and write output to file OUTFILE. File names must be given in…	v
o	--no-allow-chown	Don't allow file ownership change in old file mode (default)	
o	-o|--oldfile	Old file mode. Convert file FILE and overwrite output to it	v
o	-q|--quiet	Quiet mode. Suppress all warnings and messages. The return value is zero. Except when wrong…	
o	-r|--remove-bom	Remove Byte Order Mark (BOM). Do not write a BOM in the output file	
o	-s|--safe	Skip binary files (default)	
o	-u|--keep-utf16	Keep UTF-16 encoding	
o	-ul|--assume-utf16le	Assume that the input format is UTF-16LE	
o	-ub|--assume-utf16be	Assume that the input format is UTF-16BE	
o	-v|--verbose	Verbose operation	
o	-F|--follow-symlink	Follow symbolic links and convert the targets	
o	-R|--replace-symlink	Replace symbolic links with converted files	
o	-S|--skip-symlink	Keep symbolic links and targets unchanged (default)	
o	-V|--version	Display version number	
a	1	1
=		-c
v	ascii	
v	7bit	
v	iso	
v	mac	
=		-D
v	ansi	
v	unicode	
v	unicodebom	
v	utf8	
v	utf8bom	
=		--newfile
t	filepaths
=		-o
t	filepaths
#		1
t	filepaths

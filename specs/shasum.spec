@	
o	-a|--algorithm	Select SHA algorithm	v
o	-b|--binary	Read in binary mode	
o	-c|--check	Read SHA sums from the FILEs and check them	
o	--tag	Create a BSD-style checksum	
o	-t|--text	Read in text mode (default)	
o	-U|--UNIVERSAL	Read in Universal Newlines mode - produces same digest on Windows/Unix/Mac	
o	-0|--01	Read in BITS mode - ASCII '0' as 0-bit, ASCII '1' as 1-bit, others ignored	
o	--ignore-missing	Don't fail or report status for missing files	
o	-q|--quiet	Don't print OK for each successfully verified file	
o	-s|--status	Don't output anything, status code shows success	
o	--strict	Exit non-zero for improperly formatted checksum lines	
o	-w|--warn	Warn about improperly formatted checksum lines	
o	-h|--help	Display help and exit	
o	-v|--version	Output version information and exit	
a	1	1
=		-a
v	1	SHA-1 (default)
v	224	SHA-224
v	256	SHA-256
v	384	SHA-384
v	512	SHA-512
v	512224	SHA-512/224
v	512256	SHA-512/256
#		1
t	filepaths

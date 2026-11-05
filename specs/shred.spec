@	
o	--force|-f	Change permissions to allow writing if necessary	
o	--iterations|-n	Overwrite N times instead of the default (3)	v
o	--random-source	Get random bytes from FILE	v
o	--size|-s	Shred this many bytes (suffixes like K, M, G accepted)	v
o	--remove	Like -u but give control on HOW to delete	v
o	--verbose|-v	Show progress	
o	--exact|-x	Do not round file sizes up to the next full block; this is the default for non-regular files	
o	--zero|-z	Add a final overwrite with zeros to hide shredding	
o	--help	Display this help and exit	
o	--version	Output version information and exit	
a	1	1
=		--iterations
v	3	
v	5	
v	7	
=		--random-source
v	/dev/urandom	
v	/dev/random	
t	filepaths
=		--size
v	1K	
v	1M	
v	1G	
=		--remove
v	unlink	
v	wipe	
v	wipesync	
#		1
t	filepaths

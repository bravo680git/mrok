@	
o	--help	Shows help message	
o	--version	Displays the current version of sort	
o	-c|--check|-C	Check that the single input file is sorted	V
o	-m|--merge	Merge only. The input files are assumed to be pre-sorted. If they are not sorted the output order…	
o	-o|--output	Print the output to the output file instead of the standard output	v
o	-S|--buffer-size	Use size for the maximum size of the memory buffer	v
o	-T|--temporary-directory	Store temporary files in the directory dir	v
o	-u|--unique	Unique keys. Suppress all lines that have a key that is equal to an already processed one	
o	-s	Stable sort. This option maintains the original record order of records that have an equal key	
o	-b|--ignore-leading-blanks	Ignore leading blank characters when comparing lines	
o	-d|--dictionary-order	Consider only blank spaces and alphanumeric characters in comparisons	
o	-f|--ignore-case	Convert all lowercase characters to their upper case equivalent before comparison	
o	-g|--general-numeric-sort	Sort by general numerical value	
o	-h|--human-numeric-sort	Sort by numerical value, but take into account the SI suffix, if present	
o	-i|--ignore-nonprinting	Ignore all non-printable characters	
o	-M|--month-sort	Sort by month abbreviations. Unknown strings are considered smaller than the month names	
o	-n|--numeric-sort	Sort fields numerically by arithmetic value	
o	-R|--random-sort	Sort by a random order	
o	-r|--reverse	Sort in reverse order	
o	-V|--version-sort	Sort version numbers	
o	-k|--key	Define a restricted sort key that has the starting position field1, and optional ending position…	v
o	-t|--field-separator	Use char as a field separator character	v
o	-z|--zero-terminated	Use NUL as record separator	
o	--batch-size	Specify maximum number of files that can be opened by sort at once	v
o	--compress-program	Use PROGRAM to compress temporary files (eg. bzip2)	v
o	--random-source	In random sort, the file content is used as the source of the 'seed' data for the hash function…	v
o	--debug	Print some extra information about the sorting process to the standard output	
o	--parallel	Set the maximum number of execution threads. Default number equals to the number of CPUs	
o	--files0-from	Take the input file list from the file filename	v
o	--radixsort	Try to use radix sort, if the sort specifications allow	
o	--mergesort	Use mergesort. This is a universal algorithm that can always be used, but it is not always the…	
o	--qsort	Try to use quick sort, if the sort specifications allow. This sort algorithm cannot be used with…	
o	--heapsort	Try to use heap sort, if the sort specifications allow. This sort algorithm cannot be used with -u…	
o	--mmap	Try to use file memory mapping system call. It may increase speed in some cases	
o	--sort	Select how to sort values	v
a	1	1
=		-c
v	silent	
v	quiet	
=		-T
t	folders
=		--compress-program
t	filepaths
=		--random-source
t	filepaths
=		--files0-from
t	filepaths
=		--sort
v	general-numeric	
v	human-numeric	
v	month	
v	numeric	
v	random	
#		1
t	filepaths

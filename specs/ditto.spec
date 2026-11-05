@	
o	--help	Show help for ditto	
o	-h	Print full usage	
o	-X	When copying one or more source directories, do not descend into directories that have a different…	
o	-c	Create an archive at the destination path	
o	-z	Create compressed CPIO archives, using gzip(1) compression	
o	-j	Create compressed CPIO archives, using bzip2(1) compression	
o	-v	Print a line of output to stderr for each source directory copied	
o	-V	Print a line of output to stderr for every file, symbolic link, and device copied	
o	-x	Extract the archives given as source arguments	
o	-k	Create or extract from a PKZip archive instead of the default CPIO	
o	--keepParent	When creating an archive, embed the parent directory name src in dst_archive	
o	--arch	Thin Universal binaries to the specified architecture. If multiple --arch options are specified…	v
o	--bom	Copy only files, links, devices, and directories that are present in the specified BOM	v
o	-rsrc	Preserve resource forks and HFS meta-data. ditto will store this data in Carbon-compatible ._…	
o	--norsrc	Do not preserve resource forks and HFS meta-data. If both --norsrc and --rsrc are passed…	
o	--extattr	Preserve extended attributes (requires --rsrc). As of Mac OS X 10.5, --extattr is the default	
o	--noextattr	Do not preserve extended attributes (requires --norsrc)	
o	--qtn	Preserve quarantine information. As of Mac OS X 10.5, --qtn is the default	
o	--noqtn	Do not preserve quarantine information	
o	--acl	Preserve Access Control Lists (ACLs). As of Mac OS X 10.5, --acl is the default	
o	--noacl	Do not preserve ACLs	
o	--nocache	Do not perform copies using the Mac OS X Unified Buffer Cache. Files read and written will not be…	
o	--hfsCompression	When copying files or extracting content from an archive, if the destination is an HFS+ volume…	
o	--nohfsCompression	Do not compress files with HFS+ compression when copying or extracting content from an archive…	
o	--preserveHFSCompression	When copying files to an HFS+ volume that supports compression, ditto will preserve the…	
o	--nopreserveHFSCompression	Do not preserve HFS+ compression when copying files that are already compressed with HFS+…	
o	--sequesterRsrc	When creating a PKZip archive, preserve resource forks and HFS meta-data in the subdirectory…	
o	--zlibCompressionLevel	Sets the compression level to use when creating a PKZip archive. The compression level can be set…	v
o	--password	When extracting a password-encrypted ZIP archive, you must specify --password to allow ditto to…	
a	2	0
#		1
t	filepaths,folders
#		2
t	folders

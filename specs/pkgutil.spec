@	
s	--packages|--pkgs	List all installed package IDs on the specified --volume
s	--pkgs-plist	List all installed package IDs, in Mac OS X plist(5) format, on the specified --volume
s	--files	List all of the files installed under the package-id
s	--export-plist	Print all receipt information about the specified package-id in Mac OS X plist(5) format
s	--verify	Run repair_packages(8) to verify the specified package-id
s	--repair	Run repair_packages(8) to repair the specified package-id
s	--pkg-info	Print extended information about the specified package-id
s	--pkg-info-plist	Print extended information about the specified package-id in Mac OS X plist(5) format
s	--forget	Discard all receipt data about package-id, but don't touch installed files
s	--learn	Update the ACLs of the given path in the receipt identified by --edit-pkg
s	--pkg-groups	List all of the package groups this package-id is a member of
s	--groups	List all of the package groups ont he specified --volume
s	--group-plist	List all of the package groups ont he specified --volume in Mac OS X plist(5) format
s	--group-pkgs	List all of the packages that are members of this group-id
s	--file-info	Show the metadata known about path
s	--file-info-plist	Show the metadata known about path in Mac OS X plist(5) format
s	--expand	Expand the flat package at pkg-path into a new directory specified by dir-path
s	--flatten	Flatten the dir-path into a new flat package created at pkg-path
s	--bom	Extract any BOM files from the flat pkg at path into /tmp and return the filename(s)
s	--payload-files	List the files archived within the uninstalled flat package(s) at path
s	--check-signature	Check the validity and trust of the signature on the package at pkg-path
o	-h|--help	A brief summary of commands and usage	
o	-f|--force	Skip confirmation before a potentially destructive or ambiguous action	
o	-v|--verbose	Output in a human-readable format	
o	--volume	Perform all operations on specified volume	v
o	--edit-pkg	Specifies an existing receipt to be modified in-place by --learn	v
o	--only-files	List only files (not directories) in --files listing	
o	--only-dirs	List only directories (not files) in --files listing	
o	--regexp	Use regex to match package-id arguments, if an exact match isn't found	
o	--pkgs	List all installed package IDs, optionally matching kwarg REGEXP, on the specified --volume	v=
=		--volume
t	folders
=		--edit-pkg
g	pkgutil --pkgs	\n
@	--packages
@	--pkgs-plist
@	--files
a	1	0
#	--files	1
g	pkgutil --pkgs	\n
@	--export-plist
a	1	0
#	--export-plist	1
g	pkgutil --pkgs	\n
@	--verify
a	1	0
#	--verify	1
g	pkgutil --pkgs	\n
@	--repair
a	1	0
#	--repair	1
g	pkgutil --pkgs	\n
@	--pkg-info
a	1	0
#	--pkg-info	1
g	pkgutil --pkgs	\n
@	--pkg-info-plist
a	1	0
#	--pkg-info-plist	1
g	pkgutil --pkgs	\n
@	--forget
a	1	0
#	--forget	1
g	pkgutil --pkgs	\n
@	--learn
a	1	0
#	--learn	1
d
@	--pkg-groups
a	1	0
#	--pkg-groups	1
g	pkgutil --pkgs	\n
@	--groups
@	--group-plist
@	--group-pkgs
a	1	0
#	--group-pkgs	1
g	pkgutil --groups	\n
@	--file-info
a	1	0
#	--file-info	1
t	filepaths
@	--file-info-plist
a	1	0
#	--file-info-plist	1
t	filepaths
@	--expand
a	2	0
#	--expand	1
t	filepaths
#	--expand	2
t	folders
@	--flatten
a	2	0
#	--flatten	1
t	folders
#	--flatten	2
t	filepaths
@	--bom
a	1	0
#	--bom	1
d
@	--payload-files
a	1	0
#	--payload-files	1
d
@	--check-signature
a	1	0
#	--check-signature	1
d

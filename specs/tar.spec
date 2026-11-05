@	
s	A|-A|--catenate|--concatenate	Append archive to the end of another archive
s	c|-c|--create	Create a new archive
s	d|-d|--diff|--compare	Find differences between archive and file system
s	t|-t|--list	List the contents of an archive
s	r|-r|--append	Append files to the end of an archive
s	u|-u|--update	Append files which are newer than the corresponding copy in the archive
s	x|-x|--extract|--get	Extract files from an archive
s	--delete	Delete from the archive
s	--test-label	Test the archive volume label and exit
s	--show-defaults	Show built-in defaults for various tar options and exit
s	?|-?|--help	Display a short option summary and exit
s	--usage	Display a list of available options and exit
s	--version	Print program version and copyright information and exit
o	g|-g|--listed-incremental	Handle new GNU-format incremental backups	vp
o	--hole-detection	Use METHOD to detect holes in sparse files	Vp
o	G|-G|--incremental	Handle old GNU-format incremental backups	p
o	--sparse-version	Set version of the sparse format to use	vp
o	S|-S|--sparse	Handle sparse files efficiently	p
o	--ignore-command-error	Ignore subprocess exit codes	p
o	--no-ignore-command-error	Treat non-zero exit codes of children as error	p
o	--numeric-owner	Always use numbers for user/group names	p
o	--acls	Enable POSIX ACLs support	p
o	--no-acls	Disable POSIX ACLs support	p
o	--selinux	Enable SELinux context support	p
o	--no-selinux	Disable SELinux context support	p
o	--xattrs	Enable extended attributes support	p
o	--no-xattrs	Disable extended attributes support	p
o	--xattrs-exclude	Specify the exclude pattern for xattr keys	vp
o	--xattrs-include	Specify the include pattern for xattr keys	vp
o	--backup	Backup before removal	Vp
o	C|-C|--directory	Change to DIR before performing any operations	vp
o	--newer-mtime	Work on files whose data changed after the DATE	vp
o	--no-null	Disable the effect of the previous --null option	p
o	--no-recursion	Avoid descending automatically in directories	p
o	--no-unquote	Do not unquote input file or member names	p
o	--no-verbatim-files-from	Treat each line read from a file list as if it were supplied in the command line	p
o	-null	Instruct subsequent -T options to read null-terminated names verbatim	p
o	--recursion	Recurse into directories	p
o	--suffix	Backup before removal, override usual suffix	vp
o	T|-T|--files-from	Get names to extract or create from FILE	vp
o	--unquote	Unquote file or member names	p
o	--verbatim-files-from	Treat each line obtained from a file list as a file name, even if it starts with a dash	p
o	X|-X|--exclude-from	Exclude files matching patterns listed in FILE	vp
o	--index-file	Send verbose output to FILE	vp
o	--no-quote-chars	Disable quoting for characters from STRING	vp
o	--quote-chars	Additionally quote characters from STRING	vp
o	--quoting-style	Set quoting style for file and member names	vp
o	R|-R|--block-number	Show block number within archive with each message	p
o	--show-transformed-names|--show-stored-names	Show file or archive names after transformation by --strip and --transform options	p
o	--totals	Print total bytes after processing the archive	Vp
o	v|-v|--verbose	Verbosely list files processed	p
o	w|-w|--interactive|--confirmation	Ask for confirmation for every action	
=		--hole-detection
v	seek	
v	raw	
=		--sparse-version
v	0	
v	0.1	
v	1	
=		--backup
v	none	Never make backups
v	off	Never make backups
v	t	Make numbered backups
v	numbered	Make numbered backups
v	nil	Make numbered backups if numbered backups exist
v	existing	Make numbered backups if numbered backups exist
v	never	Always make simple backups
v	simple	Always make simple backups
=		C
t	folders
=		--newer-mtime
t	filepaths
=		T
t	filepaths
=		X
t	filepaths
=		--quoting-style
v	literal	
v	shell	
v	shell-always	
v	c	
v	c-maybe	
v	escape	
v	locale	
v	clocale	
=		--totals
v	SIGHUP	
v	HUP	
v	SIGQUIT	
v	QUIT	
v	SIGINT	
v	INT	
v	SIGUSR1	
v	USR1	
v	SIGUSR2	
v	USR2	
@	A
a	1	1
#	A	1
t	filepaths
@	c
o	--check-device	Check device numbers when creating incremental archives	
o	--level	Set dump level for created listed-incremental archive	v=
o	--no-check-device	Do not check device numbers when creating incremental archives	
o	--ignore-failed-read	Do not exit with nonzero on unreadable files	
o	--restrict	Disable the use of some potentially harmful options	
o	--remove-files	Remove files from disk after adding them to the archive	
o	W|-W|--verify	Verify the archive after writing it	
o	--atime-preserve	Preserve access times on dumped files	V
o	--group	Force NAME as group for added files	v
o	--group-map	Read group translation map from FILE	v
o	--mode	Force symbolic mode CHANGES for added files	v
o	--mtime	Set mtime for added files	v
o	--owner	Force NAME as owner for added files	v
o	--owner-map	Read owner translation map from FILE	v
o	--sort	When creating an archive, sort directory entries according to ORDER	v
o	--add-file	Add FILE to the archive	v
o	--exclude	Exclude files matching PATTERN	v
o	--exclude-backups	Exclude backup and lock files	
o	--exclude-caches	Exclude contents of directories containing file CACHEDIR.TAG, except for the tag file itself	
o	--exclude-caches-all	Exclude directories containing file CACHEDIR.TAG and the file itself	
o	--exclude-caches-under	Exclude everything under directories containing CACHEDIR.TAG	
o	--exclude-ignore	Read exclusion patterns from FILE in directory before dumping	v
o	--exclude-ignore-recursive	Same as --exclude-ignore, except that patterns from FILE affect both the directory and all its…	v
o	--exclude-tag	Exclude contents of directories containing FILE, except for FILE itself	v
o	--exclude-tag-all	Exclude directories containing FILE	v
o	--exclude-tag-under	Exclude everything under directories containing FILE	v
o	--exclude-vcs	Exclude version control system directories	
o	--exclude-vcs-ignores	Exclude files that match patterns read from VCS-specific ignore files	
o	h|-h|--dereference	Follow symlinks; archive and dump the files they point to	
o	--hard-dereference	Follow hard links; archive and dump the files they refer to	
o	N|-N|--newer|--after-date	Only store files newer than DATE	v
o	--one-file-system	Stay in local file system when creating archive	
o	P|-P|--absolute-names	Don't strip leading slashes from file names	
o	--anchored	Patterns match file name start	
o	--ignore-case	Ignore case	
o	--no-anchored	Patterns match after any /	
o	--no-ignore-case	Case sensitive matching	
o	--no-wildcards	Verbatim string matching	
o	--no-wildcards-match-slash	Wildcards do not match /	
o	--wildcards	Use wildcards	
o	--wildcards-match-slash	Wildcards match /	
o	--clamp-mtime	Only set time when the file is more recent than what was given with --mtime	
o	l|-l|--check-links	Print a message if not all links are dumped	
o	a|-a|--auto-compress	Use archive suffix to determine the compression program	
o	I|-I|--use-compress-program	Filter data through COMMAND	v
o	j|-j|--bzip2	Filter the archive through bzip2	
o	J|-J|--xz	Filter the archive through xz	
o	--lzip	Filter the archive through lzip	
o	--lzma	Filter the archive through lzma	
o	--lzop	Filter the archive through lzop	
o	--no-auto-compress	Do not use archive suffix to determine the compression program	
o	z|-z|--gzip|--gunzip|--ungzip	Filter the archive through gzip	
o	Z|-Z|--compress|--uncompress	Filter the archive through compress	
o	--zstd	Filter the archive through zstd	
o	--transform|--xform	Use sed replace EXPRESSION to transform file names	v
o	--checkpoint	Display progress messages every Nth record	V
o	--checkpoint-action	Run ACTION on each checkpoint	v
o	--full-time	Print file time to its full resolution	
o	--utc	Print file modification times in UTC	
o	b|-b|--blocking-factor	Set record size to BLOCKSx512 bytes	v
o	--record-size	Set record size	v
o	H|-H|--format	Create archive of the given format	v
o	--old-archive|--portability	Same as --format=v7	
o	--pax-option	Control pax keywords when creating PAX archives	v
o	--posix	Same as --format=posix	
o	V|-V|--label	Create archive with volume name TEXT	v
o	--warning	Enable or disable warning messages identified by KEYWORD	vp
o	o|-o	Same as --old-archive	
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
a	1	1
=	c	--atime-preserve
v	replace	Restore the times after reading
v	system	Not setting the times in the first place
=	c	--group-map
t	filepaths
=	c	--mtime
t	filepaths
=	c	--owner-map
t	filepaths
=	c	--sort
v	none	
v	name	
v	inode	
=	c	--add-file
t	filepaths
=	c	N
t	filepaths
=	c	--record-size
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
=	c	H
v	gnu	GNU tar 1.13.x format
v	oldgnu	GNU format as per tar <= 1.12
v	pax	POSIX 1003.1-2001 (pax) format
v	posix	POSIX 1003.1-2001 (pax) format
v	ustar	POSIX 1003.1-1988 (ustar) format
v	v7	Old V7 tar format
=	c	--warning
v	all	Enable all warning messages
v	none	Disable all warning messages
v	filename-with-nuls	"%s: file name read contains nul character"
v	no-filename-with-nuls	No "%s: file name read contains nul character"
v	alone-zero-block	"A lone zero block at %s"
v	no-alone-zero-block	No "A lone zero block at %s"
v	cachedir	"%s: contains a cache directory tag %s; %s"
v	no-cachedir	No "%s: contains a cache directory tag %s; %s"
v	file-shrank	"%s: File shrank by %s bytes; padding with zeros"
v	no-file-shrank	No "%s: File shrank by %s bytes; padding with zeros"
v	xdev	"%s: file is on a different filesystem; not dumped"
v	no-xdev	No "%s: file is on a different filesystem; not dumped"
v	file-ignored	"%s: Unknown file type; file ignored", "%s: socket ignored", "%s: door ignored"
v	no-file-ignored	No "%s: Unknown file type; file ignored", "%s: socket ignored", "%s: door ignored"
v	file-unchanged	"%s: file is unchanged; not dumped"
v	no-file-unchanged	No "%s: file is unchanged; not dumped"
v	ignore-archive	"%s: file is the archive; not dumped"
v	no-ignore-archive	No "%s: file is the archive; not dumped"
v	file-removed	"%s: File removed before we read it"
v	no-file-removed	No "%s: File removed before we read it"
v	file-changed	"%s: file changed as we read it"
v	no-file-changed	No "%s: file changed as we read it"
v	failed-read	Enables warnings about unreadable files or directories
v	no-failed-read	Suppresses warnings about unreadable files or directories
=	c	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
#	c	1
t	filepaths
@	d
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
o	--occurrence	Process only the Nth occurrence of each file in the archive	V
a	1	1
=	d	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
#	d	1
t	filepaths
@	t
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
o	n|-n|--seek	Assume the archive is seekable	
o	--no-seek	Assume the archive is not seekable	
o	--occurrence	Process only the Nth occurrence of each file in the archive	V
o	B|-B|--read-full-records	When listing or extracting, accept incomplete input records after end-of-file marker	
o	i|-i|--ignore-zeros	Ignore zeroed blocks in archive	
o	V|-V|--label	Use TEXT as a globbing pattern for volume name	v
o	a|-a|--auto-compress	Use archive suffix to determine the compression program	
o	I|-I|--use-compress-program	Filter data through COMMAND	v
o	j|-j|--bzip2	Filter the archive through bzip2	
o	J|-J|--xz	Filter the archive through xz	
o	--lzip	Filter the archive through lzip	
o	--lzma	Filter the archive through lzma	
o	--lzop	Filter the archive through lzop	
o	--no-auto-compress	Do not use archive suffix to determine the compression program	
o	z|-z|--gzip|--gunzip|--ungzip	Filter the archive through gzip	
o	Z|-Z|--compress|--uncompress	Filter the archive through compress	
o	--zstd	Filter the archive through zstd	
o	--transform|--xform	Use sed replace EXPRESSION to transform file names	v
o	--checkpoint	Display progress messages every Nth record	V
o	--checkpoint-action	Run ACTION on each checkpoint	v
o	--full-time	Print file time to its full resolution	
o	--utc	Print file modification times in UTC	
o	K|-K|--starting-file	Begin at the given member in the archive	v
o	--show-omitted-dirs	List each directory that does not match search criteria	
a	1	1
=	t	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
@	r
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
o	--ignore-failed-read	Do not exit with nonzero on unreadable files	
o	--restrict	Disable the use of some potentially harmful options	
o	--remove-files	Remove files from disk after adding them to the archive	
o	W|-W|--verify	Verify the archive after writing it	
o	--atime-preserve	Preserve access times on dumped files	V
o	--group	Force NAME as group for added files	v
o	--group-map	Read group translation map from FILE	v
o	--mode	Force symbolic mode CHANGES for added files	v
o	--mtime	Set mtime for added files	v
o	--owner	Force NAME as owner for added files	v
o	--owner-map	Read owner translation map from FILE	v
o	--sort	When creating an archive, sort directory entries according to ORDER	v
o	--add-file	Add FILE to the archive	v
o	--exclude	Exclude files matching PATTERN	v
o	--exclude-backups	Exclude backup and lock files	
o	--exclude-caches	Exclude contents of directories containing file CACHEDIR.TAG, except for the tag file itself	
o	--exclude-caches-all	Exclude directories containing file CACHEDIR.TAG and the file itself	
o	--exclude-caches-under	Exclude everything under directories containing CACHEDIR.TAG	
o	--exclude-ignore	Read exclusion patterns from FILE in directory before dumping	v
o	--exclude-ignore-recursive	Same as --exclude-ignore, except that patterns from FILE affect both the directory and all its…	v
o	--exclude-tag	Exclude contents of directories containing FILE, except for FILE itself	v
o	--exclude-tag-all	Exclude directories containing FILE	v
o	--exclude-tag-under	Exclude everything under directories containing FILE	v
o	--exclude-vcs	Exclude version control system directories	
o	--exclude-vcs-ignores	Exclude files that match patterns read from VCS-specific ignore files	
o	h|-h|--dereference	Follow symlinks; archive and dump the files they point to	
o	--hard-dereference	Follow hard links; archive and dump the files they refer to	
o	N|-N|--newer|--after-date	Only store files newer than DATE	v
o	--one-file-system	Stay in local file system when creating archive	
o	P|-P|--absolute-names	Don't strip leading slashes from file names	
o	--anchored	Patterns match file name start	
o	--ignore-case	Ignore case	
o	--no-anchored	Patterns match after any /	
o	--no-ignore-case	Case sensitive matching	
o	--no-wildcards	Verbatim string matching	
o	--no-wildcards-match-slash	Wildcards do not match /	
o	--wildcards	Use wildcards	
o	--wildcards-match-slash	Wildcards match /	
o	--clamp-mtime	Only set time when the file is more recent than what was given with --mtime	
o	l|-l|--check-links	Print a message if not all links are dumped	
o	a|-a|--auto-compress	Use archive suffix to determine the compression program	
o	I|-I|--use-compress-program	Filter data through COMMAND	v
o	j|-j|--bzip2	Filter the archive through bzip2	
o	J|-J|--xz	Filter the archive through xz	
o	--lzip	Filter the archive through lzip	
o	--lzma	Filter the archive through lzma	
o	--lzop	Filter the archive through lzop	
o	--no-auto-compress	Do not use archive suffix to determine the compression program	
o	z|-z|--gzip|--gunzip|--ungzip	Filter the archive through gzip	
o	Z|-Z|--compress|--uncompress	Filter the archive through compress	
o	--zstd	Filter the archive through zstd	
o	--transform|--xform	Use sed replace EXPRESSION to transform file names	v
o	--checkpoint	Display progress messages every Nth record	V
o	--checkpoint-action	Run ACTION on each checkpoint	v
o	--full-time	Print file time to its full resolution	
o	--utc	Print file modification times in UTC	
a	1	1
=	r	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
=	r	--atime-preserve
v	replace	Restore the times after reading
v	system	Not setting the times in the first place
=	r	--group-map
t	filepaths
=	r	--mtime
t	filepaths
=	r	--owner-map
t	filepaths
=	r	--sort
v	none	
v	name	
v	inode	
=	r	--add-file
t	filepaths
=	r	N
t	filepaths
#	r	1
t	filepaths
@	u
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
o	--ignore-failed-read	Do not exit with nonzero on unreadable files	
o	--restrict	Disable the use of some potentially harmful options	
o	--remove-files	Remove files from disk after adding them to the archive	
o	W|-W|--verify	Verify the archive after writing it	
o	--atime-preserve	Preserve access times on dumped files	V
o	--group	Force NAME as group for added files	v
o	--group-map	Read group translation map from FILE	v
o	--mode	Force symbolic mode CHANGES for added files	v
o	--mtime	Set mtime for added files	v
o	--owner	Force NAME as owner for added files	v
o	--owner-map	Read owner translation map from FILE	v
o	--sort	When creating an archive, sort directory entries according to ORDER	v
o	--add-file	Add FILE to the archive	v
o	--exclude	Exclude files matching PATTERN	v
o	--exclude-backups	Exclude backup and lock files	
o	--exclude-caches	Exclude contents of directories containing file CACHEDIR.TAG, except for the tag file itself	
o	--exclude-caches-all	Exclude directories containing file CACHEDIR.TAG and the file itself	
o	--exclude-caches-under	Exclude everything under directories containing CACHEDIR.TAG	
o	--exclude-ignore	Read exclusion patterns from FILE in directory before dumping	v
o	--exclude-ignore-recursive	Same as --exclude-ignore, except that patterns from FILE affect both the directory and all its…	v
o	--exclude-tag	Exclude contents of directories containing FILE, except for FILE itself	v
o	--exclude-tag-all	Exclude directories containing FILE	v
o	--exclude-tag-under	Exclude everything under directories containing FILE	v
o	--exclude-vcs	Exclude version control system directories	
o	--exclude-vcs-ignores	Exclude files that match patterns read from VCS-specific ignore files	
o	h|-h|--dereference	Follow symlinks; archive and dump the files they point to	
o	--hard-dereference	Follow hard links; archive and dump the files they refer to	
o	N|-N|--newer|--after-date	Only store files newer than DATE	v
o	--one-file-system	Stay in local file system when creating archive	
o	P|-P|--absolute-names	Don't strip leading slashes from file names	
o	--anchored	Patterns match file name start	
o	--ignore-case	Ignore case	
o	--no-anchored	Patterns match after any /	
o	--no-ignore-case	Case sensitive matching	
o	--no-wildcards	Verbatim string matching	
o	--no-wildcards-match-slash	Wildcards do not match /	
o	--wildcards	Use wildcards	
o	--wildcards-match-slash	Wildcards match /	
o	--clamp-mtime	Only set time when the file is more recent than what was given with --mtime	
o	l|-l|--check-links	Print a message if not all links are dumped	
o	a|-a|--auto-compress	Use archive suffix to determine the compression program	
o	I|-I|--use-compress-program	Filter data through COMMAND	v
o	j|-j|--bzip2	Filter the archive through bzip2	
o	J|-J|--xz	Filter the archive through xz	
o	--lzip	Filter the archive through lzip	
o	--lzma	Filter the archive through lzma	
o	--lzop	Filter the archive through lzop	
o	--no-auto-compress	Do not use archive suffix to determine the compression program	
o	z|-z|--gzip|--gunzip|--ungzip	Filter the archive through gzip	
o	Z|-Z|--compress|--uncompress	Filter the archive through compress	
o	--zstd	Filter the archive through zstd	
o	--transform|--xform	Use sed replace EXPRESSION to transform file names	v
o	--checkpoint	Display progress messages every Nth record	V
o	--checkpoint-action	Run ACTION on each checkpoint	v
o	--full-time	Print file time to its full resolution	
o	--utc	Print file modification times in UTC	
a	1	1
=	u	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
=	u	--atime-preserve
v	replace	Restore the times after reading
v	system	Not setting the times in the first place
=	u	--group-map
t	filepaths
=	u	--mtime
t	filepaths
=	u	--owner-map
t	filepaths
=	u	--sort
v	none	
v	name	
v	inode	
=	u	--add-file
t	filepaths
=	u	N
t	filepaths
#	u	1
t	filepaths
@	x
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
o	n|-n|--seek	Assume the archive is seekable	
o	--no-seek	Assume the archive is not seekable	
o	--occurrence	Process only the Nth occurrence of each file in the archive	V
o	B|-B|--read-full-records	When listing or extracting, accept incomplete input records after end-of-file marker	
o	i|-i|--ignore-zeros	Ignore zeroed blocks in archive	
o	V|-V|--label	Use TEXT as a globbing pattern for volume name	v
o	a|-a|--auto-compress	Use archive suffix to determine the compression program	
o	I|-I|--use-compress-program	Filter data through COMMAND	v
o	j|-j|--bzip2	Filter the archive through bzip2	
o	J|-J|--xz	Filter the archive through xz	
o	--lzip	Filter the archive through lzip	
o	--lzma	Filter the archive through lzma	
o	--lzop	Filter the archive through lzop	
o	--no-auto-compress	Do not use archive suffix to determine the compression program	
o	z|-z|--gzip|--gunzip|--ungzip	Filter the archive through gzip	
o	Z|-Z|--compress|--uncompress	Filter the archive through compress	
o	--zstd	Filter the archive through zstd	
o	--transform|--xform	Use sed replace EXPRESSION to transform file names	v
o	--checkpoint	Display progress messages every Nth record	V
o	--checkpoint-action	Run ACTION on each checkpoint	v
o	--full-time	Print file time to its full resolution	
o	--utc	Print file modification times in UTC	
o	K|-K|--starting-file	Begin at the given member in the archive	v
o	--show-omitted-dirs	List each directory that does not match search criteria	
o	k|-k|--keep-old-files	Don't replace existing files when extracting	
o	--keep-newer-files	Don't replace existing files that are newer than their archive copies	
o	--keep-directory-symlink	Don't replace existing symlinks to directories when extracting	
o	--no-overwrite-dir	Preserve metadata of existing directories	
o	--one-top-level	Extract all files into DIR	v
o	--overwrite	Overwrite existing files when extracting	
o	--overwrite-dir	Overwrite metadata of existing directories when extracting	
o	--recursive-unlink	Recursively remove all files in the directory prior to extracting it	
o	--skip-old-files	Don't replace existing files when extracting, silently skip over them	
o	U|-U|--unlink-first	Remove each file prior to extracting over it	
o	O|-O|--to-stdout	Extract files to standard output	
o	--to-command	Pipe extracted files to COMMAND	v
o	--delay-directory-restore	Delay setting modification times and permissions of extracted directories until the end of…	
o	m|-m|--touch	Don't extract file modified time	
o	--no-delay-directory-restore	Cancel the effect of the prior --delay-directory-restore option	
o	--no-same-owner	Extract files as yourself	
o	--no-same-permissions	Apply the user's umask when extracting permissions from the archive	
o	p|-p|--preserve-permissions|--same-permissions	Extract information about file permissions	
o	--preserve	Same as both -p and -s	
o	--same-owner	Try extracting files with the same ownership as exists in the archive	
o	s|-s|--preserve-order|--same-order	Sort names to extract to match archive	
o	--strip-components	Strip NUMBER leading components from file names on extraction	v
o	--warning	Enable or disable warning messages identified by KEYWORD	vp
o	o|-o	Same as --no-same-owner	
a	1	1
=	x	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
=	x	--to-command
t	filepaths
=	x	--warning
v	all	Enable all warning messages
v	none	Disable all warning messages
v	filename-with-nuls	"%s: file name read contains nul character"
v	no-filename-with-nuls	No "%s: file name read contains nul character"
v	alone-zero-block	"A lone zero block at %s"
v	no-alone-zero-block	No "A lone zero block at %s"
v	existing-file	"%s: skipping existing file"
v	no-existing-file	No "%s: skipping existing file"
v	timestamp	"%s: implausibly old time stamp %s", "%s: time stamp %s is %s s in the future"
v	no-timestamp	No "%s: implausibly old time stamp %s", "%s: time stamp %s is %s s in the future"
v	contiguous-cast	"Extracting contiguous files as regular files"
v	no-contiguous-cast	No "Extracting contiguous files as regular files"
v	symlink-cast	"Attempting extraction of symbolic links as hard links"
v	no-symlink-cast	No "Attempting extraction of symbolic links as hard links"
v	unknown-cast	"%s: Unknown file type '%c', extracted as normal file"
v	no-unknown-cast	No "%s: Unknown file type '%c', extracted as normal file"
v	ignore-newer	"Current %s is newer or same age"
v	no-ignore-newer	No "Current %s is newer or same age"
v	unknown-keyword	"Ignoring unknown extended header keyword '%s'"
v	no-unknown-keyword	No "Ignoring unknown extended header keyword '%s'"
v	decompress-program	Enables verbose description of failures occurring when trying to run alternative decompressor…
v	no-decompress-program	Suppresses verbose description of failures occurring when trying to run alternative decompressor…
v	record-size	"Record size = %lu blocks"
v	no-record-size	No "Record size = %lu blocks"
v	rename-directory	"%s: Directory has been renamed from %s", "%s: Directory has been renamed"
v	no-rename-directory	No "%s: Directory has been renamed from %s", "%s: Directory has been renamed"
v	new-directory	"%s: Directory is new"
v	no-new-directory	No "%s: Directory is new"
v	xdev	"%s: directory is on a different device: not purging"
v	no-xdev	No "%s: directory is on a different device: not purging"
v	bad-dumpdir	"Malformed dumpdir: 'X' never used"
@	--delete
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
o	--occurrence	Process only the Nth occurrence of each file in the archive	V
a	1	1
=	--delete	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
@	--test-label
o	f|-f|--file	Use archive file or device ARCHIVE	v
o	--force-local	Archive file is local even if it has a colon	
o	F|-F|--info-script|--new-volume-script	Run COMMAND at the end of each tape	v
o	L|-L|--tape-length	Change tape after writing Nx1024 bytes	v
o	M|-M|--multi-volume	Create/list/extract multi-volume archive	
o	--rmt-command	Use COMMAND instead of rmt when accessing remote archives	v
o	--rsh-command	Use COMMAND instead of rsh when accessing remote archives	v
o	--volno-file	Tar will keep track of which volume of a multi-volume archive it is working in FILE	v
a	1	1
=	--test-label	L
v	Blocks	
v	Bytes	
v	Gigabytes	
v	Kilobytes	
v	Megabytes	
v	Petabytes	
v	Terabytes	
v	Words	
@	--show-defaults
@	?
@	--usage
@	--version

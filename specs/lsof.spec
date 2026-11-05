@	
o	-?|-h|--help	Help	
o	-a	Apply AND to the selections (defaults to OR)	
o	-b	Avoid kernel blocks	
o	-c	Select the listing of files for processes executing a command	v
o	+c	COMMAND width (9)	v
o	+d	Search for all open instances/files/directories of directory	v
o	-d	Specify a list of file descriptors (FDs) to exclude from or include in the output listing	v
o	+D	Search tree for all open instances/files/directories of directory. *SLOW?*	v
o	+f	Enable path name arguments to be interpreted	V
o	-f	Inhibit path name arguments to be interpreted	v
o	-F	Select fields to output	v
o	-F?	Show fields for -F	
o	-g	Exclude or select by process group IDs (PGID)	v
o	-i	Selects files by [46][protocol][@hostname|hostaddr][:service|port]	v
o	-l	Inhibit conversion of user IDs to login names	
o	+L	Enable listing of file link counts	V
o	-L	Disable listing of file link counts	V
o	+M	Enable portMap registration	
o	-M	Disable portMap registration	
o	-n	No host names	
o	-N	Select NFS files	
o	-o	List file offset	
o	-O	No overhead *RISKY*	
o	-p	Exclude or select process identification numbers (PIDs)	v
o	-P	No port names	
o	+r	Repeat every t seconds (15) until no files	v
o	-r	Repeat every t seconds (15) forever	v
o	-R	List parent PID	
o	-s	List file size or exclude/select protocol	V
o	-S	Stat timeout in seconds (lstat/readlink/stat)	V
o	-T	Disable TCP/TPI info	v
o	-t	Specify terse listing	
o	-u	Exclude/select login|UID set	v
o	-U	Select Unix socket	
o	-v	List version info	
o	-V	Verbose search	
o	+w	Enable warnings	
o	-w	Disable warnings	
o	-x	Cross over +d|+D File systems or symbolic links	v
o	-X	File descriptor table only	
a	1	1
=		+d
t	folders
=		+D
t	folders
=		+f
v	c	File structure use count
v	g	File flag abbreviations
v	G	File flags in hexadecimal
=		-f
v	c	File structure use count
v	g	File flag abbreviations
v	G	File flags in hexadecimal
=		-F
v	a	Access: r = read; w = write; u = read/write
v	c	Command name
v	C	File struct share count
v	d	Device character code
v	D	Major/minor device number as 0x<hex>
v	f	File descriptor (always selected)
v	G	File flaGs
v	i	Inode number
v	k	Link count
v	K	Task ID (TID)
v	l	Lock: r/R = read; w/W = write; u = read/write
v	L	Login name
v	m	Marker between repeated output
v	M	Task comMand name
v	n	Comment, name, Internet addresses
v	o	File offset as 0t<dec> or 0x<hex>
v	p	Process ID (PID)
v	g	Process group ID (PGID)
v	P	Protocol name
v	r	Raw device number as 0x<hex>
v	R	PaRent PID
v	s	File size
v	S	Stream module and device names
v	t	File type
v	T	TCP/TPI info
v	u	User ID (UID)
v	0	(zero) use NUL field terminator instead of N
=		-i
d
=		-T
v	f	Selects reporting of socket options/states/values and tcp flag values
v	q	Selects queue length reporting
v	s	Selects connection state reporting
v	w	Selects window size reporting
=		-x
v	f	File system mount point cross-over processing
v	l	Symbolic link cross-over processing
#		1
t	folders

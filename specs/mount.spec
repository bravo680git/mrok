@	
o	-h|--help	Help for abc	
o	-a|--all	Mount all filesystems in fstab	
o	-c|--no-canonicalize	Don't canonicalize paths	
o	-f|--fake	Dry run; skip the mount(2) syscall	
o	-F|--fork	Fork off for each device (use with -a)	
o	-T|--fstab	Alternative file to /etc/fstab	v
o	-i|--internal-only	Don't call the mount.<type> helpers	
o	-l|--show-labels	Show also filesystem labels	
o	-m|--mkdir	Alias to '-o X-mount.mkdir	
o	-n|--no-mtab	Don't write to /etc/mtab	
o	--options-mode	What to do with options loaded from fstab	v
o	--options-source	Mount options source	v
o	--options-source-force	Force use of options from fstab/mtab	
o	-o|--options	Comma-separated list of mount options	v
o	-O|--test-opts	Limit the set of filesystems (use with -a)	v
o	-r|--read-only	Mount the filesystem read-only (same as -o ro)	
o	-t|--types	Limit the set of filesystem types	v
o	--source	Explicitly specifies source	v
o	--target	Explicitly specifies mountpoint	v
o	--target-prefix	Specifies path used for all mountpoints	v
o	-v|--verbose	Say what is being done	
o	-w|--rw|--read-write	Mount the filesystem read-write (default)	
o	-V|--version	Display version	
o	-B|--bind	Mount a subtree somewhere else (same as -o bind)	
o	-M|--move	Move a subtree to some other place	
o	-R|-rbind	Mount a subtree and all submounts somewhere else	
o	--make-shared	Mark a subtree as shared	
o	--make-slave	Mark a subtree as slave	
o	--make-private	Mark a subtree as private	
o	--make-unbindable	Mark a subtree as unbindable	
o	--make-rshared	Recursively mark a whole subtree as shared	
o	--make-rslave	Recursively mark a whole subtree as slave	
o	--make-rprivate	Recursively mark a whole subtree as private	
o	--make-runbindable	Recursively mark a whole subtree as unbindable	
a	2	0
=		-T
t	filepaths
=		--options-source
t	filepaths
=		--source
v	path	
v	label	
v	uuid	
=		--target
t	folders
=		--target-prefix
t	folders
#		1
t	filepaths
d
#		2
v	/mnt	
v	/run/media/	
t	folders

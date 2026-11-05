@	
o	--help|-h	Show help for fdisk	
o	--version|-V	Show version for lsblk	
o	--sector-size|-b	Specify the sector size of the disk	v
o	--protect-boot|-B	Don't erase the beginning of the first disk sector when creating a new disk label	
o	--compatibility|-c	Specify the compatibility mode, 'dos' or 'nondos'	V
o	--color|-L	Colorize the output	V
o	--list|-l	List the partition tables for the specified devices and then exit	
o	--list-details|-x	Like --list, but provides more details	
o	--lock	Use exclusive BSD lock for device or file it operates	V
o	--noauto-pt|-n	Don't automatically create a default partition table on empty device	
o	--output|-o	Desc	v
o	--getsz|-s	Print the size in 512-byte sectors of each given block device. This option is DEPRECATED in favour…	
o	--type|-t	Enable support only for disklabels of the specified type, and disable support for all other types	v
o	--units|-u	When listing partition tables, show sizes in 'sectors' or in 'cylinders'	V
o	--cylinders|-C	Specify the number of cylinders of the disk	v
o	--heads|-H	Specify the number of heads of the disk. (Not the physical number, of course, but the number used…	v
o	--sectors|-S	Specify the number of sectors per track of the disk. (Not the physical number, of course, but the…	
o	--wipe|-w	Wipe filesystem, RAID and partition-table signatures from the device, in order to avoid possible…	v
o	--wipe-partitions|-W	Wipe filesystem, RAID and partition-table signatures from a newly created partitions, in order to…	v
a	1	0
=		--sector-size
v	512	
v	1024	
v	2048	
v	4096	
=		--compatibility
v	dos	
v	nondos	
=		--color
v	always	
v	never	
v	auto	
=		--lock
v	yes	
v	no	
v	nonblock	
=		--units
v	sectors	
v	cylinders	
=		--wipe
v	auto	
v	never	
v	always	
#		1
t	filepaths

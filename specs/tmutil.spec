@	
s	version	Print the current version
s	enable	Turn on automatic backups (required root + full disk access)
s	disable	Turn off automatic backups (required root + full disk access)
s	startbackup	Begin a backup if one is not already running
s	stopbackup	Cancel a backup currently in progress
s	delete	Deletes backups with the specified timestamp from the backup volume mounted at the given mountpoint
s	deleteinprogress	Delete all in-progress backups for a machine directory
s	restore	Restore the item `source`, which is inside a backup, to the location `destination`. Same semantics…
s	compare	Perform a backup diff
s	setdestination	Configure a local HFS+ or APFS volume, AFP share, or SMB share as a backup destination (requires…
s	removedestination	Remove the destination with the specified unique identifier from the Time Machine configuration…
s	destinationinfo	Print information about destinations currently configured for use with Time Machine
s	addexclusion	Configure an exclusion that tells Time Machine not to backup a file, directory, or volume during…
s	removeexclusion	Configure Time Machine to backup a file, directory, or volume during future backups
s	isexcluded	Determine if a file, directory, or volume are excluded from Time Machine backups
s	inheritbackup	Claim a machine directory or sparsebundle for use by the current machine
s	associatedisk	Bind a volume store directory to the specified local disk, thereby reconfiguring the backup…
s	latestbackup	List this computer's latest completed backup
s	listbackups	List all of this computer's completed backups
s	machinedirectory	Print the path to the current machine directory for this computer
s	calculatedrift	Analyze the backups in an HFS machine directory and determine the amount of change between each
s	uniquesize	Analyze the specified path in an HFS+ backup or path to an APFS backup and determine its unique size
s	verifychecksums	Compute a checksum of data contained within a backup and verify the results against checksum…
s	localsnapshot	Create new local Time Machine snapshots of all APFS volumes included in the Time Machine backup
s	listlocalsnapshots	List local Time Machine snapshots of the specified volume
s	listlocalsnapshotdates	List the creation dates of all local Time Machine snapshots
s	deletelocalsnapshots	Delete all local Time Machine snapshots on all mounted disks for the specified date or on the…
s	thinlocalsnapshots	Think local Time Machine snapshots for the specified volume
@	version
@	enable
@	disable
@	startbackup
o	-a|--auto	Run the backup in a mode similar to system-scheduled backups	
o	-b|--block	Wait (block) until the backup is finished before exiting	
o	-r|--rotation	Allow automatic destination rotation during backup	
o	-d|--destination	Perform the backup to the destination corresponding to the specified ID	v
@	stopbackup
@	delete
o	-d	Delete from the given mount point	v
o	-t	Delete backups with this timestamp	v
o	-p	A specific path to delete (HFS backup disk)	v
=	delete	-p
t	filepaths,folders
@	deleteinprogress
a	1	0
@	restore
o	-v	Be verbose, showing files as they are copied	
a	2	0
@	compare
o	-@	Compare extended attributes	
o	-a	Compare all supported metadata	
o	-c	Compare creation times	
o	-d	Compare file data forks	
o	-e	Compare ACLs	
o	-f	Compare file flags	
o	-g	Compare GIDs	
o	-h	Unknown	
o	-l	Unknown	
o	-m	Compare file modes	
o	-n	No metadata comparison	
o	-s	Compare sizes	
o	-t	Compare modification times	
o	-u	Compare UIDs	
o	-E	Don't take exclusions into account when comparing items inside volumes	
o	-U	Ignore logical volume identity (volume UUIDs) when directly comparing a local volume or volume…	
o	-X	Print output in XML property list format	
o	-D	Limit traversal depth to depth levels from the beginning of iteration	v
o	-I	Ignore paths with a path component equal to name during iteration	v
a	2	0
@	setdestination
o	-a	Add the arg to the list of destinations, instead of replacing the list	
o	-p	Enter a password in a non-echoing interactive prompt	
a	1	0
@	removedestination
a	1	0
@	destinationinfo
o	-X	Print output in XML plist format	
@	addexclusion
o	-p	Configure fixed-path exclusions	
o	-v	Configure volume exclusions	
a	1	1
@	removeexclusion
o	-p	Configure fixed-path exclusions	
o	-v	Configure volume exclusions	
a	1	1
@	isexcluded
a	1	1
@	inheritbackup
a	1	0
@	associatedisk
o	-a	Find all volume stores in the same machine directory that match the identity of the volume backup…	
a	2	0
@	latestbackup
o	-d	Specify a destination volume to list backups from	
o	-m	Attempt to mount the backups and list their mounted paths	
o	-t	Only show the backup timestampt rather than the full name or path	
@	listbackups
o	-d	Specify a destination volume to list backups from	
o	-m	Attempt to mount the backups and list their mounted paths	
o	-t	Only show the backup timestampt rather than the full name or path	
@	machinedirectory
@	calculatedrift
a	1	0
@	uniquesize
a	1	1
#	uniquesize	1
t	filepaths
@	verifychecksums
a	1	1
#	verifychecksums	1
t	filepaths
@	localsnapshot
@	listlocalsnapshots
a	1	0
@	listlocalsnapshotdates
a	1	0
@	deletelocalsnapshots
a	1	0
@	thinlocalsnapshots
a	3	0
#	thinlocalsnapshots	3
v	1	
v	2	
v	3	
v	4	

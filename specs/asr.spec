@	
s	help	Displays asr usage information
s	version	Displays asr version
s	restore	Restores a disk image or volume to another volume
s	restoreexact	Same as restore verb, except that for an HFS Plus volume, the target partition is resized to match…
s	server	Multicasts source over the network
s	imagescan	Calculate checksums of the data in the provided image and store them in the image
s	info	Report the image metadata which was placed in the image by a previous use of the imagescan verb
o	--buffers	One of the options that control how asr uses memory	v
o	--buffersize	One of the options that control how asr uses memory	v
o	--csumbuffers	One of the options that control how asr uses memory	v
o	--csumbuffersize	One of the options that control how asr uses memory	v
o	--verbose	Enables verbose progress and error messages	
o	--debug	Enables other progress and error messages	
@	help
@	version
@	restore
o	--source	Can be a disk image, /dev entry, or volume mountpoint	v
o	--target	Can be a /dev entry, or volume mountpoint	v
o	--file	When performing a multicast restore, --file can be specified instead of --target	v
o	--erase	Erases target and is required. --erase must always be used, as file copies are no longer supported…	
o	--format	Specifies the destination filesystem format	V
o	--noprompt	Suppresses the prompt which usually occurs before target	
o	--timeout	Specifies num seconds that a multicast client should wait when no payload data has been received…	V
o	--puppetstrings	Provide progress output that is easy for another program to parse	
o	--noverify	Skips the verification steps normally taken to ensure that a volume has been properly restored	
o	--allowfragmentedcatalog	Allows restores to proceed even if the source's catalog file is fragmented	
o	--SHA256	Forces the restore to use the SHA-256 hash in the image during verification	
o	--sourcevolumename	Tells asr which volume in the source container to invert when doing an APFS restore	
o	--sourcevolumeUUID	Tells asr which volume in the source container to invert when doing an APFS restore	
o	--useReplication	Forces asr to use replication for restoring APFS volumes	
o	--useInverter	Forces asr to use the inverter for restoring APFS volumes	
o	--toSnapshot	Specifies the snapshot on the source APFS volume to restore to the target APFS volume	
o	--fromSnapshot	Names a snapshot on the source APFS volume to use in combination with --toSnapshot to specify a…	
=	restore	--source
t	filepaths
=	restore	--target
t	filepaths
=	restore	--file
t	filepaths
=	restore	--timeout
v	0	
@	restoreexact
o	--source	Can be a disk image, /dev entry, or volume mountpoint	v
o	--target	Can be a /dev entry, or volume mountpoint	v
o	--file	When performing a multicast restore, --file can be specified instead of --target	v
o	--erase	Erases target and is required. --erase must always be used, as file copies are no longer supported…	
o	--format	Specifies the destination filesystem format	V
o	--noprompt	Suppresses the prompt which usually occurs before target	
o	--timeout	Specifies num seconds that a multicast client should wait when no payload data has been received…	V
o	--puppetstrings	Provide progress output that is easy for another program to parse	
o	--noverify	Skips the verification steps normally taken to ensure that a volume has been properly restored	
o	--allowfragmentedcatalog	Allows restores to proceed even if the source's catalog file is fragmented	
o	--SHA256	Forces the restore to use the SHA-256 hash in the image during verification	
o	--sourcevolumename	Tells asr which volume in the source container to invert when doing an APFS restore	
o	--sourcevolumeUUID	Tells asr which volume in the source container to invert when doing an APFS restore	
o	--useReplication	Forces asr to use replication for restoring APFS volumes	
o	--useInverter	Forces asr to use the inverter for restoring APFS volumes	
o	--toSnapshot	Specifies the snapshot on the source APFS volume to restore to the target APFS volume	
o	--fromSnapshot	Names a snapshot on the source APFS volume to use in combination with --toSnapshot to specify a…	
=	restoreexact	--source
t	filepaths
=	restoreexact	--target
t	filepaths
=	restoreexact	--file
t	filepaths
=	restoreexact	--timeout
v	0	
@	server
o	--source	Source has to be a UDIF disk image	v
o	--interface	The network interface to be used for multicasting	v
o	--config	Server requires a configuration file to be passed	v
=	server	--source
t	filepaths
=	server	--config
d
@	imagescan
@	info
o	--plist	Writes its output as an XML-formatted plist	

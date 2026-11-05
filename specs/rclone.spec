@	
s	about	Get quota information from the remote
s	authorize	Remote authorization
s	backend	Run a backend specific command
s	cat	Concatenates any files and sends them to stdout
s	check	Checks the files in the source and destination match
s	cleanup	Clean up the remote if possible
s	config	Enter an interactive configuration session
s	copy	Copy files from source to dest, skipping already copied
s	copyto	Copy files from source to dest, skipping already copied
s	copyurl	Copy url content to dest
s	cryptcheck	Cryptcheck checks the integrity of a crypted remote
s	cryptdecode	Cryptdecode returns unencrypted file names
s	dedupe	Interactively find duplicate filenames and delete/rename them
s	delete	Remove the files in path
s	deletefile	Remove a single file from remote
s	genautocomplete	Output completion script for a given shell
s	gendocs	Output markdown docs for rclone to the directory supplied
s	hashsum	Produces a hashsum file for all the objects in the path
s	help	Show help for rclone commands, flags and backends
s	link	Generate public link to file/folder
s	listremotes	List all the remotes in the config file
s	ls	List the objects in the path with size and path
s	lsd	List all directories/containers/buckets in the path
s	lsf	List directories and objects in remote:path formatted for parsing
s	lsjson	List directories and objects in the path in JSON format
s	lsl	List the objects in path with modification time, size and path
s	md5sum	Produces an md5sum file for all the objects in the path
s	mkdir	Make the path if it doesn't already exist
s	mount	Mount the remote as file system on a mountpoint
s	move	Move files from source to dest
s	moveto	Move file or directory from source to dest
s	ncdu	Explore a remote with a text based user interface
s	obscure	Obscure password for use in the rclone config file
s	purge	Remove the path and all of its contents
s	rc	Run a command against a running rclone
s	rcat	Copies standard input to file on remote
s	rcd	Run rclone listening to remote control commands only
s	rmdir	Remove the empty directory at path
s	rmdirs	Remove empty directories under the path
s	selfupdate	Update the rclone binary
s	serve	Serve a remote over a protocol
s	settier	Changes storage class/tier of objects in remote
s	sha1sum	Produces an sha1sum file for all the objects in the path
s	size	Prints the total size and number of objects in remote:path
s	sync	Make source and dest identical, modifying destination only
s	test	Run a test command
s	touch	Create new file or change file modification time
s	tree	List the contents of the remote in a tree like fashion
s	version	Show the version number
o	--version	View your current rclone version	
o	--help|-h	Show help for rclone commands, flags and backends	
@	about
o	--full	Full numbers instead of SI units	
o	--json	Format output as JSON	
a	1	0
#	about	1
d
@	authorize
o	--auth-no-open-browser	Do not automatically open auth link in default browser	
@	backend
o	--json	Format output as JSON	
@	cat
o	--discard	Discard the output instead of printing	
o	--count	Only print N characters. (default -1)	v
o	--head	Only print the first N characters	v
o	--offset	Start printing at offset N (or from end if -ve)	v
o	--tail	Only print the last N characters	v
a	1	0
#	cat	1
d
@	check
o	--download	Check by downloading rather than with hash	
o	--combined	Make a combined report of changes to this file	v
o	--differ	Report all non-matching files to this file	v
o	--error	Report all files with errors (hashing or reading) to this file	v
o	--match	Report all matching files to this file	v
o	--missing-on-dst	Report all files missing from the destination to this file	v
o	--missing-on-src	Report all files missing from the source to this file	v
o	--one-way	Check one way only, source files must exist on remote	
a	2	0
=	check	--combined
t	filepaths
=	check	--differ
t	filepaths
=	check	--error
t	filepaths
=	check	--match
t	filepaths
=	check	--missing-on-dst
t	filepaths
=	check	--missing-on-src
t	filepaths
#	check	1
d
#	check	2
d
@	cleanup
a	1	0
#	cleanup	1
d
@	config
s	create	Create a new remote with name, type and options
@	config create
a	2	0
@	copy
a	2	0
#	copy	1
d
#	copy	2
d
@	copyto
a	2	0
#	copyto	1
d
#	copyto	2
d
@	copyurl
a	2	0
#	copyurl	2
d
@	cryptcheck
o	--combined	Make a combined report of changes to this file	v
o	--differ	Report all non-matching files to this file	v
o	--error	Report all files with errors (hashing or reading) to this file	v
o	--match	Report all matching files to this file	v
o	--missing-on-dst	Report all files missing from the destination to this file	v
o	--missing-on-src	Report all files missing from the source to this file	v
o	--one-way	Check one way only, source files must exist on remote	
a	2	0
=	cryptcheck	--combined
t	filepaths
=	cryptcheck	--differ
t	filepaths
=	cryptcheck	--error
t	filepaths
=	cryptcheck	--match
t	filepaths
=	cryptcheck	--missing-on-dst
t	filepaths
=	cryptcheck	--missing-on-src
t	filepaths
#	cryptcheck	1
d
#	cryptcheck	2
d
@	cryptdecode
o	--reverse	Reverse cryptdecode, encrypts filenames	
a	2	1
#	cryptdecode	1
d
@	dedupe
o	--by-hash	Find identical hashes rather than names	
o	--dedupe-mode	Dedupe mode	v
a	1	0
=	dedupe	--dedupe-mode
v	interactive	Interactive
v	skip	Removes identical files then skips anything left
v	rename	Removes identical files then renames the rest to be different
v	list	Lists duplicate dirs and files only and changes nothing
v	first	removes identical files then keeps the first one.
v	newest	removes identical files then keeps the newest one.
v	oldest	removes identical files then keeps the oldest one.
v	largest	removes identical files then keeps the largest one.
v	smallest	removes identical files then keeps the smallest one.
#	dedupe	1
d
@	delete
o	--rmdirs	Rmdirs removes empty directories but leaves root intact	
a	1	0
#	delete	1
d
@	deletefile
a	1	0
#	deletefile	1
d
@	genautocomplete
s	bash	Output bash completion script for rclone.
s	fish	Output fish completion script for rclone.
s	zsh	Output zsh completion script for rclone.
@	genautocomplete bash
a	1	0
@	genautocomplete fish
a	1	0
@	genautocomplete zsh
a	1	0
@	gendocs
a	1	0
#	gendocs	1
t	folders
@	hashsum
o	--base64	Output base64 encoded hashsum	
o	--download	Download the file and hash it locally; if this flag is not specified, the hash is requested from…	
o	--output-file	Output hashsums to a file rather than the terminal	v
a	2	0
=	hashsum	--output-file
t	filepaths
#	hashsum	1
v	MD5	
v	SHA-1	
v	DropboxHash	
v	QuickXorHash	
v	Whirlpool	
v	CRC-32	
v	MailruHash	
#	hashsum	2
d
@	help
s	flags	List of global flags
@	help flags
@	link
o	--expire	The amount of time that the link will be valid (default 100y)	v
o	--unlink	Remove existing public link to file/folder	
a	1	0
#	link	1
d
@	listremotes
o	--long	Show the type as well as names	
@	ls
a	1	0
#	ls	1
d
@	lsd
o	-R|--recursive		
a	1	0
#	lsd	1
d
@	lsf
o	--dirs-only	Only list directories	
o	--files-only	Only list files	
o	--recursive|-R	Recurse into the listing	
o	--absolute	Put a leading / in front of path names	
o	--csv	Output in CSV format	
o	-d|--dir-slash	Append a slash to directory names. (default true)	
o	--format|-F	Output format - see help for details (default "p")	v
o	--hash	Use this hash when h is used in the format (default "MD5")	v
o	--separator|-s	Separator for the items in the format. (default ";")	v
a	1	0
=	lsf	--format
v	p	path
v	s	size
v	t	modification time
v	h	hash
v	i	ID of object
v	o	Original ID of underlying object
v	m	MimeType of object if known
=	lsf	--hash
v	MD5	
v	SHA-1	
v	DropboxHash	
v	QuickXorHash	
v	Whirlpool	
v	CRC-32	
v	MailruHash	
#	lsf	1
d
@	lsjson
o	--dirs-only	Only list directories	
o	--files-only	Only list files	
o	--recursive|-R	Recurse into the listing	
o	--encrypted|-M	Show the encrypted names	
o	--hash	Include hashes in the output (may take longer)	
o	--hash-type	Show only this hash type (may be repeated)	v
o	--no-mimetype	Don't read the mime type (can speed things up)	
o	--no-modtime	Don't read the modification time (can speed things up)	
o	--original	Show the ID of the underlying Object	
a	1	0
=	lsjson	--hash-type
v	MD5	
v	SHA-1	
v	DropboxHash	
v	QuickXorHash	
v	Whirlpool	
v	CRC-32	
v	MailruHash	
#	lsjson	1
d
@	lsl
a	1	0
#	lsl	1
d
@	md5sum
o	--base64	Output base64 encoded hashsum	
o	--download	Download the file and hash it locally; if this flag is not specified, the hash is requested from…	
o	--output-file	Output hashsums to a file rather than the terminal	v
a	1	0
=	md5sum	--output-file
t	filepaths
#	md5sum	1
d
@	mkdir
a	1	0
#	mkdir	1
d
@	mount
a	2	0
#	mount	1
d
#	mount	2
t	folders
@	move
a	1	0
@	moveto
a	1	0
@	ncdu
a	1	0
@	obscure
a	1	0
@	purge
a	1	0
@	rc
a	1	0
@	rcat
a	1	0
@	rcd
a	1	0
@	rmdir
a	1	0
@	rmdirs
a	1	0
@	selfupdate
@	serve
a	1	0
@	settier
a	2	0
@	sha1sum
a	1	0
@	size
a	1	0
@	sync
a	2	0
#	sync	1
d
#	sync	2
d
@	test
a	1	0
@	touch
a	1	0
@	tree
a	1	0
@	version

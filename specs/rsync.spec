@	
o	-v|--verbose	Increase verbosity	
o	--info	Fine-grained informational verbosity	v=
o	--debug	Fine-grained debug verbosity	v=
o	--msgs2stderr	Special output handling for debugging	
o	--quiet|-q	Suppress non-error messages	
o	--no-motd	Suppress daemon-mode MOTD (see manpage caveat)	
o	--checksum|-c	Skip based on checksum, not mod-time & size	
o	-a|--archive	Archive mode; equals -rlptgoD (no -H,-A,-X)	
o	--no-OPTION	Turn off an implied OPTION (e.g. --no-D)	
o	-r|--recursive	Recurse into directories	
o	-R|--relative	Use relative path names	
o	--no-implied-dirs	Don't send implied dirs with --relative	
o	-b|--backup	Make backups (see --suffix & --backup-dir)	
o	--backup-dir	Make backups into hierarchy based in DIR	v=
o	--suffix	Set backup suffix (default ~ w/o --backup-dir)	v=
o	-u|--update	Skip files that are newer on the receiver	
o	--inplace	Update destination files in-place (SEE MAN PAGE)	
o	--append	Append data onto shorter files	
o	--append-verify	Like --append, but with old data in file checksum	
o	-d|--dirs	Transfer directories without recursing	v
o	-l|--links	Copy symlinks as symlinks	
o	-L|--copy-links	Transform symlink into referent file/dir	
o	--copy-unsafe-links	Only "unsafe" symlinks are transformed	
o	--safe-links	Ignore symlinks that point outside the source tree	
o	--munge-links	Munge symlinks to make them safer (but unusable)	
o	-k|--copy-dirlinks	Transform symlink to a dir into referent dir	
o	-K|--keep-dirlinks	Treat symlinked dir on receiver as dir	
o	-H|--hard-links	Preserve hard links	
o	-p|--perms	Preserve permissions	
o	-E|--executability	Preserve the file's executability	
o	--chmod	Affect file and/or directory permissions	v=
o	-A|--acls	Preserve ACLs (implies --perms)	
o	-X|--xattrs	Preserve extended attributes	
o	-o|--owner	Preserve owner (super-user only)	
o	-g|--group	Preserve group	
o	--devices	Preserve device files (super-user only)	
o	--copy-devices	Copy device contents as regular file	
o	--specials	Preserve special files	
o	-D	Same as --devices --specials	
o	-t|--times	Preserve modification times	
o	-O|--omit-dir-times	Omit directories from --times	v
o	-J|--omit-link-times	Omit symlinks from --times	
o	--super	Receiver attempts super-user activities	
o	--fake-super	Store/recover privileged attrs using xattrs	
o	-S|--sparse	Turn sequences of nulls into sparse blocks	
o	--preallocate	Allocate dest files before writing them	
o	-n|--dry-run	Perform a trial run with no changes made	
o	-W|--whole-file	Copy files whole (without delta-xfer algorithm)	
o	--checksum-choice	Choose the checksum algorithms	v=
o	-x|--one-file-system	Don't cross filesystem boundaries	
o	-B|--block-size	Force a fixed checksum block-size	v=
o	-e|--rsh	Specify the remote shell to use	v=
o	--rsync-path	Specify the rsync to run on the remote machine	v=
o	--existing	Skip creating new files on receiver	
o	--ignore-existing	Skip updating files that already exist on receiver	
o	--remove-source-files	Sender removes synchronized files (non-dirs)	
o	--delete	Delete extraneous files from destination dirs	
o	--delete-before	Receiver deletes before transfer, not during	
o	--delete-during|--del	Receiver deletes during the transfer	
o	--delete-delay	Find deletions during, delete after	
o	--delete-after	Receiver deletes after transfer, not during	
o	--delete-excluded	Also delete excluded files from destination dirs	
o	--ignore-missing-args	Ignore missing source args without error	
o	--delete-missing-args	Delete missing source args from destination	
o	--ignore-errors	Delete even if there are I/O errors	
o	--force	Force deletion of directories even if not empty	
o	--max-delete	Don't delete more than NUM files	v=
o	--max-size	Don't transfer any file larger than SIZE	v=
o	--min-size	Don't transfer any file smaller than SIZE	v=
o	--partial	Keep partially transferred files	
o	--partial-dir=DIR	Put a partially transferred file into DIR	v=
o	--delay-updates	Put all updated files into place at transfer's end	
o	-m|--prune-empty-dirs	Prune empty directory chains from the file-list	
o	--numeric-ids	Don't map uid/gid values by user/group name	
o	--usermap	Custom username mapping	v=
o	--groupmap	Custom groupname mapping	v=
o	--chown=USER:GROUP	Simple username/groupname mapping	v=
o	--timeout	Set I/O timeout in seconds	v=
o	--contimeout	Set daemon connection timeout in seconds	v=
o	-I|--ignore-times	Don't skip files that match in size and mod-time	
o	-M	Send OPTION to the remote side only	v
o	--remote-option	Send OPTION to the remote side only	v=
o	--size-only	Skip files that match in size	
o	-@	Set the accuracy for mod-time comparisons	v
o	--modify-window	Set the accuracy for mod-time comparisons	v=
o	-T	Create temporary files in directory DIR	v
o	--temp-dir	Create temporary files in directory DIR	v=
o	-y|--fuzzy	Find similar file for basis if no dest file	
o	--compare-dest	Also compare destination files relative to DIR	v=
o	--copy-dest	Also compare destination files relative to DIR and include copies of unchanged files	v
o	--link-dest	Hardlink to files in DIR when unchanged	v=
o	-z|--compress	Compress file data during the transfer	
o	--compress-level	Explicitly set compression level	v=
o	--skip-compress	Skip compressing files with a suffix in LIST	v=
o	-C|--cvs-exclude	Auto-ignore files the same way CVS does	
o	-f	Add a file-filtering RULE	v
o	--filter	Add a file-filtering RULE	v=
o	-F	Same as --filter='dir-merge /.rsync-filter'	v
o	--exclude	Exclude files matching PATTERN	v=
o	--exclude-from	Read exclude patterns from FILE	v=
o	--include	Don't exclude files matching PATTERN	v=
o	--include-from	Read include patterns from FILE	v=
o	--files-from	Read list of source-file names from FILE	v=
o	-0|--from0	All *-from/filter files are delimited by 0s	
o	-s|--protect-args	No space-splitting; only wildcard special-chars	
o	--address	Bind address for outgoing socket to daemon	v=
o	--port	Specify double-colon alternate port number	v=
o	--sockopts	Specify custom TCP options	v=
o	--blocking-io	Use blocking I/O for the remote shell	
o	--stats	Give some file-transfer stats	
o	-8|--8-bit-output	Leave high-bit chars unescaped in output	
o	-h|--human-readable	Output numbers in a human-readable format	
o	--progress	Show progress during transfer	
o	-P	Same as --partial --progress	
o	-i|--itemize-changes	Output a change-summary for all updates	
o	--out-format	Output updates using the specified FORMAT	v=
o	--log-file	Log what we're doing to the specified FILE	v=
o	--log-file-format	Log updates using the specified FMT	v=
o	--password-file	Read daemon-access password from FILE	v=
o	--list-only	List the files instead of copying them	
o	--bwlimit	Limit socket I/O bandwidth	v=
o	--stop-at	Stop rsync at year-month-dayThour:minute	v=
o	--time-limit	Stop rsync after MINS minutes have elapsed	v=
o	--outbuf	Set output buffering to None, Line, or Block	v=
o	--write-batch	Write a batched update to FILE	v=
o	--only-write-batch	Like --write-batch but w/o updating destination	v=
o	--read-batch	Read a batched update from FILE	v=
o	--protocol	Force an older protocol version to be used	v=
o	--iconv	Request charset conversion of filenames	v=
o	--checksum-seed	Set block/file checksum seed (advanced)	v=
o	--noatime	Do not alter atime when opening source files	
o	-4|--ipv4	Prefer IPv4	
o	-6|--ipv6	Prefer IPv6	
o	--version	Print version number	
o	-h|--help	Show help for rsync (-h is --help only if used alone)	
a	2	0
=		--backup-dir
t	folders
=		-d
t	folders
=		-O
t	folders
=		--checksum-choice
v	auto	
v	md4	
v	md5	
v	none	
=		--partial-dir=DIR
t	folders
=		-T
t	folders
=		--temp-dir
t	folders
=		--compare-dest
t	folders
=		--copy-dest
t	folders
=		--link-dest
t	folders
=		--compress-level
v	0	
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
=		-F
t	folders
=		--exclude-from
t	filepaths
=		--include-from
t	filepaths
=		--files-from
t	filepaths
=		--log-file
t	filepaths
=		--password-file
t	filepaths
=		--outbuf
v	N	
v	L	
v	B	
=		--write-batch
t	filepaths
=		--only-write-batch
t	filepaths
=		--read-batch
t	filepaths
#		1
t	history,filepaths,folders
d
#		2
t	history,filepaths,folders
d

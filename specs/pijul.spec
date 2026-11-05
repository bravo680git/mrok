@	
s	add	Adds a path to the tree
s	apply	Applies changes to a channel
s	archive	Creates an archive of the repository
s	change	Shows information about a particular change
s	channel	Manages different channels
s	clone	Clones an existing pijul repository
s	credit	Shows which change last affected each line of the given file(s)
s	diff	Shows difference between two channels/changes
s	fork	Create a new channel
s	init	Initializes an empty pijul repository
s	log	Show the entire log of changes
s	ls	
s	mv	
s	pull	Pulls changes from a remote upstream
s	push	Pushes changes to a remote upstream
s	record	Creates a new change
s	remote	Manages remote repositories
s	remove	Removes a file from the tree of tracked files (pijul record will then record this as a deletion)
s	reset	Resets the working copy to the last recorded change.
s	unrecord	Unrecords a list of changes
@	add
o	-f|--force		
o	-h|--help	Print help information	
o	-r|--recursive		
a	1	0
@	apply
o	--channel	Apply change to this channel	v
o	--deps-only	Only apply the dependencies of the change, not the change itself. Only applicable for a single…	
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
a	1	0
@	archive
o	--change	Apply these changes after switching to the channel	v
o	--channel	Use this channel, instead of the current channel	v
o	-h|--help	Print help information	
o	-k	Do not check certificates (HTTPS remotes only, this option might be dangerous)	
o	-o	Name of the output file	v
o	--prefix	Append this path in front of each path inside the archive	v
o	--remote	Ask the remote to send an archive	v
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
o	--state	Archive in this state	v
o	--umask	Append this path in front of each path inside the archive	v
@	change
o	-h|--help	Print help information	
o	--repository	Use the repository at PATH instead of the current directory	v
a	1	0
@	channel
s	delete	Delete a channel. The channel must not be the current channel
s	help	Print this message or the help of the given subcommand(s)
s	new	Create a new, empty channel
s	rename	Rename a channel
s	switch	Switch to a channel. There must not be unrecorded changes in the working copy
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
@	channel delete
o	-h|--help	Print help information	
a	1	0
@	channel help
@	channel new
@	channel rename
o	-h|--help	Print help information	
a	2	0
@	channel switch
@	clone
o	--change	Clone this change and its dependencies	v
o	--channel	Set the remote channel [default: main]	v
o	-h|--help	Print help information	
o	-k	Do not check certificates (HTTPS remotes only, this option might be dangerous)	
o	--path	Clone this path only	v
o	--state	Clone this state	v
a	3	0
@	credit
o	--channel	Use this channel instead of the current channel	v
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
a	1	0
@	diff
o	--channel	Compare with this channel	v
o	-h|--help	Print help information	
o	--json	Output the diff in JSON format instead of the default change text format	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
o	-s|--short	Show a short version of the diff	
o	--tag	Add all the changes of this channel as dependencies (except changes implied transitively), instead…	
o	-u|--untracked	Include the untracked files	
a	1	0
@	fork
o	--change	Apply this change after creating the channel	v
o	--channel	Make the new channel from this channel instead of the current channel	v
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
a	1	0
@	init
o	--channel	Set the name of the current channel (defaults to “main”)	v
o	-h|--help	Print help information	
o	-k|--kind	Project kind; if Pijul knows about your project kind, the .ignore file will be populated with a…	v
a	1	0
@	log
o	--channel	Show logs for this channel instead of the current channel	v
o	--description	Include full change description in the output	
o	-h|--help	Print help information	
o	--hash-only	Only show the change hashes	
o	--limit	Output at most this many changes	v
o	--offset	Start after this many changes	v
o	--output-format		v
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
o	--state	Include state identifiers in the output	
a	1	0
@	ls
@	mv
@	pull
o	-a|--all	Pull all changes	
o	-f|--force-cache	Force an update of the local remote cache. May effect some reporting of unrecords/concurrent…	
o	--from-channel	Pull from this remote channel	v
o	--full	Download full changes, even when not necessary	
o	-h|--help	Print help information	
o	-k	Do not check certificates (HTTPS remotes only, this option might be dangerous)	
o	--path	Only pull to these paths	v
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
o	--to-channel	Pull into this channel instead of the current channel	v
a	2	0
@	push
o	-a|--all	Push all changes	
o	-f|--force-cache	Force an update of the local remote cache. May effect some reporting of unrecords/concurrent…	
o	--from-channel	Push from this channel instead of the default channel	v
o	-h|--help	Print help information	
o	-k	Do not check certificates (HTTPS remotes only, this option might be dangerous)	
o	--path	Push changes only relating to these paths	v
o	--repository	Path to the repository. Uses the current repository if the argument is omitted	v
o	--to-channel	Push to this remote channel instead of the remote’s default channel	v
a	2	0
@	record
o	-a|--all	Record all paths that have changed	
o	--amend	Amend this change instead of creating a new change	v
o	--author	Set the author field	v
o	--channel	Record the change in this channel instead of the current channel	v
o	-h|--help	Print help information	
o	--ignore-missing	Ignore missing (deleted) files	
o	-m|--message	Set the change message	v
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
o	--timestamp	Set the timestamp field	v
o	--working-copy		v
a	1	0
@	remote
s	delete	Deletes the remote
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
@	remote delete
o	-h|--help	Print help information	
a	1	0
@	remote help
@	remove
o	-h|--help	Print help information	
a	1	0
@	reset
o	--channel	Reset the working copy to this channel, and change the current channel to this channel	v
o	--dry-run	Print this file to the standard output, without modifying the repository (works for a single file…	
o	-f|--force	Reset even if there are unrecorded changes	
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
a	1	0
@	unrecord
o	--channel	Unrecord changes from this channel instead of the current channel	v
o	-h|--help	Print help information	
o	--repository	Set the repository where this command should run. Defaults to the first ancestor of the current…	v
o	--reset	Also undo the changes in the working copy (preserving unrecorded changes if there are any)	
o	--show-changes	Show N changes in a text editor if no s were given. Defaults to the value of unrecord_changes in…	v
a	1	0

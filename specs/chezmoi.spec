@	
s	manage|add	Add an existing file, directory, or symlink to the source state
s	apply	Update the destination directory to match the target state
s	archive	Generate a tar archive of the target state
s	cat	Print the target contents of a file, script, or symlink
s	cd	Launch a shell in the source directory
s	chattr	Change the attributes of a target in the source state
s	completion	Generate shell completion code
s	data	Print the template data
s	decrypt	Decrypt file or standard input
s	diff	Print the diff between the target state and the destination state
s	doctor	Check your system for potential problems
s	dump	Generate a dump of the target state
s	edit	Edit the source state of a target
s	edit-config	Edit the configuration file
s	encrypt	Encrypt file or standard input
s	execute-template	Execute the given template(s)
s	unmanage|forget	Remove a target from the source state
s	generate	Generate a file for use with chezmoi
s	git	Run git in the source directory
s	ignored	Print ignored targets
s	import	Import an archive into the source state
s	init	Setup the source directory and update the destination directory to match the target state
s	license	Print license
s	list|managed	List the managed entries in the destination directory
s	merge	Perform a three-way merge between the destination state, the source state, and the target state
s	merge-all	Perform a three-way merge for each modified file
s	purge	Purge chezmoi's configuration and data
s	re-add	Re-add modified files
s	rm|remove	Remove a target from the source state and the destination directory
s	secret	Interact with a secret manager
s	source-path	Print the source path of a target
s	state	Manipulate the persistent state
s	status	Show the status of targets
s	target-path	Print the target path of a source path
s	unmanaged	List the unmanaged files in the destination directory
s	update	Pull and apply any changes
s	upgrade	Upgrade chezmoi to the latest released version
s	verify	Exit with success if the destination state matches the target state, fail otherwise
s	help	Help about any command
o	--cache	Set cache directory	v=p
o	--color	Colorize output	v=p
o	--config|-c	Set config file	v=p
o	--config-format	Set config file format	v=p
o	--debug	Include debug information in output	p
o	--destination|-D	Set destination directory	v=p
o	--dry-run|-n	Do not make any modifications to the destination directory	p
o	--force	Make all changes without prompting	p
o	--interactive	Prompt for all changes	p
o	--keep-going|-k	Keep going as far as possible after an error	p
o	--mode	Mode	v=p
o	--no-pager	Do not use the pager	p
o	--no-tty	Do not attempt to get a TTY for reading passwords	p
o	--output|-o	Write output to path instead of stdout	v=p
o	--persistent-state	Set persistent state file	v=p
o	--refresh-externals|-R	Refresh external cache	p
o	--source|-S	Set source directory	v=p
o	--source-path	Specify targets by source path	p
o	--use-builtin-age	Use builtin age	v=p
o	--use-builtin-git	Use builtin git	v=p
o	--verbose|-v	Make output more verbose	p
o	--working-tree|-W	Set working tree directory	v=p
o	--help|-h	Display help	p
=		--color
v	true	
v	false	
v	auto	
=		--config
t	filepaths
=		--config-format
v	json	
v	toml	
v	yaml	
=		--destination
t	folders
=		--mode
v	file	
v	symlink	
=		--output
t	filepaths
=		--source
t	folders
=		--use-builtin-age
v	true	
v	false	
v	auto	
=		--use-builtin-git
v	true	
v	false	
v	auto	
=		--working-tree
t	folders
@	manage
o	--autotemplate|-a	Generate the template when adding files as templates	
o	--create	Add files that should exist, irrespective of their contents	
o	--encrypt	Encrypt files	
o	--exact	Add directories exactly	
o	--exclude|-x	Exclude entry types	v=
o	--follow|-f	Add symlink targets instead of symlinks	
o	--include|-i	Include entry types	v=
o	--prompt|-p	Prompt before adding each entry	
o	--recursive|-r	Recurse into subdirectories	
o	--template|-T	Add files as templates	
o	--template-symlinks	Add symlinks with target in source or home dirs as templates	
a	1	1
=	manage	--exclude
d
=	manage	--include
d
#	manage	1
t	filepaths,folders
@	apply
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
a	1	1
=	apply	--exclude
d
=	apply	--include
d
#	apply	1
t	filepaths,folders
@	archive
o	--exclude|-x	Exclude entry types	v=
o	--format|-f	Set archive format	v=
o	--gzip|-z	Compress output with gzip	
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
a	1	1
=	archive	--exclude
d
=	archive	--format
v	tar	
v	tar.bz2	
v	tar.gz	
v	tar.xz	
v	tbz2	
v	tgz	
v	txz	
v	zip	
=	archive	--include
d
#	archive	1
t	filepaths,folders
@	cat
a	1	1
#	cat	1
t	filepaths,folders
@	cd
@	chattr
a	2	1
#	chattr	1
d
#	chattr	2
t	filepaths,folders
@	completion
a	1	0
#	completion	1
v	bash	
v	fish	
v	zsh	
v	powershell	
@	data
o	--format|-f	Format	v=p
=	data	--format
v	json	
v	yaml	
@	decrypt
a	1	1
#	decrypt	1
t	filepaths
@	diff
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--pager	Set pager	v=
o	--recursive|-r	Recurse into subdirectories	
o	--reverse	Reverse the direction of the diff	
o	--use-builtin-diff	Use the builtin diff	
a	1	1
=	diff	--exclude
d
=	diff	--include
d
@	doctor
@	dump
o	--exclude|-x	Exclude entry types	v=
o	--format|-f	Set output format	v=
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
a	1	1
=	dump	--exclude
d
=	dump	--include
d
#	dump	1
t	filepaths
@	edit
o	--apply|-a	Apply after editing	
o	--exclude|-x	Exclude entry types	v=
o	--hardlink	Invoke editor with a hardlink to the source file	
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
a	1	1
=	edit	--exclude
d
=	edit	--include
d
#	edit	1
t	filepaths
@	edit-config
@	encrypt
a	1	1
#	encrypt	1
t	filepaths
@	execute-template
o	--init|-i	Simulate chezmoi init	
o	--promptBool	Simulate promptBool	v=
o	--promptInt	Simulate promptInt	v=
o	--promptString|-p	Simulate promptString	v=
o	--stdinisatty	Simulate stdinIsATTY	
a	1	1
#	execute-template	1
t	filepaths
@	unmanage
a	1	1
#	unmanage	1
t	filepaths
@	generate
a	1	0
#	generate	1
v	install.sh	
@	git
@	ignored
@	import
o	--exact	Set exact_ attribute on imported directories	
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
o	--remove-destination|-r	Remove destination before import	
o	--strip-components	Strip leading path components	v=
a	1	0
=	import	--exclude
d
=	import	--include
d
#	import	1
t	filepaths
@	init
o	--apply|-a	Update destination directory	
o	--branch	Set initial branch to checkout	v=
o	--config-path|-C	Path to write generated config file	v=
o	--data	Include existing template data	
o	--depth|-d	Create a shallow clone	v=
o	--exclude|-x	Exclude entry types	v=
o	--guess-repo-url|-g	Guess the repo URL	
o	--one-shot	Run in one-shot mode	
o	--prompt	Force prompt*Once template functions to prompt	
o	--purge|-p	Purge config and source directories after running	
o	--purge-binary|-P	Purge chezmoi binary after running	
o	--ssh	Use ssh instead of https when guessing dotfile repo URL	
a	1	0
=	init	--exclude
d
@	license
@	list
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
=	list	--exclude
d
=	list	--include
d
@	merge
a	1	1
#	merge	1
t	filepaths
@	merge-all
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
@	purge
o	--binary|-P	Purge chezmoi binary	
@	re-add
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
=	re-add	--exclude
d
=	re-add	--include
d
@	rm
o	--recursive|-r	Recurse into subdirectories	
a	1	1
#	rm	1
t	filepaths
@	secret
s	keyring	Interact with keyring
@	secret keyring
s	delete	Delete a value from keyring
s	get	Get a value from keyring
s	set	Set a value in keyring
@	secret keyring delete
o	--service	Service	v=p
o	--user	User	v=p
@	secret keyring get
o	--service	Service	v=p
o	--user	User	v=p
@	secret keyring set
o	--service	Service	v=p
o	--user	User	v=p
o	--value	Value	v=p
@	source-path
a	1	1
#	source-path	1
t	filepaths
@	state
s	data	Print the raw data in the persistent state
s	delete	Delete a value from the persistent state
s	delete-bucket	Delete a bucket from the persistent state
s	dump	Generate a dump of the persistent state
s	get	Get a value from the persistent state
s	get-bucket	Get a bucket from the persistent state
s	reset	Reset the persistent state
s	set	Set a value from the persistent state
@	state data
o	--format|-f	Format	v=p
@	state delete
o	--bucket	Bucket	v=p
o	--key	Key	v=p
@	state delete-bucket
o	--bucket	Bucket	v=p
@	state dump
o	--format|-f	Format	v=p
@	state get
o	--bucket	Bucket	v=p
o	--key	Key	v=p
@	state get-bucket
o	--bucket	Bucket	v=p
o	--format|-f	Format	v=p
@	state reset
@	state set
o	--bucket	Bucket	v=p
o	--key	Key	v=p
o	--value	Value	v=p
@	status
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
a	1	1
=	status	--exclude
d
=	status	--include
d
#	status	1
t	filepaths
@	target-path
a	1	1
#	target-path	1
t	filepaths
@	unmanaged
a	1	1
#	unmanaged	1
t	filepaths
@	update
o	--apply|-a	Apply after pulling	
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
=	update	--exclude
d
=	update	--include
d
@	upgrade
o	--executable	Set executable to replace	v=
o	--method	Set upgrade method	v=
o	--owner	Set owner	v=
o	--repo	Set repo	v=
@	verify
o	--exclude|-x	Exclude entry types	v=
o	--include|-i	Include entry types	v=
o	--init	Recreate config file from template	
o	--recursive|-r	Recurse into subdirectories	
a	1	1
=	verify	--exclude
d
=	verify	--include
d
#	verify	1
t	filepaths
@	help
s	manage|add	Add an existing file, directory, or symlink to the source state
s	apply	Update the destination directory to match the target state
s	archive	Generate a tar archive of the target state
s	cat	Print the target contents of a file, script, or symlink
s	cd	Launch a shell in the source directory
s	chattr	Change the attributes of a target in the source state
s	completion	Generate shell completion code
s	data	Print the template data
s	decrypt	Decrypt file or standard input
s	diff	Print the diff between the target state and the destination state
s	doctor	Check your system for potential problems
s	dump	Generate a dump of the target state
s	edit	Edit the source state of a target
s	edit-config	Edit the configuration file
s	encrypt	Encrypt file or standard input
s	execute-template	Execute the given template(s)
s	unmanage|forget	Remove a target from the source state
s	generate	Generate a file for use with chezmoi
s	git	Run git in the source directory
s	ignored	Print ignored targets
s	import	Import an archive into the source state
s	init	Setup the source directory and update the destination directory to match the target state
s	license	Print license
s	list|managed	List the managed entries in the destination directory
s	merge	Perform a three-way merge between the destination state, the source state, and the target state
s	merge-all	Perform a three-way merge for each modified file
s	purge	Purge chezmoi's configuration and data
s	re-add	Re-add modified files
s	rm|remove	Remove a target from the source state and the destination directory
s	secret	Interact with a secret manager
s	source-path	Print the source path of a target
s	state	Manipulate the persistent state
s	status	Show the status of targets
s	target-path	Print the target path of a source path
s	unmanaged	List the unmanaged files in the destination directory
s	update	Pull and apply any changes
s	upgrade	Upgrade chezmoi to the latest released version
s	verify	Exit with success if the destination state matches the target state, fail otherwise
@	help manage
@	help apply
@	help archive
@	help cat
@	help cd
@	help chattr
@	help completion
@	help data
@	help decrypt
@	help diff
@	help doctor
@	help dump
@	help edit
@	help edit-config
@	help encrypt
@	help execute-template
@	help unmanage
@	help generate
@	help git
@	help ignored
@	help import
@	help init
@	help license
@	help list
@	help merge
@	help merge-all
@	help purge
@	help re-add
@	help rm
@	help secret
s	keyring	Interact with keyring
@	help secret keyring
s	delete	Delete a value from keyring
s	get	Get a value from keyring
s	set	Set a value in keyring
@	help secret keyring delete
@	help secret keyring get
@	help secret keyring set
@	help source-path
@	help state
s	data	Print the raw data in the persistent state
s	delete	Delete a value from the persistent state
s	delete-bucket	Delete a bucket from the persistent state
s	dump	Generate a dump of the persistent state
s	get	Get a value from the persistent state
s	get-bucket	Get a bucket from the persistent state
s	reset	Reset the persistent state
s	set	Set a value from the persistent state
@	help state data
@	help state delete
@	help state delete-bucket
@	help state dump
@	help state get
@	help state get-bucket
@	help state reset
@	help state set
@	help status
@	help target-path
@	help unmanaged
@	help update
@	help upgrade
@	help verify

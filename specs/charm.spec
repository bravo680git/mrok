@	
s	backup-keys	Backup your Charm account keys
s	completion	Generate shell completion
s	crypt	Use charm encryption
s	fs	Use the Charm file systems
s	help	Help about any command
s	id	Print your Charm ID
s	import-keys	Import previously backed up Charm account keys
s	jwt	Print a JWT
s	keys	Browse or print linked SSH keys
s	kv	Use the Charm key value store
s	link	Link multiple machines to your Charm account
s	name	Username stuff
s	serve	Start a self-hosted Charm Cloud server
o	--help|-h	Help for charm	
o	--version|-v	Version for charm	
@	backup-keys
@	completion
@	crypt
s	decrypt	Decrypt stdin with your Charm account encryption key
s	decrypt-lookup	Decrypt arg deterministically
s	encrypt	Encrypt stdin with your Charm account encryption key
s	encrypt-lookup	Encrypt arg deterministically
@	crypt decrypt
@	crypt decrypt-lookup
@	crypt encrypt
@	crypt encrypt-lookup
@	fs
s	cat	Output the content of the file at path
s	cp	Copy a file, preface source or destination with "charm:" to specify a remote path
s	ls	List file or directory at path
s	mv	Move a file, preface source or destination with "charm" to specify a remote path
s	rm	Remove file or directory at path
s	tree	Print a file system tree from path
@	fs cat
a	1	0
@	fs cp
o	--recursive|-r	Copy directories recursively	
a	2	0
@	fs ls
a	1	0
@	fs mv
a	2	0
@	fs rm
a	1	0
@	fs tree
a	1	0
@	help
@	id
@	import-keys
o	--force-overwrite|-f	Overwrite if keys exist; don't prompt for input	
a	1	0
#	import-keys	1
v	BACKUP.tar	
t	filepaths
@	jwt
@	keys
o	--randomart|-r	Print SSH 5.1 randomart for each key (the Drunken Bishop algorithm)	
o	--simple|-s	Simple, non-interactive output (good for scripts)	
@	kv
s	delete	Delete a key with an optional @ db
s	get	Get a value for a key with an optional @ db
s	list	List all key value pairs with an optional @ db
s	reset	Delete local db and pull down fresh copy from Charm Cloud
s	set	Set a value for a key with an optional @ db
s	sync	Sync local db with latest Charm Cloud db
@	kv delete
a	1	0
@	kv get
a	1	0
@	kv list
a	1	0
@	kv reset
a	1	0
@	kv set
a	2	0
@	kv sync
a	1	0
@	link
a	1	0
@	name
a	1	0
@	serve
o	--data-dir	Directory to store SQLite db, SSH keys and file data	v
o	--health-port	Health port to listen on	v
o	--http-port	HTTP port to listen on	v
o	--ssh-port	SSH port to listen on	v
o	--stats-port	Stats port to listen on	v
=	serve	--data-dir
t	folders
=	serve	--health-port
v	35356	
=	serve	--http-port
v	35354	
=	serve	--ssh-port
v	35353	
=	serve	--stats-port
v	35355	

@	
s	help	Print this message or the help of the given subcommand(s)
s	start	Start the database server
s	backup	Backup data to or from an existing database
s	import	Import a SurrealQL script into an existing database
s	export	Export an existing database as a SurrealQL script
s	version	Output the command-line tool version information
s	sql	Start an SQL REPL in your terminal with pipe support
o	--help|-h	Print help information	
@	help
a	1	0
#	help	1
t	help
@	start
o	--	Everything after this is an argument	
o	--addr	The allowed networks for master authentication [env: ADDR=] [default: 127.0.0.1/32]	v
o	--bind|-b	The hostname or ip address to listen for connections on [env: BIND=] [default: 0.0.0.0:8000]	v
o	--key|-k	Encryption key to use for on-disk encryption [env: KEY=]	v
o	--kvs-ca	Path to the CA file used when connecting to the remote KV store [env: KVS_CA=]	v
o	--kvs-crt	Path to the certificate file used when connecting to the remote KV store [env: KVS_CRT=]	v
o	--kvs-key	Path to the private key file used when connecting to the remote KV store [env: KVS_KEY=]	v
o	--log|-l	The logging level for the database server [env: LOG=] [default: info] [possible values: warn…	v
o	--pass|-p	The master password for the database [env: PASS=]	v
o	--strict|-s	Whether strict mode is enabled on this database instance [env: STRICT=]	v
o	--user|-u	The master username for the database [env: USER=] [default: root]	v
o	--web-crt	Path to the certificate file for encrypted client connections [env: WEB_CRT=]	v
o	--web-key	Path to the private key file for encrypted client connections [env: WEB_KEY=]	v
a	1	0
=	start	--log
v	warn	
v	info	
v	debug	
v	trace	
v	full	
@	backup
o	--pass|-p	Database authentication password to use when connecting [default: root]	v
o	--user|-u	Database authentication username to use when connecting [default: root]	v
a	2	0
@	import
o	--pass|-p	Database authentication password to use when connecting [default: root]	v
o	--user|-u	Database authentication username to use when connecting [default: root]	v
o	--conn|-c	Remote database server url to connect to [default: https://cloud.surrealdb.com]	v
o	--ns	The namespace to import the data into	v
o	--db	The database to import the data into	v
a	1	0
@	export
o	--pass|-p	Database authentication password to use when connecting [default: root]	v
o	--user|-u	Database authentication username to use when connecting [default: root]	v
o	--conn|-c	Remote database server url to connect to [default: https://cloud.surrealdb.com]	v
o	--ns	The namespace to export the data from	v
o	--db	The database to export the data from	v
a	1	0
@	version
@	sql
o	--pass|-p	Database authentication password to use when connecting [default: root]	v
o	--user|-u	Database authentication username to use when connecting [default: root]	v
o	--conn|-c	Remote database server url to connect to [default: https://cloud.surrealdb.com]	v
o	--ns	The namespace to export the data from	v
o	--db	The database to export the data from	v
o	--pretty	Whether database responses should be pretty printed	
a	1	0

@	
o	--help|-?	Show help for pg_dump	
o	--file|-f	Output file or directory name	v
o	--format|-F	Output file format	v
o	--jobs|-j	Number of parallel job to dump	v
o	--verbose|-v	Verbose mode	
o	--version|-V	Output version information	
o	--compress|-Z	Compression level for compressed formats	v
o	--lock-wait-timeout	Fail after waiting <timeout> for a table lock	v
o	--no-sync	Do not wait for changes to be written safely to disk	
o	--data-only|-a	Dump only the data, not the schema	
o	--blobs|-b	Include large objects in dump	
o	--no-blobs|-B	Exclude large objects in dump	
o	--clean|-c	Clean (drop) database objects before recreating	
o	--create|-C	Include commands to create database in dump	
o	--extension|-e	Dump the specified extension(s) only	v
o	--encoding|-E	Dump the data in encoding <encoding>	v
o	--schema|-n	Dump the specified schema(s) only	v
o	--exclude-schema|-N	Do NOT dump the specified schema(s)	v
o	--no-owner|-O	Skip restoration of object ownership in plain-text format	
o	--schema-only|-s	Dump only the schema, no data	
o	--superuser|-S	Superuser user name to use in plain-text format	v
o	--table|-t	Dump the specified table(s) only	v
o	--exclude-table|-T	Do NOT dump the specified table(s)	v
o	--no-privileges|-x|--no-acl	Do not dump privileges (grant/revoke)	
o	--binary-upgrade	For use by upgrade utilities only	
o	--column-inserts|--attribute-inserts	Dump data as INSERT commands with column names	
o	--disable-dollar-quoting	Disable dollar quoting, use SQL standard quoting	
o	--disable-triggers	Disable triggers during data-only restore	
o	--enable-row-security	Enable row security (dump only content user has access to)	
o	--exclude-table-data	Do NOT dump data for the specified table(s)	v
o	--extra-float-digits	Override default setting for extra_float_digits	v
o	--if-exists	Use IF EXISTS when dropping objects	
o	--include-foreign-data	Include data of foreign tables on foreign servers matching PATTERN	v
o	--inserts	Dump data as INSERT commands, rather than COPY	
o	--load-via-partition-root	Load partitions via the root table	
o	--no-comments	Do not dump comments	
o	--no-publications	Do not dump publications	
o	--no-security-labels	Do not dump security label assignments	
o	--no-subscriptions	Do not dump subscriptions	
o	--no-synchronized-snapshots	Do not use synchronized snapshots in parallel jobs	
o	--no-tablespaces	Do not dump tablespace assignments	
o	--no-toast-compression	Do not dump TOAST compression methods	
o	--no-unlogged-table-data	Do not dump unlogged table data	
o	--on-conflict-do-nothing	Add ON CONFLICT DO NOTHING to INSERT commands	
o	--quote-all-identifiers	Quote all identifiers, even if not key words	
o	--rows-per-insert	Number of rows per INSERT; implies --inserts	v
o	--section	Dump named section (pre-data, data, or post-data)	v
o	--serializable-deferrable	Wait until the dump can run without anomalies	
o	--snapshot	Use given snapshot for the dump	v
o	--strict-names	Require table and/or schema include patterns to match at least one entity each	
o	--use-set-session-authorization	Use SET SESSION AUTHORIZATION commands instead of ALTER OWNER commands to set ownership	
o	--dbname|-d	Database to dump	v
o	--host|-h	Database server host or socket directory	v
o	--port|-p	Database server port number	v
o	--username|-U	Connect as specified database user	v
o	--no-password|-w	Never prompt for password	
o	--password|-W	Force password prompt (should happen automatically)	
o	--role	Do SET ROLE before dump	v
a	1	0
=		--format
v	c	
v	d	
v	t	
v	p	
=		--compress
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

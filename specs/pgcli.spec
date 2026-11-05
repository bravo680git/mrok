@	
o	-h|--host	Host address of the postgres database	v
o	-p|--port	Port number at which the postgres instance is listening	v
o	-U|--username	Username to connect to the postgres database	v
o	-u|--user	Username to connect to the postgres database	v
o	-W|--password	Force password prompt	
o	-w|--no-password	Never prompt for password	
o	--single-connection	Do not use a separate connection for completions	
o	-v|--version	Version of pgcli	
o	-d|--dbname	Database name to connect to	v
o	--pgclirc	Location of pgclirc file	v
o	-D|--dsn	Use DSN configured into the [alias_dsn] section of pgclirc file	v
o	--list-dsn	List of DSN configured into the [alias_dsn] section of pgclirc file	
o	--row-limit	Set threshold for row limit prompt. Use 0 to disable prompt	v
o	--less-chatty	Skip intro on startup and goodbye on exit	
o	--prompt	Prompt format (Default: "\u@\h:\d> ")	v
o	--prompt-dsn	Prompt format for connections using DSN aliases (Default: "\u@\h:\d> ")	v
o	-l|--list	List available databases, then exit	
o	--auto-vertical-output	Automatically switch to vertical output mode if the result is wider than the terminal width	
o	--warn	Warn before running a destructive query	v
o	--ssh-tunnel	Open an SSH tunnel to the given address and connect to the database from it	v
o	--help	Show this message and exit	
a	1	0
=		--pgclirc
t	filepaths
=		--warn
v	all	
v	moderate	
v	off	

@	
o	--auto-rehash	Enable automatic rehashing	
o	--auto-vertical-output	Enable automatic vertical result set display	
o	--batch|-B	Do not use history file	
o	--binary-as-hex	Display binary values in hexadecimal notation	
o	--binary-mode	Disable \r\n - to - \n translation and treatment of \0 as end-of-query	
o	--bind-address	Use specified network interface to connect to MySQL Server	v
o	--character-sets-dir	Directory where character sets are installed	v
o	--column-names	Write column names in results	
o	--column-type-info	Display result set metadata	
o	--comments|-c	Whether to retain or strip comments in statements sent to the server	
o	--compress|-C	Compress all information sent between client and server	
o	--compression-algorithms	Permitted compression algorithms for connections to server	v
o	--connect-expired-password	Indicate to server that client can handle expired-password sandbox mode	
o	--connect-timeout	Number of seconds before connection timeout	v
o	-D|--database	The database to use	v
o	--debug	Write debugging log; supported only if MySQL was built with debugging support	
o	--debug-check	Print debugging information when program exits	
o	-T|--debug-info	Print debugging information, memory, and CPU statistics when program exits	
o	--default-auth	Authentication plugin to use	v
o	--default-character-set	Specify default character set	v
o	--defaults-extra-file	Read named option file in addition to usual option files	v
o	--defaults-file	Read only named option file	v
o	--defaults-group-suffix	Option group suffix value	v
o	--delimiter	Set the statement delimiter	v
o	--disable-named-commands	Disable named commands. Use the \* form only, or use named commands only at the beginning of a…	
o	--dns-srv-name	Use DNS SRV lookup for host information	v
o	--enable-cleartext-plugin	Enable cleartext authentication plugin	
o	-e|--execute	Execute the statement and quit	v
o	-f|--force	Continue even if an SQL error occurs	
o	--get-server-public-key	Request RSA public key from server	
o	--help|-?	Display help message and exit	
o	--histignore	Patterns specifying which statements to ignore for logging	
o	-h|--host	Host on which MySQL server is located	v
o	-H|--html	Produce HTML output	
o	-i|--ignore-spaces	Ignore spaces after function names	
o	--init-command	SQL statement to execute after connecting	v
o	--line-numbers	Write line numbers for errors	
o	--load-data-local-dir	Directory for files named in LOAD DATA LOCAL statements	v
o	--local-infile	Enable or disable for LOCAL capability for LOAD DATA	v
o	--login-path	Read login path options from .mylogin.cnf	v
o	--max-allowed-packet	Maximum packet length to send to or receive from server	v
o	--max-join-size	The automatic limit for rows in a join when using --safe-updates	v
o	-G|--named-commands	Enable named mysql commands	
o	--net-buffer-length	Buffer size for TCP/IP and socket communication	v
o	--network-namespace	Specify network namespace	v
o	-A|--no-auto-rehash	Disable automatic rehashing	
o	--no-beep|-b	Do not beep when errors occur	
o	--no-defaults	Read no option files	
o	-o|--one-database	Ignore statements except those for the default database named on the command line	
o	--pager	Use the given command for paging query output	v
o	-p|--password	Password to use when connecting to server	v
o	--pipe|-W	Connect to server using named pipe (Windows only)	
o	--plugin-dir	Directory where plugins are installed	v
o	-P|--port	TCP/IP port number for connection	v
o	--print-defaults	Print default options	
o	--prompt	Set the prompt to the specified format	v
o	--protocol	Transport protocol to use	v
o	-q|--quick	Do not cache each query result	
o	-r|--raw	Write column values without escape conversion	
o	--reconnect	If the connection to the server is lost, automatically try to reconnect	
o	-U|--safe-updates|--i-am-a-dummy	Allow only UPDATE and DELETE statements that specify key values	
o	--select-limit	The automatic limit for SELECT statements when using --safe-updates	v
o	--server-public-key-path	Path name to file containing RSA public key	v
o	--shared-memory-base-name	Shared-memory name for shared-memory connections (Windows only)	v
o	--show-warnings	Show warnings after each statement if there are any	
o	--sigint-ignore	Ignore SIGINT signals (typically the result of typing Control+C)	
o	-s|--silent	Silent mode. Produce less output. This option can be given multiple times to produce less and less…	
o	--skip-auto-rehash	Disable automatic rehashing	
o	-N|--skip-column-names	Do not write column names in results	
o	-L|--skip-line-numbers	Skip line numbers for errors	
o	--skip-named-commands	Disable named mysql commands	
o	--skip-pager	Disable paging	
o	--skip-reconnect	Disable reconnecting	
o	-S|--socket	Unix socket file or Windows named pipe to use"File that contains list of trusted SSL Certificate…	v
o	--ssl-ca	File that contains list of trusted SSL Certificate Authorities	v
o	--ssl-capath	Directory that contains trusted SSL Certificate Authority certificate files	v
o	--ssl-cert	File that contains X.509 certificate	v
o	--ssl-cipher	Permissible ciphers for connection encryption	
o	--ssl-crl	File that contains certificate revocation lists	v
o	--ssl-crlpath	Directory that contains certificate revocation-list files	v
o	--ssl-fips-mode	Whether to enable FIPS mode on client side	v
o	--ssl-key	File that contains X.509 key	v
o	--ssl-mode	Desired security state of connection to server	
o	-j|--syslog	Log interactive statements to syslog	
o	-t|--table	Display output in tabular format	
o	--tee	Append a copy of output to named file	v
o	--tls-ciphersuites	Permissible TLSv1.3 ciphersuites for encrypted connections	v
o	--tls-version	Permissible TLS protocols for encrypted connections	v
o	-n|--unbuffered	Flush the buffer after each query	
o	-u|--user	MySQL user name to use when connecting to server	v
o	-v|--verbose	Verbose mode	
o	-V|--version	Display version information and exit	
o	-E|--vertical	Print query output rows vertically (one line per column value)	
o	-w|--wait	If the connection cannot be established, wait and retry instead of aborting	
o	-X|--xml	Produce XML output	
o	--zstd-compression-level	Compression level for connections to server that use zstd compression	v
a	1	0
=		--character-sets-dir
t	folders
=		--compression-algorithms
v	zlib	
v	zstd	
v	uncompressed	
=		--defaults-extra-file
t	filepaths
=		--defaults-file
t	filepaths
=		--load-data-local-dir
t	folders
=		--local-infile
v	0	Disable
v	1	Enable
=		--plugin-dir
t	folders
=		--protocol
v	TCP	
v	SOCKET	
v	PIPE	
v	MEMORY	
=		--server-public-key-path
t	filepaths
=		--ssl-ca
t	filepaths
=		--ssl-capath
t	folders
=		--ssl-cert
t	filepaths
=		--ssl-crl
t	filepaths
=		--ssl-crlpath
t	folders
=		--ssl-fips-mode
v	OFF	
v	ON	
v	STRICT	
=		--ssl-key
t	filepaths
=		--tee
t	filepaths
=		--tls-ciphersuites
t	filepaths
